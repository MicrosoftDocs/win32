---
title: CIM\_Configuration class
description: The Configuration object allows the grouping of sets of parameters (defined in CIM\_Setting objects) and dependencies for one or more managed system elements.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 60c32993-3d84-4764-a062-e1bdb10bbd58
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_Configuration class
- CIM_Configuration class, described
topic_type:
- apiref
api_name:
- CIM_Configuration
- CIM_Configuration.Name
- CIM_Configuration.Caption
- CIM_Configuration.Description
api_location:
- WlbsProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CIM\_Configuration class

The Configuration object allows the grouping of sets of parameters (defined in CIM\_Setting objects) and dependencies for one or more managed system elements. The Configuration object represents a certain behavior, or a desired functional state for the managed system elements. The desired functional state is typically driven by external requirements such as time or location. For example, to connect to a mail system from 'home', a dependency on a modem exists, but a dependency on a network adapter exists at 'work'. Settings for the pertinent logical devices (in this example, POTS modem and network adapter) can be defined and aggregated by **CIM\_Configuration**. Therefore, two 'Connect to Mail' configurations may be defined grouping the relevant dependencies and [**CIM\_Setting**](cim-setting.md) objects.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class CIM_Configuration
{
  string Name;
  string Caption;
  string Description;
};
```

## Members

The **CIM\_Configuration** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Configuration** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the object

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The label by which the object is known.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



 

 





