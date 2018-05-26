---
title: WinNT User Object
description: The WinNT User object represents a user account in a Windows NT 4.0 domain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c57016e2-538b-4f37-a1bb-699fcf3c080d
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- WinNT User Object ADSI
- WinNT provider ADSI , user object
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WinNT User Object

The WinNT User object represents a user account in a Windows NT 4.0 domain. The object exhibits special features. In one instance, it does not support all the property methods of the [**IADsUser**](/windows/win32/Iads/nn-iads-iadsuser?branch=master) interface. In a second instance, it supports some custom properties that can be accessed only with the [**IADs.Get**](/windows/win32/Iads/nf-iads-iads-get?branch=master) or [**IADs.Put**](/windows/win32/Iads/nf-iads-iads-put?branch=master) method.

For more information about WinNT user objects, see:

-   [Unsupported IADsUser Properties](unsupported-iadsuser-properties.md)
-   [WinNT Custom User Properties](winnt-custom-user-properties.md)
-   [WinNT User Account Management Examples](winnt-user-account-management-examples.md)

 

 




