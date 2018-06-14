---
Description: Enumerates all certificates on the system that match the indicated criteria and returns a list of thumbprints.
ms.assetid: 69522afe-9870-4ae9-8c69-cf8787913615
title: FindValidCertificates method of the Win32\_EncryptableVolume class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FindValidCertificates method of the Win32\_EncryptableVolume class

The **FindValidCertificates** method of the [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) class enumerates all certificates on the system that match the indicated criteria and returns a list of thumbprints. The returned list only contains certificates with a valid [*object identifier*](https://msdn.microsoft.com/en-us/library/ms721599(v=VS.85).aspx) (OID). The OID may be the default, or it may be specified in the Group Policy.

## Syntax


```mof
uint32 FindValidCertificates(
  [out] string CertificateThumbprint[]
);
```



## Parameters

<dl> <dt>

*CertificateThumbprint* \[out\]
</dt> <dd>

Type: **string\[\]**

An array of strings that contains the list of valid certificates.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following codes or another error code if it fails.



| Return code/value                                                                                                                                                                           | Description                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0 (0x0)</dt> </dl>                                           | The method was successful.<br/>                |
| <dl> <dt>**FVE\_E\_INVALID\_BITLOCKER\_OID**</dt> <dt>2150695022 (0x8031006E)</dt> </dl> | The available BitLocker OID is not valid.<br/> |



 

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

 

 




