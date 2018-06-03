---
title: CIM\_NextHopRoute class
description: NextHopRoute represents one of a series of \\'hops\\' to reach a network destination.
audience: developer
ms.assetid: c1d8e36d-4279-4fcc-90c6-58f91eb96abe
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_NextHopRoute class
- CIM_NextHopRoute class, described
topic_type:
- apiref
api_name:
- CIM_NextHopRoute
- CIM_NextHopRoute.Caption
- CIM_NextHopRoute.Description
- CIM_NextHopRoute.ElementName
- CIM_NextHopRoute.InstanceID
- CIM_NextHopRoute.DestinationAddress
- CIM_NextHopRoute.AdminDistance
- CIM_NextHopRoute.RouteMetric
- CIM_NextHopRoute.IsStatic
- CIM_NextHopRoute.TypeOfRoute
api_location:
- VPNClientPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CIM\_NextHopRoute class

NextHopRoute represents one of a series of \\'hops\\' to reach a network destination. A route is administratively defined, or calculated/learned by a particular routing process. A ConcreteDependency associaton may be instantiated between a route and its routing service to indicate this. (In this scenario, the route is dependent on the service.)

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Network::Routes"), Version("2.19.0"), AMENDMENT]
class CIM_NextHopRoute : CIM_ManagedElement
{
  string  Caption;
  string  Description;
  string  ElementName;
  string  InstanceID;
  string  DestinationAddress;
  uint16  AdminDistance;
  uint16  RouteMetric;
  boolean IsStatic;
  uint16  TypeOfRoute = 3;
};
```

## Members

The **CIM\_NextHopRoute** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_NextHopRoute** class has these properties.

<dl> <dt>

**AdminDistance**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The specific administrative distance of this route, overriding any default distances specified by the system or routing service.

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

</dd> <dt>

**IsStatic**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TRUE indicates that this is a static route, and FALSE indicates a dynamically-learned route.

</dd> <dt>

**RouteMetric**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

RouteMetric provides a numeric indication as to the preference of this route, compared to other routes that reach the same destination.

</dd> <dt>

**TypeOfRoute**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An enumerated integer indicating whether the route is administrator-defined (value=2), computed (via a routing protocol/algorithm, value=3) or the actual route implemented in the network (value=4). The default is a computed route.

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

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> </dl>

 

 





