---
description: To create a security descriptor, a protected server can use the same procedure that an application would use to create a security descriptor for a securable object.
ms.assetid: f40c4b62-a3f0-4e66-875e-2ef904d052e5
title: Security Descriptors for Private Objects
ms.topic: article
ms.date: 05/31/2018
---

# Security Descriptors for Private Objects

To create a [*security descriptor*](/windows/desktop/SecGloss/s-gly), a protected server can use the same procedure that an application would use to create a security descriptor for a securable object. For sample code, see [Creating a Security Descriptor for a New Object in C++](creating-a-security-descriptor-for-a-new-object-in-c--.md). Alternatively, a protected server application can call the [**BuildSecurityDescriptor**](/windows/desktop/api/Aclapi/nf-aclapi-buildsecuritydescriptora) function to do this. If a pointer to an existing [*self-relative security descriptor*](/windows/desktop/SecGloss/s-gly) is supplied to **BuildSecurityDescriptor**, it will build the new security descriptor with information taken from that security descriptor merged with new access control information passed as parameters in the function call. The owner and group are optionally specified by [**TRUSTEE**](/windows/desktop/api/AccCtrl/ns-accctrl-trustee_a) structures passed to the function. The security descriptor created by **BuildSecurityDescriptor** is in *self-relative* format.

In addition, the Windows API provides a set of functions for merging client security information with information inherited from the security descriptor for a parent object or from a default security descriptor. The [**CreatePrivateObjectSecurity**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-createprivateobjectsecurity), [**GetPrivateObjectSecurity**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getprivateobjectsecurity), [**SetPrivateObjectSecurity**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setprivateobjectsecurity), and [**DestroyPrivateObjectSecurity**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-destroyprivateobjectsecurity) functions provide the ability to retrieve default information from an [*access token*](/windows/desktop/SecGloss/a-gly), support inheritance, and manipulate specific parts of the security descriptor. This can be useful when a client creates a private object in a hierarchy of secured objects. For example, you could use the **CreatePrivateObjectSecurity** function to create a security descriptor that contained ACEs specified by the client, ACEs inherited from a parent object, and the default owner from the creating client's access token. While [**BuildSecurityDescriptor**](/windows/desktop/api/Aclapi/nf-aclapi-buildsecuritydescriptora) creates security descriptors either from access control information passed into the function call or from an existing security descriptor, **CreatePrivateObjectSecurity** creates a security descriptor solely from the information in existing security descriptors.

[**LookupSecurityDescriptorParts**](/windows/desktop/api/Aclapi/nf-aclapi-lookupsecuritydescriptorpartsa) function obtains security descriptor information from an existing [*self-relative security descriptor*](/windows/desktop/SecGloss/s-gly). This information includes the owner and group specification, the number of ACEs in the SACL or DACL, and the list of ACEs in the SACL or DACL.

 

 
