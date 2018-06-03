---
title: IMimeMessageTree GetBody method
description: Gets the handle of a body from the message tree relative to another specified body.
ms.assetid: 27163938-f63e-4b9d-b661-a2819eb1e60a
keywords:
- GetBody method Windows Mail (formerly Outlook Express)
- GetBody method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface
- IMimeMessageTree interface Windows Mail (formerly Outlook Express) , GetBody method
topic_type:
- apiref
api_name:
- IMimeMessageTree.GetBody
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

# IMimeMessageTree::GetBody method

Gets the handle of a body from the message tree relative to another specified body.

## Syntax


```C++
HRESULT GetBody(
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

Specifies a [**BODYLOCATION**](oe-bodylocation.md) at which to get a body handle. The position is relative to the body specified by the *hPivot* parameter.

</dd> <dt>

*hPivot* \[in\]
</dt> <dd>

Type: **HBODY**

Specifies the body to use as a relative location.

</dd> <dt>

*phBody* \[out\]
</dt> <dd>

Type: **LPHBODY**

Receives the handle of the body at the specified location.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                 | Description                                                                                                    |
|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Indicates success.<br/>                                                                                  |
| <dl> <dt>**E\_FAIL**</dt> </dl>                      | Indicates that an unknown error has occurred.<br/>                                                       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                | Indicates that *location* is [**IBL\_PARENT**](oe-bodylocation.md), or that *phBody* is **NULL**. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>               | Indicates that an attempt to allocate memory failed.<br/>                                                |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl>          | Indicates that there is not a body at the specified location. <br/>                                      |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl>     | Indicates that *hPivot* is an invalid handle. <br/>                                                      |
| <dl> <dt>**MIME\_E\_BAD\_BODY\_LOCATION**</dt> </dl> | Indicates that the value of *location* is invalid. <br/>                                                 |



 

## Examples

The following example shows how to recursively enumerate the message tree.


```C++
pTree->GetBody(IBL_ROOT, &amp;hRoot);
RecurseMessageTree(pTree, hRoot);

void RecurseMessageTree(IMimeMessageTree *pTree, HBODY hBody)
{
   // Locals
   HBODY hChild;

   // If hBody is a multipart body, recurse its children.
   if (S_OK == pTree->IsContentType(hBody, STR_CNT_MULTIPART, NULL))
   {
      // Loop through the children.
      if (SUCCEEDED(pTree->GetBody(IBL_FIRST, hBody, &amp;hChild)))
      {
         // Loop through the children.
         do
         {
            // Recurse
            RecurseMessageTree(pTree, hChild);
         } 
         while (SUCCEEDED(pTree->GetBody(IBL_NEXT, hChild, &amp;hChild);
      }
   }

   // Process hBody...
}
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





