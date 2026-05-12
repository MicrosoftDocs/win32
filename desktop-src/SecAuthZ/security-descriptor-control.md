---
description: Set of bit flags that qualify the meaning of a security descriptor or its components.
ms.assetid: 9a4ef57e-c374-4ef6-99dc-1a8dd250f2c2
title: SECURITY_DESCRIPTOR_CONTROL (Winnt.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SECURITY\_DESCRIPTOR\_CONTROL

The **SECURITY\_DESCRIPTOR\_CONTROL** data type is a set of bit flags that qualify the meaning of a [*security descriptor*](/windows/desktop/SecGloss/s-gly) or its components. Each security descriptor has a **Control** member that stores the **SECURITY\_DESCRIPTOR\_CONTROL** bits.


```C++
typedef WORD SECURITY_DESCRIPTOR_CONTROL, *PSECURITY_DESCRIPTOR_CONTROL;
```



## Remarks

To get the control bits of a security descriptor, call the [**GetSecurityDescriptorControl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorcontrol) function. To set the control bits of a security descriptor, use the functions for modifying security descriptors. For a list of these functions, see the See Also section.

Applications can use the [**SetSecurityDescriptorControl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptorcontrol) function to set the control bits that relate to automatic inheritance of ACEs.

The control value retrieved by the [**GetSecurityDescriptorControl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorcontrol) function can include a combination of the following **SECURITY\_DESCRIPTOR\_CONTROL** bit flags.



| Value                                                     | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SE\_DACL\_AUTO\_INHERIT\_REQ<br/> 0x0100<br/> | Indicates a required [*security descriptor*](/windows/desktop/SecGloss/s-gly) in which the [*discretionary access control list*](/windows/desktop/SecGloss/d-gly) (DACL) is set up to support automatic propagation of inheritable [*access control entries*](/windows/desktop/SecGloss/a-gly) (ACEs) to existing child objects.<br/> For [*access control lists*](/windows/desktop/SecGloss/a-gly) (ACLs) that support auto inheritance, this bit is always set. Protected servers can call the [**ConvertToAutoInheritPrivateObjectSecurity**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-converttoautoinheritprivateobjectsecurity) function to convert a security descriptor and set this flag. <br/> |
| SE\_DACL\_AUTO\_INHERITED<br/> 0x0400<br/>    | Indicates a security descriptor in which the [*discretionary access control list*](/windows/desktop/SecGloss/d-gly) (DACL) is set up to support automatic propagation of inheritable [*access control entries*](/windows/desktop/SecGloss/a-gly) (ACEs) to existing child objects.<br/> For [*access control lists*](/windows/desktop/SecGloss/a-gly) (ACLs) that support auto inheritance, this bit is always set. Protected servers can call the [**ConvertToAutoInheritPrivateObjectSecurity**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-converttoautoinheritprivateobjectsecurity) function to convert a security descriptor and set this flag. <br/>                                                                                                  |
| SE\_DACL\_DEFAULTED<br/> 0x0008<br/>          | Indicates a security descriptor with a default DACL. For example, if the creator an object does not specify a DACL, the object receives the default DACL from the [*access token*](/windows/desktop/SecGloss/a-gly) of the creator. This flag can affect how the system treats the DACL with respect to ACE inheritance. The system ignores this flag if the SE\_DACL\_PRESENT flag is not set.<br/> This flag is used to determine how the final DACL on the object is to be computed and is not stored physically in the security descriptor control of the securable object.<br/> To set this flag, use the [**SetSecurityDescriptorDacl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptordacl) function.<br/>                                                                                                                                                                      |
| SE\_DACL\_PRESENT<br/> 0x0004<br/>            | Indicates a security descriptor that has a DACL. If this flag is not set, or if this flag is set and the DACL is **NULL**, the security descriptor allows full access to everyone.<br/> This flag is used to hold the security information specified by a caller until the security descriptor is associated with a securable object. After the security descriptor is associated with a securable object, the SE\_DACL\_PRESENT flag is always set in the security descriptor control.<br/> To set this flag, use the [**SetSecurityDescriptorDacl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptordacl) function.<br/>                                                                                                                                                                                                                                                                                                   |
| SE\_DACL\_PROTECTED<br/> 0x1000<br/>          | Prevents the DACL of the security descriptor from being modified by inheritable ACEs. To set this flag, use the [**SetSecurityDescriptorControl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptorcontrol) function.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| SE\_GROUP\_DEFAULTED<br/> 0x0002<br/>         | Indicates that the [*security identifier*](/windows/desktop/SecGloss/s-gly) (SID) of the security descriptor group was provided by a default mechanism. This flag can be used by a resource manager to identify objects whose security descriptor group was set by a default mechanism. To set this flag, use the [**SetSecurityDescriptorGroup**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptorgroup) function.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| SE\_OWNER\_DEFAULTED<br/> 0x0001<br/>         | Indicates that the SID of the owner of the security descriptor was provided by a default mechanism. This flag can be used by a resource manager to identify objects whose owner was set by a default mechanism. To set this flag, use the [**SetSecurityDescriptorOwner**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptorowner) function.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| SE\_RM\_CONTROL\_VALID<br/> 0x4000<br/>       | Indicates that the resource manager control is valid.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| SE\_SACL\_AUTO\_INHERIT\_REQ<br/> 0x0200<br/> | Indicates a required security descriptor in which the [*system access control list*](/windows/desktop/SecGloss/s-gly) (SACL) is set up to support automatic propagation of inheritable ACEs to existing child objects.<br/> The system sets this bit when it performs the automatic inheritance algorithm for the object and its existing child objects. To convert a security descriptor and set this flag, protected servers can call the [**ConvertToAutoInheritPrivateObjectSecurity**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-converttoautoinheritprivateobjectsecurity) function.<br/>                                                                                                                                                                                                                                                                                   |
| SE\_SACL\_AUTO\_INHERITED<br/> 0x0800<br/>    | Indicates a security descriptor in which the [*system access control list*](/windows/desktop/SecGloss/s-gly) (SACL) is set up to support automatic propagation of inheritable ACEs to existing child objects.<br/> The system sets this bit when it performs the automatic inheritance algorithm for the object and its existing child objects. To convert a security descriptor and set this flag, protected servers can call the [**ConvertToAutoInheritPrivateObjectSecurity**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-converttoautoinheritprivateobjectsecurity) function. <br/>                                                                                                                                                                                                                                                                                           |
| SE\_SACL\_DEFAULTED<br/> 0x0020<br/>          | A default mechanism, rather than the original [*provider*](/windows/desktop/SecGloss/p-gly) of the security descriptor, provided the SACL. This flag can affect how the system treats the SACL, with respect to ACE inheritance. The system ignores this flag if the SE\_SACL\_PRESENT flag is not set. To set this flag, use the [**SetSecurityDescriptorSacl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptorsacl) function.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| SE\_SACL\_PRESENT<br/> 0x0010<br/>            | Indicates a security descriptor that has a SACL. To set this flag, use the [**SetSecurityDescriptorSacl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptorsacl) function.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| SE\_SACL\_PROTECTED<br/> 0x2000<br/>          | Prevents the SACL of the security descriptor from being modified by inheritable ACEs. To set this flag, use the [**SetSecurityDescriptorControl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptorcontrol) function.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| SE\_SELF\_RELATIVE<br/> 0x8000<br/>           | Indicates a [*self-relative security descriptor*](/windows/desktop/SecGloss/s-gly). If this flag is not set, the security descriptor is in absolute format. For more information, see [Absolute and Self-Relative Security Descriptors](absolute-and-self-relative-security-descriptors.md).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |



 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Winnt.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Low-level Access Control](low-level-access-control.md)
</dt> <dt>

[Basic Access Control Structures](authorization-structures.md)
</dt> <dt>

[**ConvertToAutoInheritPrivateObjectSecurity**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-converttoautoinheritprivateobjectsecurity)
</dt> <dt>

[**GetSecurityDescriptorControl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorcontrol)
</dt> <dt>

[**GetSecurityDescriptorDacl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptordacl)
</dt> <dt>

[**GetSecurityDescriptorGroup**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorgroup)
</dt> <dt>

[**GetSecurityDescriptorOwner**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorowner)
</dt> <dt>

[**GetSecurityDescriptorSacl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorsacl)
</dt> <dt>

[**SetSecurityDescriptorControl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptorcontrol)
</dt> <dt>

[**SetSecurityDescriptorDacl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptordacl)
</dt> <dt>

[**SetSecurityDescriptorGroup**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptorgroup)
</dt> <dt>

[**SetSecurityDescriptorOwner**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptorowner)
</dt> <dt>

[**SetSecurityDescriptorSacl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptorsacl)
</dt> </dl>

 

