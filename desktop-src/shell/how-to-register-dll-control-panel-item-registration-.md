---
description: Control Panel items that are implemented in a DLL that exports the CPlApplet function have different registration requirements than .exe files.
title: How to Register DLL Control Panel Items
ms.topic: article
ms.date: 05/31/2018
---

# How to Register DLL Control Panel Items

> [!Note]  
> Current implementation guidelines state that new Control Panel items should be implemented as .exe files rather than .cpl files. The following information is included mainly for legacy purposes.

 

Control Panel items that are implemented in a DLL that exports the [**CPlApplet**](/windows/win32/api/cpl/nc-cpl-applet_proc) function have different registration requirements than .exe files. In Windows XP and later, new Control Panel item DLLs should be installed in the associated application's folder under the Program Files folder. Items that are stored in the System32 directory with a .cpl extension do not need to be registered; they are automatically shown in the Control Panel. All other Control Panel items that use **CPlApplet** must be registered in one of two ways:

- If the Control Panel item is to be available to all users, register the path on a per-computer basis by adding a **REG\_EXPAND\_SZ** value to the **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**Control Panel**\\**Cpls** subkey, set to the DLL path.
- If the Control Panel item is to be available on a per-user basis, use **HKEY\_CURRENT\_USER** as the root key instead of **HKEY\_LOCAL\_MACHINE**.

The following two examples register the *MyCplApp* Control Panel item. The DLL is named MyCpl.cpl and is located in the *MyCorp\\MyApp* application directory. This first example illustrates per-computer registration.

## Instructions

### Step 1:

Add this information to the registry to register the existence of the .cpl file.

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Windows
            CurrentVersion
               Control Panel
                  Cpls
                     MyCpl = [REG_EXPAND_SZ] %ProgramFiles%\MyCorp\MyApp\MyCpl.cpl
```

### Step 2:

**Windows Vista and later:** Add this additional information to the registry to provide a GUID for the Control Panel item.

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Windows
            CurrentVersion
               Control Panel
                  Extended Properties
                     System.Software.AppId
                        %ProgramFiles%\MyCorp\MyApp\MyCpl.cpl = {A newly generated GUID}
```

By generating a GUID to uniquely identify the Control Panel item, you can add task links to the Control Panel. Without this GUID, there is no way for the task links to be associated with the Control Panel item. See [Creating Searchable Task Links for a Control Panel Item](creating-searchable-task-links.md).

### Step 3:

**Windows Vista and later:** Add the following information to the registry to create a canonical name for the item.

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Windows
            CurrentVersion
               Control Panel
                  Extended Properties
                     System.ApplicationName
                        %ProgramFiles%\MyCorp\MyApp\MyCpl.cpl = [REG_SZ] MyCorporation.MyCpl
```

By adding a canonical name, users can launch the Control Panel item from a command line by entering `control.exe /name MyCorporation.MyCpl`. This also makes it possible to change an implementation from a .cpl file to a .exe file later, without requiring calling programs to make any changes since they can continue opening the item through its canonical name. For more information on canonical names, see [Executing Control Panel Items](executing-control-panel-items.md).

### Step 4:

**Windows Vista and later:** Add the following information to the registry to assign a Control Panel item to one or more categories.

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Windows
            CurrentVersion
               Control Panel
                  Extended Properties
                     System.ControlPanel.Category
                        %ProgramFiles%\MyCorp\MyApp\MyCpl.cpl = [REG_DWORD] 3
```

**Windows XP:** Add the following information to the registry to assign a Control Panel item to one or more categories.

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Windows
            CurrentVersion
               Control Panel
                  Extended Properties
                     {305CA226-D286-468e-B848-2B2E8E697B74} 2
                        %ProgramFiles%\MyCorp\MyApp\MyCpl.cpl = [REG_DWORD] 3
```

This example assigns the item to category 3, which is Network and Internet. To add an item to multiple categories, provide the list as a REG\_SZ value separated by commas, such as "3,8". Values can be provided as either decimal or hexadecimal. Note that the ability to add an item to multiple categories is only possible in Windows XP Service Pack 2 (SP2) and later. See [Assigning Control Panel Categories](assigning-control-panel-categories.md) for all possible values.

### Step 5:

**Windows Vista and later:** Add the following information to the registry to create and point to an XML file to hold task links for the item. The value must be a REG\_SZ path as shown here or a module and resource ID (for example, "C:\\Program Files\\MyCorp\\MyApp\\MyApp.exe,-31") if it is an embedded resource. The location of the XML file should be fully specified. It cannot use an environment variable such as %ProgramFiles%.

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Windows
            CurrentVersion
               Control Panel
                  Extended Properties
                     System.Software.TasksFileUrl
                        %ProgramFiles%\MyCorp\MyApp\MyCpl.cpl = [REG_SZ] C:\ProgramFiles\MyCorp\MyApp\MyTasks.xml
```

For more details on task links and how to create the XML file to hold them, see [Creating Searchable Task Links for a Control Panel Item](creating-searchable-task-links.md).

## Related topics

<dl> <dt>

[Registering Control Panel Items](registering-control-panel-items.md)
</dt> <dt>

[How To Register Executable Control Panel Items](how-to-register-an-executable-control-panel-item-registration-.md)
</dt> </dl>

 

 
