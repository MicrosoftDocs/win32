---
title: SetSSTPCertificate method of the PS\_RemoteAccessLocal class
description: This method is used to set the SSTP certificate on the RemoteAccess server.
audience: developer
ms.assetid: 90c67f71-0764-48f1-a09a-40b95110f50b
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetSSTPCertificate method
- SetSSTPCertificate method, PS_RemoteAccessLocal class
- PS_RemoteAccessLocal class, SetSSTPCertificate method
topic_type:
- apiref
api_name:
- PS_RemoteAccessLocal.SetSSTPCertificate
api_location:
- RAServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetSSTPCertificate method of the PS\_RemoteAccessLocal class

This method is used to set the SSTP certificate on the RemoteAccess server.

## Syntax


```mof
uint32 SetSSTPCertificate(
  [in] uint8   CertificateHash[],
  [in] boolean UseHttps
);
```



## Parameters

<dl> <dt>

*CertificateHash* \[in\]
</dt> <dd>

The SHA256 hash of the SSTP Certificate.

</dd> <dt>

*UseHttps* \[in\]
</dt> <dd>

Use HTTPs protocol for SSTP connection.

**Windows Server 2012 and Windows Server 2012 R2:** This parameter does not exist prior to Windows Server 2016.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessLocal**](ps-remoteaccesslocal.md)
</dt> </dl>

 

 





