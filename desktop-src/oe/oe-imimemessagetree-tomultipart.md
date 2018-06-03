---
title: IMimeMessageTree ToMultipart method
description: Converts a non-multipart body to a multipart body.
ms.assetid: b7a633a7-1469-474a-bcd8-1a18595f1354
keywords:
- ToMultipart method Windows Mail (formerly Outlook Express)
- ToMultipart method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface
- IMimeMessageTree interface Windows Mail (formerly Outlook Express) , ToMultipart method
topic_type:
- apiref
api_name:
- IMimeMessageTree.ToMultipart
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

# IMimeMessageTree::ToMultipart method

Converts a non-multipart body to a multipart body.

## Syntax


```C++
HRESULT ToMultipart(
  [in]  HBODY   hBody,
  [in]  LPCSTR  pszSubType,
  [out] LPHBODY phMultipart
);
```



## Parameters

<dl> <dt>

*hBody* \[in\]
</dt> <dd>

Type: **HBODY**

Specifies the handle of the body to convert.

</dd> <dt>

*pszSubType* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the secondary multipart [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp); for example, `mixed` or `related`.

</dd> <dt>

*phMultipart* \[out\]
</dt> <dd>

Type: **LPHBODY**

Receives the handle of the new body that was created as a child of *hBody*.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                                                        |
|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success.<br/>                                                                      |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | Indicates that an unknown error has occurred.<br/>                                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates that *hBody* or *pszSubType* is **NULL**. <br/>                                    |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl>        | Indicates that *hBody* is equal to HBODY\_ROOT (0xffffffff) and there is no root body. <br/> |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *hBody* is an invalid handle. <br/>                                           |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>           | Indicates that an attempt to allocate memory failed.<br/>                                    |



 

## Remarks

This method creates a body that is a child of *hBody* and copies the contents of *hBody* into the new body. The [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) for *hBody* is set to "multipart/*pszSubType*".

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





