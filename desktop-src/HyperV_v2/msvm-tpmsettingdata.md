---
description: Represents the configured state of the TPM device.
ms.assetid: 948ccb47-3626-48f1-b18f-ef1d05978b21
title: Msvm_TPMSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_TPMSettingData
- Msvm_TPMSettingData.Shielded
- Msvm_TPMSettingData.DataProtected
- Msvm_TPMSettingData.EnabledState
- Msvm_TPMSettingData.KeyProtector
- Msvm_TPMSettingData.LastKnownGoodKeyProtector
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_TPMSettingData class

Represents the configured state of the TPM device.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_TPMSettingData : CIM_ResourceAllocationSettingData
{
  boolean Shielded = FALSE;
  boolean DataProtected = FALSE;
  uint16  EnabledState = 3;
  uint8   KeyProtector[];
  uint8   LastKnownGoodKeyProtector[];
};
```

## Members

The **Msvm\_TPMSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_TPMSettingData** class has these properties.

<dl> <dt>

**DataProtected**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

**true** to set a policy to protect a VM's data; otherwise, **false**. A newly created TPM is disabled, so the initial data protection state is **false**.

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

The enabled and disabled states of an element. The default value is **Disabled**.

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**KeyProtector**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](/windows/desktop/WmiSdk/standard-qualifiers), **OctetString**
</dt> </dl>

The key protector from Host Guardian Service client.

</dd> <dt>

**LastKnownGoodKeyProtector**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](/windows/desktop/WmiSdk/standard-qualifiers), **OctetString**
</dt> </dl>

The last known good key protector successfully encrypted TPM device state in the last VM boot.

This property is read-only for the WMI client, and can only be modified by the VM TPM device.

</dd> <dt>

**Shielded**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

**true** to define a policy that shields a virtual machine; otherwise, **false**. A newly created TPM is disabled, so the initial shielding state is **false**.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| End of client support<br/>    | Windows 10<br/>                                                                                   |
| End of server support<br/>    | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md)
</dt> </dl>

 

