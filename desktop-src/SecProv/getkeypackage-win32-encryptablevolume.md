---
description: Exports information that may help salvage encrypted data when the drive is severely damaged and no data backup files exist.
ms.assetid: 3d376a02-3392-433e-b842-24c73074610c
title: GetKeyPackage method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 09/05/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.GetKeyPackage
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# GetKeyPackage method of the Win32\_EncryptableVolume class

The **GetKeyPackage** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class exports information that may help salvage encrypted data when the drive is severely damaged and no data backup files exist.

The exported information consists of the volume's encryption key secured by a key protector of the type "Numerical Password" or "External Key". To make use of this package, you must also save the corresponding numerical password or external key.

> [!IMPORTANT]
> If you choose to export a key package, make certain to keep this information in a well-protected location. Do not carry this information with your computer. If this key package is lost or stolen, you will need to decrypt the volume and reencrypt it by using a new key.

In the event of a drive failure, the BitLocker Repair Tool exists to help salvage available data. For more information about how this tool can use the key package, see the [BitLocker FAQ](/windows/security/operating-system-security/data-protection/bitlocker/faq).

## Syntax

```mof
uint32 GetKeyPackage(
  [in]  string VolumeKeyProtectorID,
  [out] uint8  KeyPackage[]
);
```

## Parameters

*VolumeKeyProtectorID* `[in]`

Type: **string**

A unique string identifier used to manage an encrypted volume key protector. To export a key package, you must use a key protector of type "Numerical Password" or "External Key".

*KeyPackage\[\]* `[out]`

Type: **uint8**

A byte stream that contains the encryption key for a volume, secured by the specified key protector.

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.

| Return code/value | Description |
|-------------------|-------------|
| **S_OK** `0 (0x0)` | The method was successful. |
| **FVE_E_LOCKED_VOLUME** `2150694912 (0x80310000)` | The volume is locked. |
| **FVE_E_NOT_ACTIVATED** `2150694920 (0x80310008)` | BitLocker is not enabled on the volume. Add a key protector to enable BitLocker. |
| **FVE_E_PROTECTOR_NOT_FOUND** `2150694963 (0x80310033)` | The provided key protector does not exist on the volume. |
| **FVE_E_INVALID_PROTECTOR_TYPE** `2150694970 (0x8031003A)` | The *VolumeKeyProtectorID* parameter does not refer to a key protector of the type "Numerical Password" or "External Key". Use either the [ProtectKeyWithNumericalPassword](protectkeywithnumericalpassword-win32-encryptablevolume.md) or [ProtectKeyWithExternalKey](protectkeywithexternalkey-win32-encryptablevolume.md) method to create a key protector of the appropriate type. |

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Windows SDK. They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](../wmisdk/managed-object-format--mof-.md).

## Requirements

| Requirement | Value |
|-------------|-------|
| Minimum supported client | Windows Vista Enterprise, Windows Vista Ultimate \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\]                              |
| Namespace                | Root\\CIMV2\\Security\\MicrosoftVolumeEncryption                       |
| MOF                      | Win32\_encryptablevolume.mof                                           |

## See also

[Win32_EncryptableVolume](win32-encryptablevolume.md)

[BitLocker FAQ](/windows/security/operating-system-security/data-protection/bitlocker/faq)
