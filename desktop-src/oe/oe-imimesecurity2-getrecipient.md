---
title: IMimeSecurity2 GetRecipient method
description: Gets encoding information for the specified set of recipients.
ms.assetid: f8009f1c-ad1a-44ff-b258-dc8f2a15b00d
keywords:
- GetRecipient method Windows Mail (formerly Outlook Express)
- GetRecipient method Windows Mail (formerly Outlook Express) , IMimeSecurity2 interface
- IMimeSecurity2 interface Windows Mail (formerly Outlook Express) , GetRecipient method
topic_type:
- apiref
api_name:
- IMimeSecurity2.GetRecipient
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMimeSecurity2::GetRecipient method

Gets encoding information for the specified set of recipients.

## Syntax


```C++
HRESULT GetRecipient(
  [in]      DWORD               dwFlags,
  [in]      DWORD               iRecipient,
  [in]      DWORD               cRecipients,
  [in, out] PCMS_RECIPIENT_INFO pRecipData
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> <dt>

*iRecipient* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the index of recipient information to return from the message body.

</dd> <dt>

*cRecipients* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the number of [**CMS\_RECIPIENT\_INFO**](oe-cms-recipient-info.md) structures to return, starting at the index specified by *iRecipient*.

</dd> <dt>

*pRecipData* \[in, out\]
</dt> <dd>

Type: **PCMS\_RECIPIENT\_INFO**

Receives a pointer to an array of [**CMS\_RECIPIENT\_INFO**](oe-cms-recipient-info.md) structures that contain the recipient information.

</dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                                   | Description                                                          |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *iRecipient* or *cRecipients* is invalid. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/>     |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





