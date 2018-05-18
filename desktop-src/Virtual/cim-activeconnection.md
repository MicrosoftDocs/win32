---
title: CIM\_ActiveConnection class
description: Defines a connection that is currently turned on and configured to provide communication between two CIM\_ServiceAccessPoint objects.
ms.assetid: 'bce797b1-8912-47c9-a2aa-f8aa9a816f15'
keywords: ["CIM_ActiveConnection class Hyper-V", "CIM_ActiveConnection class Hyper-V , described"]
topic_type:
- apiref
api_name:
- CIM_ActiveConnection
- CIM_ActiveConnection.Antecedent
- CIM_ActiveConnection.Dependent
- CIM_ActiveConnection.TrafficType
- CIM_ActiveConnection.OtherTrafficDescription
- CIM_ActiveConnection.IsUnidirectional
api_location:
- Root\virtualization
api_type:
- Schema
---

# CIM\_ActiveConnection class

Defines a connection that is currently turned on and configured to provide communication between two **CIM\_ServiceAccessPoint** objects. **CIM\_ActiveConnection** is used when the connection is not treated as a **CIM\_ManagedElement** object. Service access points that are connected by an active connection are typically at the same networking or application layer.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Association, Version("2.10.0"), AMENDMENT]
class CIM_ActiveConnection : CIM_SAPSAPDependency
{
  CIM_ServiceAccessPoint REF Antecedent;
  CIM_ServiceAccessPoint REF Dependent;
  uint16                     TrafficType;
  string                     OtherTrafficDescription;
  boolean                    IsUnidirectional;
};
```

## Members

The **CIM\_ActiveConnection** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ActiveConnection** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ServiceAccessPoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The service access point that is connected to the other service access point through the active connection. **CIM\_ServiceAccessPoint** object. In a unidirectional connection, this access point is the one that is transmitting data.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ServiceAccessPoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The service access point that is configured to communicate or is actively communicating with the service access point specified in the **Antecedent** property. In a unidirectional connection, this access point is the one that is receiving data.

</dd> <dt>

**IsUnidirectional**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the connection is unidirectional; false if the connection is bidirectional. When the connection is unidirectional, the **Antecedent** property specifies the access point that is transmitting data. In a bidirectional connection, **Antecedent** can specify either access point assigned to the connection.

</dd> <dt>

**OtherTrafficDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("No value"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_ActiveConnection**.**TrafficType**")
</dt> </dl>

> [!Note]  
> This property is deprecated. Instead, we recommend that you specify this information in the addressing, protocol, and basic functionality of the endpoints.

 

A description of the traffic type that is specified when the **TrafficType** property is set to "1" (Other).

</dd> <dt>

**TrafficType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("No value"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("**CIM\_ActiveConnection**.**OtherTrafficDescription**")
</dt> </dl>

> [!Note]  
> This property is deprecated. Instead, we recommend that you specify this information in the addressing, protocol, and basic functionality of the endpoints.

 

The type of traffic that is transmitted over this connection.

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_SAPSAPDependency**](cim-sapsapdependency.md)
</dt> </dl>

 

 





