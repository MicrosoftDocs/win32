---
title: IMimeMessageTree DeleteBodyProp method
description: Deletes a property from a specified body.
ms.assetid: 54f699bf-b91e-42d5-9a90-6bd25959505b
keywords:
- DeleteBodyProp method Windows Mail (formerly Outlook Express)
- DeleteBodyProp method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface
- IMimeMessageTree interface Windows Mail (formerly Outlook Express) , DeleteBodyProp method
topic_type:
- apiref
api_name:
- IMimeMessageTree.DeleteBodyProp
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

# IMimeMessageTree::DeleteBodyProp method

Deletes a property from a specified body.

## Syntax


```C++
HRESULT DeleteBodyProp(
  [in] HBODY  hBody,
  [in] LPCSTR pszName
);
```



## Parameters

<dl> <dt>

*hBody* \[in\]
</dt> <dd>

Type: **HBODY**

Specifies the handle of the body. Use HBODY\_ROOT (0xffffffff) to indicate the root body.

</dd> <dt>

*pszName* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the property name or ID.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                                                                                         |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success. <br/>                                                                                                      |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | Indicates that an unknown error has occurred. <br/>                                                                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates that *hBody* or *pszName* is **NULL**. <br/>                                                                        |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl>      | Indicates that *pszName* does not specify an existing property. <br/>                                                         |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl>        | Indicates that *hBody* is equal to HBODY\_ROOT (0xffffffff) and there is no root body or that the property has no data. <br/> |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *hBody* is an invalid handle. <br/>                                                                            |



 

## Remarks

A property ID can also be passed into this method through the *pszName* parameter using the PIDTOSTR macro.

This method is equivalent to:

pMessageTree-&gt;[**BindToObject**](oe-imimemessagetree-bindtoobject.md)(*hBody*, IID\_IMimePropertySet, (LPVOID \*)&pPropertySet);

pPropertySet-&gt;[**DeleteProp**](oe-imimepropertyset-deleteprop.md)(*pszName*);

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





