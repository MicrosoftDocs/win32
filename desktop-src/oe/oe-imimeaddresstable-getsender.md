---
title: IMimeAddressTable GetSender method
description: Gets the address properties for the sender.
ms.assetid: 5ab741ac-4513-4a5f-a07f-31c9c62619fe
keywords:
- GetSender method Windows Mail (formerly Outlook Express)
- GetSender method Windows Mail (formerly Outlook Express) , IMimeAddressTable interface
- IMimeAddressTable interface Windows Mail (formerly Outlook Express) , GetSender method
topic_type:
- apiref
api_name:
- IMimeAddressTable.GetSender
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

# IMimeAddressTable::GetSender method

Gets the address properties for the sender.

## Syntax


```C++
HRESULT GetSender(
  [in, out] LPADDRESSPROPS pAddress
);
```



## Parameters

<dl> <dt>

*pAddress* \[in, out\]
</dt> <dd>

Type: **LPADDRESSPROPS**

Receives a pointer to the [**ADDRESSPROPS**](oe-addressprops.md) structure that contains the address properties. The client is responsible for freeing this structure by calling [**FreeAddressProps**](oe-imimeallocator-freeaddressprops.md).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                        | Description                                                     |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | Indicates success. <br/>                                  |
| <dl> <dt>**E\_FAIL**</dt> </dl>             | Indicates that an unknown error has occurred. <br/>       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Indicates that *pAddress* is **NULL**. <br/>              |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl> | Indicates that a sender address could not be found. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>      | Indicates that an attempt to allocate memory failed.<br/> |



 

## Remarks

The sender is computed by first using the value of the "From" header. If the "From" header does not exist, the value from the "Sender" header is used. If the "Sender" header does not exist, then this method returns MIME\_E\_NOT\_FOUND.

The client should initialize *pAddress*-&gt;**dwProps** before calling this method to specify which properties to return.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





