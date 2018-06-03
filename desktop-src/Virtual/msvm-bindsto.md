---
title: Msvm\_BindsTo class
description: An association that establishes a service access point (SAP) as a requester of protocol services from a protocol endpoint.
ms.assetid: 333d1f79-754a-45a6-8f81-216cd4387996
keywords:
- Msvm_BindsTo class Hyper-V
- Msvm_BindsTo class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_BindsTo
- Msvm_BindsTo.Antecedent
- Msvm_BindsTo.Dependent
api_location:
- Root\Virtualization
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Msvm\_BindsTo class

An association that establishes a service access point (SAP) as a requester of protocol services from a protocol endpoint. Typically, this association runs between SAPs and endpoints on a single system. Because a protocol endpoint is a kind of SAP, this binding can be used to establish a layering of two protocols, with the upper layer represented by the **Dependent** and the lower layer represented by the **Antecedent**.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_BindsTo : CIM_BindsTo
{
  Msvm_SwitchPort   REF Antecedent;
  Msvm_VLANEndpoint REF Dependent;
};
```

## Members

The **Msvm\_BindsTo** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_BindsTo** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_SwitchPort**](msvm-switchport.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The lower-level endpoint that is accessed by the SAP.

> [!Note]  
> On Windows Server 2008, this property inherited directly from [**CIM\_BindsTo**](cim-bindsto.md).

 

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_VLANEndpoint**](https://msdn.microsoft.com/library/aa388447)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The access point or protocol endpoint that is dependent on the lower-level endpoint.

> [!Note]  
> On Windows Server 2008, this property inherited directly from [**CIM\_BindsTo**](cim-bindsto.md).

 

</dd> </dl>

## Remarks

Access to the **Msvm\_BindsTo** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Examples

See [Querying Networking Objects](querying-networking-objects.md).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_BindsTo**](cim-bindsto.md)
</dt> <dt>

[**CIM\_BindsTo**](https://msdn.microsoft.com/library/cc150664)
</dt> <dt>

[Networking Classes](networking-classes.md)
</dt> </dl>

 

 





