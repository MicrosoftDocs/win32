---
description: Represents the configured state of the security settings for.
ms.assetid: c57ab966-591e-4dd9-87be-0d2b81611d5d
title: Msvm_SecuritySettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_SecuritySettingData
- Msvm_SecuritySettingData.TpmEnabled
- Msvm_SecuritySettingData.KsdEnabled
- Msvm_SecuritySettingData.ShieldingRequested
- Msvm_SecuritySettingData.DataProtectionRequested
- Msvm_SecuritySettingData.EncryptStateAndVmMigrationTraffic
- Msvm_SecuritySettingData.VirtualizationBasedSecurityOptOut
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_SecuritySettingData class

Represents the configured state of the security settings for a virtual machine.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SecuritySettingData : CIM_SettingData
{
  boolean TpmEnabled;
  boolean KsdEnabled;
  boolean ShieldingRequested;
  boolean DataProtectionRequested;
  boolean EncryptStateAndVmMigrationTraffic;
  boolean VirtualizationBasedSecurityOptOut;
};
```

## Members

The **Msvm\_SecuritySettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_SecuritySettingData** class has these properties.

<dl> <dt>

**DataProtectionRequested**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

**true** to request data protection for a VM; otherwise, **false**. The default value is **false.**

</dd> <dt>

**EncryptStateAndVmMigrationTraffic**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

**true** to have the state and migration traffic of a VM encrypted; otherwise, **false**. The default value for a newly-created VM is **false**.

</dd> <dt>

**KsdEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

**true** to enable a key storage device (KSD) for this virtual machine; otherwise, **false**. A newly-created VM has a disable KSD.

</dd> <dt>

**ShieldingRequested**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

**true** to request shielding for a VM; otherwise, **false**. A newly-created VM has an initial shielding requested state of **false**.

</dd> <dt>

**TpmEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

**true** to enable a trusted platform nodule (TPM) for this virtual machine; otherwise, **false**. A newly-created VM has a disable TPM.

</dd> <dt>

**VirtualizationBasedSecurityOptOut**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

**true** to not offer a VM virtualization-based security; otherwise, **false**. The default setting for a newly-crated VM's opt-out state is **false**.

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

[**CIM\_SettingData**](cim-settingdata.md)
</dt> </dl>

 

