---
title: SetSslCertificate method of the BitsCompactServerUrlGroup class
description: The SetSslCertificate method sets the SSL certificate for a port.
ms.assetid: 888e4468-bbdf-4b28-a95c-24e8ff149a9f
keywords:
- SetSslCertificate method
- SetSslCertificate method, BitsCompactServerUrlGroup class
- BitsCompactServerUrlGroup class, SetSslCertificate method
topic_type:
- apiref
api_name:
- BitsCompactServerUrlGroup.SetSslCertificate
api_location:
- Root\microsoft\bits
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetSslCertificate method of the BitsCompactServerUrlGroup class

The **SetSslCertificate** method sets the SSL certificate for a port.

## Syntax


```mof
uint32 SetSslCertificate(
  [in] uint16 Port,
  [in] string StoreName,
  [in] uint8  hashBlob[]
);
```



## Parameters

<dl> <dt>

*Port* \[in\]
</dt> <dd>

Specifies the port on which the certificate must be bound.

</dd> <dt>

*StoreName* \[in\]
</dt> <dd>

A null-terminated string that contains the name of the certificate store.

</dd> <dt>

*hashBlob* \[in\]
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

 

 





