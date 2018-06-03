---
title: IMimeAllocator FreeAddressList method
description: Frees the contents of an ADDRESSLIST structure.
ms.assetid: 2a518147-8876-48c0-bbbf-f49e47e1c3b7
keywords:
- FreeAddressList method Windows Mail (formerly Outlook Express)
- FreeAddressList method Windows Mail (formerly Outlook Express) , IMimeAllocator interface
- IMimeAllocator interface Windows Mail (formerly Outlook Express) , FreeAddressList method
topic_type:
- apiref
api_name:
- IMimeAllocator.FreeAddressList
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

# IMimeAllocator::FreeAddressList method

Frees the contents of an [**ADDRESSLIST**](oe-addresslist.md) structure.

## Syntax


```C++
HRESULT FreeAddressList(
  [in, out] LPADDRESSLIST pList
);
```



## Parameters

<dl> <dt>

*pList* \[in, out\]
</dt> <dd>

Type: **LPADDRESSLIST**

Receives a pointer to the [**ADDRESSLIST**](oe-addresslist.md) structure to free.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                                                                                               |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                                                                                                             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pList* is **NULL** or that *pList*-&gt;**cAdrs** is greater than zero and *pList*-&gt;**prgAdr** is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





