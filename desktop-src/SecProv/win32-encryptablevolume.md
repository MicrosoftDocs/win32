---
description: For drive encryption or to create encryption security software, you can use the Windows encryption software, BitLocker Drive Encryption, an encryption API you can use by using the Win32\_EncryptableVolume WMI provider class.
ms.assetid: '464fa664-4330-43fa-a5e0-144d1e73cf58'
title: Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume
- Win32_EncryptableVolume.ConversionStatus
- Win32_EncryptableVolume.DeviceID
- Win32_EncryptableVolume.DriveLetter
- Win32_EncryptableVolume.EncryptionMethod
- Win32_EncryptableVolume.IsVolumeInitializedForProtection
- Win32_EncryptableVolume.PersistentVolumeID
- Win32_EncryptableVolume.ProtectionStatus
- Win32_EncryptableVolume.VolumeType
api_type: 
- Schema
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# Win32\_EncryptableVolume class

The **Win32\_EncryptableVolume** WMI provider class represents an area of storage on a hard disk that can be protected by using BitLocker Drive Encryption. Only NTFS volumes can be encrypted. It can be a volume that contains an operating system, or it can be a data volume on the local disk. It cannot be a network drive.

To realize the benefits of BitLocker, you must specify a protection method for the volume's encryption key and then fully encrypt the volume.

To protect the volume's encryption key, add key protectors by using these methods:

-   [**ProtectKeyWithCertificateFile**](protectkeywithcertificatefile-win32-encryptablevolume.md)
-   [**ProtectKeyWithCertificateThumbprint**](protectkeywithcertificatethumbprint-win32-encryptablevolume.md)
-   [**ProtectKeyWithExternalKey**](protectkeywithexternalkey-win32-encryptablevolume.md)
-   [**ProtectKeyWithNumericalPassword**](protectkeywithnumericalpassword-win32-encryptablevolume.md)
-   [**ProtectKeyWithPassphrase**](protectkeywithpassphrase-win32-encryptablevolume.md)
-   [**ProtectKeyWithTPM**](protectkeywithtpm-win32-encryptablevolume.md)
-   [**ProtectKeyWithTPMAndPIN**](protectkeywithtpmandpin-win32-encryptablevolume.md)
-   [**ProtectKeyWithTPMAndPINAndStartupKey**](protectkeywithtpmandpinandstartupkey-win32-encryptablevolume.md)
-   [**ProtectKeyWithTPMAndStartupKey**](protectkeywithtpmandstartupkey-win32-encryptablevolume.md)

Each type of key protector provides a different authentication experience for unlocking access to the encrypted data. External keys and numerical passwords can provide authentication during recovery scenarios. For TPM-based key protectors, you may first need to properly initialize the TPM. For more information, see the [**Win32\_Tpm**](win32-tpm.md) WMI provider class.

Use the [**Encrypt**](encrypt-win32-encryptablevolume.md) or [**EncryptAfterHardwareTest**](encryptafterhardwaretest-win32-encryptablevolume.md) method to begin encryption. Key protectors must be added prior to starting the encryption, or else you must use the [**DisableKeyProtectors**](disablekeyprotectors-win32-encryptablevolume.md) method to expose an unprotected clear key. If the computer turns off while encryption is in progress, encryption will automatically resume when the computer restarts.

You can use the [**GetConversionStatus**](getconversionstatus-win32-encryptablevolume.md) and [**GetProtectionStatus**](getprotectionstatus-win32-encryptablevolume.md) methods to check on the status of an accessible volume.

## Syntax

``` syntax
class Win32_EncryptableVolume
{
  string DeviceID;
  string PersistentVolumeID;
  string DriveLetter;
  uint32 ProtectionStatus;
};
```

## Members

The **Win32\_EncryptableVolume** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_EncryptableVolume** class has these methods.



| Method                                                                                                                   | Description                                                                                                                                                                                                                                                                           |
|:-------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BackupRecoveryInformationToActiveDirectory**](backuprecoveryinformationtoactivedirectory-win32-encryptablevolume.md) | Saves all external keys and related information that is needed for recovery to the Active Directory.<br/>                                                                                                                                                                       |
| [**ChangeExternalKey**](changeexternalkey-win32-encryptablevolume.md)                                                   | Changes the external key associated with an encrypted volume.<br/>                                                                                                                                                                                                              |
| [**ChangePassphrase**](changepassphrase-win32-encryptablevolume.md)                                                     | Uses the new passphrase to obtain a new derived key.<br/>                                                                                                                                                                                                                       |
| [**ChangePIN**](changepin-win32-encryptablevolume.md)                                                                   | Changes a PIN associated with an encrypted volume.<br/>                                                                                                                                                                                                                         |
| [**ClearAllAutoUnlockKeys**](clearallautounlockkeys-win32-encryptablevolume.md)                                         | Removes all external keys and related information saved onto the currently running operating system volume that are used to automatically unlock data volumes.<br/>                                                                                                             |
| [**Decrypt**](decrypt-win32-encryptablevolume.md)                                                                       | Begins decryption of a fully encrypted volume or resumes decryption of a partially encrypted volume.<br/>                                                                                                                                                                       |
| [**DeleteKeyProtector**](deletekeyprotector-win32-encryptablevolume.md)                                                 | Deletes a given key protector for the volume.<br/>                                                                                                                                                                                                                              |
| [**DeleteKeyProtectors**](deletekeyprotectors-win32-encryptablevolume.md)                                               | Deletes all key protectors for the volume.<br/>                                                                                                                                                                                                                                 |
| [**DisableAutoUnlock**](disableautounlock-win32-encryptablevolume.md)                                                   | Removes the external key saved on the currently running operating system volume so that the volume is not automatically unlocked when it is mounted.<br/>                                                                                                                       |
| [**DisableKeyProtectors**](disablekeyprotectors-win32-encryptablevolume.md)                                             | Disables all key protectors associated with this volume.<br/>                                                                                                                                                                                                                   |
| [**EnableAutoUnlock**](enableautounlock-win32-encryptablevolume.md)                                                     | Allows a data volume to be automatically unlocked when the volume is mounted.<br/>                                                                                                                                                                                              |
| [**EnableKeyProtectors**](enablekeyprotectors-win32-encryptablevolume.md)                                               | Enables all disabled key protectors.<br/>                                                                                                                                                                                                                                       |
| [**Encrypt**](encrypt-win32-encryptablevolume.md)                                                                       | Begins encryption of a fully decrypted volume or resumes encryption of a partially encrypted volume.<br/>                                                                                                                                                                       |
| [**EncryptAfterHardwareTest**](encryptafterhardwaretest-win32-encryptablevolume.md)                                     | Begins encryption of a fully decrypted volume after a hardware test.<br/>                                                                                                                                                                                                       |
| [**FindValidCertificates**](findvalidcertificates-win32-encryptablevolume.md)                                           | Enumerates all certificates on the system that match the indicated criteria and returns a list of thumbprints.<br/>                                                                                                                                                             |
| [**GetConversionStatus**](getconversionstatus-win32-encryptablevolume.md)                                               | Indicates the status of the encryption or decryption on the volume.<br/>                                                                                                                                                                                                        |
| [**GetEncryptionMethod**](getencryptionmethod-win32-encryptablevolume.md)                                               | Indicates the encryption algorithm and key size used on the volume.<br/>                                                                                                                                                                                                        |
| [**GetExternalKeyFileName**](getexternalkeyfilename-win32-encryptablevolume.md)                                         | Returns the name of the file that contains the external key.<br/>                                                                                                                                                                                                               |
| [**GetExternalKeyFromFile**](getexternalkeyfromfile-win32-encryptablevolume.md)                                         | Returns the external key from a file.<br/>                                                                                                                                                                                                                                      |
| [**GetHardwareTestStatus**](gethardwareteststatus-win32-encryptablevolume.md)                                           | Returns status information on a hardware test.<br/>                                                                                                                                                                                                                             |
| [**GetIdentificationField**](getidentificationfield-win32-encryptablevolume.md)                                         | Returns the identifier string that is available in the volume's metadata.<br/>                                                                                                                                                                                                  |
| [**GetKeyPackage**](getkeypackage-win32-encryptablevolume.md)                                                           | Returns information that make help salvage encrypted data when the drive is severely damaged.<br/>                                                                                                                                                                              |
| [**GetKeyProtectorCertificate**](getkeyprotectorcertificate-win32-encryptablevolume.md)                                 | Retrieves the public key and certificate thumbprint for a public key protector.<br/>                                                                                                                                                                                            |
| [**GetKeyProtectorExternalKey**](getkeyprotectorexternalkey-win32-encryptablevolume.md)                                 | Retrieves the external key for a given key protector of the appropriate type.<br/>                                                                                                                                                                                              |
| [**GetKeyProtectorFriendlyName**](getkeyprotectorfriendlyname-win32-encryptablevolume.md)                               | Retrieves the display name used to identify a given key protector.<br/>                                                                                                                                                                                                         |
| [**GetKeyProtectorNumericalPassword**](getkeyprotectornumericalpassword-win32-encryptablevolume.md)                     | Retrieves the numerical password for a given key protector of the appropriate type.<br/>                                                                                                                                                                                        |
| [**GetKeyProtectorPlatformValidationProfile**](getkeyprotectorplatformvalidationprofile-win32-encryptablevolume.md)     | Retrieves the platform validation profile for a given key protector of the appropriate type.<br/>                                                                                                                                                                               |
| [**GetKeyProtectors**](getkeyprotectors-win32-encryptablevolume.md)                                                     | Lists the protectors used to secure the volume's encryption key.<br/>                                                                                                                                                                                                           |
| [**GetKeyProtectorType**](getkeyprotectortype-win32-encryptablevolume.md)                                               | Indicates the type of a given key protector.<br/>                                                                                                                                                                                                                               |
| [**GetLockStatus**](getlockstatus-win32-encryptablevolume.md)                                                           | Indicates whether the contents of the volume are accessible from the currently running operating system.<br/>                                                                                                                                                                   |
| [**GetProtectionStatus**](getprotectionstatus-win32-encryptablevolume.md)                                               | Indicates whether the volume and its encryption key (if any) are secured.<br/>                                                                                                                                                                                                  |
| [**GetVersion**](getversion-win32-encryptablevolume.md)                                                                 | Indicates the FVE metadata version of the volume.<br/>                                                                                                                                                                                                                          |
| [**IsAutoUnlockEnabled**](isautounlockenabled-win32-encryptablevolume.md)                                               | Indicates whether the volume is automatically unlocked when mounted.<br/>                                                                                                                                                                                                       |
| [**IsAutoUnlockKeyStored**](isautounlockkeystored-win32-encryptablevolume.md)                                           | Indicates whether there exists in the currently running operating system volume any external keys and related information that may be used to automatically unlock data volumes.<br/>                                                                                           |
| [**IsKeyProtectorAvailable**](iskeyprotectoravailable-win32-encryptablevolume.md)                                       | Indicates whether protectors are available for the volume.<br/>                                                                                                                                                                                                                 |
| [**IsNumericalPasswordValid**](isnumericalpasswordvalid-win32-encryptablevolume.md)                                     | Indicates whether the numerical password meets the special format requirements.<br/>                                                                                                                                                                                            |
| [**Lock**](lock-win32-encryptablevolume.md)                                                                             | Dismounts the volume and removes the volume's encryption key from system memory.<br/>                                                                                                                                                                                           |
| [**PauseConversion**](pauseconversion-win32-encryptablevolume.md)                                                       | Pauses the encryption or decryption of a volume.<br/>                                                                                                                                                                                                                           |
| [**PrepareVolume**](preparevolume-win32-encryptablevolume.md)                                                           | Creates a BitLocker volume with the specified file system type of the discovery volume.<br/>                                                                                                                                                                                    |
| [**ProtectKeyWithCertificateFile**](protectkeywithcertificatefile-win32-encryptablevolume.md)                           | Validates the Enhanced Key Usage (EKU) object identifier (OID) of the provided certificate file.<br/>                                                                                                                                                                           |
| [**ProtectKeyWithCertificateThumbprint**](protectkeywithcertificatethumbprint-win32-encryptablevolume.md)               | Validates the Enhanced Key Usage (EKU) object identifier (OID) of the provided certificate thumbprint.<br/>                                                                                                                                                                     |
| [**ProtectKeyWithExternalKey**](protectkeywithexternalkey-win32-encryptablevolume.md)                                   | Secures the volume's encryption key with a 256-bit external key.<br/>                                                                                                                                                                                                           |
| [**ProtectKeyWithNumericalPassword**](protectkeywithnumericalpassword-win32-encryptablevolume.md)                       | Secures the volume's encryption key with a specially formatted 48-digit password.<br/>                                                                                                                                                                                          |
| [**ProtectKeyWithPassphrase**](protectkeywithpassphrase-win32-encryptablevolume.md)                                     | Uses the passphrase to obtain the derived key.<br/>                                                                                                                                                                                                                             |
| [**ProtectKeyWithTPM**](protectkeywithtpm-win32-encryptablevolume.md)                                                   | Secures the volume's encryption key by using the Trusted Platform Module (TPM) Security Hardware on the computer, if available.<br/>                                                                                                                                            |
| [**ProtectKeyWithTPMAndPIN**](protectkeywithtpmandpin-win32-encryptablevolume.md)                                       | Secures the volume's encryption key by using the Trusted Platform Module (TPM) Security Hardware on the computer, if available, enhanced by a user-specified personal identification number (PIN) that must be provided to the computer at startup.<br/>                        |
| [**ProtectKeyWithTPMAndPINAndStartupKey**](protectkeywithtpmandpinandstartupkey-win32-encryptablevolume.md)             | Secures the volume's encryption key by using the Trusted Platform Module (TPM) Security Hardware on the computer, if available, enhanced by a user-specified personal identification number (PIN) and by an external key that must be provided to the computer at startup.<br/> |
| [**ProtectKeyWithTPMAndStartupKey**](protectkeywithtpmandstartupkey-win32-encryptablevolume.md)                         | Secures the volume's encryption key by using the Trusted Platform Module (TPM) Security Hardware on the computer, if available, enhanced by an external key that must be provided to the computer at startup.<br/>                                                              |
| [**ResumeConversion**](resumeconversion-win32-encryptablevolume.md)                                                     | Resumes the encryption or decryption of a volume.<br/>                                                                                                                                                                                                                          |
| [**SaveExternalKeyToFile**](saveexternalkeytofile-win32-encryptablevolume.md)                                           | Writes the external key associated with the specified volume key protector to a specified file location.<br/>                                                                                                                                                                   |
| [**SetIdentificationField**](setidentificationfield-win32-encryptablevolume.md)                                         | Sets the specified identifier string in the volume's metadata.<br/>                                                                                                                                                                                                             |
| [**UnlockWithCertificateFile**](unlockwithcertificatefile-win32-encryptablevolume.md)                                   | Uses the provided certificate file to obtain the derived key and unlock the encrypted volume.<br/>                                                                                                                                                                              |
| [**UnlockWithCertificateThumbprint**](unlockwithcertificatethumbprint-win32-encryptablevolume.md)                       | Uses the provided certificate thumbprint to obtain the derived key and unlock the encrypted volume.<br/>                                                                                                                                                                        |
| [**UnlockWithExternalKey**](unlockwithexternalkey-win32-encryptablevolume.md)                                           | Uses a provided external key to access the contents of a data volume.<br/>                                                                                                                                                                                                      |
| [**UnlockWithNumericalPassword**](unlockwithnumericalpassword-win32-encryptablevolume.md)                               | Uses a provided numerical password to access the contents of a data volume.<br/>                                                                                                                                                                                                |
| [**UnlockWithPassphrase**](unlockwithpassphrase-win32-encryptablevolume.md)                                             | Uses the passphrase to obtain the derived key. After the derived key is calculated, the derived key is used to unlock the encrypted volume's master key.<br/>                                                                                                                   |
| [**UpgradeVolume**](upgradevolume-win32-encryptablevolume.md)                                                           | Upgrades a volume from the Windows Vista format to the Windows 7 format.<br/>                                                                                                                                                                                                   |



 

### Properties

The **Win32\_EncryptableVolume** class has these properties.

<dl> <dt>
  
**ConversionStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

An integer corresponding to the encryption state of the volume. This value is stored when class is instantiated. It is possible for the conversion status to change state between instantiation and when you check the value. To check the value of the **ConversionStatus** property in real time, use the [**GetConversionStatus**](getconversionstatus-win32-encryptablevolume.md) method.

| Value                                                                        | Meaning                                                                                                                                                                           |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | FULLY DECRYPTED<br/><br/> |
| <dl> <dt>1</dt> </dl> | FULLY ENCRYPTED<br/><br/> |
| <dl> <dt>2</dt> </dl> | ENCRYPTION IN PROGRESS<br/><br/> |
| <dl> <dt>3</dt> </dl> | DECRYPTION IN PROGRESS<br/><br/> |
| <dl> <dt>4</dt> </dl> | ENCRYPTION PAUSED<br/><br/> |
| <dl> <dt>5</dt> </dl> | DECRYPTION PAUSED<br/><br/> |

</dd> <dt>

**DeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>
  
Qualifiers: **Key**
</dt> </dl>

A unique identifier for the volume on this system. Use this to associate a volume with other WMI provider classes, for example, **Win32\_Volume**.

</dd> <dt>

**DriveLetter**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The drive letter of the volume. This identifier can be used to associate a volume with other WMI provider classes, for example [**Win32\_Volume**](/previous-versions/windows/desktop/legacy/aa394515(v=vs.85)).

For volumes without drive letters, this value is **NULL**.

</dd> <dt>
  
**EncryptionMethod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An integer identifying the algorithm used to encrypt the volume. 

| Value                                                                        | Meaning                                                                                                                                                                           |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | NOT ENCRYPTED<br/> The volume is not encrypted, nor has encryption begun. <br/> |
| <dl> <dt>1</dt> </dl> | AES 128 WITH DIFFUSER<br/><br/> |
| <dl> <dt>2</dt> </dl> | AES 256 WITH DIFFUSER<br/><br/> |
| <dl> <dt>3</dt> </dl> | AES 128<br/><br/> |
| <dl> <dt>4</dt> </dl> | AES 256<br/><br/> |
| <dl> <dt>5</dt> </dl> | HARDWARE ENCRYPTION<br/><br/> |
| <dl> <dt>6</dt> </dl> | XTS-AES 128<br/> This is the default setting for Windows 10. <br/> |
| <dl> <dt>7</dt> </dl> | XTS-AES 256 WITH DIFFUSER<br/><br/> |

</dd> <dt>
  
**IsVolumeInitializedForProtection**
</dt> <dd> <dl> <dt>

Data type: **bool**
</dt> <dt>

Access type: Read-only
</dt> </dl>

States whether the volume is in a state ready for encryption to start. At least one key protector must be added before this will be True and encryption can begin.

</dd> <dt>

**PersistentVolumeID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A persistent identifier for the volume on this system. This identifier is exclusive to **Win32\_EncryptableVolume**.

This identifier is an empty string if the volume is a standard fully decrypted NTFS volume; otherwise, it has a unique value.

</dd> <dt>

**ProtectionStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the volume, whether or not BitLocker is protecting the volume. This value is stored when the class is instantiated. It is possible for the protection status to change state between instantiation and when you check the value. To check the value of the **ProtectionStatus** property in real time, use the [**GetProtectionStatus**](getprotectionstatus-win32-encryptablevolume.md) method.



| Value                                                                        | Meaning                                                                                                                                                                           |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | PROTECTION OFF<br/> The volume is not encrypted, partially encrypted, or the volume's encryption key for the volume is available in the clear on the hard disk. <br/> |
| <dl> <dt>1</dt> </dl> | PROTECTION ON<br/> The volume is fully encrypted and the encryption key for the volume is not available in the clear on the hard disk. <br/>                          |
| <dl> <dt>2</dt> </dl> | PROTECTION UNKNOWN<br/> The volume protection status cannot be determined. One potential cause is that the volume is in a locked state.<br/>                          |

</dd> </dl>

**VolumeType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An integer identifying the type of volume relevant to encryption for use of appropriate key protectors and encryption methods.

| Value                                                                        | Meaning                                                                                                                                                                           |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | SYSTEM <br/> The volume contains the Windows operating system. Standard key protectors are usually TPM, sometimes in conjunction with a PIN, and Numerical (Recovery) Password <br/> |
| <dl> <dt>1</dt> </dl> | FIXED DISK<br/> This volume is a non-system storage device for the system. It is often recommended to configure auto-unlock in conjunction with the system volume. <br/> |
| <dl> <dt>2</dt> </dl> | REMOVABLE<br/> This volume is hot removable from the system. Typically this will indicate an external drive or flash drive. Different encryption methods may be considered due to compatibility concerns with other systems. <br/> |

</dd> <dt>

## Security Considerations

The **Win32\_EncryptableVolume** WMI provider class relies on the WMI namespace security and on the BitLocker Drive Encryption subsystem for access control.

To use the **Win32\_EncryptableVolume** methods, the following conditions must be met:

-   You must have administrator privileges.
-   Connection encryption must be able to connect to the provider.

    For more information about creating an encrypted connection, see [Requiring an Encrypted Connection to a Namespace](../wmisdk/requiring-an-encrypted-connection-to-a-namespace.md).

To enable remote connections, remote WMI traffic must be allowed. For more information about enabling WMI traffic, see [Connecting to WMI Remotely Starting with Vista](../wmisdk/connecting-to-wmi-remotely-starting-with-vista.md).

The default namespace security setting includes an entry to allow editing by default. For more information about WMI namespace auditing, see [Access to WMI Namespaces](../wmisdk/access-to-wmi-namespaces.md).

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Windows SDK. They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](../wmisdk/managed-object-format--mof-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista Enterprise, Windows Vista Ultimate \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\CIMV2\\Security\\MicrosoftVolumeEncryption<br/>                                             |
| MOF<br/>                      | <dl> <dt>Win32\_encryptablevolume.mof</dt> </dl> |



 

 
