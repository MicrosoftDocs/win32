---
title: GetSslCertificate method of the BitsCompactServerUrlGroup class
description: The GetSslCertificate method gets the SSL certificate for a port.
ms.assetid: ce8592c9-f105-4e2e-b979-0fbc325b26b9
keywords:
- GetSslCertificate method
- GetSslCertificate method, BitsCompactServerUrlGroup class
- BitsCompactServerUrlGroup class, GetSslCertificate method
topic_type:
- apiref
api_name:
- BitsCompactServerUrlGroup.GetSslCertificate
api_location:
- Root\microsoft\bits
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetSslCertificate method of the BitsCompactServerUrlGroup class

The **GetSslCertificate** method gets the SSL certificate for a port.

## Syntax


```mof
uint32 GetSslCertificate(
  [in]  uint16 Port,
  [out] string StoreName,
  [out] uint8  hashBlob[]
);
```



## Parameters

<dl> <dt>

*Port* \[in\]
</dt> <dd>

Specifies the port on which the certificate must be bound.

</dd> <dt>

*StoreName* \[out\]
</dt> <dd>

A null-terminated string that contains the name of the certificate store.

</dd> <dt>

*hashBlob* \[out\]
</dt> <dd>

Specifies the SHA1 hash that identifies the certificate.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                           |
| Redistributable<br/>          | Windows Management Framework on Windows Server 2008 with SP2<br/>                     |
| Namespace<br/>                | Root\\microsoft\\bits<br/>                                                            |
| MOF<br/>                      | <dl> <dt>BitsProvider.mof</dt> </dl> |



## See also

<dl> <dt>

[**BitsCompactServerUrlGroup**](bitslightweightserverurlgroup.md)
</dt> </dl>

 

 





