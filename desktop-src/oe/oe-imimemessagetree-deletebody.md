---
title: IMimeMessageTree DeleteBody method
description: Deletes a body from the message tree.
ms.assetid: 86e06cf6-2e82-4af8-a80f-7b44f85c17f0
keywords:
- DeleteBody method Windows Mail (formerly Outlook Express)
- DeleteBody method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface
- IMimeMessageTree interface Windows Mail (formerly Outlook Express) , DeleteBody method
topic_type:
- apiref
api_name:
- IMimeMessageTree.DeleteBody
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

# IMimeMessageTree::DeleteBody method

Deletes a body from the message tree.

## Syntax


```C++
HRESULT DeleteBody(
  [in] HBODY hBody,
  [in] DWORD dwFlags
);
```



## Parameters

<dl> <dt>

*hBody* \[in\]
</dt> <dd>

Type: **HBODY**

Specifies the handle of the body to delete.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a value that indicates how to do the deletion when the body specified by *hBody* is multipart.



| Value                                                                                                                                                                                                                                                        | Meaning                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DELETE_PROMOTE_CHILDREN"></span><span id="delete_promote_children"></span><dl> <dt>**DELETE\_PROMOTE\_CHILDREN**</dt> <dt>0x00000001</dt> </dl> | Indicates that the children of the specified body should not be deleted and instead should be promoted one level in the message tree.<br/> |
| <span id="DELETE_CHILDREN_ONLY"></span><span id="delete_children_only"></span><dl> <dt>**DELETE\_CHILDREN\_ONLY**</dt> <dt>0x00000002</dt> </dl>          | Indicates that only the children of the specified body should be deleted.<br/>                                                             |



 

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                   | Description                                                     |
|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                          | Indicates success.<br/>                                   |
| <dl> <dt>**E\_FAIL**</dt> </dl>                        | Indicates that an unknown error has occurred.<br/>        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                  | Indicates that *hBody* is **NULL**. <br/>                 |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl>       | Indicates that *hBody* is an invalid handle. <br/>        |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                 | Indicates that an attempt to allocate memory failed.<br/> |
| <dl> <dt>**MIME\_E\_INVALID\_DELETE\_TYPE**</dt> </dl> | Indicates that the deletion could not be performed. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





