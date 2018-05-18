---
title: Win32\_IP4RouteTable class
description: The Win32\_IP4RouteTable \ 32; WMI class represents information that governs the routing of network data packets.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'cb313097-d5d1-4b8e-bee5-20a894c6788d'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Win32_IP4RouteTable class", "Win32_IP4RouteTable class, described"]
topic_type:
- apiref
api_name:
- Win32_IP4RouteTable
- Win32_IP4RouteTable.Age
- Win32_IP4RouteTable.Caption
- Win32_IP4RouteTable.Description
- Win32_IP4RouteTable.Destination
- Win32_IP4RouteTable.Information
- Win32_IP4RouteTable.InstallDate
- Win32_IP4RouteTable.InterfaceIndex
- Win32_IP4RouteTable.Mask
- Win32_IP4RouteTable.Metric1
- Win32_IP4RouteTable.Metric2
- Win32_IP4RouteTable.Metric3
- Win32_IP4RouteTable.Metric4
- Win32_IP4RouteTable.Metric5
- Win32_IP4RouteTable.Name
- Win32_IP4RouteTable.NextHop
- Win32_IP4RouteTable.Protocol
- Win32_IP4RouteTable.Status
- Win32_IP4RouteTable.Type
api_location:
- Wmipiprt.dll
api_type:
- DllExport
---

# Win32\_IP4RouteTable class

The **Win32\_IP4RouteTable** [WMI class](https://msdn.microsoft.com/library/aa393244) represents information that governs the routing of network data packets. For example, Internet packets are usually sent to a gateway and local packets are routed directly by the client computer. Administrators can use this information to trace problems associated with misrouted packets, and also direct a computer to a new gateway as necessary. This class only represents the information shown as a result of typing the **route print** command from the command prompt.

This class is only applicable to IPv4 and does not return IPX or IPv6 data. For more information, see [IPv6 and IPv4 Support in WMI](https://msdn.microsoft.com/library/aa822883).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[dynamic, provider("RouteProvider"), SupportsCreate, CreateBy("PutInstance"), SupportsDelete, DeleteBy("DeleteInstance"), SupportsUpdate, UUID("{ABEE8C61-A43F-4088-0081-9D00B3FF6545}"), AMENDMENT]
class Win32_IP4RouteTable : CIM_LogicalElement
{
  sint32   Age;
  string   Caption;
  string   Description;
  string   Destination;
  string   Information;
  datetime InstallDate;
  sint32   InterfaceIndex;
  string   Mask;
  sint32   Metric1;
  sint32   Metric2;
  sint32   Metric3;
  sint32   Metric4;
  sint32   Metric5;
  string   Name;
  string   NextHop;
  uint32   Protocol;
  string   Status;
  uint32   Type;
};
```

## Members

The **Win32\_IP4RouteTable** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_IP4RouteTable** class has these properties.

<dl> <dt>

**Age**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of seconds since this route was last updated or otherwise determined to be correct. Whether the routing information is outdated can only be determined by knowing the routing protocol by which the route was learned.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

Short description of the object. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the object. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**Destination**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Destination IP address for this route.

</dd> <dt>

**Information**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to Management Information Base (MIB) definitions specific to the particular routing protocol that handles this route, as determined by the value specified in the route ipRouteProto value. If this information is not present, its value should be set to the OBJECT IDENTIFIER {0 0}, which is a syntactically valid object identifier, and any conforming implementation of ASN.1 and BER must be able to generate and recognize this value.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Object was installed. This property does not need a value to indicate that the object is installed. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**InterfaceIndex**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

IP address of the next hop of this route. The value in this property is the same as the value in the **InterfaceIndex** property in the instances of [**Win32\_NetworkAdapter**](https://msdn.microsoft.com/library/aa394216) and [**Win32\_NetworkAdapterConfiguration**](https://msdn.microsoft.com/library/aa394217) that represent the network interface of the next hop of the route.

In the case of a route bound to an interface that is realized using a broadcast medium, the value of this field is the agent IP address on that interface.

</dd> <dt>

**Mask**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Mask used in this entry. Masks should be joined with a logical AND to the destination address before being compared to the value in the ipRouteDest field.

</dd> <dt>

**Metric1**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Primary routing metric for this route. The routing protocol specified in the ipRouteProto value for the route determines the interpretation of this property. Set the value of this property to -1 if it is not used.

</dd> <dt>

**Metric2**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Alternate routing metric for this route. The routing protocol specified in the ipRouteProto value for the route determines the interpretation of this property. Set the value of this property to -1 if it is not used.

</dd> <dt>

**Metric3**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Alternate routing metric for this route. The routing protocol specified in the ipRouteProto value for the route determines the interpretation of this property. Set the value of this property to -1 if it is not used.

</dd> <dt>

**Metric4**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Alternate routing metric for this route. The routing protocol specified in the ipRouteProto value for the route determines the interpretation of this property. Set the value of this property to -1 if it is not used.

</dd> <dt>

**Metric5**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Alternate routing metric for this route. The routing protocol specified in the ipRouteProto value for the route determines the interpretation of this property. Set the value of this property to -1 if it is not used.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Label by which the object is known. When subclassed, this property can be overridden to be a key property. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**NextHop**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

IP address of the next hop of this route. For a route that is bound to an interface realized via a broadcast medium, the value of this field is the agent IP address on that interface.

</dd> <dt>

**Protocol**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Routing mechanism through which this route was learned. Inclusion of values for gateway routing protocols does not imply that hosts must support those protocols.

<dt>

<span id="other"></span><span id="OTHER"></span>

**other** (1)


</dt> <dd></dd> <dt>

<span id="local"></span><span id="LOCAL"></span>

**local** (2)


</dt> <dd></dd> <dt>

<span id="netmgmt"></span><span id="NETMGMT"></span>

**netmgmt** (3)


</dt> <dd></dd> <dt>

<span id="icmp"></span><span id="ICMP"></span>

**icmp** (4)


</dt> <dd></dd> <dt>

<span id="egp"></span><span id="EGP"></span>

**egp** (5)


</dt> <dd></dd> <dt>

<span id="ggp"></span><span id="GGP"></span>

**ggp** (6)


</dt> <dd></dd> <dt>

<span id="hello"></span><span id="HELLO"></span>

**hello** (7)


</dt> <dd></dd> <dt>

<span id="rip"></span><span id="RIP"></span>

**rip** (8)


</dt> <dd></dd> <dt>

<span id="is-is"></span><span id="IS-IS"></span>

**is-is** (9)


</dt> <dd></dd> <dt>

<span id="es-is"></span><span id="ES-IS"></span>

**es-is** (10)


</dt> <dd></dd> <dt>

<span id="ciscoIgrp"></span><span id="ciscoigrp"></span><span id="CISCOIGRP"></span>

**ciscoIgrp** (11)


</dt> <dd></dd> <dt>

<span id="bbnSpfIgp"></span><span id="bbnspfigp"></span><span id="BBNSPFIGP"></span>

**bbnSpfIgp** (12)


</dt> <dd></dd> <dt>

<span id="ospf"></span><span id="OSPF"></span>

**ospf** (13)


</dt> <dd></dd> <dt>

<span id="bgp"></span><span id="BGP"></span>

**bgp** (14)


</dt> <dd></dd> </dl>

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

Current status of the object. Various operational and nonoperational statuses can be defined. Operational statuses include: "OK", "Degraded", and "Pred Fail" (an element, such as a SMART-enabled hard disk disk drive, may be functioning properly but predicting a failure in the near future). Nonoperational statuses include: "Error", "Starting", "Stopping", and "Service". The latter, "Service", could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is online, yet the managed element is neither "OK" nor in one of the other states. This property is inherited from the [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) class.

The values are:

<dl><span id="_OK_"></span><span id="_ok_"></span><dt>

**"OK"**
</dt><span id="_Error_"></span><span id="_error_"></span><span id="_ERROR_"></span><dt>

**"Error"**
</dt><span id="_Degraded_"></span><span id="_degraded_"></span><span id="_DEGRADED_"></span><dt>

**"Degraded"**
</dt><span id="_Unknown_"></span><span id="_unknown_"></span><span id="_UNKNOWN_"></span><dt>

**"Unknown"**
</dt><span id="_Pred_Fail_"></span><span id="_pred_fail_"></span><span id="_PRED_FAIL_"></span><dt>

**"Pred Fail"**
</dt><span id="_Starting_"></span><span id="_starting_"></span><span id="_STARTING_"></span><dt>

**"Starting"**
</dt><span id="_Stopping_"></span><span id="_stopping_"></span><span id="_STOPPING_"></span><dt>

**"Stopping"**
</dt><span id="_Service_"></span><span id="_service_"></span><span id="_SERVICE_"></span><dt>

**"Service"**
</dt> </dl>

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Type of route. The following list lists the values.

<dt>

<span id="other"></span><span id="OTHER"></span>

**other** (1)


</dt> <dd></dd> <dt>

<span id="invalid"></span><span id="INVALID"></span>

**invalid** (2)


</dt> <dd></dd> <dt>

<span id="direct"></span><span id="DIRECT"></span>

**direct** (3)


</dt> <dd></dd> <dt>

<span id="indirect"></span><span id="INDIRECT"></span>

**indirect** (4)


</dt> <dd></dd> </dl>

Values 3 (Direct) and 4 (Indirect) refer to direct and indirect routing in the IP architecture. Setting this object to the value 2 (Invalid) invalidates the corresponding entry in the RouteTable object by disassociating the entry's destination from the entry's route. An agent may leave an invalid entry in the table. Therefore, management stations can receive information from agents that applies to entries not currently in use. To interpret such entries, examine the relevant ipRouteType object.

</dd> </dl>

## Remarks

The **Win32\_IP4RouteTable** class is derived from [**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipiprt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipiprt.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> </dl>

 

 





