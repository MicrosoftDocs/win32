---
title: IRDVTaskPlugin PluginName property (Tspubplugincom.h)
description: Contains the display name of the task agent.
ms.assetid: 6f414270-e90b-4075-80fe-f918acbdd205
ms.tgt_platform: multiple
keywords:
- PluginName property Remote Desktop Services
- PluginName property Remote Desktop Services , IRDVTaskPlugin interface
- IRDVTaskPlugin interface Remote Desktop Services , PluginName property
topic_type:
- apiref
api_name:
- IRDVTaskPlugin.PluginName
- IRDVTaskPlugin.get_PluginName
api_location:
- tspubplugincom.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IRDVTaskPlugin::PluginName property

Contains the display name of the task agent. This name is used for logging purposes only.

This property is read-only.

## Syntax


```C++
HRESULT get_PluginName(
  [out, retval] BSTR *pVal
);
```



## Property value

The display name of the task agent.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 Enterprise<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                           |
| Header<br/>                   | <dl> <dt>Tspubplugincom.h</dt> </dl> |



## See also

<dl> <dt>

[**IRDVTaskPlugin**](irdvtaskplugin.md)
</dt> </dl>

 

 





