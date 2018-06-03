---
title: AddStorageVolumes method of the MSFT\_SMStorageGroup class
description: Adds storage volumes to a storage group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8259ab39-31d3-43e9-9ef3-fca73f871306
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddStorageVolumes method
- AddStorageVolumes method, MSFT_SMStorageGroup class
- MSFT_SMStorageGroup class, AddStorageVolumes method
topic_type:
- apiref
api_name:
- MSFT_SMStorageGroup.AddStorageVolumes
api_location:
- StorageService.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddStorageVolumes method of the MSFT\_SMStorageGroup class

Adds storage volumes to a storage group.

## Syntax


```mof
Uint32 AddStorageVolumes(
  [in]            String                LUNames[],
  [in, optional]  String                DeviceNumbers[],
  [in]            Uint16                DeviceAccesses[],
  [in, optional]  String                username,
  [in, optional]  String                password,
  [out]           MSFT_SMJob        REF Job,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*LUNames* \[in\]
</dt> <dd>

An array of IDs of existing logical unit instances.

> [!Note]  
> IDs must match the **Name** property of LogicalDevice instances that represent SCSI logical units.

 

</dd> <dt>

*DeviceNumbers* \[in, optional\]
</dt> <dd>

The logical unit numbers to assign to the corresponding item in the *LUNames* parameter. If this parameter is **NULL**, all LU numbers are assigned by the hardware or instrumentation.

</dd> <dt>

*DeviceAccesses* \[in\]
</dt> <dd>

The permissions to assign to the corresponding logical unit in the *LUNames* parameter. Setting this to 'No Access' assigns the DeviceNumber for the associated initiators, but does not grant read or write access. If the *LUNames* parameter is not **NULL** then this parameter is required.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Read_Write"></span><span id="read_write"></span><span id="READ_WRITE"></span>

**Read Write** (2)


</dt> <dd></dd> <dt>

<span id="Read-Only"></span><span id="read-only"></span><span id="READ-ONLY"></span>

**Read-Only** (3)


</dt> <dd></dd> <dt>

<span id="No_Access"></span><span id="no_access"></span><span id="NO_ACCESS"></span>

**No Access** (4)


</dt> <dd></dd> </dl> </dd> <dt>

*username* \[in, optional\]
</dt> <dd>

Used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

Used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to the [**MSFT\_SMJob**](msft-smjob.md) instance. May be **NULL** if the job is completed.

**Windows Server 2012:** This parameter is not supported.

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

An [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object containing the results of calling this method.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Invalid logical unit ID** (4097)
</dt> <dt>

**Invalid permission** (4100)
</dt> <dt>

**Target/initiator combination already exposed** (4101)
</dt> <dt>

**Requested logical unit number in use** (4102)
</dt> <dt>

**Maximum Map Count Exceeded** (4103)
</dt> <dt>

**StorageService: Error LUNames Required** (40000)
</dt> <dt>

**StorageService: DeviceAccess Array Size not equal to LUNames Array Size** (40015)
</dt> <dt>

**StorageService: LU Not Found** (40020)
</dt> <dt>

**StorageService: Max Map Count for LU Exceeded** (40025)
</dt> <dt>

**StorageService: Client Should not specify DeviceNumbers for this Array** (40030)
</dt> <dt>

**StorageService: DeviceNumbers Array Size not equal to LUNames Array Size** (40035)
</dt> <dt>

**StorageService: DeviceNumbers Array contains invalid numbers - Acceptable range is 0-254** (40036)
</dt> <dt>

**StorageService: Unable to get MaskingGroup from job** (40061)
</dt> <dt>

**StorageService: Provider does not support masking and mapping operations** (40107)
</dt> <dt>

**StorageService: More than one MaskingGroup of the same type are associated with the SPC on the Provider** (40111)
</dt> <dt>

**StorageService: Unable to Find the StorageVolume Object(s) on the provider** (40117)
</dt> <dt>

**StorageService: Method invocation failed** (40300)
</dt> <dt>

**StorageService: Error: Provider job completed with errors** (41000)
</dt> <dt>

**StorageService CIM Error: Failed** (43001)
</dt> <dt>

**StorageService CIM Error: Access denied** (43002)
</dt> <dt>

**StorageService CIM Error: Invalid namespace** (43003)
</dt> <dt>

**StorageService CIM Error: Invalid parameter** (43004)
</dt> <dt>

**StorageService CIM Error: Invalid class** (43005)
</dt> <dt>

**StorageService CIM Error: Not found** (43006)
</dt> <dt>

**StorageService CIM Error: Not supported** (43007)
</dt> <dt>

**StorageService CIM Error: Class has children** (43008)
</dt> <dt>

**StorageService CIM Error: Class has instances** (43009)
</dt> <dt>

**StorageService CIM Error: Invalid superclass** (43010)
</dt> <dt>

**StorageService CIM Error: Already exists** (43011)
</dt> <dt>

**StorageService CIM Error: No such property** (43012)
</dt> <dt>

**StorageService CIM Error: Type mismatch** (43013)
</dt> <dt>

**StorageService CIM Error: Query language not supported** (43014)
</dt> <dt>

**StorageService CIM Error: Invalid query** (43015)
</dt> <dt>

**StorageService CIM Error: Method not available** (43016)
</dt> <dt>

**StorageService CIM Error: Method not found** (43017)
</dt> <dt>

**StorageService CIM Error: Unexpected response** (43018)
</dt> <dt>

**StorageService CIM Error: Invalid response destination** (43019)
</dt> <dt>

**StorageService CIM Error: Namespace not empty** (43020)
</dt> <dt>

**StorageService CIM Error: Invalid enumeration context** (43021)
</dt> <dt>

**StorageService CIM Error: Invalid operation timeout** (43022)
</dt> <dt>

**StorageService CIM Error: Pull has been abandoned** (43023)
</dt> <dt>

**StorageService CIM Error: Pull cannot be abandoned** (43024)
</dt> <dt>

**StorageService CIM Error: Filtered enumeration not supported** (43025)
</dt> <dt>

**StorageService CIM Error: Continuation on error not supported** (43026)
</dt> <dt>

**StorageService CIM Error: Server limits exceeded** (43027)
</dt> <dt>

**StorageService CIM Error: Server is shutting down** (43028)
</dt> <dt>

**StorageService CIM Error: Query feature not supported** (43029)
</dt> <dt>

**StorageService: Generic Failure** (51000)
</dt> <dt>

**StorageService: Invalid connection credentials** (51005)
</dt> <dt>

**StorageService: SSL connection failure** (51010)
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

[**MSFT\_SMStorageGroup**](msft-smstoragegroup.md)
</dt> </dl>

 

 





