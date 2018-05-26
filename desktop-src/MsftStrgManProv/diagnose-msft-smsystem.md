---
title: Diagnose method of the MSFT\_SMSystem class
description: Attempts to find more information about the health state of an array.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f2c5b7b4-fbd3-4b62-a1de-be2cde58a825
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Diagnose method
- Diagnose method, MSFT_SMSystem class
- MSFT_SMSystem class, Diagnose method
topic_type:
- apiref
api_name:
- MSFT_SMSystem.Diagnose
api_location:
- StorageService.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Diagnose method of the MSFT\_SMSystem class

Attempts to find more information about the health state of an array.

## Syntax


```mof
UInt32 Diagnose(
  [out]          String                       reason,
  [in, optional] String                       username,
  [in, optional] String                       password,
  [out]          MSFT_SMStorageDiagnoseResult DiagnoseResults[],
  [out]          MSFT_SMExtendedStatus        ExtendedStatus
);
```



## Parameters

<dl> <dt>

*reason* \[out\]
</dt> <dd>

This parameter is no longer available.

**Windows Server 2012 R2 and Windows Server 2012:** A description of the reason for the diagnosis. This parameter was removed in Windows Server 2016.

</dd> <dt>

*username* \[in, optional\]
</dt> <dd>

Used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

Used to authenticate with the SMI-S provider. If not provided, the storage service attempts to obtain these credentials from the configuration provider.

</dd> <dt>

*DiagnoseResults* \[out\]
</dt> <dd>

An [**MSFT\_SMStorageDiagnoseResult**](msft-smstoragediagnoseresult.md) object that contains the results from calling this method.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is not available before Windows Server 2016.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

An [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object that contains an error code or additional information about the result returned in the *DiagnoseResults* parameter.

</dd> </dl>

## Return value

The possible return values are:

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

**StorageService: Method invocation failed** (40300)
</dt> <dt>

**StorageService: Unable to find cause for health status** (42000)
</dt> <dt>

**StorageService: Unable to get CIM\_ComputerSystem for search** (40301)
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

[**MSFT\_SMSystem**](msft-smsystem.md)
</dt> </dl>

 

 





