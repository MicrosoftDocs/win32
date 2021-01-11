---
description: Gets the XML data (sent over the wire) that represents the token.
ms.assetid: 52EC991A-0499-4182-AC4F-512BAFB4F896
title: IUpdateEndpointAuthToken::TokenData method (UpdateEndpointAuth.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUpdateEndpointAuthToken.TokenData
api_type: 
- COM
api_location: 
- UpdateEndpointAuth.dll
---

# IUpdateEndpointAuthToken::TokenData method

Gets the XML data (sent over the wire) that represents the token.

## Syntax


```C++
HRESULT TokenData(
  [out] BSTR *pszTokenData
);
```



## Parameters

<dl> <dt>

*pszTokenData* \[out\]
</dt> <dd>

The XML data (sent over the wire) that represents the token. For example, the data for a WS-Security SAML (Security Assertion Markup Language) 1.1 token is the SAML code that is added to the request.

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

 

 




