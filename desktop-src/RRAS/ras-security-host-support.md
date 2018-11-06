---
title: RAS Security Host Support
description: Windows NT 4.0 provides a way for a third-party RAS security DLL to enhance the built-in RAS security features. Windows 95 does not provide this support.
ms.assetid: 1cbacd7f-c9b9-4fb4-b505-a4b1d1b6f632
keywords:
- Host Support, RAS
- Security Host Support, RAS
ms.topic: article
ms.date: 05/31/2018
---

# RAS Security Host Support

Windows NT 4.0 provides a way for a third-party RAS security DLL to enhance the built-in RAS security features. Windows 95 does not provide this support.

A Windows NT/Windows 2000 RAS server provides security mechanisms for validating the network access of remote users. When a RAS server receives a call, it validates the user's credentials against the local or domain account database. RAS also supports call-back security, in which the RAS server hangs up and then calls back to the remote user to establish the connection. For networks in which this level of security is not enough, you can install a third-party RAS security DLL. The security DLL can then authenticate a remote user by reading security information from a database other than the standard user account database.

When the RAS server receives a call, it invokes the security DLL to authenticate the remote user. The RAS security host support provides a mechanism for the security DLL to communicate with the remote user through a terminal window on the remote computer. In a typical scenario, the security DLL asks for the logon name of the remote user. The DLL then uses its private security database to formulate a challenge to send to the remote terminal. For example, the challenge could be a code that the user must provide as input to a cardkey reader. The cardkey reader then displays a response that the remote user types in the terminal window. The security DLL then validates the response against the user's information in the private security database.

If the security DLL authenticates the remote user, the RAS server performs its own authentication. This ensures that RAS security always authenticates a remote user, even if a security DLL is installed that grants access to all users.

> [!Note]  
> Windows NT/Windows 2000 currently provides RAS security host support only for asynchronous modem connections; other types of connections such as Ethernet (which is not a modem connection), VPN (which is also not a modem connection), or ISDN (which is synchronous), are not supported.

 

 

 




