---
title: Win32_TSLicenseReportFailedPerUserEntry class
description: Provides details about the failed Remote Desktop Services Per User client access license (RDS \ 160;Per User CAL).
ms.assetid: 27d155a4-938e-4bca-8d15-03c44740e506
ms.tgt_platform: multiple
keywords:
- Win32_TSLicenseReportFailedPerUserEntry class Remote Desktop Services
- Win32_TSLicenseReportFailedPerUserEntry class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSLicenseReportFailedPerUserEntry
- Win32_TSLicenseReportFailedPerUserEntry.User
- Win32_TSLicenseReportFailedPerUserEntry.TriedIssuanceOn
- Win32_TSLicenseReportFailedPerUserEntry.CALType
- Win32_TSLicenseReportFailedPerUserEntry.ProductVersion
- Win32_TSLicenseReportFailedPerUserEntry.ProductVersionID
api_location:
- TlsWmiProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TSLicenseReportFailedPerUserEntry class

Provides details about the failed Remote Desktop Services Per User client access license (RDS Per User CAL).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class Win32_TSLicenseReportFailedPerUserEntry
{
  string   User;
  DATETIME TriedIssuanceOn;
  string   CALType;
  string   ProductVersion;
  uint32   ProductVersionID;
};
```

## Members

The **Win32\_TSLicenseReportFailedPerUserEntry** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_TSLicenseReportFailedPerUserEntry** class has these properties.

<dl> <dt>

**CALType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the type of CAL issued. This will be one of the following values.

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

**ProductVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version of Remote Desktop Services for which the RDS Per User CAL was issued. This will be one of the following values.

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

**TriedIssuanceOn**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date on which license issuance was attempted.

</dd> <dt>

**User**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

The name of the user to whom the license issuance was attempted.

</dd> </dl>

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

[**FetchReportFailedPerUserEntries**](fetchreportfailedperuserentries-win32-tslicensereport.md)
</dt> </dl>

 

