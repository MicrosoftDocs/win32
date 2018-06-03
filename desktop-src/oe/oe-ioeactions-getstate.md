---
title: IOEActions GetState method
description: IOEActions GetState is no longer available for use as of Windows Vista.
ms.assetid: e1043c3f-3a2d-4ac1-8961-51dce22e6731
keywords:
- GetState method Windows Mail (formerly Outlook Express)
- GetState method Windows Mail (formerly Outlook Express) , IOEActions interface
- IOEActions interface Windows Mail (formerly Outlook Express) , GetState method
topic_type:
- apiref
api_name:
- IOEActions.GetState
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

# IOEActions::GetState method

\[**IOEActions::GetState** is no longer available for use as of Windows Vista.\]

## Syntax


```C++
HRESULT GetState(
  [out] DWORD *pdwState
);
```



## Parameters

<dl> <dt>

*pdwState* \[out\]
</dt> <dd>

Type: **DWORD\***

<dl> <dt>

<span id="ACT_STATE_NULL"></span><span id="act_state_null"></span>**ACT\_STATE\_NULL** (0x00000000)
</dt> <dt>

<span id="ACT_STATE_DIRTY"></span><span id="act_state_dirty"></span>**ACT\_STATE\_DIRTY** (0x00000100)
</dt> <dt>

<span id="ACT_STATE_LOADED"></span><span id="act_state_loaded"></span>**ACT\_STATE\_LOADED** (0x00000200)
</dt> <dt>

<span id="ACT_STATE_SERVER"></span><span id="act_state_server"></span>**ACT\_STATE\_SERVER** (0x01000000)
</dt> <dt>

<span id="ACT_STATE_LOCAL"></span><span id="act_state_local"></span>**ACT\_STATE\_LOCAL** (0x02000000)
</dt> <dt>

<span id="ACT_STATE_MASK"></span><span id="act_state_mask"></span>**ACT\_STATE\_MASK** (0xFF000000)
</dt> </dl> </dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows XP<br/>                                                                                          |
| End of server support<br/>    | Windows Server 2003<br/>                                                                                 |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





