---
title: Security Processing Results
description: On a secure channel, only those messages that successfully pass security checks are delivered to the application.
ms.assetid: 891e1f91-406e-4997-9da6-59b5fe578d0d
keywords:
- Security Processing Results Web Services for Windows
- WWSAPI
- WWS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Security Processing Results

On a secure channel, only those messages that successfully pass security checks are delivered to the application. For these messages, some results from security verification are attached as message properties, and the application may extract and examine these properties to perform additional steps such as authorization checks.

## 

The function [**WsGetMessageProperty**](/windows/win32/WebServices/nf-webservices-wsgetmessageproperty?branch=master) can be used to retrieve any of the security-related properties defined in [**WS\_MESSAGE\_PROPERTY\_ID**](/windows/win32/WebServices/ne-webservices-ws_message_property_id?branch=master). **WsGetMessageProperty** returns an error for queries that ask for security properties not applicable to the type of security used on the channel. The message continues to own the properties returned by the query function.

The following API elements are used with security processing results.

| Enumeration                                                                | Description                                                                                 |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [**WS\_SECURITY\_TOKEN\_PROPERTY\_ID**](/windows/win32/WebServices/ne-webservices-ws_security_token_property_id?branch=master) | Defines the keys for the fields and properties that can be extracted from a security token. |



 



| Function                                                         | Description                                           |
|------------------------------------------------------------------|-------------------------------------------------------|
| [**WsGetSecurityTokenProperty**](/windows/win32/WebServices/nf-webservices-wsgetsecuritytokenproperty?branch=master) | Extracts a field or a property from a security token. |



 



| Handle                                       | Description                                     |
|----------------------------------------------|-------------------------------------------------|
| [WS\_SECURITY\_TOKEN](ws-security-token.md) | An opaque handle representing a security token. |



 

 

 




