---
title: Extending the Taskpad of a Primary Snap-in
description: This section discusses the specific Steps necessary for an extension snap-in to extend the taskpad of an extendable node type owned by a primary snap-in. For more information about working with snap-ins, see Working with Extension Snap-ins.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0f88a2a2-50b6-4c75-a742-016e3b262b31
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- extending a primary snap-ins taskpad MMC
- primary snap-ins, extending a taskpad
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Extending the Taskpad of a Primary Snap-in

This section discusses the specific Steps necessary for an extension snap-in to extend the taskpad of an extendable node type owned by a primary snap-in. For more information about working with snap-ins, see [Working with Extension Snap-ins](working-with-extension-snap-ins.md).

A primary snap-in registers the extendable node types that it adds to its namespace. An extension snap-in can extend the taskpad of a primary snap-in's node type by adding the appropriate registration code and then implementing the [**IExtendTaskPad**](/windows/win32/Mmc/nn-mmc-iextendtaskpad?branch=master) and [**IEnumTASK**](/windows/win32/Mmc/nn-mmc-ienumtask?branch=master) interfaces. The snap-in extends a node type's taskpad by adding additional tasks to it.

A taskpad extension can optionally support [**IComponentData**](/windows/win32/Mmc/nn-mmc-icomponentdata?branch=master). If it does, it gains two features of namespace extensions:

-   When created, the taskpad extension remains loaded for the duration of the MMC session.
-   The taskpad extension can persist data in the console file by implementing [**IPersistStream**](_com_ipersiststream). For more information, see [Snap-in Persistence Model](snap-in-persistence-model.md).

Be aware that if the extension snap-in must create its own taskpad, rather than use a primary snap-in's taskpad, it should be a namespace extension instead. As a namespace extension, it can add a scope item to a primary snap-in's scope pane and create a taskpad view for that item. For more information about namespace extensions, see [Extending a Primary Snap-in's Namespace](extending-a-primary-snap-ins-namespace.md).

In the following procedure, be aware that {`CLSID`}, {`snapinCLSID`}, and {`nodetypeGUID`} all denote string representations of the specified **CLSID**s and **GUID**s. The strings must begin with an open brace ({) and end with a close brace (}).

**To extend the taskpad of a primary snap-in**

1.  The **CLSID** of each snap-in (extension or stand-alone) must be registered under the **HKEY\_CLASSES\_ROOT\\CLSID** key in the {`CLSID`} subkey as an in-process server DLL. The snap-in must also register a threading model for the snap-in **CLSID**. An apartment threading model is recommended.

    For more information about the **HKEY\_CLASSES\_ROOT\\CLSID** key, see the [CLSID Key](_com_CLSID_Key). For more information and a code example, see [Registering and Unregistering a Snap-in](registering-and-unregistering-a-snap-in.md).

2.  All snap-ins must be registered under the **HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\SnapIns** key in the {`snapinCLSID`} key. For more information about the **SnapIns** key, see [Registering and Unregistering a Snap-in](registering-and-unregistering-a-snap-in.md).
3.  Register the **CLSID** of the extension snap-in under the **HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\NodeTypes\\{*nodetypeGUID*}\\Extensions\\Task** subkey, where *nodetypeGUID* is the node type **GUID** of the node type whose taskpad is extended. For more information about the **NodeTypes** key, see [Registration Requirements for Extension Snap-ins](registration-requirements-for-extension-snap-ins.md).
4.  Implement the [**IExtendTaskPad**](/windows/win32/Mmc/nn-mmc-iextendtaskpad?branch=master) and [**IEnumTASK**](/windows/win32/Mmc/nn-mmc-ienumtask?branch=master) interfaces. The only **IExtendTaskPad** interface methods you must implement are [**EnumTasks**](/windows/win32/Mmc/nf-mmc-iextendtaskpad-enumtasks?branch=master) and [**TaskNotify**](/windows/win32/Mmc/nf-mmc-iextendtaskpad-tasknotify?branch=master). All other methods can return **E\_NOTIMPL**. The extension's **EnumTasks** implementation is used by MMC to get a pointer to the extension's **IEnumTASK** interface. The **TaskNotify** method is used for sending notifications from the taskpad to the extension when one of the extension's tasks is clicked. Be aware that the primary snap-in that owns the scope item that is that displays the taskpad is responsible for loading the taskpad template and setting up the taskpad through its own **IExtendTaskPad** methods.
5.  If the taskpad extension persists data in the console file, the snap-in must implement [**IComponentData**](/windows/win32/Mmc/nn-mmc-icomponentdata?branch=master). As a result of implementing **IComponentData**, when loaded, the taskpad extension remains loaded for the duration of the current MMC session. Also, the extension object must expose the snap-in **IComponentData** and [**IExtendTaskPad**](/windows/win32/Mmc/nn-mmc-iextendtaskpad?branch=master) interfaces.

## Related topics

<dl> <dt>

[Using Taskpads](using-taskpads.md)
</dt> <dt>

[Working with Extension Snap-ins](working-with-extension-snap-ins.md)
</dt> </dl>

 

 




