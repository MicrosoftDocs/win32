---
description: Begins encryption of a fully decrypted volume, or resumes encryption of a partially encrypted volume.
ms.assetid: bba8b800-309b-4268-8278-db69827bbdf6
title: Encrypt method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.Encrypt
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# Encrypt method of the Win32\_EncryptableVolume class

The **Encrypt** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class begins encryption of a fully decrypted volume, or resumes encryption of a partially encrypted volume. When encryption is paused or in-progress, this method behaves the same as [**ResumeConversion**](resumeconversion-win32-encryptablevolume.md). When decryption is paused or in-progress, this method stops the decryption and begins encryption.

> [!Note]  
> If the drive is hardware encrypted, this method does not encrypt data. Instead, it sets the band status to "unlocked" from "always unlocked". If the band is locked, unlocked or is read-only, the drive is considered to be encrypted.

 

**Windows Vista:** Encryption of a volume other than the currently running operating system volume is not supported.

## Syntax


```mof
uint32 Encrypt(
  [in, optional] uint32 EncryptionMethod,
  [in, optional] uint32 EncryptionFlags
);
```



## Parameters

<dl> <dt>

*EncryptionMethod* \[in, optional\]
</dt> <dd>

Type: **uint32**

An unsigned integer that specifies the encryption algorithm and key size used to encrypt the volume. If this parameter is greater than zero and the volume is partially or fully encrypted, *EncryptionMethod* must match the volume's existing encryption method. If this parameter is greater than zero and the corresponding Group Policy setting is enabled with a valid value, *EncryptionMethod* must match the Group Policy setting.

For a list of possible EncryptionMethod values, see the [**GetEncryptionMethod**](getencryptionmethod-win32-encryptablevolume.md) method.

Default value for Windows 7 or below is: 1 (AES\_128\_WITH\_DIFFUSER).

Default value for Windows 8, Windows 8.1 or Windows 10, version 1507 is: 3 (AES\_128).

Default value for Windows 10, version 1511 or above is: 6 (XTS\_AES\_128).

</dd> <dt>

*EncryptionFlags* \[in, optional\]
</dt> <dd>

Type: **uint32**

Flags that describe the encryption behavior.

**Windows 7, Windows Server 2008 R2, Windows Vista Enterprise and Windows Server 2008:** This parameter is not available.

A combination of 32 bits with following bits currently defined.



| Value                                                                                  | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0x00000001</dt> </dl>  | Perform volume encryption in data-only encryption mode when starting new encryption process. If encryption has been paused or stopped, calling the **Encrypt** method effectively resumes conversion and the value of this bit is ignored. This bit only has effect when either the **Encrypt** or [**EncryptAfterHardwareTest**](encryptafterhardwaretest-win32-encryptablevolume.md) methods start encryption from the fully decrypted state, decryption in progress state, or decryption paused state. If this bit is zero, meaning that it is not set, when starting new encryption process, then full mode conversion will be performed.<br/> |
| <dl> <dt>0x00000002</dt> </dl>  | Perform on-demand wipe of the volume free space. Calling the **Encrypt** method with this bit set is only allowed when volume is not currently converting or wiping and is in an "encrypted" state.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <dl> <dt>0x00010000 </dt> </dl> | Perform the requested operation synchronously. The call will block until requested operation has completed or was interrupted. This flag is only supported with the **Encrypt** method. This flag can be specified when **Encrypt** is called to resume stopped or interrupted encryption or wiping or when either encryption or wiping is in progress. This allows the caller to resume synchronously waiting until the process is completed or interrupted.<br/>                                                                                                                                                                                  |



 

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.

This method returns immediately. If the volume is already fully encrypted and no other errors are returned, this method returns 0.




| Return code/value | Description | 
|-------------------|-------------|
| <dl><dt><strong>S_OK</strong></dt><dt>0 (0x0)</dt></dl> | The method was successful.<br /> | 
| <dl><dt><strong>E_INVALIDARG</strong></dt><dt>2147942487 (0x80070057)</dt></dl> | The <em>EncryptionMethod</em> parameter is provided but is not within the known range or does not match the current Group Policy setting.<br /> | 
| <dl><dt><strong>FVE_E_CANNOT_ENCRYPT_NO_KEY</strong></dt><dt>2150694958 (0x8031002E)</dt></dl> | No encryption key exists for the volume. Either disable key protectors by using the <a href="disablekeyprotectors-win32-encryptablevolume.md"><strong>DisableKeyProtectors</strong></a> method or use one of the following methods to specify key protectors for the volume:<br /><ul><li><a href="protectkeywithexternalkey-win32-encryptablevolume.md"><strong>ProtectKeyWithExternalKey</strong></a></li><li><a href="protectkeywithnumericalpassword-win32-encryptablevolume.md"><strong>ProtectKeyWithNumericalPassword</strong></a></li><li><a href="protectkeywithtpm-win32-encryptablevolume.md"><strong>ProtectKeyWithTPM</strong></a></li><li><a href="protectkeywithtpmandpin-win32-encryptablevolume.md"><strong>ProtectKeyWithTPMAndPIN</strong></a></li><li><a href="protectkeywithtpmandpinandstartupkey-win32-encryptablevolume.md"><strong>ProtectKeyWithTPMAndPINAndStartupKey</strong></a></li><li><a href="protectkeywithtpmandstartupkey-win32-encryptablevolume.md"><strong>ProtectKeyWithTPMAndStartupKey</strong></a></li></ul><strong>Windows Vista:</strong> When no encryption key exists for the volume, ERROR_INVALID_OPERATION is returned instead. The decimal value is 4317 and the hexadecimal value is 0x10DD.<br /> | 
| <dl><dt><strong>FVE_E_CANNOT_SET_FVEK_ENCRYPTED</strong></dt><dt>2150694957 (0x8031002D)</dt></dl> | The provided encryption method does not match that of the partially or fully encrypted volume. To continue encryption, leave the <em>EncryptionMethod</em> parameter blank or use a value of zero.<br /> | 
| <dl><dt><strong>FVE_E_CLUSTERING_NOT_SUPPORTED</strong></dt><dt>2150694942 (0x8031001E)</dt></dl> | The volume cannot be encrypted because this computer is configured to be part of a server cluster.<br /> | 
| <dl><dt><strong>FVE_E_LOCKED_VOLUME</strong></dt><dt>2150694912 (0x80310000)</dt></dl> | The volume is locked.<br /> | 
| <dl><dt><strong>FVE_E_POLICY_PASSWORD_REQUIRED</strong></dt><dt>2150694956 (0x8031002C)</dt></dl> | No key protectors of the type "Numerical Password" are specified. The Group Policy requires a backup of recovery information to Active Directory Domain Services. To add at least one key protector of that type, use the <a href="protectkeywithnumericalpassword-win32-encryptablevolume.md"><strong>ProtectKeyWithNumericalPassword</strong></a> method.<br /> | 




 

## Remarks

When you use this method without the second optional parameter (according to the Windows 7 and Windows Vista Enterprise definition), the method will always initiate full mode conversion in order to keep backward compatible behavior. This way the security expectation of existing applications and scripts will not be broken with the addition of the second optional parameter in Windows 8 and Windows Server 2012.

You can call [**GetConversionStatus**](getconversionstatus-win32-encryptablevolume.md) to determine whether encryption is in progress and the percentage of the volume that has been encrypted.

After the volume is fully encrypted and if key protectors have been added and enabled, the protection status for the volume changes to "on".

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

 

 
