---
Description: Identifies the object-related security information being set or queried.
ms.assetid: e3e8b35d-9d18-4611-a898-72ca13e40d33
title: SECURITY\_INFORMATION
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SECURITY\_INFORMATION

The **SECURITY\_INFORMATION** data type identifies the object-related security information being set or queried. This security information includes:

-   The owner of an object
-   The primary group of an object
-   The [*discretionary access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-discretionary-access-control-list-gly) (DACL) of an object
-   The [*system access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-system-access-control-list-gly) (SACL) of an object


```C++
typedef DWORD SECURITY_INFORMATION, *PSECURITY_INFORMATION;
```



## Remarks

Some **SECURITY\_INFORMATION** members work only with the [**SetNamedSecurityInfo**](/windows/win32/Aclapi/nf-aclapi-setnamedsecurityinfoa?branch=master) function. These members are not returned in the structure returned by other security functions such as [**GetNamedSecurityInfo**](/windows/win32/Aclapi/nf-aclapi-getnamedsecurityinfoa?branch=master) or [**ConvertStringSecurityDescriptorToSecurityDescriptor**](/windows/win32/Sddl/nf-sddl-convertstringsecuritydescriptortosecuritydescriptora?branch=master).

Each item of security information is designated by a bit flag. Each bit flag can be one of the following values. For more information, see the [**SetSecurityAccessMask**](/windows/win32/Securitybaseapi/nf-securitybaseapi-setsecurityaccessmask?branch=master) and [**QuerySecurityAccessMask**](/windows/win32/Securitybaseapi/nf-securitybaseapi-querysecurityaccessmask?branch=master) functions.



| Value/rights required to query/set                                                                                                                                                                                                     | Meaning                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ATTRIBUTE\_SECURITY\_INFORMATION<br/> Right required to query: **READ\_CONTROL**<br/> Right required to set: **WRITE\_DAC**<br/>                                                                                     | The resource properties of the object being referenced. The resource properties are stored in SYSTEM\_RESOURCE\_ATTRIBUTE\_ACE types in the SACL of the security descriptor.<br/> **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This bit flag is not available.<br/> <br/>                 |
| BACKUP\_SECURITY\_INFORMATION<br/> Right required to query: **READ\_CONTROL** and **ACCESS\_SYSTEM\_SECURITY**<br/> Right required to set: **WRITE\_DAC** and **WRITE\_OWNER** and **ACCESS\_SYSTEM\_SECURITY**<br/> | All parts of the security descriptor. This is useful for backup and restore software that needs to preserve the entire security descriptor.<br/> **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This bit flag is not available.<br/> <br/>                                                  |
| DACL\_SECURITY\_INFORMATION<br/> Right required to query: **READ\_CONTROL**<br/> Right required to set: **WRITE\_DAC**<br/>                                                                                          | The DACL of the object is being referenced.<br/>                                                                                                                                                                                                                                                                                                                        |
| GROUP\_SECURITY\_INFORMATION<br/> Right required to query: **READ\_CONTROL**<br/> Right required to set: **WRITE\_OWNER** <br/>                                                                                      | The primary group identifier of the object is being referenced.<br/>                                                                                                                                                                                                                                                                                                    |
| LABEL\_SECURITY\_INFORMATION<br/> Right required to query: **READ\_CONTROL**<br/> Right required to set: **WRITE\_OWNER** <br/>                                                                                      | The mandatory integrity label is being referenced.<br/> The mandatory integrity label is an ACE in the SACL of the object.<br/> **Windows Server 2003 and Windows XP:** This bit flag is not available.<br/> <br/>                                                                                                                                    |
| OWNER\_SECURITY\_INFORMATION<br/> Right required to query: **READ\_CONTROL**<br/> Right required to set: **WRITE\_OWNER** <br/>                                                                                      | The owner identifier of the object is being referenced.<br/>                                                                                                                                                                                                                                                                                                            |
| PROTECTED\_DACL\_SECURITY\_INFORMATION<br/> Right required to query: Not available<br/> Right required to set: **WRITE\_DAC**<br/>                                                                                   | The DACL cannot inherit [*access control entries*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-entry-gly) (ACEs).<br/>                                                                                                                                                                                                                   |
| PROTECTED\_SACL\_SECURITY\_INFORMATION<br/> Right required to query: Not available<br/> Right required to set: **ACCESS\_SYSTEM\_SECURITY**<br/>                                                                     | The SACL cannot inherit ACEs.<br/>                                                                                                                                                                                                                                                                                                                                      |
| SACL\_SECURITY\_INFORMATION<br/> Right required to query: **ACCESS\_SYSTEM\_SECURITY**<br/> Right required to set: **ACCESS\_SYSTEM\_SECURITY**<br/>                                                                 | The SACL of the object is being referenced.<br/>                                                                                                                                                                                                                                                                                                                        |
| SCOPE\_SECURITY\_INFORMATION<br/> Right required to query: **READ\_CONTROL**<br/> Right required to set: **ACCESS\_SYSTEM\_SECURITY**<br/>                                                                           | The Central Access Policy (CAP) identifier applicable on the object that is being referenced. Each CAP identifier is stored in a SYSTEM\_SCOPED\_POLICY\_ID\_ACE type in the SACL of the SD.<br/> **Windows Server 2008 R2, Windows 7, Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP:** This bit flag is not available.<br/> <br/> |
| UNPROTECTED\_DACL\_SECURITY\_INFORMATION<br/> Right required to query: Not available<br/> Right required to set: **WRITE\_DAC**<br/>                                                                                 | The DACL inherits ACEs from the parent object.<br/>                                                                                                                                                                                                                                                                                                                     |
| UNPROTECTED\_SACL\_SECURITY\_INFORMATION<br/> Right required to query: Not available<br/> Right required to set: **ACCESS\_SYSTEM\_SECURITY**<br/>                                                                   | The SACL inherits ACEs from the parent object.<br/>                                                                                                                                                                                                                                                                                                                     |



 

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Winnt.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Access Control](access-control.md)
</dt> <dt>

[Basic Access Control Structures](authorization-structures.md#basic-access-control-structures)
</dt> <dt>

[**ConvertSecurityDescriptorToStringSecurityDescriptor**](/windows/win32/Sddl/nf-sddl-convertsecuritydescriptortostringsecuritydescriptora?branch=master)
</dt> <dt>

[**ConvertStringSecurityDescriptorToSecurityDescriptor**](/windows/win32/Sddl/nf-sddl-convertstringsecuritydescriptortosecuritydescriptora?branch=master)
</dt> <dt>

[**GetFileSecurity**](/windows/win32/Winbase/nf-winbase-getfilesecuritya?branch=master)
</dt> <dt>

[**GetKernelObjectSecurity**](getkernelobjectsecurity.md)
</dt> <dt>

[**GetNamedSecurityInfo**](/windows/win32/Aclapi/nf-aclapi-getnamedsecurityinfoa?branch=master)
</dt> <dt>

[**GetPrivateObjectSecurity**](getprivateobjectsecurity.md)
</dt> <dt>

[**GetSecurityInfo**](/windows/win32/Aclapi/nf-aclapi-getsecurityinfo?branch=master)
</dt> <dt>

[**GetUserObjectSecurity**](/windows/win32/Winuser/nf-winuser-getuserobjectsecurity?branch=master)
</dt> <dt>

[**QuerySecurityAccessMask**](/windows/win32/Securitybaseapi/nf-securitybaseapi-querysecurityaccessmask?branch=master)
</dt> <dt>

[**SetFileSecurity**](/windows/win32/Winbase/nf-winbase-setfilesecuritya?branch=master)
</dt> <dt>

[**SetKernelObjectSecurity**](setkernelobjectsecurity.md)
</dt> <dt>

[**SetNamedSecurityInfo**](/windows/win32/Aclapi/nf-aclapi-setnamedsecurityinfoa?branch=master)
</dt> <dt>

[**SetPrivateObjectSecurity**](setprivateobjectsecurity.md)
</dt> <dt>

[**SetSecurityAccessMask**](/windows/win32/Securitybaseapi/nf-securitybaseapi-setsecurityaccessmask?branch=master)
</dt> <dt>

[**SetSecurityInfo**](/windows/win32/Aclapi/nf-aclapi-setsecurityinfo?branch=master)
</dt> <dt>

[**SetUserObjectSecurity**](/windows/win32/Winuser/nf-winuser-setuserobjectsecurity?branch=master)
</dt> <dt>

[**TreeResetNamedSecurityInfo**](/windows/win32/Aclapi/nf-aclapi-treeresetnamedsecurityinfoa?branch=master)
</dt> <dt>

[**TreeSetNamedSecurityInfo**](/windows/win32/Aclapi/nf-aclapi-treesetnamedsecurityinfoa?branch=master)
</dt> </dl>

 

 




