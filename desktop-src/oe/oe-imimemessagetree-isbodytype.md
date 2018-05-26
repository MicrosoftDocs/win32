---
title: IMimeMessageTree IsBodyType method
description: Queries the type of a specified body.
ms.assetid: f319a9dc-4a01-460b-99d6-ee979c677c60
keywords:
- IsBodyType method Windows Mail (formerly Outlook Express)
- IsBodyType method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface
- IMimeMessageTree interface Windows Mail (formerly Outlook Express) , IsBodyType method
topic_type:
- apiref
api_name:
- IMimeMessageTree.IsBodyType
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

# IMimeMessageTree::IsBodyType method

Queries the type of a specified body.

## Syntax


```C++
HRESULT IsBodyType(
  [in] HBODY        hBody,
  [in] IMSGBODYTYPE bodytype
);
```



## Parameters

<dl> <dt>

*hBody* \[in\]
</dt> <dd>

Type: **HBODY**

Specifies the handle of the body. Use HBODY\_ROOT (0xffffffff) to indicate the root body.

</dd> <dt>

*bodytype* \[in\]
</dt> <dd>

Type: **[**IMSGBODYTYPE**](oe-imsgbodytype.md)**

Specifies an [**IMSGBODYTYPE**](oe-imsgbodytype.md) value.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                               | Description                                                                                        |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                      | Indicates that the body type matches the type specified by *bodytype*.<br/>                  |
| <dl> <dt>**S\_FALSE**</dt> </dl>                   | Indicates that the body type does not match the type specified by *bodytype*. <br/>          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>              | Indicates that *hBody* is **NULL**. <br/>                                                    |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl>          | Indicates that *hBody* is equal to HBODY\_ROOT (0xffffffff) and there is no root body. <br/> |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl>   | Indicates that *hBody* is an invalid handle. <br/>                                           |
| <dl> <dt>**MIME\_E\_INVALID\_BODYTYPE**</dt> </dl> | Indicates that *bodytype* specifies an invalid body type.<br/>                               |



 

## Remarks

This method is equivalent to:

pMessageTree-&gt;[**BindToObject**](oe-imimemessagetree-bindtoobject.md)(*hBody*, IID\_IMimeBody, (LPVOID \*)&pBody);

pBody-&gt;[**IsType**](oe-imimebody-istype.md)(*bodytype*);

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





