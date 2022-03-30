---
description: For Control Panel items that are implemented as .exe files, no special exports or message handling is required. Any .exe file can be registered as a command object to appear with an entry point in the Control Panel folder.
title: How to Register Executable Control Panel Items
ms.topic: article
ms.date: 05/31/2018
---

# How to Register Executable Control Panel Items

For Control Panel items that are implemented as .exe files, no special exports or message handling is required. Any .exe file can be registered as a command object to appear with an entry point in the Control Panel folder.

An example is used here to demonstrate the registration requirements. The example shows how to register a Control Panel item called **My Settings** as a command object so that it appears in the Control Panel window. The **My Settings** window also appears when the command `MyApp.exe /settings` is run.

## Instructions

### Step 1:

Generate a GUID for the Control Panel item. The GUID uniquely identifies the Control Panel item. In this example, `{0052D9FC-6764-4D29-A66F-2F3BD9E2BB40}` is the GUID of the Control Panel item.

### Step 2:

Using the GUID as a name, add a subkey to the registry as follows.

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         Windows
            CurrentVersion
               Explorer
                  ControlPanel
                     NameSpace
                        {0052D9FC-6764-4D29-A66F-2F3BD9E2BB40}
                           (Default) = My Settings
```

The data for the Default entry is simply the REG\_SZ name of the Control Panel item. The Default entry can be useful to identify the GUID entry, but it is optional.

### Step 3:

Using the GUID as a name, add a subkey and its entries to the registry as follows.

```
HKEY_CLASSES_ROOT
   CLSID
      {0052D9FC-6764-4D29-A66F-2F3BD9E2BB40}
         (Default) = My Settings
         LocalizedString = @%ProgramFiles%\MyCorp\MyApp.exe,-9
         InfoTip = @%ProgramFiles%\MyCorp\MyApp.exe,-5
         System.ApplicationName = MyCorporation.MySettings
         System.ControlPanel.Category = 1,8
         System.Software.TasksFileUrl = %ProgramFiles%\MyCorp\MyApp\MyTaskLinks.xml
```

- **Default**. REG\_SZ. The display name for the Control Panel item.
- **LocalizedString**. Optional. REG\_SZ or REG\_EXPAND\_SZ. The module name and string table ID of the localized name of the Control Panel item. The format is an "at" sign (@) followed by the name of the .exe or .dll that contains the Multilingual User Interface (MUI) string table. Environment variables can be used as a substitute for a part of the path. The path and file name is followed by a comma (,) and a hyphen (-), followed by the ID in the string table.

    If the module does not have a string table, then this entry can simply be the display name string. If you use only the display name string rather than a string table, the name does not adjust to the current display language.

- **InfoTip**. REG\_SZ or REG\_EXPAND\_SZ. A description of the Control Panel item. This information is shown in an InfoTip that is displayed when the mouse hovers over the item's icon. The syntax is the same as that used for LocalizedString, including the option of simply providing a string rather than a string table reference.
- **System.ApplicationName**. REG\_SZ. The canonical name of the item. The command of form `control.exe /name System.ApplicationName` opens the item; for example, `control.exe /name MyCorporation.MySettings`. See [Executing Control Panel Items](executing-control-panel-items.md) for more information on the use of Control.exe.
- **System.ControlPanel.Category**. REG\_SZ. A value that declares the Control Panel categories where the item appears. Multiple categories are separated by commas. In the case of the example above, the entry specifies that the **My Settings** item should appear in both the **Appearance and Personalization** and **Programs** categories. See [Assigning Control Panel Categories](assigning-control-panel-categories.md) for possible category values.
- **System.Software.TasksFileUrl**. REG\_SZ or REG\_EXPAND\_SZ. The path of the XML file that defines [task links](creating-searchable-task-links.md). This can be a direct file path as shown in the example, or an embedded resource specified as a module name and resource ID such as "%ProgramFiles%\\MyCorp\\MyApp\\MyApp.exe,-31".

### Step 4:

Under that same GUID subkey, add the following subkey to the registry to provide the path of the file that contains the icon and the resource ID of the image within that file.

```
HKEY_CLASSES_ROOT
   CLSID
      {0052D9FC-6764-4D29-A66F-2F3BD9E2BB40}
         DefaultIcon
            (Default) = %ProgramFiles%\MyCorp\MyApp.exe,-2
```

Note that while the syntax is otherwise similar to the LocalizedString and InfoTip entries discussed earlier, no '@' character is used as a prefix in the REG\_SZ or REG\_EXPAND\_SZ entry that specifies the path.

### Step 5:

Add the following information to the registry to provide the command that is called by the system when the user opens the Control Panel.

```
HKEY_CLASSES_ROOT
   CLSID
      {0052D9FC-6764-4D29-A66F-2F3BD9E2BB40}
         Shell
            Open
               Command
                  (Default) = [REG_EXPAND_SZ] %ProgramFiles%\MyCorp\MyApp.exe /Settings
```

## Related topics

<dl> <dt>

[Registering Control Panel Items](registering-control-panel-items.md)
</dt> <dt>

[How To Register DLL Control Panel Items](how-to-register-dll-control-panel-item-registration-.md)
</dt> </dl>

 

 



