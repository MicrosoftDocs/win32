---
title: RemapPipeNames
description: Controls how named pipes are opened on the network managed by the Network Name resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ca201852-b55d-4ce6-ab3b-c533f0ca6889
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- RemapPipeNames Failover Cluster ,for network names
- RemapPipeNames Failover Cluster
topic_type:
- apiref
api_name:
- RemapPipeNames
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemapPipeNames

Controls how named pipes are opened on the [network](networks.md) managed by the [Network Name](network-name.md) resource. The following table summarizes the attributes of the **RemapPipeNames** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | **FALSE**                                 |
| Maximum   | **TRUE**                                  |
| Default   | **FALSE**                                 |



 

## Remarks

If **RemapPipeNames** is set to **TRUE**, named pipes are always opened using local pipe names. For example, when a client opens "Pipe" on "\\\\NodeName" the client will actually open $$\\NodeName\\Pipe.

By default, **RemapPipeNames** is set to **FALSE**.

## Examples

The property value portion of a [property list](property-lists.md) entry for **RemapPipeNames** can be set with the following example code.


```C++
DWORD RemapPipeNameData            = TRUE;
CLUSPROP_DWORD RemapPipeNameValue;
RemapPipeNameValue.Syntax.dw       = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
RemapPipeNameValue.cbLength        = sizeof(DWORD);
RemapPipeNameValue.dw              = RemapPipeNameData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[Cluster Name Private Properties](network-name-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> </dl>

 

 





