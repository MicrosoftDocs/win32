---
title: Lightweight Directory Access Protocol
description: The Lightweight Directory Access Protocol (LDAP) is a directory service protocol that runs on a layer above the TCP/IP stack. It provides a mechanism used to connect to, search, and modify Internet directories.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '32bc9909-e476-423c-bbb5-3978234457fd'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
keywords: ["Lightweight Directory Access Protocol LDAP", "LDAP LDAP , Lightweight Directory Access Protocol LDAP , start page LDAP , introduction to LDAP"]
---

# Lightweight Directory Access Protocol

## Purpose

The Lightweight Directory Access Protocol (LDAP) is a directory service protocol that runs on a layer above the TCP/IP stack. It provides a mechanism used to connect to, search, and modify Internet directories.

The LDAP directory service is based on a client-server model. The function of LDAP is to enable access to an existing directory.

The data model (data and namespace) of LDAP is similar to that of the X.500 OSI directory service, but with lower resource requirements. The associated LDAP API simplifies writing Internet directory service applications.

## Where applicable

The LDAP API is applicable to directory management and browser applications that do not have directory service support as their primary function. Conversely, LDAP is neither applicable to creating directories, nor specifying how a directory service operates.

## Developer audience

The LDAP API documentation in the Platform Software Development Kit (SDK) is intended for experienced C and C++ programmers and Internet directory developers.

LDAP supports the C and C++ programming languages.

A familiarity with directory services and the LDAP Client/Server Model are necessary for the development with the LDAP API.

## Run-time requirements

Client applications that use the LDAP API, run on Windows Vista. All platforms must have TCP/IP installed.

Active Directory servers that support client applications using the LDAP API include Windows Server.

## In this section

<dl> <dt>

[About LDAP](about-the-ldap-api.md)
</dt> <dd>

General information about the Lightweight Directory Access Protocol API.

</dd> <dt>

[Using LDAP](using-the-ldap-api-in-a-client-application.md)
</dt> <dd>

Programmer's guide to using the Lightweight Directory Access Protocol API.

</dd> <dt>

[LDAP Reference](ldap-reference.md)
</dt> <dd>

Reference information for LDAP.

</dd> </dl>

## Related topics

<dl> <dt>

[Programming Guide for Active Directory Domain Services](https://msdn.microsoft.com/library/aa362244)
</dt> <dt>

[Programming Guide for Active Directory Lightweight Directory Services](https://msdn.microsoft.com/library/aa705886)
</dt> <dt>

[Programming Guide for Active Directory Service Interfaces](https://msdn.microsoft.com/library/aa772170)
</dt> <dt>

[Programming Guide for Lightweight Directory Access Protocol](lightweight-directory-access-protocol-ldap-api.md)
</dt> <dt>

[System.DirectoryServices Namespace Overview](Http://Go.Microsoft.Com/FWLink/p/?LinkID=83963)
</dt> <dt>

[System.DirectoryServices.ActiveDirectory Namespace Overview](Http://Go.Microsoft.Com/FWLink/p/?LinkID=83968)
</dt> <dt>

[System.DirectoryServices.Protocols Namespace Overview](Http://Go.Microsoft.Com/FWLink/p/?LinkID=83969)
</dt> <dt>

[Programming Guide for Directory Services Markup Language (DSML) Services for Windows](https://msdn.microsoft.com/library/aa813632)
</dt> <dt>

[Directory Services Data Exchange (DSDE) command line utility](https://msdn.microsoft.com/library/aa813598)
</dt> </dl>

 

 




