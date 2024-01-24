---
description: You can use a namespace extension to allow users to browse the contents of a file rather than have it presented as a folder. Extensions of this sort are typically used to display the contents of the members of a file type.
title: How to Display a Rooted View of a File
ms.topic: article
ms.date: 05/31/2018
---

# How to Display a Rooted View of a File

You can use a namespace extension to allow users to browse the contents of a file rather than have it presented as a folder. Extensions of this sort are typically used to display the contents of the members of a [file type](fa-file-types.md). For instance, the members of a file type might contain multiple compressed files or images, organized in a hierarchy. Rather than write an application to allow the user to view the contents of such a file, you can instead write a namespace extension and let Windows Explorer handle the display.

You must use a rooted view in order to have an extension display the contents of a file. The most common way to provide a rooted view of the members of a file type is to define a [shortcut menu verb](context.md) that launches an instance of Explorer.exe. By making this verb the default verb, a double-click will also open a rooted view of the file. You can either define a verb for all members of the file type by [modifying the registry](context.md), or dynamically define verbs on a file-by-file basis by implementing a [shortcut menu handler](context-menu-handlers.md).

## Instructions


The following example illustrates how to use the registry to provide a rooted view of the members of a file type by modifying the registry. The sample registry entry is a modification of one of the examples in [Extending Shortcut Menus](context.md). The registry entries define files with an .myp file name extension as a file type, and use the **browse** verb to launch a rooted view of members of that type.

```
HKEY_CLASSES_ROOT
   .myp
      (Default) = MyProgram.1
   MyProgram.1
      (Default) = MyProgram Application
      Shell
         (Default) = browse
         browse
            command
               (Default) = %SYSTEMROOT%\explorer.exe /e,/root,{Extension CLSID}, "%1"
```

You can use the same verb to programmatically launch a rooted view of a member of the file type by calling the [**ShellExecute**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecutea) function.

## Related topics

<dl> <dt>

[Specifying a Namespace Extension's Location](nse-junction.md)
</dt> <dt>

[How to Open a Rooted View of a Junction Point Through the Registry](how-to-use-a-junction-point-to-open-a-rooted-view.md)
</dt> <dt>

[How to Open a Rooted View of a Junction Point Through a Shortcut File](how-to-use-a-shortcut-file-to-open-a-rooted-view.md)
</dt> <dt>

[**ShellExecute**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecutea)
</dt> </dl>

 

 



