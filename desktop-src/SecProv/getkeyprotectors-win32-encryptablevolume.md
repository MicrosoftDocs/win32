---
description: Lists the protectors used to secure the volume's encryption key.
ms.assetid: ea88f128-c835-49e3-a395-c5ba472fff4b
title: GetKeyProtectors method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.GetKeyProtectors
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# GetKeyProtectors method of the Win32\_EncryptableVolume class

The **GetKeyProtectors** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class lists the protectors used to secure the volume's encryption key. If a protector type is provided, then only volume key protectors of the specified type are returned.

## Syntax


```mof
uint32 GetKeyProtectors(
  [in, optional] uint32 KeyProtectorType,
  [out]          string VolumeKeyProtectorID[]
);
```



## Parameters

<dl> <dt>

*KeyProtectorType* \[in, optional\]
</dt> <dd>

Type: **uint32**

An unsigned integer that specifies the type of key protector to return.

If this parameter is not specified, all available key protectors of the volume are returned.



| Value                                                                         | Meaning                                                           |
|-------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl>  | All types.<br/> All key protectors are returned.<br/> |
| <dl> <dt>1</dt> </dl>  | Trusted Platform Module (TPM).<br/>                         |
| <dl> <dt>2</dt> </dl>  | External key.<br/>                                          |
| <dl> <dt>3</dt> </dl>  | Numeric password.<br/>                                      |
| <dl> <dt>4</dt> </dl>  | TPM And PIN.<br/>                                           |
| <dl> <dt>5</dt> </dl>  | TPM And Startup Key.<br/>                                   |
| <dl> <dt>6</dt> </dl>  | TPM And PIN And Startup Key.<br/>                           |
| <dl> <dt>7</dt> </dl>  | Public Key.<br/>                                            |
| <dl> <dt>8</dt> </dl>  | Passphrase.<br/>                                            |
| <dl> <dt>9</dt> </dl>  | TPM Certificate<br/>                                        |
| <dl> <dt>10</dt> </dl> | Security Identifier (SID)<br/>                              |



 

</dd> <dt>

*VolumeKeyProtectorID* \[out\]
</dt> <dd>

Type: **string\[\]**

An array of strings that identify the key protectors used to secure the volume's encryption key.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                  | Description                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                  | The method was successful.<br/>                                                                          |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>2147942487 (0x80070057)</dt> </dl>          | The *VolumeKeyProtectorID* parameter is specified but does not refer to a valid *KeyProtectorType*.<br/> |
| <dl> <dt>**FVE\_E\_NOT\_ACTIVATED**</dt> <dt>2150694920 (0x80310008)</dt> </dl> | BitLocker is not enabled on the volume. Add a key protector to enable BitLocker. <br/>                   |



 

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

 

 
