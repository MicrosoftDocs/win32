---
title: MicrosoftNLB\_PortRuleLoadbalanced class
description: The MicrosoftNLB\_PortRuleLoadbalanced \ 32;WMI class represents a Network Load Balancing port rule set to Multiple-host filtering mode. Do not use this class; use MicrosoftNLB\_PortRuleEx for managing port rules instead.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9f1aae0d-4fea-4deb-aaf8-0742f5a66d84
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MicrosoftNLB_PortRuleLoadbalanced class
- MicrosoftNLB_PortRuleLoadbalanced class, described
topic_type:
- apiref
api_name:
- MicrosoftNLB_PortRuleLoadbalanced
- MicrosoftNLB_PortRuleLoadbalanced.SettingID
- MicrosoftNLB_PortRuleLoadbalanced.Caption
- MicrosoftNLB_PortRuleLoadbalanced.Description
- MicrosoftNLB_PortRuleLoadbalanced.Name
- MicrosoftNLB_PortRuleLoadbalanced.AdapterGuid
- MicrosoftNLB_PortRuleLoadbalanced.EndPort
- MicrosoftNLB_PortRuleLoadbalanced.Protocol
- MicrosoftNLB_PortRuleLoadbalanced.StartPort
- MicrosoftNLB_PortRuleLoadbalanced.Affinity
- MicrosoftNLB_PortRuleLoadbalanced.EqualLoad
- MicrosoftNLB_PortRuleLoadbalanced.LoadWeight
api_location:
- WlbsProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MicrosoftNLB\_PortRuleLoadbalanced class

The **MicrosoftNLB\_PortRuleLoadbalanced** [*WMI class*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-22-gly) represents a Network Load Balancing [*port rule*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) set to [*Multiple-host filtering mode*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-8-gly). Do not use this class; use [**MicrosoftNLB\_PortRuleEx**](microsoftnlb-portruleex.md) for managing port rules instead.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("Microsoft|NLB_Provider|V1.0"), AMENDMENT]
class MicrosoftNLB_PortRuleLoadbalanced : MicrosoftNLB_PortRule
{
  string  SettingID;
  string  Caption;
  string  Description;
  string  Name;
  string  AdapterGuid;
  uint32  EndPort = 65535;
  uint32  Protocol;
  uint32  StartPort = 0;
  uint32  Affinity;
  Boolean EqualLoad = TRUE;
  uint32  LoadWeight = 50;
};
```

## Members

The **MicrosoftNLB\_PortRuleLoadbalanced** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MicrosoftNLB\_PortRuleLoadbalanced** class has these methods.



| Method                                                               | Description                                                                                                                                                                                                                                                                                                |
|:---------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SetDefaults**](microsoftnlb-portruleloadbalanced-setdefaults.md) | Qualifiers: **Static**, [**Implemented**](https://msdn.microsoft.com/library/aa393651)<br/> Resets the node's [*port rule*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) configuration to the default.<br/> This method is inherited from [**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md).<br/> |



 

### Properties

The **MicrosoftNLB\_PortRuleLoadbalanced** class has these properties.

<dl> <dt>

**AdapterGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the GUID of the adapter to which Network Load Balancing is bound.

This property is inherited from [**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md).

</dd> <dt>

**Affinity**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies client affinity as one of the following values.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)


</dt> <dd></dd> <dt>

<span id="Single"></span><span id="single"></span><span id="SINGLE"></span>

<span id="Single"></span><span id="single"></span><span id="SINGLE"></span>**Single** (1)


</dt> <dd>

Single (the default)

</dd> <dt>

<span id="Network"></span><span id="network"></span><span id="NETWORK"></span>

<span id="Network"></span><span id="network"></span><span id="NETWORK"></span>**Network** (2)


</dt> <dd>

Class C

</dd> </dl>

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
</dt> </dl>

Not used.

This property inherits from [**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md).

</dd> <dt>

**EqualLoad**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) accepts an equal portion of the load-balanced traffic in multiple-host filtering mode for this port rule. If this property is set to **TRUE** (the default), the node accepts an equal portion of the load-balanced traffic.

</dd> <dt>

**LoadWeight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The percentage of load-balanced network traffic that this node should handle for the associated port rule. Allowed values range from 0 (zero) to 100; defaults to 50. To prevent a node from handling any network traffic, set the load weight to 0 (zero).

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

**Protocol**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
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

The identifier by which the object is known.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

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

An instance of the **MicrosoftNLB\_PortRuleLoadbalanced** class corresponds to a port rule on a single cluster node (specified by the **Name** property).

The instance can be obtained from the [**GetPortRule**](microsoftnlb-nodesetting-getportrule.md) method of the [**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md) class. After changing any **MicrosoftNLB\_PortRuleLoadbalanced** properties, you must call the [**LoadAllSettings**](microsoftnlb-nodesetting-loadallsettings.md) method of the **MicrosoftNLB\_NodeSetting** class to bring the new values into effect.

The **MicrosoftNLB\_PortRuleLoadbalanced** class is derived from the [**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md) class.

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

[**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md)
</dt> <dt>

[**MicrosoftNLB\_PortRuleFailover**](microsoftnlb-portrulefailover.md)
</dt> <dt>

[**MicrosoftNLB\_PortRuleDisabled**](microsoftnlb-portruledisabled.md)
</dt> </dl>

 

 





