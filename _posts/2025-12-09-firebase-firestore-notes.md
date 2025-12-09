# Firestore Notes
This is two `README` files connected together, and slightly abridged. The first is from this [respository](https://github.com/scarletti-ben/firebase-wrapper). The second makes references the first, and may or may not be part of a public repository in the future. It would be nice to make a slightly more coherent document one day but until then this is probably a half decent way to remind my brain of things

# Overview
The primary aim of this repository is to create my own "wrapper" for `Firebase` / `Cloud Firestore` API functionality. It is tailored for use with my `Firebase` project named `mainframe-storage` which is set up for `Firestore` database usage and `Google oAuth 2.0` authentication. I set up the `Firebase` project as a learning process but also intend to use it across many applications as the central database for user data.

There will also be a `GitHub Pages` static site within this repository for testing the wrapper, you can access the site [here](https://scarletti-ben.github.io/firebase-wrapper/)

# Security
Previous versions of this project exposed a public API key for `Firebase` and, depsite the list of protections below it still feels wrong to expose any API key to the client, that being said I haven't deleted the repository so the raw API key is still very much accessible in previous versions
- The official [quote](https://firebase.google.com/support/guides/security-checklist#:~:text=To%20store%20Firebase%20API%20keys,automatically%20acquire%20them%20during%20initialization) from `Firebase` on the matter suggests that `Firebase` API keys are not secret and can be safely embedded in code
- There are server-side authentication checks via `Google oAuth 2.0`
- There are database access rules set via `Firestore Rules`
- This `Firebase` project is connected to a free `Spark` tier account where it is impossible to incur costs

As such I decided it would be "fun" to encrypt `firebaseConfig` using `PBKDF2` / `AES-256` and store the object in the `objects.json` file, to be decrypted as needed. In this way the decrypted version can be stored client-side in `IndexedDB`. This is by no means a good method if the API key in question was truly a secret, but adds a layer of obfuscation through encryption. If `GitHub` secret scanner flags `objects.json` you can add a `secret_scanning.yaml` file to the repository as below
```yaml
paths-ignore:
  - "objects.json"
```

# Aims
The aims for the project are as follows
- The `firebaseConfig` object should be decrypted via a "pre-authorisation" phase, using `PBKDF2` and requiring the `password` and `salt` used to encrypt the original object
  - The "pre-authorisation" phase should only be required on new devices, with `firebaseConfig` then stored to `IndexedDB` indefinitely
- A user should be authenticated via `Sign in with Google` using `Google oAuth 2.0`
- An authenticated user should be able to read and write their personal data
- An authenticated user should be able to read and write personal application data for the specific app they are currently using
- The syntax of `firebase-wrapper.js` should be clear and concise and give easier access to common `Firebase` tools

# Usage

## Using `firebase-wrapper.js`
You can use the file locally or via `CDN`, in both cases you will want to define an app name. The reason for this is that `mainframe-storage` has its `Firestore` set up such that users have data for each app they use stored under `users/{userName}/apps/{appName}`, and the app name we define controls where data is stored and read from. Let us assume that we have `const appName = 'test-app'` for the snippets below

Let us also assume that we have some test document data as the constant `documentData`
```javascript
const documentData = {
    uuid: crypto.randomUUID(),
    title: 'title',
    content: 'content',
    tags: ['tag1', 'tag2'],
    created: Date.now(),
    modified: Date.now()
};
```

### Local Usage
Inside your main `JavaScript` file, `main.js` for instance, you can import from `firebase-wrapper.js` in one of two ways
1) Import individual objects via `import { initialisation, authentication, firestore } from "./firebase-wrapper.js";`
    - Initialisation would then be done via `initialisation.init(appName)`
2) Import as a namespace via `import *  as firebase from "./firebase-wrapper.js"`
    - Initialisation would then be done via `firebase.initialisation.init(appName)`

In the snippet below we use the first method, the snippet is not an exhaustive list of the features of `firebase-wrapper` but shows the basics
```javascript
// Import objects from firebase-wrapper.js
import { initialisation, authentication, firestore } from "./firebase-wrapper.js";

// Initialise Firebase with app name
await initialisation.init(appName);

// Add login functionality to an HTML button
loginButtonElement.addEventListener('click', async () => {
    let credentials = await authentication.login();
    console.log(credentials);
})

// Add logout functionality to an HTML button
logoutButtonElement.addEventListener('click', () => {
    authentication.logout();
})

// Add example callback that listens for successful user login
authentication.onLogin((user) => {
    console.log('User logged out');
})

// Add example callback that listens for successful user logout
authentication.onLogout(() => {
    console.log('User logged out');
})

// Write document at users/{userName}/apps/test-app/test-collection/{documentUUID}
firestore.writeDocument('test-collection', documentData.uuid, documentData)
```

### CDN Usage
Whilst you can add the `CDN` link directly to the `<head>` of your `HTML` file, and automatically gain access to the exported objects, `initialisation`, `authentication`, and `firestore`. It is probably best practice to import within your `JavaScript` file, as seen below

```javascript
// Import individual objects
import { initialisation, authentication, firestore }  from 'https://scarletti-ben.github.io/firebase-wrapper/firebase-wrapper.js';

// Alternatively: Import as namespace
import *  as firebase from 'https://scarletti-ben.github.io/firebase-wrapper/firebase-wrapper.js'
```

Once you have imported `firebase-wrapper.js` you can use it much the same as you would in a local environment, albeit with no code completion from your `IDE`

#### CDN Links
If you are accessing the file via a GitHub Pages link you can expect to be using the latest version of the file as they exist on the main branch of the repository
- https://scarletti-ben.github.io/firebase-wrapper/firebase-wrapper.js

If you are accessing the file via a `jsDelivr` link you can specify an exact release tag, here we use `v1.0.0`, and ensure that the files you are accessing do not change, ensuring consistent functionality
- https://cdn.jsdelivr.net/gh/scarletti-ben/firebase-wrapper@v1.0.0/firebase-wrapper.js

> [!NOTE]
> Do not use the direct link to the file on `GitHub`, only use the `GitHub Pages` served version of the file, or a link from `jsDelivr`

### Exported Objects / Object Methods
Below is a rough list what is exposed when importing `firebase-wrapper.js` correctly, more features may be added in future, and this list may not be entirely up to date
- `initialisation`
  - `initialisation.init(appName)`
- `authentication`
  - `authentication.login()`
  - `authentication.logout()`
  - `authentication.onLogin(callback)`
  - `authentication.onLogout(callback)`
  - `authentication.isAuthenticated()`
- `firestore`
  - `firestore.writeDocument(collectionName, documentName, documentData, replaceBoolean)`
  - `firestore.updateDocument(collectionName, documentName, documentData)`
  - `firestore.readDocument(collectionName, documentName)`
  - `firestore.deleteDocument(collectionName, documentName)`
  - `firestore.readCollection(collectionName)`

# Miscellaneous

## Project Notes
- `firebase-wrapper.js` does not make authentication checks for you eg. for  `firestore.writeDocument`
  - It is safe, and `Firestore` rules prevent unauthenticated writes, but it will throw errors and it is up to the developer to ensure user is logged in and authenticated

## Setting Up Firebase / Firestore
You can create a new `Firebase` project, giving you access to the `Firebase Console` for your project. In the `Firebase Console` you can add apps to your project, the app itself doesn't necessarily need to exist but when you add an app to a `Firebase` project you generate a new `appId` that can be used alongside the public API key to interact with the components of your `Firebase` project. The `appId` itself isn't noticed by `Firestore` which is why we use a manually entered `appName` to separate collections under each user.

You need to then enable `Authentication` [here](https://console.firebase.google.com/u/3/project/mainframe-storage/authentication), and choose `Google` as a sign-in provider, ignore the warnings for `SHA-1`

You then enable / create a `Firestore` database and update the `Firestore` rules for read / write access

Add `https://scarletti-ben.github.io/` to "authorised domains" if you want to access via a `GitHub Pages` static site

You can use `Firebase` for hosting an app / site as well but this shows that it's not entirely necessary, you can host the site anywhere and you can still interface with a `Firestore` database, with authentication handled server-side by `Google`

Linking an application to `Firebase` gives you the code similar to the snippet below, which we have an encrypted version of within the `objects.json` file. It is important to note that the `apiKey` is is not meant to be a secret, it is entirely public as it identifies your `Firebase` project. Safety of data is primarily handled by `Google` authentication and manually defined `Firestore` rules.
```javascript
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "abc123",
    authDomain: "mainframe-storage.firebaseapp.com",
    projectId: "mainframe-storage",
    storageBucket: "mainframe-storage.firebasestorage.app",
    messagingSenderId: "1234",
    appId: "1:1234:web:xyz789",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
```

### Testing Firebase Locally
By default `Firebase` only allows connections from whitelisted sites, this means that you may need to add a local URL to the whitelisted sites if it doesn't start with `localhost`, adding `http://127.0.0.1` to the whitelist will likely help

## Cloud Firestore Database
A simplified version of the database structure can be seen below, with this structure a user can have data across multiple apps all stored within the same `Firestore` database, and accessed via the same credentials
```text
users/
  └─ {userId}/
    └─ apps/
      └─ {appName}/
        └─ .../
          └─ .../
```

A user with `ID` of `UID9876` using an app called `test-app`, storing a document with an `ID` of `note-1234` to that app's `notes` collection would create the path structure seen below
```text
users/
  └─ UID9876/
    └─ apps/
      └─ test-app/
        └─ notes/
          └─ note-1234/
```

### Firestore Rules
The `Firestore Rules` as they stand are below, you can read them [here](https://console.firebase.google.com/u/3/project/mainframe-storage/firestore/databases/-default-/rules)
```text
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
  
    // allow user to read/write any document or subcollection under their apps
    match /users/{userId}/apps/{appName}/{path=**} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
    
  }
}
```

# Learnings

## User Authentication / Tokens Between Sessions
An ID token is often short-lived, or "ephemeral", lasting say an hour, and to get an ID token you need a valid refresh token. Some sites rotate the refresh token when the ID token is returned, meaning the old refresh token is no longer valid. The ID token is used in request headers to show that the user is authenticated. An ID token should not be used to get refresh tokens. Refresh tokens are usually generated during initial authentication.

To ensure you receive a refresh token, your request for authentication must include the scope. This scope tells `Google` to provide a refresh token along with the ID token during initial authentication.

The refresh token is managed automatically for you when using `Firebase` via `getAuth`, it will check if the current ID token is valid, then attempt to refresh it if not using the refresh token, rotating the ID token, and likely the refresh token itself in the process. In other apps where `Google OAuth 2.0` is used you may have to manage this manually.

# Project Information

## Developement Environment Information
- Tested using `Google Chrome Version 135.0.7049.96 (Official Build) (64-bit)`
- Not tested on mobile devices or other desktop browsers

## Repository Metadata
```yaml
---
metadata:
  author: "Ben Scarletti"
  date-created: "2025-04-24"
  date-modified: "2025-05-29"
  description: "Firebase wrapper to be used as is, or repurposed for my future projects"
  tags: [
    "dev", "webdev", "programming", "coding", "javascript", "html", "cdn", "ecma6", "export", "import", "firebase", "firestore", "firestore rules", "cloud firestore", "firebase cli", "database", "authentication", "google oauth 2.0", "api", "api keys", "encryption", "pbkdf2", "https", "tokens", "refresh tokens", "id tokens", "sign in with google", "encryption", "decryption", "pbkdf2", "obfuscation", "aes", "aes-256", "indexeddb"
  ]
---
```

# PART 2

# Firebase Refresher

## Overview
Often I make test apps / demos and want a quick way to sync data between different devices. One of the easiest ways to do this is via [`Firebase`](https://firebase.google.com/), which is a service offered by `Google`. It allows you to use the "Sign in with Google" system for authentication via `Google OAuth 2.0`. The most common use of this system, once you have signed in, is to read and write data to a database. Often the database you write to is only accessible to your account. In this way you can sync data and access on different devices as long as each device is signed into the same `Google` account

## Accessing Firebase Projects
The `Firebase` [console](https://console.firebase.google.com/) shows you all your `Firebase` projects. When you are on the console page, make sure that the correct `Google` account is signed in

## Project Apps
Each `Firebase` project can hold multiple "apps". It's easy to create a new app from the `Firebase` console and each one will be given a different `appId`. From within an app on the console you can access the `firebaseConfig` object. You can see the `firebaseConfig` object and sample code given for two apps that are children of my project titled "mainframe-storage". The application identifiers are `appId: "1:432631138940:web:916056dd852890f69317f9"` and `appId: "1:432631138940:web:ae5059b05db6b3e09317f9"` respectively

```javascript
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAx5VIksX5JeW2hk5FDf_8rhyBa6CibH84",
  authDomain: "mainframe-storage.firebaseapp.com",
  projectId: "mainframe-storage",
  storageBucket: "mainframe-storage.firebasestorage.app",
  messagingSenderId: "432631138940",
  appId: "1:432631138940:web:916056dd852890f69317f9",
  measurementId: "G-18HKHHX6GP"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
```

```javascript

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAx5VIksX5JeW2hk5FDf_8rhyBa6CibH84",
  authDomain: "mainframe-storage.firebaseapp.com",
  projectId: "mainframe-storage",
  storageBucket: "mainframe-storage.firebasestorage.app",
  messagingSenderId: "432631138940",
  appId: "1:432631138940:web:ae5059b05db6b3e09317f9",
  measurementId: "G-LXYPVDN1K4"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
```

> [!NOTE]
> - An important note to make is that a `Firestore` project may have multiple apps but `const app = initializeApp(firebaseConfig); const firestore = getFirestore(app)` for two different `firebaseConfig` objects where both are apps from the same project will both return `Firestore` instances that point to the same backend database
> - The main point of this is that you will still need to manually decide where data is stored within the database, it is not handled by the application name or `appId`. In a sense the `appName` argument passed in `const app = initializeApp(firebaseConfig, appName);` is *mostly* ceremonial

## Adding Firebase to JavaScript via CDN
You can import `Firebase` via `CDN` either in the `HTML` or the `JavaScript`. Generally I prefer to use the `import` keyword in the `JavaScript` (`ECMAScript 2015` / `ES6`) so that's what this refresher will focus on

The `CDN` imports that I get the most mileage out of are below, you may not need all of them for every project, and may need ones not listed so this is not an exhaustive list. You will notice the `12.2.1` in each `URL`, this is the version number and it's best to check what the current version is before just blindly copy and pasting the code below!

```javascript
import {
    initializeApp
} from "https://www.gstatic.com/firebasejs/12.2.1/firebase-app.js";

import {
    getAnalytics
} from "https://www.gstatic.com/firebasejs/12.2.1/firebase-analytics.js";

import {
    getAuth,
    onAuthStateChanged,
    signInAnonymously,
    updateProfile
} from "https://www.gstatic.com/firebasejs/12.2.1/firebase-auth.js";

import {
    getFirestore, 
    doc, 
    setDoc, 
    getDoc, 
    getDocs, 
    updateDoc, 
    deleteDoc, 
    collection
} from "https://www.gstatic.com/firebasejs/12.2.1/firebase-firestore.js";

import {
    getDatabase,
    ref,
    get,
    set,
    remove,
    push,
    onValue,
    onChildAdded
} from 'https://www.gstatic.com/firebasejs/12.2.1/firebase-database.js';
```

In addition to the above you will need to add the `firebaseConfig` object which is mentioned [here](#firebase-project-apps). The `firebaseConfig` object is information used to connect to *your* `Firebase` project and app specifically. It's meant to be public as authentication is handled via `Google` authentication and manually set `Firebase Security Rules` rather than just keeping the API key secret

## Writing Data to Firestore Database
As mentioned in a note above, the application name and `appId` don't actually do anything to control where files are stored for your project. All apps have access to the same `Firestore` and, as such, you need to be careful about where files are being stored

For a previous project, documents would be written to `users/{userId}/apps/{appName}/{collectionName}/{documentName}` and the function signature would be something like `async writeDocument(collectionName, documentName, documentData)`

Assuming that `writeDocument` is a method of an object with a `.auth` attribute you'd find some variant of the code below useful when writing data as a document in the database

```javascript
const userId = this.auth.currentUser.uid;
const docPath = `users/${userId}/apps/${this.appName}/${collectionName}/${documentName}`;
const docRef = doc(this.db, docPath);
await setDoc(docRef, documentData);
```

## Firestore Security Rules
As an extension of the section [here](#writing-data-to-firestore-database), you need to make sure that access to data is locked down via `Firestore Security Rules`. You need to ensure users can't access each others' data

An example of the security rules for a previous project can be found below, they are not to be used verbatim and may even be dangerous - but it shows roughly the syntax used. The project in question has users as the top level, but you could have apps at the top level and then sort by user per app if you wish

```text
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
  
    // allow user to read/write any document or subcollection under their apps
    match /users/{userId}/apps/{appName}/{path=**} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
    
  }
}
```

The general structure of the database was something akin to the diagram below
```text
users/
├── 9iLmTQskE6QZcHwlwG5PaX831jW2/
│   └── apps/
│       ├── firebase-wrapper/
│       └── test-app/
└── Whsalu2nU8TnOVwv0xZiCvzFgR33/
    └── apps/
        └── test-app/
```

[!NOTE]
> - Just because you have robust `Firestore Security Rules` does not mean that the data is fully protected. The `Firestore` itself is stored in plain text, and the owner of the project is able to read data for all users exactly as it was sent to the database. In some cases you may wish to implement encryption and decryption on the client side, or set up a real server that handles this

## Firestore vs Realtime Database
Both services are offered by `Firebase`, they're both variants of a database system. To use `Firestore` you'd use `import ... from "https://www.gstatic.com/firebasejs/12.2.1/firebase-firestore.js"`, and for `Realtime Database` you'd use `import ... from "https://www.gstatic.com/firebasejs/12.2.1/firebase-database.js"`. There are subtle differences to how you might read or write to these that I won't explore in depth. In simple terms `Firestore` is a more structured "filesystem" style database with a complex query system that scales well and encourages nested data. `Realtime Database` is more of a `JSON` tree style database with live updating, best used for immediate communication between devices as it pushes changes immediately - not intended to scale as much, and encourages flat or simple data.

## Miscellaneous
- The notes in this document are for "vanilla" `JavaScript` / `HTML` sites, without build-tools. The general concepts can still be applied to other site-building methods
    - This means that imports are done via `CDN` and there are no type hints, which can be a bit annoying. Though it is not impossible to have a bit of a hybrid with your own manually written `TypeScript` files
- I have a few projects that have made use of `Firebase` but one that has a bit of documentation is [here](https://github.com/scarletti-ben/firebase-wrapper). I have not checked it for any errors but the site I built around it functions as intended
- There is a design philosophy decision when picking between `users/` as the top level of the database and `apps/`. It can affect how easy some queries are to make, and make it easier or harder for users to access their data across different apps
    - You can also implement a hybrid approach with `users/` and `apps/` with some data existing in both
- The way the `Firestore` database works means it goes collection/document/collection/document. Collections have documents, and documents have collections as well as fields. A collection can be thought of as a folder, a container that holds documents, it cannot hold data directly. The collections that are children of documents are "subcollections" of sorts