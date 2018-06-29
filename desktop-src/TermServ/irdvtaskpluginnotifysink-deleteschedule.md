---
title: IRDVTaskPluginNotifySink DeleteSchedule method
description: Called by the task agent to delete a scheduled task.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 67a9493e-367a-48c9-8f94-276d696406b7
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
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
ms.author: windowssdkdev
ms.topic: article
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



|                                     |                                   |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | Windows 7 Enterprise<br/>   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/> |



## See also

<dl> <dt>

[**IRDVTaskPluginNotifySink**](irdvtaskpluginnotifysink.md)
</dt> </dl>

 

 





