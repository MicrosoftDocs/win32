---
description: Defines a connection that is currently turned on and configured to provide communication between two CIM\_ServiceAccessPoint objects.
ms.assetid: 03f8e43f-a77b-46e2-bb7d-c29758c65aee
title: CIM_ActiveConnection class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ActiveConnection
- CIM_ActiveConnection.Antecedent
- CIM_ActiveConnection.Dependent
- CIM_ActiveConnection.TrafficType
- CIM_ActiveConnection.OtherTrafficDescription
- CIM_ActiveConnection.IsUnidirectional
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_ActiveConnection class

Defines a connection that is currently turned on and configured to provide communication between two **CIM\_ServiceAccessPoint** objects. **CIM\_ActiveConnection** is used when the connection is not treated as a **CIM\_ManagedElement** object. Service access points that are connected by an active connection are typically at the same networking or application layer.

## Syntax

``` syntax
[Association, Abstract, Version("2.10.0"), UMLPackagePath("CIM::Core::Service"), AMENDMENT]
class CIM_ActiveConnection : CIM_SAPSAPDependency
{
  CIM_ServiceAccessPoint REF Antecedent;
  CIM_ServiceAccessPoint REF Dependent;
  uint16                     TrafficType;
  string                     OtherTrafficDescription;
  boolean                    IsUnidirectional;
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

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

The service access point that is connected to the other service access point through the active connection. **CIM\_ServiceAccessPoint** object. In a unidirectional connection, this access point is the one that is transmitting data.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ServiceAccessPoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
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

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("No value"), [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_ActiveConnection**.**TrafficType**")
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

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("No value"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_ActiveConnection**.**OtherTrafficDescription**")
</dt> </dl>

> [!Note]  
> This property is deprecated. Instead, we recommend that you specify this information in the addressing, protocol, and basic functionality of the endpoints.

 

The type of traffic that is transmitted over this connection.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unicast"></span><span id="unicast"></span><span id="UNICAST"></span>

**Unicast** (2)


</dt> <dd></dd> <dt>

<span id="Broadcast"></span><span id="broadcast"></span><span id="BROADCAST"></span>

**Broadcast** (3)


</dt> <dd></dd> <dt>

<span id="Multicast"></span><span id="multicast"></span><span id="MULTICAST"></span>

**Multicast** (4)


</dt> <dd></dd> <dt>

<span id="Anycast"></span><span id="anycast"></span><span id="ANYCAST"></span>

**Anycast** (5)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_SAPSAPDependency**](cim-sapsapdependency.md)
</dt> </dl>

 

