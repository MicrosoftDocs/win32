---
title: CreateSelfSignedCertificate method of the PS\_RemoteAccessLocal class
description: This method creates a self signed certificate.
audience: developer
ms.assetid: '08c1675b-0e87-4ca9-b447-cf4a6ae8f722'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateSelfSignedCertificate method", "CreateSelfSignedCertificate method, PS_RemoteAccessLocal class", "PS_RemoteAccessLocal class, CreateSelfSignedCertificate method"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessLocal.CreateSelfSignedCertificate
api_location:
- RAServerPSProvider.dll
api_type:
- COM
---

# CreateSelfSignedCertificate method of the PS\_RemoteAccessLocal class

This method creates a self signed certificate.

## Syntax


```mof
uint32 CreateSelfSignedCertificate(
  [in]  string SubjectName,
  [in]  string FriendlyName,
  [in]  uint32 Purpose,
  [out] uint8  EncodedCertificate[]
);
```



## Parameters

<dl> <dt>

*SubjectName* \[in\]
</dt> <dd>

Subject name of the Certificate

</dd> <dt>

*FriendlyName* \[in\]
</dt> <dd>

Friendly name of the certificate

</dd> <dt>

*Purpose* \[in\]
</dt> <dd>

Bitmasked purpose of this Self-signed certificate 1st Bit - Server Authentication. 2nd Bit - Data Encryption

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

 

 





