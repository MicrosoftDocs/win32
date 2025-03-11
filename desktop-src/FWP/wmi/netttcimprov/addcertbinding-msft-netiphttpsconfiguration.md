---
description: Adds a HTTP SSL certificate to the profile.
ms.assetid: 2d5d5c2a-33d3-4a41-8624-db0ab7e86914
title: AddCertBinding method of the MSFT\_NetIPHttpsConfiguration class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# AddCertBinding method of the MSFT\_NetIPHttpsConfiguration class

Adds a HTTP SSL certificate to the profile.

## Syntax


```mof
uint32 AddCertBinding(
  [in] string  CertificateHash,
  [in] string  ApplicationId,
  [in] string  IpPort,
  [in] string  CertificateStoreName,
  [in] boolean NullEncryption
);
```



## Parameters

<dl> <dt>

*CertificateHash* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*ApplicationId* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*IpPort* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*CertificateStoreName* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*NullEncryption* \[in\]
</dt> <dd>

TBD

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTtCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTtCim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetIPHttpsConfiguration**](msft-netiphttpsconfiguration.md)
</dt> </dl>

 

 




