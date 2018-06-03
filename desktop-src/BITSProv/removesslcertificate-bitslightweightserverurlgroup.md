---
title: RemoveSslCertificate method of the BitsCompactServerUrlGroup class
description: The RemoveSslCertificate method removes the SSL certificate for a port.
ms.assetid: 31ee32b1-4859-4e4e-bc8c-d997225accd8
keywords:
- RemoveSslCertificate method
- RemoveSslCertificate method, BitsCompactServerUrlGroup class
- BitsCompactServerUrlGroup class, RemoveSslCertificate method
topic_type:
- apiref
api_name:
- BitsCompactServerUrlGroup.RemoveSslCertificate
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

# RemoveSslCertificate method of the BitsCompactServerUrlGroup class

The **RemoveSslCertificate** method removes the SSL certificate for a port.

## Syntax


```mof
uint32 RemoveSslCertificate(
  [in] uint16 Port
);
```



## Parameters

<dl> <dt>

*Port* \[in\]
</dt> <dd>

Specifies the port on which the certificate to be removed is bound.

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

 

 





