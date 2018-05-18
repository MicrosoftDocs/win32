---
title: CIM\_ElementConfiguration class
description: This association relates a CIM\_Configuration object to one or more managed system elements. The CIM\_Configuration object represents a certain behavior, or a desired functional state for the associated managed system elements.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '65436b1c-6058-45eb-ab93-375b926938b7'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_ElementConfiguration class", "CIM_ElementConfiguration class, described"]
topic_type:
- apiref
api_name:
- CIM_ElementConfiguration
- CIM_ElementConfiguration.Element
- CIM_ElementConfiguration.Configuration
api_location:
- WlbsProv.dll
api_type:
- DllExport
---

# CIM\_ElementConfiguration class

This association relates a [**CIM\_Configuration**](cim-configuration.md) object to one or more managed system elements. The **CIM\_Configuration** object represents a certain behavior, or a desired functional state for the associated managed system elements.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, AMENDMENT]
class CIM_ElementConfiguration
{
  CIM_ManagedSystemElement REF Element;
  CIM_Configuration        REF Configuration;
};
```

## Members

The **CIM\_ElementConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ElementConfiguration** class has these properties.

<dl> <dt>

**Configuration**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Configuration**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The object that groups the settings and dependencies associated with the managed system element

</dd> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedSystemElement**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The managed system element

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



 

 





