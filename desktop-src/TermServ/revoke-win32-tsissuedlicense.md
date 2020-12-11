---
title: Revoke method of the Win32_TSIssuedLicense class
description: Revokes the Remote Desktop Services Per Device client access licenses (RDS \ 160;Per Device CALs) that are represented by the Win32\_TSIssuedLicense object. This is not a static function.
ms.assetid: b1eb7448-5d8e-4c2d-ba52-9363e8e0297a
ms.tgt_platform: multiple
keywords:
- Revoke method Remote Desktop Services
- Revoke method Remote Desktop Services , Win32_TSIssuedLicense class
- Win32_TSIssuedLicense class Remote Desktop Services , Revoke method
topic_type:
- apiref
api_name:
- Win32_TSIssuedLicense.Revoke
api_location:
- TlsWmiProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Revoke method of the Win32\_TSIssuedLicense class

Revokes the Remote Desktop Services Per Device client access licenses (RDS Per Device CALs) that are represented by the [**Win32\_TSIssuedLicense**](win32-tsissuedlicense.md) object. This is not a static function.

## Syntax


```mof
uint32 Revoke(
  [out] uint32   RevokableCals,
  [out] DATETIME NextRevokeAllowedOn
);
```



## Parameters

<dl> <dt>

*RevokableCals* \[out\]
</dt> <dd>

Number of RDS CALs of the same type as the current object that can be revoked.

</dd> <dt>

*NextRevokeAllowedOn* \[out\]
</dt> <dd>

Date that the administrator can next try to revoke licenses. This parameter only contains valid data when the **Revoke** method call has failed because the maximum revoke count has been reached.

</dd> </dl>

## Remarks

You must be a member of the Administrators group to call this method.

Only RDS Per Device CALs can be revoked.

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
</dt> </dl>

 

