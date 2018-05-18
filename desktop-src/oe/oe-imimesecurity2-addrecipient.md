---
title: IMimeSecurity2 AddRecipient method
description: Adds the specified recipient data to the message body.
ms.assetid: '0ca95d2e-1829-47b2-ba27-1bb80c340552'
keywords: ["AddRecipient method Windows Mail (formerly Outlook Express)", "AddRecipient method Windows Mail (formerly Outlook Express) , IMimeSecurity2 interface", "IMimeSecurity2 interface Windows Mail (formerly Outlook Express) , AddRecipient method"]
topic_type:
- apiref
api_name:
- IMimeSecurity2.AddRecipient
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeSecurity2::AddRecipient method

Adds the specified recipient data to the message body.

## Syntax


```C++
HRESULT AddRecipient(
  [in] DWORD               dwFlags,
  [in] DWORD               cRecipData,
  [in] PCMS_RECIPIENT_INFO recipData
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the value SMIME\_RECIPIENT\_REPLACE\_ALL.

</dd> <dt>

*cRecipData* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the number of [**CMS\_RECIPIENT\_INFO**](oe-cms-recipient-info.md) structures in *recipData*.

</dd> <dt>

*recipData* \[in\]
</dt> <dd>

Type: **PCMS\_RECIPIENT\_INFO**

Specifies a pointer to an array of [**CMS\_RECIPIENT\_INFO**](oe-cms-recipient-info.md) structures that contain the recipient information.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                      | Description                                                      |
|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                             | Indicates success. <br/>                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                     | Indicates that *dwFlags* or *recipData* is invalid. <br/>  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                    | Indicates that an attempt to allocate memory failed.<br/>  |
| <dl> <dt>**MIME\_E\_SECURITY\_NOTIMPLEMENTED**</dt> </dl> | Indicates that security information is not available.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





