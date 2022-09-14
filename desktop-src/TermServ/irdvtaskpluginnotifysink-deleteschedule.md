---
title: IRDVTaskPluginNotifySink DeleteSchedule method
description: Called by the task agent to delete a scheduled task.
ms.assetid: 67a9493e-367a-48c9-8f94-276d696406b7
ms.tgt_platform: multiple
keywords:
- DeleteSchedule method Remote Desktop Services
- DeleteSchedule method Remote Desktop Services , IRDVTaskPluginNotifySink interface
- IRDVTaskPluginNotifySink interface Remote Desktop Services , DeleteSchedule method
topic_type:
- apiref
api_name:
- IRDVTaskPluginNotifySink.DeleteSchedule
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IRDVTaskPluginNotifySink::DeleteSchedule method

Called by the task agent to delete a scheduled task.

## Syntax


```C++
HRESULT DeleteSchedule(
  [in] BSTR bstrIdentifier
);
```



## Parameters

<dl> <dt>

*bstrIdentifier* \[in\]
</dt> <dd>

The identifier of the scheduled task.

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

[**IRDVTaskPluginNotifySink**](irdvtaskpluginnotifysink.md)
</dt> </dl>

 

 





