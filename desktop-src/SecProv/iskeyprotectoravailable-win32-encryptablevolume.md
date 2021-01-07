---
description: Indicates whether protectors are available for the volume.
ms.assetid: 92a959ea-27ec-4d38-a955-846bfd7b3a60
title: IsKeyProtectorAvailable method of the Win32_EncryptableVolume class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_EncryptableVolume.IsKeyProtectorAvailable
api_type: 
- COM
api_location: 
- Root\CIMV2\Security\MicrosoftVolumeEncryption
---

# IsKeyProtectorAvailable method of the Win32\_EncryptableVolume class

The **IsKeyProtectorAvailable** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class indicates whether protectors are available for the volume.

If a protector type is provided, then the method indicates whether protectors of the specified type are available for the volume.

## Syntax


```mof
uint32 IsKeyProtectorAvailable(
  [in, optional] uint32  KeyProtectorType,
  [out]          boolean IsKeyProtectorAvailable
);
```



## Parameters

<dl> <dt>

*KeyProtectorType* \[in, optional\]
</dt> <dd>

Type: **uint32**

An unsigned integer that indicates the type of volume key protector queried.

If this parameter is not specified, all available key protectors of the volume are queried.



| Value                                                                         | Meaning                                                          |
|-------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl>  | All types.<br/> All key protectors are queried.<br/> |
| <dl> <dt>1</dt> </dl>  | Trusted Platform Module (TPM).<br/>                        |
| <dl> <dt>2</dt> </dl>  | External key.<br/>                                         |
| <dl> <dt>3</dt> </dl>  | Numerical password.<br/>                                   |
| <dl> <dt>4</dt> </dl>  | TPM And PIN.<br/>                                          |
| <dl> <dt>5</dt> </dl>  | TPM And Startup Key.<br/>                                  |
| <dl> <dt>6</dt> </dl>  | TPM And PIN And Startup Key.<br/>                          |
| <dl> <dt>7</dt> </dl>  | Public Key.<br/>                                           |
| <dl> <dt>8</dt> </dl>  | Passphrase.<br/>                                           |
| <dl> <dt>9</dt> </dl>  | TPM Certificate<br/>                                       |
| <dl> <dt>10</dt> </dl> | Security Identifier (SID)<br/>                             |



 

</dd> <dt>

*IsKeyProtectorAvailable* \[out\]
</dt> <dd>

Type: **boolean**

A Boolean value that indicates whether a volume key protector of the specified type exists on the volume.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                         | Description                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                         | The method was successful.<br/>                                                                      |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>2147942487 (0x80070057)</dt> </dl> | The *KeyProtectorType* parameter is specified but does not refer to a valid key protector type.<br/> |



 

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

 

 
