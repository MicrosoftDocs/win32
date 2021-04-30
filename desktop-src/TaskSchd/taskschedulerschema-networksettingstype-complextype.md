---
title: networkSettingsType Complex Type
description: Defines the elements that provide the settings that the Task Scheduler service uses to obtain a network profile.
ms.assetid: e5df1dda-b691-47ff-a956-50ff1ce9c7cc
keywords:
- networkSettingsType complex type Task Scheduler
topic_type:
- apiref
api_name:
- networkSettingsType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# networkSettingsType Complex Type

Defines the elements that provide the settings that the Task Scheduler service uses to obtain a network profile.

``` syntax
<xs:complexType name="networkSettingsType">
    <xs:all>
        <xs:element name="Name"
            type="nonEmptyString"
            minOccurs="0"
         />
        <xs:element name="Id"
            type="guidType"
            minOccurs="0"
         />
    </xs:all>
</xs:complexType>
```

## Child elements



| Element                                                              | Type                                                        | Description                                                                                 |
|----------------------------------------------------------------------|-------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [**Id**](taskschedulerschema-id-networksettingstype-element.md)     | [**guidType**](taskschedulerschema-guidtype-simpletype.md) | Specifies a GUID value that identifies a network profile. <br/>                       |
| [**Name**](taskschedulerschema-name-networksettingstype-element.md) | nonEmptyString                                              | Specifies the name of a network profile. The name is used for display purposes. <br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





