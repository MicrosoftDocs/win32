---
Description: User interface objects support only one handle per object. Processes cannot inherit or duplicate handles to user objects. Processes in one session cannot reference a user handle in another session.
ms.assetid: 07edc049-26d9-4f42-a5e7-e1f4c8435a6c
title: User Objects
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# User Objects

User interface objects support only one handle per object. Processes cannot inherit or duplicate handles to user objects. Processes in one session cannot reference a user handle in another session.

There is a theoretical limit of 65,536 user handles per session. However, the maximum number of user handles that can be opened per session is usually lower, since it is affected by available memory. There is also a default per-process limit of user handles. To change this limit, set the following registry value:

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Windows NT**\\**CurrentVersion**\\**Windows**\\**USERProcessHandleQuota**

This value can be set to a number between 200 and 18,000.

## Handles to User Objects

Handles to user objects are public to all processes. That is, any process can use the user object handle, provided that the process has security access to the object.

In the following illustration, an application creates a window object. The [**CreateWindow**](_win32_createwindow_cpp) function creates the window object and returns an object handle.

![application creating a window object](images/cshob-01.png)

After the window object has been created, the application can use the window handle to display or change the window. The handle remains valid until the window object is destroyed.

In the next illustration, the application destroys the window object. The [**DestroyWindow**](_win32_destroywindow_cpp) function removes the window object from memory, which invalidates the window handle.

![destroying a window object](images/cshob-02.png)

## Managing User Objects

The following table lists the user objects, along with each object's creator and destroyer functions. The creator functions either create the object and an object handle or simply return the existing object handle. The destroyer functions remove the object from memory, which invalidates the object handle.



| User object       | Creator function                                                                                                                                                                                                                                                              | Destroyer function                                                                                   |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Accelerator table | [**CreateAcceleratorTable**](_win32_createacceleratortable_cpp)                                                                                                                                                                                                               | [**DestroyAcceleratorTable**](_win32_destroyacceleratortable_cpp)                                    |
| Caret             | [**CreateCaret**](_win32_createcaret_cpp)                                                                                                                                                                                                                                     | [**DestroyCaret**](_win32_destroycaret_cpp)                                                          |
| Cursor            | [**CreateCursor**](_win32_createcursor_cpp), [**LoadCursor**](_win32_loadcursor_cpp), [**LoadImage**](_win32_loadimage_cpp)                                                                                                                                                   | [**DestroyCursor**](_win32_destroycursor_cpp)                                                        |
| DDE conversation  | [**DdeConnect**](_win32_ddeconnect_cpp), [**DdeConnectList**](_win32_ddeconnectlist_cpp)                                                                                                                                                                                      | [**DdeDisconnect**](_win32_ddedisconnect_cpp), [**DdeDisconnectList**](_win32_ddedisconnectlist_cpp) |
| Hook              | [**SetWindowsHookEx**](_win32_setwindowshookex_cpp)                                                                                                                                                                                                                           | [**UnhookWindowsHookEx**](_win32_unhookwindowshookex_cpp)                                            |
| Icon              | [**CreateIconIndirect**](_win32_createiconindirect_cpp), [**LoadIcon**](_win32_loadicon_cpp), [**LoadImage**](_win32_loadimage_cpp)                                                                                                                                           | [**DestroyIcon**](_win32_destroyicon_cpp)                                                            |
| Menu              | [**CreateMenu**](_win32_createmenu_cpp), [**CreatePopupMenu**](_win32_createpopupmenu_cpp), [**LoadMenu**](_win32_loadmenu_cpp), [**LoadMenuIndirect**](_win32_loadmenuindirect_cpp)                                                                                          | [**DestroyMenu**](_win32_destroymenu_cpp)                                                            |
| Window            | [**CreateWindow**](_win32_createwindow_cpp), [**CreateWindowEx**](_win32_createwindowex_cpp), [**CreateDialogParam**](_win32_createdialogparam_cpp), [**CreateDialogIndirectParam**](_win32_createdialogindirectparam_cpp), [**CreateMDIWindow**](_win32_createmdiwindow_cpp) | [**DestroyWindow**](_win32_destroywindow_cpp)                                                        |
| Window position   | [**BeginDeferWindowPos**](_win32_begindeferwindowpos_cpp)                                                                                                                                                                                                                     | [**EndDeferWindowPos**](_win32_enddeferwindowpos_cpp)                                                |



 

 

 



