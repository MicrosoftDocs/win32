---
title: About Active Directory Domain Services
description: This guide provides essential information for integrating Microsoft Active Directory in distributed applications designed for operating systems that support Active Directory.
ms.assetid: cc6c63dd-ae22-40a7-8312-0a4648bb92bd
ms.tgt_platform: multiple
keywords:
- Active Directory Active Directory , about
- Active Directory Domain Services Active Directory , about
ms.topic: article
ms.date: 05/31/2018
---

# About Active Directory Domain Services

## Writing Powerful Applications that Use Active Directory Domain Services

This guide provides essential information for integrating Active Directory Domain Services in distributed applications designed for operating systems that support Active Directory Domain Services, including:

-   Windows Server 2008
-   Windows Server 2008 R2
-   Windows Server 2012
-   Windows Server 2012 R2
-   Windows Server 2016

> [!Note]  
> These topics are for software developers. For support issues, see [Microsoft Support](https://windows.microsoft.com/windows/support#1tc). For information about administering Active Directory, see [Active Directory Domain Services](https://technet.microsoft.com/library/cc770946.aspx) at TechNet.

 

## Fundamental Directory Features

A directory service is a fundamental service for distributed applications. A directory service must provide the features listed in the following table.



| Feature               | Description                                                                                         |
|-----------------------|-----------------------------------------------------------------------------------------------------|
| Location transparency | Able to find user, group, networked service, or resource, data without the object address           |
| Object data           | Able to store user, group, organization, and service data in a hierarchical tree                    |
| Rich query            | Able to locate an object by querying for object properties                                          |
| High availability     | Able to locate a replica of the directory at a location that is efficient for read/write operations |



 

## Advanced Features of Active Directory Domain Services

Active Directory Domain Services provides the features listed in the following table.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Feature</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Support for Internet standards</td>
<td>Active Directory Domain Services implements its features in accordance with published Internet standards such as LDAP and DNS.</td>
</tr>
<tr class="even">
<td>Tightly integrated and flexible security</td>
<td>Advantages include:<br/>
<ul>
<li>Choice of authentication packages. Kerberos, Secure Sockets Layer (SSL), or a combination; for example, establish an SSL channel for encryption and then use Kerberos for authentication.</li>
<li>Central management of service and resource access by using the users and groups in Active Directory Domain Services.</li>
<li>Delegation of administration so that central administrators can delegate administrative tasks such as password changing or specific object creation and deletion.</li>
<li>The Active Directory server uses the same access control mechanisms used on file systems in the Windows operating systems. Thus, the same tools that manage access control on a file system work for Active Directory Domain Services.</li>
<li>Comprehensive Public Key infrastructure. The Microsoft Certificate Server and Smart Card support are integrated with Active Directory Domain Services to provide Smart Card logon and Certificate management.</li>
</ul></td>
</tr>
<tr class="odd">
<td>Easily programmable</td>
<td>The Active Directory server can be programmatically accessed and administered using the <a href="https://docs.microsoft.com/windows/desktop/ADSI/active-directory-service-interfaces-adsi">Active Directory Service Interfaces</a> API, <a href="https://docs.microsoft.com/previous-versions/windows/desktop/ldap/lightweight-directory-access-protocol-ldap-api">Lightweight Directory Access Protocol</a> API, or the <a href="https://docs.microsoft.com/dotnet/api/system.directoryservices?redirectedfrom=MSDN">System.DirectoryServices</a> namespace.</td>
</tr>
<tr class="even">
<td>Directory enabled system services</td>
<td>Your client application can be easily deployed to distributed desktops by creating a Windows Installer package and using the application deployment feature available in the Windows operating systems.</td>
</tr>
<tr class="odd">
<td>Key application integration</td>
<td>Key distributed applications, such as Exchange, are integrated with Active Directory Domain Services. Thus, companies can reduce the number of directory services to be managed.</td>
</tr>
<tr class="even">
<td>Rich and extensible schema</td>
<td>The schema defines what objects and properties can be written and read from a directory service. The Active Directory Schema is rich. Most of the objects and properties a service requires are available. If not, a distributed application can extend the schema to support the application requirements.</td>
</tr>
</tbody>
</table>



 

For more information about Active Directory Domain Services, see:

-   [Core Concepts of Active Directory Domain Services](core-concepts-of-active-directory-domain-services.md)
-   [Active Directory Architecture](active-directory-domain-services-architecture.md)
-   [Active Directory Schema](active-directory-schema.md)

 

 





