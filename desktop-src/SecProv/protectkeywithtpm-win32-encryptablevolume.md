---
description: If the Trusted Platform Module (TPM) is available, this method secures the volume's encryption key.
ms.assetid: 79bee9ca-c86a-482b-a06f-1cfb887e7fae
title: ProtectKeyWithTPM method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.ProtectKeyWithTPM
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# ProtectKeyWithTPM method of the Win32\_EncryptableVolume class

The **ProtectKeyWithTPM** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class secures the volume's encryption key by using the Trusted Platform Module (TPM) Security Hardware on the computer, if available.

A key protector of type "TPM" is created for the volume, if one does not already exist.

This method is only applicable for the volume that contains the currently running operating system, and if a key protector does not already exist on the volume.

## Syntax


```mof
uint32 ProtectKeyWithTPM(
  [in, optional] string FriendlyName,
  [in, optional] uint8  PlatformValidationProfile[],
  [out]          string VolumeKeyProtectorID
);
```



## Parameters

<dl> <dt>

*FriendlyName* \[in, optional\]
</dt> <dd>

Type: **string**

A string that specifies a user-assigned string identifier for this key protector. If this parameter is not specified, a blank value is used.

</dd> <dt>

*PlatformValidationProfile* \[in, optional\]
</dt> <dd>

Type: **uint8\[\]**

An array of integers that specifies how the computer's Trusted Platform Module (TPM) Security Hardware secures the disk volume's encryption key.

A platform validation profile consists of a set of Platform Configuration Register (PCR) indices ranging from 0 to 23, inclusive. Repeat values in the parameter are ignored. Each PCR index is associated with services that run when the operating system starts. Each time the computer starts, the TPM will check that the services you specified in the platform validation profile have not changed. If any of these services change while BitLocker Drive Encryption (BDE) protection remains on, the TPM will not release the encryption key to unlock the disk volume and the computer will enter into recovery mode.

If this parameter is specified while the corresponding Group Policy setting has been enabled, it must match the Group Policy setting.

If this parameter is not specified, the default of 0, 2, 4, 5, 8, 9, 10, and 11 is used. The default platform validation profile secures the encryption key against changes to the Core Root of Trust of Measurement (CRTM), BIOS, and Platform Extensions (PCR 0), Option ROM Code (PCR 2), the Master Boot Record (MBR) Code (PCR 4), the Master Boot Record (MBR) Partition Table (PCR 5), the NTFS Boot Sector (PCR 8), the NTFS Boot Code (PCR 9), the Boot Manager (PCR 10), and the BitLocker Drive Encryption Access Control (PCR 11). For the security of your computer, we recommend the default profile. Unified Extensible Firmware Interface (UEFI)–based computers do not use PCR 5 by default. For additional protection against early startup configuration changes, use a profile of PCRs 0, 1, 2, 3, 4, 5, 8, 9, 10, 11.

Changing from the default profile affects the security and manageability of your computer. The sensitivity of BitLocker to platform modifications (malicious or authorized) is increased or decreased depending upon the inclusion or exclusion, respectively, of the PCRs. For BitLocker protection to be enabled, the platform validation profile must include PCR 11.



| Value                                                                         | Meaning                                                                             |
|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl>  | Core Root of Trust of Measurement (CRTM), BIOS, and Platform Extensions.<br/> |
| <dl> <dt>1</dt> </dl>  | Platform and Motherboard Configuration and Data<br/>                          |
| <dl> <dt>2</dt> </dl>  | Option ROM Code<br/>                                                          |
| <dl> <dt>3</dt> </dl>  | Option ROM Configuration and Data<br/>                                        |
| <dl> <dt>4</dt> </dl>  | Master Boot Record (MBR) Code<br/>                                            |
| <dl> <dt>5</dt> </dl>  | Master Boot Record (MBR) Partition Table<br/>                                 |
| <dl> <dt>6</dt> </dl>  | State Transition and Wake Events<br/>                                         |
| <dl> <dt>7</dt> </dl>  | Computer Manufacturer-Specific<br/>                                           |
| <dl> <dt>8</dt> </dl>  | NTFS Boot Sector<br/>                                                         |
| <dl> <dt>9</dt> </dl>  | NTFS Boot Code<br/>                                                           |
| <dl> <dt>10</dt> </dl> | Boot Manager<br/>                                                             |
| <dl> <dt>11</dt> </dl> | BitLocker Drive Encryption Access Control<br/>                                |
| <dl> <dt>12</dt> </dl> | Defined for use by the static operating system<br/>                           |
| <dl> <dt>13</dt> </dl> | Defined for use by the static operating system<br/>                           |
| <dl> <dt>14</dt> </dl> | Defined for use by the static operating system<br/>                           |
| <dl> <dt>15</dt> </dl> | Defined for use by the static operating system<br/>                           |
| <dl> <dt>16</dt> </dl> | Used for debugging<br/>                                                       |
| <dl> <dt>17</dt> </dl> | Dynamic CRTM<br/>                                                             |
| <dl> <dt>18</dt> </dl> | Platform defined<br/>                                                         |
| <dl> <dt>19</dt> </dl> | Used by trusted operating system<br/>                                         |
| <dl> <dt>20</dt> </dl> | Used by trusted operating system<br/>                                         |
| <dl> <dt>21</dt> </dl> | Used by trusted operating system<br/>                                         |
| <dl> <dt>22</dt> </dl> | Used by trusted operating system<br/>                                         |
| <dl> <dt>23</dt> </dl> | Application support<br/>                                                      |



 

</dd> <dt>

*VolumeKeyProtectorID* \[out\]
</dt> <dd>

Type: **string**

A string that uniquely identifies the created protector and which can be used to manage the key protector.

If the drive supports hardware encryption and BitLocker has not taken band ownership, the ID string is set to "BitLocker" and the key protector is written to per band metadata.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                         | Description                                                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                         | The method was successful.<br/>                                                                                                                                              |
| <dl> <dt>**FVE\_E\_LOCKED\_VOLUME**</dt> <dt>2150694912 (0x80310000)</dt> </dl>        | The volume is locked.<br/>                                                                                                                                                   |
| <dl> <dt>**TBS\_E\_SERVICE\_NOT\_RUNNING**</dt> <dt>2150121480 (0x80284008)</dt> </dl> | No compatible TPM is found on this computer.<br/>                                                                                                                            |
| <dl> <dt>**FVE\_E\_FOREIGN\_VOLUME**</dt> <dt>2150694947 (0x80310023)</dt> </dl>       | The TPM cannot secure the volume's encryption key because the volume does not contain the currently running operating system.<br/>                                           |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>2147942487 (0x80070057)</dt> </dl>                 | The *PlatformValidationProfile* parameter is provided but its values are not within the known range, or it does not match the Group Policy setting currently in effect.<br/> |
| <dl> <dt>**FVE\_E\_PROTECTOR\_EXISTS**</dt> <dt>2150694961 (0x80310031)</dt> </dl>            | A key protector of this type already exists.<br/>                                                                                                                             |



 

## Security Considerations

For the security of your computer, we recommend the default profile. For additional protection against early startup configuration changes, use a profile of PCRs 0, 1, 2, 3, 4, 5, 8, 9, 10, 11.

Changing from the default profile affects the security or usability of your computer.

## Remarks

At most one key protector of type "TPM" can exist for a volume at any time. If you want to change the display name or the platform validation profile used by an existing "TPM" key protector, you must first remove the existing key protector and then call **ProtectKeyWithTPM** to create a new one.

For PCR indices 0 through 5, the current measurements in the registers are used to protect the encryption key. For PCR values 8 through 11, the measurements used are the ones expected to exist on the next start cycle.

Additional key protectors should be specified to unlock the volume in recovery scenarios where access to the volume's encryption key cannot be obtained; for example, when the TPM cannot successfully validate against the platform validation profile. Use [**ProtectKeyWithExternalKey**](protectkeywithexternalkey-win32-encryptablevolume.md) or [**ProtectKeyWithNumericalPassword**](protectkeywithnumericalpassword-win32-encryptablevolume.md) to create one or more key protectors for recovering an otherwise locked volume.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Windows SDK. They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](../wmisdk/managed-object-format--mof-.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista Enterprise, Windows Vista Ultimate \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\CIMV2\\Security\\MicrosoftVolumeEncryption<br/>                                             |
| MOF<br/>                      | <dl> <dt>Win32\_encryptablevolume.mof</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_EncryptableVolume**](win32-encryptablevolume.md)
</dt> <dt>

[**Win32\_Tpm**](win32-tpm.md)
</dt> </dl>

 

 
