---
description: Returns the preferred type of authentication token for the endpoint of the service.
ms.assetid: DF60C49A-89FE-4EEB-8E82-C2C43F2D2F2A
title: IUpdateEndpointAuthProvider::GetPreferredEndpointTokenType method (UpdateEndpointAuth.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUpdateEndpointAuthProvider.GetPreferredEndpointTokenType
api_type: 
- COM
api_location: 
- UpdateEndpointAuth.dll
---

# IUpdateEndpointAuthProvider::GetPreferredEndpointTokenType method

Returns the preferred type of authentication token for the endpoint of the service.

## Syntax


```C++
HRESULT GetPreferredEndpointTokenType(
  [in]  GUID               serviceId,
  [in]  UpdateEndpointType endpointType,
  [in]  ULONG              ulRequestedTypes,
  [out] ULONG              *pulPreferredTokenTypes
);
```



## Parameters

<dl> <dt>

*serviceId* \[in\]
</dt> <dd>

Identifies the service to be updated.

</dd> <dt>

*endpointType* \[in\]
</dt> <dd>

Identifies the type of endpoint tneeded to connect to the service.

</dd> <dt>

*ulRequestedTypes* \[in\]
</dt> <dd>

Identifies the ORed set of tokens that are supported by the endpoint.

</dd> <dt>

*pulPreferredTokenTypes* \[out\]
</dt> <dd>

Specify the ORed set of authentication token types that are preferred. (Set to 0 to indicate that no authentication token is needed).

</dd> </dl>

## Return value

Returns S\_OK if successful. Otherwise, returns a COM or Windows error code.

## Remarks

When this method is returned, WUA chooses a token type from the preferred types and passes it to the tokenType parameter of the [**GetEndpointToken**](iupdateendpointauthprovider-getendpointtoken.md) method.

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

[**IUpdateEndpointAuthProvider**](iupdateendpointauthprovider.md)
</dt> <dt>

[**GetEndpointToken**](iupdateendpointauthprovider-getendpointtoken.md)
</dt> </dl>

 

 




