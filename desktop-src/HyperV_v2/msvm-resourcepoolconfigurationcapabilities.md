---
description: Describes the capabilities of the associated Msvm\_ResourcePoolConfigurationService class.
ms.assetid: 3e6857f9-62a0-420b-8f1d-8aad685a7ff7
title: Msvm_ResourcePoolConfigurationCapabilities class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ResourcePoolConfigurationCapabilities
- Msvm_ResourcePoolConfigurationCapabilities.InstanceID
- Msvm_ResourcePoolConfigurationCapabilities.Caption
- Msvm_ResourcePoolConfigurationCapabilities.Description
- Msvm_ResourcePoolConfigurationCapabilities.ElementName
- Msvm_ResourcePoolConfigurationCapabilities.AsynchronousMethodsSupported
- Msvm_ResourcePoolConfigurationCapabilities.SynchronousMethodsSupported
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_ResourcePoolConfigurationCapabilities class

Describes the capabilities of the associated [**Msvm\_ResourcePoolConfigurationService**](msvm-resourcepoolconfigurationservice.md) class. Clients can use instances of this class to determine which methods are supported synchronously or asynchronously. The same method must not be in both lists. Method implementations must either be synchronous or asynchronous.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider")]
class Msvm_ResourcePoolConfigurationCapabilities : CIM_Capabilities
{
  string InstanceID;
  string Caption = "Resource Pool Configuration Capabilities";
  string Description = "Microsoft Resource Pool Configuration Capabilities";
  string ElementName = "Resource Pool Configuration Capabilities";
  uint32 AsynchronousMethodsSupported[];
  uint32 SynchronousMethodsSupported[];
};
```

## Members

The **Msvm\_ResourcePoolConfigurationCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ResourcePoolConfigurationCapabilities** class has these properties.

<dl> <dt>

**AsynchronousMethodsSupported**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of method identifiers, each identifying a method of the [**Msvm\_ResourcePoolConfigurationService**](msvm-resourcepoolconfigurationservice.md) class that is supported asynchronously by the implementation.

<dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (..)


</dt> <dd></dd> <dt>

<span id="CreatePool_is_supported"></span><span id="createpool_is_supported"></span><span id="CREATEPOOL_IS_SUPPORTED"></span>

**CreatePool is supported** (32768)


</dt> <dd></dd> <dt>

<span id="ChangePoolResources_is_supported"></span><span id="changepoolresources_is_supported"></span><span id="CHANGEPOOLRESOURCES_IS_SUPPORTED"></span>

**ChangePoolResources is supported** (32769)


</dt> <dd></dd> <dt>

<span id="ChangePoolSettings_is_supported"></span><span id="changepoolsettings_is_supported"></span><span id="CHANGEPOOLSETTINGS_IS_SUPPORTED"></span>

**ChangePoolSettings is supported** (32770)


</dt> <dd></dd> <dt>

<span id="DeletePool_is_supported"></span><span id="deletepool_is_supported"></span><span id="DELETEPOOL_IS_SUPPORTED"></span>

**DeletePool is supported** (32771)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved** (32772..65535)


</dt> <dd></dd> </dl>

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A short description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement), and it is always set to "Resource Pool Configuration Capabilities".

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement), and it is always set to "Microsoft Resource Pool Configuration Capabilities".

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A display name for the object. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement), and it is always set to "Resource Pool Configuration Capabilities".

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Uniquely identifies an instance of this class. This property is inherited from [**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement).

</dd> <dt>

**SynchronousMethodsSupported**
</dt> <dd> <dl> <dt>

Data type: **uint32** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of method identifiers, each identifying a method of the [**Msvm\_ResourcePoolConfigurationService**](msvm-resourcepoolconfigurationservice.md) class that is supported synchronously by the implementation.

<dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (..)


</dt> <dd></dd> <dt>

<span id="CreatePool_is_supported"></span><span id="createpool_is_supported"></span><span id="CREATEPOOL_IS_SUPPORTED"></span>

**CreatePool is supported** (32768)


</dt> <dd></dd> <dt>

<span id="ChangePoolResources_is_supported"></span><span id="changepoolresources_is_supported"></span><span id="CHANGEPOOLRESOURCES_IS_SUPPORTED"></span>

**ChangePoolResources is supported** (32769)


</dt> <dd></dd> <dt>

<span id="ChangePoolSettings_is_supported"></span><span id="changepoolsettings_is_supported"></span><span id="CHANGEPOOLSETTINGS_IS_SUPPORTED"></span>

**ChangePoolSettings is supported** (32770)


</dt> <dd></dd> <dt>

<span id="DeletePool_is_supported"></span><span id="deletepool_is_supported"></span><span id="DELETEPOOL_IS_SUPPORTED"></span>

**DeletePool is supported** (32771)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved** (32772..65535)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

