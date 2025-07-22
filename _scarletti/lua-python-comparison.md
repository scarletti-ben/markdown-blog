# Lua vs Python Syntax Comparisons

1. For Loop

Python:
```python
for i in range(1, 6):
    print(i)
```
Lua:
```lua
for i = 1, 5 do
  print(i)
end
```
2. List Comprehension

Python:
```python
squares = [x * x for x in xs]
```
Lua:
```lua
squares = {}
for _, x in ipairs(xs) do
  table.insert(squares, x * x)
end
```
3. List Append

Python:
```python
mylist.append(7)
```
Lua:
```lua
table.insert(mylist, 7)
```
4. Enumerated Iteration

Python:
```python
for i, val in enumerate(mylist):
    print(i, val)
```
Lua:
```lua
for i, val in ipairs(mylist) do
  print(i, val)
end
```
5. Dictionary/Table Access & Mutation

Python:
```python
mydict = {}
mydict["a"] = 1
print(mydict["a"])
```
Lua:
```lua
mydict = {}
mydict["a"] = 1
print(mydict["a"])
```
OR dot syntax:

```lua
mydict = {}
mydict.a = 1
print(mydict.a)
```
6. Indexing Start

Python: Indexes start at 0  
Example: mylist[0] accesses first element

Lua: Indexes start at 1  
Example: mylist[1] accesses first element

7. Truthy/Falsy Values

Python:  
Falsy - False, None, 0, "", empty containers  
Truthy - everything else

Lua:  
Falsy - false, nil  
Truthy - everything else (including 0 and "")

8. Error Handling

Python:  
try/except blocks for catching exceptions

Lua:  
pcall(function) and xpcall(function, handler) for protected calls and error catching

9. Anonymous Functions

Python:  
lambda expressions and def functions

Lua:  
function expressions (anonymous functions)

Example Lua:

```lua
local f = function(x) return x * 2 end
print(f(3))
```
10. Async Support

Python:  
Native async/await keywords and asyncio library

Lua:  
No native async/await; uses coroutines for cooperative multitasking

11. Chaining

Python:  
Method chaining common in some libraries

Lua:  
No native chaining syntax but can simulate by returning self from methods

Example Lua:

```lua
local obj = {}
function obj:set(x) self.x = x; return self end
function obj:add(y) self.x = self.x + y; return self end

obj:set(5):add(3)
print(obj.x)
```
12. Block Delimiters

Python:  
Blocks defined by indentation

Lua:  
Blocks explicitly closed with `end`

Example:

```lua
if x > 0 then
  print("positive")
end
```
No equivalent of indentation-based blocks in Lua.

13. Functions and Classes

Python:  
def keyword, classes with class keyword

Lua:  
Functions as first-class values, classes simulated with tables and metatables

Example class in Lua:

```lua
local Player = {}
Player.__index = Player

function Player:new(name)
  local obj = setmetatable({}, Player)
  obj.name = name
  return obj
end

function Player:greet()
  print("Hello, " .. self.name)
end

local p = Player:new("Ben")
p:greet()
```
Missing Lua vs Python Notes

1. Coroutines (Lua async alternative)

Lua example:

```lua
function asyncTask()
  for i = 1, 3 do
    print("Step", i)
    coroutine.yield()
  end
end

co = coroutine.create(asyncTask)

coroutine.resume(co)
coroutine.resume(co)
coroutine.resume(co)
```
2. Error catching with pcall/xpcall

```lua
local success, err = pcall(function()
  error("Something went wrong")
end)

if not success then
  print("Caught error:", err)
end
```
3. Truthy/Falsy in Lua

Only `false` and `nil` are falsey; everything else (0, "", tables) is truthy.

Example:

```lua
if 0 then print("0 is truthy") end
if "" then print("Empty string is truthy") end
if false then print("Won't print") end
```
4. `then` vs `do`

- `then` used after `if` and `elseif` conditions:

```lua
if x > 0 then
  print("positive")
end
```
- `do` used for loops and explicit blocks:

```lua
for i = 1, 5 do
  print(i)
end

do
  local a = 5
end
```
5. Metatables for OOP

Example class uses metatable for inheritance and method lookup.

```lua
local Class = {}
Class.__index = Class

function Class:new()
  local obj = setmetatable({}, Class)
  return obj
end
```
6. Indexing starts at 1

Arrays and strings start at 1, unlike Python's 0.

7. Simple GUI with SUIT

```lua
local suit = require "suit"

function love.update(dt)
  if suit.Button("Click me", 100, 100, 120, 30).hit then
    print("Clicked!")
  end
end

function love.draw()
  suit.draw()
end
```
8. Anonymous functions, no arrow syntax

Lua supports anonymous functions but no arrow shorthand.

```lua
local f = function(x) return x * 2 end
print(f(5))
```
9. Method chaining by returning self

```lua
local obj = {}
function obj:set(x) self.x = x; return self end
function obj:add(y) self.x = self.x + y; return self end

obj:set(10):add(5)
print(obj.x) -- 15
```
10. No try/catch, use pcall

Lua does not have try/catch; use `pcall` for error catching.

11. No built-in type hints, optional annotations

Use EmmyLua or similar for JSDoc-like type annotations in comments.

12. Blocks closed by `end`

Lua uses explicit `end` for all blocks instead of indentation.

13. Minimal syntax philosophy

Lua opts for simple, consistent syntax avoiding indentation sensitivity.