---
description: UnlockWithPassphrase method of the Win32_EncryptableVolume class - Uses the passphrase to obtain the derived key.
ms.assetid: 09b4ae7f-7084-42bd-8bbe-da686d6280e9
title: UnlockWithPassphrase method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.UnlockWithPassphrase
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# UnlockWithPassphrase method of the Win32\_EncryptableVolume class

The **UnlockWithPassphrase** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class uses the passphrase to obtain the derived key. After the derived key is calculated, the derived key is used to unlock the encrypted volume's master key.

> [!Note]  
> If the disc supports hardware encryption this function sets the band status to "unlocked""

 

## Syntax


```mof
uint32 UnlockWithPassphrase(
  [in] string Passphrase
);
```



## Parameters

<dl> <dt>

*Passphrase* \[in\]
</dt> <dd>

Type: **string**

A string that specifies the passphrase.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                                       | Description                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                                       | The method was successful.<br/>                                                                                     |
| <dl> <dt>**FVE\_E\_NOT\_ACTIVATED**</dt> <dt>2150694920 (0x80310008)</dt> </dl>                      | BitLocker is not enabled on the volume. Add a key protector to enable BitLocker. <br/>                              |
| <dl> <dt>**FVE\_E\_FIPS\_PREVENTS\_PASSPHRASE**</dt> <dt>2150695020 (0x8031006C)</dt> </dl>          | The group policy setting that requires FIPS compliance prevented the passphrase from being generated or used. <br/> |
| <dl> <dt>**FVE\_E\_POLICY\_INVALID\_PASSPHRASE\_LENGTH**</dt> <dt>2150695040 (0x80310080)</dt> </dl> | The passphrase provided does not meet the minimum or maximum length requirements.<br/>                              |
| <dl> <dt>**FVE\_E\_POLICY\_PASSPHRASE\_TOO\_SIMPLE**</dt> <dt>2150695041 (0x80310081)</dt> </dl>     | The passphrase does not meet the complexity requirements set by the administrator in group policy.<br/>             |
| <dl> <dt>**FVE\_E\_FAILED\_AUTHENTICATION**</dt> <dt>2150694951 (0x80310027)</dt> </dl>              | The volume cannot be unlocked with the provided information. <br/>                                                  |
| <dl> <dt>**FVE\_E\_PROTECTOR\_NOT\_FOUND**</dt> <dt>2150694963 (0x80310033)</dt> </dl>               | The provided key protector does not exist on the volume. You must enter another key protector.<br/>                 |



 

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

 

 




