---
title: MimeOleVariantFree function
description: Do not use. Frees any memory pointed to by the variant.
ms.assetid: c1da6884-5c1e-4587-87c6-e0e61ba6ba9c
keywords:
- MimeOleVariantFree function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleVariantFree
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

# MimeOleVariantFree function

Do not use. Frees any memory pointed to by the variant.

## Syntax


```C++
HRESULT MimeOleVariantFree(
  _Inout_ LPPROPVARIANT pProp
);
```



## Parameters

<dl> <dt>

*pProp* \[in, out\]
</dt> <dd>

Type: **LPPROPVARIANT**

Specifies [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072) structure.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                 |
|----------------------------------------------------------------------------------------------|---------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates invalid variant type. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





