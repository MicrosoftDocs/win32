---
title: GetRecordCount method of the Win32\_ReliabilityStabilityMetrics class
description: Retrieves the number of records in the Win32\_ReliabilityStabilityMetrics class.
ms.assetid: 0328a232-db91-4914-885b-f555a675f9da
keywords:
- GetRecordCount method
- GetRecordCount method, Win32_ReliabilityStabilityMetrics class
- Win32_ReliabilityStabilityMetrics class, GetRecordCount method
topic_type:
- apiref
api_name:
- Win32_ReliabilityStabilityMetrics.GetRecordCount
api_location:
- RacWmiProv.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetRecordCount method of the Win32\_ReliabilityStabilityMetrics class

Retrieves the number of records in the [**Win32\_ReliabilityStabilityMetrics**](win32-reliabilitystabilitymetrics.md) class.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 GetRecordCount(
  [out] uint32 GetRecordCount
);
```



## Parameters

<dl> <dt>

*GetRecordCount* \[out\]
</dt> <dd>

Returns an unsigned integer value for the number of records in [**Win32\_ReliabilityStabilityMetrics**](win32-reliabilitystabilitymetrics.md) class. Example: "400".

</dd> </dl>

## Return value

Returns an HRESULT, where 0 (zero) indicates success. A nonzero return value indicates an error. If the number of records is inaccessible, the method returns **WBEM\_S\_NO\_MORE\_DATA** (0x40005). For more information about C++ and scripting error codes, see [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559) or [**WbemErrorEnum Constants**](https://msdn.microsoft.com/library/aa393978), respectively.

## Remarks

If the RacTask scheduled task is updating the records in [**Win32\_ReliabilityStabilityMetrics**](win32-reliabilitystabilitymetrics.md) class, the *RecordCount* parameter might not match the number of records after the update is finished. This method is not available on 64-bit versions of the Windows operating system.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>RacWmiProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RacWmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_ReliabilityStabilityMetrics**](win32-reliabilitystabilitymetrics.md)
</dt> </dl>

 

 





