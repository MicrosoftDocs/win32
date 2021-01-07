---
description: Applications, processes, and windows can opt to make themselves unavailable for pinning to the taskbar or for inclusion in the Start menu's Most Frequently Used (MFU) list.
title: How to Exclude Items from Taskbar Pinning and Recent/Frequent Lists
ms.topic: article
ms.date: 05/31/2018
---

# How to Exclude Items from Taskbar Pinning and Recent/Frequent Lists

Applications, processes, and windows can opt to make themselves unavailable for pinning to the taskbar or for inclusion in the **Start** menu's Most Frequently Used (MFU) list.

## Instructions


There are three mechanisms to accomplish the exclusion of items from taskbar pinning and recent/frequent lists:

-   Add the NoStartPage entry to the application's registration as shown in this example:

    ```
    HKEY_CLASSES_ROOT
       Applications
          Example.exe
             NoStartPage
    ```

    The data associated with the NoStartPage entry is ignored. Only the presence of the entry is required. Therefore, the ideal type for NoStartPage is **REG\_NONE**.

    Note that any use of an explicit Application User Model ID (AppUserModelID) overrides the NoStartPage entry. If an explicit AppUserModelID is applied to a shortcut, process, or window, it becomes pinnable and eligible for the **Start** menu MFU list.

-   Set the [System.AppUserModel.PreventPinning](../properties/props-system-appusermodel-preventpinning.md) property on windows and shortcuts. This property must be set on a window before the [PKEY\_AppUserModel\_ID](../properties/props-system-appusermodel-id.md) property is set.
-   Add an explicit AppUserModelID as a value under the following registry subkey as shown in this example:

    ```
    HKEY_LOCAL_MACHINE
       Software
          Microsoft
             Windows
                CurrentVersion
                   Explorer
                      FileAssociation
                         NoStartPageAppUserModelIDs
                            AppUserModelID1
                            AppUserModelID2
                            AppUserModelID3
    ```

    Each entry is a **REG\_NULL** value with the name of the AppUserModelID. Any AppUserModelID that is found in this list is not pinnable and not eligible for inclusion in the **Start** menu MFU list.

## Remarks

Be aware that certain executable files, as well as shortcuts that contain certain strings in their names, are automatically excluded from pinning and inclusion in the MFU list.

> [!Note]  
> This automatic exclusion can be overridden by applying an explicit AppUserModelID.

 

If any of the following strings, regardless of case, are included in the shortcut name, the program is not pinnable and is not displayed in the most frequently used list (not applicable to Windows 10):

-   Documentation
-   Help
-   Install
-   More Info
-   Read me
-   Read First
-   Readme
-   Remove
-   Setup
-   Support
-   What's New

The following list of programs are not pinnable and are excluded from the most frequently used list:

-   Applaunch.exe
-   Control.exe
-   Dfsvc.exe
-   Dllhost.exe
-   Guestmodemsg.exe
-   Hh.exe
-   Install.exe
-   Isuninst.exe
-   Lnkstub.exe
-   Mmc.exe
-   Mshta.exe
-   Msiexec.exe
-   Msoobe.exe
-   Rundll32.exe
-   Setup.exe
-   St5unst.exe
-   Unwise.exe
-   Unwise32.exe
-   Werfault.exe
-   Winhlp32.exe
-   Wlrmdr.exe
-   Wuapp.exe

The preceding lists are stored in the following registry values.

> [!Note]  
> These lists should not be modified by applications. Use one of the exclusion list methods described earlier in this topic for the same experience.

 

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Windows
            CurrentVersion
               Explorer
                  FileAssociation
                     AddRemoveApps
                     HostApps
```

## Related topics

<dl> <dt>

[The Taskbar](taskbar.md)
</dt> <dt>

[Taskbar Extensions](taskbar-extensions.md)
</dt> </dl>

 

 
