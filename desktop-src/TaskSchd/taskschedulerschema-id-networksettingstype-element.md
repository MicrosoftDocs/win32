---
title: Id (networkSettingsType) Element
description: Contains a GUID value that identifies a network profile.
ms.assetid: 527912ab-9a81-4570-91c5-8f5943e79a28
keywords:
- Id element Task Scheduler
topic_type:
- apiref
api_name:
- Id
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Id (networkSettingsType) Element

Contains a GUID value that identifies a network profile.

``` syntax
<xs:element name="Id"
    type="guidType"
    minOccurs="0"
 />
```

The **Id** element is defined by the [**networkSettingsType**](taskschedulerschema-networksettingstype-complextype.md) complex type.

## Parent element



| Element                                                                                            | Derived from                                                                       | Description                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NetworkSettings (settingsType)**](taskschedulerschema-networksettings-settingstype-element.md) | [**networkSettingsType**](taskschedulerschema-networksettingstype-complextype.md) | Contains the settings that the Task Scheduler service uses to obtain a network profile. The Task Scheduler service checks the availability of this network when the [**RunOnlyIfNetworkAvailable**](taskschedulerschema-runonlyifnetworkavailable-settingstype-element.md) element is set to **True**.<br/> |



## Remarks

For C++ development, see [**Id Property of INetworkSettings**](/windows/desktop/api/taskschd/nf-taskschd-inetworksettings-get_id).

For script development, see [**NetworkSettings.Id**](networksettings-id.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





