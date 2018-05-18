---
title: Developing and Testing Applications with the Messenger Service APIs
description: This topic provides basic information and requirements you need to develop, test, and deploy Messenger client applications that use the Messenger service APIs.
ms.assetid: 'e38c6145-a617-4768-b9c8-1af725d1e00d'
keywords: ["Windows Messenger,developing applications", "Windows Messenger,testing applications", "Windows Messenger,terminology", "Messenger client,terminology", "Messenger service,terminology", "Messenger Lock and Key,terminology", "Lock and Key,terminology", "Messenger Lock and Key,request", "Lock and Key,request", "Messenger client,challenge", "Messenger client,response", "Messenger Lock and Key,result", "Lock and Key,result", "Messenger Session Invite", "RSA-MD5 Message Digest Algorithm (MD5)", "MD5 (RSA-MD5 Message Digest Algorithm)", "Messenger client,ID", "Messenger service,key", "server cloud", "Microsoft .NET Messenger Service"]
---

# Developing and Testing Applications with the Messenger Service APIs

This topic provides basic information and requirements you need to develop, test, and deploy Messenger client applications that use the Messenger service  APIs.

This topic contains the following sections.

-   [Introduction](#introduction)
-   [Terminology](#terminology)
-   [Related topics](#related-topics)

## Introduction

A mechanism called "Messenger Lock and Key" helps protect the Messenger service   APIs. This means that any application that uses the Messenger service   APIs must first unlock them using an authentication process, which is described in detail in [Messenger Lock and Key API](im-lock-and-key-ovw.md).

Any Messenger client application uses at least one Messenger service and, therefore, server clouds are available for both the production and the development environments. You should begin by registering an ID/key pair that you can use to develop the application. This type of ID/key pair can only be used to develop a Messenger client application and test it within the Test Server Cloud environment.

After a Messenger client application is ready for deployment to a production environment, you must obtain a second ID/key pair, which is used by the application in a production environment. Each type of ID/key pair functions in only one of the environments. The licensing, terms, and conditions for each environment are processed separately.

> \[!Important\]  
> ID/key pairs are no longer being issued.

 

## Terminology

The following terms have a specific meaning in the context of the Messenger client APIs.



|                                        |                                                                                                                                                                                                                                                                     |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Messenger client                       | Application that uses the APIs exposed by Windows Messenger to provide client-side functionality for use with Messenger service s.                                                                                                                                  |
| Messenger service                      | Service used by a Messenger client application. Messenger client applications can use Microsoft .NET Messenger Service.                                                                                                                                             |
| Messenger Lock and Key                 | A friendly name for three interfaces that are exposed by Messenger client applications and are used to unlock the Messenger service  APIs.                                                                                                                          |
| Messenger Session Invite               | A friendly name for a set of interfaces in the Messenger service  APIs that are locked with the Lock and Key mechanism.                                                                                                                                             |
| ID                                     | An alphanumeric string value that identifies an application used to unlock the licensed Messenger client APIs.                                                                                                                                                      |
| Key                                    | An alphanumeric string value that identifies an application used to unlock the Messenger service  APIs.                                                                                                                                                             |
| RSA-MD5 Message Digest Algorithm (MD5) | The RSA-MD5 Message Digest Algorithm (MD5). This algorithm is used to encrypt authentication data during a challenge-response transaction between an application that uses the Messenger client APIs to authenticate with Microsoft .NET Messenger Service.         |
| Request                                | The first step in the Lock and Key authentication process. An application must issue a request through the Messenger client API in order to receive a challenge, to which it can then reply with a response.                                                        |
| Challenge                              | A response from Microsoft .NET Messenger Service to an application's request. A challenge is issued in the form of a Unicode string. A challenge can be issued to a Messenger client at any time, without the need for a request by a Messenger client application. |
| Response                               | A response from a Messenger client application to a challenge it has received from Microsoft .NET Messenger Service.                                                                                                                                                |
| Result                                 | The result of a Lock and Key authentication transaction between a Messenger client application and Microsoft .NET Messenger Service. The result can either be successful or unsuccessful.                                                                           |
| Server Cloud                           | A computer network with a topology that is configured to host applications and services.                                                                                                                                                                            |



 

## Related topics

<dl> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Windows Messenger](im-messenger-entry.md)
</dt> </dl>

 

 




