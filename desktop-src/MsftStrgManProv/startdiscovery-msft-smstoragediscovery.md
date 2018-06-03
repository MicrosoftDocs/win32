---
title: StartDiscovery method of the MSFT\_SMStorageDiscovery class
description: Starts the Microsoft storage service discovery process.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2ba1d32a-6dab-48c7-b833-e4d078512286
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- StartDiscovery method
- StartDiscovery method, MSFT_SMStorageDiscovery class
- MSFT_SMStorageDiscovery class, StartDiscovery method
topic_type:
- apiref
api_name:
- MSFT_SMStorageDiscovery.StartDiscovery
api_location:
- StorageService.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StartDiscovery method of the MSFT\_SMStorageDiscovery class

Starts the Microsoft storage service discovery process.

## Syntax


```mof
Uint32 StartDiscovery(
  [in]            String                host,
  [in, optional]  String                hostType,
  [in]            Boolean               forceRediscovery = false,
  [in]            Uint32                discoveryLevel,
  [in]            String                interopNamespace,
  [in]            String                username,
  [in]            String                password,
  [out]           MSFT_SMJob        REF Job,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*host* \[in\]
</dt> <dd>

The host to discover.

</dd> <dt>

*hostType* \[in, optional\]
</dt> <dd>

The type of the host to discover.

The possible values are.

<dt>

<span id="host-resource"></span><span id="HOST-RESOURCE"></span>

**host-resource** ("host-resource")


</dt> <dd></dd> <dt>

<span id="smis-wmi"></span><span id="SMIS-WMI"></span>

**smis-wmi** ("smis-wmi")


</dt> <dd></dd> <dt>

<span id="smis-cimxml"></span><span id="SMIS-CIMXML"></span>

**smis-cimxml** ("smis-cimxml")


</dt> <dd></dd> </dl> </dd> <dt>

*forceRediscovery* \[in\]
</dt> <dd>

**True** to force the storage service to re-discover the host, even when the information about the host is already in the cache; otherwise, **False**.

</dd> <dt>

*discoveryLevel* \[in\]
</dt> <dd>

Indicates the level of discovery to perform.

The possible values are.

<dt>

<span id="Top-Level"></span><span id="top-level"></span><span id="TOP-LEVEL"></span>

**Top-Level** (0)


</dt> <dd></dd> <dt>

<span id="Mid-Level"></span><span id="mid-level"></span><span id="MID-LEVEL"></span>

**Mid-Level** (1)


</dt> <dd></dd> <dt>

<span id="AllExceptDiskDrives"></span><span id="allexceptdiskdrives"></span><span id="ALLEXCEPTDISKDRIVES"></span>

**AllExceptDiskDrives** (2)


</dt> <dd></dd> <dt>

<span id="All"></span><span id="all"></span><span id="ALL"></span>

**All** (3)


</dt> <dd></dd> </dl> </dd> <dt>

*interopNamespace* \[in\]
</dt> <dd>

The interoperation namespace used for the discovery process.

</dd> <dt>

*username* \[in\]
</dt> <dd>

The username used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*password* \[in\]
</dt> <dd>

The password used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to the [**MSFT\_SMJob**](msft-smjob.md) instance. May be **NULL** if the job is completed.

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

An [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object that contains the results of calling this method.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Failed** (1)
</dt> <dt>

**Job started** (4096)
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

[**MSFT\_SMStorageDiscovery**](msft-smstoragediscovery.md)
</dt> </dl>

 

 





