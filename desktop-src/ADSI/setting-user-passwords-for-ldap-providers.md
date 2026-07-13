---
title: Setting and Changing User Passwords with the LDAP Provider
description: To a set a user password, use the IADsUser.SetPassword method.
ms.assetid: da3d9861-dd04-406c-9356-db1e4ff0eebc
ms.tgt_platform: multiple
keywords:
- LDAP provider ADSI ,user object,Setting passwords
ms.topic: concept-article
ms.date: 05/31/2018
---

# Setting and Changing User Passwords with the LDAP Provider

To a set a user password, use the [**IADsUser.SetPassword**](/windows/desktop/api/Iads/nf-iads-iadsuser-setpassword) method.

The LDAP provider for Active Directory uses one of three processes to set the password (third-party LDAP directories such as iPlanet do not use this password authentication process). The method may vary according to the network configuration. The set password methods occur in the following order:

-   First, the LDAP provider attempts to use Kerberos. 
-   Second, if Kerberos is unsuccessful, the LDAP provider attempts to establish a Secure LDAP connection. For Secure LDAP to operate successfully, the LDAP server must have the appropriate server authentication certificate installed and the clients running the ADSI code must trust the authority that issued those certificates. Both the server and the client must support at least 128-bit encryption.
-   Third, if the Secure LDAP connection is unsuccessful, the LDAP provider attempts a [**NetUserSetInfo**](/windows/win32/api/lmaccess/nf-lmaccess-netusersetinfo) API call. In previous releases, ADSI called **NetUserSetInfo** in the security context in which the thread was running, and not the security context specified in the call to [**IADsOpenDSObject.OpenDSObject**](/windows/win32/api/Iads/nf-iads-iadsopendsobject-opendsobject) or [**ADsOpenObject**](/windows/win32/api/Adshlp/nf-adshlp-adsopenobject). In later releases, this was changed so that the ADSI LDAP provider would impersonate the user specified in the **OpenDSObject** call when it calls **NetUserSetInfo**.

To change a user password, use the [**IADsUser.ChangePassword**](/windows/win32/api/Iads/nf-iads-iadsuser-changepassword) method. Like [**SetPassword**](/windows/win32/api/Iads/nf-iads-iadsuser-setpassword), this method can use multiple processes to change the password. The change password methods occur in the same order:

-   First, the LDAP provider attempts to use Kerberos.
-   Second, the LDAP provider tries to use Secure LDAP.
-   Third, if the Secure LDAP connection is unsuccessful, the LDAP provider tries a [**NetUserChangePassword**](/windows/win32/api/lmaccess/nf-lmaccess-netuserchangepassword) API call. Like [**SetPassword**](/windows/win32/api/Iads/nf-iads-iadsuser-setpassword), in earlier releases, the ADSI LDAP provider impersonates the user credentials passed using the [**IADsOpenDSObject.OpenDSObject**](/windows/win32/api/Iads/nf-iads-iadsopendsobject-opendsobject) method or the [**ADsOpenObject**](/windows/win32/api/Adshlp/nf-adshlp-adsopenobject) function.

 

 
