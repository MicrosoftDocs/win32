---
description: Retrieves the platform validation profile for a given key protector of the appropriate type.
ms.assetid: 45fa6ba7-169c-4753-8586-0029a7650acc
title: GetKeyProtectorPlatformValidationProfile method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.GetKeyProtectorPlatformValidationProfile
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# GetKeyProtectorPlatformValidationProfile method of the Win32\_EncryptableVolume class

The **GetKeyProtectorPlatformValidationProfile** method retrieves the platform validation profile for a given key protector of the appropriate type.

The key protector identifier must refer to a key protector of type "TPM", "TPM And PIN", "TPM And PIN And Startup Key", or "TPM And Startup Key".

## Syntax


```mof
uint32 GetKeyProtectorPlatformValidationProfile(
  [in]  string VolumeKeyProtectorID,
  [out] uint8  PlatformValidationProfile[]
);
```



## Parameters

<dl> <dt>

*VolumeKeyProtectorID* \[in\]
</dt> <dd>

Type: **string**

A unique string identifier used to manage an encrypted volume key protector.

</dd> <dt>

*PlatformValidationProfile* \[out\]
</dt> <dd>

Type: **uint8\[\]**

An array of integers that specifies how the Trusted Platform Module (TPM) Security Hardware of the computer secures the encryption key of the disk volume.



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



 

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                  | Description                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                  | The method was successful.<br/>                                                                                                                                        |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>2147942487 (0x80070057)</dt> </dl>          | The *VolumeKeyProtectorID* parameter does not refer to a key protector of the type "TPM", "TPM And PIN", "TPM And PIN And Startup Key", or "TPM And Startup Key".<br/> |
| <dl> <dt>**FVE\_E\_NOT\_ACTIVATED**</dt> <dt>2150694920 (0x80310008)</dt> </dl> | BitLocker is not enabled on the volume. Add a key protector to enable BitLocker.<br/>                                                                                  |



 

## Remarks

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
</dt> </dl>

 

 
