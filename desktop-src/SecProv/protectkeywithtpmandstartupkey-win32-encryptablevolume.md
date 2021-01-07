---
description: If the Trusted Platform Module (TPM) is available, this method secures the volume's encryption key enhanced by an external key.
ms.assetid: 58bc2de7-645f-4049-949c-975062f8c8ce
title: ProtectKeyWithTPMAndStartupKey method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.ProtectKeyWithTPMAndStartupKey
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# ProtectKeyWithTPMAndStartupKey method of the Win32\_EncryptableVolume class

The **ProtectKeyWithTPMAndStartupKey** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class secures the volume's encryption key by using the Trusted Platform Module (TPM) Security Hardware on the computer, if available, enhanced by an external key that must be presented to the computer at startup.

Both validation by the TPM and input of a USB memory device that contains the external key are necessary to access the volume's encryption key and unlock the volume contents. Use the [**SaveExternalKeyToFile**](saveexternalkeytofile-win32-encryptablevolume.md) method to save this external key to a file on a USB memory device for usage as a startup key.

This method is only applicable for the volume that contains the currently running operating system.

A key protector of type "TPM And Startup Key" is created for the volume, if one does not already exist.

## Syntax


```mof
uint32 ProtectKeyWithTPMAndStartupKey(
  [in, optional] string FriendlyName,
  [in, optional] uint8  PlatformValidationProfile[],
  [in, optional] uint8  ExternalKey[],
  [out]          string VolumeKeyProtectorID
);
```



## Parameters

<dl> <dt>

*FriendlyName* \[in, optional\]
</dt> <dd>

Type: **string**

A user-assigned string identifier for this key protector. If this parameter is not specified, a blank value is used.

</dd> <dt>

*PlatformValidationProfile* \[in, optional\]
</dt> <dd>

Type: **uint8\[\]**

An array of integers that specifies how the computer's Trusted Platform Module (TPM) Security Hardware secures the encryption key of the disk volume.

A platform validation profile consists of a set of Platform Configuration Register (PCR) indices ranging from 0 to 23, inclusive. Repeat values in the parameter are ignored. Each PCR index is associated with services that run when the operating system starts. Each time the computer starts, the TPM will check that the services you specified in the platform validation profile have not changed. If any of these services change while BitLocker Drive Encryption (BDE) protection remains on, the TPM will not release the encryption key to unlock the disk volume, and the computer will enter into recovery mode.

If this parameter is specified while the corresponding Group Policy setting has been enabled, it must match the Group Policy setting.

If this parameter is not specified, the default of 0, 2, 4, 5, 8, 9, 10, and 11 is used. The default platform validation profile secures the encryption key against changes to the following elements:

-   Core Root of Trust of Measurement (CRTM)
-   BIOS
-   Platform Extensions (PCR 0)
-   Option ROM Code (PCR 2)
-   Master Boot Record (MBR) Code (PCR 4)
-   Master Boot Record (MBR) Partition Table (PCR 5)
-   NTFS Boot Sector (PCR 8)
-   NTFS Boot Block (PCR 9)
-   Boot Manager (PCR 10)
-   BitLocker Access Control (PCR 11)

For the security of your computer, we recommend the default profile. For additional protection against early startup configuration changes, use a profile of PCRs 0, 1, 2, 3, 4, 5, 8, 9, 10, 11. Unified Extensible Firmware Interface (UEFI)–based computers do not use PCR 5 by default.

Changing from the default profile affects the security and manageability of your computer. The sensitivity of BitLocker to platform modifications (malicious or authorized) is increased or decreased depending upon the inclusion or exclusion, respectively, of the PCRs. For BitLocker protection to be enabled, the platform validation profile must include PCR 11.



| Value                                                                         | Meaning                                                                            |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl>  | Core Root of Trust of Measurement (CRTM), BIOS, and Platform Extensions<br/> |
| <dl> <dt>1</dt> </dl>  | Platform and Motherboard Configuration and Data<br/>                         |
| <dl> <dt>2</dt> </dl>  | Option ROM Code<br/>                                                         |
| <dl> <dt>3</dt> </dl>  | Option ROM Configuration and Data<br/>                                       |
| <dl> <dt>4</dt> </dl>  | Master Boot Record (MBR) Code<br/>                                           |
| <dl> <dt>5</dt> </dl>  | Master Boot Record (MBR) Partition Table<br/>                                |
| <dl> <dt>6</dt> </dl>  | State Transition and Wake Events<br/>                                        |
| <dl> <dt>7</dt> </dl>  | Computer Manufacturer-Specific<br/>                                          |
| <dl> <dt>8</dt> </dl>  | NTFS Boot Sector<br/>                                                        |
| <dl> <dt>9</dt> </dl>  | NTFS Boot Block<br/>                                                         |
| <dl> <dt>10</dt> </dl> | Boot Manager<br/>                                                            |
| <dl> <dt>11</dt> </dl> | BitLocker Access Control<br/>                                                |
| <dl> <dt>12</dt> </dl> | Defined for use by the static operating system<br/>                          |
| <dl> <dt>13</dt> </dl> | Defined for use by the static operating system<br/>                          |
| <dl> <dt>14</dt> </dl> | Defined for use by the static operating system<br/>                          |
| <dl> <dt>15</dt> </dl> | Defined for use by the static operating system<br/>                          |
| <dl> <dt>16</dt> </dl> | Used for debugging<br/>                                                      |
| <dl> <dt>17</dt> </dl> | Dynamic CRTM<br/>                                                            |
| <dl> <dt>18</dt> </dl> | Platform defined<br/>                                                        |
| <dl> <dt>19</dt> </dl> | Used by a trusted operating system<br/>                                      |
| <dl> <dt>20</dt> </dl> | Used by a trusted operating system<br/>                                      |
| <dl> <dt>21</dt> </dl> | Used by a trusted operating system<br/>                                      |
| <dl> <dt>22</dt> </dl> | Used by a trusted operating system<br/>                                      |
| <dl> <dt>23</dt> </dl> | Application support<br/>                                                     |



 

</dd> <dt>

*ExternalKey* \[in, optional\]
</dt> <dd>

Type: **uint8\[\]**

An array of bytes that specifies the 256-bit external key used to unlock the volume when the computer starts.

If no external key is specified, one is randomly generated. Use the [**GetKeyProtectorExternalKey**](getkeyprotectorexternalkey-win32-encryptablevolume.md) method to obtain the randomly generated key.

</dd> <dt>

*VolumeKeyProtectorID* \[out\]
</dt> <dd>

Type: **string**

A string that is the unique identifier associated with the created key protector that can be used to manage the key protector.

If the drive supports hardware encryption and BitLocker has not taken band ownership, the ID string is set to "BitLocker" and the key protector is written to per band metadata.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                         | Description                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                         | The method was successful.<br/>                                                                                                                                                                                                                                  |
| <dl> <dt>**FVE\_E\_LOCKED\_VOLUME**</dt> <dt>2150694912 (0x80310000)</dt> </dl>        | The volume is locked.<br/>                                                                                                                                                                                                                                       |
| <dl> <dt>**TBS\_E\_SERVICE\_NOT\_RUNNING**</dt> <dt>2150121480 (0x80284008)</dt> </dl> | No compatible TPM is found on this computer.<br/>                                                                                                                                                                                                                |
| <dl> <dt>**FVE\_E\_FOREIGN\_VOLUME**</dt> <dt>2150694947 (0x80310023)</dt> </dl>       | The TPM cannot secure the volume's encryption key because the volume does not contain the currently running operating system.<br/>                                                                                                                               |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>2147942487 (0x80070057)</dt> </dl>                 | The *PlatformValidationProfile* parameter is provided, but its values are not within the known range, or it does not match the Group Policy setting currently in effect.<br/> The *ExternalKey* parameter is provided but is not an array of size 32.<br/> |
| <dl> <dt>**FVE\_E\_BOOTABLE\_CDDVD**</dt> <dt>2150694960 (0x80310030)</dt> </dl>       | A bootable CD/DVD is found in this computer. Remove the CD/DVD and restart the computer.<br/>                                                                                                                                                                    |
| <dl> <dt>**FVE\_E\_PROTECTOR\_EXISTS**</dt> <dt>2150694961 (0x80310031)</dt> </dl>     | A key protector of this type already exists.<br/>                                                                                                                                                                                                                |



 

## Security Considerations

For the security of your computer, we recommend the default profile. For additional protection against early startup code changes, use a profile of PCRs 0, 2, 4, 5, 8, 9, 10, and 11. For additional protection against early startup configuration changes, use a profile of PCRs 0, 1, 2, 3, 4, 5, 8, 9, 10, 11.

Changing from the default profile affects the security or usability of your computer.

## Remarks

At most one key protector of type "TPM And Startup Key" can exist for a volume at any time. If you want to change the display name or the platform validation profile used by an existing "TPM plus Startup Key" key protector, you must first remove the existing key protector and then call **ProtectKeyWithTPMAndStartupKey** to create a new one. Additional key protectors should be specified to unlock the volume in recovery scenarios where access to the volume's encryption key cannot be obtained; for example, when the TPM cannot successfully validate against the platform validation profile or when USB memory that contains the external key is lost.

Use [**ProtectKeyWithExternalKey**](protectkeywithexternalkey-win32-encryptablevolume.md) or [**ProtectKeyWithNumericalPassword**](protectkeywithnumericalpassword-win32-encryptablevolume.md) to create one or more key protectors for recovering an otherwise locked volume.

While it is possible to have both a key protector of the type "TPM" and another of the type "TPM And Startup Key", the presence of the "TPM" key protector type negates the effects of other TPM-based key protectors.

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

 

 
