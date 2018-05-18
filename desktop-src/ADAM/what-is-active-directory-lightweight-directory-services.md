---
title: What Is Active Directory Lightweight Directory Services
description: Active Directory Lightweight Directory Services (AD LDS) is an independent mode of Active Directory, minus infrastructure features, that provides directory services for applications.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '29337b03-f641-4760-88bb-16c48196d88b'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-application-mode'
ms.tgt_platform: multiple
keywords: ["AD LDS ADAM , defined"]
---

# What Is Active Directory Lightweight Directory Services?

Active Directory Lightweight Directory Services (AD LDS) is an independent mode of Active Directory, minus infrastructure features, that provides directory services for applications.

## AD LDS is a mode of Active Directory that provides directory services for applications.

AD LDS provides dedicated directory services for applications. It provides a data store and services for accessing the data store. It uses standard application programming interfaces (APIs) for accessing the application data. The APIs include those of Active Directory, Active Directory Service Interfaces, Lightweight Data Access Protocol, and System.DirectoryServices.

AD LDS operates independently of Active Directory and independently of Active Directory domains or forests. It operates either as a standalone data store, or it operates with replication. Its independence enables local control and autonomy of directory services for specific applications. It also facilitates independent, flexible schemas, and naming contexts.

## AD LDS does not have the infrastructure capabilities of Active Directory.

AD LDS does not include directory services for the Windows operating system, so it concentrates on the requirements of specific applications. If AD LDS operates in an Active Directory environment, it can use Active Directory for authentication. Because AD LDS does not support the Messaging Application Programming Interface, Microsoft Exchange cannot use AD LDS.

## AD LDS usage complements that of Active Directory.

Although AD LDS and Active Directory can operate concurrently within the same network, AD LDS serves the requirements of specific applications. An instance of AD LDS can be created for a specific application without concern for the dependencies required by Active Directory. AD LDS can be installed without affecting Active Directory. Multiple instances of AD LDS, each supporting a separate application, can run on a single AD LDS installation.

 

 




