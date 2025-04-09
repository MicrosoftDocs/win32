---
description: "RouteUsesEndpoint depicts the relationship between a next hop route and the local Endpoint that is used to transmit the traffic to the \\'next hop\\'."
ms.assetid: '800282ae-45a7-4be8-a02b-c6b553348caa'
title: "CIM\_RouteUsesEndpoint class"


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_RouteUsesEndpoint
- CIM_RouteUsesEndpoint.Antecedent
- CIM_RouteUsesEndpoint.Dependent
api_type: 
- DllExport
api_location: 
- netTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# CIM\_RouteUsesEndpoint class

RouteUsesEndpoint depicts the relationship between a next hop route and the local Endpoint that is used to transmit the traffic to the \\'next hop\\'.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, UMLPackagePath("CIM::Network::Routes"), Version("2.7.0"), AMENDMENT]
class CIM_RouteUsesEndpoint : CIM_Dependency
{
  CIM_ProtocolEndpoint REF Antecedent;
  CIM_NextHopRoute     REF Dependent;
};
```

## Members

The **CIM\_RouteUsesEndpoint** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_RouteUsesEndpoint** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ProtocolEndpoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("Antecedent"), [**Max**](/windows/win32/wmisdk/standard-qualifiers) (1)
</dt> </dl>

The endpoint used to reach the route's destination.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_NextHopRoute**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("Dependent")
</dt> </dl>

The route using the endpoint.

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

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

