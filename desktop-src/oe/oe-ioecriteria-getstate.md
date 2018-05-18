---
title: IOECriteria GetState method
description: IOECriteria GetState is no longer available for use as of Windows Vista.
ms.assetid: '86904e1b-8b19-464f-a283-1cb25e0cba19'
keywords: ["GetState method Windows Mail (formerly Outlook Express)", "GetState method Windows Mail (formerly Outlook Express) , IOECriteria interface", "IOECriteria interface Windows Mail (formerly Outlook Express) , GetState method"]
topic_type:
- apiref
api_name:
- IOECriteria.GetState
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IOECriteria::GetState method

\[**IOECriteria::GetState** is no longer available for use as of Windows Vista.\]

## Syntax


```C++
HRESULT GetState(
  [out] DWORD *pdwState
);
```



## Parameters

<dl> <dt>

*pdwState* \[out\]
</dt> <dd>

Type: **DWORD\***

<dl> <dt>

<span id="CRIT_STATE_NULL"></span><span id="crit_state_null"></span>**CRIT\_STATE\_NULL** ()
</dt> <dt>

<span id="CRIT_STATE_DIRTY"></span><span id="crit_state_dirty"></span>**CRIT\_STATE\_DIRTY** ()
</dt> <dt>

<span id="CRIT_STATE_LOADED"></span><span id="crit_state_loaded"></span>**CRIT\_STATE\_LOADED** ()
</dt> <dt>

<span id="CRIT_STATE_HEADER"></span><span id="crit_state_header"></span>**CRIT\_STATE\_HEADER** ()
</dt> <dt>

<span id="CRIT_STATE_ALL"></span><span id="crit_state_all"></span>**CRIT\_STATE\_ALL** ()
</dt> <dt>

<span id="CRIT_STATE_MASK"></span><span id="crit_state_mask"></span>**CRIT\_STATE\_MASK** ()
</dt> </dl> </dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows XP<br/>                                                                                          |
| End of server support<br/>    | Windows Server 2003<br/>                                                                                 |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Oerules.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





