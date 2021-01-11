---
description: Gets the XML format of an unattached reference to the token.
ms.assetid: D5D61ED7-68FB-4FC0-9C2A-90D3B1219351
title: IUpdateEndpointAuthToken::TokenReferenceUnattached method (UpdateEndpointAuth.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUpdateEndpointAuthToken.TokenReferenceUnattached
api_type: 
- COM
api_location: 
- UpdateEndpointAuth.dll
---

# IUpdateEndpointAuthToken::TokenReferenceUnattached method

Gets the XML format of an unattached reference to the token.

## Syntax


```C++
HRESULT TokenReferenceUnattached(
  [out] BSTR *pszTokenReference
);
```



## Parameters

<dl> <dt>

*pszTokenReference* \[out\]
</dt> <dd>

Pointer to the unattached token reference.

</dd> </dl>

## Return value

Returns **S\_OK** if successful. Otherwise, returns a COM or Windows error code.

## Remarks

An unattached reference refers a referece (such as the signiture that is using the token) that is not in the message where the token resides.

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

 

 




