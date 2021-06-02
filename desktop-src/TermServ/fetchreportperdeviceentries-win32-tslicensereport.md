---
title: FetchReportPerDeviceEntries method of the Win32_TSLicenseReport class
description: Retrieves information of issued Remote Desktop Services Per Device client access licenses (RDS \ 160;Per Device CALs) from the report.
ms.assetid: 3f632a65-d6e0-4efd-9498-d04a05f9ddec
ms.tgt_platform: multiple
keywords:
- FetchReportPerDeviceEntries method Remote Desktop Services
- FetchReportPerDeviceEntries method Remote Desktop Services , Win32_TSLicenseReport class
- Win32_TSLicenseReport class Remote Desktop Services , FetchReportPerDeviceEntries method
topic_type:
- apiref
api_name:
- Win32_TSLicenseReport.FetchReportPerDeviceEntries
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# FetchReportPerDeviceEntries method of the Win32\_TSLicenseReport class

Retrieves information of issued Remote Desktop Services Per Device client access licenses (RDS Per Device CALs) from the report.

## Syntax


```mof
uint32 FetchReportPerDeviceEntries(
  [in]      uint32                              StartIndex,
  [in, out] uint32                              Count,
  [out]     Win32_TSLicenseReportPerDeviceEntry ReportPerDeviceEntries[]
);
```



## Parameters

<dl> <dt>

*StartIndex* \[in\]
</dt> <dd>

The index of the first report entry to be retrieved. The first report entry has an index of zero.

</dd> <dt>

*Count* \[in, out\]
</dt> <dd>

The number of report entries to retrieve from the report object. A value of zero indicates that all of the report entries starting at *StartIndex* are to be retrieved. On return, contains the number of entries in the *ReportPerDeviceEntries* array.

</dd> <dt>

*ReportPerDeviceEntries* \[out\]
</dt> <dd>

An array of [**Win32\_TSLicenseReportPerDeviceEntry**](win32-tslicensereportperdeviceentry.md) classes the represent the license entries retrieved. The *Count* parameter contains the number of elements in this array.

</dd> </dl>

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>TlsWmiProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TlsWmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSLicenseReport**](win32-tslicensereport.md)
</dt> </dl>

 

 





