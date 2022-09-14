---
description: Defines the type of tokens that can be used for authenticating with an endpoint.
ms.assetid: 2048BD09-056F-47C1-AD2F-998DE6C52EA6
title: UpdateEndpointAuthTokenType enumeration (UpdateEndpointAuth.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- UpdateEndpointAuthTokenType
api_type: 
- HeaderDef
api_location: 
- UpdateEndpointAuth.h
---

# UpdateEndpointAuthTokenType enumeration

Defines the type of tokens that can be used for authenticating with an endpoint.

## Syntax


```C++
typedef enum tagUpdateEndpointAuthTokenType { 
  ueattInvalidTokenType  = 0x0,
  ueattSAML11Token       = 0X1
} UpdateEndpointAuthTokenType;
```



## Constants

<dl> <dt>

<span id="ueattInvalidTokenType"></span><span id="ueattinvalidtokentype"></span><span id="UEATTINVALIDTOKENTYPE"></span>**ueattInvalidTokenType**
</dt> <dd>

No authentication token is needed.

</dd> <dt>

<span id="ueattSAML11Token"></span><span id="ueattsaml11token"></span><span id="UEATTSAML11TOKEN"></span>**ueattSAML11Token**
</dt> <dd>

The authentication token for the endpoint is a WS-Security SAML (Security Assertion Markup Language) 1.1 token.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                        |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                              |
| Header<br/>                   | <dl> <dt>UpdateEndpointAuth.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>UpdateEndpointAuth.idl</dt> </dl> |



 

 




