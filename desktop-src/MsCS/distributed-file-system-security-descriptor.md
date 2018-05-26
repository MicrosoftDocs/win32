---
title: Security Descriptor
description: security descriptor of a Distributed File System resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 13f6cceb-54b8-4134-8e34-467bc1a4c4be
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Security Descriptor Failover Cluster ,for file system
- Security Descriptor Failover Cluster
topic_type:
- apiref
api_name:
- Security Descriptor
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Security Descriptor

Stores the [security descriptor](https://msdn.microsoft.com/library/windows/desktop/aa379563) of a Distributed File System resource. The following table summarizes the attributes of the **Security Descriptor** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Byte array                                                       |
| Access    | [Read/write](read-write-properties.md) (see Remarks)            |
| Status    | Optional                                                         |
| Structure | [**CLUSPROP\_BINARY**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_binary?branch=master)                      |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | 0                                                                |



 

## Remarks

Although the property value is read/write, the underlying security descriptor can be changed only through the [Access Control](https://msdn.microsoft.com/library/windows/desktop/aa374860) or [Network Management](https://msdn.microsoft.com/library/windows/desktop/aa370672) APIs. To change the value of the **Security Descriptor** property.

-   Retrieve the value of the property.

-   Assign the value to a [**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/desktop/aa379561) structure.

-   Pass the value to any Access Control or Network Management API function that will change the discretionary access control list (DACL) of the descriptor, such as [**SetSecurityDescriptorDacl**](https://msdn.microsoft.com/library/windows/desktop/aa379583) or [**NetShareSetInfo**](https://msdn.microsoft.com/library/windows/desktop/bb525389).

-   Once the value has been modified, update the **Security Descriptor** property.

-   Take the Distributed File System resource offline and bring it back online to activate the new security settings.

**Note**  

When you use the Failover Cluster API to create the File Share resource, permissions for the "Everyone" group for that file share are set to full control by default. You can modify this property as previously described to change the default permissions.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Distributed File System Private Properties](distributed-file-system-private-properties.md)
</dt> <dt>

[Access Control](https://msdn.microsoft.com/library/windows/desktop/aa374860)
</dt> <dt>

[**CLUSPROP\_BINARY**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_binary?branch=master)
</dt> <dt>

[Network Management](https://msdn.microsoft.com/library/windows/desktop/aa370672)
</dt> <dt>

[**NetShareSetInfo**](https://msdn.microsoft.com/library/windows/desktop/bb525389)
</dt> <dt>

[**Security**](file-shares-security.md)
</dt> <dt>

[**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/desktop/aa379561)
</dt> <dt>

[**SetSecurityDescriptorDacl**](https://msdn.microsoft.com/library/windows/desktop/aa379583)
</dt> </dl>

 

 





