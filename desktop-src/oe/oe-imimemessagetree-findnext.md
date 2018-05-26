---
title: IMimeMessageTree FindNext method
description: Finds the next body in the message tree that matches a specified content type.
ms.assetid: b27f93ec-361a-4332-a5b5-4c28e4a09623
keywords:
- FindNext method Windows Mail (formerly Outlook Express)
- FindNext method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface
- IMimeMessageTree interface Windows Mail (formerly Outlook Express) , FindNext method
topic_type:
- apiref
api_name:
- IMimeMessageTree.FindNext
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

# IMimeMessageTree::FindNext method

Finds the next body in the message tree that matches a specified content type.

## Syntax


```C++
HRESULT FindNext(
  [in, out] LPFINDBODY pFindBody,
  [out]     LPHBODY    phBody
);
```



## Parameters

<dl> <dt>

*pFindBody* \[in, out\]
</dt> <dd>

Type: **LPFINDBODY**

Specifies a pointer to a [**FINDBODY**](oe-findbody.md) structure that specifies the [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) of the body to find.

</dd> <dt>

*phBody* \[out\]
</dt> <dd>

Type: **LPHBODY**

Receives the handle of the body found.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                        | Description                                                     |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | Indicates success.<br/>                                   |
| <dl> <dt>**E\_FAIL**</dt> </dl>             | Indicates that an unknown error has occurred.<br/>        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Indicates that *pFindBody* or *phBody* is **NULL**. <br/> |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl> | Indicates that a body was not found. <br/>                |



 

## Remarks

The [**IMimeMessageTree::FindFirst**](oe-imimemessagetree-findfirst.md) and **IMimeMessageTree::FindNext** methods can be used to enumerate all the bodies in the message tree, or can be used to enumerate bodies that match a specified [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp).

If *pFindBody*-&gt;**pszPriType** and *pFindBody*-&gt;**pszSubType** are both **NULL**, all bodies are enumerated.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





