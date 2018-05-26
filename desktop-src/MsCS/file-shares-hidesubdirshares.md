---
title: HideSubDirShares
description: Determines whether the subdirectories of a file share are displayed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 32f8b7e6-7d94-41d0-9a64-d7f9a1fd93f2
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- HideSubDirShares Failover Cluster ,for file shares
- HideSubDirShares Failover Cluster
topic_type:
- apiref
api_name:
- HideSubDirShares
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# HideSubDirShares

\[The **HideSubDirShares** property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2003:  **

Determines whether the subdirectories of a [file share](file-share.md) are displayed. The following table summarizes the attributes of the **HideSubDirShares** property.



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

The **HideSubDirShares** property can be set to one of the following values.



| Value     | Description                                      |
|-----------|--------------------------------------------------|
| **TRUE**  | Any subdirectories of the file share are hidden. |
| **FALSE** | File share subdirectories are not hidden.        |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **HideSubDirShares** can be set with the following example code.


```C++
DWORD          HideSubDirSharesData = FALSE;
CLUSPROP_DWORD HideSubDirSharesValue;

HideSubDirSharesValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
HideSubDirSharesValue.cbLength  = sizeof(DWORD);
HideSubDirSharesValue.dw        = HideSubDirSharesData;
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

 

 





