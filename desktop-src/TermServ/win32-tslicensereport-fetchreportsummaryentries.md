---
title: FetchReportSummaryEntries method of the Win32_TSLicenseReport class
description: Retrieves summaries of Remote Desktop Services Per User client access licenses (RDS \ 160;Per User CALs) from the report.
ms.assetid: 0312B787-83E9-42FC-B21B-904B804C5C94
ms.tgt_platform: multiple
keywords:
- FetchReportSummaryEntries method Remote Desktop Services
- FetchReportSummaryEntries method Remote Desktop Services , Win32_TSLicenseReport class
- Win32_TSLicenseReport class Remote Desktop Services , FetchReportSummaryEntries method
topic_type:
- apiref
api_name:
- Win32_TSLicenseReport.FetchReportSummaryEntries
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# FetchReportSummaryEntries method of the Win32\_TSLicenseReport class

Retrieves summaries of Remote Desktop Services Per User client access licenses (RDS Per User CALs) from the report.

## Syntax


```mof
uint32 FetchReportSummaryEntries(
  [in]      uint32                            StartIndex,
  [in, out] uint32                            Count,
  [out]     Win32_TSLicenseReportSummaryEntry ReportSummaryEntries[]
);
```



## Parameters

<dl> <dt>

*StartIndex* \[in\]
</dt> <dd>

Index of the first report entry to be received. The first report entry has an index of zero.

</dd> <dt>

*Count* \[in, out\]
</dt> <dd>

Number of report entries to retrieve from the report object. A value of zero indicates that all of the report entries starting at *StartIndex* are to be retrieved. On return, contains the number of entries in the *ReportSummaryEntries* array.

</dd> <dt>

*ReportSummaryEntries* \[out\]
</dt> <dd>

Returns an array of [**Win32\_TSLicenseReportSummaryEntry**](win32-tslicensereportsummaryentry.md) classes.

</dd> </dl>

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. A value of **LSERVER\_I\_NO\_MORE\_DATA** (0x4001) indicates that there are no more report entries.

## Remarks

This is not a static method. This method must be called from a per user license usage report object.

You must be a member of the Administrators group to call this method.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                            |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>TlsWmiProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TlsWmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSLicenseReport**](win32-tslicensereport.md)
</dt> <dt>

[**Win32\_TSLicenseReportSummaryEntry**](win32-tslicensereportsummaryentry.md)
</dt> </dl>

 

