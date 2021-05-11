---
description: Shortcut menu handlers, also known as context menu handlers or verb handlers, are a type of file type handler. Like all such handlers, they are in-process Component Object Model (COM) objects implemented as DLLs.
ms.assetid: cff79cdc-8a01-4575-9af7-2a485c6a8e46
title: Creating Shortcut Menu Handlers
ms.topic: article
ms.date: 05/31/2018
---

# Creating Shortcut Menu Handlers

Shortcut menu handlers, also known as context menu handlers or verb handlers, are a type of file type handler. These handlers may be impelmented in a way that causes them to load in their own process or in the explorer, or other 3rd party processes. Take care when creating in-process handlers as they can cause harm to the process that loads them.

> [!Note]  
> There are special considerations for 64-bit based versions of Windows when registering handlers that work in the context of 32-bit applications: when invoked in the context of an application of different bitness, the WOW64 subsystem redirects file system access to some paths. If your .exe handler is stored in one of those paths, it is not accessible in this context. Therefore, as a work around, either store your .exe in a path that does not get redirected, or store a stub version of your .exe that launches the real version.

This topic is organized as follows:

-   [Canonical Verbs](#canonical-verbs)
-   [Extended Verbs](#extended-verbs)
-   [Programmatic Access Only Verbs](#programmaticaccessonly-verbs)
-   [Customizing a Shortcut Menu Using Static Verbs](#customizing-a-shortcut-menu-using-static-verbs)
    -   [Activating Your Handler Using the IDropTarget Interface](#activating-your-handler-using-the-idroptarget-interface)
    -   [Specifying the Position and Order of Static Verbs](#specifying-the-position-and-order-of-static-verbs)
    -   [Positioning Verbs at the Top or Bottom of the Menu](#positioning-verbs-at-the-top-or-bottom-of-the-menu)
    -   [Creating Static Cascading Menus](#creating-static-cascading-menus)
    -   [Getting Dynamic Behavior for Static Verbs by Using Advanced Query Syntax](#getting-dynamic-behavior-for-static-verbs-by-using-advanced-query-syntax)
    -   [Deprecated: Associating Verbs with Dynamic Data Exchange Commands](#deprecated-associating-verbs-with-dynamic-data-exchange-commands)
-   [Completing Verb Implementation Tasks](#completing-verb-implementation-tasks)
    -   [Customizing the Shortcut Menu for Predefined Shell Objects](#customizing-the-shortcut-menu-for-predefined-shell-objects)
    -   [Extending a New Submenu](#extending-a-new-submenu)
    -   [Suppressing Verbs and Controlling Visibility](#suppressing-verbs-and-controlling-visibility)
    -   [Employing the Verb Selection Model](#employing-the-verb-selection-model)
    -   [Using Item Attributes](#using-item-attributes)
    -   [Implementing Custom Verbs for Folders through Desktop.ini](#implementing-custom-verbs-for-folders-through-desktopini)
-   [Related topics](#related-topics)

## Canonical Verbs

Applications are generally responsible for providing localized display strings for the verbs they define. However, to provide a degree of language independence, the system defines a standard set of commonly used verbs called canonical verbs. A canonical verb is never displayed to the user, and can be used with any UI language. The system uses the canonical name to automatically generate a properly localized display string. For instance, the open verb's display string is set to **Open** on an English system, and to the German equivalent on a German system.


| Canonical verb | Description                                                          |
|----------------|----------------------------------------------------------------------|
| Open           | Opens the file or folder.                                            |
| Opennew        | Opens the file or folder in a new window.                            |
| Print          | Prints the file.                                                     |
| Printto        | Permits the user to print a file by dragging it to a printer object. |
| Explore        | Opens Windows Explorer with the folder selected.                     |
| Properties     | Opens the object's property sheet.                                   |

> [!Note]  
> The **Printto** verb is also canonical, but it is never displayed. Its inclusion enables the user to print a file by dragging it to a printer object.

Shortcut menu handlers can provide their own canonical verbs through [**IContextMenu::GetCommandString**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-getcommandstring) with **GCS\_VERBW**, or **GCS\_VERBA**. The system will use the canonical verbs as the second parameter (*lpOperation*) passed to [**ShellExecute**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecutea), and is the [**CMINVOKECOMMANDINFO**](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-cminvokecommandinfo).**lpVerb** member passed to the [**IContextMenu::InvokeCommand**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-invokecommand) method.

## Extended Verbs

When the user right-clicks an object, the shortcut menu displays the default verbs. You might want to add and support commands on some shortcut menus that are not displayed on every shortcut menu. For example, you could have commands that are not commonly used or that are intended for experienced users. For this reason, you can also define one or more extended verbs. These verbs are similar to normal verbs, but are distinguished from normal verbs by the way they are registered. To have access to extended verbs, the user must right-click an object while pressing the SHIFT key. When the user does so, the extended verbs are displayed in addition to the default verbs.

You can use the registry to define one or more extended verbs. The associated commands will be displayed only when the user right-clicks an object while also pressing the SHIFT key. To define a verb as extended, add an "extended" **REG\_SZ** value to the verb's subkey. The value should not have any data associated with it.

## Programmatic Access Only

These verbs are never displayed in a context menu. These can be accessed using [**ShellExecute**], specifying the **lpVerb** parameter. To define a verb as programmatic access only, add an "ProgrammaticAccessOnly" **REG\_SZ** value to the verb's subkey. The value should not have any data associated with it.

You can use the registry to define one or more extended verbs. The associated commands will be displayed only when the user right-clicks an object while also pressing the SHIFT key. To define a verb as extended, add an "extended" **REG\_SZ** value to the verb's subkey. The value should not have any data associated with it.

## Customizing a Shortcut Menu Using Static Verbs

After [Choosing a Static or Dynamic Verb for your Shortcut Menu](shortcut-choose-method.md) you can extend the shortcut menu for a file type by registering a static verb for the file type. To do so, add a **Shell** subkey below the subkey for the ProgID of the application associated with the file type. Optionally, you can define a default verb for the file type by making it the default value of the **Shell** subkey.

The default verb is displayed first on the shortcut menu. Its purpose is to provide the Shell with a verb it can use when the [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa) function is called, but no verb is specified. The Shell does not necessarily select the default verb when **ShellExecuteEx** is used in this fashion.

The Shell uses the first available verb in the following order:

1.  The default verb
2.  The first verb in the registry, if the verb order is specified
3.  The **Open** verb
4.  The **Open With** verb

If none of the verbs listed is available, the operation fails.

Create one subkey for each verb you want to add under the Shell subkey. Each of these subkeys must have a **REG\_SZ** value set to the verb's display string (localized string). For each verb subkey, create a command subkey with the default value set to the command line for activating the items. For canonical verbs, such as **Open** and **Print**, you can omit the display string because the system automatically displays a properly localized string. For noncanonical verbs, if you omit the display string, the verb string is displayed.

In the following registry example, note that:

-   Because **Doit** is not a canonical verb, it is assigned a display name, which can be selected by pressing the D key.
-   The **Printto** verb does not appear on the shortcut menu. However, its inclusion in the registry enables the user to print files by dropping them on a printer icon.
-   One subkey is shown for each verb. **%1** represents the file name and **%2** the printer name.

```
HKEY_CLASSES_ROOT
   .myp-ms
      (Default) = MyProgram.1
      MyProgram.1
         (Default) = My Program Application
         Shell
            (Default) = doit
            doit
               (Default) = &Do It
               command
                  (Default) = c:\MyDir\MyProgram.exe /d "%1"
            open
               command
                  (Default) = c:\MyDir\MyProgram.exe /d "%1"
            print
               command
                  (Default) = c:\MyDir\MyProgram.exe /p "%1"
            printto
               command
                  (Default) = c:\MyDir\MyProgram.exe /p "%1" "%2"
```

The following diagram illustrates the extension of the shortcut menu in accordance with the registry entries above. This shortcut menu has **Open**, **Do It**, and **Print** verbs on its menu, with **Do It** as the default verb.

![screen shot of the do it default verb shortcut menu](images/context-menu/context-doitdefaultverb.png)

### Activating Your Handler Using the IDropTarget Interface

Dynamic Data Exchange (DDE) is deprecated; use [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget) instead. **IDropTarget** is more robust and has better activation support because it uses COM activation of the handler. In the case of multiple item selection, **IDropTarget** is not subject to the buffer size restrictions found in both DDE and the [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa). Also, items are passed to the application as a data object that can be converted to an item array by using the [**SHCreateShellItemArrayFromDataObject**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateshellitemarrayfromdataobject) function. Doing so is simpler, and does not lose namespace information as occurs when the item is converted to a path for command-line or DDE protocols.

For more information about [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget) and Shell queries for file association attributes, see [Perceived Types and Application Registration](fa-perceivedtypes.md).

### Specifying the Position and Order of Static Verbs

Normally verbs are ordered on a shortcut menu based on how they are enumerated; enumeration is based first on the order of the association array, and then on the order of the items in the association array, as defined by the sort order of the registry.

Verbs can be ordered by specifying the default value of the Shell subkey for the association entry. This default value can include a single item, which will be displayed at the top position of the shortcut menu, or a list of items separated by spaces or commas. In the latter case, the first item in the list is the default item, and the other verbs are displayed immediately below it in the order specified.

For example, the following registry entry produces shortcut menu verbs in the following order:

1.  Display
2.  Gadgets
3.  Personalization

```
HKEY_CLASSES_ROOT
   DesktopBackground
      Shell
         Display
         Gadgets
         Personalization
```

Similarly, the following registry entry produces shortcut menu verbs in the following order:

1.  Personalization
2.  Gadgets
3.  Display

```
HKEY_CLASSES_ROOT
   DesktopBackground
      Shell = "Personalization,Gadgets"
      Display
```

### Positioning Verbs at the Top or Bottom of the Menu

The following registry attribute can be used to place a verb at the top or bottom of the menu. If there are multiple verbs that specify this attribute then the last one to do so gets priority:

``` syntax
Position=Top | Bottom 
```

### Creating Static Cascading Menus

In Windows 7 and later, cascading menu implementation is supported through registry settings. Prior to Windows 7, the creation of cascading menus was possible only through the implementation of the [**IContextMenu**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu) interface. In Windows 7 and later, you should resort to COM code-based solutions only when the static methods are insufficient.

The following screen shot provides an example of a cascading menu.

![screen shot showing an example of a cascading menu](images/file-assoc/filecascademenu2ndex.png)

In Windows 7 and later, there are three ways to create cascading menus:

-   [Creating Cascading Menus with the SubCommands Registry Entry](#creating-cascading-menus-with-the-subcommands-registry-entry)
-   [Creating Cascading Menus with the ExtendedSubCommandsKey Registry Entry](#creating-cascading-menus-with-the-extendedsubcommandskey-registry-entry)
-   [Creating Cascading Menus with the IExplorerCommand Interface](#creating-cascading-menus-with-the-iexplorercommand-interface)

### Creating Cascading Menus with the SubCommands Registry Entry

In Windows 7 and later, you can use the SubCommands entry to create cascading menus by using the following procedure.

**To create a cascading menu by using the SubCommands entry**

1.  Create a subkey under **HKEY\_CLASSES\_ROOT**\\*ProgID*\\**shell** to represent your cascading menu. In this example, we give this subkey the name *CascadeTest*. Ensure that the default value of the *CascadeTest* subkey is empty, and shown as **(value not set)**.

    ```
    HKEY_CLASSES_ROOT
       *
          shell
             CascadeTest
                (Default)
    ```

2.  To your *CascadeTest* subkey, add a MUIVerb entry of type **REG\_SZ** and assign it the text that will appear as its name on the shortcut menu. In this example, we assign it "Test Cascade Menu".

    ```
    HKEY_CLASSES_ROOT
       *
          shell
             CascadeTest
                (Default)
                MUIVerb = Test Cascade Menu
    ```

3.  To your *CascadeTest* subkey, add a SubCommands entry of type **REG\_SZ** that is assigned list, demlimited by semi-colons, of the verbs that should appear on the menu, in the order of appearance. For example, here we assign a number of system-provided verbs:

    ```
    HKEY_CLASSES_ROOT
       *
          Shell
             CascadeTest
                SubCommands
                Windows.delete;Windows.properties;Windows.rename;Windows.cut;Windows.copy;Windows.paste
    ```

4.  In the case of custom verbs, implement them using any of the static verb implementation methods and list them under the **CommandStore** subkey as shown in this example for a fictional verb *VerbName*:

    ```
    HKEY_LOCAL_MACHINE
       Software
          Microsoft
             Windows
                CurrentVersion
                   Explorer
                      CommandStore
                         Shell
                            VerbName
                            command
                               (Default) = notepad.exe %1
    ```

> [!Note]  
> This method has the advantage that the custom verbs can be registered once and reused by listing the verb name under the SubCommands entry. However, it requires the application to have permission to modify the registry under **HKEY\_LOCAL\_MACHINE**.

 

### Creating Cascading Menus with the ExtendedSubCommandsKey Registry Entry

In Windows 7 and later, you can use the ExtendedSubCommandKey entry to create extended cascading menus: cascading menus within cascading menus.

The following screen shot is an example of an extended cascading menu.

![screen shot showing extended cascading menu for devices](images/file-assoc/extendedsubcommandskey.png)

Because **HKEY\_CLASSES\_ROOT** is a combination of **HKEY\_CURRENT\_USER** and **HKEY\_LOCAL\_MACHINE**, you can register any custom verbs under the **HKEY\_CURRENT\_USER**\\**Software**\\**Classes** subkey. The main advantage of doing so is that elevated permission is not required. Also, other file associations can reuse this entire set of verbs by specifying the same ExtendedSubCommandsKey subkey. If you do not need to reuse this set of verbs, you can list the verbs under the parent, but ensure that the Default value of the parent is empty.

**To create a cascading menu by using an ExtendedSubCommandsKey entry**

1.  Create a subkey under **HKEY\_CLASSES\_ROOT**\\*ProgID*\\**shell** to represent your cascading menu. In this example, we give this subkey the name *CascadeTest2*. Ensure that the default value of the *CascadeTest* subkey is empty, and shown as **(value not set)**.

    ```
    HKEY_CLASSES_ROOT
       *
          shell
             CascadeTest2
                (Default)
    ```

2.  To your *CascadeTest* subkey, add a MUIVerb entry of type **REG\_SZ** and assign it the text that will appear as its name on the shortcut menu. In this example, we assign it "Test Cascade Menu".

    ```
    HKEY_CLASSES_ROOT
       *
          shell
             CascadeTest
                (Default)
                MUIVerb = Test Cascade Menu 2
    ```

3.  Under the *CascadeTest* subkey you have created, add an **ExtendedSubCommandsKey** subkey, and then add the document subcommands (of **REG\_SZ** type); for example:

    ```
    HKEY_CLASSES_ROOT
       txtfile
          Shell
             Test Cascade Menu 2
                (Default)
                ExtendedSubCommandsKey
                   Layout
                   Properties
                   Select all
    ```

    Ensure that the default value of the *Test Cascade Menu 2* subkey is empty, and shown as **(value not set)**.

4.  Populate the subverbs using any of the following static verb implementations. Note that the CommandFlags subkey represents EXPCMDFLAGS values. If you want to add a separator before or after the cascade menu item, use ECF\_SEPARATORBEFORE (0x20) or ECF\_SEPARATORAFTER (0x40). For a description of these Windows 7 and later flags, see [**IExplorerCommand::GetFlags**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iexplorercommand-getflags). ECF\_SEPARATORBEFORE works only for the top level menu items. MUIVerb is of type **REG\_SZ**, and CommandFlags is of type **REG\_DWORD**.

    ```
    HKEY_CLASSES_ROOT
       txtile
          Shell
             Test Cascade Menu 2
                (Default)
                ExtendedSubCommandsKey
                   Shell
                      cmd1
                         MUIVerb = Notepad
                         command
                            (Default) = %SystemRoot%\system32\notepad.exe %1
                      cmd2
                         MUIVerb = Wordpad
                         CommandFlags = 0x20
                         command
                            (Default) = "C:\Program Files\Windows NT\Accessories\wordpad.exe" %1
    ```

The following screen shot is an illustration of the previous registry key entry examples.

![screen shot showing an example of a cascading menu showing choices of notepad and wordpad](images/file-assoc/testcascademenu2.png)

### Creating Cascading Menus with the IExplorerCommand Interface

Another option for adding verbs to a cascading menu is through [**IExplorerCommand::EnumSubCommands**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iexplorercommand-enumsubcommands). This method enables data sources that provide their command module commands through [**IExplorerCommandProvider**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommandprovider) to use those commands as verbs on a shortcut menu. In Windows 7 and later, you can provide the same verb implementation using [**IExplorerCommand**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommand) as you can with [**IContextMenu**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-icontextmenu).

The following two screen shots illustrate the use of cascading menus in the **Devices** folder.

![Screenshot that shows an example of a cascading menu in the devices folder.](images/file-assoc/filecascademenu.png)

The following screen shot illustrates another implementation of a cascading menu in the **Devices** folder.

![screen shot showing an example of a cascading menu in the devices folder](images/file-assoc/cascadedevices2.png)

> [!Note]  
> Because [**IExplorerCommand**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iexplorercommand) supports in-process activation only, it is recommended for use by Shell data sources that need to share the implementation between commands and shortcut menus.

 

### Getting Dynamic Behavior for Static Verbs by Using Advanced Query Syntax

Advanced Query Syntax (AQS) can express a condition that will be evaluated using properties from the item that the verb is being instantiated for. This system works only with fast properties. These are properties that the Shell data source reports as fast by not returning [****SHCOLSTATE\_SLOW****](/windows/win32/api/shtypes/ne-shtypes-shcolstate) from [**IShellFolder2::GetDefaultColumnState**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder2-getdefaultcolumnstate).

Windows 7 and later support canonical values that avoid problems on localized builds. The following canonical syntax is required on localized builds to take advantage of this Windows 7 enhancement.

``` syntax
System.StructuredQueryType.Boolean#True
```

In the following example registry entry:

-   The **AppliesTo** value controls whether the verb is displayed or hidden.
-   The DefaultAppliesTo value controls which verb is the default.
-   The HasLUAShield value controls whether a User Account Control (UAC) shield is displayed.

In this example the **DefaultAppliesTo** value makes this verb the default for any file with the word "exampleText1" in its file name. The **AppliesTo** value enables the verb for any file with "exampleText1" in the name. The **HasLUAShield** value displays the shield for files with "exampleText2" in the name.

```
HKEY_CLASSES_ROOT
   txtile
      shell
         test.verb
            DefaultAppliesTo = System.ItemName:"exampleText1"
            HasLUAShield = System.ItemName:"exampleText2"
            AppliesTo = System.ItemName:"exampleText1"
```

Add the **Command** subkey, and a value:

```
HKEY_CLASSES_ROOT
   txtile
      shell
         test.verb
            Command
               (Default) = %SystemRoot%\system32\notepad.exe %1
```

In the Windows 7 registry, see **HKEY\_CLASSES\_ROOT**\\**drive** as an example of bitlocker verbs that employ the following approach:

-   AppliesTo = System.Volume.BitlockerProtection:=2
-   System.Volume.BitlockerRequiresAdmin:=System.StructuredQueryType.Boolean\#True

For more information about AQS, see [Advanced Query Syntax](../search/-search-3x-advancedquerysyntax.md).

### Deprecated: Associating Verbs with Dynamic Data Exchange Commands

DDE is deprecated; use [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget) instead. DDE is deprecated because it relies on a broadcast window message to discover the DDE server. A DDE server hang stalls the broadcast window message and thus hangs DDE conversations for other applications. It is common for a single stuck application to cause subsequent hangs all across the user's experience.

The [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget) method is more robust and has better activation support because it uses COM activation of the handler. In the case of multiple item selection, **IDropTarget** is not subject to the buffer size restrictions found in both DDE and the [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa). Also, items are passed to the application as a data object that can be converted to an item array by using the [**SHCreateShellItemArrayFromDataObject**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-shcreateshellitemarrayfromdataobject) function. Doing so is simpler, and does not lose namespace information as occurs when the item is converted to a path for command-line or DDE protocols.

For more information about [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget) and Shell queries for file association attributes, see [Perceived Types and Application Registration](fa-perceivedtypes.md).

## Completing Verb Implementation Tasks

The following tasks for implementing verbs are relevant to both static and dynamic verb implementations. For more information on dynamic verbs, see [Customizing a Shortcut Menu Using Dynamic Verbs](shortcut-menu-using-dynamic-verbs.md).

### Customizing the Shortcut Menu for Predefined Shell Objects

Many predefined Shell objects have shortcut menus that can be customized. Register the command in much the same way that you register typical file types, but use the name of the predefined object as the file type name.

A list of predefined objects is in the *Predefined Shell Objects* section of [Creating Shell Extension Handlers](handlers.md). Those predefined Shell objects whose shortcut menus can be customized by adding verbs in the registry are marked in the table with the word Verb.

### Extending a New Submenu

When a user opens the **File** menu in Windows Explorer, one of the commands displayed is **New**. Selecting this command displays a submenu. By default, the submenu contains two commands, **Folder** and **Shortcut**, that enable users to create subfolders and shortcuts. This submenu can be extended to include file creation commands for any file type.

To add a file-creation command to the **New** submenu, your application's files must have an associated file type. Include a **ShellNew** subkey under the file name. When the **File** menu's **New** command is selected, the Shell adds the file type to the **New** submenu. The command's display string is the descriptive string that is assigned to the program's ProgID.

To specify the file creation method, assign one or more data values to the **ShellNew** subkey. The available values are listed in the following table.



| ShellNew subkey value | Description                                                                                                                                                              |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Command               | Executes an application. This **REG\_SZ** value specifies the path of the application to be executed. For example, you could set it to launch a wizard.                  |
| Data                  | Creates a file containing specified data. This **REG\_BINARY** value specifies the file's data. **Data** is ignored if either **NullFile** or **FileName** is specified. |
| FileName              | Creates a file that is a copy of a specified file. This **REG\_SZ** value specifies the fully qualified path of the file to be copied.                                   |
| NullFile              | Creates an empty file. **NullFile** has no assigned a value. If **NullFile** is specified, the **Data** and **FileName** registry values are ignored.                    |



 

The following registry key example and screen shot illustrate the **New** submenu for the .myp-ms file type. It has a command, **MyProgram Application**.

```
HKEY_CLASSES_ROOT
   .myp
      (Default) = MyProgram.1
      MyProgram.1
         ShellNew
         NullFile
```

The screen shot illustrates the **New** submenu. When a user selects **MyProgram Application** from the **New** submenu, the Shell creates a file named **New MyProgram Application.myp-ms** and passes it to **MyProgram.exe**.

![screen shot of windows explorer showing a new "myprogram application" command on the "new" submenu](images/context-menu/context-myprogramexe.png)

### Creating Drag-and-Drop Handlers

The basic procedure for implementing a drag-and-drop handler is the same as for conventional shortcut menu handlers. However, shortcut menu handlers normally use only the [**IDataObject**](/windows/win32/api/objidl/nn-objidl-idataobject) pointer passed to the handler's [**IShellExtInit::Initialize**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellextinit-initialize) method to extract the object's name. A drag-and-drop handler could implement a more sophisticated data handler to modify the behavior of the dragged object.

When a user right-clicks a Shell object to drag an object, a shortcut menu is displayed when the user attempts to drop the object. The following screen shot illustrates a typical drag-and-drop shortcut menu.

![screen shot of drag-and-drop shortcut menu](images/context-menu/context-dragdrop.png)

A drag-and-drop handler is a shortcut menu handler that can add items to this shortcut menu. Drag-and-drop handlers are typically registered under the following subkey.

```
HKEY_CLASSES_ROOT
   Directory
      shellex
         DragDropHandlers
```

Add a subkey under the **DragDropHandlers** subkey named for the drag-and-drop handler, and set the subkey's default value to the string form of the handler's class identifier (CLSID) GUID. The following example enables the **MyDD** drag-and-drop handler.

```
HKEY_CLASSES_ROOT
   Directory
      shellex
         DragDropHandlers
            MyDD
               (Default) = {MyDD CLSID GUID}
```

### Suppressing Verbs and Controlling Visibility

You can use Windows policy settings to control verb visibility. Verbs can be suppressed through policy settings by adding a **SuppressionPolicy** value, or a **SuppressionPolicyEx** GUID value to the verb's registry subkey. Set the value of the **SuppressionPolicy** subkey to the policy ID. If the policy is turned on, the verb and its associated shortcut menu entry are suppressed. For possible policy ID values, see the [**RESTRICTIONS**](/windows/desktop/api/shlobj_core/ne-shlobj_core-restrictions) enumeration.

### Employing the Verb Selection Model

Registry values must be set for verbs to handle situations where a user can select a single item, multiple items, or a selection from an item. A verb requires separate registry values for each of these three situations that the verb supports. The possible values for the verb selection model are as follows:

-   Specify the MultiSelectModel value for all verbs. If the MultiSelectModel value is not specified, it is inferred from the type of verb implementation you have chosen. For COM-based methods (such as DropTarget and ExecuteCommand) **Player** is assumed, and for the other methods **Document** is assumed.
-   Specify **Single** for verbs that support only a single selection.
-   Specify **Player** for verbs that support any number of items.
-   Specify **Document** for verbs that create a top level window for each item. Doing so limits the number of items activated and helps avoid running out of system resources if the user opens too many windows.

When the number of items selected does not match the verb selection model or is greater than the default limits outlined in the following table, the verb fails to appear.



| Type of verb implementation | Document | Player    |
|-----------------------------|----------|-----------|
| Legacy                      | 15 items | 100 items |
| COM                         | 15 items | No limit  |



 

The following are example registry entries using the MultiSelectModel value.

```
HKEY_CLASSES_ROOT
   Folder
      shell
         open
             = MultiSelectModel = Document
```

```
HKEY_CLASSES_ROOT
   ProgID
      shell
         verb
             = MultiSelectModel = Single | Document | Player
```

### Using Item Attributes

The [**SFGAO**](sfgao.md) flag values of the Shell attributes for an item can be tested to determine whether the verb should be enabled or disabled.

To use this attribute feature, add the following the **REG\_DWORD** values under the verb:

-   The AttributeMask value specifies the [**SFGAO**](sfgao.md) value of the bit values of the mask to test with.
-   The AttributeValue value specifies the [**SFGAO**](sfgao.md) value of the bits that are tested.
-   The ImpliedSelectionModel specifies zero for item verbs, or nonzero for verbs on the background shortcut menu.

In the following example registry entry, the AttributeMask is set to [**SFGAO\_READONLY**](sfgao.md) (0x40000).

```
HKEY_CLASSES_ROOT
   txtfile
      Shell
         test.verb2
            AttributeMask = 0x40000
            AttributeValue = 0x0
            ImpliedSelectionModel = 0x0
            command
               (Default) = %SystemRoot%\system32\notepad.exe %1
```

### Implementing Custom Verbs for Folders through Desktop.ini

In Windows 7 and later, you can add verbs to a folder through Desktop.ini. For more information about Desktop.ini files, see [How to Customize Folders with Desktop.ini](how-to-customize-folders-with-desktop-ini.md).

> [!Note]  
> Desktop.ini files should always be marked **System** + **Hidden** so they won't be displayed to users.

 

**To add custom verbs for folders through a Desktop.ini file, perform the following steps:**

1.  Create a folder that is marked **Read-only** or **System**.
2.  Create a Desktop.ini file that includes a \[.ShellClassInfo\] DirectoryClass=Folder ProgID.
3.  In the registry create **HKEY\_CLASSES\_ROOT**\\**Folder ProgID** with a value of CanUseForDirectory. The CanUseForDirectory value avoids the misuse of ProgIDs that are set not to participate in implementing custom verbs for folders through Desktop.ini.
4.  Add verbs under the **Folder**ProgID subkey, for example:

    ```
    HKEY_CLASSES_ROOT
       CustomFolderType
          Shell
             MyVerb
                command
                   (Default) = %SystemRoot%\system32\notepad.exe %1\desktop.ini
    ```

> [!Note]  
> These verbs can be the default verb, in which case double-clicking the folder activates the verb.

 

## Related topics

<dl> <dt>

[Best Practices for Shortcut Menu Handlers and Multiple Selection Verbs](verbs-best-practices.md)
</dt> <dt>

[Choosing a Static or Dynamic Verb for your Shortcut Menu](shortcut-choose-method.md)
</dt> <dt>

[Customizing a Shortcut Menu Using Dynamic Verbs](shortcut-menu-using-dynamic-verbs.md)
</dt> <dt>

[Shortcut (Context) Menus and Shortcut Menu Handlers](context-menu.md)
</dt> <dt>

[Verbs and File Associations](fa-verbs.md)
</dt> <dt>

[Shortcut Menu Reference](context-menu-reference.md)
</dt> </dl>

 

 
