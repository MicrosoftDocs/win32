---
title: IsDfsRoot
description: Identifies a file share \ 32;resource as a DFS root.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5d4f17f5-56f4-4994-a9c8-ded974a49224
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- IsDfsRoot Failover Cluster ,for file shares
- IsDfsRoot Failover Cluster
topic_type:
- apiref
api_name:
- IsDfsRoot
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IsDfsRoot

\[The **IsDfsRoot** property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2003:  **

Identifies a [file share](file-share.md) [resource](resources.md) as a DFS root. The following table summarizes the attributes of the **IsDfsRoot** property.



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

The data value for the **IsDfsRoot** property can be set to one of the following values.



| IsDfsRoot property data value | Description                       |
|-------------------------------|-----------------------------------|
| **FALSE**                     | The file share is not a DFS root. |
| **TRUE**                      | The file share is a DFS root.     |



 

There can be only one DFS root per [*cluster*](c-gly.md#-wolf-cluster-gly). In other words, a cluster can have only one file share resource whose **IsDfsRoot** property is set to **TRUE**.

## Examples

The property value portion of a [property list](property-lists.md) entry for **IsDfsRoot** can be set with the following example code.


```C++
DWORD          IsDfsRootData = TRUE;
CLUSPROP_DWORD IsDfsRootValue;

IsDfsRootValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
IsDfsRootValue.cbLength  = sizeof(DWORD);
IsDfsRootValue.dw        = IsDfsRootData;
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

 

 





