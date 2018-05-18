---
title: Connecting to the Server
description: Connecting to the Server
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '47538328-3053-47ea-8cc7-5d6ae0257678'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
keywords: ["Connecting to the Server LDAP"]
---

# Connecting to the Server

Although it is not required that a client call [**ldap\_connect**](ldap-connect.md) to establish a connection to the server, it is good programming practice to do so. If you do not call **ldap\_connect** but, instead, call another function, like [**ldap\_bind\_s**](ldap-bind-s.md), that function will detect that there is no connection and will establish the connection itself. However, if you must troubleshoot this part of your application, establishing the connection prior to making a call to some other function, will separate the possible problems if the connection fails. Another reason for calling **ldap\_connect** prior to calling other functions is that you may want to specify certain options at the time that the connection is made. For example, a client can call [**ldap\_init**](ldap-init.md) to initialize a session, then call **ldap\_connect** with a non-NULL timeout parameter value, to connect to the server with a specified timeout.

The ldap\_connect function simply connects to the server. It does not perform authentication. If the call to [**ldap\_connect**](ldap-connect.md) succeeds, and if an explicit bind is not performed, the client can perform further operations as an anonymous user.

Calling [**ldap\_connect**](ldap-connect.md) does not establish SASL signing or sealing (encryption). However, TLS (SSL) encryption will be established if all the necessary preliminaries, such as having certificates set up on both client and server, have been taken care of, and you have requested that SSL/TLS be used on the connection.

 

 




