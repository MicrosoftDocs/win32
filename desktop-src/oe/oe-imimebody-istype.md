---
title: IMimeBody IsType method
description: Queries the type of a body.
ms.assetid: 57eb83ca-3bdc-476b-a1ec-aee0e5cfe37c
keywords:
- IsType method Windows Mail (formerly Outlook Express)
- IsType method Windows Mail (formerly Outlook Express) , IMimeBody interface
- IMimeBody interface Windows Mail (formerly Outlook Express) , IsType method
topic_type:
- apiref
api_name:
- IMimeBody.IsType
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

# IMimeBody::IsType method

Queries the type of a body.

## Syntax


```C++
HRESULT IsType(
  [in] IMSGBODYTYPE bodytype
);
```



## Parameters

<dl> <dt>

*bodytype* \[in\]
</dt> <dd>

Type: **[**IMSGBODYTYPE**](oe-imsgbodytype.md)**

Specifies the [**IMSGBODYTYPE**](oe-imsgbodytype.md) to query.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                               | Description                                                                               |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                      | Indicates that the body type matches the type specified by *bodytype*.<br/>         |
| <dl> <dt>**S\_FALSE**</dt> </dl>                   | Indicates that the body type does not match the type specified by *bodytype*. <br/> |
| <dl> <dt>**MIME\_E\_INVALID\_BODYTYPE**</dt> </dl> | Indicates that *bodytype* specifies an invalid body type.<br/>                      |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





