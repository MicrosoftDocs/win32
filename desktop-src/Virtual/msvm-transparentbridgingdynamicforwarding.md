---
title: Msvm\_TransparentBridgingDynamicForwarding class
description: Connects a transparent bridging service to a dynamic forward entry (learned MAC address).
ms.assetid: '29d10369-c51c-47b3-a900-b43845031f95'
keywords: ["Msvm_TransparentBridgingDynamicForwarding class Hyper-V", "Msvm_TransparentBridgingDynamicForwarding class Hyper-V , described"]
topic_type:
- apiref
api_name:
- Msvm_TransparentBridgingDynamicForwarding
- Msvm_TransparentBridgingDynamicForwarding.Antecedent
- Msvm_TransparentBridgingDynamicForwarding.Dependent
api_location:
- Root\Virtualization
api_type:
- Schema
---

# Msvm\_TransparentBridgingDynamicForwarding class

Connects a transparent bridging service to a dynamic forward entry (learned MAC address).

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_TransparentBridgingDynamicForwarding : CIM_TransparentBridgingDynamicForwarding
{
  Msvm_TransparentBridgingService REF Antecedent;
  Msvm_DynamicForwardingEntry     REF Dependent;
};
```

## Members

The **Msvm\_TransparentBridgingDynamicForwarding** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_TransparentBridgingDynamicForwarding** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_TransparentBridgingService**](msvm-transparentbridgingservice.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

A reference to the transparent bridging service.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_DynamicForwardingEntry**](msvm-dynamicforwardingentry.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A reference to the dynamic forwarding entry of forwarding database.

</dd> </dl>

## Remarks

Access to the **Msvm\_TransparentBridgingDynamicForwarding** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_TransparentBridgingDynamicForwarding**](cim-transparentbridgingdynamicforwarding.md)
</dt> <dt>

[**CIM\_TransparentBridgingDynamicForwarding**](https://msdn.microsoft.com/library/mt146307)
</dt> <dt>

[Networking Classes](networking-classes.md)
</dt> </dl>

 

 





