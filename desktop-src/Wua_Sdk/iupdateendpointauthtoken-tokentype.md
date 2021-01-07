---
description: Gets the type of the endpoint token, such as a WS-Security SAML (Security Assertion Markup Language) 1.1 token.
ms.assetid: 1C6FFAD7-DC80-4957-96B4-FA0D954786DD
title: IUpdateEndpointAuthToken::TokenType method (UpdateEndpointAuth.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUpdateEndpointAuthToken.TokenType
api_type: 
- COM
api_location: 
- UpdateEndpointAuth.dll
---

# IUpdateEndpointAuthToken::TokenType method

Gets the type of the endpoint token, such as a WS-Security SAML (Security Assertion Markup Language) 1.1 token.

## Syntax


```C++
HRESULT TokenType(
  [out] UpdateEndpointAuthTokenType *pTokenType
);
```



## Parameters

<dl> <dt>

*pTokenType* \[out\]
</dt> <dd>

The type of the endpoint token.

</dd> </dl>

## Return value

Returns **S\_OK** if successful. Otherwise, returns a COM or Windows error code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP, Windows 2000 Professional with SP3 \[desktop apps only\]<br/>                   |
| Minimum supported server<br/> | Windows Server 2003, Windows 2000 Server with SP3 \[desktop apps only\]<br/>                |
| Header<br/>                   | <dl> <dt>UpdateEndpointAuth.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>UpdateEndpointAuth.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>UpdateEndpointAuth.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>UpdateEndpointAuth.dll</dt> </dl> |



## See also

<dl> <dt>

[**IUpdateEndpointAuthToken**](iupdateendpointauthtoken.md)
</dt> </dl>

 

 




