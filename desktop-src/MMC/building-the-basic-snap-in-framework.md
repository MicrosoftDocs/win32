---
title: Building the Basic Snap-in Framework
description: This section discusses how to build a basic snap-in in C++. You must implement two MMC interfaces and two COM interfaces and write registration and unregistration code for the snap-in.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 701fcbbd-fc0a-4567-b26b-7ce7867d89f3
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- building the basic snap-in framework MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Building the Basic Snap-in Framework

This section discusses how to build a basic snap-in in C++. You must implement two MMC interfaces and two COM interfaces and write registration and unregistration code for the snap-in.

The two MMC-defined COM interfaces you must implement are:

-   [**IComponentData**](/windows/win32/Mmc/nn-mmc-icomponentdata?branch=master)
-   [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master)

The two standard COM interfaces you must implement are:

-   [**IDataObject**](_ole_idataobject)
-   [**IClassFactory**](_com_iclassfactory)

Be aware that this section does not discuss how to add items to a snap-in's scope pane or result pane.

For more information, see:

-   [Working with the Scope Pane](working-with-the-scope-pane.md)
-   [Using Different Result Pane View Types](using-different-result-pane-view-types.md)
-   [Working with Key Interfaces](working-with-key-interfaces.md)
-   [Registering and Unregistering a Snap-in](registering-and-unregistering-a-snap-in.md)

 

 




