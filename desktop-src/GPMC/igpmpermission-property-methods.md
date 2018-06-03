---
title: IGPMPermission Property Methods
description: The property methods of the IGPMPermission interface get the properties described in the following table. For a general discussion of property methods, see Interface Property Methods in the ADSI documentation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4af04405-66a4-4721-83ff-70ae505b3494
ms.prod: windows-server-dev
ms.technology: group-policy
ms.tgt_platform: multiple
keywords:
- IGPMPermission Property Methods GPMC
topic_type:
- apiref
api_name:
- IGPMPermission Property Methods
- IGPMPermission.Denied
- IGPMPermission.get_Denied
- IGPMPermission.Inheritable
- IGPMPermission.get_Inheritable
- IGPMPermission.Inherited
- IGPMPermission.get_Inherited
- IGPMPermission.Permission
- IGPMPermission.get_Permission
- IGPMPermission.Trustee
- IGPMPermission.get_Trustee
api_location:
- Gpmgmt.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IGPMPermission Property Methods

The property methods of the **IGPMPermission** interface get the properties described in the following table. For a general discussion of property methods, see [Interface Property Methods](https://msdn.microsoft.com/library/aa746378) in the ADSI documentation.

## Properties

<dl> <dt>

**Denied**
</dt> <dd> <dl>

Value that indicates whether the permission is denied. If **VARIANT\_TRUE**, the permission is denied.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **Boolean**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Denied(
  [out] VARIANT_BOOL* pVal
);
```


</dt> </dl> </dd> <dt>

**Inheritable**
</dt> <dd> <dl>

Value that indicates whether the permission can be inherited by child containers. If **VARIANT\_TRUE**, the permission can be inherited.

When setting security for GPOs, the value of this property is always **VARIANT\_TRUE**; For WMI filters, it is always **VARIANT\_FALSE**. For **permSOMWMICreate**, **permSOMWMIFullControl**, and **permSOMGPOCreate**, the value is always **VARIANT\_FALSE**.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **Boolean**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Inheritable(
  [out] VARIANT_BOOL* pVal
);
```


</dt> </dl> </dd> <dt>

**Inherited**
</dt> <dd> <dl>

Value that indicates whether the permission is inherited from a parent container. If **VARIANT\_TRUE**, the permission is inherited.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **Boolean**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Inherited(
  [out] VARIANT_BOOL* pVal
);
```


</dt> </dl> </dd> <dt>

**Permission**
</dt> <dd> <dl>

The policy-related permission level; for example, **permGPOApply**, **permWMIFilterEdit**, and **permSOMLink**. For a complete list of the supported permission levels, see the [**IGPM::CreatePermission**](/previous-versions/windows/desktop/api/Gpmgmt/nf-gpmgmt-igpm-createpermission) method.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **String**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Permission(
  [out] GPMPermissionType* pVal
);
```


</dt> </dl> </dd> <dt>

**Trustee**
</dt> <dd> <dl>

Returns the [**IGPMTrustee**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmtrustee) interface and the trustee part of the permission.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **GPMTrustee**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Trustee(
  [out] IGPMTrustee* pGPMTrustee
);
```


</dt> </dl> </dd> </dl>

 

## Remarks

For more information about policy-related permissions, see [**IGPM::CreatePermission**](/previous-versions/windows/desktop/api/Gpmgmt/nf-gpmgmt-igpm-createpermission).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>Gpmgmt.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Gpmgmt.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Gpmgmt.dll</dt> </dl> |
| IID<br/>                      | IID\_IGPMPermission is defined as 35EBCA40-E1A1-4A02-8905-D79416FB464A<br/>     |



## See also

<dl> <dt>

[**IGPMPermission**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmpermission)
</dt> <dt>

[**IGPM**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpm)
</dt> <dt>

[**IGPMTrustee**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmtrustee)
</dt> <dt>

[**IGPMSecurityInfo**](/previous-versions/windows/desktop/api/Gpmgmt/nn-gpmgmt-igpmsecurityinfo)
</dt> </dl>

 

 





