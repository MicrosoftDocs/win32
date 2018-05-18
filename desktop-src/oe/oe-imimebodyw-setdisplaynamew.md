---
title: IMimeBodyW SetDisplayNameW method
description: Sets the display name for the body. MimeOLE always appends the size of the body to the end of the display name (for example, \ 0034;Display Name (560 KB) \ 0034;).
ms.assetid: '98a1d433-3735-46be-8719-228bdce601d8'
keywords: ["SetDisplayNameW method Windows Mail (formerly Outlook Express)", "SetDisplayNameW method Windows Mail (formerly Outlook Express) , IMimeBodyW interface", "IMimeBodyW interface Windows Mail (formerly Outlook Express) , SetDisplayNameW method"]
topic_type:
- apiref
api_name:
- IMimeBodyW.SetDisplayNameW
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeBodyW::SetDisplayNameW method

Sets the display name for the body. MimeOLE always appends the size of the body to the end of the display name (for example, "Display Name (560 KB)").

## Syntax


```C++
HRESULT SetDisplayNameW(
  [in] LPCWSTR pwszDisplay
);
```



## Parameters

<dl> <dt>

*pwszDisplay* \[in\]
</dt> <dd>

Type: **LPCWSTR**

Specifies the display name.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pwszDisplay* is **NULL**. <br/>           |
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



 

 





