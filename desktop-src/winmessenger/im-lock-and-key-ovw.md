---
title: Messenger Lock and Key API
description: This topic explains how to unlock the Messenger service APIs using Messenger Lock and Key.
ms.assetid: f094589c-53bb-466e-9758-ea3df5c84e74
keywords:
- Windows Messenger,Lock and Key
- Windows Messenger,unlocking Messenger service
- unlocking Messenger service
- Messenger service,unlocking
- Messenger service,Lock and Key
- Messenger Lock and Key,unlocking Messenger service
- Lock and Key,unlocking Messenger service
- Messenger Lock and Key,authentication
- Lock and Key,authentication
- Messenger Lock and Key,encryption
- Lock and Key,encryption
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Messenger Lock and Key API

The Messenger service  APIs can be used to access a Messenger service programmatically. These Messenger service interfaces and objects are locked by a mechanism called "Messenger Lock and Key" and must be unlocked before they can be used to connect to the Microsoft .NET Messenger Service. The lock and key restriction does not apply when connecting to corporate instant messaging servers, such as Microsoft Exchange Instant Messaging.

This topic explains how to unlock the Messenger service  APIs using Messenger Lock and Key. Programming with the Messenger service  APIs is discussed separately in [Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md) and [Windows Messenger](im-messenger-entry.md).

This topic contains the following sections.

-   [Introduction](#introduction)
-   [Terminology](#terminology)
-   [Prerequisites](#prerequisites)
-   [Interfaces and Objects](#interfaces-and-objects)
    -   [Objects](#objects)
    -   [Interfaces](#interfaces-and-objects)
-   [Authentication Process](#interfaces-and-objects)
    -   [Request](#request)
    -   [Challenge-Response](#challenge-response)
    -   [Result](#result)
-   [Security and Encryption](#security-and-encryption)
    -   [External References](#external-references)
    -   [ID/Key Pairs](#idkey-pairs)
    -   [Hiding ID/Key Pairs](#hiding-idkey-pairs)
-   [Related topics](#related-topics)

## Introduction

The Lock and Key mechanism applies to more than one of the objects exposed by the Messenger client and must be used to unlock each Messenger service object used by an application. For more information, see [Interfaces and Objects](#interfaces-and-objects).

The Messenger Lock and Key mechanism is an authentication process initiated by a Messenger client application. Each step of the process is described in detail in the [Authentication Process](#interfaces-and-objects) section.

The section on [Security and Encryption](#security-and-encryption) describes general precautions that can be taken to prevent Messenger client applications from exposing authentication information.

> [!Note]  
> To unlock and use the Messenger service  APIs, you must use a valid ID/key pair. For more information, see [Developing and Testing Applications with the Messenger Service APIs](im-app-devtest.md).

 

> \[!Important\]  
> ID/key pairs are no longer being issued.

 

## Terminology

The following terms have a specific meaning within the context of the Messenger APIs.



|                                        |                                                                                                                                                                                                                                                  |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Messenger client                       | Application that uses the APIs exposed by Windows Messenger to provide client-side functionality for use with Messenger service s.                                                                                                               |
| Messenger service                      | Service that a Messenger client application uses. Messenger client applications can use Microsoft .NET Messenger Service.                                                                                                                        |
| Messenger Lock and Key                 | A friendly name for the mechanism that is used to unlock Messenger service  APIs programmatically.                                                                                                                                               |
| Messenger Session Invite               | A friendly name for a set of Messenger service  APIs that are locked with the Lock and Key mechanism, For more information, see [Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md).                                |
| ID                                     | An alphanumeric string value that identifies an application used to unlock the Messenger service  APIs.                                                                                                                                          |
| Key                                    | An alphanumeric string value that identifies an application used to access the Messenger service  APIs.                                                                                                                                          |
| RSA-MD5 Message Digest Algorithm (MD5) | MD5 is used to hash data that is exchanged between your application and the Microsoft .NET Messenger Service during a challenge-response transaction.                                                                                            |
| Request                                | The first step in the Lock and Key authentication process. An application must issue a request through the Messenger client API in order to receive a challenge to which it then can reply with a response.                                      |
| Challenge                              | A response from a Messenger service to an application's request. A challenge is issued in the form of a Unicode string. A challenge can be issued to a Messenger client at any time, even without a request from a Messenger client application. |
| Response                               | A response from a Messenger client application to a challenge it has received from a Messenger service .                                                                                                                                         |
| Result                                 | The result of a Lock and Key authentication transaction between a Messenger client application and a Messenger service . The result can either be successful or unsuccessful.                                                                    |
| Server Cloud                           | A computer network with a topology that is configured to host applications and services.                                                                                                                                                         |



 

 

> [!Note]  
> Microsoft maintains a list of all valid ID/Key pairs that have been assigned for use by applications. For more information, see [Developing and Testing Applications with the Messenger Service APIs](im-app-devtest.md).

 

## Prerequisites

This section illustrates basic programming techniques that you can use to unlock the Messenger service  APIs. Therefore, the reader should be familiar with using and referencing APIs that are exposed by Component Object Model (COM) objects.

Some familiarity with hashing and authentication techniques will be beneficial to the reader, because the Messenger Lock and Key mechanism makes use of the MD5 hash algorithm, which helps provide an additional degree of security to the authentication process. Before implementing an application that uses the Messenger service  APIs, obtain a valid ID/Key pair from Microsoft. This ID/Key pair must be used to authenticate an application and unlock the Messenger service  APIs.

## Interfaces and Objects

The Messenger service  APIs provide programmable objects and COM interfaces that you can use in a Messenger client application. Each is discussed in this section.

### Objects

The Messenger service  API exposes two programmable objects that implement the Messenger Lock and Key mechanism. The following table links to the reference pages for the Microsoft Visual C++ objects.



| C++ Object References                                      | Description              |
|------------------------------------------------------------|--------------------------|
| [**MsgrSessionManager**](im-msgrsessionmanager-object.md) | Messenger Session Object |
| [**MessengerPriv**](im-messengerpriv-object.md)           | Messenger Private Object |



 

If either a [**MsgrSessionManager**](im-msgrsessionmanager-object.md) or [**MessengerPriv**](im-messengerpriv-object.md) object is used by an application, each object must first be unlocked before it can be used. If more than one object is instantiated by an application, then each object must be unlocked separately using the Messenger Lock and Key mechanism.

### Interfaces

The following table lists the interfaces used with Messenger Lock and Key.



| Interface                                             | Description                                                                                                                                                                      |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IMsgrLock**](im-imsgrlock.md)                     | Implements the Messenger Lock and Key API.                                                                                                                                       |
| [**IMessengerPrivate**](im-imessengerprivate.md)     | A Messenger service   API that implements [**IMsgrLock**](im-imsgrlock.md) and provides programmatic access to the [**MessengerPriv**](im-messengerpriv-object.md) object.     |
| [**IMsgrSessionManager**](im-imsgrsessionmanager.md) | A Messenger service that implements [**IMsgrLock**](im-imsgrlock.md) and provides programmatic access to the [**MsgrSessionManager**](im-msgrsessionmanager-object.md) object. |



 

As you can see from the following table, there is a correspondence between the interfaces and the programmable objects described in the previous section. [**IMsgrLock**](im-imsgrlock.md) provides the API for a Messenger client to invoke each step of the Messenger Lock and Key authentication process. **IMsgrLock** also exposes the [**Status**](im-imsgrlock-status-property.md) property, which can be used to obtain the status of the API locking for a given object.

The following table lists the dispinterfaces that are used with Messenger Lock and Key.



| Dispinterface                                                     | Description                                                                                                                         |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [**DMessengerPrivateEvents**](im-dmessengerprivateevents.md)     | Fires notifications from a Messenger service for applications that implement [**IMessengerPrivate**](im-imessengerprivate.md).     |
| [**DMsgrSessionManagerEvents**](im-dmsgrsessionmanagerevents.md) | Fires notifications from a Messenger service for applications that implement [**IMsgrSessionManager**](im-imsgrsessionmanager.md). |



 

Messenger Lock and Key events are fired to [**DMessengerPrivateEvents**](im-dmessengerprivateevents.md) or [**DMsgrSessionManagerEvents**](im-dmsgrsessionmanagerevents.md), depending on the type of object from which the [**IMsgrLock**](im-imsgrlock.md) interface is obtained.

## Authentication Process

A Messenger client application must provide authentication to a Messenger service in each of the following scenarios.

-   When a Messenger service requests authentication with a challenge.
-   When a Messenger client application requires access to one or more of the Messenger service  APIs.

In both scenarios, the Messenger Lock and Key mechanism is used to provide authentication and unlock the Messenger service  APIs. The Messenger Lock and Key mechanism is implemented so that objects are unlocked individually. Therefore, the authentication process detailed in this section must be done for each Messenger service object in use by an application.

The following sections describe each step of the Messenger Lock and Key authentication process. Subsequent sections illustrate how a [**MsgrSessionManager**](im-msgrsessionmanager-object.md) object can be unlocked with Messenger Lock and Key. The same process is used to unlock any Messenger service object. Therefore, the [**IMessengerPrivate**](im-imessengerprivate.md) object can be unlocked using exactly the same procedure as shown in the following code, which unlocks the **MsgrSessionManager** object.

### Request

This is the first step in the authentication process of a Messenger client application. Initially, a Messenger client application must issue a request for authentication to a Messenger service . In the first transaction between the Messenger client application and a Messenger service , the application must call the [**RequestChallenge**](im-imsgrlock-requestchallenge-method.md) method.

In order for a Messenger client application to participate in an authentication transaction, it must first instantiate an object. The Messenger client application must provide the appropriate event handlers for these events.

The [**RequestChallenge**](im-imsgrlock-requestchallenge-method.md) method takes a single parameter that uniquely identifies the authentication transaction. A random number should be used for this purpose.

> [!Note]  
> A Messenger client application must provide Lock and Key authentication for each Messenger object it creates. It must also re-authenticate after it has gone offline.

 

### Challenge-Response

The Messenger service responds to an application's request with an authentication challenge. The application receives the server challenge when the [**OnLockChallenge**](im-dmessengerprivateevents-onlockchallenge.md) event is fired.

The [**OnLockChallenge**](im-dmessengerprivateevents-onlockchallenge.md) event handler has two arguments. The first, lCookie, is the same value that the Messenger client application passes to the Messenger service when the [**RequestChallenge**](im-imsgrlock-requestchallenge-method.md) method is invoked. The second argument, sChallenge, is a string that is generated by the Messenger service .

The first step in the [**OnLockChallenge**](im-dmessengerprivateevents-onlockchallenge.md) event handler compares the value of lCookie with the variable passed by the [**RequestChallenge**](im-imsgrlock-requestchallenge-method.md) method to verify that the event notification corresponds to the applications challenge request. If the correct notification is received, then the server challenge string, bstrChallenge, is stored for later use in a variable. A Boolean variable is also set to **TRUE** in this handler, this value is used in other parts of the code to verify that a challenge has been received by the application.

After the [**OnLockChallenge**](im-dmessengerprivateevents-onlockchallenge.md) event handler has received and verified the server's challenge, the application can proceed by formulating and sending its response.

You must concatenate the server challenge string and your key. It is important to combine the values prior to hashing so that authentication is successful.

> [!Note]  
> Each application must obtain its own ID/Key pair.

 

After the Messenger service challenge and Messenger client application key strings have been combined, a method on a hypothetical MD5 provider object is called to hash the resulting string using an MD5 algorithm.

The MD5 hashed string is passed as the second parameter of the **SendResponse** method. The use of the MD5 hash helps provide additional security during the authentication process.

After the Messenger client has received the authentication transaction, it processes the data and returns a result.

> [!Note]  
> It is the responsibility of the developer to implement or locate an implementation of the MD5 hash algorithm. MD5 has been implemented in several libraries that can by used with a variety of programming languages. Some are freely distributed in the public domain and can be found on the Internet.

 

### Result

A Messenger client application receives the result of a Messenger Lock and Key authentication transaction with the [**OnLockResult**](im-dmessengerprivateevents-onlockresult.md) event.

A Messenger client application cannot unlock the licensed Messenger client APIs more than once during a session. Therefore, if an application attempts to re-authenticate during the same session, the **MSGR\_E\_API\_ALREADY\_UNLOCKED** error code is returned and there is no resulting transaction.

## Security and Encryption

### External References

Although it is generally useful to encapsulate components using DLL files, the use of external references by an application can sometimes introduce a security hole. For example, using an external DLL that implements MD5 is not recommended, because this provides an opportunity for hackers to replace the external DLL file with a simple component that echoes the data sent by the application.

Therefore, instead of using an external DLL to perform MD5 hash, it is strongly recommended that any Messenger client application includes its own MD5 implementation. Using an internal code implementation instead of referencing an external DLL helps protect the security of the application.

### ID/Key Pairs

As illustrated in the section on the Messenger Lock and Key Authentication Process, an MD5 algorithm is used to hash some of the authentication data, which helps provide an additional degree of security. A unique ID/key pair must be assigned for use by a particular Messenger client application. For more information, see [Developing and Testing Applications with the Messenger Service APIs](im-app-devtest.md).

### Hiding ID/Key Pairs

When source code is compiled, the resulting binary executable file invariably contains searchable strings of data. For example, when variables are declared and initialized with values, these can be detected by examining the contents of a compiled executable file. Therefore, care must be taken in developing a Messenger client application to ensure that the ID/Key pair is reasonably well hidden inside the executable file. Several techniques can be used to obfuscate or scramble sensitive data. Generally, the sensitive data is broken into its constituent characters. These characters are then transformed or encrypted so that the ID/Key is not trivial to read directly from the uncompiled source code. Additional code is implemented to reassemble the ID/Key programmatically at runtime.

Using one or more techniques to hide the ID/Key pair in the executable file of a Messenger client application is strongly recommended.

## Related topics

<dl> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Windows Messenger](im-messenger-entry.md)
</dt> </dl>

 

 




