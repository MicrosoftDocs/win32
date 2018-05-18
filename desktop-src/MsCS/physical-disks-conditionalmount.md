---
title: ConditionalMount
description: This property is not supported.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '847c4fd1-2de3-40eb-b0a0-cf5d26ba2ecf'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ConditionalMount Failover Cluster ,for physical disks", "ConditionalMount Failover Cluster"]
topic_type:
- apiref
api_name:
- ConditionalMount
api_type:
- NA
---

# ConditionalMount

\[The **ConditionalMount** property is no longer available for use as of Windows Server 2012. Instead, use the [**DiskRunChkDsk**](diskrunchkdsk.md) property.\]

This property is not supported.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | **FALSE** (0) always mount the disk       |
| Maximum   | **TRUE** (1) conditionally mount the disk |
| Default   | **TRUE**                                  |



 

## Remarks

Setting **ConditionalMount** to **FALSE** causes the operating system to attempt to mount the disk regardless of chkdsk failures, if any. With **ConditionalMount** set to **TRUE** (the default), the operating system will not attempt to mount a disk if chkdsk reports errors for the disk. Note that if chkdsk does not run, it will not produce errors, and therefore the operating system will attempt to mount the disk regardless of the **ConditionalMount** setting. The [**SkipChkdsk**](physical-disks-skipchkdsk.md) property determines if chkdsk runs or not.

The following table summarizes the interaction between [**SkipChkdsk**](physical-disks-skipchkdsk.md) and **ConditionalMount**.



| [**SkipChkdsk**](physical-disks-skipchkdsk.md) value | **ConditionalMount** value | Chkdsk runs? | Disk mounted?                                 |
|-------------------------------------------------------|----------------------------|--------------|-----------------------------------------------|
| **FALSE**                                             | **TRUE**                   | yes          | If chkdsk reports errors, no. Otherwise, yes. |
| **FALSE**                                             | **FALSE**                  | yes          | yes                                           |
| **TRUE**                                              | **TRUE**                   | no           | yes                                           |
| **TRUE**                                              | **FALSE**                  | no           | yes                                           |



 

Forcing a disk to mount despite errors can result in loss of data. Use caution when changing these properties.

## Examples

The property value portion of a [property list](property-lists.md) entry for **ConditionalMount** can be set with the following example code.


```C++
DWORD          ConditionalMountData = FALSE;
CLUSPROP_DWORD ConditionalMountValue;

ConditionalMountValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
ConditionalMountValue.cbLength  = sizeof(DWORD);
ConditionalMountValue.dw        = ConditionalMountData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[**SkipChkdsk**](physical-disks-skipchkdsk.md)
</dt> </dl>

 

 





