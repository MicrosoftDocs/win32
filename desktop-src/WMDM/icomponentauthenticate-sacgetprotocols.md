---
title: IComponentAuthenticate SACGetProtocols method
description: The SACGetProtocols method is used by a component to discover the authentication protocols supported by another component.
ms.assetid: 'db01f2a4-5cd5-4acc-be17-37b4c9861cc9'
keywords: ["SACGetProtocols method windows Media Device Manager", "SACGetProtocols method windows Media Device Manager , IComponentAuthenticate interface", "IComponentAuthenticate interface windows Media Device Manager , SACGetProtocols method"]
topic_type:
- apiref
api_name:
- IComponentAuthenticate.SACGetProtocols
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
---

# IComponentAuthenticate::SACGetProtocols method

The **SACGetProtocols** method is used by a component to discover the authentication protocols supported by another component.

## Syntax


```C++
HRESULT SACGetProtocols(
  [out] DWORD **ppdwProtocols,
  [out] DWORD *pdwProtocolCount
);
```



## Parameters

<dl> <dt>

*ppdwProtocols* \[out\]
</dt> <dd>

Pointer to an array of supported protocols. For this version of Windows Media Device Manager, it is a single-element **DWORD** array containing the value SAC\_PROTOCOL\_V1.

</dd> <dt>

*pdwProtocolCount* \[out\]
</dt> <dd>

Pointer to a **DWORD** containing the number of protocols returned in *ppdwProtocols*. The number is always 1 for this version.

</dd> </dl>

## Return value

The method returns an **HRESULT**. All the interface methods in Windows Media Device Manager can return any of the following classes of error codes:

-   Standard COM error codes
-   Windows error codes converted to HRESULT values
-   Windows Media Device Manager error codes

For an extensive list of possible error codes, see [Error Codes](error-codes.md).

## Remarks

This method is implemented by a service provider, and never called by an application.

## Examples

The following method demonstrates a service provider's implementation of the **SACGetProtocols** method. It does this by calling [**CSecureChannelServer::SACGetProtocols**](csecurechannelserver-sacgetprotocols.md) on its private [CSecureChannelServer](csecurechannelserver-class.md) member.


```C++
STDMETHODIMP CMyServiceProvider::SACGetProtocols(
    DWORD **ppdwProtocols,
    DWORD  *pdwProtocolCount)
{
    HRESULT hr = E_FAIL;

    // Verify that the global CSecureChannelServer member is valid.
    if(g_pAppSCServer == NULL)
       return hr;

    hr = g_pAppSCServer->SACGetProtocols(
        ppdwProtocols,
        pdwProtocolCount
    );

    return hr;
}
```



## Requirements



|                    |                                                                                                       |
|--------------------|-------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Icomponentauthenticate.idl</dt> </dl> |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl>               |



## See also

<dl> <dt>

[**Authenticating the Service Provider**](authenticating-the-service-provider.md)
</dt> <dt>

[**CSecureChannelServer::SACGetProtocols**](csecurechannelserver-sacgetprotocols.md)
</dt> <dt>

[**IComponentAuthenticate Interface**](icomponentauthenticate.md)
</dt> </dl>

 

 





