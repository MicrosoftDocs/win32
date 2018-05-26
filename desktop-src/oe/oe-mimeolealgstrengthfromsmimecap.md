---
title: MimeOleAlgStrengthFromSMimeCap function
description: Do not use. Used to obtain the bit strength of an encryption algorithm.
ms.assetid: 0e493432-374f-4c3a-a09c-c28727d73543
keywords:
- MimeOleAlgStrengthFromSMimeCap function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleAlgStrengthFromSMimeCap
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MimeOleAlgStrengthFromSMimeCap function

Do not use. Used to obtain the bit strength of an encryption algorithm.

## Syntax


```C++
HRESULT MimeOleAlgStrengthFromSMimeCap(
  _In_  LPBYTE pb,
  _In_  DWORD  cb,
  _In_  BOOL   fEncryption,
  _Out_ DWORD  *pdwStrength
);
```



## Parameters

<dl> <dt>

*pb* \[in\]
</dt> <dd>

Type: **LPBYTE**

Specifies pointer to the S/MIME capabilities array.

</dd> <dt>

*cb* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies array length.

</dd> <dt>

*fEncryption* \[in\]
</dt> <dd>

Type: **BOOL**

Specifies whether to check the encryption algorithm.

</dd> <dt>

*pdwStrength* \[out\]
</dt> <dd>

Type: **DWORD\***

Returns the bit strength of algorithm used.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                         |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                      |
| <dl> <dt>**S\_FALSE**</dt> </dl>       | Indicates *pdwStrength* was checked for, but not found. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates allocation failed. <br/>                            |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





