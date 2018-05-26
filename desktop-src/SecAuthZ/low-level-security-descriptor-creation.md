---
Description: Functions for creating a security descriptor and getting and setting the components of a security descriptor.
ms.assetid: d07dab5a-7c06-40c4-aa59-fa0baaaa77e7
title: Low-level Security Descriptor Creation
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Low-level Security Descriptor Creation

Low-level access control provides a set of functions for creating a [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly) and getting and setting the components of a security descriptor. The low-level functions for initializing and setting the components of a security descriptor work only with absolute-format security descriptors. The low-level functions for getting the components of a security descriptor work with both [absolute and self-relative security descriptors](absolute-and-self-relative-security-descriptors.md).

The [**InitializeSecurityDescriptor**](initializesecuritydescriptor.md) function initializes a [**SECURITY\_DESCRIPTOR**](/windows/win32/Winnt/ns-winnt-_security_descriptor?branch=master) buffer. The initialized security descriptor is in [*absolute*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-absolute-security-descriptor-gly) format and has no owner, primary group, [*discretionary access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-discretionary-access-control-list-gly) (DACL), or [*system access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-system-access-control-list-gly) (SACL). You can use the following low-level functions to get or set specific components of a specified security descriptor.



| Function                                                             | Description                                                                                                                                                               |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetSecurityDescriptorControl**](getsecuritydescriptorcontrol.md) | Retrieves revision and control information from a security descriptor.                                                                                                    |
| [**GetSecurityDescriptorDacl**](getsecuritydescriptordacl.md)       | Retrieves the DACL from a security descriptor.                                                                                                                            |
| [**GetSecurityDescriptorGroup**](getsecuritydescriptorgroup.md)     | Retrieves the primary group [*security identifier*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-identifier-gly) (SID) from a security descriptor. |
| [**GetSecurityDescriptorLength**](getsecuritydescriptorlength.md)   | Returns the length of a security descriptor.                                                                                                                              |
| [**GetSecurityDescriptorOwner**](getsecuritydescriptorowner.md)     | Retrieves the owner SID from a security descriptor.                                                                                                                       |
| [**GetSecurityDescriptorSacl**](getsecuritydescriptorsacl.md)       | Retrieves the SACL from a security descriptor.                                                                                                                            |
| [**SetSecurityDescriptorDacl**](setsecuritydescriptordacl.md)       | Puts a DACL into a security descriptor, superseding any existing DACL.                                                                                                    |
| [**SetSecurityDescriptorGroup**](setsecuritydescriptorgroup.md)     | Sets the primary group SID of a security descriptor.                                                                                                                      |
| [**SetSecurityDescriptorOwner**](setsecuritydescriptorowner.md)     | Sets the owner SID of a security descriptor.                                                                                                                              |
| [**SetSecurityDescriptorSacl**](setsecuritydescriptorsacl.md)       | Puts a SACL into a security descriptor, superseding any existing SACL.                                                                                                    |



 

To check the revision level and structural [*integrity*](https://msdn.microsoft.com/library/windows/desktop/ms721588#-security-integrity-gly) of a security descriptor, call the [**IsValidSecurityDescriptor**](isvalidsecuritydescriptor.md) function.

 

 



