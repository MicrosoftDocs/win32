---
description: Represents an IP route for the TCP/IP (Internet Protocol Suite) WMIv2 provider.
ms.assetid: 06dfd275-25f9-48bc-8361-87ab1c905c17
title: MSFT\_NetRoute class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
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
api_type: 
- DllExport
api_location: 
- NetTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetRoute class

Represents an IP route for the TCP/IP (Internet Protocol Suite) WMIv2 provider.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Network::Routes"), ClassVersion("1.0.0"), dynamic, provider("nettcpip"), AMENDMENT]
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



| Method                                 | Description                                                       |
|:---------------------------------------|:------------------------------------------------------------------|
| [**Create**](create-msft-netroute.md) | Create an IP route.<br/>                                    |
| [**Find**](find-msft-netroute.md)     | Retrieves an IP route to the specified remote address.<br/> |



 

### Properties

The **MSFT\_NetRoute** class has these properties.

<dl> <dt>

**AddressFamily**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a value that indicates whether the route uses the IPv4 or IPv6 address family. This property gets one of the following values.

<dl> <dt>

<span id="IPv4"></span><span id="ipv4"></span><span id="IPV4"></span>**IPv4** (2)
</dt> <dt>

<span id="IPv6"></span><span id="ipv6"></span><span id="IPV6"></span>**IPv6** (23)
</dt> </dl>

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

Qualifiers: [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (64)
</dt> </dl>

Contains a short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides a textual description of the object.

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

Gets the destination prefix of the route.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains a user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier)
</dt> </dl>

Uniquely and opaquely identifies an instance of this class within the scope of the containing Namespace.

> \[!Important\]In order to ensure uniqueness within the Namespace, the value of **InstanceID** should be constructed in the following pattern:
>
> *OrgID*:*LocalID*
>
> *OrgID* must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity defining the **InstanceID**, or be a registered ID that is assigned by a recognized global authority. This is similar to the structure of Schema class names. In addition, to ensure uniqueness the first colon in **InstanceID** must be between the *OrgID* and*LocalID*. Therefor the *OrgID* must not contain a colon (':').
>
> *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
>
> If the preceding pattern is not used, the defining entity must assure that the resultant **InstanceID** is not re-used across any **InstanceID**s produced by this or other providers for this Namespace.
>
> For Distributed Management Task Force (DMTF) defined instances, the pattern must be used with the *OrgID* set to CIM.

 

This property is inherited from [**CIM\_NextHopRoute**](cim-nexthoproute.md).

</dd> <dt>

**InterfaceAlias**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the interface alias of the route.

</dd> <dt>

**InterfaceIndex**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the interface index of the route.

</dd> <dt>

**IsStatic**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** indicates that this is a static route, and **FALSE** indicates a dynamically-learned route.

This property is inherited from [**CIM\_NextHopRoute**](cim-nexthoproute.md).

</dd> <dt>

**NextHop**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the address of the next hop for the route.

</dd> <dt>

**PreferredLifetime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the preferred end time of the lifetime of the route. The default value for this property is infinite.

</dd> <dt>

**Protocol**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The protocol from which the route was learned.



| Value                                                                                                                                                                                                                       | Meaning                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span><dl> <dt>**Other**</dt> <dt>1</dt> </dl>         | other protocol<br/>                                          |
| <span id="Local"></span><span id="local"></span><span id="LOCAL"></span><dl> <dt>**Local**</dt> <dt>2</dt> </dl>         | local routing<br/>                                           |
| <span id="NetMgmt"></span><span id="netmgmt"></span><span id="NETMGMT"></span><dl> <dt>**NetMgmt**</dt> <dt>3</dt> </dl> | Network Management static routing protocol (NETMGMT)<br/>    |
| <span id="Icmp"></span><span id="icmp"></span><span id="ICMP"></span><dl> <dt>**Icmp**</dt> <dt>4</dt> </dl>             | Internet Control Message Protocol (ICMP)<br/>                |
| <span id="Egp"></span><span id="egp"></span><span id="EGP"></span><dl> <dt>**Egp**</dt> <dt>5</dt> </dl>                 | Exterior Gateway Protocol (EGP)<br/>                         |
| <span id="Ggp"></span><span id="ggp"></span><span id="GGP"></span><dl> <dt>**Ggp**</dt> <dt>6</dt> </dl>                 | Gateway-to-Gateway Protocol (GGP)<br/>                       |
| <span id="Hello"></span><span id="hello"></span><span id="HELLO"></span><dl> <dt>**Hello**</dt> <dt>7</dt> </dl>         | Hellospeak protocol (HELLO)<br/>                             |
| <span id="Rip"></span><span id="rip"></span><span id="RIP"></span><dl> <dt>**Rip**</dt> <dt>8</dt> </dl>                 | Routing Information Protocol (RIP)<br/>                      |
| <span id="IsIs"></span><span id="isis"></span><span id="ISIS"></span><dl> <dt>**IsIs**</dt> <dt>9</dt> </dl>             | Intermediate System to Intermediate System (IS-IS)<br/>      |
| <span id="EsIs"></span><span id="esis"></span><span id="ESIS"></span><dl> <dt>**EsIs**</dt> <dt>10</dt> </dl>            | End System to Intermediate System (ES-IS)<br/>               |
| <span id="Igrp"></span><span id="igrp"></span><span id="IGRP"></span><dl> <dt>**Igrp**</dt> <dt>11</dt> </dl>            | Interior Gateway Routing Protocol (IGRP)<br/>                |
| <span id="Bbn"></span><span id="bbn"></span><span id="BBN"></span><dl> <dt>**Bbn**</dt> <dt>12</dt> </dl>                | BBN protocol<br/>                                            |
| <span id="Ospf"></span><span id="ospf"></span><span id="OSPF"></span><dl> <dt>**Ospf**</dt> <dt>13</dt> </dl>            | Open Shortest Path First (OSPF)<br/>                         |
| <span id="Bgp"></span><span id="bgp"></span><span id="BGP"></span><dl> <dt>**Bgp**</dt> <dt>14</dt> </dl>                | Border Gateway Protocol (BGP)<br/>                           |
| <span id="Idpr"></span><span id="idpr"></span><span id="IDPR"></span><dl> <dt>**Idpr**</dt> <dt>15</dt> </dl>            | Interdomain Routing Protocol (IDPR)<br/>                     |
| <span id="Eigrp"></span><span id="eigrp"></span><span id="EIGRP"></span><dl> <dt>**Eigrp**</dt> <dt>16</dt> </dl>        | Enhanced Interior Gateway Routing Protocol (EIGRP)<br/>      |
| <span id="Dvmrp"></span><span id="dvmrp"></span><span id="DVMRP"></span><dl> <dt>**Dvmrp**</dt> <dt>17</dt> </dl>        | Distance Vector Multicast Routing Protocol (DVMRP)<br/>      |
| <span id="Rpl"></span><span id="rpl"></span><span id="RPL"></span><dl> <dt>**Rpl**</dt> <dt>18</dt> </dl>                | Routing Protocol for Low-Power and Lossy Networks (RPL)<br/> |
| <span id="Dhcp"></span><span id="dhcp"></span><span id="DHCP"></span><dl> <dt>**Dhcp**</dt> <dt>19</dt> </dl>            | Dynamic Host Configuration Protocol (DHCP)<br/>              |



 

</dd> <dt>

**Publish**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets a value that indicates how to advertise the route. The default value for this property is 0.



| Value                                                                                                                                                                                                       | Meaning                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <span id="No"></span><span id="no"></span><span id="NO"></span><dl> <dt>**No**</dt> <dt>0</dt> </dl>     | Do not advertise the route.<br/>                  |
| <span id="Age"></span><span id="age"></span><span id="AGE"></span><dl> <dt>**Age**</dt> <dt>1</dt> </dl> | Advertise the route for a specific interval.<br/> |
| <span id="Yes"></span><span id="yes"></span><span id="YES"></span><dl> <dt>**Yes**</dt> <dt>2</dt> </dl> | Advertise the route indefinitely.<br/>            |



 

</dd> <dt>

**RouteMetric**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides a numeric indication as to the preference of this route, compared to other routes that reach the same destination.

This property is inherited from [**CIM\_NextHopRoute**](cim-nexthoproute.md).

</dd> <dt>

**Store**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets a value that indicates whether the state of the route persists after a reboot. This property can contain one of the following values.



| Value                                                                                                                                                                                                                                   | Meaning                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <span id="Persistent"></span><span id="persistent"></span><span id="PERSISTENT"></span><dl> <dt>**Persistent**</dt> <dt>0</dt> </dl> | The state of the route persists after a reboot.<br/>         |
| <span id="Active"></span><span id="active"></span><span id="ACTIVE"></span><dl> <dt>**Active**</dt> <dt>1</dt> </dl>                 | The state of the route does not persist after a reboot.<br/> |



 

</dd> <dt>

**TypeOfRoute**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the type of route.

This property is inherited from [**CIM\_NextHopRoute**](cim-nexthoproute.md).

<dl> <dt>

<span id="Administrator_Defined_Route"></span><span id="administrator_defined_route"></span><span id="ADMINISTRATOR_DEFINED_ROUTE"></span>**Administrator Defined Route** (2)
</dt> <dt>

<span id="Computed_Route"></span><span id="computed_route"></span><span id="COMPUTED_ROUTE"></span>**Computed Route** (3)
</dt> <dt>

<span id="Actual_Route"></span><span id="actual_route"></span><span id="ACTUAL_ROUTE"></span>**Actual Route** (4)
</dt> </dl>

</dd> <dt>

**ValidLifetime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the valid end time of the lifetime of the route. The default value for this property is infinite.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_NextHopRoute**](cim-nexthoproute.md)
</dt> <dt>

[NetTCPIP Provider Classes](net-tcpip-classes.md)
</dt> </dl>

 

