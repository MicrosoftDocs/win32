---
title: IRDVTaskPlugin interface
description: The IRDVTaskPlugin interface is implemented by a virtual machine update task agent to allow the task agent to manage system updates for a virtual machine.
ms.assetid: e06eb707-be78-4d1f-96d3-21526b167e61
ms.tgt_platform: multiple
keywords:
- IRDVTaskPlugin interface Remote Desktop Services
- IRDVTaskPlugin interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IRDVTaskPlugin
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IRDVTaskPlugin interface

The **IRDVTaskPlugin** interface is implemented by a virtual machine update *task agent* to allow the task agent to manage system updates for a virtual machine. This interface is used by the *trigger agent*, which is implemented by the host system.

## Members

The **IRDVTaskPlugin** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IRDVTaskPlugin** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IRDVTaskPlugin** interface has these methods.



| Method                                          | Description                                                        |
|:------------------------------------------------|:-------------------------------------------------------------------|
| [**Initialize**](irdvtaskplugin-initialize.md) | Called to initialize the task agent.<br/>                    |
| [**StartTask**](irdvtaskplugin-starttask.md)   | Called to start the update task on the virtual machine.<br/> |
| [**Terminate**](irdvtaskplugin-terminate.md)   | Called when the task agent is being shut down.<br/>          |



 

### Properties

The **IRDVTaskPlugin** interface has these properties.



| Property                                                   | Access type          | Description                                             |
|:-----------------------------------------------------------|:---------------------|:--------------------------------------------------------|
| [**PluginName**](irdvtaskplugin-pluginname.md)<br/> | Read-only<br/> | Contains the display name of the task agent.<br/> |



 

## Remarks

The task agent is run on the virtual machine when that virtual machine is scheduled for a system update. The task agent updates the virtual machine when the [**StartTask**](irdvtaskplugin-starttask.md) method is called.

To register the task agent, add the following key to the registry of the virtual machine:

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**Windows NT**\\**CurrentVersion**\\**Terminal Server**\\**Task**\\**Plugins**\\**TaskAgentName**

Under this registry key, add the following values:



| Name                     | Type                      | Description                                                                   |
|--------------------------|---------------------------|-------------------------------------------------------------------------------|
| **CLSID**<br/>     | **REG\_SZ**<br/>    | A string that represents the **CLSID** of the task agent.<br/>          |
| **IsEnabled**<br/> | **REG\_DWORD**<br/> | 0 if the task agent is disabled or 1 if the task agent is enabled.<br/> |



 

> [!Note]  
> More than one task agent can be registered, but only one task agent will be used. If more than one task agent is enabled, only the first one found will be used.

 

Although this interface is supported on the operating systems identified in the Requirements below, it will only be used if the virtual machine is hosted on Windows Server 2012.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | Windows 7 Enterprise<br/>   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/> |



 

