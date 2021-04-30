---
title: IRDVTaskPluginNotifySink OnTerminated method (Sbtsv.h)
description: Called by the task agent to request that the task agent be shut down.
ms.assetid: 163e0ce5-f4ee-4242-bdbb-977c5ede3451
ms.tgt_platform: multiple
keywords:
- OnTerminated method Remote Desktop Services
- OnTerminated method Remote Desktop Services , IRDVTaskPluginNotifySink interface
- IRDVTaskPluginNotifySink interface Remote Desktop Services , OnTerminated method
topic_type:
- apiref
api_name:
- IRDVTaskPluginNotifySink.OnTerminated
api_location:
- sbtsv.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IRDVTaskPluginNotifySink::OnTerminated method

Called by the task agent to request that the task agent be shut down.

## Syntax


```C++
HRESULT OnTerminated(
  [in] HRESULT hr
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Indicates if the shut down is due to a normal shut down or a failure. If the shut down is normal, this contains **S\_OK**. Otherwise, it contains an **HRESULT** error code.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 Enterprise<br/>                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                  |
| Header<br/>                   | <dl> <dt>Sbtsv.h</dt> </dl> |



## See also

<dl> <dt>

[**IRDVTaskPluginNotifySink**](irdvtaskpluginnotifysink.md)
</dt> </dl>

 

 





