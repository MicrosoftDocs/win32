---
title: IMimeSecurityCallback FindKeyFor method
description: IMimeSecurityCallback FindKeyFor method
ms.assetid: 4a108aa2-7fe7-4153-b900-013ae910e42c
keywords:
- FindKeyFor method Windows Mail (formerly Outlook Express)
- FindKeyFor method Windows Mail (formerly Outlook Express) , IMimeSecurityCallback interface
- IMimeSecurityCallback interface Windows Mail (formerly Outlook Express) , FindKeyFor method
topic_type:
- apiref
api_name:
- IMimeSecurityCallback.FindKeyFor
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

# IMimeSecurityCallback::FindKeyFor method

\[**IMimeSecurityCallback::FindKeyFor** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

## Syntax


```C++
HRESULT FindKeyFor(
  [in]            HWND                    hwnd,
  [in]            DWORD                   dwFlags,
  [in]            DWORD                   dwRecipientIndex,
  [in]      const CMSG_CMS_RECIPIENT_INFO *pRecipInfo,
  [out]           DWORD                   *pdwCtrl,
  [in, out]       CMS_CTRL_DECRYPT_INFO   *pDecryptInfo,
  [out]           PCCERT_CONTEXT          *ppccert
);
```



## Parameters

<dl> <dt>

*hwnd* \[in\]
</dt> <dd>

Type: **HWND**

Specifies handle to window.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

</dd> <dt>

*dwRecipientIndex* \[in\]
</dt> <dd>

Type: **DWORD**

</dd> <dt>

*pRecipInfo* \[in\]
</dt> <dd>

Type: **const CMSG\_CMS\_RECIPIENT\_INFO\***

Specifies pointer to structure

</dd> <dt>

*pdwCtrl* \[out\]
</dt> <dd>

Type: **DWORD\***

</dd> <dt>

*pDecryptInfo* \[in, out\]
</dt> <dd>

Type: **[**CMS\_CTRL\_DECRYPT\_INFO**](oe-cms-ctrl-decrypt-info.md)\***

</dd> <dt>

*ppccert* \[out\]
</dt> <dd>

Type: **PCCERT\_CONTEXT\***

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



 

 





