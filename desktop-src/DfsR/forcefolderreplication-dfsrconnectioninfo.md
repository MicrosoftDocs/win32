---
title: ForceFolderReplication method of the DfsrConnectionInfo class
description: Controls replication by forcing a designated folder to replicate. After the duration expires, the DFS Replication service will revert to the configured replication schedule.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ed2c8660-c405-41e0-a9b6-5a44ba8ee6f8
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ForceFolderReplication method Distributed File System Replication
- ForceFolderReplication method Distributed File System Replication , DfsrConnectionInfo class
- DfsrConnectionInfo class Distributed File System Replication , ForceFolderReplication method
topic_type:
- apiref
api_name:
- DfsrConnectionInfo.ForceFolderReplication
api_location:
- DfsRWmiV2.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ForceFolderReplication method of the DfsrConnectionInfo class

Controls replication by forcing a designated folder to replicate. After the duration expires, the DFS Replication service will revert to the configured replication schedule.

## Syntax


```mof
uint32 ForceFolderReplication(
  [in] uint32 DurationInMin,
  [in] uint32 Bandwidth,
  [in] string ReplicatedFolderGuid
);
```



## Parameters

<dl> <dt>

*DurationInMin* \[in\]
</dt> <dd>

The duration, in minutes. This value cannot exceed one week (10,080 minutes).

</dd> <dt>

*Bandwidth* \[in\]
</dt> <dd>

The valid bandwidth level. This parameter can be one of the following values.

<dt>

<span id="BANDWIDTH_LEVEL_OFF"></span><span id="bandwidth_level_off"></span>

<span id="BANDWIDTH_LEVEL_OFF"></span><span id="bandwidth_level_off"></span>**BANDWIDTH\_LEVEL\_OFF** (0x0)


</dt> <dd>

No replication.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_16_KBPS"></span><span id="bandwidth_level_16_kbps"></span>

<span id="BANDWIDTH_LEVEL_16_KBPS"></span><span id="bandwidth_level_16_kbps"></span>**BANDWIDTH\_LEVEL\_16\_KBPS** (0x1)


</dt> <dd>

16 kilobits per second (Kbps).

</dd> <dt>

<span id="BANDWIDTH_LEVEL_64_KBPS"></span><span id="bandwidth_level_64_kbps"></span>

<span id="BANDWIDTH_LEVEL_64_KBPS"></span><span id="bandwidth_level_64_kbps"></span>**BANDWIDTH\_LEVEL\_64\_KBPS** (0x2)


</dt> <dd>

64 Kbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_128_KBPS"></span><span id="bandwidth_level_128_kbps"></span>

<span id="BANDWIDTH_LEVEL_128_KBPS"></span><span id="bandwidth_level_128_kbps"></span>**BANDWIDTH\_LEVEL\_128\_KBPS** (0x3)


</dt> <dd>

128 Kbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_256_KBPS"></span><span id="bandwidth_level_256_kbps"></span>

<span id="BANDWIDTH_LEVEL_256_KBPS"></span><span id="bandwidth_level_256_kbps"></span>**BANDWIDTH\_LEVEL\_256\_KBPS** (0x4)


</dt> <dd>

256 Kbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_512_KBPS"></span><span id="bandwidth_level_512_kbps"></span>

<span id="BANDWIDTH_LEVEL_512_KBPS"></span><span id="bandwidth_level_512_kbps"></span>**BANDWIDTH\_LEVEL\_512\_KBPS** (0x5)


</dt> <dd>

512 Kbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_1_MBPS"></span><span id="bandwidth_level_1_mbps"></span>

<span id="BANDWIDTH_LEVEL_1_MBPS"></span><span id="bandwidth_level_1_mbps"></span>**BANDWIDTH\_LEVEL\_1\_MBPS** (0x6)


</dt> <dd>

1 Mbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_2_MBPS"></span><span id="bandwidth_level_2_mbps"></span>

<span id="BANDWIDTH_LEVEL_2_MBPS"></span><span id="bandwidth_level_2_mbps"></span>**BANDWIDTH\_LEVEL\_2\_MBPS** (0x7)


</dt> <dd>

2 Mbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_4_MBPS"></span><span id="bandwidth_level_4_mbps"></span>

<span id="BANDWIDTH_LEVEL_4_MBPS"></span><span id="bandwidth_level_4_mbps"></span>**BANDWIDTH\_LEVEL\_4\_MBPS** (0x8)


</dt> <dd>

4 Mbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_8_MBPS"></span><span id="bandwidth_level_8_mbps"></span>

<span id="BANDWIDTH_LEVEL_8_MBPS"></span><span id="bandwidth_level_8_mbps"></span>**BANDWIDTH\_LEVEL\_8\_MBPS** (0x9)


</dt> <dd>

8 Mbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_16_MBPS"></span><span id="bandwidth_level_16_mbps"></span>

<span id="BANDWIDTH_LEVEL_16_MBPS"></span><span id="bandwidth_level_16_mbps"></span>**BANDWIDTH\_LEVEL\_16\_MBPS** (0xA)


</dt> <dd>

16 Mbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_32_MBPS"></span><span id="bandwidth_level_32_mbps"></span>

<span id="BANDWIDTH_LEVEL_32_MBPS"></span><span id="bandwidth_level_32_mbps"></span>**BANDWIDTH\_LEVEL\_32\_MBPS** (0xB)


</dt> <dd>

32 Mbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_64_MBPS"></span><span id="bandwidth_level_64_mbps"></span>

<span id="BANDWIDTH_LEVEL_64_MBPS"></span><span id="bandwidth_level_64_mbps"></span>**BANDWIDTH\_LEVEL\_64\_MBPS** (0xC)


</dt> <dd>

64 Mbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_128_MBPS"></span><span id="bandwidth_level_128_mbps"></span>

<span id="BANDWIDTH_LEVEL_128_MBPS"></span><span id="bandwidth_level_128_mbps"></span>**BANDWIDTH\_LEVEL\_128\_MBPS** (0xD)


</dt> <dd>

128 Mbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_256_MBPS"></span><span id="bandwidth_level_256_mbps"></span>

<span id="BANDWIDTH_LEVEL_256_MBPS"></span><span id="bandwidth_level_256_mbps"></span>**BANDWIDTH\_LEVEL\_256\_MBPS** (0xE)


</dt> <dd>

256 Mbps.

</dd> <dt>

<span id="BANDWIDTH_LEVEL_INFINITE"></span><span id="bandwidth_level_infinite"></span>

<span id="BANDWIDTH_LEVEL_INFINITE"></span><span id="bandwidth_level_infinite"></span>**BANDWIDTH\_LEVEL\_INFINITE** (0xF)


</dt> <dd>

Full bandwidth (no throttling.)

</dd> </dl> </dd> <dt>

*ReplicatedFolderGuid* \[in\]
</dt> <dd>

The unique identifier of the replicated folder to force replication on.

</dd> </dl>

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| End of client support<br/>    | Windows Vista<br/>                                                                 |
| Namespace<br/>                | Root\\MicrosoftDfs<br/>                                                            |
| MOF<br/>                      | <dl> <dt>DfsRProvs.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**DfsrConnectionInfo**](dfsrconnectioninfo.md)
</dt> </dl>

 

 





