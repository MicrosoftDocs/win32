---
title: Win32_TSLicenseReport class
description: Provides instances of Remote Desktop Services Per User client access license (RDS \ 160;Per User CAL) usage reports that are generated on the Remote Desktop license server, and methods for license report generation, fetch, and delete operations.
ms.assetid: 8d67f158-cda3-4cf4-a766-09d08c21c49e
ms.tgt_platform: multiple
keywords:
- Win32_TSLicenseReport class Remote Desktop Services
- Win32_TSLicenseReport class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSLicenseReport
- Win32_TSLicenseReport.FileName
- Win32_TSLicenseReport.LicenseUsageCount
- Win32_TSLicenseReport.InstalledLicenses
- Win32_TSLicenseReport.GenerationDateTime
- Win32_TSLicenseReport.ScopeType
- Win32_TSLicenseReport.ScopeValue
- Win32_TSLicenseReport.Version
api_location:
- TlsWmiProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TSLicenseReport class

Provides instances of Remote Desktop Services Per User client access license (RDS Per User CAL) usage reports that are generated on the Remote Desktop license server, and methods for license report generation, fetch, and delete operations.

## Syntax

``` syntax
[dynamic, provider("Win32_WIN32_TERMSERVLICENSING_Prov"), AMENDMENT]
class Win32_TSLicenseReport
{
  string   FileName;
  uint32   LicenseUsageCount;
  uint32   InstalledLicenses;
  DATETIME GenerationDateTime;
  uint32   ScopeType;
  string   ScopeValue;
  uint32   Version;
};
```

## Members

The **Win32\_TSLicenseReport** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_TSLicenseReport** class has these methods.



| Method                                                                                                         | Description                                                                                                                                                                                     |
|:---------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DeleteReport**](deletereport-win32-tslicensereport.md)                                                     | Deletes a report object on the Remote Desktop license server. This is not a static method.<br/>                                                                                           |
| [**FetchReportEntries**](fetchreportentries-win32-tslicensereport.md)                                         | Retrieves entries in the report object.<br/>                                                                                                                                              |
| [**FetchReportFailedPerUserEntries**](fetchreportfailedperuserentries-win32-tslicensereport.md)               | Retrieves details of failed Remote Desktop Services Per User client access licenses (RDS Per User CALs) from the report.<br/>                                                             |
| [**FetchReportFailedPerUserSummaryEntries**](fetchreportfailedperusersummaryentries-win32-tslicensereport.md) | Retrieves summary information of failed Remote Desktop Services Per User client access licenses (RDS Per User CALs) from the report.<br/>                                                 |
| [**FetchReportPerDeviceEntries**](fetchreportperdeviceentries-win32-tslicensereport.md)                       | Retrieves information of issued Remote Desktop Services Per Device client access licenses (RDS Per Device CALs) from the report.<br/>                                                     |
| [**FetchReportSummaryEntries**](win32-tslicensereport-fetchreportsummaryentries.md)                           | Retrieves license summaries from the report object.<br/>                                                                                                                                  |
| [**GenerateReport**](generatereport-win32-tslicensereport.md)                                                 | This method is not supported.<br/> **Windows Server 2008 R2 and Windows Server 2008:** Generates a current per user license usage report on the Remote Desktop license server.<br/> |
| [**GenerateReportEx**](generatereportex-win32-tslicensereport.md)                                             | Generates a current per user license usage report on the Remote Desktop license server.<br/>                                                                                              |



 

### Properties

The **Win32\_TSLicenseReport** class has these properties.

<dl> <dt>

**FileName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

The report name.

</dd> <dt>

**GenerationDateTime**
</dt> <dd> <dl> <dt>

Data type: **[DATETIME](/windows/desktop/WmiSdk/datetime)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

RD Licensing report generation date and time.

</dd> <dt>

**InstalledLicenses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

This property is not supported.

**Windows Server 2008 R2 and Windows Server 2008:** Number of RDS Per User CALs that are installed.

</dd> <dt>

**LicenseUsageCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

This property is not supported.

**Windows Server 2008 R2 and Windows Server 2008:** Number of RDS Per User CALs that are currently in use.

</dd> <dt>

**ScopeType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

This property is not supported.

**Windows Server 2008 R2 and Windows Server 2008:** RD Licensing report scope type.

</dd> <dt>

**ScopeValue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DEPRECATED**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

This property is not supported.

**Windows Server 2008 R2 and Windows Server 2008:** RD Licensing report scope value.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

RD Licensing report version.

</dd> </dl>

## Remarks

Reports that are generated by using WMI are displayed in RD Licensing Manager. Reports that are deleted by using WMI are also deleted from RD Licensing Manager.

You must be a member of the Administrators group to use this class.

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

[**Win32\_TSIssuedLicense**](win32-tsissuedlicense.md)
</dt> <dt>

[**Win32\_TSLicenseKeyPack**](win32-tslicensekeypack.md)
</dt> <dt>

[**Win32\_TSLicenseReportEntry**](win32-tslicensereportentry.md)
</dt> <dt>

[**Win32\_TSLicenseServer**](win32-tslicenseserver.md)
</dt> </dl>

 

