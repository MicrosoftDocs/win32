---
title: CreatePool method of the MSFT\_SMSystem class
description: Creates a concrete pool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c47b3165-8c54-47b3-b95e-59c9c1455785
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreatePool method
- CreatePool method, MSFT_SMSystem class
- MSFT_SMSystem class, CreatePool method
topic_type:
- apiref
api_name:
- MSFT_SMSystem.CreatePool
api_location:
- StorageService.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreatePool method of the MSFT\_SMSystem class

Creates a concrete pool.

## Syntax


```mof
Uint32 CreatePool(
  [in]            String                ElementName,
  [in]            String                DiskDriveObjectIds[],
  [in]            String                PoolSettingObjectId,
  [in, optional]  Boolean               ThinlyProvisioned,
  [in]            UInt16                Usage,
  [in]            String                OtherUsageDescription,
  [out]           MSFT_SMJob        REF Job,
  [out]           MSFT_SMPool       REF Pool,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus,
  [in, optional]  String                username,
  [in, optional]  String                password
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

Display name to assign to the pool

</dd> <dt>

*DiskDriveObjectIds* \[in\]
</dt> <dd>

The ObjectIds of the disk drives to use for the pool.

</dd> <dt>

*PoolSettingObjectId* \[in\]
</dt> <dd>

The ObjectId of a pool setting the defines the service level that the storage pool is expected to provide. If **NULL** the storage service will try to locate a default setting.

</dd> <dt>

*ThinlyProvisioned* \[in, optional\]
</dt> <dd>

If **True**, the created pool is thinly provisioned.

</dd> <dt>

*Usage* \[in\]
</dt> <dd>

The usage of the storage pool.

The possible values are.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unrestricted"></span><span id="unrestricted"></span><span id="UNRESTRICTED"></span>

**Unrestricted** (2)


</dt> <dd></dd> <dt>

<span id="Reserved_for_ComputerSystem__the_block_server_"></span><span id="reserved_for_computersystem__the_block_server_"></span><span id="RESERVED_FOR_COMPUTERSYSTEM__THE_BLOCK_SERVER_"></span>

**Reserved for ComputerSystem (the block server)** (3)


</dt> <dd></dd> <dt>

<span id="Reserved_as_a_Delta_Replica_Container"></span><span id="reserved_as_a_delta_replica_container"></span><span id="RESERVED_AS_A_DELTA_REPLICA_CONTAINER"></span>

**Reserved as a Delta Replica Container** (4)


</dt> <dd></dd> <dt>

<span id="Reserved_for_Migration_Services"></span><span id="reserved_for_migration_services"></span><span id="RESERVED_FOR_MIGRATION_SERVICES"></span>

**Reserved for Migration Services** (5)


</dt> <dd></dd> <dt>

<span id="Reserved_for_Local_Replication_Services"></span><span id="reserved_for_local_replication_services"></span><span id="RESERVED_FOR_LOCAL_REPLICATION_SERVICES"></span>

**Reserved for Local Replication Services** (6)


</dt> <dd></dd> <dt>

<span id="Reserved_for_Remote_Replication_Services"></span><span id="reserved_for_remote_replication_services"></span><span id="RESERVED_FOR_REMOTE_REPLICATION_SERVICES"></span>

**Reserved for Remote Replication Services** (7)


</dt> <dd></dd> <dt>

<span id="Reserved_for_Sparing"></span><span id="reserved_for_sparing"></span><span id="RESERVED_FOR_SPARING"></span>

**Reserved for Sparing** (8)


</dt> <dd></dd> </dl> </dd> <dt>

*OtherUsageDescription* \[in\]
</dt> <dd>

Text description of the usage when the *Usage* parameter is **Other**.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the [**MSFT\_SMJob**](msft-smjob.md) instance. May be **NULL** if the job is completed.

</dd> <dt>

*Pool* \[out\]
</dt> <dd>

Reference to the created [**MSFT\_SMPool**](msft-smpool.md) instance.

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

An [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object containing the results of calling this method.

</dd> <dt>

*username* \[in, optional\]
</dt> <dd>

Used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

Used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> </dl>

## Return value

<dl> <dt>

**Job Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**In Use** (6)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**StorageService: Method invocation failed** (40300)
</dt> <dt>

**StorageService: Cannot modify Pool instance to set ElementName** (40304)
</dt> <dt>

**StorageService: Failed to create storage settings on provider** (40602)
</dt> <dt>

**StorageService: Failed to modify storage settings on provider** (40603)
</dt> <dt>

**StorageService: Concrete Pool creation is not supported by the provider** (40800)
</dt> <dt>

**StorageService: Concrete Pool creation using DiskDrives or StorageExtents is not supported** (40801)
</dt> <dt>

**StorageService: DiskDrives specified are already in use by one or more Concrete Pools** (40802)
</dt> <dt>

**StorageService: DiskDrives specified are part of multiple primoridal pools** (40803)
</dt> <dt>

**StorageService: No StorageExtents were found based on the specified DiskDrives** (40804)
</dt> <dt>

**StorageService: Unable to get StorageExtents from DiskDrives** (40805)
</dt> <dt>

**StorageService: Invalid Pool Setting ObjectId was specified** (40806)
</dt> <dt>

**StorageService: PoolSetting and DiskDrives specified do not belong to the same Primordial Pool** (40807)
</dt> <dt>

**StorageService: Cannot create Concrete Pool using DiskDrive(s) reserved for hot spare** (40812)
</dt> <dt>

**StorageService: Provider does not support ThinlyProvisioned StoragePools** (40816)
</dt> <dt>

**StorageService: Unable to find StorageCapabilities on provider** (40817)
</dt> <dt>

**StorageService: Unable to identify default StorageSettings on provider** (40818)
</dt> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMSystem**](msft-smsystem.md)
</dt> </dl>

 

 





