---
title: Rules for Using Pointers
description: Porting your code to compile for both 32- and 64-bit Microsoft Windows is straightforward. You need only follow a few simple rules about casting pointers, and use the new data types in your code. The rules for pointer manipulation are as follows.
ms.assetid: 4c38bee2-fa1c-493f-a12d-e673df4d4895
keywords:
- rules for using pointers 64-bit Windows Programming
- pointer manipulation 64-bit Windows Programming
- casting pointers 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# Rules for Using Pointers

Porting your code to compile for both 32- and 64-bit Microsoft Windows is straightforward. You need only follow a few simple rules about casting pointers, and use the new data types in your code. The rules for pointer manipulation are as follows.

1.  Do not cast pointers to **int**, **long**, **ULONG**, or **DWORD**.

    If you must cast a pointer to test some bits, set or clear bits, or otherwise manipulate its contents, use the **UINT\_PTR** or **INT\_PTR** type. These types are integral types that scale to the size of a pointer for both 32- and 64-bit Windows (for example, **ULONG** for 32-bit Windows and \_int64 for 64-bit Windows). For example, assume you are porting the following code:

    `ImageBase = (PVOID)((ULONG)ImageBase | 1);`

    As a part of the porting process, you would change the code as follows:

    `ImageBase = (PVOID)((ULONG_PTR)ImageBase | 1);`

    Use **UINT\_PTR** and **INT\_PTR** where appropriate (and if you are uncertain whether they are required, there is no harm in using them just in case). Do not cast your pointers to the types **ULONG**, **LONG**, **INT**, **UINT**, or **DWORD**.

    Note that **HANDLE** is defined as a **void\***, so typecasting a **HANDLE** value to a **ULONG** value to test, set, or clear the low-order 2 bits is an error on 64-bit Windows.

2.  Use the **PtrToLong** or **PtrToUlong** function to truncate pointers.

    If you must truncate a pointer to a 32-bit value, use the **PtrToLong** or **PtrToUlong** function (defined in Basetsd.h). These functions disable the pointer truncation warning for the duration of the call.

    Use these functions carefully. After you convert a pointer variable using one of these functions, never use it as a pointer again. These functions truncate the upper 32 bits of an address, which are usually needed to access the memory originally referenced by pointer. Using these functions without careful consideration will result in fragile code.

3.  Be careful when using POINTER\_32 values in code that may be compiled as 64-bit code. The compiler will sign-extend the pointer when it is assigned to a native pointer in 64-bit code, not zero-extend the pointer.
4.  Be careful when using POINTER\_64 values in code that may be compiled as 32-bit code. The compiler will sign-extend the pointer in 32-bit code, not zero-extend the pointer.
5.  Be careful using OUT parameters.

    For example, suppose you have a function defined as follows:

    `void func( OUT PULONG *PointerToUlong );`

    Do not call this function as follows.

    ``` syntax
    ULONG ul;
    PULONG lp;
    func((PULONG *)&ul);
    lp = (PULONG)ul;
    ```

    Instead, use the following call.

    ``` syntax
    PULONG lp;
    func(&lp);
    ```

    Typecasting &ul to **PULONG\*** prevents a compiler error, but the function will write a 64-bit pointer value into the memory at &ul. This code works on 32-bit Windows, but will cause data corruption on 64-bit Windows and it will be subtle, hard-to-find corruption. The bottom line: Do not play tricks with the C code—straightforward and simple is better.

6.  Be careful with polymorphic interfaces.

    Do not create functions that accept **DWORD** parameters for polymorphic data. If the data can be a pointer or an integral value, use the UINT\_PTR or **PVOID** type.

    For example, do not create a function that accepts an array of exception parameters typed as **DWORD** values. The array should be an array of **DWORD\_PTR** values. Therefore, the array elements can hold addresses or 32-bit integral values. (The general rule is that if the original type is **DWORD** and it needs to be pointer width, convert it to a **DWORD\_PTR** value. That is why there are corresponding pointer-precision types.) If you have code that uses **DWORD**, **ULONG**, or other 32-bit types in a polymorphic way (that is, you really want the parameter or structure member to hold an address), use **UINT\_PTR** in place of the current type.

7.  Use the new window class functions.

    If you have window or class private data that contains pointers, your code will need to use the following new functions:

    -   [**GetClassLongPtr**](/windows/win32/api/winuser/nf-winuser-getclasslongptra)
    -   [**GetWindowLongPtr**](/windows/win32/api/winuser/nf-winuser-getwindowlongptra)
    -   [**SetClassLongPtr**](/windows/win32/api/winuser/nf-winuser-setclasslongptra)
    -   [**SetWindowLongPtr**](/windows/win32/api/winuser/nf-winuser-setwindowlongptra)

    These functions can be used on both 32- and 64-bit Windows, but they are required on 64-bit Windows. Prepare for the transition by using these functions now.

    Additionally, you must access pointers or handles in class private data using the new functions on 64-bit Windows. To aid you in finding these cases, the following indexes are not defined in Winuser.h during a 64-bit compile:

    -   GWL\_WNDPROC
    -   GWL\_HINSTANCE
    -   GWL\_HWNDPARENT
    -   GWL\_USERDATA

    Instead, Winuser.h defines the following new indexes:

    -   GWLP\_WNDPROC
    -   GWLP\_HINSTANCE
    -   GWLP\_HWNDPARENT
    -   GWLP\_USERDATA
    -   GWLP\_ID

    For example, the following code does not compile:

    `SetWindowLong(hWnd, GWL_WNDPROC, (LONG)MyWndProc);`

    It should be changed as follows:

    `SetWindowLongPtr(hWnd, GWLP_WNDPROC, (LONG_PTR)MyWndProc);`

    When setting the **cbWndExtra** member of the [**WNDCLASS**](/windows/win32/api/winuser/ns-winuser-wndclassa) structure, be sure to reserve enough space for pointers. For example, if you are currently reserving sizeof(DWORD) bytes for a pointer value, reserve sizeof(DWORD\_PTR) bytes.

8.  Access all window and class data using **FIELD\_OFFSET**.

    It is common to access window data using hard-coded offsets. This technique is not portable to 64-bit Windows. To make your code portable, access your window and class data using the **FIELD\_OFFSET** macro. Do not assume that the second pointer has an offset of 4.

9.  The **LPARAM**, **WPARAM**, and **LRESULT** types change size with the platform.

    When compiling 64-bit code, these types expand to 64 bits, because they typically hold pointers or integral types. Do not mix these values with **DWORD**, **ULONG**, **UINT**, **INT**, **int**, or **long** values. Examine how you use these types and ensure that you do not inadvertently truncate values.

 

 
