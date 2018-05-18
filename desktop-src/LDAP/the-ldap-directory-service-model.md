---
title: The LDAP Directory Service Model
description: The LDAP directory service is based on a client-server model.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'b03bde36-ab68-454b-b4ae-c0faafc2e818'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
---

# The LDAP Directory Service Model

The LDAP directory service is based on a client-server model. One or more LDAP servers contain the data making up the LDAP directory tree. An LDAP client connects to an LDAP server and requests information or performs an operation. The server performs the operation or provides the information, or refers the client to another LDAP server that may be able to provide the information. Regardless of the LDAP server to which a client connects, the client sees the same view of the directory; a name presented to one LDAP server references the same entry the name would at another LDAP server. This is an important feature of a global directory service such as LDAP.

It is important to remember that LDAP is designed to allow speedy and efficient access to an existing directory. Its streamlined (lightweight) design prevents it from being able to create a directory or specify how the directory service itself operates.

This section covers the following topics:

-   [What is a Directory Service?](what-is-a-directory-service.md)
-   [Directory Entries](directory-entries.md)
-   [Accessing Directory Information](accessing-directory-information.md)

 

 




