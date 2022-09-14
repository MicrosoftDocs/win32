---
description: Represents the available providers for replication.
ms.assetid: CAAD1CFC-6473-4642-8366-0A5625AE1F70
title: Msvm_ReplicationProvider class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ReplicationProvider
- Msvm_ReplicationProvider.InstanceID
- Msvm_ReplicationProvider.Caption
- Msvm_ReplicationProvider.Description
- Msvm_ReplicationProvider.ElementName
- Msvm_ReplicationProvider.Name
- Msvm_ReplicationProvider.OperationalStatus
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_ReplicationProvider class

Represents the available providers for replication.

The following syntax is simplified from MOF code and includes these inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ReplicationProvider : CIM_ManagedSystemElement
{
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
  string Name;
  uint16 OperationalStatus[];
};
```

## Members

The **Msvm\_ReplicationProvider** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ReplicationProvider** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (64)
</dt> </dl>

A short description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement). For this object, the value is:

"Replication Provider"

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement). For external providers, the value is provided by them. For host to host inbuilt provider, the value is:

"Virtual machine replication provider to Hyper-V host"

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A display name for the endpoint provider. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

For host to host inbuilt provider, this property is always set to:

"Virtual machine replication provider to Hyper-V host"

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **MaxLen** (256)
</dt> </dl>

The WMI instance ID, which identifies the provider. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement). The format of this property is "Microsoft:&lt;host-machine-name&gt;\\ReplicationProvider\\&lt;provider-Name&gt;."

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Name"), [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

The globally unique identifier (GUID) of the provider that identifies the endpoint provider. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement).

In the case of an external provider, this property is the CLSID of the provider COM class object. For host to host inbuilt provider, this property is fixed as:

"22391CDC-272C-4DDF-BA88-9BEFB1A0975C"

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current statuses of the object. This property is inherited from [**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement), and each array element is always set to:

<dl> <dt>

<span id="S_OK"></span><span id="s_ok"></span>**S\_OK** (2)
</dt> </dl>

</dd> </dl>

## Remarks

You can use any of available providers and the [**Msvm\_ReplicationRelationship**](msvm-replicationrelationship.md) class to enable a replication relationship. Hyper-V by default chooses the inbuilt host to host provider, which can be changed while creating the replication. Hyper-V management service communicates with an external provider by using COM.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md)
</dt> <dt>

[**CIM\_ManagedSystemElement**](/windows/desktop/CIMWin32Prov/cim-managedsystemelement)
</dt> </dl>

 

