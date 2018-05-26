---
title: IMimeMessageTree IsContentType method
description: Queries the Content-Type of a specified body.
ms.assetid: 5ef72e1a-ee97-4994-8ca1-da44b47cc6e3
keywords:
- IsContentType method Windows Mail (formerly Outlook Express)
- IsContentType method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface
- IMimeMessageTree interface Windows Mail (formerly Outlook Express) , IsContentType method
topic_type:
- apiref
api_name:
- IMimeMessageTree.IsContentType
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

# IMimeMessageTree::IsContentType method

Queries the [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) of a specified body.

## Syntax


```C++
HRESULT IsContentType(
  [in] HBODY  hBody,
  [in] LPCSTR pszPriType,
  [in] LPCSTR pszSubType
);
```



## Parameters

<dl> <dt>

*hBody* \[in\]
</dt> <dd>

Type: **HBODY**

Specifies the handle of the body. Use HBODY\_ROOT (0xffffffff) to indicate the root body.

</dd> <dt>

*pszPriType* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the primary [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp); for example, multipart or text.

</dd> <dt>

*pszSubType* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the secondary [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp); for example, mixed or html.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates that the [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) of the specified body matches the specified types or that both *pszPriType* and *pszSubType* are **NULL**.<br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl>                 | Indicates that the [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) of the specified body does not match the specified types. <br/>                                                 |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates that *hBody* is **NULL**. <br/>                                                                                                                                                                                                       |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl>        | Indicates that *hBody* is equal to HBODY\_ROOT (0xffffffff) and there is no root body. <br/>                                                                                                                                                    |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *hBody* is an invalid handle. <br/>                                                                                                                                                                                              |



 

## Remarks

This method is equivalent to:

pMessageTree-&gt;[**BindToObject**](oe-imimemessagetree-bindtoobject.md)(*hBody*, IID\_IMimePropertySet, (LPVOID \*)&pPropertySet);

pPropertySet-&gt;[**IsContentType**](oe-imimepropertyset-iscontenttype.md)(*pszPriType*, *pszSubType*);

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





