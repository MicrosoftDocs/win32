---
description: User interface objects support only one handle per object. Processes cannot inherit or duplicate handles to user objects. Processes in one session cannot reference a user handle in another session.
ms.assetid: 07edc049-26d9-4f42-a5e7-e1f4c8435a6c
title: User Objects
ms.topic: article
ms.date: 05/31/2018
---

# User Objects

User interface objects support only one handle per object. Processes cannot inherit or duplicate handles to user objects. Processes in one session cannot reference a user handle in another session.

There is a theoretical limit of 65,536 user handles per session. However, the maximum number of user handles that can be opened per session is usually lower, since it is affected by available memory. There is also a default per-process limit of user handles. To change this limit, set the following registry value:

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Windows NT**\\**CurrentVersion**\\**Windows**\\**USERProcessHandleQuota**

This value can be set to a number between 200 and 18,000.

## Handles to User Objects

Handles to user objects are public to all processes. That is, any process can use the user object handle, provided that the process has security access to the object.

In the following illustration, an application creates a window object. The [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa) function creates the window object and returns an object handle.

![application creating a window object](images/cshob-01.png)

After the window object has been created, the application can use the window handle to display or change the window. The handle remains valid until the window object is destroyed.

In the next illustration, the application destroys the window object. The [**DestroyWindow**](/windows/win32/api/winuser/nf-winuser-destroywindow) function removes the window object from memory, which invalidates the window handle.

![destroying a window object](images/cshob-02.png)

## Managing User Objects

The following table lists the user objects, along with each object's creator and destroyer functions. The creator functions either create the object and an object handle or simply return the existing object handle. The destroyer functions remove the object from memory, which invalidates the object handle.



| User object       | Creator function                                                                                                                                                                                                                                                              | Destroyer function                                                                                   |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Accelerator table | [**CreateAcceleratorTable**](/windows/win32/api/winuser/nf-winuser-createacceleratortablea)                                                                                                                                                                                                               | [**DestroyAcceleratorTable**](/windows/win32/api/winuser/nf-winuser-destroyacceleratortable)                                    |
| Caret             | [**CreateCaret**](/windows/win32/api/winuser/nf-winuser-createcaret)                                                                                                                                                                                                                                     | [**DestroyCaret**](/windows/win32/api/winuser/nf-winuser-destroycaret)                                                          |
| Cursor            | [**CreateCursor**](/windows/win32/api/winuser/nf-winuser-createcursor), [**LoadCursor**](/windows/win32/api/winuser/nf-winuser-loadcursora), [**LoadImage**](/windows/win32/api/winuser/nf-winuser-loadimagea)                                                                                                                                                   | [**DestroyCursor**](/windows/win32/api/winuser/nf-winuser-destroycursor)                                                        |
| DDE conversation  | [**DdeConnect**](/windows/win32/api/ddeml/nf-ddeml-ddeconnect), [**DdeConnectList**](/windows/win32/api/ddeml/nf-ddeml-ddeconnectlist)                                                                                                                                                                                      | [**DdeDisconnect**](/windows/win32/api/ddeml/nf-ddeml-ddedisconnect), [**DdeDisconnectList**](/windows/win32/api/ddeml/nf-ddeml-ddedisconnectlist) |
| Hook              | [**SetWindowsHookEx**](/windows/win32/api/winuser/nf-winuser-setwindowshookexa)                                                                                                                                                                                                                           | [**UnhookWindowsHookEx**](/windows/win32/api/winuser/nf-winuser-unhookwindowshookex)                                            |
| Icon              | [**CreateIconIndirect**](/windows/win32/api/winuser/nf-winuser-createiconindirect), [**LoadIcon**](/windows/win32/api/winuser/nf-winuser-loadicona), [**LoadImage**](/windows/win32/api/winuser/nf-winuser-loadimagea)                                                                                                                                           | [**DestroyIcon**](/windows/win32/api/winuser/nf-winuser-destroyicon)                                                            |
| Menu              | [**CreateMenu**](/windows/win32/api/winuser/nf-winuser-createmenu), [**CreatePopupMenu**](/windows/win32/api/winuser/nf-winuser-createpopupmenu), [**LoadMenu**](/windows/win32/api/winuser/nf-winuser-loadmenua), [**LoadMenuIndirect**](/windows/win32/api/winuser/nf-winuser-loadmenuindirecta)                                                                                          | [**DestroyMenu**](/windows/win32/api/winuser/nf-winuser-destroymenu)                                                            |
| Window            | [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa), [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa), [**CreateDialogParam**](/windows/win32/api/winuser/nf-winuser-createdialogparama), [**CreateDialogIndirectParam**](/windows/win32/api/winuser/nf-winuser-createdialogindirectparama), [**CreateMDIWindow**](/windows/win32/api/winuser/nf-winuser-createmdiwindowa) | [**DestroyWindow**](/windows/win32/api/winuser/nf-winuser-destroywindow)                                                        |
| Window position   | [**BeginDeferWindowPos**](/windows/win32/api/winuser/nf-winuser-begindeferwindowpos)                                                                                                                                                                                                                     | [**EndDeferWindowPos**](/windows/win32/api/winuser/nf-winuser-enddeferwindowpos)                                                |



 

 

 
