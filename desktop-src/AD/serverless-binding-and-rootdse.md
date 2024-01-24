---
title: Serverless Binding and RootDSE
description: If possible, do not hard-code a server name.
ms.assetid: 24cfd8ce-18e6-42f1-8bc5-2c6dee82d133
ms.tgt_platform: multiple
keywords:
- Serverless Binding and RootDSE AD
- Serverless Binding AD
- RootDSE AD
- Active Directory, Using, Binding, Serverless Binding
ms.topic: article
ms.date: 05/31/2018
---

# Serverless Binding and RootDSE

If possible, do not hard-code a server name. Furthermore, under most circumstances, binding should not be unnecessarily tied to a single server. Active Directory Domain Services support serverless binding, which means that Active Directory can be bound to on the default domain without specifying the name of a domain controller. For ordinary applications, this is typically the domain of the logged-on user. For service applications, this is either the domain of the service logon account or that of the client that the service impersonates.

In LDAP 3.0, rootDSE is defined as the root of the directory data tree on a directory server. The rootDSE is not part of any namespace. The purpose of the rootDSE is to provide data about the directory server. The following is the binding string that is used to bind to rootDSE.


```C++
LDAP://<servername>/rootDSE
```



The &lt;servername&gt; is the DNS name of a server. The &lt;servername&gt; is optional, as shown in the following format.


```C++
LDAP://rootDSE
```



In this case, a default domain controller from the domain that the security context of the calling thread is in will be used. If a domain controller cannot be accessed within the site, the first domain controller that can be found will be used.

The rootDSE is a well-known and reliable location on every directory server to get distinguished names of the domain, schema, and configuration containers, and other data about the server and the contents of its directory data tree. These properties rarely change on a particular server. An application can read these properties at startup and use them throughout the session.

In summary, an application should use serverless binding to bind to the directory on the current domain, use rootDSE to get the distinguished name for a namespace, and use that distinguished name to bind to objects in the namespace.

For more information about attributes supported by rootDSE, see [RootDSE](/windows/desktop/ADSchema/rootdse) in the Active Directory Schema documentation.

For more information and a code example that shows how to use serverless binding and rootDSE, see [Example Code for Getting the Distinguished Name of the Domain](example-code-for-getting-the-distinguished-name-of-the-domain.md).

 

 
