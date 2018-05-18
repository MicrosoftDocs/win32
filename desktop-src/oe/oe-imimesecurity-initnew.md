---
title: IMimeSecurity InitNew method
description: Initializes an IMimeSecurity object.
ms.assetid: '819e365f-336c-4620-bc43-8828523af58e'
keywords: ["InitNew method Windows Mail (formerly Outlook Express)", "InitNew method Windows Mail (formerly Outlook Express) , IMimeSecurity interface", "IMimeSecurity interface Windows Mail (formerly Outlook Express) , InitNew method"]
topic_type:
- apiref
api_name:
- IMimeSecurity.InitNew
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeSecurity::InitNew method

Initializes an [**IMimeSecurity**](oe-imimesecurity.md) object.

## Syntax


```C++
HRESULT InitNew();
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



 

## Remarks

The client calls this method after the constructor.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





