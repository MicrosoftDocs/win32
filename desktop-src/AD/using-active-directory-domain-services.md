---
title: Using Active Directory Domain Services
description: This section provides guidelines for writing applications that use or publish data in an Active Directory directory service.
ms.assetid: 2ae20169-08a5-4e15-8430-ea99a917725f
ms.tgt_platform: multiple
keywords:
- Active Directory Active Directory , using
- Active Directory Domain Services Active Directory , using
- Active Directory examples Active Directory
- Active Directory Domain Services examples Active Directory
- examples Active Directory
- Active Directory Active Directory , examples see Active Directory Domain Services examples
ms.topic: article
ms.date: 05/31/2018
---

# Using Active Directory Domain Services

This section provides guidelines for writing applications that use or publish data in an Active Directory directory service.

> [!Note]  
> The following documentation is for computer programmers. If you are trying to resolve an Active Directory home printing error, see the [following suggestion](https://answers.microsoft.com/en-us/windows/forum/all/clicking-find-printer-shows-error-the-active/52bfd961-ff62-4397-b8cf-a0708f0cb3d2) from the Microsoft community pages; if that doesn't help, try these recommendations from [TechNet](https://social.technet.microsoft.com/Forums/windowsserver/d6212275-24d6-4168-830a-9441f861cb76/error-message-when-attempting-to-print-active-directory-domain-service-is-currently-unavailable?forum=winserverprint).

 

Active Directory Domain Services are compliant with Lightweight Directory Access Protocol 3.0, which is defined by RFC 2251 and other RFCs. Any of the following API sets can be used to access Active Directory Domain Services. Each API set has advantages and disadvantages that depend on the programming language, programming environment, and intended method of execution. The majority of the examples in this guide use ADSI, which is supported by languages such as C and C++, as well as automation-compliant languages such as Microsoft Visual Basic and Visual Basic Scripting Edition.

For more information about specific Active Directory Domain Services technologies, see:

-   [Lightweight Directory Access Protocol](/previous-versions/windows/desktop/ldap/lightweight-directory-access-protocol-ldap-api)
-   [Active Directory Service Interfaces](../adsi/active-directory-service-interfaces-adsi.md)
-   [System.DirectoryServices](/dotnet/api/system.directoryservices)

This section discusses the following topics:

-   [Binding to Active Directory Domain Services](binding-to-active-directory-domain-services.md)
-   [Searching in Active Directory Domain Services](searching-in-active-directory-domain-services.md)
-   [Creating and Deleting Objects in Active Directory Domain Services](creating-and-deleting-objects-in-active-directory-domain-services.md)
-   [Moving Objects](moving-objects.md)
-   [Reading and Writing Attributes of Objects in Active Directory Domain Services](reading-and-writing-attributes-of-objects-in-active-directory-domain-services.md)
-   [Controlling Access to Objects in Active Directory Domain Services](controlling-access-to-objects-in-active-directory-domain-services.md)
-   [Extending the Schema](extending-the-schema.md)
-   [Extending the User Interface for Directory Objects](extending-the-user-interface-for-directory-objects.md)
-   [Managing Users](managing-users.md)
-   [Managing Groups](managing-groups.md)
-   [Tracking Changes](tracking-changes.md)
-   [Service Publication](service-publication.md)
-   [Service Logon Accounts](service-logon-accounts.md)
-   [Mutual Authentication Using Kerberos](mutual-authentication-using-kerberos.md)
-   [Backing Up and Restoring Active Directory](backing-up-and-restoring-an-active-directory-server.md)
-   [Storing Dynamic Data](storing-dynamic-data.md)
-   [Application Directory Partitions](application-directory-partitions.md)
-   [Detecting the Operation Mode of a Domain](detecting-the-operation-mode-of-a-domain.md)

 

 
