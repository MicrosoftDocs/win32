---
title: ISCPSession EndSession method
description: The EndSession method indicates the ending of a transfer session.
ms.assetid: '322794ae-f8cd-4e2d-a329-728d281755cd'
keywords: ["EndSession method windows Media Device Manager", "EndSession method windows Media Device Manager , ISCPSession interface", "ISCPSession interface windows Media Device Manager , EndSession method"]
topic_type:
- apiref
api_name:
- ISCPSession.EndSession
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
---

# ISCPSession::EndSession method

The **EndSession** method indicates the ending of a transfer session.

## Syntax


```C++
HRESULT EndSession(
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

 

 





