---
title: AddCertificate method of the MDM\_SideLoader class
description: Adds the package-signing certificate.
ms.assetid: 397096e8-d7a9-442b-b1f0-d0ec08d1699e
keywords:
- AddCertificate method MDM Settings
- AddCertificate method MDM Settings , MDM_SideLoader class
- MDM_SideLoader class MDM Settings , AddCertificate method
topic_type:
- apiref
api_name:
- MDM_SideLoader.AddCertificate
api_location:
- MDMSettingsProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AddCertificate method of the MDM\_SideLoader class

Adds the package-signing certificate.

## Syntax


```mof
uint32 AddCertificate(
  [in] string CertificateBlob
);
```



## Parameters

<dl> <dt>

*CertificateBlob* \[in\]
</dt> <dd>

The certificate in Base64-encoded format.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| Header<br/>                   | <dl> <dt>Certenroll.h</dt> </dl>        |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MDM\_SideLoader**](https://msdn.microsoft.com/library/dn610395)
</dt> </dl>

 

 





