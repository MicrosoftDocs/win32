---
title: NetworkSettings (settingsType) Element
description: Contains the settings that the Task Scheduler service uses to obtain a network profile. The Task Scheduler service checks the availability of this network when the RunOnlyIfNetworkAvailable element is set to True.
ms.assetid: 7452b788-a170-4afe-abc5-ebcd3722da0d
keywords:
- NetworkSettings element Task Scheduler
topic_type:
- apiref
api_name:
- NetworkSettings
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# NetworkSettings (settingsType) Element

Contains the settings that the Task Scheduler service uses to obtain a network profile. The Task Scheduler service checks the availability of this network when the [**RunOnlyIfNetworkAvailable**](taskschedulerschema-runonlyifnetworkavailable-settingstype-element.md) element is set to **True**.

``` syntax
<xs:element name="NetworkSettings"
    type="networkSettingsType"
    minOccurs="0"
 />
```

The **NetworkSettings** element is defined by the [**settingsType**](taskschedulerschema-settingstype-complextype.md) complex type.

## Parent element



| Element                                                                      | Derived from                                                         | Description                                                                         |
|------------------------------------------------------------------------------|----------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [**Settings (taskType)**](taskschedulerschema-settings-tasktype-element.md) | [**settingsType**](taskschedulerschema-settingstype-complextype.md) | Specifies the settings that the Task Scheduler uses to perform the task.<br/> |



## Remarks

For C++ development, see [**NetworkSettings Property of ITaskSettings**](/windows/desktop/api/taskschd/nf-taskschd-itasksettings-get_networksettings).

For script development, see [**TaskSettings.NetworkSettings**](tasksettings-networksettings.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





