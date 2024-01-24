---
title: Win32_TSLicenseReportSummaryEntry class
description: Provides a summary of the installed and issued Remote Desktop Services Per User client access licenses (RDS \ 160;Per User CALs).
ms.assetid: 0FD3BFFE-58B9-4037-969F-8C2323136C9D
ms.tgt_platform: multiple
keywords:
- Win32_TSLicenseReportSummaryEntry class Remote Desktop Services
- Win32_TSLicenseReportSummaryEntry class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSLicenseReportSummaryEntry
- Win32_TSLicenseReportSummaryEntry.ProductVersion
- Win32_TSLicenseReportSummaryEntry.ProductVersionID
- Win32_TSLicenseReportSummaryEntry.TSCALType
- Win32_TSLicenseReportSummaryEntry.InstalledLicenses
- Win32_TSLicenseReportSummaryEntry.IssuedLicenses
- Win32_TSLicenseReportSummaryEntry.TSCALAvailability
api_location:
- TlsWmiProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TSLicenseReportSummaryEntry class

Provides a summary of the installed and issued Remote Desktop Services Per User client access licenses (RDS Per User CALs).

## Syntax

``` syntax
[AMENDMENT]
class Win32_TSLicenseReportSummaryEntry
{
  string ProductVersion;
  uint32 ProductVersionID;
  string TSCALType;
  uint32 InstalledLicenses;
  uint32 IssuedLicenses;
  string TSCALAvailability;
};
```

## Members

The **Win32\_TSLicenseReportSummaryEntry** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_TSLicenseReportSummaryEntry** class has these properties.

<dl> <dt>

**InstalledLicenses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of RDS Per User CALs that are installed.

</dd> <dt>

**IssuedLicenses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of RDS Per User CALs that are issued.

</dd> <dt>

**ProductVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Version of Remote Desktop Services for which the RDS Per User CAL was issued.

<dt>

"Windows Server 2012"
</dt> <dd>

Only servers running Windows Server 2012, Windows Server 2008 R2, or Windows Server 2008 are supported with this license.

</dd> <dt>

"Windows Server 7"
</dt> <dd>

Only servers running Windows Server 2008 R2, or Windows Server 2008 are supported with this license.

</dd> <dt>

"Windows Server 2008"
</dt> <dd>

Only servers running Windows Server 2008 are supported with this license.

</dd> </dl>

</dd> <dt>

**ProductVersionID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Product version identifier for the Remote Desktop Services license key pack.

<dt>

4
</dt> <dd>

Windows Server 2012

</dd> <dt>

3
</dt> <dd>

Windows Server 2008 R2

</dd> <dt>

2
</dt> <dd>

Windows Server 2008

</dd> <dt>

1
</dt> <dd>

Not supported.

</dd> <dt>

0
</dt> <dd>

Not supported.

</dd> </dl>

</dd> <dt>

**TSCALAvailability**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The availability of the RDS Per User CALs. This will be one of the following values.

<dt>

"Available"
</dt> <dd>

The RDS Per User CALs are available.

</dd> <dt>

"Limited"
</dt> <dd>

The availability of the RDS Per User CALs is limited.

</dd> <dt>

"None"
</dt> <dd>

The RDS Per User CALs are not available.

</dd> <dt>

"Not Tracking"
</dt> <dd>

The availability of the RDS Per User CALs is not being tracked.

</dd> </dl>

</dd> <dt>

**TSCALType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of RDS Per User CALs. This will be one of the following values.

<dt>

"Per Device"
</dt> <dd>

The RDS Per User CALs are issued per device.

</dd> <dt>

"Per User"
</dt> <dd>

The RDS Per User CALs are issued per user.

</dd> <dt>

"Unknown"
</dt> <dd>

The type of RDS Per User CALs is unknown.

</dd> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                            |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>TlsWmiProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TlsWmiProv.dll</dt> </dl> |



 

 





