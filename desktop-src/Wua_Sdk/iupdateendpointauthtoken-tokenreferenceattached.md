---
description: Gets the XML format of an attached reference to the token.
ms.assetid: F4329A2E-61FD-40E0-9E24-87C9A4585E55
title: IUpdateEndpointAuthToken::TokenReferenceAttached method (UpdateEndpointAuth.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUpdateEndpointAuthToken.TokenReferenceAttached
api_type: 
- COM
api_location: 
- UpdateEndpointAuth.dll
---

# IUpdateEndpointAuthToken::TokenReferenceAttached method

Gets the XML format of an attached reference to the token.

## Syntax


```C++
HRESULT TokenReferenceAttached(
  [out] BSTR *pszTokenReference
);
```



## Parameters

<dl> <dt>

*pszTokenReference* \[out\]
</dt> <dd>

Pointer to the attached token reference.

</dd> </dl>

## Return value

Returns **S\_OK** if successful. Otherwise, returns a COM or Windows error code.

## Remarks

An attached reference refers a referece (such as the signiture that is using the token) that is in the same message where the token resides.

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

 

 




