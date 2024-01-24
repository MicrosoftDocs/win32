---
description: When a user right-clicks a Shell object such as a file, the Shell displays a shortcut (context) menu.
ms.assetid: 4f46b8c3-1e12-447c-87f4-bbe2c305f77a
title: Verbs and File Associations
ms.topic: article
ms.date: 05/31/2018
---

# Verbs and File Associations

When a user right-clicks a Shell object such as a file, the Shell displays a shortcut (context) menu. This menu contains a list of commands that the user can select to perform various actions on the item. These commands are also known as shortcut menu items or verbs. Shortcut menus can be customized.

This topic is organized as follows:

-   [Introduction to Shortcut Menus for File System Objects](#introduction-to-shortcut-menus-for-file-system-objects)
    -   [Add Commands to a Shortcut Menu](#add-commands-to-a-shortcut-menu)
-   [Shortcut Menu Verbs](#shortcut-menu-verbs)
-   [Stream Non-File System Items and OpenSearch Results.](#stream-non-file-system-items-and-opensearch-results)
-   [Register an Application to Handle Arbitrary File Types](#register-an-application-to-handle-arbitrary-file-types)
-   [Additional Resources](#additional-resources)
-   [Related topics](#related-topics)

## Introduction to Shortcut Menus for File System Objects

Because shortcut menus are often used for file management, the Shell provides a set of default commands, such as **Cut** and **Copy**, that appear on the shortcut menu for any file system object such as a file or a folder.

The following example illustrates a default shortcut menu that displayed by right-clicking **MyFile.xyz-ms**.

![screen shot of the default shortcut menu](images/context-menu/context-filesystemobjects.png)

The reason that a default shortcut menu appears for **MyFile.xyz-ms** is due to the fact that **.xyz-ms** is not a member of a registered file type. In contrast, **.txt** is a registered file type. If you right-click a **.txt** file, then you see a shortcut menu with three additional commands in its upper section: **Print**, **Edit** and **Open with**.

![screen shot of the shortcut menu for a file with a registered file type](images/context-menu/context-registeredfiletype.png)

To extend the shortcut menu for a file type, you must create a registry entry for each command. A more sophisticated approach is to implement a shortcut menu (verb) handler, which allows you to extend the shortcut menu for a file type on a file-by-file basis. For more information, see [Creating Context Menu Handlers](context-menu-handlers.md), and [Context Menu Reference](context-menu-reference.md).

### Add Commands to a Shortcut Menu

A shortcut menu handler is a file type handler that adds commands to an existing shortcut menu. Shortcut menu handlers are associated with a file type, and are called whenever a shortcut menu is displayed for a member of the class. The Shell checks the registry to see if the file type is associated with any shortcut menu handlers. If it is, the Shell queries the handlers for additional shortcut menu items.

## Shortcut Menu Verbs

Each command on the shortcut menu is identified in the registry by its verb. These verbs are the same as those used by [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa) when launching applications programmatically.

A verb is a simple text string that is used by the Shell to identify the associated command. Each verb corresponds to the command string used to launch the command in a console window or batch (.bat) file.

For example, the open verb normally launches a program to open a file. The command string typically looks as follows:


```
"My Program.exe" "%1"
```



If any element of the command string contains or might contain spaces, it must be enclosed in quotation marks. Otherwise, if the element contains a space, it will not parse correctly. For instance, **"My Program.exe"** starts the application properly. If you use **My Program.exe** without quotation marks, then the system attempts to launch **My** with **Program.exe** as its first command line argument. You should always use quotation marks with arguments such as **"%1**" that are expanded to strings by the Shell, because you cannot be certain that the string will not contain a space.

Verbs can also have a display name associated with them, which is displayed on the shortcut menu instead of the verb string itself. For example, the display string for openas is **Open With**. Like normal menu strings, including an ampersand character in the display string allows keyboard selection of the command.

## Stream Non-File System Items and OpenSearch Results.

In Windows 7 and later, there is support of the connection of external sources to the Windows Client via by the [OpenSearch](http://www.opensearch.org/) protocol. This allows users to search a remote data store and view results from within Windows Explorer. The OpenSearch v1.1 standard defines simple file formats that can be used to describe how a client should query the web service for the data store and how the service should return results to be rendered by the client.

You may need to streaming non-file system items to avoid the need to download items in the case of [OpenSearch](http://www.opensearch.org/) results. Federated search feature enables searching items from non-file system locations which support OpenSearch, such as SharePoint and other web services-backed sites, for example. When invoking verbs on these items the system downloads a temporary version of the item and passes it to the verb implementation. Verb implementers are encouraged to avoid the need to download the file by registering the set of URL schemas that the verb supports to stream the items. Verbs do so by using the **SupportedProtocols** registry key.

## Register an Application to Handle Arbitrary File Types

Defining shortcut menu items for a particular file type allows you to specify how the associated application opens a member of the file type. However, applications can also register a separate default procedure to be used when a user attempts to use the application to open a file type that is not associated with the application. You register the default procedure in much the same way you register shortcut menu items. For more detailed information about defining shortcut menu items, see [Creating Context Menu Handlers](context-menu.md).

The default procedure serves two basic purposes. One is to specify how your application should be invoked to open an arbitrary file type. You could, for instance, use a command-line flag to indicate that an unknown file type is being opened. The other purpose is to define the various characteristics of a file type, such as the shortcut menu items and the icon. If a user associates your application with an additional file type, that class will have these characteristics. If the additional file type was previously associated with another application, these characteristics will replace the originals.

To register the default procedure, place the same registry keys you created for your application's ProgID under the application's subkey of **HKEY\_CLASSES\_ROOT\\Applications**. You can also include a **FriendlyAppName** value to provide the system with a friendly name for your application. The application's friendly name may also be extracted from its executable file, but only if the FriendlyAppName value is absent.

The following sample registry entry illustrates a default procedure for **MyProgram.exe** that defines a friendly name and several shortcut menu items. The command strings include the **/a** flag to notify the application that it is opening an arbitrary file type. If you include a **DefaultIcon** subkey, then you should use a generic icon.

```
HKEY_CLASSES_ROOT
   MyProgram.exe
      shell
         open
            command
               (Default) = C:\MyDir\MyProgram.exe /a "%1"
         print
            command
               (Default) = C:\MyDir\MyProgram.exe /a /p "%1"
         printto
            command
               (Default) = C:\MyDir\MyProgram.exe /a /p "%1" "%2"
```

## Additional Resources

-   For additional background, see [Introduction to File Associations](fa-intro.md).
-   For conceptual information about extending the Shell with file type handlers, see [Creating Shell Extension Handlers](handlers.md).

## Related topics

<dl> <dt>

[Best Practices for Shortcut Menu Handlers and Multiple Selection Verbs](verbs-best-practices.md)
</dt> <dt>

[Choosing a Static or Dynamic Verb for your Shortcut Menu](shortcut-choose-method.md)
</dt> <dt>

[Creating Shortcut Menu Handlers](context-menu-handlers.md)
</dt> <dt>

[Customizing a Shortcut Menu Using Dynamic Verbs](shortcut-menu-using-dynamic-verbs.md)
</dt> <dt>

[Shortcut (Context) Menus and Shortcut Menu Handlers](context-menu.md)
</dt> <dt>

[Shortcut Menu Reference](context-menu-reference.md)
</dt> </dl>

 

 



