---
title: Win32_TSLicenseReportEntry class
description: Provides details of the issued Remote Desktop Services Per User client access license (RDS \ 160;Per User CAL).
ms.assetid: 75fa7f39-af5b-45a0-ba2b-5c667edfec16
ms.tgt_platform: multiple
keywords:
- Win32_TSLicenseReportEntry class Remote Desktop Services
- Win32_TSLicenseReportEntry class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSLicenseReportEntry
- Win32_TSLicenseReportEntry.User
- Win32_TSLicenseReportEntry.ExpirationDate
- Win32_TSLicenseReportEntry.CALType
- Win32_TSLicenseReportEntry.ProductVersion
- Win32_TSLicenseReportEntry.ProductVersionID
api_location:
- TlsWmiProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TSLicenseReportEntry class

Provides details of the issued Remote Desktop Services Per User client access license (RDS Per User CAL).

## Syntax

``` syntax
[AMENDMENT]
class Win32_TSLicenseReportEntry
{
  string   User;
  DATETIME ExpirationDate;
  string   CALType;
  string   ProductVersion;
  uint32   ProductVersionID;
};
```

## Members

The **Win32\_TSLicenseReportEntry** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_TSLicenseReportEntry** class has these properties.

<dl> <dt>

**CALType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the type of CAL issued. This will be one of the following values.

**Windows Server 2008 R2 and Windows Server 2008:** This property is not supported.

"Built-in TS Per Device CAL"

"TS Per Device CAL"

"TS Internet Connector CAL"

"TS Per User CAL"

"TS or RDS Per Device CAL"

"TS or RDS Per User CAL"

"VDI Standard Suite Per Device subscription license"

"VDI Premium Suite Per Device subscription license"

"RDS Per Device CAL"

"RDS Per User CAL"

</dd> <dt>

**ExpirationDate**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Expiration date of the license that was issued to the user.

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

**User**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Name of the user to whom the license was issued.

</dd> </dl>

## Remarks

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

[**FetchReportEntries**](fetchreportentries-win32-tslicensereport.md)
</dt> <dt>

[**Win32\_TSIssuedLicense**](win32-tsissuedlicense.md)
</dt> <dt>

[**Win32\_TSLicenseKeyPack**](win32-tslicensekeypack.md)
</dt> <dt>

[**Win32\_TSLicenseReport**](win32-tslicensereport.md)
</dt> <dt>

[**Win32\_TSLicenseServer**](win32-tslicenseserver.md)
</dt> </dl>

 

