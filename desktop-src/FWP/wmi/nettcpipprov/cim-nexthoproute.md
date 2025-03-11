---
description: "Represents one of a series of 'hops' to reach a network destination. A route is administratively defined, or calculated/learned by a particular routing process."
ms.assetid: '2c1d0fdd-0914-4c81-a1ff-d8104c5c734d'
title: "CIM\_NextHopRoute class"


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
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
api_type: 
- DllExport
api_location: 
- netTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# CIM\_NextHopRoute class

Represents one of a series of 'hops' to reach a network destination. A route is administratively defined, or calculated/learned by a particular routing process. A ConcreteDependency association may be instantiated between a route and its routing service to indicate this. (In this scenario, the route is dependent on the service.)

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

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("InstanceID")
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

 

</dd> <dt>

**IsStatic**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** indicates that this is a static route, and **FALSE** indicates a dynamically-learned route.

</dd> <dt>

**RouteMetric**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides a numeric indication as to the preference of this route, compared to other routes that reach the same destination.

</dd> <dt>

**TypeOfRoute**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the type of route.

<dl> <dt>

<span id="Administrator_Defined_Route"></span><span id="administrator_defined_route"></span><span id="ADMINISTRATOR_DEFINED_ROUTE"></span>**Administrator Defined Route** (2)
</dt> <dt>

<span id="Computed_Route"></span><span id="computed_route"></span><span id="COMPUTED_ROUTE"></span>**Computed Route** (3)
</dt> <dt>

<span id="Actual_Route"></span><span id="actual_route"></span><span id="ACTUAL_ROUTE"></span>**Actual Route** (4)
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\standardcimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> </dl>

 

