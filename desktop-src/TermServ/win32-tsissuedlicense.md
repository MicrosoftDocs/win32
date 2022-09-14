---
title: Win32_TSIssuedLicense class
description: Describes instances of Remote Desktop Services Per Device client access licenses (RDS \ 160;Per Device CALs) that are issued from a Remote Desktop license server.
ms.assetid: 15825dc5-9ada-4c11-ac77-beb681e9b33c
ms.tgt_platform: multiple
keywords:
- Win32_TSIssuedLicense class Remote Desktop Services
- Win32_TSIssuedLicense class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSIssuedLicense
- Win32_TSIssuedLicense.LicenseId
- Win32_TSIssuedLicense.KeyPackId
- Win32_TSIssuedLicense.sIssuedToUser
- Win32_TSIssuedLicense.sIssuedToComputer
- Win32_TSIssuedLicense.LicenseStatus
- Win32_TSIssuedLicense.IssueDate
- Win32_TSIssuedLicense.ExpirationDate
- Win32_TSIssuedLicense.sHardwareId
api_location:
- TlsWmiProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TSIssuedLicense class

Describes instances of Remote Desktop Services Per Device client access licenses (RDS Per Device CALs) that are issued from a Remote Desktop license server.

## Syntax

``` syntax
[dynamic, provider("Win32_WIN32_TERMSERVLICENSING_Prov"), AMENDMENT]
class Win32_TSIssuedLicense
{
  uint32   LicenseId;
  uint32   KeyPackId;
  string   sIssuedToUser;
  string   sIssuedToComputer;
  uint32   LicenseStatus;
  DATETIME IssueDate;
  DATETIME ExpirationDate;
  string   sHardwareId;
};
```

## Members

The **Win32\_TSIssuedLicense** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_TSIssuedLicense** class has these methods.



| Method                                         | Description                                                                                               |
|:-----------------------------------------------|:----------------------------------------------------------------------------------------------------------|
| [**Revoke**](revoke-win32-tsissuedlicense.md) | Revokes the RDS Per Device CALs that are represented by the **Win32\_TSIssuedLicense** object.<br/> |



 

### Properties

The **Win32\_TSIssuedLicense** class has these properties.

<dl> <dt>

**ExpirationDate**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifies the date that the license will expire.

</dd> <dt>

**IssueDate**
</dt> <dd> <dl> <dt>

Data type: **DATETIME**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifies the date that the license was issued.

</dd> <dt>

**KeyPackId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Identifies the Remote Desktop Services license key pack.

</dd> <dt>

**LicenseId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Unique identifier for this license.

</dd> <dt>

**LicenseStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Status of the license.

<dt>

0
</dt> <dd>

The license status is unknown.

</dd> <dt>

1
</dt> <dd>

The license is a temporary license.

</dd> <dt>

2
</dt> <dd>

The license is active.

</dd> <dt>

3
</dt> <dd>

The license is an upgrade license.

</dd> <dt>

4
</dt> <dd>

The license has been revoked.

</dd> <dt>

5
</dt> <dd>

The license status is pending.

</dd> <dt>

6
</dt> <dd>

The license is a concurrent license.

</dd> </dl>

</dd> <dt>

**sHardwareId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Hardware identifier for which the license was issued.

</dd> <dt>

**sIssuedToComputer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Computer name for which the license was issued.

</dd> <dt>

**sIssuedToUser**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

User name for which the license was issued.

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

[**Win32\_TSLicenseKeyPack**](win32-tslicensekeypack.md)
</dt> <dt>

[**Win32\_TSLicenseReport**](win32-tslicensereport.md)
</dt> <dt>

[**Win32\_TSLicenseReportEntry**](win32-tslicensereportentry.md)
</dt> <dt>

[**Win32\_TSLicenseServer**](win32-tslicenseserver.md)
</dt> </dl>

 

