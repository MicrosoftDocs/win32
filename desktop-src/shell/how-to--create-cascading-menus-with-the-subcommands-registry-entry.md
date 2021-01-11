---
description: In Windows 7 and later, you can use the SubCommands entry in the registry to create cascading menus by using the procedure given in this topic.
title: Create Cascading Menus with the SubCommands Registry Entry
ms.topic: article
ms.date: 05/31/2018
---

# How to Create Cascading Menus with the SubCommands Registry Entry

In Windows 7 and later, you can use the SubCommands entry in the registry to create cascading menus by using the procedure given in this topic.

## Instructions

### Step 1:

Create a new subkey under **HKEY\_CLASSES\_ROOT**\\*ProgID*\\**shell**, where *ProgID* is the file type for which you want to add a cascading menu. You can name this new subkey anything you'd like. For the remainder of this topic, we'll call it *CascadeMenu*, as shown in the following example.

```
HKEY_CLASSES_ROOT
   ProgID
      shell
         CascadeMenu
```

### Step 2:

Add an entry named "MUIVerb", of type **REG\_SZ** or **REG\_EXPAND\_SZ**, to the *CascadeMenu* subkey. Assign this entry a string value such as "Test Cascade Menu". Normally, this string is provided as a resource reference in the form "@file, resource". The (Default) value for the *CascadeMenu* subkey should not be set.

```
HKEY_CLASSES_ROOT
   ProgID
      shell
         CascadeMenu
            (Default)
            MUIVerb = Test Cascade Menu
```

### Step 3:

Add an entry named "SubCommands", of type **REG\_SZ** or **REG\_EXPAND\_SZ**, to the *CascadeMenu* subkey. Assign this entry a semicolon-delimited list of the verbs that should appear on the menu, in their desired order of appearance.

```
HKEY_CLASSES_ROOT
   ProgID
      Shell
         CascadeMenu
            SubCommands = Windows.delete;Windows.properties;Windows.rename;Windows.cut;Windows.copy;Windows.paste
```

### Step 4:

Populate the **CommandStore** subkey with verb implementations for any custom static verb implementation methods that you've used in your SubCommands entry; for example:

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

## Related topics

<dl> <dt>

[Creating Static Cascading Menus](creating-static-cascading-menus.md)
</dt> </dl>

 

 



