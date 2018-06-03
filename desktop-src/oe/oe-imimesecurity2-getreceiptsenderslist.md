---
title: IMimeSecurity2 GetReceiptSendersList method
description: Gets an array of recipient names that send receipts.
ms.assetid: 560d875e-337e-46a4-8cb6-7abe02d882d9
keywords:
- GetReceiptSendersList method Windows Mail (formerly Outlook Express)
- GetReceiptSendersList method Windows Mail (formerly Outlook Express) , IMimeSecurity2 interface
- IMimeSecurity2 interface Windows Mail (formerly Outlook Express) , GetReceiptSendersList method
topic_type:
- apiref
api_name:
- IMimeSecurity2.GetReceiptSendersList
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

# IMimeSecurity2::GetReceiptSendersList method

Gets an array of recipient names that send receipts.

## Syntax


```C++
HRESULT GetReceiptSendersList(
  [in]  DWORD          dwFlags,
  [out] DWORD          *pcSendersList,
  [out] CERT_NAME_BLOB **rgSendersList
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> <dt>

*pcSendersList* \[out\]
</dt> <dd>

Type: **DWORD\***

Receives a pointer to a **DWORD** that contains the number of receipt senders in *rgSendersList*.

</dd> <dt>

*rgSendersList* \[out\]
</dt> <dd>

Type: **CERT\_NAME\_BLOB\*\***

Receives a pointer to an array of [CERT\_NAME\_BLOB](http://msdn.microsoft.com/library/seccrypto/security/cryptoapi_blob.asp) structures that contain the names of the receipt senders.

</dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                                   | Description                                               |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                            |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that no matching receipt was found. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





