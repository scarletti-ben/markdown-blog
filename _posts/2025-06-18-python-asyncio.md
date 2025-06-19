---
title: "Python Asyncio Notes"
date: "2025-06-18"
date-modified: "2025-06-18"
description: "Python Asyncio Notes from a while ago"
categories: [
  coding
]
tags: [
  coding, dev, python, asyncio, async, asynchronous
]
author: "Ben Scarletti"
---

-------------------------------------------------------------------------------------------------------------------------------

~ Random Stack Exchange Comments:

`asyncio.sleep()` always pauses the current task and switches execution to another one.
`asyncio.sleep(0)` has no special meaning (but it has internal optimization for the case).

"yield control to the event loop" without incurring additional overhead of sleeping

 ``sleep()`` always suspends the current task, allowing other tasks
   to run.

Basically the same as `time.sleep(0)` for multithreaded program.

I doubt if we need to blow the documentation with all possible related details.

~ ==========================================================================================================================================
~ Section 1: https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-1.html
~ ==========================================================================================================================================

--- Fundamental Point:
	- Async works best for I/O bound code where long pauses are expected to wait for something else (another PC, a web request)

--- Core Terms
	- Blocking means "take a long time before it returns", a function or async coroutine may be "blocking" if it is slow and remains the active executor during this time

~ Part A - General Overview of Asyncio and I/O Bound Processes

Python has a global interpreter lock (GIL) that allows only one thread to control the python interpreter at one time
Asyncio is not multithreaded, it does not allow two python instructions to be instructed at the same time
It is essentially interwoven, you are doing things one at a time but out of order

CPU bound processes
	- Consist of a series of instructions that need to be executed one after another until the result has been computed

I/O bound processes
	- Spend a lot of time sending and receiving data from external devices or processes
	- The usually start an operation and wait for it to complete before carrying on, in the meantime they aren't doing anything
	- This means that I/O bound code leaves the CPU doing nothing at all as it waits for something being done elsewhere

Asyncio is for this I/O bound issue and is designed to allow you to structure your code so that when one piece of linear single-threaded code (called a coroutine) is doing nothing and waiting for something to happen another can take over and use the CPU

Asyncio is not about using multiple cores, its about using a single core more efficiently

~ Part B - Subroutines vs. Coroutines

A class object in Python may call a method, this denotes a bit of code that can be called by other code
Similarly a function is a bit of code that can be called by other code

Subroutines
	- A subroutine is the normal process of Python, when you call a function execution moves from the start of that function until it reaches the return statement or the end (implicit return None)
	- Future calles to the same function are independent calls that start again at the beginning of the function
	- Created variables exist in the local scope of each independent function call
	
Coroutines - An alternative model of code execution
	- The function / method can move execution back to the caller, it does this by yielding control (yield keyword)
	- When the coroutine yields execution moves back to the point immediately after it was called
	- IMPORTANTLY future calls to the coroutine do not start at the beginning, instead they continue from where the execution left off
	- This is a way of bouncing control back and forth between the calling code and the coroutine code

In essence a function in normal code is a subroutine of the main code, and an asynchronous function is a coroutine of the main code

Generators have always been possible in python as a way of achieving this behaviour but Asyncio makes this more natural and adds functionality
Execution in Asyncio moves around betweeen coroutines when the current one gets blocked

~ Part C - Stack Machines

Most operating systems and programming languages makes use of an abstraction known as a "stack machine"
	- This is one of the mechanisms that allows us to call one piece of code from another
	- There is usually a single stack per thread and in single threaded coding there is just one stack
A function call adds a new "frame" to the top of ths stack and a return pointer to the top of the stack which tells the interpreter where to return to executing when the function ends

In Asyncio this all works a little differently, thee is no longer one stack per thread, each thread has an object called an Event Loop
Event loops contain a list of objects called Tasks, each Task maintains a single stack and execution pointer
The event loop can only have one task actually executing and all other tasks in the loop are paused
	- The active task works like a synchronous function until it would need to wait for something to continue
	- Instead of waiting it yields control and asks the event loop to pause its task and wake it later when what it is waiting for has happened
	- The event loop then selects one of its other sleeping tasks to wake up as the new executing task
	- The event loop will wait if no task is ready to be awakened
	- The CPU's time is therefore shared between all the tasks

* Important Note:
	- An event loop cannot forcibly interrupt a coroutine that is currently executing. A coroutine that is executing will continue executing until it yields control. The event loop serves to select which coroutine to schedule next, and keeps track of which coroutines are blocked and unable to execute until some I/O has completed, but it only does these things when no coroutine is currently executing.

This execution pattern is called "coroutine calling" and is exactly what asyncio brings to Python programming

~ ==========================================================================================================================================
~ Section 2: https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-2
~ ==========================================================================================================================================

~ Part A - Keywords and Notes

The most basic tool is the new keyword async def, which is used to declare an asynchronous coroutine function in the same way that def is used to define a normal synchronous function

async def example_coroutine_function(a, b):
    # Asynchronous code goes here
    ...

def example_function(a, b):
    # Synchronous code goes here
    ...

There are several new keywords which can only be used inside asynchronous code
	~ await, async with and async for

Unlike a synchronous function, calling test = example_coroutine_function(1, 2, 3) does not call the function, it returns an object of the Coroutine class

The most common way to call a coroutine is with the await keyword

* Important: It’s pretty common for people to be sloppy in their terminology and use the word “coroutine” to refer to any of three things:
	- The code block of asynchronous code inside an async def statement
	- The callable object that the async def statement creates
	- The object of class Coroutine that is returned by the callable object when it is called
	~ Best practice is to term an object of the Coroutine class a coroutine object, and term the async def callable a coroutine function
		~ The code block is simply "the code block inside an async def statement

~ Part B - Await Keyword and Awaitables

The await keyword is, in many ways, the very core of asynchronous code
It can only be used from within aynchronous code blocks eg. that of an async def statement defining a coroutine function

Usage:
	- await takes a single parameter and returns a value
		- r = await a             will perform the away action on the object a and return a value assigned to r

Coroutine objects are awaitable and can be used in an await statement
	* However asynchronous code is run in the context of a Task which is an object maintained by The Event Loop (TEL) where each Task has its own call stack

Three types of objects are awaitable:
	- Coroutine objects
	- Any object of the class asyncio.Future, which, when awaited causes the current Task to be paused until a specific condition occurs
	- Any object that implements the magic method __await__, what happens is defined by that method

* Important:
	- The currently executing Task cannot be paused by any means other than awaiting an asyncio.Future
	- Any statement that is not an await statement also cannot cause your current Task to be paused
	- Data races which occur in multithreaded code are possible where different "threads" of execution alter the same value

-- Code Examples

For the purposes of data shared between Tasks on the same event loop all synchronous code can be considered “atomic”. To illustrate what this means consider the following code:

import asyncio

async def get_some_values_from_io():
    # Some IO code which returns a list of values
    ...

vals = []

async def fetcher():
    while True:
        io_vals = await get_some_values_from_io()

        for val in io_vals:
            vals.append(io_vals)

async def monitor():
    while True:
        print (len(vals))

        await asyncio.sleep(1)

async def main():
    t1 = asyncio.create_task(fetcher())
    t2 = asyncio.create_task(monitor())
    await asyncio.gather(t1, t2)

asyncio.run(main())

Though both fetcher and monitor access the global variable vals they do so in two tasks that are running in the same event loop. For this reason it is not possible for the print statement in monitor to run unless fetcher is currently asleep waiting for io.

This means that it is not possible for the length of vals to be printed whilst the for loop is only part-way through running. So if the get_some_values_from_io always returns 10 values at a time (for example) then the printed length of vals will always be a multiple of ten. It is simply not possible for the print statement to execute at a time when vals has a non-multiple of ten length.

~ Part C - Futures

A Future object is a type of awaitable. Unlike a coroutine object, when a future is awaited it does not cause a block of code to be executed. Instead a future object can be thought of as representing some process that is ongoing elsewhere and which may or may not yet be finished.

When you await a future the following happens:

If the process the future represents has finished and returned a value then the await statement immediately returns that value.
If the process the future represents has finished and raised an exception then the await statement immediately raises that exception.
If the process the future represents has not yet finished then the current Task is paused until the process has finished. Once it is finished it behaves as described in the first two bullet points here.

All Future objects "f" have the following synchronous interface in addition to being awaitable:

f.done() returns True if the process the future represents has finished.
f.exception() raises an asyncio.InvalidStateError exception if the process has not yet finished. If the process has finished it returns the exception it raised, or None if it terminated without raising.
f.result() raises an asyncio.InvalidStateError exception if the process has not yet finished. If the process has finished it raises the exception it raised, or returns the value it returned if it finished without raising.
It’s important to note that there is no way for a future that is done to ever change back into one that is not yet done. A future becoming done is a one-time occurrence.

* Important
	- The distinction between a Coroutine and a Future is important. A Coroutine’s code will not be executed until it is awaited. A future represents something that is executing anyway, and simply allows your code to wait for it to finish, check if it has finished, and fetch the result if it has.

~ Part D - Tasks

- Each event loop contains a number of tasks and every coroutine that is executing does so inside a task
- Tasks can be created in the synchronous code with asyncio.create_task(coroutine_object) where a coroutine object is a called() asynchronous function async def 

async def example_coroutine_function():
    ...

t = asyncio.create_task(example_coroutine_function())

In older python 3.6
t = asyncio.get_event_loop().create_task(example_coroutine_function())

- The method create_task takes a coroutine object as a parameter and returns a Task object, which inherits from asyncio.Future. The call creates the task inside the event loop for the current thread, and starts the task executing at the beginning of the coroutine’s code-block. The returned future will be marked as done() only when the task has finished execution. As you might expect the return value of the coroutine’s code block is the result() which will be stored in the future object when it is finished (and if it raises an exception then the exception will be caught and stored in the future)

- Creating a task to wrap a coroutine is a synchronous call, so it can be done anywhere, including inside synchronous or asynchronous code. If you do it in asynchronous code then the event loop is already running (since it is currently executing your asynchronous code), and when it next gets the opportunity (ie. next time your current task pauses) it might make the new task active

- When you do it in synchronous code, however, chances are that the event loop is not yet running. Manualy manipulating event loops is discouranged by the python documentation. Unless you are developing libraries extending asyncio functionality, you should probably avoid trying to create a task from synchronous code

- You can’t run async code unless you have an event loop to run it in so awaiting asynchronous coroutines in a program that doesn’t have a running event loop means you need to start an event loop. 

* If you do need to call a single piece of async code in an otherwise synchronous script, you can use asyncio.run()

~ Part E - Running Async Programs