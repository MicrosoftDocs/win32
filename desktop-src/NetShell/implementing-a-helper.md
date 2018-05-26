---
title: Implementing a Helper
description: Steps to create a NetShell helper.
ms.assetid: 274d9511-361e-4844-a2af-4d463daded2d
keywords:
- helper NetSh , command syntax, implementing
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Implementing a Helper

Developers creating NetShell helpers must take the following steps:

-   Include the Netsh.h file in their application.
-   Export the [**InitHelperDll**](/windows/previous-versions/Netsh/nc-netsh-ns_dll_init_fn?branch=master) function, defined in the [NetShell Reference](netshell-reference.md) section.
-   Register the helper with Windows.

The following sections provide essential information for developers creating NetShell helpers.

 

 




