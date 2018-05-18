---
Description: 'Another option for adding verbs to a cascading menu is through IExplorerCommand::EnumSubCommands.'
ms.assetid: '010157F3-B950-4A57-B0AA-248B4990DA34'
title: How to Create Cascading Menus with the IExplorerCommand Interface
---

# How to Create Cascading Menus with the IExplorerCommand Interface

Another option for adding verbs to a cascading menu is through [**IExplorerCommand::EnumSubCommands**](iexplorercommand-enumsubcommands.md). This method enables data sources that provide their command module commands through the [**IExplorerCommandProvider**](iexplorercommandprovider.md) interface to use those commands as verbs on a shortcut menu. In Windows 7 and later, you can provide the same verb implementation using the [**IExplorerCommand**](iexplorercommand.md) interface as you can with the [**IContextMenu**](icontextmenu.md) interface.

## Instructions

### 

The following two screen shots illustrate the use of cascading menus in the **Devices** folder.

![screen shot showing an example of a cascading menu in the devices folder](images/file-assoc/filecascademenu.png)

![screen shot showing an example of a cascading menu in the devices folder](images/file-assoc/cascadedevices2.png)

## Remarks

> [!Note]  
> Because [**IExplorerCommand**](iexplorercommand.md) supports in-process activation only, it is recommended for use by Shell data sources that need to share the implementation between commands and shortcut menus.

 

## Related topics

<dl> <dt>

[**IExplorerCommand**](iexplorercommand.md)
</dt> <dt>

[**IExplorerCommandProvider**](iexplorercommandprovider.md)
</dt> <dt>

[**IContextMenu**](icontextmenu.md)
</dt> </dl>

 

 



