---
Description: User interface objects support only one handle per object. Processes cannot inherit or duplicate handles to user objects. Processes in one session cannot reference a user handle in another session.
ms.assetid: 07edc049-26d9-4f42-a5e7-e1f4c8435a6c
title: User Objects
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
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

In the following illustration, an application creates a window object. The [**CreateWindow**](https://www.bing.com/search?q=**CreateWindow**) function creates the window object and returns an object handle.

![application creating a window object](https://www.bing.com/search?q=application creating a window object)

After the window object has been created, the application can use the window handle to display or change the window. The handle remains valid until the window object is destroyed.

In the next illustration, the application destroys the window object. The [**DestroyWindow**](https://www.bing.com/search?q=**DestroyWindow**) function removes the window object from memory, which invalidates the window handle.

![destroying a window object](https://www.bing.com/search?q=destroying a window object)

## Managing User Objects

The following table lists the user objects, along with each object's creator and destroyer functions. The creator functions either create the object and an object handle or simply return the existing object handle. The destroyer functions remove the object from memory, which invalidates the object handle.



| User object       | Creator function                                                                                                                                                                                                                                                              | Destroyer function                                                                                   |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Accelerator table | [**CreateAcceleratorTable**](https://www.bing.com/search?q=**CreateAcceleratorTable**)                                                                                                                                                                                                               | [**DestroyAcceleratorTable**](https://www.bing.com/search?q=**DestroyAcceleratorTable**)                                    |
| Caret             | [**CreateCaret**](https://www.bing.com/search?q=**CreateCaret**)                                                                                                                                                                                                                                     | [**DestroyCaret**](https://www.bing.com/search?q=**DestroyCaret**)                                                          |
| Cursor            | [**CreateCursor**](https://www.bing.com/search?q=**CreateCursor**), [**LoadCursor**](https://www.bing.com/search?q=**LoadCursor**), [**LoadImage**](https://www.bing.com/search?q=**LoadImage**)                                                                                                                                                   | [**DestroyCursor**](https://www.bing.com/search?q=**DestroyCursor**)                                                        |
| DDE conversation  | [**DdeConnect**](https://www.bing.com/search?q=**DdeConnect**), [**DdeConnectList**](https://www.bing.com/search?q=**DdeConnectList**)                                                                                                                                                                                      | [**DdeDisconnect**](https://www.bing.com/search?q=**DdeDisconnect**), [**DdeDisconnectList**](https://www.bing.com/search?q=**DdeDisconnectList**) |
| Hook              | [**SetWindowsHookEx**](https://www.bing.com/search?q=**SetWindowsHookEx**)                                                                                                                                                                                                                           | [**UnhookWindowsHookEx**](https://www.bing.com/search?q=**UnhookWindowsHookEx**)                                            |
| Icon              | [**CreateIconIndirect**](https://www.bing.com/search?q=**CreateIconIndirect**), [**LoadIcon**](https://www.bing.com/search?q=**LoadIcon**), [**LoadImage**](https://www.bing.com/search?q=**LoadImage**)                                                                                                                                           | [**DestroyIcon**](https://www.bing.com/search?q=**DestroyIcon**)                                                            |
| Menu              | [**CreateMenu**](https://www.bing.com/search?q=**CreateMenu**), [**CreatePopupMenu**](https://www.bing.com/search?q=**CreatePopupMenu**), [**LoadMenu**](https://www.bing.com/search?q=**LoadMenu**), [**LoadMenuIndirect**](https://www.bing.com/search?q=**LoadMenuIndirect**)                                                                                          | [**DestroyMenu**](https://www.bing.com/search?q=**DestroyMenu**)                                                            |
| Window            | [**CreateWindow**](https://www.bing.com/search?q=**CreateWindow**), [**CreateWindowEx**](https://www.bing.com/search?q=**CreateWindowEx**), [**CreateDialogParam**](https://www.bing.com/search?q=**CreateDialogParam**), [**CreateDialogIndirectParam**](https://www.bing.com/search?q=**CreateDialogIndirectParam**), [**CreateMDIWindow**](https://www.bing.com/search?q=**CreateMDIWindow**) | [**DestroyWindow**](https://www.bing.com/search?q=**DestroyWindow**)                                                        |
| Window position   | [**BeginDeferWindowPos**](https://www.bing.com/search?q=**BeginDeferWindowPos**)                                                                                                                                                                                                                     | [**EndDeferWindowPos**](https://www.bing.com/search?q=**EndDeferWindowPos**)                                                |



 

 

 



