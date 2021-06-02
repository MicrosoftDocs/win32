---
title: GenerateReport method of the Win32_TSLicenseReport class (Gpmgmt.h)
description: GenerateReport is no longer available for use as of Windows Server 2012.
ms.assetid: 2d3b16d6-52e8-491f-b6e5-419e9a21013b
ms.tgt_platform: multiple
keywords:
- GenerateReport method Remote Desktop Services
- GenerateReport method Remote Desktop Services , Win32_TSLicenseReport class
- Win32_TSLicenseReport class Remote Desktop Services , GenerateReport method
topic_type:
- apiref
api_name:
- Win32_TSLicenseReport.GenerateReport
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GenerateReport method of the Win32\_TSLicenseReport class

\[**GenerateReport** is no longer available for use as of Windows Server 2012. Instead, use [**GenerateReportEx**](generatereportex-win32-tslicensereport.md).\]

This method is not supported.

**Windows Server 2008 R2 and Windows Server 2008:** Generates a current per user license usage report on the Remote Desktop license server.

## Syntax


```mof
uint32 GenerateReport(
  [in]  uint32 ScopeType,
  [in]  string ScopeValue,
  [out] string FileName
);
```



## Parameters

<dl> <dt>

*ScopeType* \[in\]
</dt> <dd>

Scope of the license usage report. It can have the following values.

<dt>

1
</dt> <dd>

The report will be generated for the entire domain.

</dd> <dt>

2
</dt> <dd>

The report will be generated for the organizational unit (OU) that is specified in the *ScopeValue* parameter.

</dd> <dt>

3
</dt> <dd>

The report will be generated for all trusted domains.

</dd> </dl> </dd> <dt>

*ScopeValue* \[in\]
</dt> <dd>

If the *ScopeType* parameter is 2, *ScopeType* specifies the OU for which the report will be generated. You must specify *ScopeValue* by using the format **OU=***OUName1***,OU=***OUName2***...**.

</dd> <dt>

*FileName* \[out\]
</dt> <dd>

The file name of the generated report.

</dd> </dl>

## Return value

Returns **WBEM\_E\_NOT\_SUPPORTED**.

**Windows Server 2008 R2 and Windows Server 2008:** If the method succeeds, it returns zero. If the method is unsuccessful, it returns a nonzero value. For a list of error codes, see [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md).

## Remarks

This is a static method.

You must be a member of the Administrators group to call this method.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                            |
| End of client support<br/>    | None supported<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                         |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                    |
| Header<br/>                   | <dl> <dt>Gpmgmt.h</dt> </dl>       |
| MOF<br/>                      | <dl> <dt>TlsWmiProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TlsWmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSLicenseReport**](win32-tslicensereport.md)
</dt> </dl>

 

