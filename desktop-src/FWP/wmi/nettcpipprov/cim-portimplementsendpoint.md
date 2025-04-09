---
description: Associates a logical port with one or more protocol endpoints that are implemented on it.
ms.assetid: 80f294fc-1427-489a-a47e-f4811d0b35fd
title: CIM\_PortImplementsEndpoint class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_PortImplementsEndpoint
- CIM_PortImplementsEndpoint.Antecedent
- CIM_PortImplementsEndpoint.Dependent
api_type: 
- DllExport
api_location: 
- netTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# CIM\_PortImplementsEndpoint class

Associates a logical port with one or more protocol endpoints that are implemented on it. This class specializes the [**DeviceSAPImplementation**](cim-devicesapimplementation.md) association. It indicates that the referenced endpoint is dependent on the operations of the port device.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, UMLPackagePath("CIM::Device::Ports"), Version("2.10.0"), AMENDMENT]
class CIM_PortImplementsEndpoint : CIM_DeviceSAPImplementation
{
  CIM_LogicalPort      REF Antecedent;
  CIM_ProtocolEndpoint REF Dependent;
};
```

## Members

The **CIM\_PortImplementsEndpoint** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_PortImplementsEndpoint** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalPort**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

A [**CIM\_LogicalPort**](cim-logicalport.md) that represents the Device behind the protocol endpoint.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ProtocolEndpoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("Dependent")
</dt> </dl>

A [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md) that is implemented on the logical port.

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

[**CIM\_DeviceSAPImplementation**](cim-devicesapimplementation.md)
</dt> </dl>

 

