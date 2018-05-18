---
title: GetRecordCount method of the Win32\_ReliabilityRecords class
description: Retrieves the number of records in the Win32\_ReliabilityRecords class.
ms.assetid: 'a2d0701e-741f-4baf-aafd-5b6d49ce85d5'
keywords: ["GetRecordCount method", "GetRecordCount method, Win32_ReliabilityRecords class", "Win32_ReliabilityRecords class, GetRecordCount method"]
topic_type:
- apiref
api_name:
- Win32_ReliabilityRecords.GetRecordCount
api_location:
- RacWmiProv.dll
api_type:
- COM
---

# GetRecordCount method of the Win32\_ReliabilityRecords class

Retrieves the number of records in the [**Win32\_ReliabilityRecords**](win32-reliabilityrecords.md) class.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 GetRecordCount(
  [out] uint32 RecordCount
);
```



## Parameters

<dl> <dt>

*RecordCount* \[out\]
</dt> <dd>

Returns an unsigned integer value for the number of records in [**Win32\_ReliabilityRecords**](win32-reliabilityrecords.md) class.

</dd> </dl>

## Return value

Returns an HRESULT, where 0 (zero) indicates success. A nonzero return value indicates an error. If the number of records is inaccessible, the method returns **WBEM\_S\_NO\_MORE\_DATA** (0x40005). For more information about C++ and scripting error codes, see [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559) or [**WbemErrorEnum Constants**](https://msdn.microsoft.com/library/aa393978), respectively.

## Remarks

If the RacTask scheduled task is updating the records in [**Win32\_ReliabilityRecords**](win32-reliabilityrecords.md) class, the *RecordCount* parameter might not match the number of records after the update is finished. This method is not available on 64-bit versions of the Windows operating system.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>RacWmiProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RacWmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_ReliabilityRecords**](win32-reliabilityrecords.md)
</dt> </dl>

 

 





