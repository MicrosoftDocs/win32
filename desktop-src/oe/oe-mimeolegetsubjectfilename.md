---
title: MimeOleGetSubjectFileName function
description: Do not use. Returns E\_FAIL.
ms.assetid: 6ac8692c-3229-4c21-824a-c5ebb69ee99d
keywords:
- MimeOleGetSubjectFileName function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleGetSubjectFileName
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

# MimeOleGetSubjectFileName function

Do not use. Returns E\_FAIL.

## Syntax


```C++
HRESULT MimeOleGetSubjectFileName(
  _In_    IMimePropertySet *pPropertySet,
  _Out_   ULONG            *pulPart,
  _Out_   ULONG            *pulTotal,
  _Inout_ LPSTR            pszFileName,
  _In_    ULONG            cchMax
);
```



## Parameters

<dl> <dt>

*pPropertySet* \[in\]
</dt> <dd>

Type: **[**IMimePropertySet**](oe-imimepropertyset.md)\***

Not used.

</dd> <dt>

*pulPart* \[out\]
</dt> <dd>

Type: **ULONG\***

Not used.

</dd> <dt>

*pulTotal* \[out\]
</dt> <dd>

Type: **ULONG\***

Not used.

</dd> <dt>

*pszFileName* \[in, out\]
</dt> <dd>

Type: **LPSTR**

Not used.

</dd> <dt>

*cchMax* \[in\]
</dt> <dd>

Type: **ULONG**

Not used.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                            | Description                   |
|----------------------------------------------------------------------------------------|-------------------------------|
| <dl> <dt>**E\_FAIL**</dt> </dl> | Indicates failure.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





