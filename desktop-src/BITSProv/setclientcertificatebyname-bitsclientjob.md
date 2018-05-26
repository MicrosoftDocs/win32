---
title: SetClientCertificateByName method of the BitsClientJob class
description: The SetClientCertificateByName method sets the client certificate to use for client authentication in an HTTPS (SSL) request.
ms.assetid: 37e6b35f-8955-4524-abe4-8f4c6f39d1fa
keywords:
- SetClientCertificateByName method
- SetClientCertificateByName method, BitsClientJob class
- BitsClientJob class, SetClientCertificateByName method
topic_type:
- apiref
api_name:
- BitsClientJob.SetClientCertificateByName
api_location:
- bits2_5.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SetClientCertificateByName method of the BitsClientJob class

The **SetClientCertificateByName** method sets the client certificate to use for client authentication in an HTTPS (SSL) request.

## Syntax


```mof
uint32 SetClientCertificateByName(
  [in] uint16 CertStoreLocation,
  [in] string StoreName,
  [in] string SubjectName
);
```



## Parameters

<dl> <dt>

*CertStoreLocation* \[in\]
</dt> <dd>

Defines the location of the client certificate store. This parameter can be set to one of the following values:



| Store                                                                        | Meaning                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | Use the current user's certificate store.<br/>                                                                                                                                                                        |
| <dl> <dt>1</dt> </dl> | Use the local computer's certificate store.<br/>                                                                                                                                                                      |
| <dl> <dt>2</dt> </dl> | Use the current service's certificate store.<br/>                                                                                                                                                                     |
| <dl> <dt>3</dt> </dl> | Use a specific service's certificate store.<br/>                                                                                                                                                                      |
| <dl> <dt>4</dt> </dl> | Use a specific user's certificate store.<br/>                                                                                                                                                                         |
| <dl> <dt>5</dt> </dl> | Use the current user's Group Policy certificate store. In a network setting, stores in this location are downloaded to the client computer from the Group Policy template during computer startup or user logon.<br/> |
| <dl> <dt>6</dt> </dl> | Use the local computer's certificate store. In a network setting, stores in this location are downloaded to the client computer from the Group Policy template during computer startup or user logon.<br/>            |
| <dl> <dt>7</dt> </dl> | Use the enterprise certificate store. The enterprise store is shared across domains in the enterprise and downloaded from the global enterprise directory.<br/>                                                       |



 

</dd> <dt>

*StoreName* \[in\]
</dt> <dd>

A null-terminated string that contains the name of the certificate store.

</dd> <dt>

*SubjectName* \[in\]
</dt> <dd>

A null-terminated string that contains the simple subject name of the certificate.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                           |
| Redistributable<br/>          | Windows Management Framework on Windows Server 2008 with SP2<br/>                     |
| Namespace<br/>                | Root\\microsoft\\bits<br/>                                                            |
| Header<br/>                   | <dl> <dt>Bits2\_5.h</dt> </dl>       |
| MOF<br/>                      | <dl> <dt>BitsProvider.mof</dt> </dl> |



## See also

<dl> <dt>

[**BitsClientJob**](bitsclientjob.md)
</dt> </dl>

 

 





