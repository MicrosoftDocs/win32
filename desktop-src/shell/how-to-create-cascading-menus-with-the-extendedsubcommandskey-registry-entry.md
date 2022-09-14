---
description: In Windows 7 and later, you can use the ExtendedSubCommandsKey subkey to create extended cascading menus.
ms.assetid: 6E8B4FB7-D4DB-4DBC-AF6F-59D02CB6AB13
title: Create Cascading Menus with the ExtendedSubCommandsKey Registry Entry
ms.topic: article
ms.date: 05/31/2018
---

# How to Create Cascading Menus with the ExtendedSubCommandsKey Registry Entry

In Windows 7 and later, you can use the **ExtendedSubCommandsKey** subkey to create extended cascading menus.

The following screen shot is an example of an extended cascading menu.

![screen shot showing extended cascading menu for devices](images/file-assoc/extendedsubcommandskey.png)

Because **HKEY\_CLASSES\_ROOT** is a combination of **HKEY\_CURRENT\_USER** and **HKEY\_LOCAL\_MACHINE**, you can register the subverbs under the **HKEY\_CURRENT\_USER**\\**Software**\\**Classes** subkey. The advantage of doing so is that elevated permission is not required. Other file associations can reuse this entire set of verbs by specifying the same **ExtendedSubCommandsKey** subkey. If you do not need to reuse this set of verbs, you can list the verbs under the parent. In this case, make sure the default value of the parent is empty, as illustrated in the registry entry example in this section.

## Instructions

### Step 1:

Create a subkey under **HKEY\_CLASSES\_ROOT**\\*ProgID*\\**shell**\\*CascadeMenuKey* and give the CascadeMenuKey a name such as *CascadeTest*, for example. Then add a MUIVerb entry of **REG\_SZ** type and give it a name such as Test Cascade Menu 2, as illustrated in the following registry example.

```
HKEY_CLASSES_ROOT
   txtfile
      shell
         CascadeTest
            MUIVerb = Test Cascade Menu 2
```

### Step 2:

Under the *CascadeTest* subkey that you created, add an **ExtendedSubCommandsKey** subkey, and then add the document subcommands (of type **REG\_SZ**); for example:

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

### Step 3:

Populate the subverbs using any of the following static verb implementations. Note that the CommandFlags subkey represents EXPCMDFLAGS values. If you want to add a separator before or after the cascade menu item, use ECF\_SEPARATORBEFORE (0x20) or ECF\_SEPARATORAFTER (0x40). For a description of these Windows 7 and later flags, see [**IExplorerCommand::GetFlags**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iexplorercommand-getflags). ECF\_SEPARATORBEFORE works only for the top level menu items. MUIVerb is of type **REG\_SZ**, and CommandFlags is of type **REG\_DWORD**.

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
                        (Default) = C:\Program Files\Windows NT\Accessories\wordpad.exe %1
```

## Remarks

The following screen shot is an illustration of the previous registry key entry examples.

![screen shot showing an example of a cascading menu showing choices of notepad and wordpad](images/file-assoc/testcascademenu2.png)

 

 



