---
Description: Creates a BitLocker volume with the specified file system type of the discovery volume.
ms.assetid: 088e7224-a336-4742-a12f-86755defe16c
title: PrepareVolume method of the Win32\_EncryptableVolume class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PrepareVolume method of the Win32\_EncryptableVolume class

The **PrepareVolume** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class creates a BitLocker volume with the specified file system type of the discovery volume. This method must be called before the volume can be protected with any of the **ProtectKeyWith\*** methods.

## Syntax


```mof
uint32 PrepareVolume(
  [in] string DiscoveryVolumeType,
  [in] uint32 ForceEncryptionType
);
```



## Parameters

<dl> <dt>

*DiscoveryVolumeType* \[in\]
</dt> <dd>

Type: **string**

A string that specifies the type of discovery volume.



| Value                                                                                                                                                  | Meaning                                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <span id="_none_"></span><span id="_NONE_"></span><dl> <dt>**&lt;none&gt;**</dt> </dl>          | No discovery volume. This value creates a native BitLocker volume.<br/> |
| <span id="_default_"></span><span id="_DEFAULT_"></span><dl> <dt>**&lt;default&gt;**</dt> </dl> | This value is the default behavior.<br/>                                |
| <span id="FAT32"></span><span id="fat32"></span><dl> <dt>**FAT32**</dt> </dl>                   | This value creates a FAT32 discovery volume.<br/>                       |



 

</dd> <dt>

*ForceEncryptionType* \[in\]
</dt> <dd>

Type: **uint32**

Integer that specifies the encryption type. This can be one of the following values.



| Value                                                                                                                                                                                                                                       | Meaning                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| <span id="Unspecified"></span><span id="unspecified"></span><span id="UNSPECIFIED"></span><dl> <dt>**Unspecified**</dt> <dt>0</dt> </dl> | The encryption type is not specified.<br/> |
| <span id="Software"></span><span id="software"></span><span id="SOFTWARE"></span><dl> <dt>**Software**</dt> <dt>1</dt> </dl>             | Software encryption.<br/>                  |
| <span id="Hardware"></span><span id="hardware"></span><span id="HARDWARE"></span><dl> <dt>**Hardware**</dt> <dt>2</dt> </dl>             | Hardware encryption.<br/>                  |



 

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                 | Description                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl> | The method was successful.<br/> |



 

## Remarks

If you do not call this method when enabling a BitLocker volume, it is the same as calling this method with the default value in the *DiscoveryVolumeType* parameter.

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 Enterprise, Windows 7 Ultimate \[desktop apps only\]<br/>                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                 |
| Namespace<br/>                | Root\\CIMV2\\Security\\MicrosoftVolumeEncryption<br/>                                             |
| MOF<br/>                      | <dl> <dt>Win32\_encryptablevolume.mof</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_EncryptableVolume**](win32-encryptablevolume.md)
</dt> </dl>

 

 




