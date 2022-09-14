---
title: Security Contexts and Active Directory Domain Services
description: When an application binds to an Active Directory Domain Controller (DC), it does so in the security context of a security principal, which can be a user or an entity such as a computer or a system service.
ms.assetid: 7ad0acbe-f81b-46d6-be87-3526b0bfbd1b
ms.tgt_platform: multiple
keywords:
- Active Directory Active Directory ,security contexts
- security contexts Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# Security Contexts and Active Directory Domain Services

When an application binds to an Active Directory Domain Controller (DC), it does so in the security context of a security principal, which can be a user or an entity such as a computer or a system service. The security context is the user account that the system uses to enforce security when a thread attempts to access a securable object. This data includes the user security identifier (SID), group memberships, and privileges.

A user establishes a security context by presenting credentials for authentication. If the credentials are authenticated, the system produces an access token that identifies the group memberships and privileges associated with the user account. The system verifies your access token when you attempt to access a directory object. It compares the data in your access token to the accounts and groups granted or denied access by the object security descriptor.

Use the following methods to control the security context with which you bind to an Active Directory DC:

-   Bind using the **ADS\_SECURE\_AUTHENTICATION** option with the [**ADsOpenObject**](/windows/desktop/api/adshlp/nf-adshlp-adsopenobject) function or [**IADsOpenDSObject::OpenDSObject**](/windows/desktop/api/iads/nf-iads-iadsopendsobject-opendsobject) method and explicitly specify a user name and password. The system authenticates these credentials and generates an access token that it uses for access verification for the duration of that binding. For more information, see [Authentication](authentication.md).
-   Bind using the **ADS\_SECURE\_AUTHENTICATION** option, but without specifying credentials. If you are not impersonating a user, the system uses the primary security context of your application, that is, the security context of the user who started your application. In the case of a system service, this is the security context of the service account or the LocalSystem account.
-   Impersonate a user and then bind with **ADS\_SECURE\_AUTHENTICATION**, but without specifying credentials. In this case, the system uses the security context of the client that is impersonated. For more information, see [Client Impersonation](/windows/desktop/SecAuthZ/client-impersonation).
-   Bind using [**ADsOpenObject**](/windows/desktop/api/adshlp/nf-adshlp-adsopenobject) or [**IADsOpenDSObject::OpenDSObject**](/windows/desktop/api/iads/nf-iads-iadsopendsobject-opendsobject) with the **ADS\_NO\_AUTHENTICATION** option. This method binds without authentication and results in "Everyone" as the security context. Only the LDAP provider supports this option.

If possible, bind without specifying credentials. That is, use the security context of the logged-on user or the impersonated client. This enables you to avoid caching credentials. If you must use alternate user credentials, prompt for the credentials, bind with them, but do not cache them. To use the same security context in multiple bind operations, you can specify the user name and password for the first bind operation and then specify only the user name to make subsequent binds. For more information about using this technique, see [Authentication](authentication.md).

Some security contexts are more powerful than others. For example, the LocalSystem account on a domain controller has complete access to Active Directory Domain Services, whereas a typical user has only limited access to a some of the objects in the directory. In general, your application should not run in a powerful security context, such as LocalSystem, when a less powerful security context is sufficient to perform the operations. This means that you may want to divide your application into separate components, each of which runs in a security context appropriate to the operations to perform. For example, your application setup can be divided as follows:

-   Perform schema changes and extensions in the context of a user who is a member of the Schema Administrators group.
-   Perform configuration container changes in the context of a user who is a member of the Enterprise Administrators group.
-   Perform domain container changes in the context of a user who is a member of the Domain Administrators group.

 

 