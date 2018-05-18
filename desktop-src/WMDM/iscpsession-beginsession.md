---
title: ISCPSession BeginSession method
description: The BeginSession method indicates beginning of a transfer session. It can be used to optimize operations that need to occur only once per transfer session.
ms.assetid: 'da458458-5828-4ab4-8793-d59a07f46569'
keywords: ["BeginSession method windows Media Device Manager", "BeginSession method windows Media Device Manager , ISCPSession interface", "ISCPSession interface windows Media Device Manager , BeginSession method"]
topic_type:
- apiref
api_name:
- ISCPSession.BeginSession
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
---

# ISCPSession::BeginSession method

The **BeginSession** method indicates beginning of a transfer session. It can be used to optimize operations that need to occur only once per transfer session.

## Syntax


```C++
HRESULT BeginSession(
  [in] IMDSPDevice *pIDevice,
  [in] BYTE        *pCtx,
  [in] DWORD       dwSizeCtx
);
```



## Parameters

<dl> <dt>

*pIDevice* \[in\]
</dt> <dd>

Pointer to an [**IMDSPDevice**](imdspdevice.md) object.

</dd> <dt>

*pCtx* \[in\]
</dt> <dd>

Pointer to the context.

</dd> <dt>

*dwSizeCtx* \[in\]
</dt> <dd>

**DWORD** containing the size of context.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If the method fails, it returns an **HRESULT** error code.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMSCP.idl</dt> </dl>    |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**ISCPSession Interface**](iscpsession.md)
</dt> </dl>

 

 





