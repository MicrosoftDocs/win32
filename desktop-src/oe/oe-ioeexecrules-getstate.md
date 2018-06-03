---
title: IOEExecRules GetState method
description: IOEExecRules GetState is no longer available for use as of Windows Vista.
ms.assetid: c3551e34-2dfa-4d87-b5d0-968fb587de7f
keywords:
- GetState method Windows Mail (formerly Outlook Express)
- GetState method Windows Mail (formerly Outlook Express) , IOEExecRules interface
- IOEExecRules interface Windows Mail (formerly Outlook Express) , GetState method
topic_type:
- apiref
api_name:
- IOEExecRules.GetState
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

# IOEExecRules::GetState method

\[**IOEExecRules::GetState** is no longer available for use as of Windows Vista.\]

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

Specifies a bitmask of ERF\_xxx flags

<dl> <dt>

<span id="ERF_ONLYSERVER"></span><span id="erf_onlyserver"></span>**ERF\_ONLYSERVER** (0x00000001)
</dt> <dt>

<span id="ERF_NOSERVER"></span><span id="erf_noserver"></span>**ERF\_NOSERVER** (0x00000002)
</dt> <dt>

<span id="ERF_SKIPPARTIALS"></span><span id="erf_skippartials"></span>**ERF\_SKIPPARTIALS** (0x00000004)
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



 

 





