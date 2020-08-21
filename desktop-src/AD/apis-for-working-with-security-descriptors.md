---
title: APIs for Working with Security Descriptors
description: APIs for Working with Security Descriptors
ms.assetid: eb5ee183-949c-41f5-9f74-f9c418fdf0a2
ms.tgt_platform: multiple
keywords:
- security descriptors AD
ms.topic: article
ms.date: 05/31/2018
---

# APIs for Working with Security Descriptors

Each object in Active Directory Domain Services has an **nTSecurityDescriptor** attribute that contains the object security descriptor. There are two primary ways to read and manipulate a directory object security descriptor:

-   Use the [**IADs::Get**](/windows/desktop/api/iads/nf-iads-iads-get) method to retrieve the security descriptor as an ADSI COM object with an [**IADsSecurityDescriptor**](/windows/desktop/api/iads/nn-iads-iadssecuritydescriptor) interface. The **IADsSecurityDescriptor**, [**IADsAccessControlList**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrollist), and [**IADsAccessControlEntry**](/windows/desktop/api/iads/nn-iads-iadsaccesscontrolentry) interfaces can be used to handle the security descriptor and its components (ACLs, ACEs, and so on). For more information and a code example, see [Using IADs to Get a Security Descriptor](using-iads-to-get-a-security-descriptor.md).
-   Use the [**IDirectoryObject::GetObjectAttributes**](/windows/desktop/api/iads/nf-iads-idirectoryobject-getobjectattributes) method to retrieve an object security descriptor as a pointer to a [**SECURITY\_DESCRIPTOR**](/windows/desktop/api/winnt/ns-winnt-security_descriptor) structure. Use this pointer with a Win32 access-control function, such as [**AccessCheck**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-accesscheck) or [**BuildSecurityDescriptor**](/windows/desktop/api/aclapi/nf-aclapi-buildsecuritydescriptora). For more information and a code example, see [Using IDirectoryObject to Get a Security Descriptor](using-idirectoryobject-to-get-a-security-descriptor.md).

The recommended technique, and the one used by most of the code examples in this guide, is to use the **IADs\*** interfaces because they simplify handling security descriptors, ACLs, and ACEs. For Visual Basic programmers, the **IADs\*** interfaces are the most efficient way to handle security descriptors.

The [**IDirectoryObject**](/windows/desktop/api/iads/nn-iads-idirectoryobject) technique is useful when a [**SECURITY\_DESCRIPTOR**](/windows/desktop/api/winnt/ns-winnt-security_descriptor) structure is required. For example, the code example in [Checking a Control Access Right in an Object's ACL](checking-a-control-access-right-in-an-objectampaposs-acl.md) uses this method to retrieve a security descriptor to pass to the [**AccessCheckByTypeResultList**](/windows/desktop/api/securitybaseapi/nf-securitybaseapi-accesscheckbytyperesultlist) function.

For more information, see:

-   [Using IADs to Get a Security Descriptor](using-iads-to-get-a-security-descriptor.md)
-   [Using IDirectoryObject to Get a Security Descriptor](using-idirectoryobject-to-get-a-security-descriptor.md)
-   [Security Descriptor Components](security-descriptor-components.md)
-   [Retrieving an Object's DACL](retrieving-an-objectampaposs-dacl.md)
-   [Retrieving an Object's SACL](retrieving-an-objectampaposs-sacl.md)
-   [Reading an Object's Security Descriptor](reading-an-objectampaposs-security-descriptor.md)
-   [Example Code for Creating a Security Descriptor](example-code-for-creating-a-security-descriptor.md)
-   [Example Code for Enumerating the ACL of an Object in Active Directory Domain Services](example-code-for-enumerating-the-acl-of-an-active-directory-object.md)

 

 