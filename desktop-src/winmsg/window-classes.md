---
Description: This topic describes the types of window classes, how the system locates them, and the elements that define the default behavior of windows that belong to them.
ms.assetid: 'vs|winui|~\winui\windowsuserinterface\windowing\window_89windowclasse.htm'
title: Window Classes
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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
| [**GetClassInfoEx**](https://msdn.microsoft.com/en-us/library/ms633579(v=VS.85).aspx)     | Retrieves information about a window class, including a handle to the small icon associated with the window class. The [**GetClassInfo**](https://msdn.microsoft.com/en-us/library/ms633578(v=VS.85).aspx) function does not retrieve a handle to the small icon.<br/> |
| [**GetClassLong**](https://msdn.microsoft.com/en-us/library/ms633580(v=VS.85).aspx)         | Retrieves the specified 32-bit (**long**) value from the [**WNDCLASSEX**](https://msdn.microsoft.com/en-us/library/ms633577(v=VS.85).aspx) structure associated with the specified window. <br/>                                                                         |
| [**GetClassLongPtr**](https://msdn.microsoft.com/en-us/library/ms633581(v=VS.85).aspx)   | Retrieves the specified value from the [**WNDCLASSEX**](https://msdn.microsoft.com/en-us/library/ms633577(v=VS.85).aspx) structure associated with the specified window.<br/>                                                                                            |
| [**GetClassName**](https://msdn.microsoft.com/en-us/library/ms633582(v=VS.85).aspx)         | Retrieves the name of the class to which the specified window belongs. <br/>                                                                                                                                            |
| [**GetWindowLong**](https://msdn.microsoft.com/en-us/library/ms633584(v=VS.85).aspx)       | Retrieves information about the specified window. The function also retrieves the 32-bit (**long**) value at the specified offset into the extra window memory.<br/>                                                    |
| [**GetWindowLongPtr**](https://msdn.microsoft.com/en-us/library/ms633585(v=VS.85).aspx) | Retrieves information about the specified window. The function also retrieves the value at a specified offset into the extra window memory.<br/>                                                                        |
| [**RegisterClass**](https://msdn.microsoft.com/en-us/library/ms633586(v=VS.85).aspx)       | Registers a window class for subsequent use in calls to the [**CreateWindow**](https://msdn.microsoft.com/en-us/library/ms632679(v=VS.85).aspx) or [**CreateWindowEx**](https://msdn.microsoft.com/en-us/library/ms632680(v=VS.85).aspx) function.<br/>                                                             |
| [**RegisterClassEx**](https://msdn.microsoft.com/en-us/library/ms633587(v=VS.85).aspx)   | Registers a window class for subsequent use in calls to the [**CreateWindow**](https://msdn.microsoft.com/en-us/library/ms632679(v=VS.85).aspx) or [**CreateWindowEx**](https://msdn.microsoft.com/en-us/library/ms632680(v=VS.85).aspx) function. <br/>                                                            |
| [**SetClassLongPtr**](https://msdn.microsoft.com/en-us/library/ms633589(v=VS.85).aspx)   | Replaces the specified value at the specified offset in the extra class memory or the [**WNDCLASSEX**](https://msdn.microsoft.com/en-us/library/ms633577(v=VS.85).aspx) structure for the class to which the specified window belongs.<br/>                              |
| [**SetClassWord**](https://msdn.microsoft.com/en-us/library/ms633590(v=VS.85).aspx)         | Replaces the 16-bit (**WORD**) value at the specified offset into the extra class memory for the window class to which the specified window belongs.<br/>                                                               |
| [**SetWindowLong**](https://msdn.microsoft.com/en-us/library/ms633591(v=VS.85).aspx)       | Changes an attribute of the specified window. The function also sets the 32-bit (long) value at the specified offset into the extra window memory.<br/>                                                                 |
| [**SetWindowLongPtr**](https://msdn.microsoft.com/en-us/library/ms644898(v=VS.85).aspx) | Changes an attribute of the specified window. The function also sets a value at the specified offset in the extra window memory.<br/>                                                                                   |
| [**UnregisterClass**](https://msdn.microsoft.com/en-us/library/ms644899(v=VS.85).aspx)   | Unregisters a window class, freeing the memory required for the class. <br/>                                                                                                                                            |



 

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
<td><a href="https://msdn.microsoft.com/en-us/library/ms633578(v=VS.85).aspx"><strong>GetClassInfo</strong></a></td>
<td>Retrieves information about a window class. <br/>
<blockquote>
[!Note]<br />
The <a href="https://msdn.microsoft.com/en-us/library/ms633578(v=VS.85).aspx"><strong>GetClassInfo</strong></a> function has been superseded by the <a href="https://msdn.microsoft.com/en-us/library/ms633579(v=VS.85).aspx"><strong>GetClassInfoEx</strong></a> function. You can still use <strong>GetClassInfo</strong>, however, if you do not need information about the class small icon.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/en-us/library/ms633583(v=VS.85).aspx"><strong>GetClassWord</strong></a></td>
<td>Retrieves the 16-bit (<strong>WORD</strong>) value at the specified offset into the extra class memory for the window class to which the specified window belongs.
<blockquote>
[!Note]<br />
This function is deprecated for any use other than <em>nIndex</em> set to GCW_ATOM. The function is provided only for compatibility with 16-bit versions of Windows. Applications should use the <a href="https://msdn.microsoft.com/en-us/library/ms633580(v=VS.85).aspx"><strong>GetClassLong</strong></a> function.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/en-us/library/ms633588(v=VS.85).aspx"><strong>SetClassLong</strong></a></td>
<td>Replaces the specified 32-bit (<strong>long</strong>) value at the specified offset into the extra class memory or the <a href="https://msdn.microsoft.com/en-us/library/ms633577(v=VS.85).aspx"><strong>WNDCLASSEX</strong></a> structure for the class to which the specified window belongs.
<blockquote>
[!Note]<br />
This function has been superseded by the <a href="https://msdn.microsoft.com/en-us/library/ms633589(v=VS.85).aspx"><strong>SetClassLongPtr</strong></a> function. To write code that is compatible with both 32-bit and 64-bit versions of Windows, use <strong>SetClassLongPtr</strong>.
</blockquote>
<br/> <br/></td>
</tr>
</tbody>
</table>



 

### Window Class Structures



| Name                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WNDCLASS**](https://msdn.microsoft.com/en-us/library/ms633576(v=VS.85).aspx)     | Contains the window class attributes that are registered by the [**RegisterClass**](https://msdn.microsoft.com/en-us/library/ms633586(v=VS.85).aspx) function. <br/> This structure has been superseded by the [**WNDCLASSEX**](https://msdn.microsoft.com/en-us/library/ms633577(v=VS.85).aspx) structure used with the [**RegisterClassEx**](https://msdn.microsoft.com/en-us/library/ms633587(v=VS.85).aspx) function. You can still use [**WNDCLASS**](https://msdn.microsoft.com/en-us/library/ms633576(v=VS.85).aspx) and [**RegisterClass**](https://msdn.microsoft.com/en-us/library/ms633586(v=VS.85).aspx) if you do not need to set the small icon associated with the window class.<br/>                                                  |
| [**WNDCLASSEX**](https://msdn.microsoft.com/en-us/library/ms633577(v=VS.85).aspx) | Contains window class information. It is used with the [**RegisterClassEx**](https://msdn.microsoft.com/en-us/library/ms633587(v=VS.85).aspx) and [**GetClassInfoEx**](https://msdn.microsoft.com/en-us/library/ms633579(v=VS.85).aspx)  functions. <br/> The [**WNDCLASSEX**](https://msdn.microsoft.com/en-us/library/ms633577(v=VS.85).aspx) structure is similar to the [**WNDCLASS**](https://msdn.microsoft.com/en-us/library/ms633576(v=VS.85).aspx) structure. There are two differences. **WNDCLASSEX** includes the **cbSize** member, which specifies the size of the structure, and the **hIconSm** member, which contains a handle to a small icon associated with the window class.<br/> |



 

 

 




