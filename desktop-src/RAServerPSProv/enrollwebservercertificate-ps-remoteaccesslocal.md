---
title: EnrollWebServerCertificate method of the PS\_RemoteAccessLocal class
description: This method enrolls a web server certificate.
audience: developer
ms.assetid: '0eedd0b3-4b78-473b-8b67-7504e7fad082'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["EnrollWebServerCertificate method", "EnrollWebServerCertificate method, PS_RemoteAccessLocal class", "PS_RemoteAccessLocal class, EnrollWebServerCertificate method"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessLocal.EnrollWebServerCertificate
api_location:
- RAServerPSProvider.dll
api_type:
- COM
---

# EnrollWebServerCertificate method of the PS\_RemoteAccessLocal class

This method enrolls a web server certificate.

## Syntax


```mof
uint32 EnrollWebServerCertificate(
  [in]  string TemplateName,
  [in]  string SubjectName,
  [out] uint8  EncodedCertificate[]
);
```



## Parameters

<dl> <dt>

*TemplateName* \[in\]
</dt> <dd>

Template name of the Certificate

</dd> <dt>

*SubjectName* \[in\]
</dt> <dd>

Subject name of the certificate

</dd> <dt>

*EncodedCertificate* \[out\]
</dt> <dd>

The certificate

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessLocal**](ps-remoteaccesslocal.md)
</dt> </dl>

 

 





