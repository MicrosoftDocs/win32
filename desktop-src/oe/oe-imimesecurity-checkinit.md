---
title: IMimeSecurity CheckInit method
description: Checks whether an instance of the IMimeSecurity object has been successfully initialized.
ms.assetid: 95ce6a0b-4884-4433-8bad-2c580086458f
keywords:
- CheckInit method Windows Mail (formerly Outlook Express)
- CheckInit method Windows Mail (formerly Outlook Express) , IMimeSecurity interface
- IMimeSecurity interface Windows Mail (formerly Outlook Express) , CheckInit method
topic_type:
- apiref
api_name:
- IMimeSecurity.CheckInit
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

# IMimeSecurity::CheckInit method

Checks whether an instance of the [**IMimeSecurity**](oe-imimesecurity.md) object has been successfully initialized.

## Syntax


```C++
HRESULT CheckInit();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                               | Description                                                     |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                      | Indicates success. <br/>                                  |
| <dl> <dt>**MIME\_E\_SECURITY\_NOTINIT**</dt> </dl> | Indicates that the object has not been initialized. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





