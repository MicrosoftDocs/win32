---
description: This topic describes the types of window classes, how the system locates them, and the elements that define the default behavior of windows that belong to them.
ms.assetid: 'vs|winui|~\winui\windowsuserinterface\windowing\window_89windowclasse.htm'
title: Window Classes (Windows and Messages)
ms.topic: article
ms.date: 05/31/2018
---

# Window Classes (Windows and Messages)

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
| [**GetClassInfoEx**](/windows/win32/api/winuser/nf-winuser-getclassinfoexa)     | Retrieves information about a window class, including a handle to the small icon associated with the window class. The [**GetClassInfo**](/windows/win32/api/winuser/nf-winuser-getclassinfoa) function does not retrieve a handle to the small icon.<br/> |
| [**GetClassLong**](/windows/win32/api/winuser/nf-winuser-getclasslonga)         | Retrieves the specified 32-bit (**long**) value from the [**WNDCLASSEX**](/windows/win32/api/winuser/ns-winuser-wndclassexa) structure associated with the specified window. <br/>                                                                         |
| [**GetClassLongPtr**](/windows/win32/api/winuser/nf-winuser-getclasslongptra)   | Retrieves the specified value from the [**WNDCLASSEX**](/windows/win32/api/winuser/ns-winuser-wndclassexa) structure associated with the specified window.<br/>                                                                                            |
| [**GetClassName**](/windows/win32/api/winuser/nf-winuser-getclassname)         | Retrieves the name of the class to which the specified window belongs. <br/>                                                                                                                                            |
| [**GetWindowLong**](/windows/win32/api/winuser/nf-winuser-getwindowlonga)       | Retrieves information about the specified window. The function also retrieves the 32-bit (**long**) value at the specified offset into the extra window memory.<br/>                                                    |
| [**GetWindowLongPtr**](/windows/win32/api/winuser/nf-winuser-getwindowlongptra) | Retrieves information about the specified window. The function also retrieves the value at a specified offset into the extra window memory.<br/>                                                                        |
| [**RegisterClass**](/windows/win32/api/winuser/nf-winuser-registerclassa)       | Registers a window class for subsequent use in calls to the [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa) or [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function.<br/>                                                             |
| [**RegisterClassEx**](/windows/win32/api/winuser/nf-winuser-registerclassexa)   | Registers a window class for subsequent use in calls to the [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa) or [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function. <br/>                                                            |
| [**SetClassLongPtr**](/windows/win32/api/winuser/nf-winuser-setclasslongptra)   | Replaces the specified value at the specified offset in the extra class memory or the [**WNDCLASSEX**](/windows/win32/api/winuser/ns-winuser-wndclassexa) structure for the class to which the specified window belongs.<br/>                              |
| [**SetClassWord**](/windows/win32/api/winuser/nf-winuser-setclassword)         | Replaces the 16-bit (**WORD**) value at the specified offset into the extra class memory for the window class to which the specified window belongs.<br/>                                                               |
| [**SetWindowLong**](/windows/win32/api/winuser/nf-winuser-setwindowlonga)       | Changes an attribute of the specified window. The function also sets the 32-bit (long) value at the specified offset into the extra window memory.<br/>                                                                 |
| [**SetWindowLongPtr**](/windows/win32/api/winuser/nf-winuser-setwindowlongptra) | Changes an attribute of the specified window. The function also sets a value at the specified offset in the extra window memory.<br/>                                                                                   |
| [**UnregisterClass**](/windows/win32/api/winuser/nf-winuser-unregisterclassa)   | Unregisters a window class, freeing the memory required for the class. <br/>                                                                                                                                            |



 

The following functions are obsolete.




| Name | Description | 
|------|-------------|
| <a href="/windows/desktop/api/winuser/nf-winuser-getclassinfoa"><strong>GetClassInfo</strong></a> | Retrieves information about a window class. <br /><blockquote>[!Note]<br />The <a href="/windows/desktop/api/winuser/nf-winuser-getclassinfoa"><strong>GetClassInfo</strong></a> function has been superseded by the <a href="/windows/desktop/api/winuser/nf-winuser-getclassinfoexa"><strong>GetClassInfoEx</strong></a> function. You can still use <strong>GetClassInfo</strong>, however, if you do not need information about the class small icon.</blockquote><br /> | 
| <a href="/windows/desktop/api/winuser/nf-winuser-getclassword"><strong>GetClassWord</strong></a> | Retrieves the 16-bit (<strong>WORD</strong>) value at the specified offset into the extra class memory for the window class to which the specified window belongs.<blockquote>[!Note]<br />This function is deprecated for any use other than <em>nIndex</em> set to GCW_ATOM. The function is provided only for compatibility with 16-bit versions of Windows. Applications should use the <a href="/windows/desktop/api/winuser/nf-winuser-getclasslonga"><strong>GetClassLong</strong></a> function.</blockquote><br /><br /> | 
| <a href="/windows/desktop/api/winuser/nf-winuser-setclasslonga"><strong>SetClassLong</strong></a> | Replaces the specified 32-bit (<strong>long</strong>) value at the specified offset into the extra class memory or the <a href="/windows/win32/api/winuser/ns-winuser-wndclassexa"><strong>WNDCLASSEX</strong></a> structure for the class to which the specified window belongs.<blockquote>[!Note]<br />This function has been superseded by the <a href="/windows/desktop/api/winuser/nf-winuser-setclasslongptra"><strong>SetClassLongPtr</strong></a> function. To write code that is compatible with both 32-bit and 64-bit versions of Windows, use <strong>SetClassLongPtr</strong>.</blockquote><br /><br /> | 




 

### Window Class Structures



| Name                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WNDCLASS**](/windows/win32/api/winuser/ns-winuser-wndclassa)     | Contains the window class attributes that are registered by the [**RegisterClass**](/windows/win32/api/winuser/nf-winuser-registerclassa) function. <br/> This structure has been superseded by the [**WNDCLASSEX**](/windows/win32/api/winuser/ns-winuser-wndclassexa) structure used with the [**RegisterClassEx**](/windows/win32/api/winuser/nf-winuser-registerclassexa) function. You can still use [**WNDCLASS**](/windows/win32/api/winuser/ns-winuser-wndclassa) and [**RegisterClass**](/windows/win32/api/winuser/nf-winuser-registerclassa) if you do not need to set the small icon associated with the window class.<br/>                                                  |
| [**WNDCLASSEX**](/windows/win32/api/winuser/ns-winuser-wndclassexa) | Contains window class information. It is used with the [**RegisterClassEx**](/windows/win32/api/winuser/nf-winuser-registerclassexa) and [**GetClassInfoEx**](/windows/win32/api/winuser/nf-winuser-getclassinfoexa)  functions. <br/> The [**WNDCLASSEX**](/windows/win32/api/winuser/ns-winuser-wndclassexa) structure is similar to the [**WNDCLASS**](/windows/win32/api/winuser/ns-winuser-wndclassa) structure. There are two differences. **WNDCLASSEX** includes the **cbSize** member, which specifies the size of the structure, and the **hIconSm** member, which contains a handle to a small icon associated with the window class.<br/> |



 

 

 
