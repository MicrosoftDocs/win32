---
title: IPersistMime Load method
description: Loads an IMimeMessage object.
ms.assetid: a80adbb0-fa71-4740-864b-b814ad0f48fb
keywords:
- Load method Windows Mail (formerly Outlook Express)
- Load method Windows Mail (formerly Outlook Express) , IPersistMime interface
- IPersistMime interface Windows Mail (formerly Outlook Express) , Load method
topic_type:
- apiref
api_name:
- IPersistMime.Load
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPersistMime::Load method

\[**IPersistMime::Load** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Loads an [**IMimeMessage**](oe-imimemessage.md) object.

## Syntax


```C++
HRESULT Load(
  [in] IMimeMessage *pMsg
);
```



## Parameters

<dl> <dt>

*pMsg* \[in\]
</dt> <dd>

Type: **[**IMimeMessage**](oe-imimemessage.md)\***

Specifies the message to load.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                    |
|----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                 |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pMsg* is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





