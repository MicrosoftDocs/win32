---
description: Request a token for the endpoint of the service using the specified credentials.
ms.assetid: 2CA0F826-9A05-4385-AF1A-A8C05B3DAFE2
title: IUpdateEndpointAuthProvider::GetEndpointToken method (UpdateEndpointAuth.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IUpdateEndpointAuthProvider.GetEndpointToken
api_type: 
- COM
api_location: 
- UpdateEndpointAuth.dll
---

# IUpdateEndpointAuthProvider::GetEndpointToken method

Request a token for the endpoint of the service using the specified credentials.

## Syntax


```C++
HRESULT GetEndpointToken(
  [in]  GUID                        serviceId,
  [in]  UpdateEndpointType          endpointType,
  [in]  UpdateEndpointProxySettings proxySettings,
  [in]  HANDLE_PTR                  hUserToken,
  [in]  UpdateEndpointAuthTokenType tokenType,
  [in]  BOOL                        fRefreshOnline,
  [out] IUnknown                    **ppEndpointToken
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

Identifies the type of endpoint that is implemented by the service.

</dd> <dt>

*proxySettings* \[in\]
</dt> <dd>

The settings to be used when connecting to a proxy server. See the [**UpdateEndpointProxySettings**](updateendpointproxysettings.md) structure for more details.

</dd> <dt>

*hUserToken* \[in\]
</dt> <dd></dd> <dt>

*tokenType* \[in\]
</dt> <dd>

Identifies the type of authentication token that is used for authentication.

</dd> <dt>

*fRefreshOnline* \[in\]
</dt> <dd>

Indicates weather WUA requests a new token. True indicates that a new token is requested. False indicates that a new or cached token is requested. See Remarks for more information.

</dd> <dt>

*ppEndpointToken* \[out\]
</dt> <dd>

Specifiy the endpoint token to be used.

</dd> </dl>

## Return value

Returns S\_OK if successful. Otherwise, returns a COM or Windows error code.

## Remarks

WUA typically sets the fRefreshOnline parameter to false when this method is first called, then if a connection error occures WUA sets that parameter to true when the method is called again. However, the implementation of this method can request a new token from a Security Token Service (STS) or provide a cached token at any time.

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
</dt> </dl>

 

 




