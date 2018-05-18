---
title: MicrosoftNLB\_PortRuleEx class
description: Represents a port rule on a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '02b6cb2f-eb70-4dfb-bd9c-d1fa44987540'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MicrosoftNLB_PortRuleEx class", "MicrosoftNLB_PortRuleEx class, described"]
topic_type:
- apiref
api_name:
- MicrosoftNLB_PortRuleEx
- MicrosoftNLB_PortRuleEx.Name
- MicrosoftNLB_PortRuleEx.VirtualIpAddress
- MicrosoftNLB_PortRuleEx.StartPort
- MicrosoftNLB_PortRuleEx.EndPort
- MicrosoftNLB_PortRuleEx.Protocol
- MicrosoftNLB_PortRuleEx.AdapterGuid
- MicrosoftNLB_PortRuleEx.FilteringMode
- MicrosoftNLB_PortRuleEx.EqualLoad
- MicrosoftNLB_PortRuleEx.LoadWeight
- MicrosoftNLB_PortRuleEx.ClientStickinessTimeout
- MicrosoftNLB_PortRuleEx.Affinity
- MicrosoftNLB_PortRuleEx.Priority
- MicrosoftNLB_PortRuleEx.PortState
api_location:
- WlbsProv.dll
api_type:
- DllExport
---

# MicrosoftNLB\_PortRuleEx class

The **MicrosoftNLB\_PortRuleEx** [*WMI class*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-22-gly) represents a [*port rule*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) on a node. The provider will only return the instances for this class that correspond to the [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) upon which it resides. Consequently, to configure a node, the client must explicitly connect to that node.

Always use the **MicrosoftNLB\_PortRuleEx** class instead of the [**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md), [**MicrosoftNLB\_PortRuleFailover**](microsoftnlb-portrulefailover.md), [**MicrosoftNLB\_PortRuleLoadbalanced**](microsoftnlb-portruleloadbalanced.md), and [**MicrosoftNLB\_PortRuleDisabled**](microsoftnlb-portruledisabled.md) classes.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("Microsoft|NLB_Provider|V1.0"), AMENDMENT]
class MicrosoftNLB_PortRuleEx
{
  string  Name;
  string  VirtualIpAddress = "255.255.255.255";
  uint32  StartPort = 0;
  uint32  EndPort = 65535;
  uint32  Protocol = 3;
  string  AdapterGuid;
  uint32  FilteringMode = 2;
  Boolean EqualLoad = TRUE;
  uint32  LoadWeight = 50;
  uint32  ClientStickinessTimeout = 20;
  uint32  Affinity = 1;
  uint32  Priority = 1;
  uint32  PortState;
};
```

## Members

The **MicrosoftNLB\_PortRuleEx** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MicrosoftNLB\_PortRuleEx** class has these methods.



| Method                                                     | Description                                                                                                            |
|:-----------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------|
| [**SetDefaults**](microsoftnlb-portruleex-setdefaults.md) | Resets the node's [*port rule*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) configuration to the default.<br/> |



 

### Properties

The **MicrosoftNLB\_PortRuleEx** class has these properties.

<dl> <dt>

**AdapterGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the **GUID** of the adapter to which Network Load Balancing is bound.

</dd> <dt>

**Affinity**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the client affinity as one of the following values.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (0)


</dt> <dd></dd> <dt>

<span id="Single"></span><span id="single"></span><span id="SINGLE"></span>

**Single** (1)


</dt> <dd></dd> <dt>

<span id="Network"></span><span id="network"></span><span id="NETWORK"></span>

**Network** (2)


</dt> <dd></dd> </dl>

1 (Single) and 2 (Network) are used to ensure that all network traffic from a particular client be directed to the same cluster host. The default is 1 (Single).

</dd> <dt>

**ClientStickinessTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the Extended Affinity time-out (in minutes) of load-balanced network traffic that this host should handle for the associated port rule. This can be used to keep SSL sessions connected to the same node across NLB configuration changes (for example adding or removing nodes from the NLB cluster). This property is ignored (and Extended Affinity is disabled) if any of the following conditions are met:

-   Any nodes in the cluster are running Windows Server 2008.
-   The **FilteringMode** property is not set to 2 (Multiple Host).
-   The **Affinity** property is set to 0 (None).

<dt>



 (0)


</dt> <dd>

This value disables Extended Affinity for this port rule on this node.

</dd> <dt>

20
</dt> <dd>

Default value

</dd> <dt>

0–240
</dt> <dd>

Valid range

</dd> </dl>

**Windows Server 2008:** The **ClientStickinessTimeout** property is not supported until Windows Server 2008 R2.

</dd> <dt>

**EndPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ending port number to which this rule applies.

<dt>



 (65535)


</dt> <dd>

Default value

</dd> <dt>

0–65535
</dt> <dd>

Valid range

</dd> </dl>

</dd> <dt>

**EqualLoad**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates that the host accepts an equal portion of the load-balanced traffic in [*multiple-host filtering mode*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-8-gly) for this port rule.

<dt>



 (TRUE)


</dt> <dd>

The value for the **LoadWeight** property is ignored. Default value.

</dd> <dt>

False
</dt> <dd>

The value of the **LoadWeight** property is used to determine the portion of load-balanced traffic for this port rule.

</dd> </dl>

</dd> <dt>

**FilteringMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The filtering mode for this rule. This can be one of the following values.

<dt>

<span id="Single_Host"></span><span id="single_host"></span><span id="SINGLE_HOST"></span>

<span id="Single_Host"></span><span id="single_host"></span><span id="SINGLE_HOST"></span>**Single Host** (1)


</dt> <dd>

[*Single-host filtering mode*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-18-gly)

</dd> <dt>

<span id="Multiple_Host"></span><span id="multiple_host"></span><span id="MULTIPLE_HOST"></span>

<span id="Multiple_Host"></span><span id="multiple_host"></span><span id="MULTIPLE_HOST"></span>**Multiple Host** (2)


</dt> <dd>

[*Multiple-host filtering mode*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-8-gly). Default value.

</dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (3)


</dt> <dd>

Disabled

</dd> </dl>

If the value is 2 (Multiple Host), the value for the **Priority** property is ignored. If the value is 1 (Single Host), the values for **EqualLoad**, **LoadWeight**, and **Affinity** are ignored. If the value is 3 (Disabled), the values for **EqualLoad**, **LoadWeight**, **Affinity**, and **Priority** are ignored.

</dd> <dt>

**LoadWeight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The relative weight of load-balanced network traffic that this host should handle for the associated port rule.

<dt>

0
</dt> <dd>

Prevents a host from handling any network traffic.

</dd> <dt>



 (50)


</dt> <dd>

Default value

</dd> <dt>

0–100
</dt> <dd>

Valid range

</dd> </dl>

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Name")
</dt> </dl>

The name of the host to which this port rule applies.

</dd> <dt>

**PortState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current status of the port rule. This is one of the following values.

<dt>

<span id="NLB_PORT_RULE_NOT_FOUND"></span><span id="nlb_port_rule_not_found"></span>

**NLB\_PORT\_RULE\_NOT\_FOUND** (0)


</dt> <dd></dd> <dt>

<span id="NLB_PORT_RULE_ENABLED"></span><span id="nlb_port_rule_enabled"></span>

**NLB\_PORT\_RULE\_ENABLED** (1)


</dt> <dd></dd> <dt>

<span id="NLB_PORT_RULE_DISABLED"></span><span id="nlb_port_rule_disabled"></span>

**NLB\_PORT\_RULE\_DISABLED** (2)


</dt> <dd></dd> <dt>

<span id="NLB_PORT_RULE_DRAINING"></span><span id="nlb_port_rule_draining"></span>

**NLB\_PORT\_RULE\_DRAINING** (3)


</dt> <dd></dd> </dl>

If this port rule was created using the [*WMI*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-20-gly) [*provider*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-9-gly) and the [**LoadAllSettings**](microsoftnlb-nodesetting-loadallsettings.md) method of the [**MicrosoftNLB\_NodeSetting**](https://msdn.microsoft.com/library/aa371157) class was not called, this property will return **NLB\_PORT\_RULE\_NOT\_FOUND**.

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The [*priority*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-3-gly) of the local host for handling the networking traffic for this port rule. The host with the highest handling priority (lowest numerical value) for this rule among the current members of the cluster will handle all of the traffic for this rule. The allowed values range from 1, the highest priority, to the maximum number of hosts allowed. This value must be unique for all hosts in the cluster. The default is 1.

</dd> <dt>

**Protocol**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The protocol for which this rule applies as one of the following values.

<dt>

<span id="TCP"></span><span id="tcp"></span>

<span id="TCP"></span><span id="tcp"></span>**TCP** (1)


</dt> <dd>

TCP

</dd> <dt>

<span id="UDP"></span><span id="udp"></span>

<span id="UDP"></span><span id="udp"></span>**UDP** (2)


</dt> <dd>

UDP

</dd> <dt>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>**Both** (3)


</dt> <dd>

Both (the default)

</dd> </dl>

</dd> <dt>

**StartPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The starting port number to which this rule applies.

<dt>



 (0)


</dt> <dd>

Default value

</dd> <dt>

0–65535
</dt> <dd>

Valid range

</dd> </dl>

</dd> <dt>

**VirtualIpAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The virtual IP address to which this rule applies. The value of virtual IP address to specify 'All Vip' (the rest of the virtual IP addresses) is "255.255.255.255". The default value is "255.255.255.255".

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



 

 





