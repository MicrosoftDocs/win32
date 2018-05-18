---
title: MimeOleSMimeCapsFull function
description: Do not use.
ms.assetid: 'f9e9d8f4-3563-4701-878d-3d3a0cc84b68'
keywords: ["MimeOleSMimeCapsFull function Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- MimeOleSMimeCapsFull
api_location:
- Inetcomm.dll
api_type:
- DllExport
---

# MimeOleSMimeCapsFull function

Do not use. Builds a list of encryption capabilities (if all encryption algorithms are to be supported) from the passed-in cookie, or defaults to 40-bit RC2. Similarly, if all signature algorithms are to be supported, builds a list of signing capabilities from the cookie, or defaults to SHA-1. The results are used to encode an Secure/Multipurpose Internet Mail Extensions (S/MIME) capabilities array object of the specified size.

## Syntax


```C++
HRESULT MimeOleSMimeCapsFull(
  _In_    LPVOID pv,
  _In_    BOOL   fFullEncryption,
  _In_    BOOL   fFullSigning,
  _Inout_ LPBYTE pbSymCaps,
  _Inout_ DWORD  *pcbSymCaps
);
```



## Parameters

<dl> <dt>

*pv* \[in\]
</dt> <dd>

Type: **LPVOID**

Specifies cookie containing capabilities.

</dd> <dt>

*fFullEncryption* \[in\]
</dt> <dd>

Type: **BOOL**

Specifies whether all encryption algorithms are to be supported.

</dd> <dt>

*fFullSigning* \[in\]
</dt> <dd>

Type: **BOOL**

Specifies whether all signature algorithms are to be supported.

</dd> <dt>

*pbSymCaps* \[in, out\]
</dt> <dd>

Type: **LPBYTE**

Specifies pointer to the S/MIME capabilities array.

</dd> <dt>

*pcbSymCaps* \[in, out\]
</dt> <dd>

Type: **DWORD\***

Returns array length.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                            | Description                                             |
|----------------------------------------------------------------------------------------|---------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Indicates encryption capabilities list set. <br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl> | Indicates capabilities list not set. <br/>        |



 

## Remarks

This function call is memory-intensive, and the results are always the same during a session. (They can only change with software upgrade.) Cache the results for better performance.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





