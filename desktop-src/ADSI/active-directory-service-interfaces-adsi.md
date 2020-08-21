---
title: Active Directory Service Interfaces
description: Introduction to Active Directory Services Interfaces, with links to different guides.
ms.assetid: b24f9789-b9f5-49c4-9812-298bae8b28a9
ms.tgt_platform: multiple
keywords:
- ADSI ADSI
- Active Directory Service Interfaces (See ADSI)
- ADSI ADSI ,start page
ms.topic: article
ms.date: 05/31/2018
---

# Active Directory Service Interfaces

## Purpose

Active Directory Service Interfaces (ADSI) is a set of COM interfaces used to access the features of directory services from different network providers. ADSI is used in a distributed computing environment to present a single set of directory service interfaces for managing network resources. Administrators and developers can use ADSI services to enumerate and manage the resources in a directory service, no matter which network environment contains the resource.

ADSI enables common administrative tasks, such as adding new users, managing printers, and locating resources in a distributed computing environment.

> [!Note]  
> The following documentation is for computer programmers. If you are an end-user trying to debug a printing error or home network issue, see the [Microsoft community forums](https://answers.microsoft.com).

 

## Where applicable

Network Administrators can use ADSI to automate common tasks, such as adding users and groups, managing printers, and setting permissions on network resources.

Independent Software Vendors and end-user developers can use ADSI to "directory enable" their products and applications. Services can publish themselves in a directory, clients can use the directory to find the services, and both can use the directory to find and manipulate other objects of interest. Because Active Directory Service Interfaces are independent of the underlying directory service(s), directory-enabled products and applications can operate successfully in multiple network and directory environments.

## Developer audience

You can write ADSI client applications in many languages. For most administrative tasks, ADSI defines interfaces and objects accessible from Automation-compliant languages like Microsoft Visual Basic, Microsoft Visual Basic Scripting Edition (VBScript), and Java to the more performance and efficiency-conscious languages such as C and C++. A good foundation in COM programming is useful to the ADSI programmer.

## Run-time requirements

Active Directory runs on Windows Server domain controllers. However, client applications using ADSI may be written and run on Windows. In addition, developers will want the Platform Software Development Kit (SDK), also available on the MSDN website. To investigate the contents of Active Directory, use the Active Directory Users and Computers MMC snap-in. This snap-in replaces the Adsvw tool that was available for previous versions of Windows.

## In this section

<dl> <dt>

[About ADSI](about-adsi.md)
</dt> <dd>

General information about ADSI.

</dd> <dt>

[Using ADSI](using-adsi.md)
</dt> <dd>

Programmer's Guide to using ADSI.

</dd> <dt>

[ADSI Quick-start Tutorials](adsi-quick-start-tutorials.md)
</dt> <dd>

Using ADSI with Automation to manage directories.

</dd> <dt>

[ADSI Reference](adsi-reference.md)
</dt> <dd>

Documentation of ADSI interfaces and methods.

</dd> </dl>

## Related topics

<dl> <dt>

[The Component Object Model](../com/the-component-object-model.md)
</dt> <dt>

[COM Clients and Servers](../com/com-clients-and-servers.md)
</dt> <dt>

[Active Directory Domain Services](../ad/active-directory-domain-services.md)
</dt> </dl>

 

 