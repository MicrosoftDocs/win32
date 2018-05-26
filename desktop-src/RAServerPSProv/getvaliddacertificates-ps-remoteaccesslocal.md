---
title: GetValidDACertificates method of the PS\_RemoteAccessLocal class
description: This method retrieves a list of certificates for DirectAccess based on the purpose specified.
audience: developer
ms.assetid: bee3067a-7272-42e0-833d-4bdf218ce458
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetValidDACertificates method
- GetValidDACertificates method, PS_RemoteAccessLocal class
- PS_RemoteAccessLocal class, GetValidDACertificates method
topic_type:
- apiref
api_name:
- PS_RemoteAccessLocal.GetValidDACertificates
api_location:
- RAServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetValidDACertificates method of the PS\_RemoteAccessLocal class

This method retrieves a list of certificates for DirectAccess based on the purpose specified.

## Syntax


```mof
uint32 GetValidDACertificates(
  [in]  uint32               Purpose,
  [out] DACertificateContext EncodedCertificate[]
);
```



## Parameters

<dl> <dt>

*Purpose* \[in\]
</dt> <dd>

The purpose for which this certificate will be used. The values are: 0 - None 1 - IP-HTTPS Certificate 2 - NLS Certificate 3 - IPsec Root Certificate 4 - IPsec Intermediate Certificate 5 - VPN.

<dt>

<span id="0"></span>

**0** (0)


</dt> <dd></dd> <dt>

<span id="1"></span>

**1** (1)


</dt> <dd></dd> <dt>

<span id="2"></span>

**2** (2)


</dt> <dd></dd> <dt>

<span id="3"></span>

**3** (3)


</dt> <dd></dd> <dt>

<span id="4"></span>

**4** (4)


</dt> <dd></dd> <dt>

<span id="5"></span>

**5** (5)


</dt> <dd></dd> </dl> </dd> <dt>

*EncodedCertificate* \[out\]
</dt> <dd>

On success, contains an array of [**DACertificateContext**](dacertificatecontext.md) objects that correspond to the purpose specified in the input.

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

 

 





