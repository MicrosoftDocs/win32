---
description: As of Windows 7, cascading menus are created through the SubCommands registry entry, the ExtendedSubCommandsKey registry entry, or the IExplorerCommand interface.
title: Creating Static Cascading Menus
ms.topic: article
ms.date: 05/31/2018
ms.assetid: E3A6F174-BE53-48EF-AE9B-A3F297E91B95
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Creating Static Cascading Menus

In Windows 7 and later, cascading menu implementation is supported through registry settings. Prior to Windows 7, the creation of cascading menus was possible only through the implementation of the [**IContextMenu**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu) interface. In Windows 7 and later, you should resort to Component Object Model (COM) code-based solutions only when the static methods are insufficient.

The following screen shot provides an example of a cascading menu.

![screen shot showing an example of a cascading menu](images/file-assoc/filecascademenu2ndex.png)

In Windows 7 and later, there are three ways to create cascading menus, which are described in the following sections.

-   [How to Create Cascading Menus with the SubCommands Registry Entry](how-to--create-cascading-menus-with-the-subcommands-registry-entry.md)
-   [How to Create Cascading Menus with the ExtendedSubCommandsKey Registry Entry](how-to-create-cascading-menus-with-the-extendedsubcommandskey-registry-entry.md)
-   [How to Create Cascading Menus with the IExplorerCommand Interface](how-to-create-cascading-menus-with-the-iexplorercommand-interface.md)

 

 
