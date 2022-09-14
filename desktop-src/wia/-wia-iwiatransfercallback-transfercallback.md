---
description: Provides progress and other notifications during a transfer.
ms.assetid: 0faba0f8-b318-4c47-85e0-5ce128fe1c82
title: IWiaTransferCallback::TransferCallback method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaTransferCallback.TransferCallback
api_type: 
- COM
api_location: 
- Wiaguid.lib
- Wiaguid.dll
---

# IWiaTransferCallback::TransferCallback method

Provides progress and other notifications during a transfer.

## Syntax


```C++
HRESULT TransferCallback(
  [in] LONG              lFlags,
  [in] WiaTransferParams *pWiaTransferParams
);
```



## Parameters

<dl> <dt>

*lFlags* \[in\]
</dt> <dd>

Type: **LONG**

Currently unused. Should be set to zero.

</dd> <dt>

*pWiaTransferParams* \[in\]
</dt> <dd>

Type: **[**WiaTransferParams**](-wia-wiatransferparams.md)\***

Specifies a pointer to a [**WiaTransferParams**](-wia-wiatransferparams.md) structure.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

When this method is implemented by an image processing filter, the Windows Image Acquisition (WIA) 2.0 minidriver calls it during image acquisition to send progress messages back to the application.

A filter's **IWiaTransferCallback::TransferCallback** must delegate to the application callback's **IWiaTransferCallback::TransferCallback** method. Usually, the filter stream filters the data passed to it and writes the filtered data directly to the application provided stream. When image processing filter stores data between calls to its [IStream::Write](/windows/win32/api/objidl/nf-objidl-isequentialstream-write) method, it must also modify the *lPercentComplete* and *ulBytesWrittenToCurrentStream* values in the [**WiaTransferParams**](-wia-wiatransferparams.md) structure.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>       |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Wiaguid.lib</dt> </dl> |



 

 
