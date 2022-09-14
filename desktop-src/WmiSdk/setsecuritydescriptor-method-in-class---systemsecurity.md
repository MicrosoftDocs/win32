---
description: Writes an updated version of the security descriptor that controls access to the WMI namespace to which you are connected. The security descriptor is represented by an instance of \_\_SecurityDescriptor.
ms.assetid: e92430fd-61b1-4986-88dc-b85f502f62e6
ms.tgt_platform: multiple
title: SetSecurityDescriptor method of the __SystemSecurity class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __SystemSecurity.SetSecurityDescriptor
api_type: 
- COM
api_location: 
- All
---

# SetSecurityDescriptor method of the \_\_SystemSecurity class

The [**SetSecurityDescriptor**](/windows/desktop/CIMWin32Prov/setsecuritydescriptor-method-in-class-win32-printer) method writes an updated version of the security descriptor that controls access to the WMI namespace to which you are connected. The security descriptor is represented by an instance of [**\_\_SecurityDescriptor**](--securitydescriptor.md). For more information, see [Changing Access Security on Securable Objects](changing-access-security-on-securable-objects.md).

## Syntax


```mof
uint32 SetSecurityDescriptor(
  [in] __SecurityDescriptor Descriptor
);
```



## Parameters

<dl> <dt>

*Descriptor* \[in\]
</dt> <dd>

The security descriptor associated with the WMI Namespace.

</dd> </dl>

## Return value

Returns one of the values listed in the following list, or a different value to indicate an error. For more information, see [WMI Return Codes](wmi-return-codes.md) or [**WbemErrorEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemerrorenum).

<dl> <dt>

**0**
</dt> <dd>

Successful completion.

</dd> <dt>

**2**
</dt> <dd>

The user does not have access to the requested information.

</dd> <dt>

**8**
</dt> <dd>

Unknown failure.

</dd> <dt>

**9**
</dt> <dd>

The user does not have adequate privileges to execute the method.

</dd> <dt>

**21**
</dt> <dd>

A parameter specified in the method call is not valid.

</dd> </dl>

## Remarks

The [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor) instance represents a [**SECURITY\_DESCRIPTOR\_CONTROL**](/windows/desktop/SecAuthZ/security-descriptor-control) data type and contains a [*discretionary access control list*](/windows/desktop/SecGloss/d-gly) (DACL) and a [*System Access Control List*](/windows/desktop/SecGloss/a-gly) (SACL). For more information, see [Access Control Lists](/windows/desktop/SecAuthZ/access-control-lists).

If the **SeSecurityPrivilege** is not granted or enabled when getting a security descriptor, then only the DACL is returned in the returned security descriptor. For more information, see [**Privilege Constants**](privilege-constants.md) and [Executing Privileged Operations](executing-privileged-operations.md).

You can update both the DACL and the SACL in the [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor) instance when calling this method, but you also can update only the DACL or only the SACL.

The following values in [**SECURITY\_DESCRIPTOR\_CONTROL**](/windows/desktop/SecAuthZ/security-descriptor-control) determine whether the DACL or the SACL or both are updated.

-   **SE\_DACL\_PRESENT**

    Indicates that the DACL should be updated. If this is not set then WMI preserves the original value of the DACL.

-   **SE\_SACL\_PRESENT**

    Indicates that the SACL should be updated. If this is not set then WMI preserves the original value of the SACL. To update the SACL, the account must have the **SeSecurityPrivilege** privilege enabled. For scripting, the privilege name is **SeSecurityPrivilege**. For more information, see [**Privilege Constants**](privilege-constants.md).

If the Group trustee and the Owner trustee properties are not **NULL**, then they are updated. Otherwise, WMI preserves the original values. For more information, see [WMI Security Descriptor Objects](wmi-security-descriptor-objects.md).

When a new SACL is **NULL** in a call this method, then the security descriptor SACL on the target securable object is left unchanged.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_SystemSecurity**](--systemsecurity.md)
</dt> <dt>

[Setting Namepace Security Descriptors](setting-namespace-security-descriptors.md)
</dt> </dl>

 

