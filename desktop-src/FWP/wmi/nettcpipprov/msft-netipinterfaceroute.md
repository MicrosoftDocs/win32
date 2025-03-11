---
description: Represents an association between a TCP/IP network interface and an IP route.
ms.assetid: 52b4b78f-5648-4a70-9da5-49eff23518ca
title: MSFT\_NetIPInterfaceRoute class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetIPInterfaceRoute
- MSFT_NetIPInterfaceRoute.Antecedent
- MSFT_NetIPInterfaceRoute.Dependent
api_type: 
- DllExport
api_location: 
- NetTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetIPInterfaceRoute class

Represents an association between a TCP/IP network interface and an IP route.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, UMLPackagePath("CIM::Network::Routes"), ClassVersion("1.0.0"), dynamic, provider("nettcpip"), AMENDMENT]
class MSFT_NetIPInterfaceRoute : CIM_RouteUsesEndpoint
{
  CIM_LANEndpoint REF Antecedent;
  MSFT_NetRoute   REF Dependent;
};
```

## Members

The **MSFT\_NetIPInterfaceRoute** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetIPInterfaceRoute** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LANEndpoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Max**](/windows/win32/wmisdk/standard-qualifiers) (1), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

The [**CIM\_LANEndpoint**](./cim-lanendpoint.md) object for the communication endpoint associated with the TCP/IP network interface that is used to reach the destination of the route.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetRoute**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("Dependent")
</dt> </dl>

The [**MSFT\_NetRoute**](msft-netroute.md) object for the route associated with the interface.

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

[**CIM\_RouteUsesEndpoint**](cim-routeusesendpoint.md)
</dt> <dt>

[**CIM\_LANEndpoint**](./cim-lanendpoint.md)
</dt> <dt>

[**MSFT\_NetRoute**](msft-netroute.md)
</dt> </dl>

 

