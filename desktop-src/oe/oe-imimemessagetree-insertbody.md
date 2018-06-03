---
title: IMimeMessageTree InsertBody method
description: Inserts a new, empty body into the message tree at the specified location.
ms.assetid: 2ff4681d-bc57-47fe-b27f-3b25d63cab98
keywords:
- InsertBody method Windows Mail (formerly Outlook Express)
- InsertBody method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface
- IMimeMessageTree interface Windows Mail (formerly Outlook Express) , InsertBody method
topic_type:
- apiref
api_name:
- IMimeMessageTree.InsertBody
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

# IMimeMessageTree::InsertBody method

Inserts a new, empty body into the message tree at the specified location.

## Syntax


```C++
HRESULT InsertBody(
  [in]  BODYLOCATION location,
  [in]  HBODY        hPivot,
  [out] LPHBODY      phBody
);
```



## Parameters

<dl> <dt>

*location* \[in\]
</dt> <dd>

Type: **[**BODYLOCATION**](oe-bodylocation.md)**

Specifies a [**BODYLOCATION**](oe-bodylocation.md) that indicates the insertion position relative to the body specified by the *hPivot* parameter.

</dd> <dt>

*hPivot* \[in\]
</dt> <dd>

Type: **HBODY**

Specifies the body to use as a relative location.

</dd> <dt>

*phBody* \[out\]
</dt> <dd>

Type: **LPHBODY**

Receives the handle of the new body.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                 | Description                                                                                                                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Indicates success.<br/>                                                                                                                                                                                                                            |
| <dl> <dt>**E\_FAIL**</dt> </dl>                      | Indicates that an unknown error has occurred.<br/>                                                                                                                                                                                                 |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                | Indicates that *location* is [**IBL\_PARENT**](oe-bodylocation.md). <br/>                                                                                                                                                                         |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>               | Indicates that an attempt to allocate memory failed.<br/>                                                                                                                                                                                          |
| <dl> <dt>**MIME\_E\_CANT\_RESET\_ROOT**</dt> </dl>   | Indicates that *location* is equal to [**IBL\_ROOT**](oe-bodylocation.md) and there is already a root body. <br/>                                                                                                                                 |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl>     | Indicates that *phBody* is an invalid handle. <br/>                                                                                                                                                                                                |
| <dl> <dt>**MIME\_E\_NOT\_MULTIPART**</dt> </dl>      | Indicates that *hPivot* is not a multipart body when *location* is [**IBL\_FIRST**](oe-bodylocation.md) or **IBL\_LAST**. Or, this return code indicates that *hPivot* has no parent when *location* is **IBL\_NEXT** or **IBL\_PREVIOUS**. <br/> |
| <dl> <dt>**MIME\_E\_BAD\_BODY\_LOCATION**</dt> </dl> | Indicates that the value of *location* is invalid. <br/>                                                                                                                                                                                           |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





