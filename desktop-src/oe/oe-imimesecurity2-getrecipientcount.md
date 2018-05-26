---
title: IMimeSecurity2 GetRecipientCount method
description: Gets the number of recipients on the recipients list for the message.
ms.assetid: 30f81641-d570-40e0-9e7c-784e1d6cb169
keywords:
- GetRecipientCount method Windows Mail (formerly Outlook Express)
- GetRecipientCount method Windows Mail (formerly Outlook Express) , IMimeSecurity2 interface
- IMimeSecurity2 interface Windows Mail (formerly Outlook Express) , GetRecipientCount method
topic_type:
- apiref
api_name:
- IMimeSecurity2.GetRecipientCount
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMimeSecurity2::GetRecipientCount method

Gets the number of recipients on the recipients list for the message.

## Syntax


```C++
HRESULT GetRecipientCount(
  [in]  DWORD dwFlags,
  [out] DWORD *pdwRecipCount
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> <dt>

*pdwRecipCount* \[out\]
</dt> <dd>

Type: **DWORD\***

Receives a pointer to a **DWORD** that contains the number of recipients.

</dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                                  | Description                                               |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                            |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Indicates that an unknown error has occurred. <br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *dwFlags* is invalid. <br/>          |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





