---
title: GetDACertificateFromSubjectName method of the PS\_RemoteAccessLocal class
description: This method retrieves a Certificate from the local machine which matches the specified subject name.
audience: developer
ms.assetid: d8c1b97a-3617-426f-8f47-1c8cc37c0a1f
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetDACertificateFromSubjectName method
- GetDACertificateFromSubjectName method, PS_RemoteAccessLocal class
- PS_RemoteAccessLocal class, GetDACertificateFromSubjectName method
topic_type:
- apiref
api_name:
- PS_RemoteAccessLocal.GetDACertificateFromSubjectName
api_location:
- RAServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetDACertificateFromSubjectName method of the PS\_RemoteAccessLocal class

This method retrieves a Certificate from the local machine which matches the specified subject name.

## Syntax


```mof
uint32 GetDACertificateFromSubjectName(
  [in]  string               SubjectName,
  [in]  boolean              IncludeSelfSigned,
  [in]  uint32               Flags,
  [out] DACertificateContext EncodedCertificate
);
```



## Parameters

<dl> <dt>

*SubjectName* \[in\]
</dt> <dd>

Certificate Subject name.

</dd> <dt>

*IncludeSelfSigned* \[in\]
</dt> <dd>

This boolean indicates that self signed certificates should also be included while searching.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Flags indicating specific options for the search. The values are: 0 - None. 1 - Only search certificates with Server EKU.

<dt>

<span id="0"></span>

**0** (0)


</dt> <dd></dd> <dt>

<span id="1"></span>

**1** (1)


</dt> <dd></dd> </dl> </dd> <dt>

*EncodedCertificate* \[out\]
</dt> <dd>

On success, contains a [**DACertificateContext**](dacertificatecontext.md) that describes the encoded certificate.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessLocal**](ps-remoteaccesslocal.md)
</dt> </dl>

 

 





