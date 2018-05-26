---
title: IMimeSecurity2 CapabilitiesSupported method
description: Indicates the availability of various features.
ms.assetid: c311d082-5252-4aea-9d7e-84d3c6fc0bdc
keywords:
- CapabilitiesSupported method Windows Mail (formerly Outlook Express)
- CapabilitiesSupported method Windows Mail (formerly Outlook Express) , IMimeSecurity2 interface
- IMimeSecurity2 interface Windows Mail (formerly Outlook Express) , CapabilitiesSupported method
topic_type:
- apiref
api_name:
- IMimeSecurity2.CapabilitiesSupported
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

# IMimeSecurity2::CapabilitiesSupported method

Indicates the availability of various features.

## Syntax


```C++
HRESULT CapabilitiesSupported(
  [in, out] DWORD *pdwFeatures
);
```



## Parameters

<dl> <dt>

*pdwFeatures* \[in, out\]
</dt> <dd>

Type: **DWORD\***

Receives a pointer to a **DWORD** that contains a bitmask that indicates various features that are available.

<dl> <dt>

<span id="SMIME_SUPPORT_LABELS"></span><span id="smime_support_labels"></span>**SMIME\_SUPPORT\_LABELS** (0x00000001)
</dt> <dt>

<span id="SMIME_SUPPORT_RECEIPTS"></span><span id="smime_support_receipts"></span>**SMIME\_SUPPORT\_RECEIPTS** (0x00000002)
</dt> <dt>

<span id="SMIME_SUPPORT_MAILLIST"></span><span id="smime_support_maillist"></span>**SMIME\_SUPPORT\_MAILLIST** (0x00000004)
</dt> <dt>

<span id="SMIME_SUPPORT_KEY_AGREE"></span><span id="smime_support_key_agree"></span>**SMIME\_SUPPORT\_KEY\_AGREE** (0x00000008)
</dt> </dl> </dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





