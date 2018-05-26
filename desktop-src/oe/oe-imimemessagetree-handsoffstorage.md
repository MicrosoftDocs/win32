---
title: IMimeMessageTree HandsOffStorage method
description: Forces the object to release storage objects that it does not own.
ms.assetid: 8e235319-6489-41ee-84e5-6856730a5ffa
keywords:
- HandsOffStorage method Windows Mail (formerly Outlook Express)
- HandsOffStorage method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface
- IMimeMessageTree interface Windows Mail (formerly Outlook Express) , HandsOffStorage method
topic_type:
- apiref
api_name:
- IMimeMessageTree.HandsOffStorage
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

# IMimeMessageTree::HandsOffStorage method

Forces the object to release storage objects that it does not own.

## Syntax


```C++
HRESULT HandsOffStorage();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                       | Description                                                                                  |
|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | Indicates success.<br/>                                                                |
| <dl> <dt>**E\_FAIL**</dt> </dl>            | Indicates that an unknown error has occurred.<br/>                                     |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>     | Indicates that an attempt to allocate memory failed.<br/>                              |
| <dl> <dt>**STG\_E\_MEDIUMFULL**</dt> </dl> | Indicates that not enough disk space or memory is available to save the message. <br/> |



 

## Remarks

When a message is loaded through [IPersistStreamInit](http://msdn.microsoft.com/library/com/htm/cmi_n2p_64dw.asp) or [IPersistFile](http://msdn.microsoft.com/library/com/htm/cmi_n2p_99ph.asp), MimeOLE keeps a reference on the [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) or file, respectively, therefore keeping those resources open. A client can use this method to force the message object to release those resources.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





