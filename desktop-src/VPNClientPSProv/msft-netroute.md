---
title: MSFT\_NetRoute class
description: Represents the Route class in TCPIP WMIv2 provider.
audience: developer
ms.assetid: 78b07a1c-971d-4d3f-9eed-4c9e5a9bd169
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_NetRoute class
- MSFT_NetRoute class, described
topic_type:
- apiref
api_name:
- MSFT_NetRoute
- MSFT_NetRoute.Caption
- MSFT_NetRoute.Description
- MSFT_NetRoute.ElementName
- MSFT_NetRoute.InstanceID
- MSFT_NetRoute.DestinationAddress
- MSFT_NetRoute.AdminDistance
- MSFT_NetRoute.RouteMetric
- MSFT_NetRoute.IsStatic
- MSFT_NetRoute.TypeOfRoute
- MSFT_NetRoute.DestinationPrefix
- MSFT_NetRoute.InterfaceIndex
- MSFT_NetRoute.InterfaceAlias
- MSFT_NetRoute.NextHop
- MSFT_NetRoute.Publish
- MSFT_NetRoute.ValidLifetime
- MSFT_NetRoute.PreferredLifetime
- MSFT_NetRoute.Store
- MSFT_NetRoute.AddressFamily
- MSFT_NetRoute.Protocol
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_NetRoute class

Represents the Route class in TCPIP WMIv2 provider.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Network::Routes"), ClassVersion("1.0.0"), dynamic, provider("VpnClientPSProvider"), AMENDMENT]
class MSFT_NetRoute : CIM_NextHopRoute
{
  string   Caption;
  string   Description;
  string   ElementName;
  string   InstanceID;
  string   DestinationAddress;
  uint16   AdminDistance;
  uint16   RouteMetric;
  boolean  IsStatic;
  uint16   TypeOfRoute = 3;
  string   DestinationPrefix;
  uint32   InterfaceIndex;
  string   InterfaceAlias;
  string   NextHop;
  uint8    Publish;
  datetime ValidLifetime;
  datetime PreferredLifetime;
  uint8    Store;
  uint16   AddressFamily;
  uint16   Protocol;
};
```

## Members

The **MSFT\_NetRoute** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetRoute** class has these methods.



| Method                                 | Description                                                                                        |
|:---------------------------------------|:---------------------------------------------------------------------------------------------------|
| [**Create**](msft-netroute-create.md) | Create the Route.<br/>                                                                       |
| [**Select**](msft-netroute-select.md) | Selects the best local IP address and best route to reach the specified remote address.<br/> |



 

### Properties

The **MSFT\_NetRoute** class has these properties.

<dl> <dt>

**AddressFamily**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

To indicate whether the address family for this route is v4 or v6.

<dt>

<span id="IPv4"></span><span id="ipv4"></span><span id="IPV4"></span>

**IPv4** (2)


</dt> <dd></dd> <dt>

<span id="IPv6"></span><span id="ipv6"></span><span id="IPV6"></span>

**IPv6** (23)


</dt> <dd></dd> </dl>

</dd> <dt>

**AdminDistance**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The specific administrative distance of this route, overriding any default distances specified by the system or routing service.

This property is inherited from [**CIM\_NextHopRoute**](cim-nexthoproute.md).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Description property provides a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**DestinationAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The address which serves as the destination to be reached.

This property is inherited from [**CIM\_NextHopRoute**](cim-nexthoproute.md).

</dd> <dt>

**DestinationPrefix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The destination prefix.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information.

Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM\_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("InstanceID")
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following \\'preferred\\' algorithm:

&lt;OrgID&gt;:&lt;LocalID&gt;

Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon \\':\\', and where &lt;OrgID&gt; MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority. (This is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness &lt;OrgID&gt; MUST NOT contain a colon (\\':\\'). When using this algorithm, the first colon to appear in InstanceID MUST appear between &lt;OrgID&gt; and &lt;LocalID&gt;.

&lt;LocalID&gt; is chosen by the business entity and SHOULD not be re-used to identify different underlying (real-world) elements. If the above \\'preferred\\' algorithm is not used, the defining entity MUST assure that the resultant InstanceID is not re-used across any InstanceIDs produced by this or other providers for this instance\\'s NameSpace.

For DMTF defined instances, the \\'preferred\\' algorithm MUST be used with the &lt;OrgID&gt; set to \\'CIM\\'.

This property is inherited from [**CIM\_NextHopRoute**](cim-nexthoproute.md).

</dd> <dt>

**InterfaceAlias**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user-friendly interface name.

</dd> <dt>

**InterfaceIndex**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user-friendly interface index.

</dd> <dt>

**IsStatic**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TRUE indicates that this is a static route, and FALSE indicates a dynamically-learned route.

This property is inherited from [**CIM\_NextHopRoute**](cim-nexthoproute.md).

</dd> <dt>

**NextHop**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The next hop address or gateway address.

</dd> <dt>

**PreferredLifetime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Lifetime over which the route is preferred. The default value is infinite.

</dd> <dt>

**Protocol**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The routing mechanism via which this route was learned.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Local"></span><span id="local"></span><span id="LOCAL"></span>

**Local** (2)


</dt> <dd></dd> <dt>

<span id="NetMgmt"></span><span id="netmgmt"></span><span id="NETMGMT"></span>

**NetMgmt** (3)


</dt> <dd></dd> <dt>

<span id="Icmp"></span><span id="icmp"></span><span id="ICMP"></span>

**Icmp** (4)


</dt> <dd></dd> <dt>

<span id="Egp"></span><span id="egp"></span><span id="EGP"></span>

**Egp** (5)


</dt> <dd></dd> <dt>

<span id="Ggp"></span><span id="ggp"></span><span id="GGP"></span>

**Ggp** (6)


</dt> <dd></dd> <dt>

<span id="Hello"></span><span id="hello"></span><span id="HELLO"></span>

**Hello** (7)


</dt> <dd></dd> <dt>

<span id="Rip"></span><span id="rip"></span><span id="RIP"></span>

**Rip** (8)


</dt> <dd></dd> <dt>

<span id="IsIs"></span><span id="isis"></span><span id="ISIS"></span>

**IsIs** (9)


</dt> <dd></dd> <dt>

<span id="EsIs"></span><span id="esis"></span><span id="ESIS"></span>

**EsIs** (10)


</dt> <dd></dd> <dt>

<span id="Igrp"></span><span id="igrp"></span><span id="IGRP"></span>

**Igrp** (11)


</dt> <dd></dd> <dt>

<span id="Bbn"></span><span id="bbn"></span><span id="BBN"></span>

**Bbn** (12)


</dt> <dd></dd> <dt>

<span id="Ospf"></span><span id="ospf"></span><span id="OSPF"></span>

**Ospf** (13)


</dt> <dd></dd> <dt>

<span id="Bgp"></span><span id="bgp"></span><span id="BGP"></span>

**Bgp** (14)


</dt> <dd></dd> <dt>

<span id="Idpr"></span><span id="idpr"></span><span id="IDPR"></span>

**Idpr** (15)


</dt> <dd></dd> <dt>

<span id="Eigrp"></span><span id="eigrp"></span><span id="EIGRP"></span>

**Eigrp** (16)


</dt> <dd></dd> <dt>

<span id="Dvmrp"></span><span id="dvmrp"></span><span id="DVMRP"></span>

**Dvmrp** (17)


</dt> <dd></dd> <dt>

<span id="Rpl"></span><span id="rpl"></span><span id="RPL"></span>

**Rpl** (18)


</dt> <dd></dd> <dt>

<span id="Dhcp"></span><span id="dhcp"></span><span id="DHCP"></span>

**Dhcp** (19)


</dt> <dd></dd> </dl>

</dd> <dt>

**Publish**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

One of the following values: No: Not advertised in Route Advertisements. This is the default. Age: Advertised in Route Advertisements with a finite lifetime. Yes: Advertised in Route Advertisements with an infinite lifetime.

<dt>

<span id="No"></span><span id="no"></span><span id="NO"></span>

**No** (0)


</dt> <dd></dd> <dt>

<span id="Age"></span><span id="age"></span><span id="AGE"></span>

**Age** (1)


</dt> <dd></dd> <dt>

<span id="Yes"></span><span id="yes"></span><span id="YES"></span>

**Yes** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**RouteMetric**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

RouteMetric provides a numeric indication as to the preference of this route, compared to other routes that reach the same destination.

This property is inherited from [**CIM\_NextHopRoute**](cim-nexthoproute.md).

</dd> <dt>

**Store**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

One of the following values: Active: Change only lasts until next boot. Persistent: Change is persistent. This is the default.

<dt>

<span id="Persistent"></span><span id="persistent"></span><span id="PERSISTENT"></span>

**Persistent** (0)


</dt> <dd></dd> <dt>

<span id="Active"></span><span id="active"></span><span id="ACTIVE"></span>

**Active** (1)


</dt> <dd></dd> </dl>

</dd> <dt>

**TypeOfRoute**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An enumerated integer indicating whether the route is administrator-defined (value=2), computed (via a routing protocol/algorithm, value=3) or the actual route implemented in the network (value=4). The default is a computed route.

This property is inherited from [**CIM\_NextHopRoute**](cim-nexthoproute.md).

<dt>

<span id="Administrator_Defined_Route"></span><span id="administrator_defined_route"></span><span id="ADMINISTRATOR_DEFINED_ROUTE"></span>

**Administrator Defined Route** (2)


</dt> <dd></dd> <dt>

<span id="Computed_Route"></span><span id="computed_route"></span><span id="COMPUTED_ROUTE"></span>

**Computed Route** (3)


</dt> <dd></dd> <dt>

<span id="Actual_Route"></span><span id="actual_route"></span><span id="ACTUAL_ROUTE"></span>

**Actual Route** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**ValidLifetime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Lifetime over which the route is valid. The default value is infinite.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_NextHopRoute**](cim-nexthoproute.md)
</dt> </dl>

 

 





