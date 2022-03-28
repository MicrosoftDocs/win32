---
description: This section discusses the creation of shortcut (context) menus, and the implementation of shortcut menu (verb) handlers.
title: Shortcut (Context) Menus and Shortcut Menu Handlers
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 956f3b10-2bc6-4f1f-a6ed-7184f94b545a
topic_type: 
 - kbArticle
---

# Shortcut (Context) Menus and Shortcut Menu Handlers

This section discusses the creation of shortcut (context) menus, and the implementation of shortcut menu (verb) handlers.

This section on file types and file associations is organized as follows:

- [Verbs and File Associations](fa-verbs.md)
- [Choosing a Static or Dynamic Shortcut Menu Method](shortcut-choose-method.md)
- [Best Practices for Shortcut Menu Handlers and Multiple Verbs](verbs-best-practices.md)
- [Creating Shortcut Menu Handlers](context-menu-handlers.md)
- [Creating Static Cascading Menus](creating-static-cascading-menus.md)
- [How to Suppress and Control Verb Visibility](how-to-suppress-and-control-visibility.md)
- [How to Employ the Verb Selection Model](how-to-employ-the-verb-selection-model.md)
- [How to Use Item Attributes](how-to-use-item-attributes.md)- [How to Implement Custom Verbs for Folders through Desktop.ini](how-to-implement-custom-verbs-for-folders-through-desktop-ini.md)
- [Customizing a Shortcut Menu Using Dynamic Verbs](shortcut-menu-using-dynamic-verbs.md)
- [How to Implement the IContextMenu Interface](how-to-implement-the-icontextmenu-interface.md)
- [Shortcut Menu Reference](context-menu-reference.md)

## Additional Resources

For related conceptual background, see the following topics:

- [Introduction to File Associations](fa-intro.md).
- To extend the Shell with file type handlers, see [Creating Shell Extension Handlers](handlers.md).
- To create a Shell data store, see [Implementing the Basic Folder Object Interfaces](nse-implement.md).

For related reference documenation, see the following topics:

- To execute a verb on a Shell item, see the [**InvokeVerb**](folderitem-invokeverb.md) method.
- To retrieve a collection of verbs that can be executed on a Shell item, see the [**Verbs**](folderitem-verbs.md) method.
- To perform an operation on a specified file, see either the [**ShellExecute**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecutea) or [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa) functions.