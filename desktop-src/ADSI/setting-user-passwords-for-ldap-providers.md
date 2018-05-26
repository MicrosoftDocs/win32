---
title: Setting and Changing User Passwords with the LDAP Provider
description: To a set a user password, use the IADsUser.SetPassword method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: da3d9861-dd04-406c-9356-db1e4ff0eebc
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- LDAP provider ADSI ,user object,Setting passwords
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Setting and Changing User Passwords with the LDAP Provider

To a set a user password, use the [**IADsUser.SetPassword**](/windows/win32/Iads/nf-iads-iadsuser-setpassword?branch=master) method.

The LDAP provider for Active Directory uses one of three processes to set the password (third-party LDAP directories such as iPlanet do not use this password authentication process). The method may vary according to the network configuration. The set password methods occur in the following order:

-   First, the LDAP provider attempts to use LDAP over a 128-bit SSL connection. For LDAP SSL to operate successfully, the LDAP server must have the appropriate server authentication certificate installed and the clients running the ADSI code must trust the authority that issued those certificates. Both the server and the client must support 128-bit encryption.
-   Second, if the SSL connection is unsuccessful, the LDAP provider attempts to use Kerberos. On Windows 2000, Kerberos may not support cross-forest authentication. Later enhancements to Kerberos support cross-forest authentication.
-   Third, if Kerberos is unsuccessful, the LDAP provider attempts a [**NetUserSetInfo**](https://msdn.microsoft.com/library/windows/desktop/aa370659) API call. In previous releases, ADSI called **NetUserSetInfo** in the security context in which the thread was running, and not the security context specified in the call to [**IADsOpenDSObject.OpenDSObject**](/windows/win32/Iads/nf-iads-iadsopendsobject-opendsobject?branch=master) or [**ADsOpenObject**](/windows/win32/Adshlp/nf-adshlp-adsopenobject?branch=master). In later releases, this was changed so that the ADSI LDAP provider would impersonate the user specified in the **OpenDSObject** call when it calls **NetUserSetInfo**.

To change a user password, use the [**IADsUser.ChangePassword**](/windows/win32/Iads/nf-iads-iadsuser-changepassword?branch=master) method. Like [**SetPassword**](/windows/win32/Iads/nf-iads-iadsuser-setpassword?branch=master), this method can use multiple processes to change the password. The change password methods occur in the following order:

-   First, the LDAP provider tries to use LDAP over a 128-bit SSL connection.
-   Second, if the 128-SSL connection is unsuccessful, the LDAP provider tries a [**NetUserChangePassword**](https://msdn.microsoft.com/library/windows/desktop/aa370650) API call. Like [**SetPassword**](/windows/win32/Iads/nf-iads-iadsuser-setpassword?branch=master), in earlier releases, the ADSI LDAP provider impersonates the user credentials passed using the [**IADsOpenDSObject.OpenDSObject**](/windows/win32/Iads/nf-iads-iadsopendsobject-opendsobject?branch=master) method or the [**ADsOpenObject**](/windows/win32/Adshlp/nf-adshlp-adsopenobject?branch=master) function.

 

 




