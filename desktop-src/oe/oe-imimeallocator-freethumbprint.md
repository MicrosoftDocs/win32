---
title: IMimeAllocator FreeThumbprint method
description: Frees the contents of an THUMBBLOB structure.
ms.assetid: 816e6d1f-7a6b-4dd0-b4d1-01aefddf9f96
keywords:
- FreeThumbprint method Windows Mail (formerly Outlook Express)
- FreeThumbprint method Windows Mail (formerly Outlook Express) , IMimeAllocator interface
- IMimeAllocator interface Windows Mail (formerly Outlook Express) , FreeThumbprint method
topic_type:
- apiref
api_name:
- IMimeAllocator.FreeThumbprint
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

# IMimeAllocator::FreeThumbprint method

Frees the contents of an [THUMBBLOB](http://msdn.microsoft.com/library/winsock/winsock/blob_2.asp) structure.

## Syntax


```C++
HRESULT FreeThumbprint(
  [in] THUMBBLOB *pthumbprint
);
```



## Parameters

<dl> <dt>

*pthumbprint* \[in\]
</dt> <dd>

Type: **THUMBBLOB\***

Receives a pointer to the [THUMBBLOB](http://msdn.microsoft.com/library/winsock/winsock/blob_2.asp) structure to free.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns the following value.



| Return code                                                                          | Description                   |
|--------------------------------------------------------------------------------------|-------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | Indicates success.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





