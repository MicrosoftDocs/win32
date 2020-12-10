---
title: IRDVTaskPlugin Initialize method
description: Called to initialize the task agent.
ms.assetid: eef813e6-ecca-400a-a9f3-efca6bd81161
ms.tgt_platform: multiple
keywords:
- Initialize method Remote Desktop Services
- Initialize method Remote Desktop Services , IRDVTaskPlugin interface
- IRDVTaskPlugin interface Remote Desktop Services , Initialize method
topic_type:
- apiref
api_name:
- IRDVTaskPlugin.Initialize
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IRDVTaskPlugin::Initialize method

Called to initialize the task agent.

## Syntax


```C++
HRESULT Initialize(
  [in] IRDVTaskPluginNotifySink *pNotifySink
);
```



## Parameters

<dl> <dt>

*pNotifySink* \[in\]
</dt> <dd>

Type: **[**IRDVTaskPluginNotifySink**](irdvtaskpluginnotifysink.md)\***

A pointer to an [**IRDVTaskPluginNotifySink**](irdvtaskpluginnotifysink.md) interface that the task agent uses to communicate with the trigger agent. You must release this interface when it is no longer needed.

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

[**IRDVTaskPlugin**](irdvtaskplugin.md)
</dt> </dl>

 

 





