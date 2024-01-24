---
description: Identifies the object-related security information being set or queried.
ms.assetid: e3e8b35d-9d18-4611-a898-72ca13e40d33
title: SECURITY_INFORMATION (Winnt.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SECURITY\_INFORMATION

The **SECURITY\_INFORMATION** data type identifies the object-related security information being set or queried. This security information includes:

-   The owner of an object
-   The primary group of an object
-   The [*discretionary access control list*](/windows/desktop/SecGloss/d-gly) (DACL) of an object
-   The [*system access control list*](/windows/desktop/SecGloss/s-gly) (SACL) of an object


```C++
typedef DWORD SECURITY_INFORMATION, *PSECURITY_INFORMATION;
```



## Remarks

Some **SECURITY\_INFORMATION** members work only with the [**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa) function. These members are not returned in the structure returned by other security functions such as [**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa) or [**ConvertStringSecurityDescriptorToSecurityDescriptor**](/windows/desktop/api/Sddl/nf-sddl-convertstringsecuritydescriptortosecuritydescriptora).

Each item of security information is designated by a bit flag. Each bit flag can be one of the following values. For more information, see the [**SetSecurityAccessMask**](/windows/desktop/api/Securitybaseapi/nf-securitybaseapi-setsecurityaccessmask) and [**QuerySecurityAccessMask**](/windows/desktop/api/Securitybaseapi/nf-securitybaseapi-querysecurityaccessmask) functions.



| Value/rights required to query/set                                                                                                                                                                                                     | Meaning                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ATTRIBUTE\_SECURITY\_INFORMATION<br/> Right required to query: **READ\_CONTROL**<br/> Right required to set: **WRITE\_DAC**<br/>                                                                                     | The resource properties of the object being referenced. The resource properties are stored in SYSTEM\_RESOURCE\_ATTRIBUTE\_ACE types in the SACL of the security descriptor.<br/> **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This bit flag is not available.<br/> <br/>                 |
| BACKUP\_SECURITY\_INFORMATION<br/> Right required to query: **READ\_CONTROL** and **ACCESS\_SYSTEM\_SECURITY**<br/> Right required to set: **WRITE\_DAC** and **WRITE\_OWNER** and **ACCESS\_SYSTEM\_SECURITY**<br/> | All parts of the security descriptor. This is useful for backup and restore software that needs to preserve the entire security descriptor.<br/> **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This bit flag is not available.<br/> <br/>                                                  |
| DACL\_SECURITY\_INFORMATION<br/> Right required to query: **READ\_CONTROL**<br/> Right required to set: **WRITE\_DAC**<br/>                                                                                          | The DACL of the object is being referenced.<br/>                                                                                                                                                                                                                                                                                                                        |
| GROUP\_SECURITY\_INFORMATION<br/> Right required to query: **READ\_CONTROL**<br/> Right required to set: **WRITE\_OWNER** <br/>                                                                                      | The primary group identifier of the object is being referenced.<br/>                                                                                                                                                                                                                                                                                                    |
| LABEL\_SECURITY\_INFORMATION<br/> Right required to query: **READ\_CONTROL**<br/> Right required to set: **WRITE\_OWNER** <br/>                                                                                      | The mandatory integrity label is being referenced.<br/> The mandatory integrity label is an ACE in the SACL of the object.<br/> **Windows Server 2003 and Windows XP:** This bit flag is not available.<br/> <br/>                                                                                                                                    |
| OWNER\_SECURITY\_INFORMATION<br/> Right required to query: **READ\_CONTROL**<br/> Right required to set: **WRITE\_OWNER** <br/>                                                                                      | The owner identifier of the object is being referenced.<br/>                                                                                                                                                                                                                                                                                                            |
| PROTECTED\_DACL\_SECURITY\_INFORMATION<br/> Right required to query: Not available<br/> Right required to set: **WRITE\_DAC**<br/>                                                                                   | The DACL cannot inherit [*access control entries*](/windows/desktop/SecGloss/a-gly) (ACEs).<br/>                                                                                                                                                                                                                   |
| PROTECTED\_SACL\_SECURITY\_INFORMATION<br/> Right required to query: Not available<br/> Right required to set: **ACCESS\_SYSTEM\_SECURITY**<br/>                                                                     | The SACL cannot inherit ACEs.<br/>                                                                                                                                                                                                                                                                                                                                      |
| SACL\_SECURITY\_INFORMATION<br/> Right required to query: **ACCESS\_SYSTEM\_SECURITY**<br/> Right required to set: **ACCESS\_SYSTEM\_SECURITY**<br/>                                                                 | The SACL of the object is being referenced.<br/>                                                                                                                                                                                                                                                                                                                        |
| SCOPE\_SECURITY\_INFORMATION<br/> Right required to query: **READ\_CONTROL**<br/> Right required to set: **ACCESS\_SYSTEM\_SECURITY**<br/>                                                                           | The Central Access Policy (CAP) identifier applicable on the object that is being referenced. Each CAP identifier is stored in a SYSTEM\_SCOPED\_POLICY\_ID\_ACE type in the SACL of the SD.<br/> **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This bit flag is not available.<br/> <br/> |
| UNPROTECTED\_DACL\_SECURITY\_INFORMATION<br/> Right required to query: Not available<br/> Right required to set: **WRITE\_DAC**<br/>                                                                                 | The DACL inherits ACEs from the parent object.<br/>                                                                                                                                                                                                                                                                                                                     |
| UNPROTECTED\_SACL\_SECURITY\_INFORMATION<br/> Right required to query: Not available<br/> Right required to set: **ACCESS\_SYSTEM\_SECURITY**<br/>                                                                   | The SACL inherits ACEs from the parent object.<br/>                                                                                                                                                                                                                                                                                                                     |



 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Winnt.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Access Control](access-control.md)
</dt> <dt>

[Basic Access Control Structures](authorization-structures.md)
</dt> <dt>

[**ConvertSecurityDescriptorToStringSecurityDescriptor**](/windows/desktop/api/Sddl/nf-sddl-convertsecuritydescriptortostringsecuritydescriptora)
</dt> <dt>

[**ConvertStringSecurityDescriptorToSecurityDescriptor**](/windows/desktop/api/Sddl/nf-sddl-convertstringsecuritydescriptortosecuritydescriptora)
</dt> <dt>

[**GetFileSecurity**](/windows/desktop/api/Winbase/nf-winbase-getfilesecuritya)
</dt> <dt>

[**GetKernelObjectSecurity**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getkernelobjectsecurity)
</dt> <dt>

[**GetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getnamedsecurityinfoa)
</dt> <dt>

[**GetPrivateObjectSecurity**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getprivateobjectsecurity)
</dt> <dt>

[**GetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-getsecurityinfo)
</dt> <dt>

[**GetUserObjectSecurity**](/windows/desktop/api/Winuser/nf-winuser-getuserobjectsecurity)
</dt> <dt>

[**QuerySecurityAccessMask**](/windows/desktop/api/Securitybaseapi/nf-securitybaseapi-querysecurityaccessmask)
</dt> <dt>

[**SetFileSecurity**](/windows/desktop/api/Winbase/nf-winbase-setfilesecuritya)
</dt> <dt>

[**SetKernelObjectSecurity**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setkernelobjectsecurity)
</dt> <dt>

[**SetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setnamedsecurityinfoa)
</dt> <dt>

[**SetPrivateObjectSecurity**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setprivateobjectsecurity)
</dt> <dt>

[**SetSecurityAccessMask**](/windows/desktop/api/Securitybaseapi/nf-securitybaseapi-setsecurityaccessmask)
</dt> <dt>

[**SetSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-setsecurityinfo)
</dt> <dt>

[**SetUserObjectSecurity**](/windows/desktop/api/Winuser/nf-winuser-setuserobjectsecurity)
</dt> <dt>

[**TreeResetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-treeresetnamedsecurityinfoa)
</dt> <dt>

[**TreeSetNamedSecurityInfo**](/windows/desktop/api/Aclapi/nf-aclapi-treesetnamedsecurityinfoa)
</dt> </dl>

 

