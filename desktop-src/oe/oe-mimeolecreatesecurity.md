---
title: MimeOleCreateSecurity function
description: Do not use. On success, creates a new Secure/Multipurpose Internet Mail Extensions (S/MIME) object.
ms.assetid: 'fba5030c-95cb-440f-ad60-6194d73b9318'
keywords: ["MimeOleCreateSecurity function Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- MimeOleCreateSecurity
api_location:
- Inetcomm.dll
api_type:
- DllExport
---

# MimeOleCreateSecurity function

Do not use. On success, creates a new Secure/Multipurpose Internet Mail Extensions (S/MIME) object.

## Syntax


```C++
HRESULT MimeOleCreateSecurity(
  _Out_ IMimeSecurity **ppSecurity
);
```



## Parameters

<dl> <dt>

*ppSecurity* \[out\]
</dt> <dd>

Type: **[**IMimeSecurity**](oe-imimesecurity.md)\*\***

Receives pointer to address of new S/MIME object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                              |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that pointer argument is **NULL**. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that memory allocation failed. <br/>     |



 

## Remarks

> [!Note]  
> User is responsible for freeing S/MIME object.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





