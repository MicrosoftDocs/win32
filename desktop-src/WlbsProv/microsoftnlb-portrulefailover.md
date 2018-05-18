---
title: MicrosoftNLB\_PortRuleFailover class
description: The MicrosoftNLB\_PortRuleFailover \ 32;WMI class represents a Network Load Balancing port rule set to Single-host filtering mode. Do not use this class; use MicrosoftNLB\_PortRuleEx for managing port rules instead.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '146a30f4-d22a-4925-9a55-1741886fe1d5'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MicrosoftNLB_PortRuleFailover class", "MicrosoftNLB_PortRuleFailover class, described"]
topic_type:
- apiref
api_name:
- MicrosoftNLB_PortRuleFailover
- MicrosoftNLB_PortRuleFailover.SettingID
- MicrosoftNLB_PortRuleFailover.Caption
- MicrosoftNLB_PortRuleFailover.Description
- MicrosoftNLB_PortRuleFailover.Name
- MicrosoftNLB_PortRuleFailover.AdapterGuid
- MicrosoftNLB_PortRuleFailover.EndPort
- MicrosoftNLB_PortRuleFailover.Protocol
- MicrosoftNLB_PortRuleFailover.StartPort
- MicrosoftNLB_PortRuleFailover.Priority
api_location:
- WlbsProv.dll
api_type:
- DllExport
---

# MicrosoftNLB\_PortRuleFailover class

The **MicrosoftNLB\_PortRuleFailover** [*WMI class*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-22-gly) represents a Network Load Balancing [*port rule*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) set to [*Single-host filtering mode*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-18-gly). Do not use this class; use [**MicrosoftNLB\_PortRuleEx**](microsoftnlb-portruleex.md) for managing port rules instead.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("Microsoft|NLB_Provider|V1.0"), AMENDMENT]
class MicrosoftNLB_PortRuleFailover : MicrosoftNLB_PortRule
{
  string SettingID;
  string Caption;
  string Description;
  string Name;
  string AdapterGuid;
  uint32 EndPort = 65535;
  uint32 Protocol;
  uint32 StartPort = 0;
  uint32 Priority = 1;
};
```

## Members

The **MicrosoftNLB\_PortRuleFailover** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MicrosoftNLB\_PortRuleFailover** class has these methods.



| Method                                                           | Description                                                                                                                                                                                                                                                                                                |
|:-----------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SetDefaults**](microsoftnlb-portrulefailover-setdefaults.md) | Qualifiers: **Static**, [**Implemented**](https://msdn.microsoft.com/library/aa393651)<br/> Resets the node's [*port rule*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) configuration to the default.<br/> This method is inherited from [**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md).<br/> |



 

### Properties

The **MicrosoftNLB\_PortRuleFailover** class has these properties.

<dl> <dt>

**AdapterGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

Specifies the GUID of the adapter to which Network Load Balancing is bound.

This property is inherited from [**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md).

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

Not used.

This property inherits from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**EndPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

Not used.

This property inherits from [**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md).

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

This property is inherited from [**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md).

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the local node's [*host priority*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-3-gly) for handling the networking traffic for this port rule. The node with the highest handling priority (lowest numerical value) for this rule among the current members of the cluster will handle all of the traffic for this rule. The allowed values range from 1, the highest priority (and the default), to the maximum number of nodes allowed. This value must be unique for all nodes in the cluster.

</dd> <dt>

**Protocol**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

Describes the network [*protocol*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-8-gly) to which this rule applies. The possible values are the following.

This property is inherited from [**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md).

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

This property is inherited from [**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md).

</dd> </dl>

## Remarks

An instance of the **MicrosoftNLB\_PortRuleFailover** class corresponds to a port rule on a single cluster node (specified by the **Name** property). The instance can be obtained from the [**GetPortRule**](microsoftnlb-nodesetting-getportrule.md) method of the [**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md) class. After changing any **MicrosoftNLB\_PortRuleFailover** properties, you must call the [**LoadAllSettings**](microsoftnlb-nodesetting-loadallsettings.md) method of the **MicrosoftNLB\_NodeSetting** class to bring the new values into effect.

The **MicrosoftNLB\_PortRuleFailover** class is derived from the [**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md) class.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md)
</dt> <dt>

[**MicrosoftNLB\_PortRuleLoadbalanced**](microsoftnlb-portruleloadbalanced.md)
</dt> <dt>

[**MicrosoftNLB\_PortRuleDisabled**](microsoftnlb-portruledisabled.md)
</dt> </dl>

 

 





