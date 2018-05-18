---
title: MimeOleAlgNameFromSMimeCap function
description: Do not use. Obtains algorithm name from supplied Secure/Multipurpose Internet Mail Extensions (S/MIME) capabilities array.
ms.assetid: '4689523e-219f-40a4-82db-e6d197bfca7f'
keywords: ["MimeOleAlgNameFromSMimeCap function Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- MimeOleAlgNameFromSMimeCap
api_location:
- Inetcomm.dll
api_type:
- DllExport
---

# MimeOleAlgNameFromSMimeCap function

Do not use. Obtains algorithm name from supplied Secure/Multipurpose Internet Mail Extensions (S/MIME) capabilities array.

## Syntax


```C++
HRESULT MimeOleAlgNameFromSMimeCap(
  _In_  LPBYTE pb,
  _In_  DWORD  cb,
  _Out_ LPCSTR *ppzProtocol
);
```



## Parameters

<dl> <dt>

*pb* \[in\]
</dt> <dd>

Type: **LPBYTE**

Pointer to a S/MIME capabilities array.

</dd> <dt>

*cb* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies array length.

</dd> <dt>

*ppzProtocol* \[out\]
</dt> <dd>

Type: **LPCSTR\***

Returns address of pointer to algorithm name string.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                             | Description                    |
|-----------------------------------------------------------------------------------------|--------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Indicates success. <br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates failure. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





