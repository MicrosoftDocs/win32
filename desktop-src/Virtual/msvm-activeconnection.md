---
title: Msvm\_ActiveConnection class
description: Connects a switch port to the LAN endpoint to which the port is connected.
ms.assetid: '061a97bc-dc12-4fa5-bdb7-9ebe8c403d84'
keywords: ["Msvm_ActiveConnection class Hyper-V", "Msvm_ActiveConnection class Hyper-V , described"]
topic_type:
- apiref
api_name:
- Msvm_ActiveConnection
- Msvm_ActiveConnection.TrafficType
- Msvm_ActiveConnection.OtherTrafficDescription
- Msvm_ActiveConnection.IsUnidirectional
- Msvm_ActiveConnection.Antecedent
- Msvm_ActiveConnection.Dependent
api_location:
- Root\Virtualization
api_type:
- Schema
---

# Msvm\_ActiveConnection class

Connects a switch port to the LAN endpoint to which the port is connected. The existence of this object means that the switch port and the LAN endpoint are actively connected and the Ethernet port associated with the LAN endpoint can communicate with the network through the switch port.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ActiveConnection : CIM_ActiveConnection
{
  uint16              TrafficType;
  string              OtherTrafficDescription;
  boolean             IsUnidirectional;
  Msvm_SwitchPort REF Antecedent;
  CIM_LANEndpoint REF Dependent;
};
```

## Members

The **Msvm\_ActiveConnection** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ActiveConnection** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_SwitchPort**](msvm-switchport.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

A service access point (SAP) that is configured to communicate or is actively communicating with the dependent SAP. In a unidirectional connection, this SAP is the one that is transmitting.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_LANEndpoint**](https://msdn.microsoft.com/library/cc136865)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The service access points that are hosted on a given system.

</dd> <dt>

**IsUnidirectional**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the connection is unidirectional; false if the connection is bidirectional. When the connection is unidirectional, the **Antecedent** property specifies the access point that is transmitting data. In a bidirectional connection, **Antecedent** can specify either access point assigned to the connection.

This property is inherited from [**CIM\_ActiveConnection**](cim-activeconnection.md).

</dd> <dt>

**OtherTrafficDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("No value"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ActiveConnection**](cim-activeconnection.md).**TrafficType**")
</dt> </dl>

> [!Note]  
> This property is deprecated. Instead, we recommend that you specify this information in the addressing, protocol, and basic functionality of the endpoints.

 

A description of the traffic type that is specified when the **TrafficType** property is set to "1" (Other).

This property is inherited from [**CIM\_ActiveConnection**](cim-activeconnection.md).

</dd> <dt>

**TrafficType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](https://msdn.microsoft.com/library/aa393651) ("No value"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ActiveConnection**](cim-activeconnection.md).**OtherTrafficDescription**")
</dt> </dl>

> [!Note]  
> This property is deprecated. Instead, we recommend that you specify this information in the addressing, protocol, and basic functionality of the endpoints.

 

The type of traffic that is transmitted over this connection.

This property is inherited from [**CIM\_ActiveConnection**](cim-activeconnection.md).

</dd> </dl>

## Remarks

Access to the **Msvm\_ActiveConnection** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Examples

See [Querying Networking Objects](querying-networking-objects.md).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ActiveConnection**](cim-activeconnection.md)
</dt> <dt>

[**CIM\_ActiveConnection**](https://msdn.microsoft.com/library/cc136779)
</dt> <dt>

[Networking Classes](networking-classes.md)
</dt> </dl>

 

 





