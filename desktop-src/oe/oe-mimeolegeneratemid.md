---
title: MimeOleGenerateMID function
description: Do not use. Creates a message ID as a string.
ms.assetid: f06bc048-39b3-46ad-8aed-a515909bb461
keywords:
- MimeOleGenerateMID function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleGenerateMID
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MimeOleGenerateMID function

Do not use. Creates a message ID as a string.

## Syntax


```C++
HRESULT MimeOleGenerateMID(
  _Inout_ LPSTR   pszMID,
  _In_    ULONG   cchMax,
  _In_    boolean fAbsolute
);
```



## Parameters

<dl> <dt>

*pszMID* \[in, out\]
</dt> <dd>

Type: **LPSTR**

Specifies address of string into which message ID is saved. If relative, then prepend "MID:" to the message ID and include the beginning and ending angle brackets in the string.

</dd> <dt>

*cchMax* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies the output buffer size.

</dd> <dt>

*fAbsolute* \[in\]
</dt> <dd>

Type: **boolean**

Specifies whether returned *pszMID* is absolute or relative.

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



 

 





