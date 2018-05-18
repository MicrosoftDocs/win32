---
title: IMimeBody SetDisplayName method
description: Sets the display name for the body. MimeOLE always appends the size of the body to the end of the display name; for example, \ 0034;Display Name (560 KB) \ 0034;.
ms.assetid: '74d80caf-a5ff-466f-8ca3-1d85ef6a6bcb'
keywords: ["SetDisplayName method Windows Mail (formerly Outlook Express)", "SetDisplayName method Windows Mail (formerly Outlook Express) , IMimeBody interface", "IMimeBody interface Windows Mail (formerly Outlook Express) , SetDisplayName method"]
topic_type:
- apiref
api_name:
- IMimeBody.SetDisplayName
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeBody::SetDisplayName method

Sets the display name for the body. MimeOLE always appends the size of the body to the end of the display name; for example, "Display Name (560 KB)".

## Syntax


```C++
HRESULT SetDisplayName(
  [in] LPCSTR pszDisplay
);
```



## Parameters

<dl> <dt>

*pszDisplay* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the display name.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pszDisplay* is **NULL**. <br/>            |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





