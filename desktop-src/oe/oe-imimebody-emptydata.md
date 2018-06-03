---
title: IMimeBody EmptyData method
description: Removes the data that is currently stored in the body. This method has no effect on the body header, for example, the property set.
ms.assetid: 8279911c-2081-455c-87d0-417d4519152c
keywords:
- EmptyData method Windows Mail (formerly Outlook Express)
- EmptyData method Windows Mail (formerly Outlook Express) , IMimeBody interface
- IMimeBody interface Windows Mail (formerly Outlook Express) , EmptyData method
topic_type:
- apiref
api_name:
- IMimeBody.EmptyData
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

# IMimeBody::EmptyData method

Removes the data that is currently stored in the body. This method has no effect on the body header, for example, the property set.

## Syntax


```C++
HRESULT EmptyData();
```



## Parameters

This method has no parameters.

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



 

 





