---
Description: Another option for adding verbs to a cascading menu is through IExplorerCommandEnumSubCommands.
ms.assetid: 010157F3-B950-4A57-B0AA-248B4990DA34
title: How to Create Cascading Menus with the IExplorerCommand Interface
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How to Create Cascading Menus with the IExplorerCommand Interface

Another option for adding verbs to a cascading menu is through [**IExplorerCommand::EnumSubCommands**](/windows/win32/shobjidl_core/nf-shobjidl_core-iexplorercommand-enumsubcommands?branch=master). This method enables data sources that provide their command module commands through the [**IExplorerCommandProvider**](/windows/win32/shobjidl_core/nn-shobjidl_core-iexplorercommandprovider?branch=master) interface to use those commands as verbs on a shortcut menu. In Windows 7 and later, you can provide the same verb implementation using the [**IExplorerCommand**](/windows/win32/shobjidl_core/nn-shobjidl_core-iexplorercommand?branch=master) interface as you can with the [**IContextMenu**](/windows/win32/Shobjidl/nn-shobjidl_core-icontextmenu?branch=master) interface.

## Instructions

### 

The following two screen shots illustrate the use of cascading menus in the **Devices** folder.

![screen shot showing an example of a cascading menu in the devices folder](images/file-assoc/filecascademenu.png)

![screen shot showing an example of a cascading menu in the devices folder](images/file-assoc/cascadedevices2.png)

## Remarks

> [!Note]  
> Because [**IExplorerCommand**](/windows/win32/shobjidl_core/nn-shobjidl_core-iexplorercommand?branch=master) supports in-process activation only, it is recommended for use by Shell data sources that need to share the implementation between commands and shortcut menus.

 

## Related topics

<dl> <dt>

[**IExplorerCommand**](/windows/win32/shobjidl_core/nn-shobjidl_core-iexplorercommand?branch=master)
</dt> <dt>

[**IExplorerCommandProvider**](/windows/win32/shobjidl_core/nn-shobjidl_core-iexplorercommandprovider?branch=master)
</dt> <dt>

[**IContextMenu**](/windows/win32/Shobjidl/nn-shobjidl_core-icontextmenu?branch=master)
</dt> </dl>

 

 



