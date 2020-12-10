---
title: NetworkProfileName (settingsType) Element
description: Contains the name of a network profile. The Task Scheduler service checks the availability of this network when the RunOnlyIfNetworkAvailable element is set to True. The name is used for display purposes.
ms.assetid: f02dc75c-6c48-4a42-8263-13d9704b993c
keywords:
- NetworkProfileName element Task Scheduler
topic_type:
- apiref
api_name:
- NetworkProfileName
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# NetworkProfileName (settingsType) Element

Contains the name of a network profile. The Task Scheduler service checks the availability of this network when the [**RunOnlyIfNetworkAvailable**](taskschedulerschema-runonlyifnetworkavailable-settingstype-element.md) element is set to **True**. The name is used for display purposes.

``` syntax
<xs:element name="NetworkProfileName"
    type="string"
    minOccurs="0"
 />
```

The **NetworkProfileName** element is defined by the [**settingsType**](taskschedulerschema-settingstype-complextype.md) complex type.

## Parent element



| Element                                                                      | Derived from                                                         | Description                                                                         |
|------------------------------------------------------------------------------|----------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [**Settings (taskType)**](taskschedulerschema-settings-tasktype-element.md) | [**settingsType**](taskschedulerschema-settingstype-complextype.md) | Specifies the settings that the Task Scheduler uses to perform the task.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





