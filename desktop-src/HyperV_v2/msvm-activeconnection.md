---
description: Connects a switch port to the LAN endpoint to which the port is connected.
ms.assetid: 963EC004-6A67-4F75-BD93-1BCD17F32490
title: Msvm_ActiveConnection class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ActiveConnection
- Msvm_ActiveConnection.Antecedent
- Msvm_ActiveConnection.Dependent
- Msvm_ActiveConnection.TrafficType
- Msvm_ActiveConnection.OtherTrafficDescription
- Msvm_ActiveConnection.IsUnidirectional
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_ActiveConnection class

Connects a switch port to the LAN endpoint to which the port is connected. The existence of this object means that the switch port and the LAN endpoint are actively connected and the Ethernet port associated with the LAN endpoint can communicate with the network through the switch port.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ActiveConnection : CIM_ActiveConnection
{
  Msvm_LANEndpoint REF Antecedent;
  CIM_LANEndpoint  REF Dependent;
  uint16               TrafficType;
  string               OtherTrafficDescription;
  boolean              IsUnidirectional;
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

Data type: **[**Msvm\_LANEndpoint**](msvm-lanendpoint.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

A reference to an instance of the [**Msvm\_LANEndpoint**](msvm-lanendpoint.md) class that represents the service access point (SAP) that is configured to communicate or is actively communicating with the dependent SAP. In an unidirectional connection, this SAP is the one that is transmitting.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_LANEndpoint**](cim-lanendpoint.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

A reference to an instance of the [**Msvm\_LANEndpoint**](cim-lanendpoint.md) class that represents the SAP that is configured to communicate or is actively communicating with the antecedent SAP. In an unidirectional connection, this SAP is the one that is receiving.

</dd> <dt>

**IsUnidirectional**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If this property is **True**, this connection is unidirectional; otherwise, this connection is bidirectional. When a connection is unidirectional, the "speaker" should be defined as the **Antecedent** reference. In a bidirectional connection, it does not matter whether the selected access point is the **Antecedent** or **Dependent**. This property is inherited from [**CIM\_ActiveConnection**](/previous-versions//cc136779(v=vs.85)).

</dd> <dt>

**OtherTrafficDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is inherited from [**CIM\_ActiveConnection**](/previous-versions//cc136779(v=vs.85)), but it is not used.

</dd> <dt>

**TrafficType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is inherited from [**CIM\_ActiveConnection**](/previous-versions//cc136779(v=vs.85)), but it is not used.

</dd> </dl>

## Remarks

Access to the **Msvm\_ActiveConnection** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Examples

See [Querying networking objects](querying-networking-objects.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_ActiveConnection**](cim-activeconnection.md)
</dt> <dt>

[**CIM\_ActiveConnection**](/previous-versions//cc136779(v=vs.85))
</dt> </dl>

 

