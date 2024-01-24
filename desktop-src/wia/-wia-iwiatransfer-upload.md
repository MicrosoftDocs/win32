---
description: Initiates a data upload of a single item from the caller.
ms.assetid: 301ac5d9-b864-4c3c-bd4b-143cc4032dcb
title: IWiaTransfer::Upload method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaTransfer.Upload
api_type: 
- COM
api_location: 
- Wiaguid.lib
- Wiaguid.dll
---

# IWiaTransfer::Upload method

Initiates a data upload of a single item from the caller.

## Syntax


```C++
HRESULT Upload(
  [in] LONG                 lFlags,
  [in] IStream              *pSource,
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

*pSource* \[in\]
</dt> <dd>

Type: **[IStream](/windows/win32/api/objidl/nn-objidl-istream)\***

Specifies a pointer to the [IStream](/windows/win32/api/objidl/nn-objidl-istream) data.

</dd> <dt>

*pIWiaTransferCallback* \[in\]
</dt> <dd>

Type: **[**IWiaTransferCallback**](-wia-iwiatransfercallback.md)\***

Specifies a pointer to the caller's [**IWiaTransferCallback**](-wia-iwiatransfercallback.md) interface.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>       |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Wiaguid.lib</dt> </dl> |



 

 
