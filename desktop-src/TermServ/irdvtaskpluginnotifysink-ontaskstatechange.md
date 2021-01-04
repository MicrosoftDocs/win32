---
title: IRDVTaskPluginNotifySink OnTaskStateChange method
description: Used to notify the trigger agent that the state of a task has changed.
ms.assetid: 3021ea7a-2627-48d1-8df5-c40e7a9b51c5
ms.tgt_platform: multiple
keywords:
- OnTaskStateChange method Remote Desktop Services
- OnTaskStateChange method Remote Desktop Services , IRDVTaskPluginNotifySink interface
- IRDVTaskPluginNotifySink interface Remote Desktop Services , OnTaskStateChange method
topic_type:
- apiref
api_name:
- IRDVTaskPluginNotifySink.OnTaskStateChange
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IRDVTaskPluginNotifySink::OnTaskStateChange method

Used to notify the trigger agent that the state of a task has changed.

## Syntax


```C++
HRESULT OnTaskStateChange(
  [in] BSTR            bstrIdentifier,
  [in] RDV_TASK_STATUS status
);
```



## Parameters

<dl> <dt>

*bstrIdentifier* \[in\]
</dt> <dd>

Type: **BSTR**

The identifier of the task. This is the identifier passed to the [**StartTask**](irdvtaskplugin-starttask.md) method.

</dd> <dt>

*status* \[in\]
</dt> <dd>

Type: **[**RDV\_TASK\_STATUS**](/windows/desktop/api/SessDirPublicTypes/ne-sessdirpublictypes-rdv_task_status)**

A value of the [**RDV\_TASK\_STATUS**](/windows/desktop/api/SessDirPublicTypes/ne-sessdirpublictypes-rdv_task_status) enumeration that specifies the new state of the task.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | Windows 7 Enterprise<br/>   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/> |



## See also

<dl> <dt>

[**RDV\_TASK\_STATUS**](/windows/desktop/api/SessDirPublicTypes/ne-sessdirpublictypes-rdv_task_status)
</dt> <dt>

[**IRDVTaskPluginNotifySink**](irdvtaskpluginnotifysink.md)
</dt> </dl>

 

 





