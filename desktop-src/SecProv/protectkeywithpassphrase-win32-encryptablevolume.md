---
description: ProtectKeyWithPassphrase method of the Win32_EncryptableVolume class - Uses the passphrase to obtain the derived key.
ms.assetid: 62b070ec-4788-47cc-bfa4-6811a712ddbd
title: ProtectKeyWithPassphrase method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.ProtectKeyWithPassphrase
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# ProtectKeyWithPassphrase method of the Win32\_EncryptableVolume class

The **ProtectKeyWithPassphrase** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class uses the passphrase to obtain the derived key. After the derived key is calculated, the derived key is used to secure the encrypted volume's master key.

## Syntax


```mof
uint32 ProtectKeyWithPassphrase(
  [in, optional] string FriendlyName,
  [in]           string Passphrase,
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

*Passphrase* \[in\]
</dt> <dd>

Type: **string**

A string that specifies the passphrase.

</dd> <dt>

*VolumeKeyProtectorID* \[out\]
</dt> <dd>

Type: **string**

A string that uniquely identifies the created key protector.

If the drive supports hardware encryption and BitLocker has not taken band ownership, the ID string is set to "BitLocker" and the key protector is written to per band metadata.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                                        | Description                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                                        | The method was successful.<br/>                                                                                    |
| <dl> <dt>**FVE\_E\_NOT\_ALLOWED\_IN\_SAFE\_MODE**</dt> <dt>2150694976 (0x80310040)</dt> </dl>         | BitLocker Drive Encryption can only be used for recovery purposes when used in Safe Mode.<br/>                     |
| <dl> <dt>**FVE\_E\_POLICY\_PASSPHRASE\_NOT\_ALLOWED**</dt> <dt>2150695018 (0x8031006A)</dt> </dl>     | Group policy does not permit the creation of a passphrase.<br/>                                                    |
| <dl> <dt>**FVE\_E\_FIPS\_PREVENTS\_PASSPHRASE**</dt> <dt>2150695020 (0x8031006C)</dt> </dl>           | The group policy setting that requires FIPS compliance prevented the passphrase from being generated or used.<br/> |
| <dl> <dt>**FVE\_E\_POLICY\_INVALID\_PASSPHRASE\_LENGTH**</dt> <dt>2150695040 (0x80310080)</dt> </dl>  | The passphrase provided does not meet the minimum or maximum length requirements.<br/>                             |
| <dl> <dt>**FVE\_E\_POLICY\_PASSPHRASE\_TOO\_SIMPLE**</dt> <dt>2150695041 (0x80310081)</dt> </dl>      | The passphrase does not meet the complexity requirements set by the administrator in group policy.<br/>            |
| <dl> <dt>**FVE\_E\_LOCKED\_VOLUME**</dt> <dt>2150694912 (0x80310000)</dt> </dl>                       | The volume is already locked by BitLocker Drive Encryption. You must unlock the drive from Control Panel.<br/>     |
| <dl> <dt>**FVE\_E\_OVERLAPPED\_UPDATE**</dt> <dt>2150694948 (0x80310024)</dt> </dl>                   | The control block for the encrypted volume was updated by another thread.<br/>                                     |
| <dl> <dt>**FVE\_E\_KEY\_PROTECTOR\_NOT\_SUPPORTED**</dt> <dt>2150695017 (0x80310069)</dt> </dl>       | The key protector is not supported by the version of BitLocker Drive Encryption currently on the volume.<br/>      |
| <dl> <dt>**FVE\_E\_OS\_VOLUME\_PASSPHRASE\_NOT\_ALLOWED**</dt> <dt>2150695021 (0x8031006D)</dt> </dl> | The passphrase cannot be added to the operating system volume. <br/>                                               |
| <dl> <dt>**FVE\_E\_PROTECTOR\_EXISTS**</dt> <dt>2150694960 (0x80310030)</dt> </dl>                    | The provided key protector already exists on this volume.<br/>                                                     |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 Enterprise, Windows 7 Ultimate \[desktop apps only\]<br/>                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | Root\\CIMV2\\Security\\MicrosoftVolumeEncryption<br/>                                             |
| MOF<br/>                      | <dl> <dt>Win32\_encryptablevolume.mof</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_EncryptableVolume**](win32-encryptablevolume.md)
</dt> </dl>

 

 




