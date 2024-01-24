---
description: Begins encryption of a fully decrypted operating system volume after a hardware test.
ms.assetid: 216c96bb-7737-4421-8b16-1ce295342266
title: EncryptAfterHardwareTest method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.EncryptAfterHardwareTest
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# EncryptAfterHardwareTest method of the Win32\_EncryptableVolume class

The **EncryptAfterHardwareTest** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class begins encryption of a fully decrypted operating system volume after a hardware test. A reboot is required to perform this hardware test. Use this method instead of the [**Encrypt**](encrypt-win32-encryptablevolume.md) method to check that BitLocker will work as expected.

> [!Note]  
> If the hard drive is hardware encrypted, this method does not encrypt data. Instead, it sets the band status to unlocked from "perpetually unlocked". If the band is locked, unlocked or is read-only, the drive is considered to be encrypted.

 

## Syntax


```mof
uint32 EncryptAfterHardwareTest(
  [in, optional] uint32 EncryptionMethod,
  [in, optional] uint32 EncryptionFlags
);
```



## Parameters

<dl> <dt>

*EncryptionMethod* \[in, optional\]
</dt> <dd>

Type: **uint32**

Specifies the encryption algorithm and key size used to encrypt the volume. Leave this parameter blank to use the default value of zero. If the volume is partially or fully encrypted, the value of this parameter must be 0 or match the volume's existing encryption method. If the corresponding Group Policy setting has been enabled with a valid value, the value of this parameter must be 0 or match the Group Policy setting.

If the corresponding Group Policy setting is invalid, the default of AES 128 with diffuser is used.



| Value                                                                                                                                                                                                                                       | Meaning                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unspecified"></span><span id="unspecified"></span><span id="UNSPECIFIED"></span><dl> <dt>**Unspecified**</dt> <dt>0</dt> </dl> | Use the current Group Policy setting, if available and valid, or the default encryption method otherwise.<br/>                                                                              |
| <dl> <dt>1</dt> </dl>                                                                                                                                                                | AES 128 WITH DIFFUSER<br/> Encrypt the volume by using the Advanced Encryption Standard (AES) algorithm enhanced with a diffuser layer and by using an AES key size of 128 bits.<br/> |
| <dl> <dt>2</dt> </dl>                                                                                                                                                                | AES 256 WITH DIFFUSER<br/> Encrypt the volume by using the Advanced Encryption Standard (AES) algorithm enhanced with a diffuser layer and by using an AES key size of 256 bits.<br/> |
| <span id="AES_128"></span><span id="aes_128"></span><dl> <dt>**AES\_128**</dt> <dt>3</dt> </dl>                                          | Encrypt the volume by using the Advanced Encryption Standard (AES) algorithm and by using an AES key size of 128 bits.<br/>                                                                 |
| <span id="AES_256"></span><span id="aes_256"></span><dl> <dt>**AES\_256**</dt> <dt>4</dt> </dl>                                          | Encrypt the volume by using the Advanced Encryption Standard (AES) algorithm and by using an AES key size of 256 bits.<br/>                                                                 |



 

</dd> <dt>

*EncryptionFlags* \[in, optional\]
</dt> <dd>

Type: **uint32**

Flags that describe the encryption behavior.

**Windows 7, Windows Server 2008 R2, Windows Vista Enterprise and Windows Server 2008:** This parameter is not available.

A combination of 32 bits with the following bits currently defined.



| Value                                                                                  | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0x00000001</dt> </dl>  | Perform volume encryption in data-only encryption mode when starting new encryption process. If encryption has been paused or stopped, calling the [**Encrypt**](encrypt-win32-encryptablevolume.md) method effectively resumes conversion and the value of this bit is ignored. This bit only has effect when either the **Encrypt** or **EncryptAfterHardwareTest** methods start encryption from the fully decrypted state, decryption in progress state, or decryption paused state. If this bit is zero, meaning that it is not set, when starting new encryption process, then full mode conversion will be performed.<br/> |
| <dl> <dt>0x00000002</dt> </dl>  | Perform on-demand wipe of the volume free space. Calling the [**Encrypt**](encrypt-win32-encryptablevolume.md) method with this bit set is only allowed when volume is not currently converting or wiping and is in an "encrypted" state.<br/>                                                                                                                                                                                                                                                                                                                                                                                    |
| <dl> <dt>0x00010000 </dt> </dl> | Perform the requested operation synchronously. The call will block until requested operation has completed or was interrupted. This flag is only supported with the [**Encrypt**](encrypt-win32-encryptablevolume.md) method. This flag can be specified when **Encrypt** is called to resume stopped or interrupted encryption or wiping or when either encryption or wiping is in progress. This allows the caller to resume synchronously waiting until the process is completed or interrupted.<br/>                                                                                                                          |



 

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.

This method returns immediately. If the volume is already fully encrypted and no other errors are returned, this method returns zero.




| Return code/value | Description | 
|-------------------|-------------|
| <dl><dt><strong>S_OK</strong></dt><dt>0 (0x0)</dt></dl> | The method was successful.<br /> | 
| <dl><dt><strong>E_INVALIDARG</strong></dt><dt>2147942487 (0x80070057)</dt></dl> | The <em>EncryptionMethod</em> parameter is provided but is not within the known range or does not match the current Group Policy setting.<br /> | 
| <dl><dt><strong>FVE_E_CANNOT_ENCRYPT_NO_KEY</strong></dt><dt>2150694958 (0x8031002E)</dt></dl> | No encryption key exists for the volume.<br /> Either disable key protectors by using the <a href="disablekeyprotectors-win32-encryptablevolume.md"><strong>DisableKeyProtectors</strong></a> method, or use one of the following methods to specify key protectors for the volume:<ul><li><a href="protectkeywithexternalkey-win32-encryptablevolume.md"><strong>ProtectKeyWithExternalKey</strong></a></li><li><a href="protectkeywithnumericalpassword-win32-encryptablevolume.md"><strong>ProtectKeyWithNumericalPassword</strong></a></li><li><a href="protectkeywithtpm-win32-encryptablevolume.md"><strong>ProtectKeyWithTPM</strong></a></li><li><a href="protectkeywithtpmandpin-win32-encryptablevolume.md"><strong>ProtectKeyWithTPMAndPIN</strong></a></li><li><a href="protectkeywithtpmandpinandstartupkey-win32-encryptablevolume.md"><strong>ProtectKeyWithTPMAndPINAndStartupKey</strong></a></li><li><a href="protectkeywithtpmandstartupkey-win32-encryptablevolume.md"><strong>ProtectKeyWithTPMAndStartupKey</strong></a></li></ul><br /> | 
| <dl><dt><strong>FVE_E_CLUSTERING_NOT_SUPPORTED</strong></dt><dt>2150694942 (0x8031001E)</dt></dl> | The volume cannot be encrypted because this computer is configured to be part of a server cluster.<br /> | 
| <dl><dt><strong>FVE_E_NO_PROTECTORS_TO_TEST</strong></dt><dt>2150694971 (0x8031003B)</dt></dl> | No key protectors of the type "TPM", "TPM And PIN", "TPM And PIN And Startup Key", "TPM And Startup Key", or "External Key" can be found. The hardware test only involves the previous key protectors.<br /> If you still want to run a hardware test, you must use one of the following methods to specify key protectors for the volume:<ul><li><a href="protectkeywithexternalkey-win32-encryptablevolume.md"><strong>ProtectKeyWithExternalKey</strong></a></li><li><a href="protectkeywithnumericalpassword-win32-encryptablevolume.md"><strong>ProtectKeyWithNumericalPassword</strong></a></li><li><a href="protectkeywithtpm-win32-encryptablevolume.md"><strong>ProtectKeyWithTPM</strong></a></li><li><a href="protectkeywithtpmandpin-win32-encryptablevolume.md"><strong>ProtectKeyWithTPMAndPIN</strong></a></li><li><a href="protectkeywithtpmandpinandstartupkey-win32-encryptablevolume.md"><strong>ProtectKeyWithTPMAndPINAndStartupKey</strong></a></li><li><a href="protectkeywithtpmandstartupkey-win32-encryptablevolume.md"><strong>ProtectKeyWithTPMAndStartupKey</strong></a></li></ul><br /> | 
| <dl><dt><strong>FVE_E_NOT_DECRYPTED</strong></dt><dt>2150694969 (0x80310039)</dt></dl> | The volume is partially or fully encrypted.<br /> The hardware test applies before encryption occurs. If you still want to run the test, first use the <a href="decrypt-win32-encryptablevolume.md"><strong>Decrypt</strong></a> method and then use one of the following methods to add key protectors:<ul><li><a href="protectkeywithexternalkey-win32-encryptablevolume.md"><strong>ProtectKeyWithExternalKey</strong></a></li><li><a href="protectkeywithnumericalpassword-win32-encryptablevolume.md"><strong>ProtectKeyWithNumericalPassword</strong></a></li><li><a href="protectkeywithtpm-win32-encryptablevolume.md"><strong>ProtectKeyWithTPM</strong></a></li><li><a href="protectkeywithtpmandpin-win32-encryptablevolume.md"><strong>ProtectKeyWithTPMAndPIN</strong></a></li><li><a href="protectkeywithtpmandstartupkey-win32-encryptablevolume.md"><strong>ProtectKeyWithTPMAndStartupKey</strong></a></li></ul><br /> | 
| <dl><dt><strong>FVE_E_NOT_OS_VOLUME</strong></dt><dt>2150694952 (0x80310028)</dt></dl> | The volume is a data volume.<br /> The hardware test applies only to volumes that can start the operating system. Run this method on the currently started operating system volume.<br /> | 
| <dl><dt><strong>FVE_E_POLICY_PASSWORD_REQUIRED</strong></dt><dt>2150694956 (0x8031002C)</dt></dl> | No key protectors of the type "Numerical Password" are specified. The Group Policy requires a backup of recovery information to Active Directory Domain Services. To add at least one key protector of that type, use the <a href="protectkeywithnumericalpassword-win32-encryptablevolume.md"><strong>ProtectKeyWithNumericalPassword</strong></a> method.<br /> | 




 

## Remarks

When you use this method without the second optional parameter (according to the Windows 7 and Windows Vista Enterprise definition), the method will always initiate full mode conversion in order to keep backward compatible behavior. This way the security expectation of existing applications and scripts will not be broken with the addition of the second optional parameter in Windows 8 and Windows Server 2012.

Unlike the [**Encrypt**](encrypt-win32-encryptablevolume.md) method, this method does the following:

-   Tests whether the TPM will be able to unlock the volume, if a TPM-related key protector exists.
-   Tests whether the computer can read a USB flash drive that contains an external key file during start, if the volume will be unlocked by an external key (including a startup key).
-   Requires a computer restart to run the hardware test.
-   Begins encryption only if the hardware test succeeds.
-   Cannot be used on a data volume, on a partially or fully encrypted volume, or to resume encryption.

Before running this method, use the following methods to create the related key protectors:

-   [**ProtectKeyWithExternalKey**](protectkeywithexternalkey-win32-encryptablevolume.md)
-   [**ProtectKeyWithTPM**](protectkeywithtpm-win32-encryptablevolume.md)
-   [**ProtectKeyWithTPMAndPIN**](protectkeywithtpmandpin-win32-encryptablevolume.md)
-   [**ProtectKeyWithTPMAndPINAndStartupKey**](protectkeywithtpmandpinandstartupkey-win32-encryptablevolume.md)
-   [**ProtectKeyWithTPMAndStartupKey**](protectkeywithtpmandstartupkey-win32-encryptablevolume.md)

After running this method, take these additional steps:

1.  Insert into the computer a USB flash drive that contains an external key file. This step applies only if the volume has a key protector of type "External Key" or "TPM And Startup Key".
2.  Restart the computer.

On computer restart, the hardware test runs automatically.

Encryption begins if the hardware test succeeds. Otherwise, attempt to resolve any hardware failures. Run [**GetHardwareTestStatus**](gethardwareteststatus-win32-encryptablevolume.md) after restarting the computer to get test results.

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

 

 
