---
title: IMimeSecurity2 DeleteRecipient method
description: Currently, not available for use.
ms.assetid: '13fc0cb9-eab0-48cf-9923-103766a0af3d'
keywords: ["DeleteRecipient method Windows Mail (formerly Outlook Express)", "DeleteRecipient method Windows Mail (formerly Outlook Express) , IMimeSecurity2 interface", "IMimeSecurity2 interface Windows Mail (formerly Outlook Express) , DeleteRecipient method"]
topic_type:
- apiref
api_name:
- IMimeSecurity2.DeleteRecipient
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeSecurity2::DeleteRecipient method

Currently, not available for use.

## Syntax


```C++
HRESULT DeleteRecipient(
  [in] DWORD dwFlags,
  [in] DWORD iRecipent,
  [in] DWORD cRecipients
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> <dt>

*iRecipent* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the index in the array of [**CMS\_RECIPIENT\_INFO**](oe-cms-recipient-info.md) structures to begin deleting.

</dd> <dt>

*cRecipients* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the number of [**CMS\_RECIPIENT\_INFO**](oe-cms-recipient-info.md) structures to delete from the array.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





