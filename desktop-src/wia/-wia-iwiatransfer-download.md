---
description: Initiates a data download to the caller.
ms.assetid: e639fabb-2c13-4009-affa-1c2b06c0d4c8
title: IWiaTransfer::Download method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaTransfer.Download
api_type: 
- COM
api_location: 
- Wiaguid.lib
- Wiaguid.dll
---

# IWiaTransfer::Download method

Initiates a data download to the caller.

## Syntax


```C++
HRESULT Download(
  [in] LONG                 lFlags,
  [in] IWiaTransferCallback *pIWiaTransferCallback
);
```



## Parameters

<dl> <dt>

*lFlags* \[in\]
</dt> <dd>

Type: **LONG**

Currently unused. Should be set to zero.

</dd> <dt>

*pIWiaTransferCallback* \[in\]
</dt> <dd>

Type: **[**IWiaTransferCallback**](-wia-iwiatransfercallback.md)\***

Specifies a pointer to the caller's [**IWiaTransferCallback**](-wia-iwiatransfercallback.md) interface.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If a folder is downloaded, then all the child items of that folder are also transferred. Each item is transferred in a separate stream.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>       |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Wiaguid.lib</dt> </dl> |



 

 




