---
title: STRICT Compliance
description: Some source code that compiles successfully might produce error messages when you enable STRICT type checking.
ms.assetid: 88368fec-b375-4ad0-aa13-ffadf0338a44
ms.topic: article
ms.date: 05/31/2018
---

# STRICT Compliance

Some source code that compiles successfully might produce error messages when you enable **STRICT** type checking. The following sections describe the minimal requirements for making your code compile when **STRICT** is enabled. Additional steps are recommended, especially to produce portable code.

## General Requirements

The principal requirement is that you must declare correct handle types and function pointers instead of relying on more general types. You cannot use one handle type where another is expected. This also means that you may have to change function declarations and use more type casts.

For best results, the generic **HANDLE** type should be used only when necessary.

## Declaring Functions Within Your Application

Make sure all application functions are declared. Placing all function declarations in an include file is recommended because you can easily scan your declarations and look for parameter and return types that should be changed.

If you use the **/Zg** compiler option to create header files for your functions, remember that you will get different results depending on whether you have enabled **STRICT** type checking. With **STRICT** disabled, all handle types generate the same base type. With **STRICT** enabled, they generate different base types. To avoid conflict, you need to re-create the header file each time you enable or disable **STRICT**, or edit the header file to use the types **HWND**, **HDC**, **HANDLE**, and so on, instead of the base types.

Any function declarations that you copied from Windows.h into your source code may have changed, and your local declaration may be out of date. Remove your local declaration.

## Types that Require Casts

Some functions have generic return types or parameters. For example, the [**SendMessage**](/windows/win32/api/winuser/nf-winuser-sendmessage) function returns data that may be any number of types, depending on the context. When you see any of these functions in your source code, make sure that you use the correct type cast and that it is as specific as possible. The following list is an example of these functions.

-   [**LocalLock**](/windows/desktop/api/winbase/nf-winbase-locallock)
-   [**GlobalLock**](/windows/desktop/api/winbase/nf-winbase-globallock)
-   [**GetWindowLong**](/windows/win32/api/winuser/nf-winuser-getwindowlonga)
-   [**SetWindowLong**](/windows/win32/api/winuser/nf-winuser-setwindowlonga)
-   [**SendMessage**](/windows/win32/api/winuser/nf-winuser-sendmessage)
-   [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)
-   [**SendDlgItemMessage**](/windows/win32/api/winuser/nf-winuser-senddlgitemmessagea)

When you call [**SendMessage**](/windows/win32/api/winuser/nf-winuser-sendmessage), [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca), or [**SendDlgItemMessage**](/windows/win32/api/winuser/nf-winuser-senddlgitemmessagea), you should first cast the result to type **UINT\_PTR**. You need to take similar steps for any function that returns an **LRESULT** or **LONG\_PTR** value, where the result contains a handle. This is necessary for writing portable code because the size of a handle varies, depending on the version of Windows. The (**UINT\_PTR**) cast ensures proper conversion. The following code shows an example in which **SendMessage** returns a handle to a brush:


```C++
HBRUSH hbr;

hbr = (HBRUSH)(UINT_PTR)SendMessage(hwnd, WM_CTLCOLOR, ..., ...);
```



The **CreateWindow** and **CreateWindowEx** parameter *hmenu* is sometimes used to pass an integer control identifier (ID). In this case, you must cast the ID to an **HMENU** type:


```C++
HWND hwnd;
int id;

hwnd = CreateWindow(
        TEXT("Button"), TEXT("OK"), BS_PUSHBUTTON,
        x, y, cx, cy, hwndParent,
        (HMENU)id,    // Cast required here
        hinst,
        NULL);
```



## Additional Considerations

To get the most benefit from **STRICT** type checking, there are additional guidelines you should follow. Your code will be more portable in future versions of Windows if you make the following changes.

The types **WPARAM**, **LPARAM**, **LRESULT**, and **LPVOID** are *polymorphic data types*. They hold different kinds of data at different times, even when **STRICT** type checking is enabled. To get the benefit of type checking, you should cast values of these types as soon as possible. (Note that message crackers automatically recast *wParam* and *lParam* for you in a portable way.)

Take special care to distinguish **HMODULE** and **HINSTANCE** types. Even with **STRICT** enabled, they are defined as the same base type. Most kernel module management functions use **HINSTANCE** types, but there are a few functions that return or accept only **HMODULE** types.

## Related topics

<dl> <dt>

[Disabling STRICT](disabling-strict.md)
</dt> <dt>

[Enabling STRICT](enabling-strict.md)
</dt> </dl>

 

 