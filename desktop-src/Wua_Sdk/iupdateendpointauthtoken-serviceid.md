---
description: Gets the identifier of the service to be authenticated with the endpoint token.
ms.assetid: FE110B8E-F8FB-4CC8-BDD8-6427BA8B7920
title: IUpdateEndpointAuthToken::ServiceID method (UpdateEndpointAuth.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUpdateEndpointAuthToken.ServiceID
api_type: 
- COM
api_location: 
- UpdateEndpointAuth.dll
---

# IUpdateEndpointAuthToken::ServiceID method

Gets the identifier of the service to be authenticated with the endpoint token.

## Syntax


```C++
HRESULT ServiceID(
  [out] GUID *pServiceID
);
```



## Parameters

<dl> <dt>

*pServiceID* \[out\]
</dt> <dd>

The identifier of the service.

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

 

 




