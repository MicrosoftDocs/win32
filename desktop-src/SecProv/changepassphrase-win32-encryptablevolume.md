---
description: Uses the new passphrase to obtain a new derived key.
ms.assetid: 89398bae-a2a2-466c-8a1e-a702018d679f
title: ChangePassphrase method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.ChangePassphrase
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# ChangePassphrase method of the Win32\_EncryptableVolume class

The **ChangePassphrase** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class uses the new passphrase to obtain a new derived key. After the derived key is calculated, the new derived key is used to secure the encrypted volume's master key.

## Syntax


```mof
uint32 ChangePassphrase(
  [in]  string VolumeKeyProtectorID,
  [in]  string NewPassphrase,
  [out] string NewProtectorID
);
```



## Parameters

<dl> <dt>

*VolumeKeyProtectorID* \[in\]
</dt> <dd>

Type: **string**

A unique string identifier that is used to manage an encrypted volume key protector.

</dd> <dt>

*NewPassphrase* \[in\]
</dt> <dd>

Type: **string**

An updated string that specifies the passphrase.

</dd> <dt>

*NewProtectorID* \[out\]
</dt> <dd>

Type: **string**

An updated unique string identifier used to manage an encrypted volume key protector.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                                       | Description                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                                       | The method was successful.<br/>                                                                                  |
| <dl> <dt>**FVE\_E\_LOCKED\_VOLUME**</dt> <dt>2150694912 (0x80310000)</dt> </dl>                      | The volume is already locked by BitLocker Drive Encryption. You must unlock the drive from Control Panel.<br/>   |
| <dl> <dt>**FVE\_E\_NOT\_ACTIVATED**</dt> <dt>2150694920 (0x80310008)</dt> </dl>                      | BitLocker is not enabled on the volume. Add a key protector to enable BitLocker. <br/>                           |
| <dl> <dt>**FVE\_E\_OVERLAPPED\_UPDATE**</dt> <dt>2150694948 (0x80310024)</dt> </dl>                  | The control block for the encrypted volume was updated by another thread.<br/>                                   |
| <dl> <dt>**FVE\_E\_INVALID\_PROTECTOR\_TYPE**</dt> <dt>2150694970 (0x8031003A)</dt> </dl>            | The specified key protector is not of the correct type. <br/>                                                    |
| <dl> <dt>**FVE\_E\_POLICY\_INVALID\_PASSPHRASE\_LENGTH**</dt> <dt>2150695040 (0x80310080)</dt> </dl> | The updated passphrase provided does not meet the minimum or maximum length requirements. <br/>                  |
| <dl> <dt>**FVE\_E\_POLICY\_PASSPHRASE\_TOO\_SIMPLE**</dt> <dt>2150695041 (0x80310081)</dt> </dl>     | The updated passphrase does not meet the complexity requirements set by the administrator in group policy. <br/> |



 

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

 

 




