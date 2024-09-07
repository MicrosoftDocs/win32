---
title: Working with Strings
description: Working with Strings
ms.assetid: 876ff8bb-67c3-4dcc-aa94-7fbd915c67dc
ms.topic: article
ms.date: 07/03/2024
---

# Working with Strings

This topic explains how Windows supports Unicode strings for UI elements, file names, and so on (Unicode is the preferred character encoding because it supports all character sets and languages).

Windows represents Unicode characters using UTF-16 encoding, in which each character is encoded as one or two 16-bit values. To distinguish them from 8-bit ANSI characters, UTF-16 characters are called *wide* characters. The Visual C++ compiler supports the built-in data type **wchar\_t** for wide characters. The header file WinNT.h also defines the following **typedef**.

```C++
typedef wchar_t WCHAR;
```

To declare a wide-character literal or a wide-character string literal, put **L** before the literal.

```C++
wchar_t a = L'a';
wchar_t *str = L"hello";
```

The following table lists some other string-related typedefs:

| Typedef                   | Definition       |
|---------------------------|------------------|
| **CHAR**                  | `char`           |
| **PSTR** or **LPSTR**     | `char*`          |
| **PCSTR** or **LPCSTR**   | `const char*`    |
| **PWSTR** or **LPWSTR**   | `wchar_t*`       |
| **PCWSTR** or **LPCWSTR** | `const wchar_t*` |

> [!IMPORTANT]
> The **WCHAR** and **wchar_t** types are typically described as representing Unicode _characters_. However, it is more precise to say that they represent Unicode UTF-16 _code units_. The Unicode® Standard uses the term **character** to refer to the abstract text elements encoded by the standard, and **code unit** to refer to the typed values used to represent them in a Unicode encoding form. In UTF-16 encoding, Unicode characters are encoded as _one or two_ 16-bit code units. In Windows, WCHAR and wchar_t are always a single 16-bit code unit. While many Unicode characters are represented using a single WCHAR or wchar_t value, many other Unicode characters require a sequence of two such values. These pairs of UTF-16 code units are often referred to as **surrogate pairs**, and each of the 16-bit values in a surrogate pair is known as a **surrogate code unit**. When working with Unicode strings, it is important never to treat a single surrogate code unit as a complete character. See [Surrogates and Supplementary Characters](windows/win32/intl/surrogates-and-supplementary-characters) for more information.

## Unicode and ANSI Functions

When Microsoft introduced Unicode support to Windows, it eased the transition by providing two parallel sets of APIs, one for ANSI strings and the other for Unicode strings. For example, there are two functions to set the text of a window's title bar:

- **SetWindowTextA** takes an ANSI string.
- **SetWindowTextW** takes a Unicode string.

Internally, the ANSI version translates the string to Unicode. The Windows headers also define a macro that resolves to the Unicode version when the preprocessor symbol `UNICODE` is defined or the ANSI version otherwise.

```C++
#ifdef UNICODE
#define SetWindowText  SetWindowTextW
#else
#define SetWindowText  SetWindowTextA
#endif 
```

The function is documented under the name [**SetWindowText**](/windows/desktop/api/winuser/nf-winuser-setwindowtexta), even though that is really the macro name, not the actual function name.

New applications should always call the Unicode versions. Many world languages require Unicode. If you use ANSI strings, it will be impossible to localize your application. The ANSI versions are also less efficient, because the operating system must convert the ANSI strings to Unicode at run time. Depending on your preference, you can call the Unicode functions explicitly, such as **SetWindowTextW**, or use the macros. Most recent Windows APIs typically have just a Unicode version.

## TCHARs

In some cases it might be useful to compile the same code for either ANSI or Unicode strings, depending on the target platform. To this end, the Windows SDK provides macros that map strings to Unicode or ANSI, depending on the platform.

| Macro     | Unicode   | ANSI   |
|-----------|-----------|--------|
| TCHAR     | `wchar_t` | `char` |
| `TEXT("x")` or `_T("x")` | `L"x"`    | `"x"`  |

For example, the following code:

```C++
SetWindowText(TEXT("My Application"));
```

resolves to one of the following:

```C++
SetWindowTextW(L"My Application"); // Unicode function with wide-character string.

SetWindowTextA("My Application");  // ANSI function.
```

The **TEXT** and **TCHAR** macros are less useful today, because all applications should use Unicode.

The headers for the Microsoft C run-time libraries define a similar set of macros. For example, **\_tcslen** resolves to **strlen** if `_UNICODE` is undefined; otherwise it resolves to **wcslen**, which is the wide-character version of **strlen**.

```C++
#ifdef _UNICODE
#define _tcslen     wcslen
#else
#define _tcslen     strlen
#endif 
```

Be careful: Some headers use the preprocessor symbol `UNICODE`, others use `_UNICODE` with an underscore prefix. Always define both symbols. Visual C++ sets them both by default when you create a new project.

## Next

[What Is a Window?](what-is-a-window-.md)
