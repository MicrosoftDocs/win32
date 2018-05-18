---
title: IComponentAuthenticate SACAuth method
description: The SACAuth method establishes a secure authenticated channel between components.
ms.assetid: '26cecd09-5f28-47e5-92ec-c2f277be8052'
keywords: ["SACAuth method windows Media Device Manager", "SACAuth method windows Media Device Manager , IComponentAuthenticate interface", "IComponentAuthenticate interface windows Media Device Manager , SACAuth method"]
topic_type:
- apiref
api_name:
- IComponentAuthenticate.SACAuth
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
---

# IComponentAuthenticate::SACAuth method

The **SACAuth** method establishes a secure authenticated channel between components.

## Syntax


```C++
HRESULT SACAuth(
  [in]  DWORD dwProtocolID,
  [in]  DWORD dwPass,
  [in]  BYTE  *pbDataIn,
  [in]  DWORD dwDataInLen,
  [out] BYTE  **ppbDataOut,
  [out] DWORD *pdwDataOutLen
);
```



## Parameters

<dl> <dt>

*dwProtocolID* \[in\]
</dt> <dd>

**DWORD** containing the protocol identifier. For this version of Windows Media Device Manager, always set this parameter to SAC\_PROTOCOL\_V1.

</dd> <dt>

*dwPass* \[in\]
</dt> <dd>

**DWORD** containing the number of the current communication pass. A pass consists of two messages, one in each direction. SAC\_PROTOCOL\_V1 is a two-pass protocol, and the passes are numbered 0 and 1.

</dd> <dt>

*pbDataIn* \[in\]
</dt> <dd>

Pointer to the input data.

</dd> <dt>

*dwDataInLen* \[in\]
</dt> <dd>

**DWORD** containing the length of the data to which *pbDataIn* points.

</dd> <dt>

*ppbDataOut* \[out\]
</dt> <dd>

Pointer to a pointer to the output data.

</dd> <dt>

*pdwDataOutLen* \[out\]
</dt> <dd>

Pointer to a **DWORD** containing the length of the data to which *ppbDataOut* points.

</dd> </dl>

## Return value

The method returns an **HRESULT**. All the interface methods in Windows Media Device Manager can return any of the following classes of error codes:

-   Standard COM error codes
-   Windows error codes converted to HRESULT values
-   Windows Media Device Manager error codes

For an extensive list of possible error codes, see [Error Codes](error-codes.md).

## Remarks

This method is called only by service providers. It is called one or more times as dictated by the protocol identifier.

The structure of the data in *pbDataIn* and *ppbDataOut* is determined by the values of *dwProtocolID* and *dwPass*.

## Examples

The following C++ code demonstrates a service provider's implementation of **SACAuth**. It calls [**CSecureChannelServer::SACAuth**](csecurechannelserver-sacauth.md) on a previously created private [CSecureChannelServer](csecurechannelserver-class.md) member.


```C++
HRESULT CMyServiceProvider::SACAuth(
    DWORD   dwProtocolID,
    DWORD   dwPass,
    BYTE   *pbDataIn,
    DWORD   dwDataInLen,
    BYTE  **ppbDataOut,
    DWORD  *pdwDataOutLen)
{
    HRESULT hr = S_OK;

    // Verify that the global CSecureChannelServer member is valid.
    if(g_pAppSCServer == NULL)
        return E_FAIL;

    hr = g_pAppSCServer->SACAuth(
        dwProtocolID,
        dwPass,
        pbDataIn, dwDataInLen,
        ppbDataOut, pdwDataOutLen
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

[**CSecureChannelServer::SACAuth**](csecurechannelserver-sacauth.md)
</dt> <dt>

[**IComponentAuthenticate Interface**](icomponentauthenticate.md)
</dt> </dl>

 

 





