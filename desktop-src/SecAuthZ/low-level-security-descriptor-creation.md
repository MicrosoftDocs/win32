---
description: Functions for creating a security descriptor and getting and setting the components of a security descriptor.
ms.assetid: d07dab5a-7c06-40c4-aa59-fa0baaaa77e7
title: Low-level Security Descriptor Creation
ms.topic: article
ms.date: 05/31/2018
---

# Low-level Security Descriptor Creation

Low-level access control provides a set of functions for creating a [*security descriptor*](/windows/desktop/SecGloss/s-gly) and getting and setting the components of a security descriptor. The low-level functions for initializing and setting the components of a security descriptor work only with absolute-format security descriptors. The low-level functions for getting the components of a security descriptor work with both [absolute and self-relative security descriptors](absolute-and-self-relative-security-descriptors.md).

The [**InitializeSecurityDescriptor**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-initializesecuritydescriptor) function initializes a [**SECURITY\_DESCRIPTOR**](/windows/desktop/api/Winnt/ns-winnt-security_descriptor) buffer. The initialized security descriptor is in [*absolute*](/windows/desktop/SecGloss/a-gly) format and has no owner, primary group, [*discretionary access control list*](/windows/desktop/SecGloss/d-gly) (DACL), or [*system access control list*](/windows/desktop/SecGloss/s-gly) (SACL). You can use the following low-level functions to get or set specific components of a specified security descriptor.



| Function                                                             | Description                                                                                                                                                               |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetSecurityDescriptorControl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorcontrol) | Retrieves revision and control information from a security descriptor.                                                                                                    |
| [**GetSecurityDescriptorDacl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptordacl)       | Retrieves the DACL from a security descriptor.                                                                                                                            |
| [**GetSecurityDescriptorGroup**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorgroup)     | Retrieves the primary group [*security identifier*](/windows/desktop/SecGloss/s-gly) (SID) from a security descriptor. |
| [**GetSecurityDescriptorLength**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorlength)   | Returns the length of a security descriptor.                                                                                                                              |
| [**GetSecurityDescriptorOwner**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorowner)     | Retrieves the owner SID from a security descriptor.                                                                                                                       |
| [**GetSecurityDescriptorSacl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorsacl)       | Retrieves the SACL from a security descriptor.                                                                                                                            |
| [**SetSecurityDescriptorDacl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptordacl)       | Puts a DACL into a security descriptor, superseding any existing DACL.                                                                                                    |
| [**SetSecurityDescriptorGroup**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptorgroup)     | Sets the primary group SID of a security descriptor.                                                                                                                      |
| [**SetSecurityDescriptorOwner**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptorowner)     | Sets the owner SID of a security descriptor.                                                                                                                              |
| [**SetSecurityDescriptorSacl**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptorsacl)       | Puts a SACL into a security descriptor, superseding any existing SACL.                                                                                                    |



 

To check the revision level and structural [*integrity*](/windows/desktop/SecGloss/i-gly) of a security descriptor, call the [**IsValidSecurityDescriptor**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-isvalidsecuritydescriptor) function.

 

 
