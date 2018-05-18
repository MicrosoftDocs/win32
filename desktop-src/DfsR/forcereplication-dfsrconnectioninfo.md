---
title: ForceReplication method of the DfsrConnectionInfo class
description: Controls replication by either forcing or suspending replication. DFSR will revert to the normal schedule at the end of the specified duration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2ba1bae4-2a9d-495c-b7ba-7e44f4cfa301'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-replication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ForceReplication method Distributed File System Replication", "ForceReplication method Distributed File System Replication , DfsrConnectionInfo class", "DfsrConnectionInfo class Distributed File System Replication , ForceReplication method"]
topic_type:
- apiref
api_name:
- DfsrConnectionInfo.ForceReplication
api_location:
- DfsRWmiV2.dll
api_type:
- COM
---

# ForceReplication method of the DfsrConnectionInfo class

Controls replication by either forcing or suspending replication. DFSR will revert to the normal schedule at the end of the specified duration.

## Syntax


```mof
uint32 ForceReplication(
  [in] uint32 Mode,
  [in] uint32 DurationInMin,
  [in] uint32 Bandwidth
);
```



## Parameters

<dl> <dt>

*Mode* \[in\]
</dt> <dd>

The replication mode. This parameter can be one of the following values.

<dt>

<span id="Obey_Configured_Schedule"></span><span id="obey_configured_schedule"></span><span id="OBEY_CONFIGURED_SCHEDULE"></span>

<span id="Obey_Configured_Schedule"></span><span id="obey_configured_schedule"></span><span id="OBEY_CONFIGURED_SCHEDULE"></span>**Obey Configured Schedule** (1)


</dt> <dd>

Use the configured schedule.

</dd> <dt>

<span id="Sync_Now"></span><span id="sync_now"></span><span id="SYNC_NOW"></span>

<span id="Sync_Now"></span><span id="sync_now"></span><span id="SYNC_NOW"></span>**Sync Now** (2)


</dt> <dd>

Ignore the configured schedule and replicate now for the specified duration.

</dd> <dt>

<span id="Stop_Sync"></span><span id="stop_sync"></span><span id="STOP_SYNC"></span>

<span id="Stop_Sync"></span><span id="stop_sync"></span><span id="STOP_SYNC"></span>**Stop Sync** (3)


</dt> <dd>

Ignore the configured schedule and stop replication for the specified duration.

</dd> <dt>

<span id="Sync_Until_In-Sync"></span><span id="sync_until_in-sync"></span><span id="SYNC_UNTIL_IN-SYNC"></span>

<span id="Sync_Until_In-Sync"></span><span id="sync_until_in-sync"></span><span id="SYNC_UNTIL_IN-SYNC"></span>**Sync Until In-Sync** (4)


</dt> <dd>

Ignore the configured schedule until this member is fully synchronized with its upstream partner.

</dd> </dl> </dd> <dt>

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

</dd> </dl> </dd> </dl>

## Return value

This method returns one of the [MONITOR\_STATUS return codes](monitor-status-return-codes.md) or one of the [system error codes](https://msdn.microsoft.com/library/windows/desktop/ms681381).

## Remarks

This method is meaningful only for inbound connections. It always fails with an error on outbound connections.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| End of client support<br/>    | Windows Vista<br/>                                                                 |
| Namespace<br/>                | Root\\MicrosoftDfs<br/>                                                            |
| MOF<br/>                      | <dl> <dt>DfsRProvs.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsRWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**DfsrConnectionInfo**](dfsrconnectioninfo.md)
</dt> </dl>

 

 





