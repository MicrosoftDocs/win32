---
title: IMimeBodyW GetDisplayNameW method
description: Gets the display name for the body. If a display name is set, MimeOLE generates a display name based on the content of the body.
ms.assetid: 'ddaaf0a4-6182-4209-8c6b-6a8ad1575949'
keywords: ["GetDisplayNameW method Windows Mail (formerly Outlook Express)", "GetDisplayNameW method Windows Mail (formerly Outlook Express) , IMimeBodyW interface", "IMimeBodyW interface Windows Mail (formerly Outlook Express) , GetDisplayNameW method"]
topic_type:
- apiref
api_name:
- IMimeBodyW.GetDisplayNameW
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeBodyW::GetDisplayNameW method

Gets the display name for the body. If a display name is set, MimeOLE generates a display name based on the content of the body.

## Syntax


```C++
HRESULT GetDisplayNameW(
  [out] LPWSTR *ppwszDisplay
);
```



## Parameters

<dl> <dt>

*ppwszDisplay* \[out\]
</dt> <dd>

Type: **LPWSTR\***

Receives a pointer to a **LPWSTR** that contains the display name. The client is responsible for freeing this pointer by calling [IMalloc::Free](http://msdn.microsoft.com/library/com/htm/cmi_m_1smd.asp).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                      | Description                                                     |
|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>             | Indicates success.<br/>                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>     | Indicates that *ppwszDisplay* is **NULL**.<br/>           |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>    | Indicates that an attempt to allocate memory failed.<br/> |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl> | Indicates that there is no display name.<br/>             |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





