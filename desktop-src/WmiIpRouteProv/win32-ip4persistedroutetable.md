---
title: Win32\_IP4PersistedRouteTable class
description: The Win32\_IP4PersistedRouteTable WMI class represents persisted IP routes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '474ce759-0b70-4925-a6b9-cbbb6ab1d4ac'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Win32_IP4PersistedRouteTable class", "Win32_IP4PersistedRouteTable class, described"]
topic_type:
- apiref
api_name:
- Win32_IP4PersistedRouteTable
- Win32_IP4PersistedRouteTable.Caption
- Win32_IP4PersistedRouteTable.Description
- Win32_IP4PersistedRouteTable.Destination
- Win32_IP4PersistedRouteTable.InstallDate
- Win32_IP4PersistedRouteTable.Mask
- Win32_IP4PersistedRouteTable.Metric1
- Win32_IP4PersistedRouteTable.Name
- Win32_IP4PersistedRouteTable.NextHop
- Win32_IP4PersistedRouteTable.Status
api_location:
- Wmipiprt.dll
api_type:
- DllExport
---

# Win32\_IP4PersistedRouteTable class

The **Win32\_IP4PersistedRouteTable** [WMI class](https://msdn.microsoft.com/library/aa393244) represents persisted IP routes. By default, the routes added to the routing table are not permanent. Rebooting the computer clears the routes from the table. However, the following command makes the route persist after the computer is restarted: **route -p add**.

Persistent entries are automatically inserted again in the route table each time the route table is rebuilt. The operating system stores persistent routes in the registry. An entry can be removed through the method call [**SWbemServices.Delete**](https://msdn.microsoft.com/library/aa393860) for scripting or [**IWbemServices::DeleteInstance**](https://msdn.microsoft.com/library/aa392101) for C++ programming.

This class is only applicable to IPv4 and does not return IPX or IPv6 data. For more information, see [IPv6 and IPv4 Support in WMI](https://msdn.microsoft.com/library/aa822883).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[dynamic, provider("RouteProvider"), UUID("{2CAF4666-AC9B-45AB-00A6-AF8C537794C2}"), SupportsCreate, CreateBy("PutInstance"), SupportsDelete, DeleteBy("DeleteInstance"), AMENDMENT]
class Win32_IP4PersistedRouteTable : CIM_LogicalElement
{
  string   Caption;
  string   Description;
  string   Destination;
  datetime InstallDate;
  string   Mask;
  sint32   Metric1;
  string   Name;
  string   NextHop;
  string   Status;
};
```

## Members

The **Win32\_IP4PersistedRouteTable** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_IP4PersistedRouteTable** class has these properties.

<dl> <dt>

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

Destination IP address for this persisted route.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Object was installed. This property does not need a value to indicate that the object is installed. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

</dd> <dt>

**Mask**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Mask used in this persisted entry. Use the logical AND operation to combine the mask with the destination address. Compare the result to the value in the ipRouteDest field.

</dd> <dt>

**Metric1**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Primary routing metric for this persisted route. The semantics of this metric are determined by the routing protocol specified in the route's ipRouteProto value. If this property is not used, its value should be set to -1.

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

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

IP address of the next hop of this persisted route. If the route is bound to an interface that is realized via a broadcast medium, this field contains the agent's IP address on that interface.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

Current status of the object. Various operational and nonoperational statuses can be defined. Operational statuses include: "OK", "Degraded", and "Pred Fail" (an element, such as a SMART-enabled hard disk drive, may be functioning properly but predicting a failure in the near future). Nonoperational statuses include: "Error", "Starting", "Stopping", and "Service". The latter, "Service", could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is online, yet the managed element is neither "OK" nor in one of the other states. This property is inherited from [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898).

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

</dd> </dl>

## Remarks

The **Win32\_IP4PersistedRouteTable** class is derived from [**CIM\_LogicalElement**](https://msdn.microsoft.com/library/aa387892) which derives from the [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) class.

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

 

 





