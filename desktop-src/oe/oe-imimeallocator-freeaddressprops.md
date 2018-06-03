---
title: IMimeAllocator FreeAddressProps method
description: Frees the contents of an ADDRESSPROPS structure.
ms.assetid: 3d1f3218-5d5e-49f8-9101-6cc885a6df4d
keywords:
- FreeAddressProps method Windows Mail (formerly Outlook Express)
- FreeAddressProps method Windows Mail (formerly Outlook Express) , IMimeAllocator interface
- IMimeAllocator interface Windows Mail (formerly Outlook Express) , FreeAddressProps method
topic_type:
- apiref
api_name:
- IMimeAllocator.FreeAddressProps
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMimeAllocator::FreeAddressProps method

Frees the contents of an [**ADDRESSPROPS**](oe-addressprops.md) structure.

## Syntax


```C++
HRESULT FreeAddressProps(
  [in, out] LPADDRESSPROPS pAddress
);
```



## Parameters

<dl> <dt>

*pAddress* \[in, out\]
</dt> <dd>

Type: **LPADDRESSPROPS**

Receives a pointer to the [**ADDRESSPROPS**](oe-addressprops.md) structure to free.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                        |
|----------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pAddress* is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





