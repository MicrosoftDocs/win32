---
title: MimeOleClearDirtyTree function
description: Do not use. Clears dirty tree flag and any dirty body flags for the specified message tree object.
ms.assetid: a9d22522-3b0e-49d6-b125-820f48665e7f
keywords:
- MimeOleClearDirtyTree function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleClearDirtyTree
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MimeOleClearDirtyTree function

Do not use. Clears dirty tree flag and any dirty body flags for the specified message tree object.

## Syntax


```C++
HRESULT MimeOleClearDirtyTree(
  _In_ IMimeMessageTree *pTree
);
```



## Parameters

<dl> <dt>

*pTree* \[in\]
</dt> <dd>

Type: **[**IMimeMessageTree**](oe-imimemessagetree.md)\***

Specifies a pointer to the [**IMimeMessageTree**](oe-imimemessagetree.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                     |
|----------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pTree* is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





