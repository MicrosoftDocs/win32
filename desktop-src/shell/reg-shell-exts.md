---
description: A Shell extension handler object must be registered before the Shell can use it. This topic is a general discussion of how to register a Shell extension handler.
ms.assetid: e4b98c18-746b-4909-8821-f25de9d15373
title: Registering Shell Extension Handlers
ms.topic: article
ms.date: 05/31/2018
---

# Registering Shell Extension Handlers

A Shell extension handler object must be registered before the Shell can use it. This topic is a general discussion of how to register a Shell extension handler.

Any time you create or change a Shell extension handler, it is important to notify the system that you have made a change. Do so by calling [**SHChangeNotify**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shchangenotify), specifying the **SHCNE\_ASSOCCHANGED** event. If you do not call **SHChangeNotify**, the change might not be recognized until the system is rebooted.

There are some additional factors that apply to Windows 2000 systems. For details, see the [Registering Shell Extension Handlers on Windows 2000 Systems](#registering-shell-extension-handlers) section.

As with all Component Object Model (COM) objects, you must create a GUID for the handler using a tool such as Guidgen.exe, which is provided with the Windows Software Development Kit (SDK). Create a subkey under **HKEY\_CLASSES\_ROOT**\\**CLSID** whose name is the string form of that GUID. Because Shell extension handlers are in-process servers, you also must create an **InprocServer32** subkey under that GUID subkey with the (Default) value set to the path of the handler's DLL. Use the apartment threading model. An example is shown here:

```
HKEY_CLASSES_ROOT
   CLSID
      {00021500-0000-0000-C000-000000000046}
         InprocServer32
            (Default) = %windir%\System32\Example.dll
            ThreadingModel = Apartment
```

Any time the Shell takes an action that can involve a Shell extension handler, it checks the appropriate registry subkey. The subkey under which an extension handler is registered controls when it will be called. For instance, it is a common practice to have a shortcut menu handler called when the Shell displays a shortcut menu for a member of a [file type](fa-file-types.md). In this case, the handler must be registered under the file type's **ProgID** subkey.

This topic discusses the following subjects:

-   [Handler Names](#handler-names)
-   [Predefined Shell Objects](#predefined-shell-objects)
-   [Example of an Extension Handler Registration](#example-of-an-extension-handler-registration)
    -   [Registering Shell Extension Handlers](#registering-shell-extension-handlers)
-   [Related topics](#related-topics)

## Handler Names

To enable a Shell extension handler, create a subkey with the handler subkey name (see below) under the **ShellEx** subkey of either the **ProgID** (for file types) or the Shell object type name (for [predefined\_shell\_objects](handlers.md)).

For example, if you wanted to register a shortcut menu extension handler for MyProgram.1, you begin by creating the following subkey:

```
HKEY_CLASSES_ROOT
   MyProgram.1
      ShellEx
         ContextMenuHandlers
```

For the following handlers, create a subkey underneath the "Handler Subkey name" subkey named as the string version of the class identifier (CLSID) of the Shell extension. Multiple extensions can be registered under the handler subkey name by creating multiple subkeys.



| Handler                 | Interface          | Handler Subkey Name       |
|-------------------------|--------------------|---------------------------|
| Column provider handler | IColumnProvider    | **ColumnHandlers**        |
| Shortcut menu handler   | IContextMenu       | **ContextMenuHandlers**   |
| Copyhook handler        | ICopyHook          | **CopyHookHandlers**      |
| Drag-and-drop handler   | IContextMenu       | **DragDropHandlers**      |
| Property sheet handler  | IShellPropSheetExt | **PropertySheetHandlers** |



 

For the following handlers, the default value of the "Handler Subkey Name" key is the string version of the CLSID of the Shell extension. Only one extension can be registered for these handlers.



| Handler                 | Interface            | Handler Subkey Name                        |
|-------------------------|----------------------|--------------------------------------------|
| Data handler            | IDataObject          | **DataHandler**                            |
| Drop handler            | IDropTarget          | **DropHandler**                            |
| Icon handler            | IExtractIconA/W      | **IconHandler**                            |
| Thumbnail image handler | IThumbnailProvider   | **{E357FCCD-A995-4576-B01F-234630154E96}** |
| Infotip handler         | IQueryInfo           | **{00021500-0000-0000-C000-000000000046}** |
| Shell link (ANSI)       | IShellLinkA          | **{000214EE-0000-0000-C000-000000000046}** |
| Shell link (UNICODE)    | IShellLinkW          | **{000214F9-0000-0000-C000-000000000046}** |
| Structured storage      | IStorage             | **{0000000B-0000-0000-C000-000000000046}** |
| Metadata                | IPropertySetStorage  | **PropertyHandler**                        |
| Pin to Start Menu       | IStartMenuPinnedList | **{a2a9545d-a0c2-42b4-9708-a0b2badd77c8}** |
| Pin to Taskbar          |                      | **{90AA3A4E-1CBA-4233-B8BB-535773D48449}** |



 

The subkeys specified to add **Pin to Start Menu** and **Pin to Taskbar** to an item's shortcut menu are only required for file types that include the [IsShortCut](./links.md) entry.

## Predefined Shell Objects

The Shell defines additional objects under **HKEY\_CLASSES\_ROOT** which can be extended in the same way as file types. For example, to add a property sheet handler for all files, you can register under the **PropertySheetHandlers** subkey.

```
HKEY_CLASSES_ROOT
   *
      shellex
         PropertySheetHandlers
```

The following table gives the various subkeys of **HKEY\_CLASSES\_ROOT** under which extension handlers can be registered. Note that many extension handlers cannot be registered under all of the listed subkeys. For further details, see the specific handler's documentation.



| Subkey                    | Description                                                          | Possible Handlers                                |
|---------------------------|----------------------------------------------------------------------|--------------------------------------------------|
| **\***                    | All files                                                            | Shortcut Menu, Property Sheet, Verbs (see below) |
| **AllFileSystemObjects**  | All files and file folders                                           | Shortcut Menu, Property Sheet, Verbs             |
| **Folder**                | All folders                                                          | Shortcut Menu, Property Sheet, Verbs             |
| **Directory**             | File folders                                                         | Shortcut Menu, Property Sheet, Verbs             |
| **Directory\\Background** | File folder background                                               | Shortcut Menu only                               |
| **DesktopBackground**     | Desktop background (Windows 7 and higher)                            | Shortcut Menu, Verbs                             |
| **Drive**                 | All drives in MyComputer, such as "C:\\"                             | Shortcut Menu, Property Sheet, Verbs             |
| **Network**               | Entire network (under My Network Places)                             | Shortcut Menu, Property Sheet, Verbs             |
| **Network\\Type\\\#**     | All objects of type \# (see below)                                   | Shortcut Menu, Property Sheet, Verbs             |
| **NetShare**              | All network shares                                                   | Shortcut Menu, Property Sheet, Verbs             |
| **NetServer**             | All network servers                                                  | Shortcut Menu, Property Sheet, Verbs             |
| *network\_provider\_name* | All objects provided by network provider "*network\_provider\_name*" | Shortcut Menu, Property Sheet, Verbs             |
| **Printers**              | All printers                                                         | Shortcut Menu, Property Sheet                    |
| **AudioCD**               | Audio CD in CD drive                                                 | Verbs only                                       |
| **DVD**                   | DVD drive (Windows 2000)                                             | Shortcut Menu, Property Sheet, Verbs             |



 

### Notes

-   The file folder background shortcut menu is accessed by right-clicking within a file folder, but not over any of the folder's contents.
-   "Verbs" are special commands registered under **HKEY\_CLASSES\_ROOT**\\*Subkey*\\**Shell**\\**Verb**.
-   For **Network**\\**Type**\\**\#**, "\#" is a network provider type code in decimal. The network provider type code is the high word of a network type. The list of network types is given in the Winnetwk.h header file (WNNC\_NET\_\* values). For example, WNNC\_NET\_SHIVA is 0x00330000, so the corresponding type subkey would be **HKEY\_CLASSES\_ROOT**\\**Network**\\**Type**\\**51**.
-   "*network\_provider\_name*" is a network provider name as specified by [**WNetGetProviderName**](/windows/win32/api/winnetwk/nf-winnetwk-wnetgetprovidernamea), with the spaces converted into underscores. For example, if the Microsoft Networking network provider is installed, its provider name is "Microsoft Windows Network", and the corresponding *network\_provider\_name* is **Microsoft\_Windows\_Network**.

## Example of an Extension Handler Registration

To enable a particular handler, create a subkey under the extension handler type subkey with the name of the handler. The Shell does not use the handler's name, but it must be different from all other names under that type subkey. Set the default value of the name subkey to the string form of the handler's GUID.

The following example illustrates registry entries that enable shortcut menu and property sheet extension handlers, using an example .myp file type.

```
HKEY_CLASSES_ROOT
   .myp
      (Default) = MyProgram.1
   CLSID
      {00000000-1111-2222-3333-444444444444}
         InProcServer32
            (Default) = C:\MyDir\MyCommand.dll
            ThreadingModel = Apartment
      {11111111-2222-3333-4444-555555555555}
         InProcServer32
            (Default) = C:\MyDir\MyPropSheet.dll
            ThreadingModel = Apartment
   MyProgram.1
      (Default) = MyProgram Application
      Shellex
         ContextMenuHandler
            MyCommand
               (Default) = {00000000-1111-2222-3333-444444444444}
         PropertySheetHandlers
            MyPropSheet
               (Default) = {11111111-2222-3333-4444-555555555555}
```

### Registering Shell Extension Handlers

The registration procedure discussed in this section must be followed for all Windows systems. However, with later systems, an additional step might be necessary. Because these later versions of Windows are designed to be used in a managed environment, access to the registry could be administratively restricted, requiring a somewhat different approach to installation than described in the previous section.

> [!Note]  
> Setup programs should generally not write directly to the registry. Instead, setup should be accomplished with Windows Installer packages. These tools ensure that software runs well and provides access to capabilities such as per-user class registration.

 

Shell extension handlers run in the Shell process. Because it is a system process, the administrator of a system can limit Shell extension handlers to those on an approved list by setting the EnforceShellExtensionSecurity value of the **Explorer** key to 1 as shown here:

```
HKEY_CURRENT_USER
   Software
      Microsoft
         Windows
            CurrentVersion
               Policies
                  Explorer
                     EnforceShellExtensionSecurity = 1
```

To place a Shell extension handler on the approved list, create a **REG\_SZ** value whose name is the string form of the handler's GUID under the **Approved** subkey.

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Windows
            CurrentVersion
               Shell Extensions
                  Approved
```

For example, the following example adds the *MyCommand* and *MyPropSheet* handlers to the approved list.

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Windows
            CurrentVersion
               Shell Extensions
                  Approved
                     {00000000-1111-2222-3333-444444444444} = MyCommand
                     {11111111-2222-3333-4444-555555555555} = MyPropSheet
```

The Shell does not use the value that is assigned to the GUID, but it should be set to make inspecting the registry easier.

Your setup application can add values to the **Approved** subkey only if the person installing the application has sufficient privileges. If the attempt to add an extension handler fails, you should inform the user that administrative privileges are required to fully install the application. If the handler is essential to the application, you should fail the setup and notify the user to contact an administrator.

## Related topics

<dl> <dt>

[Initializing Shell Extension Handlers](int-shell-exts.md)
</dt> </dl>

 

 
