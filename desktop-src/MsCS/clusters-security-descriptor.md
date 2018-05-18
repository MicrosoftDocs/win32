---
title: Security Descriptor
description: Stores the security descriptor of a cluster. The following table summarizes the attributes of the Security Descriptor property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd2a416bc-891e-42b0-a67f-04d0b257ffac'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Security Descriptor Failover Cluster ,for clusters", "Security Descriptor Failover Cluster"]
topic_type:
- apiref
api_name:
- Security Descriptor
api_type:
- NA
---

# Security Descriptor

Stores the [security descriptor](https://msdn.microsoft.com/library/windows/desktop/aa379563) of a [*cluster*](c-gly.md#-wolf-cluster-gly). The following table summarizes the attributes of the Security Descriptor property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Byte array                                                       |
| Access    | [Read/write](read-write-properties.md) (see Remarks)            |
| Structure | [**CLUSPROP\_BINARY**](clusprop-binary.md)                      |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | 0                                                                |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_CLUS\_SD**.

Although the property value is read/write, the underlying security descriptor can be changed only through the [Access Control](https://msdn.microsoft.com/library/windows/desktop/aa374860) or [Network Management](https://msdn.microsoft.com/library/windows/desktop/aa370672) APIs. To change the value of the Security Descriptor property:

-   Retrieve the value of the property.
-   Assign the value to a [**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/desktop/aa379561) structure.
-   Pass the value to any Access Control or Network Management API function that will change the DACL of the descriptor, such as [**SetSecurityDescriptorDacl**](https://msdn.microsoft.com/library/windows/desktop/aa379583) or [**NetShareSetInfo**](https://msdn.microsoft.com/library/windows/desktop/bb525389).
-   Once the value has been modified, update the Security Descriptor property.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[Access Control](https://msdn.microsoft.com/library/windows/desktop/aa374860)
</dt> <dt>

[**CLUSPROP\_BINARY**](clusprop-binary.md)
</dt> <dt>

[Network Management](https://msdn.microsoft.com/library/windows/desktop/aa370672)
</dt> <dt>

[**NetShareSetInfo**](https://msdn.microsoft.com/library/windows/desktop/bb525389)
</dt> <dt>

[**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/desktop/aa379561)
</dt> <dt>

[**SetSecurityDescriptorDacl**](https://msdn.microsoft.com/library/windows/desktop/aa379583)
</dt> </dl>

 

 





