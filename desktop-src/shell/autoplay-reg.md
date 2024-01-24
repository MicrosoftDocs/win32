---
description: There are many situations where AutoRun may need to be temporarily or persistently disabled.
ms.assetid: 5e65a3d8-04b9-46ba-b4e5-a976e1923bfd
title: Enabling and Disabling AutoRun
ms.topic: article
ms.date: 03/03/2023
---

# Enabling and Disabling AutoRun

There are many situations where AutoRun may need to be temporarily or persistently disabled. For example, AutoRun might interfere with the operation of a running application and need to be disabled for the duration. The system provides several ways to disable AutoRun.

-   [Suppressing AutoRun Programmatically](#suppressing-autorun-programmatically)
-   [Using the Registry to Disable AutoRun](#using-the-registry-to-disable-autorun)
-   [AutoRun for Other Types of Storage Media](#autorun-for-other-types-of-storage-media)

## Suppressing AutoRun Programmatically

There are a variety of situations where AutoRun may need to be suppressed programmatically. Two examples are:

-   Your application has a setup program that requires the user to insert another disc that may contain an Autorun.inf file.
-   During the operation of your application, the user may need to insert another disc that may contain an Autorun.inf file.

In either case, you will normally not want to launch another application while the original is in progress.

Users can manually suppress AutoRun by holding down the SHIFT key when they insert the CD-ROM. However, it is usually preferable to handle this operation programmatically rather than depending on the user.

With systems that have Shell [version 4.70](versions.md) and later, Windows sends a "QueryCancelAutoPlay" message to the foreground window. Your application can respond to this message to suppress AutoRun. This approach is used by system utilities such as the [Open](../dlgbox/open-and-save-as-dialog-boxes.md) common dialog box to disable AutoRun.

The following code fragments illustrate how to set up and handle this message. Your application must be running in the foreground window. First, register "QueryCancelAutoPlay" as a Windows message:


```C++
uMessage = RegisterWindowMessage(TEXT("QueryCancelAutoPlay"));
```



Your application's window must be in the foreground to receive this message. The message handler should return **TRUE** to cancel AutoRun and **FALSE** to enable it. The following code fragment illustrates how to use this message to disable AutoRun.


```C++
UINT g_uQueryCancelAutoPlay = 0;

LRESULT WndProc(HWND hwnd, UINT uMsg,  WPARAM wParam, LPARAM lParam) 
{ 
    switch (uMsg) 
    { 
    ... 
    default: 
        if (!g_uQueryCancelAutoPlay)
        { 
            g_uQueryCancelAutoPlay = RegisterWindowMessage(TEXT("QueryCancelAutoPlay"));
        } 
        if (uMsg && uMsg == g_uQueryCancelAutoPlay)
        { 
            return TRUE;       // Cancel AutoRun
        }
    }
}
```



If your application is using a dialog box and needs to respond to a "QueryCancelAutoPlay" message, it cannot simply return **TRUE** or **FALSE**. Instead, call [**SetWindowLong**](/windows/win32/api/winuser/nf-winuser-setwindowlonga) with *nIndex* set to **DWL\_MSGRESULT**. Set the *dwNewLong* parameter to **TRUE** to cancel AutoRun, and **FALSE** to enable it. For example, the following sample dialog box procedure cancels AutoRun when it receives a "QueryCancelAutoPlay" message.


```C++
UINT g_uQueryCancelAutoPlay = 0;

BOOL DialogProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) 
{ 
    switch (uMsg) 
    { 
    ...
    default: 
        if (!g_uQueryCancelAutoPlay)
        {
            g_uQueryCancelAutoPlay = RegisterWindowMessage(TEXT("QueryCancelAutoPlay"));
        } 
        if (uMsg == g_uQueryCancelAutoPlay) 
        {
            SetWindowLong(hDlg, DWL_MSGRESULT, TRUE);          
            return 1;               
        }
    } 
```



## Using the Registry to Disable AutoRun

There are two registry values that can be used to persistently disable AutoRun: NoDriveAutoRun and NoDriveTypeAutoRun. The first value disables AutoRun for specified drive letters and the second disables AutoRun for a class of drives. If either of these values is set to disable AutoRun for a particular device, it will be disabled.

> [!Note]  
> The NoDriveAutoRun and NoDriveTypeAutoRun values should only be modified by system administrators to change the value for the entire system for testing or administrative purposes. Applications should not modify these values, as there is no way to reliably restore them to their original values.

 

The NoDriveAutoRun value disables AutoRun for specified drive letters. It is a REG\_DWORD data value, found under the following key:

```
HKEY_CURRENT_USER
   Software
      Microsoft
         Windows
            CurrentVersion
               Policies
                  Explorer
```

The first bit of the value corresponds to drive A:, the second to B:, and so on. To disable AutoRun for one or more drive letters, set the corresponding bits. For example, to disable the A: and C: drives, set NoDriveAutoRun to `0x00000005`.

The NoDriveTypeAutoRun value disables AutoRun for a class of drives. It is a REG\_DWORD or 4-byte REG\_BINARY data value, found under the same key.

```
HKEY_CURRENT_USER
   Software
      Microsoft
         Windows
            CurrentVersion
               Policies
                  Explorer
```

By setting the bits of this value's first byte, different drives can be excluded from working with AutoRun.

The following table gives the bits and bitmask constants, that can be set in the first byte of NoDriveTypeAutoRun to disable AutoRun for a particular drive type. You must restart Windows Explorer before the changes take effect.



| Bit Number | Bitmask Constant      | Description                                             |
|------------|-----------------------|---------------------------------------------------------|
| 0x04       | **DRIVE\_REMOVEABLE** | Disk can be removed from drive (such as a floppy disk). |
| 0x08       | **DRIVE\_FIXED**      | Disk cannot be removed from drive (a hard disk).        |
| 0x10       | **DRIVE\_REMOTE**     | Network drive.                                          |
| 0x20       | **DRIVE\_CDROM**      | CD-ROM drive.                                           |
| 0x40       | **DRIVE\_RAMDISK**    | RAM disk.                                               |



 

## AutoRun for Other Types of Storage Media

AutoRun is primarily intended for public distribution of applications on CD-ROM and DVD-ROM, and its use is discouraged for other storage media. However, it is often useful to enable AutoRun on other types of removable storage media. This feature is typically used simplify the debugging of AutoRun.inf files. AutoRun only works on removable storage devices when the following criteria are met:

-   The device must have AutoRun-compatible drivers. To be AutoRun-compatible, a driver must notify the system that a disk has been inserted by sending a [**WM\_DEVICECHANGE**](../devio/wm-devicechange.md) message.
-   The root directory of the inserted media must contain an Autorun.inf file.
-   The device must not have AutoRun disabled through the [registry](#using-the-registry-to-disable-autorun).
-   The foreground application has not [suppressed](#suppressing-autorun-programmatically) AutoRun.

> [!Note]  
> This feature should not be used to distribute applications on removable media. Because implementing AutoRun on removable media provides an easy way to spread computer viruses, users should be suspicious of any publicly distributed floppy disk that contains an Autorun.inf file.

 

Normally, AutoRun starts automatically, but it can also be started manually. If the device meets the criteria listed above, the drive letter's shortcut menu will include an **AutoPlay** command. To run AutoRun manually, either right-click the drive icon and select **AutoPlay** from the shortcut menu or double-click the drive icon. If the drivers are not AutoRun-compatible, the shortcut menu will not have an **AutoPlay** item and AutoRun cannot be started.

AutoRun-compatible drivers are provided with some removable disk drives, as well as some other types of removable media such as CompactFlash cards. AutoRun also works with network drives that are mapped to a drive letter with Windows Explorer or mounted with the [Microsoft Management Console (MMC)](/previous-versions/windows/desktop/mmc/microsoft-management-console-start-page). As with mounted hardware, a mounted network drive must have an Autorun.inf file in its root directory, and must not be disabled through the [registry](#using-the-registry-to-disable-autorun).

 

 
