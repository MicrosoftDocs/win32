---
title: MicrosoftNLB\_PortRule class
description: The MicrosoftNLB\_PortRule \ 32;WMI class is an abstract base class from which classes that represent port rules are derived. Do not use this class; use MicrosoftNLB\_PortRuleEx instead.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fc019a96-17ac-4e5f-863e-444347f8b1c2
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MicrosoftNLB_PortRule class
- MicrosoftNLB_PortRule class, described
topic_type:
- apiref
api_name:
- MicrosoftNLB_PortRule
- MicrosoftNLB_PortRule.SettingID
- MicrosoftNLB_PortRule.Caption
- MicrosoftNLB_PortRule.Description
- MicrosoftNLB_PortRule.Name
- MicrosoftNLB_PortRule.AdapterGuid
- MicrosoftNLB_PortRule.EndPort
- MicrosoftNLB_PortRule.Protocol
- MicrosoftNLB_PortRule.StartPort
api_location:
- WlbsProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MicrosoftNLB\_PortRule class

The **MicrosoftNLB\_PortRule** [*WMI class*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-22-gly) is an abstract base class from which classes that represent [*port rules*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) are derived. Do not use this class; use [**MicrosoftNLB\_PortRuleEx**](microsoftnlb-portruleex.md) instead.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Abstract, Provider("Microsoft|NLB_Provider|V1.0"), AMENDMENT]
class MicrosoftNLB_PortRule : CIM_Setting
{
  string SettingID;
  string Caption;
  string Description;
  string Name;
  string AdapterGuid;
  uint32 EndPort = 65535;
  uint32 Protocol;
  uint32 StartPort = 0;
};
```

## Members

The **MicrosoftNLB\_PortRule** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MicrosoftNLB\_PortRule** class has these methods.



| Method                                                   | Description                                                                                                                                                                                              |
|:---------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SetDefaults**](microsoftnlb-portrule-setdefaults.md) | Qualifiers: **Static**, [**Implemented**](https://msdn.microsoft.com/library/aa393651)<br/> Resets the node's [*port rule*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) configuration to the default.<br/> |



 

### Properties

The **MicrosoftNLB\_PortRule** class has these properties.

<dl> <dt>

**AdapterGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the GUID of the adapter to which Network Load Balancing is bound.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

Not used.

This property inherits from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**EndPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the ending port number to which this rule applies. The default is 65535.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Name")
</dt> </dl>

The name of the host to which this port rule applies

</dd> <dt>

**Protocol**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the network [*protocol*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-8-gly) to which this rule applies. The possible values are the following.

<dt>

<span id="TCP"></span><span id="tcp"></span>

<span id="TCP"></span><span id="tcp"></span>**TCP** (1)


</dt> <dd></dd> <dt>

<span id="UDP"></span><span id="udp"></span>

<span id="UDP"></span><span id="udp"></span>**UDP** (2)


</dt> <dd></dd> <dt>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>**Both** (3)


</dt> <dd>

Both (the default)

</dd> </dl>

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Not used.

This property inherits from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**StartPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Specifies the starting port number to which this rule applies. The default is 0 (zero).

</dd> </dl>

## Remarks

The **MicrosoftNLB\_PortRule** class is derived from the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) class.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Setting**](cim-setting.md)
</dt> <dt>

[**MicrosoftNLB\_PortRuleEx**](microsoftnlb-portruleex.md)
</dt> </dl>

 

 





