---
title: SetSecurityDescriptor method of the StdRegProv class
description: Updates the security descriptor of the specified key with a new security descriptor that is defined by an instance of a \_\_SecurityDescriptor class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4cbf8ea7-dc53-4fce-8694-0e80ded3e54b
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetSecurityDescriptor method
- SetSecurityDescriptor method, StdRegProv class
- StdRegProv class, SetSecurityDescriptor method
topic_type:
- apiref
api_name:
- StdRegProv.SetSecurityDescriptor
api_location:
- Stdprov.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetSecurityDescriptor method of the StdRegProv class

The **SetSecurityDescriptor** method updates the security descriptor of the specified key with a new security descriptor that is defined by an instance of a [**\_\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394673) class.

## Syntax


```mof
uint32 SetSecurityDescriptor(
  [in] uint32               hDefKey = HKEY_LOCAL_MACHINE,
  [in] string               sSubKeyName,
  [in] __SecurityDescriptor Descriptor
);
```



## Parameters

<dl> <dt>

*hDefKey* \[in\]
</dt> <dd>

A registry tree, also known as a hive, that contains the *sSubKeyName* path. The default value is **HKEY\_LOCAL\_MACHINE**.

The following trees are defined in WinReg.h.

<dt>

<span id="HKEY_CLASSES_ROOT"></span><span id="hkey_classes_root"></span>

**HKEY\_CLASSES\_ROOT** (2147483648)


</dt> <dd></dd> <dt>

<span id="HKEY_CURRENT_USER"></span><span id="hkey_current_user"></span>

**HKEY\_CURRENT\_USER** (2147483649)


</dt> <dd></dd> <dt>

<span id="HKEY_LOCAL_MACHINE"></span><span id="hkey_local_machine"></span>

**HKEY\_LOCAL\_MACHINE** (2147483650)


</dt> <dd></dd> <dt>

<span id="HKEY_USERS"></span><span id="hkey_users"></span>

**HKEY\_USERS** (2147483651)


</dt> <dd></dd> <dt>

<span id="HKEY_CURRENT_CONFIG"></span><span id="hkey_current_config"></span>

**HKEY\_CURRENT\_CONFIG** (2147483653)


</dt> <dd></dd> </dl> </dd> <dt>

*sSubKeyName* \[in\]
</dt> <dd>

The key name on which to set the security descriptor.

</dd> <dt>

*Descriptor* \[in\]
</dt> <dd>

The security descriptor to set on the key name.

</dd> </dl>

## Return value

In C++, the method returns a **uint32** value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that is defined in WinError.h. In C++, use the [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag to get a generic description of the error. You can also look up return values under the [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559).

In scripting or Visual Basic, the method returns an integer value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that you can look up in [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Remarks

The [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402) instance represents a [**SECURITY\_DESCRIPTOR\_CONTROL**](https://msdn.microsoft.com/library/windows/desktop/aa379566) data type and contains a [*discretionary access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-discretionary-access-control-list-gly) (DACL) and a [*system access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-system-access-control-list-gly) (SACL). For more information, see [Access Control Lists](https://msdn.microsoft.com/library/windows/desktop/aa374872).

If the **SeSecurityPrivilege** is not granted or enabled when getting a security descriptor, then only the DACL is returned in the returned security descriptor. For more information, see [**Privilege Constants**](https://msdn.microsoft.com/library/aa392758) and [Executing Privileged Operations](https://msdn.microsoft.com/library/aa390428).

You can update both the DACL and the SACL in the [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402) instance when calling this method, but you also can update only the DACL or only the SACL.

The following values in [**SECURITY\_DESCRIPTOR\_CONTROL**](https://msdn.microsoft.com/library/windows/desktop/aa379566) determine whether the DACL or the SACL or both are updated.

-   **SE\_DACL\_PRESENT**

    Indicates that the DACL should be updated. If this is not set then WMI preserves the original value of the DACL.

-   **SE\_SACL\_PRESENT**

    Indicates that the SACL should be updated. If this is not set then WMI preserves the original value of the SACL. To update the SACL, the account must have the **SeSecurityPrivilege** privilege enabled. For scripting, the privilege name is **SeSecurityPrivilege**. For more information, see [**Privilege Constants**](https://msdn.microsoft.com/library/aa392758).

If the Group trustee and the Owner trustee properties are not **NULL**, then they are updated. Otherwise, WMI preserves the original values. For more information, see [WMI Security Descriptor Objects](https://msdn.microsoft.com/library/aa394577).

When a new SACL is **NULL** in a call this method, then the security descriptor SACL on the target securable object is left unchanged.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\default<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RegEvent.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Stdprov.dll</dt> </dl>  |



## See also

<dl> <dt>

[**StdRegProv**](stdregprov.md)
</dt> <dt>

[Modifying the System Registry](https://msdn.microsoft.com/library/aa392388)
</dt> <dt>

[WMI Tasks: Registry](https://msdn.microsoft.com/library/aa394600)
</dt> </dl>

 

 





