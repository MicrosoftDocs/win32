---
title: CreateSnapshot method of the MSFT\_SMStorageVolume class
description: Starts a job to create an associated un-synced snapshot of the MSFT\_SMStorageVolume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 590be8be-769b-46f5-96c9-436457d09a03
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateSnapshot method
- CreateSnapshot method, MSFT_SMStorageVolume class
- MSFT_SMStorageVolume class, CreateSnapshot method
topic_type:
- apiref
api_name:
- MSFT_SMStorageVolume.CreateSnapshot
api_location:
- StorageService.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateSnapshot method of the MSFT\_SMStorageVolume class

Starts a job to create an associated un-synced snapshot of the [**MSFT\_SMStorageVolume**](msft-smstoragevolume.md).

## Syntax


```mof
uint32 CreateSnapshot(
  [in, optional]  string                   ElementName,
  [out, optional] MSFT_SMStorageVolume REF TargetStorageVolume,
  [in, optional]  MSFT_SMPool          REF TargetPool,
  [in, optional]  String                   username,
  [in, optional]  String                   password,
  [out]           MSFT_SMJob           REF Job,
  [out, optional] MSFT_SMExtendedStatus    ExtendedStatus
);
```



## Parameters

<dl> <dt>

*ElementName* \[in, optional\]
</dt> <dd>

End-user relevant name for the element being created. If **NULL**, then a system supplied name is used.

</dd> <dt>

*TargetStorageVolume* \[out, optional\]
</dt> <dd>

A reference to the created target storage element, that is the replica. If a job is created, the target element may not be available immediately.

</dd> <dt>

*TargetPool* \[in, optional\]
</dt> <dd>

The underlying storage for the target element (the replica) will be drawn from TargetPool if specified, otherwise the allocation is implementation specific.

</dd> <dt>

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

Reference to the [**MSFT\_SMJob**](msft-smjob.md) instance. May be **NULL** if the job is completed.

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

An [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object containing the results of calling this method.

</dd> </dl>

## Return value

<dl> <dt>

**Success**
</dt> <dd>

0

</dd> <dt>

**Not Supported**
</dt> <dd>

1

</dd> <dt>

**Unspecified Error**
</dt> <dd>

2

</dd> <dt>

**Timeout**
</dt> <dd>

3

</dd> <dt>

**Failed**
</dt> <dd>

4

</dd> <dt>

**Invalid Parameter**
</dt> <dd>

5

</dd> <dt>

**Method Parameters Checked - Job Started**
</dt> <dd>

4096

</dd> <dt>

**StorageService: Method invocation failed**
</dt> <dd>

40300

</dd> <dt>

**StorageService: Cannot modify volume instance**
</dt> <dd>

40304

</dd> <dt>

**StorageService: Snapshot capability not supported**
</dt> <dd>

40308

</dd> <dt>

**StorageService: Replication type not supported per reported capabilities**
</dt> <dd>

40500

</dd> <dt>

**StorageService CIM Error: Failed**
</dt> <dd>

43001

</dd> <dt>

**StorageService CIM Error: Access denied**
</dt> <dd>

43002

</dd> <dt>

**StorageService CIM Error: Invalid namespace**
</dt> <dd>

43003

</dd> <dt>

**StorageService CIM Error: Invalid parameter**
</dt> <dd>

43004

</dd> <dt>

**StorageService CIM Error: Invalid class**
</dt> <dd>

43005

</dd> <dt>

**StorageService CIM Error: Not found**
</dt> <dd>

43006

</dd> <dt>

**StorageService CIM Error: Not supported**
</dt> <dd>

43007

</dd> <dt>

**StorageService CIM Error: Class has children**
</dt> <dd>

43008

</dd> <dt>

**StorageService CIM Error: Class has instances**
</dt> <dd>

43009

</dd> <dt>

**StorageService CIM Error: Invalid superclass**
</dt> <dd>

43010

</dd> <dt>

**StorageService CIM Error: Already exists**
</dt> <dd>

43011

</dd> <dt>

**StorageService CIM Error: No such propert**
</dt> <dd>

43012

</dd> <dt>

**StorageService CIM Error: Type mismatch**
</dt> <dd>

43013

</dd> <dt>

**StorageService CIM Error: Query language not supported**
</dt> <dd>

43014

</dd> <dt>

**StorageService CIM Error: Invalid query**
</dt> <dd>

43015

</dd> <dt>

**StorageService CIM Error: Method not available**
</dt> <dd>

43016

</dd> <dt>

**StorageService CIM Error: Method not found**
</dt> <dd>

43017

</dd> <dt>

**StorageService CIM Error: Unexpected response**
</dt> <dd>

43018

</dd> <dt>

**StorageService CIM Error: Invalid response destination**
</dt> <dd>

43019

</dd> <dt>

**StorageService CIM Error: Namespace not empty**
</dt> <dd>

43020

</dd> <dt>

**StorageService CIM Error: No such property**
</dt> <dd>

43012

</dd> <dt>

**StorageService CIM Error: Invalid enumeration context**
</dt> <dd>

43021

**Windows Server 2012 R2:** Unavailable for Windows Server 2012.

</dd> <dt>

**StorageService CIM Error: Invalid operation timeout**
</dt> <dd>

43022

</dd> <dt>

**StorageService CIM Error: Pull has been abandoned**
</dt> <dd>

43023

</dd> <dt>

**StorageService CIM Error: Pull cannot be abandoned**
</dt> <dd>

43024

</dd> <dt>

**StorageService CIM Error: Filtered enumeration not supported**
</dt> <dd>

43025

</dd> <dt>

**StorageService CIM Error: Continuation on error not supported**
</dt> <dd>

43026

</dd> <dt>

**StorageService CIM Error: Server limits exceeded**
</dt> <dd>

43027

</dd> <dt>

**StorageService CIM Error: Server is shutting down**
</dt> <dd>

43028

</dd> <dt>

**StorageService CIM Error: Query feature not supported**
</dt> <dd>

43029

</dd> <dt>

**StorageService: Generic Failure**
</dt> <dd>

51000

</dd> <dt>

**StorageService: Invalid connection credentials**
</dt> <dd>

51005

</dd> <dt>

**StorageService: SSL connection failure**
</dt> <dd>

51010

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| Header<br/>                   | <dl> <dt>Dbdaoint.h</dt> </dl>         |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMStorageVolume**](msft-smstoragevolume.md)
</dt> </dl>

 

 





