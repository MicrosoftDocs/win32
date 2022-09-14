---
title: MDM_BitLocker class
description: The MDM\_BitLocker class is used by the enterprise to manage encryption of PCs and devices.
ms.assetid: e8bea6dc-8d3d-46d2-b2e3-9a4c547a639f
keywords:
- MDM_BitLocker class
- MDM_BitLocker class, described
topic_type:
- apiref
api_name:
- MDM_BitLocker
- MDM_BitLocker.InstanceID
- MDM_BitLocker.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_BitLocker class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The MDM\_BitLocker class is used by the enterprise to manage encryption of PCs and devices.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv1")]
class MDM_BitLocker
{
  string InstanceID;
  string ParentID;
  sint32 RequireStorageCardEncryption;
  sint32 RequireDeviceEncryption;
  string EncryptionMethodByDriveType;
  string SystemDrivesRequireStartupAuthentication;
  string SystemDrivesMinimumPINLength;
  string SystemDrivesRecoveryMessage;
  string SystemDrivesRecoveryOptions;
  string FixedDrivesRecoveryOptions;
  string FixedDrivesRequireEncryption;
  string RemovableDrivesRequireEncryption;
  sint32 AllowWarningForOtherDiskEncryption;
};
```

## Members

The **MDM\_BitLocker** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_BitLocker** class has these properties.

<dl> <dt>

[AllowWarningForOtherDiskEncryption](/windows/client-management/mdm/bitlocker-csp#allowwarningforotherdiskencryption)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[EncryptionMethodByDriveType](/windows/client-management/mdm/bitlocker-csp#encryptionmethodbydrivetype)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[FixedDrivesRecoveryOptions](/windows/client-management/mdm/bitlocker-csp#fixeddrivesrecoveryoptions)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[FixedDrivesRequireEncryption](/windows/client-management/mdm/bitlocker-csp#fixeddrivesrequireencryption)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

</dd> <dt>

[RemovableDrivesRequireEncryption](/windows/client-management/mdm/bitlocker-csp#removabledrivesrequireencryption)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[RequireDeviceEncryption](/windows/client-management/mdm/bitlocker-csp#requiredeviceencryption)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[RequireStorageCardEncryption](/windows/client-management/mdm/bitlocker-csp#requirestoragecardencryption)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[SystemDrivesMinimumPINLength](/windows/client-management/mdm/bitlocker-csp#systemdrivesminimumpinlength)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[SystemDrivesRecoveryMessage](/windows/client-management/mdm/bitlocker-csp#systemdrivesrecoverymessage)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[SystemDrivesRecoveryOptions](/windows/client-management/mdm/bitlocker-csp#systemdrivesrecoveryoptions)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

[SystemDrivesRequireStartupAuthentication](/windows/client-management/mdm/bitlocker-csp#systemdrivesrequirestartupauthentication)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | None supported<br/>                                                                       |
| Namespace<br/>                | Root\\cimv2\\mdm\\dmmap<br/>                                                              |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv1.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl>  |



 

