---
title: CIM\_SettingContext class
description: This relationship associates a setting with one or more configuration objects. For example, a network adapters settings could change based on the site/network to which its hosting computer system is attached.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 554ec217-4ec5-43b4-9c6c-e82b0ae8b7d7
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_SettingContext class
- CIM_SettingContext class, described
topic_type:
- apiref
api_name:
- CIM_SettingContext
- CIM_SettingContext.Context
- CIM_SettingContext.Setting
api_location:
- WlbsProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_SettingContext class

This relationship associates a setting with one or more configuration objects. For example, a network adapter's settings could change based on the site/network to which its hosting computer system is attached.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, AMENDMENT]
class CIM_SettingContext
{
  CIM_Configuration REF Context;
  CIM_Setting       REF Setting;
};
```

## Members

The **CIM\_SettingContext** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SettingContext** class has these properties.

<dl> <dt>

**Context**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Configuration**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The configuration object that aggregates the setting

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Setting**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An aggregated setting.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



 

 





