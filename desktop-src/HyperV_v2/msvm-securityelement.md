---
description: Represents the runtime security settings of a CIM\_ComputerSystem.
ms.assetid: fa4448dc-9353-475f-ac9b-5c50f36360d8
title: Msvm_SecurityElement class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_SecurityElement
- Msvm_SecurityElement.SystemCreationClassName
- Msvm_SecurityElement.SystemName
- Msvm_SecurityElement.CreationClassName
- Msvm_SecurityElement.Shielded
- Msvm_SecurityElement.EncryptStateAndVmMigrationTrafficEnabled
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_SecurityElement class

Represents the runtime security settings of a [**CIM\_ComputerSystem**](cim-computersystem.md).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SecurityElement : CIM_EnabledLogicalElement
{
  string  SystemCreationClassName;
  string  SystemName;
  string  CreationClassName;
  boolean Shielded;
  boolean EncryptStateAndVmMigrationTrafficEnabled;
};
```

## Members

The **Msvm\_SecurityElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_SecurityElement** class has these properties.

<dl> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

The name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, **CreationClassName** allows all instances of this class and its subclasses to be uniquely identified.

</dd> <dt>

**EncryptStateAndVmMigrationTrafficEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the VM is currently having its state and migration traffic encrypted.

</dd> <dt>

**Shielded**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the VM is currently shielded.

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256), [**Propagated**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_System**](cim-system.md).**CreationClassName**")
</dt> </dl>

The creation class name of the scoping system.

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256), [**Propagated**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_System**](cim-system.md).**Name**")
</dt> </dl>

The name of the scoping system.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1703 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md)
</dt> </dl>

 

