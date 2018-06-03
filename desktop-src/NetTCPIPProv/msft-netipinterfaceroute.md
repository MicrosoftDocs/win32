---
Description: Represents an association between a TCP/IP network interface and an IP route.
ms.assetid: 52b4b78f-5648-4a70-9da5-49eff23518ca
title: MSFT\_NetIPInterfaceRoute class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The [**CIM\_LANEndpoint**](https://msdn.microsoft.com/library/mt269482) object for the communication endpoint associated with the TCP/IP network interface that is used to reach the destination of the route.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetRoute**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
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

[**CIM\_LANEndpoint**](https://msdn.microsoft.com/library/mt269482)
</dt> <dt>

[**MSFT\_NetRoute**](msft-netroute.md)
</dt> </dl>

 

 




