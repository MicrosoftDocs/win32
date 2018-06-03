---
Description: Functions for creating a security descriptor and getting and setting the components of a security descriptor.
ms.assetid: d07dab5a-7c06-40c4-aa59-fa0baaaa77e7
title: Low-level Security Descriptor Creation
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Low-level Security Descriptor Creation

Low-level access control provides a set of functions for creating a [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly) and getting and setting the components of a security descriptor. The low-level functions for initializing and setting the components of a security descriptor work only with absolute-format security descriptors. The low-level functions for getting the components of a security descriptor work with both [absolute and self-relative security descriptors](absolute-and-self-relative-security-descriptors.md).

The [**InitializeSecurityDescriptor**](https://www.bing.com/search?q=**InitializeSecurityDescriptor**) function initializes a [**SECURITY\_DESCRIPTOR**](/windows/desktop/api/Winnt/ns-winnt-_security_descriptor) buffer. The initialized security descriptor is in [*absolute*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-absolute-security-descriptor-gly) format and has no owner, primary group, [*discretionary access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-discretionary-access-control-list-gly) (DACL), or [*system access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-system-access-control-list-gly) (SACL). You can use the following low-level functions to get or set specific components of a specified security descriptor.



| Function                                                             | Description                                                                                                                                                               |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetSecurityDescriptorControl**](https://www.bing.com/search?q=**GetSecurityDescriptorControl**) | Retrieves revision and control information from a security descriptor.                                                                                                    |
| [**GetSecurityDescriptorDacl**](https://www.bing.com/search?q=**GetSecurityDescriptorDacl**)       | Retrieves the DACL from a security descriptor.                                                                                                                            |
| [**GetSecurityDescriptorGroup**](https://www.bing.com/search?q=**GetSecurityDescriptorGroup**)     | Retrieves the primary group [*security identifier*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-identifier-gly) (SID) from a security descriptor. |
| [**GetSecurityDescriptorLength**](https://www.bing.com/search?q=**GetSecurityDescriptorLength**)   | Returns the length of a security descriptor.                                                                                                                              |
| [**GetSecurityDescriptorOwner**](https://www.bing.com/search?q=**GetSecurityDescriptorOwner**)     | Retrieves the owner SID from a security descriptor.                                                                                                                       |
| [**GetSecurityDescriptorSacl**](https://www.bing.com/search?q=**GetSecurityDescriptorSacl**)       | Retrieves the SACL from a security descriptor.                                                                                                                            |
| [**SetSecurityDescriptorDacl**](https://www.bing.com/search?q=**SetSecurityDescriptorDacl**)       | Puts a DACL into a security descriptor, superseding any existing DACL.                                                                                                    |
| [**SetSecurityDescriptorGroup**](https://www.bing.com/search?q=**SetSecurityDescriptorGroup**)     | Sets the primary group SID of a security descriptor.                                                                                                                      |
| [**SetSecurityDescriptorOwner**](https://www.bing.com/search?q=**SetSecurityDescriptorOwner**)     | Sets the owner SID of a security descriptor.                                                                                                                              |
| [**SetSecurityDescriptorSacl**](https://www.bing.com/search?q=**SetSecurityDescriptorSacl**)       | Puts a SACL into a security descriptor, superseding any existing SACL.                                                                                                    |



 

To check the revision level and structural [*integrity*](https://msdn.microsoft.com/library/windows/desktop/ms721588#-security-integrity-gly) of a security descriptor, call the [**IsValidSecurityDescriptor**](https://www.bing.com/search?q=**IsValidSecurityDescriptor**) function.

 

 



