---
title: CreateUrl method of the BitsCompactServerUrlGroup class
description: The CreateUrl method creates a URL on the host. This method also creates a URL group on the host if the URL group was not available earlier.
ms.assetid: '723be8ba-8c3b-43b6-aa76-87d4d0bd6a5f'
keywords: ["CreateUrl method", "CreateUrl method, BitsCompactServerUrlGroup class", "BitsCompactServerUrlGroup class, CreateUrl method"]
topic_type:
- apiref
api_name:
- BitsCompactServerUrlGroup.CreateUrl
api_location:
- Root\microsoft\bits
api_type:
- COM
---

# CreateUrl method of the BitsCompactServerUrlGroup class

The **CreateUrl** method creates a URL on the host. This method also creates a URL group on the host if the URL group was not available earlier.

## Syntax


```mof
uint32 CreateUrl(
  [in]           string UrlSuffix,
  [in]           string SourceFilePath,
  [in]           string SDDLAuth,
  [in, optional] uint8  CertificateHashAccessCheck[]
);
```



## Parameters

<dl> <dt>

*UrlSuffix* \[in\]
</dt> <dd>

Specifies the URL suffix for the BITS transfer job.

</dd> <dt>

*SourceFilePath* \[in\]
</dt> <dd>

Specifies the path of the source file to be hosted on the server.

</dd> <dt>

*SDDLAuth* \[in\]
</dt> <dd>

Specifies the security descriptor string that is used to authenticate client requests for the specified BITS transfer job.

</dd> <dt>

*CertificateHashAccessCheck* \[in, optional\]
</dt> <dd>

Reserved for future use.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                           |
| Redistributable<br/>          | Windows Management Framework on Windows Server 2008 with SP2<br/>                     |
| Namespace<br/>                | Root\\microsoft\\bits<br/>                                                            |
| MOF<br/>                      | <dl> <dt>BitsProvider.mof</dt> </dl> |



## See also

<dl> <dt>

[**BitsCompactServerUrlGroup**](bitslightweightserverurlgroup.md)
</dt> </dl>

 

 





