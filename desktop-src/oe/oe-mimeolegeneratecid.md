---
title: MimeOleGenerateCID function
description: Do not use. Creates a content ID as a string.
ms.assetid: 0980da1b-e7fe-4f80-86a8-36a03a725a6f
keywords:
- MimeOleGenerateCID function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleGenerateCID
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

# MimeOleGenerateCID function

Do not use. Creates a content ID as a string.

## Syntax


```C++
HRESULT MimeOleGenerateCID(
  _Inout_ LPSTR   pszCID,
  _In_    ULONG   cchMax,
  _In_    boolean fAbsolute
);
```



## Parameters

<dl> <dt>

*pszCID* \[in, out\]
</dt> <dd>

Type: **LPSTR**

Specifies address of string into which content ID is saved. If absolute, then prepend "CID:" to the content ID.

</dd> <dt>

*cchMax* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies the output buffer size.

</dd> <dt>

*fAbsolute* \[in\]
</dt> <dd>

Type: **boolean**

Specifies whether returned *pszCID* is absolute or relative.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                              |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that pointer argument is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





