---
title: IMimeMessage GetAddressTable method
description: Gets an IMimeAddressTable object for the message.
ms.assetid: 097941e5-1bb0-4905-a1ff-0520f5371f85
keywords:
- GetAddressTable method Windows Mail (formerly Outlook Express)
- GetAddressTable method Windows Mail (formerly Outlook Express) , IMimeMessage interface
- IMimeMessage interface Windows Mail (formerly Outlook Express) , GetAddressTable method
topic_type:
- apiref
api_name:
- IMimeMessage.GetAddressTable
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

# IMimeMessage::GetAddressTable method

Gets an [**IMimeAddressTable**](oe-imimeaddresstable.md) object for the message.

## Syntax


```C++
HRESULT GetAddressTable(
  [out] IMimeAddressTable **ppTable
);
```



## Parameters

<dl> <dt>

*ppTable* \[out\]
</dt> <dd>

Type: **[**IMimeAddressTable**](oe-imimeaddresstable.md)\*\***

Receives the address of a pointer to an [**IMimeAddressTable**](oe-imimeaddresstable.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                      |
|----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *ppTable* is **NULL**.<br/> |



 

## Remarks

This method is equivalent to:

pMessage-&gt;[**BindToObject**](oe-imimemessagetree-bindtoobject.md)(HBODY\_ROOT, IID\_IMimeAddressTable, (LPVOID \*)&pAddressTable);

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





