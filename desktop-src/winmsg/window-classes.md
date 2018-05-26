---
Description: This topic describes the types of window classes, how the system locates them, and the elements that define the default behavior of windows that belong to them.
ms.assetid: db79fd4b-6a15-4bf9-a0d9-5f6415f6c75f
title: Window Classes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Window Classes

This topic describes the types of window classes, how the system locates them, and the elements that define the default behavior of windows that belong to them.

A window class is a set of attributes that the system uses as a template to create a window. Every window is a member of a window class. All window classes are process specific.

### In This Section



| Name                                                 | Description                                                                                                                                                                                                                                                    |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About Window Classes](about-window-classes.md)     | Discusses window classes. Each window class has an associated window procedure shared by all windows of the same class. The window procedure processes messages for all windows of that class and therefore controls their behavior and appearance.<br/> |
| [Using Window Classes](using-window-classes.md)     | Demonstrates how to register a local window and use it to create a main window.<br/>                                                                                                                                                                     |
| [Window Class Reference](window-class-reference.md) | Contains the API reference.<br/>                                                                                                                                                                                                                         |



 

### Window Class Functions



| Name                                         | Description                                                                                                                                                                                                                   |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetClassInfoEx**](getclassinfoex.md)     | Retrieves information about a window class, including a handle to the small icon associated with the window class. The [**GetClassInfo**](/windows/win32/Winuser/nf-kusbfnclasslib-usbfnkmclasslibgetclassinformation?branch=master) function does not retrieve a handle to the small icon.<br/> |
| [**GetClassLong**](getclasslong.md)         | Retrieves the specified 32-bit (**long**) value from the [**WNDCLASSEX**](wndclassex.md) structure associated with the specified window. <br/>                                                                         |
| [**GetClassLongPtr**](getclasslongptr.md)   | Retrieves the specified value from the [**WNDCLASSEX**](wndclassex.md) structure associated with the specified window.<br/>                                                                                            |
| [**GetClassName**](getclassname.md)         | Retrieves the name of the class to which the specified window belongs. <br/>                                                                                                                                            |
| [**GetWindowLong**](getwindowlong.md)       | Retrieves information about the specified window. The function also retrieves the 32-bit (**long**) value at the specified offset into the extra window memory.<br/>                                                    |
| [**GetWindowLongPtr**](getwindowlongptr.md) | Retrieves information about the specified window. The function also retrieves the value at a specified offset into the extra window memory.<br/>                                                                        |
| [**RegisterClass**](/windows/win32/Winuser/nf-kusbfnclasslib-usbfnkmclasslibregisterclassdevice?branch=master)       | Registers a window class for subsequent use in calls to the [**CreateWindow**](/windows/win32/Winuser/ns-pointofservicedriverinterface-_linedisplaycreatewindowdata?branch=master) or [**CreateWindowEx**](createwindowex.md) function.<br/>                                                             |
| [**RegisterClassEx**](registerclassex.md)   | Registers a window class for subsequent use in calls to the [**CreateWindow**](/windows/win32/Winuser/ns-pointofservicedriverinterface-_linedisplaycreatewindowdata?branch=master) or [**CreateWindowEx**](createwindowex.md) function. <br/>                                                            |
| [**SetClassLongPtr**](setclasslongptr.md)   | Replaces the specified value at the specified offset in the extra class memory or the [**WNDCLASSEX**](wndclassex.md) structure for the class to which the specified window belongs.<br/>                              |
| [**SetClassWord**](setclassword.md)         | Replaces the 16-bit (**WORD**) value at the specified offset into the extra class memory for the window class to which the specified window belongs.<br/>                                                               |
| [**SetWindowLong**](setwindowlong.md)       | Changes an attribute of the specified window. The function also sets the 32-bit (long) value at the specified offset into the extra window memory.<br/>                                                                 |
| [**SetWindowLongPtr**](setwindowlongptr.md) | Changes an attribute of the specified window. The function also sets a value at the specified offset in the extra window memory.<br/>                                                                                   |
| [**UnregisterClass**](/windows/win32/Winuser/nf-kusbfnclasslib-usbfnkmclasslibunregisterclassdevice?branch=master)   | Unregisters a window class, freeing the memory required for the class. <br/>                                                                                                                                            |



 

The following functions are obsolete.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>GetClassInfo</strong>](/windows/win32/Winuser/nf-kusbfnclasslib-usbfnkmclasslibgetclassinformation?branch=master)</td>
<td>Retrieves information about a window class. <br/>
<blockquote>
[!Note]<br />
The [<strong>GetClassInfo</strong>](/windows/win32/Winuser/nf-kusbfnclasslib-usbfnkmclasslibgetclassinformation?branch=master) function has been superseded by the [<strong>GetClassInfoEx</strong>](getclassinfoex.md) function. You can still use <strong>GetClassInfo</strong>, however, if you do not need information about the class small icon.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetClassWord</strong>](getclassword.md)</td>
<td>Retrieves the 16-bit (<strong>WORD</strong>) value at the specified offset into the extra class memory for the window class to which the specified window belongs.
<blockquote>
[!Note]<br />
This function is deprecated for any use other than <em>nIndex</em> set to GCW_ATOM. The function is provided only for compatibility with 16-bit versions of Windows. Applications should use the [<strong>GetClassLong</strong>](getclasslong.md) function.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td>[<strong>SetClassLong</strong>](setclasslong.md)</td>
<td>Replaces the specified 32-bit (<strong>long</strong>) value at the specified offset into the extra class memory or the [<strong>WNDCLASSEX</strong>](wndclassex.md) structure for the class to which the specified window belongs.
<blockquote>
[!Note]<br />
This function has been superseded by the [<strong>SetClassLongPtr</strong>](setclasslongptr.md) function. To write code that is compatible with both 32-bit and 64-bit versions of Windows, use <strong>SetClassLongPtr</strong>.
</blockquote>
<br/> <br/></td>
</tr>
</tbody>
</table>



 

### Window Class Structures



| Name                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WNDCLASS**](wndclass.md)     | Contains the window class attributes that are registered by the [**RegisterClass**](/windows/win32/Winuser/nf-kusbfnclasslib-usbfnkmclasslibregisterclassdevice?branch=master) function. <br/> This structure has been superseded by the [**WNDCLASSEX**](wndclassex.md) structure used with the [**RegisterClassEx**](registerclassex.md) function. You can still use [**WNDCLASS**](wndclass.md) and [**RegisterClass**](/windows/win32/Winuser/nf-kusbfnclasslib-usbfnkmclasslibregisterclassdevice?branch=master) if you do not need to set the small icon associated with the window class.<br/>                                                  |
| [**WNDCLASSEX**](wndclassex.md) | Contains window class information. It is used with the [**RegisterClassEx**](registerclassex.md) and [**GetClassInfoEx**](getclassinfoex.md)  functions. <br/> The [**WNDCLASSEX**](wndclassex.md) structure is similar to the [**WNDCLASS**](wndclass.md) structure. There are two differences. **WNDCLASSEX** includes the **cbSize** member, which specifies the size of the structure, and the **hIconSm** member, which contains a handle to a small icon associated with the window class.<br/> |



 

 

 




