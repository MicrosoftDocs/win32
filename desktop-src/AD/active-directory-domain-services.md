---
title: Active Directory Domain Services
description: Microsoft Active Directory Domain Services are the foundation for distributed networks built on Windows 2000 Server, Windows Server 2003 and Microsoft Windows Server 2008 operating systems that use domain controllers.
ms.assetid: 9fc78c72-c59c-4c4d-ace5-00a431645c4b
ms.tgt_platform: multiple
keywords:
- Active Directory Domain Services Active Directory
- Active Directory Active Directory , start page
- Active Directory Domain Services Active Directory , start page
ms.topic: article
ms.date: 05/31/2018
---

# Active Directory Domain Services

## Purpose

Microsoft Active Directory Domain Services are the foundation for distributed networks built on Windows 2000 Server, Windows Server 2003 and Microsoft Windows Server 2008 operating systems that use domain controllers. Active Directory Domain Services provide secure, structured, hierarchical data storage for objects in a network such as users, computers, printers, and services. Active Directory Domain Services provide support for locating and working with these objects.

This guide provides an overview of Active Directory Domain Services and sample code for basic tasks, such as searching for objects and reading properties, to more advanced tasks such as service publication.

Windows 2000 Server and later operating systems provide a user interface for users and administrators to work with the objects and data in Active Directory Domain Services. This guide describes how to extend and customize that user interface. It also describes how to extend Active Directory Domain Services by defining new object classes and attributes.

> [!Note]  
> The following documentation is for computer programmers. If you are an end-user trying to debug a printing error or home network issue, see the [Microsoft community forums](http://answers.microsoft.coms).

 

## Where applicable

Network administrators write scripts and applications that access Active Directory Domain Services to automate common administrative tasks, such as adding users and groups, managing printers, and setting permissions for network resources.

Independent software vendors and end-user developers can use Active Directory Domain Services programming to directory-enable their products and applications. Services can publish themselves in Active Directory Domain Services; clients can use Active Directory Domain Services to find services, and both can use Active Directory Domain Services to locate and work with other objects on a network.

## Developer audience

Applications that access data in Active Directory Domain Services can be written using the [Active Directory Service Interfaces](https://msdn.microsoft.com/library/aa772170) API, [Lightweight Directory Access Protocol](https://msdn.microsoft.com/library/aa367008) API, or the [System.DirectoryServices](https://msdn.microsoft.com/library/9t2667d1.aspx) namespace.

## Run-time requirements

Active Directory Domain Services run on Windows 2000 and later domain controllers. However, client applications can be written for and run on Windows Vista, Windows Server 2003, Windows XP, Windows 2000, Windows NT 4.0, Windows 98, and Windows 95.

## In this section

<dl> <dt>

[About Active Directory Domain Services](about-active-directory-domain-services.md)
</dt> <dd>

General information about Active Directory Domain Services.

</dd> <dt>

[Using Active Directory Domain Services](using-active-directory-domain-services.md)
</dt> <dd>

Active Directory Domain Services programming guide.

</dd> <dt>

[Active Directory Domain Services Reference](active-directory-domain-services-reference.md)
</dt> <dd>

Active Directory Domain Services programming reference.

</dd> </dl>

 

 




