---
description: The primary responsibility of any Control Panel item is to display a window that allows the user to view and manipulate settings.
title: User Experience Guidelines
ms.topic: article
ms.date: 09/24/2020
ms.assetid: f03a154b-9781-4718-8244-3d57fee0755e
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# User Experience Guidelines

The primary responsibility of any Control Panel item is to display a window that allows the user to view and manipulate settings. See the [Control Panels user experience (UX) guidelines](../uxguide/winenv-ctrl-panels.md) for the behavior and design of Control Panel items. The guidelines discussed in that topic show a task flow method of organizing a Control Panel item. This places the most important settings on a home page. Less frequently used settings are placed on spoke pages or accessed from links in a side pane.

The Control Panel includes many items that follow these guidelines, such as Ease of Access Center and Network and Sharing Center. Other Control Panel items use the tabbed dialog property sheet format as in earlier versions of Windows. Examples include the Mouse item and Internet Options. Use of the property sheet format should be discontinued. If you create new Control Panel items, you should follow the task flow guidelines.

In the past, Control Panel items were packaged as .cpl files. That is no longer necessary. New Control Panel items should be implemented as a standalone .exe file or as a command-line flag option for the application's main executable file.

> [!Note]  
> On 64-bit systems, 32-bit Control Panel items are displayed in the Control Panel when the **View 32-bit Control Panel Items folder** option is selected. The 32-bit items must be located in the %SystemRoot%\\SysWOW64 folder to be displayed. They do not require any further registration.

 

## Related topics

<dl> <dt>

[Control Panel Items](control-panel-applications.md)
</dt> <dt>

[Registering Control Panel Items](registering-control-panel-items.md)
</dt> <dt>

[Using CPLApplet](using-cplapplet.md)
</dt> <dt>

[Control Panel Message Processing](message-processing.md)
</dt> <dt>

[Executing Control Panel Items](executing-control-panel-items.md)
</dt> <dt>

[Extending System Control Panel Items](extending-system-control-panel-items.md)
</dt> <dt>

[Assigning Control Panel Categories](assigning-control-panel-categories.md)
</dt> <dt>

[Creating Searchable Task Links for a Control Panel Item](creating-searchable-task-links.md)
</dt> <dt>

[Accessing the Control Panel in Safe Mode](accessing-the-cp-in-safe-mode-under-vista.md)
</dt> </dl>

 

 



