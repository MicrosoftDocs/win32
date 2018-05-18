---
title: Msvm\_GlobalEthernetPortSAPImplementation class
description: An association that connects a LAN endpoint to a global Ethernet port (either an external or internal Ethernet port).
ms.assetid: '59f8ea5c-9ea6-4ffd-a09f-ac5702191c29'
keywords: ["Msvm_GlobalEthernetPortSAPImplementation class Hyper-V", "Msvm_GlobalEthernetPortSAPImplementation class Hyper-V , described"]
topic_type:
- apiref
api_name:
- Msvm_GlobalEthernetPortSAPImplementation
- Msvm_GlobalEthernetPortSAPImplementation.Dependent
- Msvm_GlobalEthernetPortSAPImplementation.Antecedent
api_location:
- Root\Virtualization
api_type:
- Schema
---

# Msvm\_GlobalEthernetPortSAPImplementation class

An association that connects a LAN endpoint to a global Ethernet port (either an external or internal Ethernet port).

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_GlobalEthernetPortSAPImplementation : CIM_DeviceSAPImplementation
{
  CIM_LANEndpoint  REF Dependent;
  CIM_EthernetPort REF Antecedent;
};
```

## Members

The **Msvm\_GlobalEthernetPortSAPImplementation** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_GlobalEthernetPortSAPImplementation** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_EthernetPort**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The Ethernet port.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LANEndpoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The LAN endpoint.

</dd> </dl>

## Remarks

Access to the **Msvm\_GlobalEthernetPortSAPImplementation** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_DeviceSAPImplementation**](cim-devicesapimplementation.md)
</dt> <dt>

[**CIM\_DeviceSAPImplementation**](https://msdn.microsoft.com/library/aa387245)
</dt> <dt>

[Networking Classes](networking-classes.md)
</dt> </dl>

 

 





