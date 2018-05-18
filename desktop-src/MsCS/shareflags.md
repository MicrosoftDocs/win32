---
title: ShareFlags
description: Share flags of a File Share resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5a14f232-1d58-4d1c-8aa7-53a56a0374ac'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ShareFlags Failover Cluster , for File private properties", "ShareFlags Failover Cluster"]
topic_type:
- apiref
api_name:
- ShareFlags
api_type:
- NA
---

# ShareFlags

\[The **ShareFlags** property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2003:  **

Stores the share flags of a File Share resource. The following table summarizes the attributes of the **ShareFlags** property.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](clusprop-dword.md)<br/> |
| Minimum<br/>   | 0<br/>                                         |
| Maximum<br/>   | 0xF30<br/>                                     |
| Default<br/>   | 0<br/>                                         |



 

## Remarks

See the definition of the **SHI1005\_VALID\_FLAGS\_SET** value defined in LMShare.h and the descriptions of the values allowed for the **shi1005\_flags** member of the [**SHARE\_INFO\_1005**](https://msdn.microsoft.com/library/windows/desktop/bb525404) structure for more information on the meaning of the individual flags.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[File Share Private Properties](file-share-private-properties.md)
</dt> <dt>

[**ShareFlags property of a DFS resource**](distributed-file-system-shareflags.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





