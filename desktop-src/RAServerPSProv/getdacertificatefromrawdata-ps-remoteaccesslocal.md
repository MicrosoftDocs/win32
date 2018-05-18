---
title: GetDACertificateFromRawData method of the PS\_RemoteAccessLocal class
description: This method retrieves a Certificate from the local machine which matches the input raw data.
audience: developer
ms.assetid: 'c5649292-329c-43fa-9b67-56049a1423c0'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetDACertificateFromRawData method", "GetDACertificateFromRawData method, PS_RemoteAccessLocal class", "PS_RemoteAccessLocal class, GetDACertificateFromRawData method"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessLocal.GetDACertificateFromRawData
api_location:
- RAServerPSProvider.dll
api_type:
- COM
---

# GetDACertificateFromRawData method of the PS\_RemoteAccessLocal class

This method retrieves a Certificate from the local machine which matches the input raw data.

## Syntax


```mof
uint32 GetDACertificateFromRawData(
  [in]  uint8                CertificateRawData[],
  [in]  uint32               CertificateRawDataType,
  [in]  uint32               Purpose,
  [out] DACertificateContext EncodedCertificate
);
```



## Parameters

<dl> <dt>

*CertificateRawData* \[in\]
</dt> <dd>

Raw certificate data.

</dd> <dt>

*CertificateRawDataType* \[in\]
</dt> <dd>

Type of data in the CertificateRawData field.

<dt>

<span id="0"></span>

<span id="0"></span>**0** (0)


</dt> <dd>

None

</dd> <dt>

<span id="1"></span>

<span id="1"></span>**1** (1)


</dt> <dd>

SHA1 hash

</dd> <dt>

<span id="2"></span>

<span id="2"></span>**2** (2)


</dt> <dd>

SHA256 hash

</dd> <dt>

<span id="3"></span>

<span id="3"></span>**3** (3)


</dt> <dd>

Encoded Certificate from CERT\_CONTEXT

</dd> </dl> </dd> <dt>

*Purpose* \[in\]
</dt> <dd>

The purpose for which the certificate would be used. The values for this field are: 0 - None 1 - IP-HTTPS Certificate 2 - NLS Certificate 3 - IPsec Root Certificate 4 - IPsec Intermediate Certificate 5 - VPN.

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

On success, contains a [**DACertificateContext**](dacertificatecontext.md) that describes the encoded certificate.

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

 

 





