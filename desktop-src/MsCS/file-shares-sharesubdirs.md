---
title: ShareSubDirs
description: Determines whether the subdirectories of a file share are included in the share.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dde4819a-268e-42a8-841f-7bcabf3c2167
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ShareSubDirs Failover Cluster ,for file shares
- ShareSubDirs Failover Cluster
topic_type:
- apiref
api_name:
- ShareSubDirs
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ShareSubDirs

\[The **ShareSubDirs** property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2003:  **

Determines whether the subdirectories of a [file share](file-share.md) are included in the share. The following table summarizes the attributes of the **ShareSubDirs** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | **FALSE**                                 |
| Maximum   | **TRUE**                                  |
| Default   | **FALSE**                                 |



 

## Remarks

The **ShareSubDirs** property can be set to one of the following values.



| Value     | Description                                                     |
|-----------|-----------------------------------------------------------------|
| **TRUE**  | Any subdirectories of the file share are included in the share. |
| **FALSE** | No subdirectories are included in the share.                    |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **ShareSubDirs** can be set with the following example code.


```C++
DWORD          ShareSubDirsData  = TRUE;
CLUSPROP_DWORD ShareSubDirsValue;

ShareSubDirsValue.Syntax.dw      = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
ShareSubDirsValue.cbLength       = sizeof(DWORD);
ShareSubDirsValue.dw             = ShareSubDirsData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[File Share Private Properties](file-share-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> </dl>

 

 





