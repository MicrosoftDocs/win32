---
title: CIM\_Setting class
description: The CIM\_Setting class represents configuration-related and operational parameters for one or more managed system elements.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 490e0f30-10db-4210-ab7b-14b745c08bca
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_Setting class
- CIM_Setting class, described
topic_type:
- apiref
api_name:
- CIM_Setting
- CIM_Setting.SettingID
- CIM_Setting.Caption
- CIM_Setting.Description
api_location:
- WlbsProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_Setting class

The **CIM\_Setting** class represents configuration-related and operational parameters for one or more managed system elements. A managed system element may have multiple setting objects associated with it. The current operational values for an element's parameters are reflected by properties in the element itself or by properties in its associations. These properties do not have to be the same values present in the **CIM\_Setting** object. For example, a modem may have a setting baud rate of 56Kb/sec but be operating at 19.2Kb/sec.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, AMENDMENT]
class CIM_Setting
{
  string SettingID;
  string Caption;
  string Description;
};
```

## Members

The **CIM\_Setting** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Setting** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the CIM\_Setting object.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the CIM\_Setting object.

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The identifier by which the CIM\_Setting object is known.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



 

 





