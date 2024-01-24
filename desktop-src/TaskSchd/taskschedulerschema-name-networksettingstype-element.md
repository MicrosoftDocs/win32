---
title: Name (networkSettingsType) Element
description: Contains the name of a network profile. The name is used for display purposes.
ms.assetid: 86e4e68d-3c36-41eb-8563-d7d5125a5957
keywords:
- Name element Task Scheduler
topic_type:
- apiref
api_name:
- Name
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Name (networkSettingsType) Element

Contains the name of a network profile. The name is used for display purposes.

``` syntax
<xs:element name="Name"
    type="nonEmptyString"
    minOccurs="0"
 />
```

The **Name** element is defined by the [**networkSettingsType**](taskschedulerschema-networksettingstype-complextype.md) complex type.

## Parent element



| Element                                                                                            | Derived from                                                                       | Description                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetworkSettings (settingsType)**](taskschedulerschema-networksettings-settingstype-element.md) | [**networkSettingsType**](taskschedulerschema-networksettingstype-complextype.md) | Contains the settings that the Task Scheduler service uses to obtain a network profile. The Task Scheduler service checks the availability of this network when the [**RunOnlyIfNetworkAvailable**](taskschedulerschema-runonlyifnetworkavailable-settingstype-element.md) element is set to **True**.<br/> |



## Remarks

For C++ development, see [**Name Property of INetworkSettings**](/windows/desktop/api/taskschd/nf-taskschd-inetworksettings-get_name).

For script development, see [**NetworkSettings.Name**](networksettings-name.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





