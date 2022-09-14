---
title: Win32_TSLicenseReportPerDeviceEntry class
description: Provides details about the failed Remote Desktop Services Per Device client access license (RDS \ 160;Per Device CAL).
ms.assetid: b26f2518-439c-4562-9492-a0cfa60c457a
ms.tgt_platform: multiple
keywords:
- Win32_TSLicenseReportPerDeviceEntry class Remote Desktop Services
- Win32_TSLicenseReportPerDeviceEntry class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSLicenseReportPerDeviceEntry
- Win32_TSLicenseReportPerDeviceEntry.sIssuedToComputer
- Win32_TSLicenseReportPerDeviceEntry.sHardwareId
- Win32_TSLicenseReportPerDeviceEntry.ExpirationDate
- Win32_TSLicenseReportPerDeviceEntry.CALType
- Win32_TSLicenseReportPerDeviceEntry.ProductVersion
- Win32_TSLicenseReportPerDeviceEntry.ProductVersionID
api_location:
- TlsWmiProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TSLicenseReportPerDeviceEntry class

Provides details about the failed Remote Desktop Services Per Device client access license (RDS Per Device CAL).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class Win32_TSLicenseReportPerDeviceEntry
{
  string   sIssuedToComputer;
  string   sHardwareId;
  DATETIME ExpirationDate;
  string   CALType;
  string   ProductVersion;
  uint32   ProductVersionID;
};
```

## Members

The **Win32\_TSLicenseReportPerDeviceEntry** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_TSLicenseReportPerDeviceEntry** class has these properties.

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

**ExpirationDate**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The expiration date of the license.

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

**sHardwareId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

The hardware identifier of the computer.

</dd> <dt>

**sIssuedToComputer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the computer that the license issuance was attempted for.

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

[**FetchReportPerDeviceEntries**](fetchreportperdeviceentries-win32-tslicensereport.md)
</dt> </dl>

 

