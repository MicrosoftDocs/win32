---
title: MicrosoftNLB\_ClusterSetting class
description: The MicrosoftNLB\_ClusterSetting WMI class represents data that identifies the Network Load Balancing (NLB) cluster to which a node belongs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 280c56d3-f6c0-4f8d-9a28-7ff87104b181
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MicrosoftNLB_ClusterSetting class
- MicrosoftNLB_ClusterSetting class, described
topic_type:
- apiref
api_name:
- MicrosoftNLB_ClusterSetting
- MicrosoftNLB_ClusterSetting.SettingID
- MicrosoftNLB_ClusterSetting.Caption
- MicrosoftNLB_ClusterSetting.Description
- MicrosoftNLB_ClusterSetting.Name
- MicrosoftNLB_ClusterSetting.ClusterName
- MicrosoftNLB_ClusterSetting.ClusterIPAddress
- MicrosoftNLB_ClusterSetting.ClusterNetworkMask
- MicrosoftNLB_ClusterSetting.ClusterMACAddress
- MicrosoftNLB_ClusterSetting.MulticastSupportEnabled
- MicrosoftNLB_ClusterSetting.RemoteControlEnabled
- MicrosoftNLB_ClusterSetting.IGMPSupport
- MicrosoftNLB_ClusterSetting.ClusterIPToMulticastIP
- MicrosoftNLB_ClusterSetting.MulticastIPAddress
- MicrosoftNLB_ClusterSetting.AdapterGuid
- MicrosoftNLB_ClusterSetting.BDATeamActive
- MicrosoftNLB_ClusterSetting.BDATeamId
- MicrosoftNLB_ClusterSetting.BDATeamMaster
- MicrosoftNLB_ClusterSetting.BDAReverseHash
- MicrosoftNLB_ClusterSetting.IdentityHeartbeatEnabled
- MicrosoftNLB_ClusterSetting.UnicastInterHostCommSupportEnabled
api_location:
- WlbsProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MicrosoftNLB\_ClusterSetting class

The **MicrosoftNLB\_ClusterSetting** [*WMI class*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-22-gly) represents data that identifies the Network Load Balancing (NLB) [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly) to which a [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) belongs.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("Microsoft|NLB_Provider|V1.0"), AMENDMENT]
class MicrosoftNLB_ClusterSetting : CIM_Setting
{
  string  SettingID;
  string  Caption;
  string  Description;
  string  Name;
  string  ClusterName;
  string  ClusterIPAddress;
  string  ClusterNetworkMask;
  string  ClusterMACAddress;
  Boolean MulticastSupportEnabled;
  Boolean RemoteControlEnabled;
  Boolean IGMPSupport;
  Boolean ClusterIPToMulticastIP;
  string  MulticastIPAddress;
  string  AdapterGuid;
  Boolean BDATeamActive;
  string  BDATeamId;
  Boolean BDATeamMaster;
  Boolean BDAReverseHash;
  Boolean IdentityHeartbeatEnabled;
  Boolean UnicastInterHostCommSupportEnabled;
};
```

## Members

The **MicrosoftNLB\_ClusterSetting** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MicrosoftNLB\_ClusterSetting** class has these methods.



| Method                                                                     | Description                                                                                                                                     |
|:---------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AccessNLBRegParam**](microsoftnlb-clustersetting-accessnlbregparam.md) | This method gets or sets instance-specific or global NLB registry parameters.<br/>                                                        |
| [**LoadAllSettings**](microsoftnlb-clustersetting-loadallsettings.md)     | Propagates all current settings (cluster, node, and [*port rules*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly)) to the NLB driver.<br/> |
| [**SetDefaults**](microsoftnlb-clustersetting-setdefaults.md)             | Resets all of the properties of the **MicrosoftNLB\_ClusterSetting** class to their default values.<br/>                                  |
| [**SetPassword**](microsoftnlb-clustersetting-setpassword.md)             | This method is no longer available.<br/>                                                                                                  |



 

### Properties

The **MicrosoftNLB\_ClusterSetting** class has these properties.

<dl> <dt>

**AdapterGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The **GUID** of the adapter to which NLB is bound.

</dd> <dt>

**BDAReverseHash**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether bi-directional affinity (BDA) will reverse hash on the cluster that this network adapter is a part of. For more information on BDA, please see online help.

</dd> <dt>

**BDATeamActive**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether BDA is enabled on the cluster that this network adapter is a part of.

</dd> <dt>

**BDATeamId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The BDA team identifier of the cluster that this network adapter is a part of. The value of this property must be a GUID.

</dd> <dt>

**BDATeamMaster**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the cluster that this network adapter is a part of is the BDA master cluster.

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

**ClusterIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Cluster.InterconnectAddress")
</dt> </dl>

The cluster's primary [*IP address*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-6-gly) in standard dotted decimal notation ("xxx.xxx.xxx.xxx").

</dd> <dt>

**ClusterIPToMulticastIP**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

This property is no longer in use.

</dd> <dt>

**ClusterMACAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The media access control (MAC) address of the cluster.

</dd> <dt>

**ClusterName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The full Internet name for the NLB cluster (for example, "cluster.domain.com"). This name is used for the cluster as a whole and should be the same for all nodes in the cluster.

</dd> <dt>

**ClusterNetworkMask**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The subnet mask.

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

**IdentityHeartbeatEnabled**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

This property is no longer in use.

</dd> <dt>

**IGMPSupport**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Determines how multicast traffic is handled as follows.

<dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE**


</dt> <dd>

Default. NLB does not send IGMP join messages. Switches send all traffic (including multicast packets) to all switch ports.

</dd> <dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE**


</dt> <dd>

NLB sends IGMP join messages. Switches to send multicast traffic to specific ports rather than to all ports.

</dd> </dl>

</dd> <dt>

**MulticastIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The multicast IP address used to derive the cluster's MAC address if ClusterIPToMulticastIP is **FALSE**. A multicast IP group address should not interfere with other traffic or hinder any multicast applications that may be running on [*nodes*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) that are part of the subnet on which the NLB [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly) resides.

</dd> <dt>

**MulticastSupportEnabled**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether a multicast MAC address should be used for cluster operations. If this option is enabled, NLB converts the cluster MAC address belonging to the cluster adapter into a multicast address. It also ensures that the cluster's primary IP address resolves to this multicast address as part of the ARP protocol. At the same time, the adapter can now use its original, built-in MAC address, which, in unicast mode, was disabled.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The name of the node to which these settings apply. This is the name stored in the [**MicrosoftNLB\_Node**](microsoftnlb-node.md) [**Name**](https://msdn.microsoft.com/library/aa371151) property.

</dd> <dt>

**RemoteControlEnabled**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

This property is no longer in use. To access a remote node's settings or to perform actions such as enabling or disabling a [*port rule*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-7-gly), you must connect to each node individually using [*WMI*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-21-gly). For an example, see [Making Direct Connections](making-direct-connections.md).

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

**UnicastInterHostCommSupportEnabled**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property enables inter-host communication in a unicast cluster.

</dd> </dl>

## Remarks

Enumerating the **MicrosoftNLB\_ClusterSetting** class always returns one instance only. This instance represents the cluster settings for the [*provider node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-11-gly).

After changing any **MicrosoftNLB\_ClusterSetting** properties, you must call [**LoadAllSettings**](microsoftnlb-clustersetting-loadallsettings.md) on every node in the cluster to bring the new values into effect. For more information, see **LoadAllSettings**.

The **MicrosoftNLB\_ClusterSetting** class is derived from the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) class.

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

[**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md)
</dt> </dl>

 

 





