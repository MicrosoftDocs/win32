---
description: Msvm_EthernetDeviceSAPImplementation class - Represents an association between a service access point and the logical device that implements it.
ms.assetid: C0DDB199-AD97-4DD7-8056-BD6BD0CECFA8
title: Msvm_EthernetDeviceSAPImplementation class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_EthernetDeviceSAPImplementation
- Msvm_EthernetDeviceSAPImplementation.Antecedent
- Msvm_EthernetDeviceSAPImplementation.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_EthernetDeviceSAPImplementation class

Represents an association between a service access point and the logical device that implements it. The cardinality of this association is many-to-many. A service access point (SAP) can be provided by more than one logical device, operating in conjunction. Any device can provide more than one SAP. When many logical devices are associated with a single SAP, it is assumed that these elements operate in conjunction to provide the access point. If different implementations of a SAP exist, each of these implementations would result in individual instantiations of the SAP object. These individual instantiations would then have associations to the unique implementations.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_EthernetDeviceSAPImplementation : CIM_DeviceSAPImplementation
{
  CIM_EthernetPort REF Antecedent;
  Msvm_LANEndpoint REF Dependent;
};
```

## Members

The **Msvm\_EthernetDeviceSAPImplementation** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_EthernetDeviceSAPImplementation** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_EthernetPort**](/previous-versions/windows/desktop/iscsitarg/cim-ethernetport)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

A reference to a class derived from [**CIM\_EthernetPort**](/previous-versions/windows/desktop/iscsitarg/cim-ethernetport) that represents the logical device.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_LANEndpoint**](msvm-lanendpoint.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

A reference to an instance of the [**Msvm\_LANEndpoint**](msvm-lanendpoint.md) class that represents the SAP that is using the **Antecedent**.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

