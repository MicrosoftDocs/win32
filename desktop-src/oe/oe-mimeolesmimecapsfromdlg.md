---
title: MimeOleSMimeCapsFromDlg function
description: Do not use.
ms.assetid: e917688f-289c-44e4-9b64-7138d64479ac
keywords:
- MimeOleSMimeCapsFromDlg function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleSMimeCapsFromDlg
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

# MimeOleSMimeCapsFromDlg function

Do not use. Reads a combo box of encryption algorithm IDs (Using the handle passed in), to select a default encryption algorithm and reads a combo box of signature algorithm IDs to select a default signing algorithm. A list of capabilities for each is built from the combo box items. Without combo boxes, the defaults are 40-bit RC2 and SHA-1. Optionally, if a checkbox with a blob item ID is checked, the capabilities list is generated as a blob. The results are used to encode an Secure/Multipurpose Internet Mail Extensions (S/MIME) capabilities array object of the specified size.

## Syntax


```C++
HRESULT MimeOleSMimeCapsFromDlg(
  _In_    HWND   hwnd,
  _In_    DWORD  idEncAlgs,
  _In_    DWORD  idSignAlgs,
  _In_    DWORD  idBlob,
  _Inout_ LPBYTE pbSMimeCaps,
  _Inout_ DWORD  *pcbSmimeCaps
);
```



## Parameters

<dl> <dt>

*hwnd* \[in\]
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

</dd> <dt>

*pbSMimeCaps* \[in, out\]
</dt> <dd>

Type: **LPBYTE**

Specifies pointer to the S/MIME capabilities array.

</dd> <dt>

*pcbSmimeCaps* \[in, out\]
</dt> <dd>

Type: **DWORD\***

Returns array length.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                            | Description                                      |
|----------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Indicates capabilities list set. <br/>     |
| <dl> <dt>**E\_FAIL**</dt> </dl> | Indicates capabilities list not set. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





