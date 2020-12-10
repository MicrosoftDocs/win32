---
title: GenerateReportEx method of the Win32_TSLicenseReport class
description: Generates a current license usage report for both Per User and Per Device licenses.
ms.assetid: c454e0c5-ca1c-41c7-86b2-1e52c414aeb5
ms.tgt_platform: multiple
keywords:
- GenerateReportEx method Remote Desktop Services
- GenerateReportEx method Remote Desktop Services , Win32_TSLicenseReport class
- Win32_TSLicenseReport class Remote Desktop Services , GenerateReportEx method
topic_type:
- apiref
api_name:
- Win32_TSLicenseReport.GenerateReportEx
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GenerateReportEx method of the Win32\_TSLicenseReport class

Generates a current license usage report for both Per User and Per Device licenses.

## Syntax


```mof
uint32 GenerateReportEx(
  [out] string FileName
);
```



## Parameters

<dl> <dt>

*FileName* \[out\]
</dt> <dd>

The file name of the generated report.

</dd> </dl>

## Return value

If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

This is a static method.

You must be a member of the Administrators group to call this method.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

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

 

