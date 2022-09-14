---
description: Changes the PIN associated with an encrypted volume.
ms.assetid: 8b0043cc-cf86-44e5-ab7c-038a6782f347
title: ChangePIN method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.ChangePIN
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# ChangePIN method of the Win32\_EncryptableVolume class

The **ChangePIN** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class changes the PIN associated with an encrypted volume. If the "Allow enhanced PINs for startup" group policy is enabled, a PIN can contain letters, symbols, and spaces in addition to numbers.

## Syntax


```mof
uint32 ChangePIN(
  [in] string VolumeKeyProtectorID,
  [in] string NewPIN
);
```



## Parameters

<dl> <dt>

*VolumeKeyProtectorID* \[in\]
</dt> <dd>

Type: **string**

The unique string identifier used to manage an encrypted volume key protector.

</dd> <dt>

*NewPIN* \[in\]
</dt> <dd>

Type: **string**

A user-specified personal identification string. This string must consist of a sequence of 4 to 20 digits or, if the "Allow enhanced PINs for startup" group policy is enabled, 4 to 20 letters, symbols, spaces, or numbers.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                                | The method was successful.<br/>                                                                                                                                                                                                                                                                                                                                                                       |
| <dl> <dt>**FVE\_E\_BOOTABLE\_CDDVD**</dt> <dt>2150694960 (0x80310030)</dt> </dl>              | A bootable CD/DVD is found in this computer. Remove the CD/DVD and restart the computer.<br/>                                                                                                                                                                                                                                                                                                         |
| <dl> <dt>**FVE\_E\_INVALID\_PIN\_CHARS**</dt> <dt>2150695066 (0x8031009A)</dt> </dl>          | The *NewPIN* parameter contains characters that are not valid. When the "Allow enhanced PINs for startup" Group Policy is disabled, only numbers are supported.<br/>                                                                                                                                                                                                                                  |
| <dl> <dt>**FVE\_E\_INVALID\_PROTECTOR\_TYPE**</dt> <dt>2150694970 (0x8031003A)</dt> </dl>     | The *VolumeKeyProtectorID* parameter does not refer to a key protector of the type "Numerical Password" or "External Key". Use either the [**ProtectKeyWithNumericalPassword**](protectkeywithnumericalpassword-win32-encryptablevolume.md) or [**ProtectKeyWithExternalKey**](protectkeywithexternalkey-win32-encryptablevolume.md) method to create a key protector of the appropriate type.<br/> |
| <dl> <dt>**FVE\_E\_LOCKED\_VOLUME**</dt> <dt>2150694912 (0x80310000)</dt> </dl>               | The volume is locked.<br/>                                                                                                                                                                                                                                                                                                                                                                            |
| <dl> <dt>**FVE\_E\_NOT\_ACTIVATED**</dt> <dt>2150694920 (0x80310008)</dt> </dl>               | BitLocker is not enabled on the volume. Add a key protector to enable BitLocker. <br/>                                                                                                                                                                                                                                                                                                                |
| <dl> <dt>**FVE\_E\_POLICY\_INVALID\_PIN\_LENGTH**</dt> <dt>2150695016 (0x80310068)</dt> </dl> | The *NewPIN* parameter supplied is either longer than 20 characters, shorter than 4 characters, or shorter than the minimum length specified by Group Policy.<br/>                                                                                                                                                                                                                                    |
| <dl> <dt>**FVE\_E\_PROTECTOR\_NOT\_FOUND**</dt> <dt>2150694963 (0x80310033)</dt> </dl>        | The provided key protector does not exist on the volume.<br/>                                                                                                                                                                                                                                                                                                                                         |
| <dl> <dt>**TBS\_E\_SERVICE\_NOT\_RUNNING**</dt> <dt>2150121480 (0x80284008)</dt> </dl>        | No compatible Trusted Platform Module (TPM) is found on this computer.<br/>                                                                                                                                                                                                                                                                                                                           |



 

## Remarks

The **ChangePIN** method creates a new TPM and PIN protector based on the existing protector information and the newly provided PIN. The new protector will have the same GUID. The **ChangePIN** method can also be called to change the PIN of any key protector that uses a PIN, for example, TPM and PIN or TPM with PIN and USB.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Windows SDK. They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](../wmisdk/managed-object-format--mof-.md).

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

 

 
