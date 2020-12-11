---
title: IRDVTaskPlugin Terminate method
description: Called when the task agent is being shut down.
ms.assetid: b693a318-1da7-4207-8046-a62b7ccca471
ms.tgt_platform: multiple
keywords:
- Terminate method Remote Desktop Services
- Terminate method Remote Desktop Services , IRDVTaskPlugin interface
- IRDVTaskPlugin interface Remote Desktop Services , Terminate method
topic_type:
- apiref
api_name:
- IRDVTaskPlugin.Terminate
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IRDVTaskPlugin::Terminate method

Called when the task agent is being shut down.

## Syntax


```C++
HRESULT Terminate(
  [in] HRESULT hr
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Indicates whether the shut down is due to a normal shut down or a failure. If the shut down is normal, this contains **S\_OK**. Otherwise, it contains an **HRESULT** error code.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | Windows 7 Enterprise<br/>   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/> |



## See also

<dl> <dt>

[**IRDVTaskPlugin**](irdvtaskplugin.md)
</dt> </dl>

 

 





