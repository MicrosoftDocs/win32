---
title: How Access Control Works in Active Directory Domain Services
description: Access control for objects in Active Directory Domain Services is based on Windows NT and Windows 2000 access-control models.
ms.assetid: 70eed84b-ada0-48e7-b448-704586e9afaa
ms.tgt_platform: multiple
keywords:
- Active Directory Domain Services, security, description
ms.topic: article
ms.date: 05/31/2018
---

# How Access Control Works in Active Directory Domain Services

Access control for objects in Active Directory Domain Services is based on Windows NT and Windows 2000 access-control models. For more information and a detailed description of this model and its components such as security descriptors, access tokens, SIDs, ACLs, and ACEs, see [Access Control Model](/windows/desktop/SecAuthZ/access-control-model).

Access privileges for resources in Active Directory Domain Services are usually granted through the use of an access control entry (ACE). An ACE defines an access or audit permission on an object for a specific user or group. An access-control list (ACL) is the ordered collection of access control entries defined for an object. A security descriptor supports properties and methods that create and manage ACLs. For more information about security models, see [Security](/windows/desktop/SecAuthZ/access-control) or the *Windows 2000 Server Resource Kit*. (This resource may not be available in some languages and countries or regions.)

The basic outline of the security model is:

-   Security descriptor. Each directory object has its own security descriptor that contains security data that protects the object. The security descriptor can contain a discretionary access-control list (DACL). A DACL contains a list of ACEs. Each ACE grants or denies a set of access rights to a user or group. The access rights correspond to the operations, such as reading and writing properties, that can be performed on the object.
-   Security context. When a directory object is accessed, the application specifies the credentials of the security principal that is making the access attempt. When authenticated, these credentials determine the application's security context, which includes the group memberships and privileges associated with the security principal. For more information about security contexts, see [Security Contexts and Active Directory Domain Services](security-contexts-and-active-directory-domain-services.md).
-   Access check. The system grants access to an object only if the object's security descriptor grants the necessary access rights to the security principal attempting the operation (or to groups to which the security principal belongs).

The following table lists ADSI interfaces used to manipulate the access control features of Active Directory Domain Services.



| Interface                                                 | Description                                                               |
|-----------------------------------------------------------|---------------------------------------------------------------------------|
| [**IADsSecurityDescriptor**](/windows/desktop/api/iads/nn-iads-iadssecuritydescriptor) | Used to read and write security properties of a directory service object. |
| [**IADsAccessControlList**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrollist)   | Used to manage and enumerate all ACEs for a directory service object.     |
| [**IADsAccessControlEntry**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrolentry) | Used to read and write ACE properties.                                    |



 

 

 