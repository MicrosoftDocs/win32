---
title: MicrosoftNLB\_NodeSetting class
description: The MicrosoftNLB\_NodeSetting \ 32;WMI class represents the configuration data specific to a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2deb5f13-4cf5-4ca2-938c-402a90974ddb'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MicrosoftNLB_NodeSetting class", "MicrosoftNLB_NodeSetting class, described"]
topic_type:
- apiref
api_name:
- MicrosoftNLB_NodeSetting
- MicrosoftNLB_NodeSetting.SettingID
- MicrosoftNLB_NodeSetting.Caption
- MicrosoftNLB_NodeSetting.Description
- MicrosoftNLB_NodeSetting.Name
- MicrosoftNLB_NodeSetting.DedicatedIPAddress
- MicrosoftNLB_NodeSetting.DedicatedIPAddresses
- MicrosoftNLB_NodeSetting.DedicatedNetworkMask
- MicrosoftNLB_NodeSetting.DedicatedNetworkMasks
- MicrosoftNLB_NodeSetting.NumberOfRules
- MicrosoftNLB_NodeSetting.HostPriority
- MicrosoftNLB_NodeSetting.AliveMessagePeriod
- MicrosoftNLB_NodeSetting.AliveMessageTolerance
- MicrosoftNLB_NodeSetting.ClusterModeOnStart
- MicrosoftNLB_NodeSetting.ClusterModeSuspendOnStart
- MicrosoftNLB_NodeSetting.PersistSuspendOnReboot
- MicrosoftNLB_NodeSetting.RemoteControlUDPPort
- MicrosoftNLB_NodeSetting.MaskSourceMAC
- MicrosoftNLB_NodeSetting.MaxConnectionDescriptors
- MicrosoftNLB_NodeSetting.DescriptorsPerAlloc
- MicrosoftNLB_NodeSetting.MaxDescriptorsPerAlloc
- MicrosoftNLB_NodeSetting.FilterIcmp
- MicrosoftNLB_NodeSetting.TcpDescriptorTimeout
- MicrosoftNLB_NodeSetting.IpSecDescriptorTimeout
- MicrosoftNLB_NodeSetting.NumActions
- MicrosoftNLB_NodeSetting.NumPackets
- MicrosoftNLB_NodeSetting.NumAliveMessages
- MicrosoftNLB_NodeSetting.AdapterGuid
api_location:
- WlbsProv.dll
api_type:
- DllExport
---

# MicrosoftNLB\_NodeSetting class

The **MicrosoftNLB\_NodeSetting** [*WMI class*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-22-gly) represents the configuration data specific to a [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("Microsoft|NLB_Provider|V1.0"), AMENDMENT]
class MicrosoftNLB_NodeSetting : CIM_Setting
{
  string  SettingID;
  string  Caption;
  string  Description;
  string  Name;
  string  DedicatedIPAddress;
  string  DedicatedIPAddresses[];
  string  DedicatedNetworkMask;
  string  DedicatedNetworkMasks[];
  uint32  NumberOfRules;
  uint32  HostPriority;
  uint32  AliveMessagePeriod;
  uint32  AliveMessageTolerance;
  Boolean ClusterModeOnStart;
  Boolean ClusterModeSuspendOnStart;
  Boolean PersistSuspendOnReboot;
  uint32  RemoteControlUDPPort;
  Boolean MaskSourceMAC;
  uint32  MaxConnectionDescriptors;
  uint32  DescriptorsPerAlloc;
  uint32  MaxDescriptorsPerAlloc;
  uint32  FilterIcmp;
  uint32  TcpDescriptorTimeout;
  uint32  IpSecDescriptorTimeout;
  uint32  NumActions;
  uint32  NumPackets;
  uint32  NumAliveMessages;
  string  AdapterGuid;
};
```

## Members

The **MicrosoftNLB\_NodeSetting** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MicrosoftNLB\_NodeSetting** class has these methods.



| Method                                                              | Description                                                                                                                                                                                                                 |
|:--------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetPortRule**](microsoftnlb-nodesetting-getportrule.md)         | Qualifier: [**Implemented**](https://msdn.microsoft.com/library/aa393651)<br/> This method retrieves the port rule associated with a port number.<br/>                                                                          |
| [**GetPortRuleEx**](microsoftnlb-nodesetting-getportruleex.md)     | Qualifier: [**Implemented**](https://msdn.microsoft.com/library/aa393651)<br/> This method retrieves the port rule associated with a virtual [*IP address*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-6-gly) and port number.<br/> |
| [**LoadAllSettings**](microsoftnlb-nodesetting-loadallsettings.md) | Qualifier: [**Implemented**](https://msdn.microsoft.com/library/aa393651)<br/> Propagates all current settings (cluster, node, and port rule) to the Network Load Balancing driver<br/>                                         |
| [**SetDefaults**](microsoftnlb-nodesetting-setdefaults.md)         | Qualifier: [**Implemented**](https://msdn.microsoft.com/library/aa393651)<br/> Resets all of the properties of the **MicrosoftNLB\_NodeSetting** class to their default values.<br/>                                            |



 

### Properties

The **MicrosoftNLB\_NodeSetting** class has these properties.

<dl> <dt>

**AdapterGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The **GUID** of the adapter to which Network Load Balancing is bound.

</dd> <dt>

**AliveMessagePeriod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The message exchange period in milliseconds. You should pick this number based on your failover requirements. A longer message exchange period will reduce the networking overhead needed to maintain fault tolerance, but it will increase the failover delay.

</dd> <dt>

**AliveMessageTolerance**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of exchanged messages from a node that can be missed before the [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly) initiates [*convergence*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-8-gly). You should adjust this number based on your availability requirements. Increasing the number of message exchanges before convergence will reduce the number of unnecessary convergence initiations due to transient network congestion, but it will also increase the failover delay.

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

**ClusterModeOnStart**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the node should join the cluster on boot. If set to **TRUE**, the node will join the cluster on boot, unless both of the following are true:

PersistSuspendOnReboot is **TRUE**

The node was shut down while in a suspended state.

</dd> <dt>

**ClusterModeSuspendOnStart**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the node should boot with cluster operations suspended. If set to **TRUE**, the node will not join the cluster and remain in the **WLBS\_SUSPENDED** state until a resume operation is performed. The value of this property is ignored if the **ClusterModeOnStart** property is set to **TRUE**.

</dd> <dt>

**DedicatedIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**MicrosoftNLB\_Node**](microsoftnlb-node.md).**DedicatedIPAddress**")
</dt> </dl>

This property is no longer supported. Use the **DedicatedIPAddress** property of the [**MicrosoftNLB\_Node**](https://msdn.microsoft.com/library/aa371151) class instead.

</dd> <dt>

**DedicatedIPAddresses**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The nodes unique IP addresses used for network traffic not associated with the cluster (for example, Telnet access to a specific node within the cluster).

</dd> <dt>

**DedicatedNetworkMask**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

This property is no longer in supported. Use the **DedicatedNetworkMasks** property instead.

</dd> <dt>

**DedicatedNetworkMasks**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property denotes the subnet masks for the dedicated IP addresses.

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

**DescriptorsPerAlloc**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

This property is no longer supported. Use the **MaxConnectionDescriptors** property instead.

</dd> <dt>

**FilterIcmp**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If set to **TRUE**, all ICMP traffic will be filtered by the cluster and accepted by only a single host. If set to **FALSE**, all hosts in the cluster will accept all ICMP traffic (this is the default behavior.)

</dd> <dt>

**HostPriority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**MicrosoftNLB\_Node**](microsoftnlb-node.md).**HostPriority**")
</dt> </dl>

A node's unique priority for handling default network traffic for TCP and UDP ports that are not otherwise specified in the [*port rules*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly) tab of the Network Load Balancing **Properties** dialog box. It is used in case a node within the cluster goes offline, and it determines which node within the cluster will take over handling this traffic if required. The allowed values for a node's [*host priority*](https://msdn.microsoft.com/library/aa369591#mscs-f---m-3-gly) range from 1 to the maximum number of nodes. Lower values indicate higher priorities (where 1 is the highest priority). Each node within the cluster must specify a unique host priority.

</dd> <dt>

**IpSecDescriptorTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

This property is no longer in use.

</dd> <dt>

**MaskSourceMAC**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, mangle source MAC address to prevent switch learning. Use a value of **FALSE** if the cluster is on a hub; this value optimizes switch performance by re-enabling learning.

</dd> <dt>

**MaxConnectionDescriptors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of connection-tracking descriptors that can be allocated at any time.

</dd> <dt>

**MaxDescriptorsPerAlloc**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

This property is no longer supported. Use the **MaxConnectionDescriptors** property instead.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The name of the node that owns this set of cluster configuration data. This is the name stored in the [**MicrosoftNLB\_Node**](microsoftnlb-node.md) **Name** property.

</dd> <dt>

**NumActions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

This property is no longer in use.

</dd> <dt>

**NumAliveMessages**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

This property is no longer in use.

</dd> <dt>

**NumberOfRules**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of defined port rules.

</dd> <dt>

**NumPackets**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

This property is no longer in use.

</dd> <dt>

**PersistSuspendOnReboot**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether a **WLBS\_SUSPENDED** state should persist after a reboot. If set to **TRUE**, a node that is in a suspended state when shut down will remain suspended when rebooted, regardless of the **ClusterModeOnStart** setting.

</dd> <dt>

**RemoteControlUDPPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

This property is no longer in use.

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

**TcpDescriptorTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

This property is no longer in use.

</dd> </dl>

## Remarks

After changing any [**MicrosoftNLB\_ClusterSetting**](microsoftnlb-clustersetting.md) properties, you must call [**LoadAllSettings**](microsoftnlb-clustersetting-loadallsettings.md) to bring the new values into effect. For more information, see **LoadAllSettings**.

The **MicrosoftNLB\_NodeSetting** class is derived from the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) class.

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

[**CIM\_Setting**](cim-setting.md)
</dt> <dt>

[**MicrosoftNLB\_ClusterSetting**](microsoftnlb-clustersetting.md)
</dt> </dl>

 

 





