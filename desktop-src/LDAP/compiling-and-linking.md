---
title: Compiling and Linking
description: To define the LDAP version of an application, call ldap\_set\_option with LDAP\_OPT\_VERSION and the appropriate option value. The default value is LDAP\_VERSION2.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 5a053184-39c0-469f-807a-59366b9b1265
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Compiling and Linking

To define the LDAP version of an application, call [**ldap\_set\_option**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_set_option) with LDAP\_OPT\_VERSION and the appropriate option value. The default value is LDAP\_VERSION2.

The header file Winldap.h contains declarations for the Microsoft implementation of the LDAP API. Include the header file Winsock2.h to add protocol and connection definitions.

Link to the LDAP import library Wldap.dll.

-   DLL: %systemroot%\\system32\\wldap32.dll
-   LIB: wldap32.lib

Ensure that the client application can find the library by:

-   Copying the library to the same folder as the client executable.
-   Copying the library to the system folder. -or-
-   Setting the PATH environment variable.

For more information about error handling, see [Return Values](return-values.md).

 

 




