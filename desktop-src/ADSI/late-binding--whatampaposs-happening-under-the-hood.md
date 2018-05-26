---
title: Late Binding Whats Happening Under the Hood
description: This topic describes how late binding works in ADSI.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: f4ff19fc-d69e-4528-a6e2-2544d9149e8c
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- extensions ADSI ,late binding, whats happening under the hood
- binding AD ,late binding
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Late Binding: What's Happening Under the Hood?

The following list outlines the general process for performing a late bind:

-   Something binds to an ADSI directory object. For example, "LDAP://CN=Jeffsmith,OU=Sales,DC=Fabrikam,DC=COM" binds using COM late binding. This causes ADSI to call the [**QueryInterface**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) method on the **IDispatch** interface.
-   ADSI finds an object in the user class and creates an object that supports the appropriate interfaces, such as [**IADs**](/windows/win32/Iads/nn-iads-iads?branch=master), [**IADsUser**](/windows/win32/Iads/nn-iads-iadsuser?branch=master).
-   ADSI performs a lookup in the registry and finds extension CLSIDs for user. Be aware that ADSI caches this data.
-   Something makes a call to the **MyNewMethod** method. ADSI looks up its dispatch ID and the dispatch IDs for other ADSI extensions. ADSI then finds the extension that serves this call, and calls the [**IADsExtension**](/windows/win32/Iads/nn-iads-iadsextension?branch=master) interface for that extension.
-   The extension executes the function.
-   Now, the client writer invokes the **YourNewMethod** method using the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface for the current extension. The extension's **IDispatch** implementation delegates back to the **IDispatch** for ADSI.
-   The [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) for ADSI again searches for the appropriate extension, or itself, then it calls the appropriate extension using the [**IADsExtension**](/windows/win32/Iads/nn-iads-iadsextension?branch=master) interface for that extension.

 

 




