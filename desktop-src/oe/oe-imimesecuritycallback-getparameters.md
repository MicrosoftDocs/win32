---
title: IMimeSecurityCallback GetParameters method
description: IMimeSecurityCallback GetParameters method
ms.assetid: e033c3c8-357b-4ffa-9c8b-5c9afbbc9fa1
keywords:
- GetParameters method Windows Mail (formerly Outlook Express)
- GetParameters method Windows Mail (formerly Outlook Express) , IMimeSecurityCallback interface
- IMimeSecurityCallback interface Windows Mail (formerly Outlook Express) , GetParameters method
topic_type:
- apiref
api_name:
- IMimeSecurityCallback.GetParameters
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

# IMimeSecurityCallback::GetParameters method

\[**IMimeSecurityCallback::GetParameters** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

## Syntax


```C++
HRESULT GetParameters(
  [in]      PCCERT_CONTEXT pccert,
  [in]      HCERTSTORE     hstoreMsg,
  [in, out] DWORD          *pcbParams,
  [in, out] BYTE           **pbParams
);
```



## Parameters

<dl> <dt>

*pccert* \[in\]
</dt> <dd>

Type: **PCCERT\_CONTEXT**

</dd> <dt>

*hstoreMsg* \[in\]
</dt> <dd>

Type: **HCERTSTORE**

</dd> <dt>

*pcbParams* \[in, out\]
</dt> <dd>

Type: **DWORD\***

</dd> <dt>

*pbParams* \[in, out\]
</dt> <dd>

Type: **BYTE\*\***

</dd> </dl>

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
| IDL<br/>                      | <dl> <dt>Mimeolepriv.idl</dt> </dl>                     |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





