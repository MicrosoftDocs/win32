---
title: MimeOleSMimeCapsToDlg function
description: Do not use. Outputs supplied Secure/Multipurpose Internet Mail Extensions (S/MIME) capabilities to supplied dialog.
ms.assetid: 'a2998610-a77a-4fa4-8a08-c7ab76140eac'
keywords: ["MimeOleSMimeCapsToDlg function Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- MimeOleSMimeCapsToDlg
api_location:
- Inetcomm.dll
api_type:
- DllExport
---

# MimeOleSMimeCapsToDlg function

Do not use. Outputs supplied Secure/Multipurpose Internet Mail Extensions (S/MIME) capabilities to supplied dialog.

## Syntax


```C++
HRESULT MimeOleSMimeCapsToDlg(
  _In_ LPBYTE     pbSMimeCaps,
  _In_ DWORD      cbSMimeCaps,
  _In_ DWORD      cCerts,
  _In_ PCX509CERT *rgCerts,
  _In_ HWND       hwndDlg,
  _In_ DWORD      idEncAlgs,
  _In_ DWORD      idSignAlgs,
  _In_ DWORD      idBlob
);
```



## Parameters

<dl> <dt>

*pbSMimeCaps* \[in\]
</dt> <dd>

Type: **LPBYTE**

Specifies pointer to the S/MIME capabilities array.

</dd> <dt>

*cbSMimeCaps* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies array length.

</dd> <dt>

*cCerts* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the number of certificates.

</dd> <dt>

*rgCerts* \[in\]
</dt> <dd>

Type: **PCX509CERT\***

Specifies the address of a pointer to a [CERT\_CONTEXT](http://msdn.microsoft.com/library/seccrypto/security/cert_context.asp) containing the certificates.

</dd> <dt>

*hwndDlg* \[in\]
</dt> <dd>

Type: **HWND**

Specifies a handle to the dialog window.

</dd> <dt>

*idEncAlgs* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies encryption algorithm combo box ID.

</dd> <dt>

*idSignAlgs* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies signature algorithm combo box ID.

</dd> <dt>

*idBlob* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a blob item checkbox ID.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                            | Description                                 |
|----------------------------------------------------------------------------------------|---------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Indicates success. <br/>              |
| <dl> <dt>**E\_FAIL**</dt> </dl> | Indicates that decoding failed. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





