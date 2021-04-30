---
title: FetchReportFailedPerUserSummaryEntries method of the Win32_TSLicenseReport class
description: Retrieves summary information of failed Remote Desktop Services Per User client access licenses (RDS \ 160;Per User CALs) from the report.
ms.assetid: dc9c4a36-b2a8-407e-b902-ee9d51227909
ms.tgt_platform: multiple
keywords:
- FetchReportFailedPerUserSummaryEntries method Remote Desktop Services
- FetchReportFailedPerUserSummaryEntries method Remote Desktop Services , Win32_TSLicenseReport class
- Win32_TSLicenseReport class Remote Desktop Services , FetchReportFailedPerUserSummaryEntries method
topic_type:
- apiref
api_name:
- Win32_TSLicenseReport.FetchReportFailedPerUserSummaryEntries
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# FetchReportFailedPerUserSummaryEntries method of the Win32\_TSLicenseReport class

Retrieves summary information of failed Remote Desktop Services Per User client access licenses (RDS Per User CALs) from the report.

## Syntax


```mof
uint32 FetchReportFailedPerUserSummaryEntries(
  [in]      uint32                                         StartIndex,
  [in, out] uint32                                         Count,
  [out]     Win32_TSLicenseReportFailedPerUserSummaryEntry ReportFailedPerUserSummaryEntries[]
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

The number of report entries to retrieve from the report object. A value of zero indicates that all of the report entries starting at *StartIndex* are to be retrieved. On return, contains the number of entries in the *ReportFailedPerUserSummaryEntries* array.

</dd> <dt>

*ReportFailedPerUserSummaryEntries* \[out\]
</dt> <dd>

An array of [**Win32\_TSLicenseReportFailedPerUserSummaryEntry**](win32-tslicensereportfailedperusersummaryentry.md) classes that represent the license entries retrieved. The *Count* parameter contains the number of elements in this array.

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

 

 





