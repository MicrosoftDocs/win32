---
title: Windows Coding Conventions
description: If you are new to Windows programming, it can be disconcerting when you first see a Windows program.
ms.assetid: 466a66db-7681-4fce-9672-07849cd1b096
ms.topic: article
ms.date: 05/31/2018
---

# Windows Coding Conventions

If you are new to Windows programming, it can be disconcerting when you first see a Windows program. The code is filled with strange type definitions like **DWORD\_PTR** and **LPRECT**, and variables have names like *hWnd* and *pwsz* (called Hungarian notation). It's worth taking a moment to learn some of the Windows coding conventions.

The vast majority of Windows APIs consist of either functions or Component Object Model (COM) interfaces. Very few Windows APIs are provided as C++ classes. (A notable exception is GDI+, one of the 2-D graphics APIs.)

## Typedefs

The Windows headers contain a lot of typedefs. Many of these are defined in the header file WinDef.h. Here are some that you will encounter often.

### Integer types

| Data type     | Size    | Signed?  |
|---------------|---------|----------|
| **BYTE**      | 8 bits  | Unsigned |
| **DWORD**     | 32 bits | Unsigned |
| **INT32**     | 32 bits | Signed   |
| **INT64**     | 64 bits | Signed   |
| **LONG**      | 32 bits | Signed   |
| **LONGLONG**  | 64 bits | Signed   |
| **UINT32**    | 32 bits | Unsigned |
| **UINT64**    | 64 bits | Unsigned |
| **ULONG**     | 32 bits | Unsigned |
| **ULONGLONG** | 64 bits | Unsigned |
| **WORD**      | 16 bits | Unsigned |

As you can see, there is a certain amount of redundancy in these typedefs. Some of this overlap is simply due to the history of the Windows APIs. The types listed here have fixed size, and the sizes are the same in both 32-bit and 64-applications. For example, the **DWORD** type is always 32 bits wide.

### Boolean Type

**BOOL** is a type alias for `int`, distinct from C++ **bool** and other types that represent [Boolean](https://en.wikipedia.org/wiki/Boolean_algebra). The header file WinDef.h also defines two values for use with **BOOL**.

```C++
#define FALSE    0 
#define TRUE     1
```

Despite this definition of **TRUE**, however, most functions that return a **BOOL** type can return any non-zero value to indicate Boolean truth. Therefore, you should always write this:

```C++
// Right way.
if (SomeFunctionThatReturnsBoolean()) 
{ 
    ...
}

// or

if (SomeFunctionThatReturnsBoolean() != FALSE)
{ 
    ...
}

```

and not this:

```C++
if (result == TRUE) // Wrong!
{
    ... 
}
```

Be aware that **BOOL** is an integer type and is not interchangeable with C++ **bool**.

### Pointer Types

Windows defines many data types of the form *pointer-to-X*. These usually have the prefix *P-* or *LP-* in the name. For example, **LPRECT** is a pointer to a [**RECT**](/previous-versions//dd162897(v=vs.85)), where **RECT** is a structure that describes a rectangle. The following variable declarations are equivalent.

```C++
RECT*  rect;  // Pointer to a RECT structure.
LPRECT rect;  // The same
PRECT  rect;  // Also the same.
```

On 16bit architectures (16-bit Windows) there are 2 types of pointers, *P* for "pointer" and *LP* stands for "long pointer". Long pointers (also called *far pointers*) were needed to address memory ranges outside the current segment. The *LP* prefix was preserved to make it easier to port 16-bit code to 32-bit Windows. Today there is no distinction — a pointer is a pointer. Avoid using these prefixes or if you must use one use *P*.

### Pointer Precision Types

The following data types are always the size of a pointer—that is, 32 bits wide in 32-bit applications, and 64 bits wide in 64-bit applications. The size is determined at compile time. When a 32-bit application runs on 64-bit Windows, these data types are still 4 bytes wide. (A 64-bit application cannot run on 32-bit Windows, so the reverse situation does not occur.)

-   **DWORD\_PTR**
-   **INT\_PTR**
-   **LONG\_PTR**
-   **ULONG\_PTR**
-   **UINT\_PTR**

These types are used in situations where an integer might be cast to a pointer. They are also used to define variables for pointer arithmetic and to define loop counters that iterate over the full range of bytes in memory buffers. More generally, they appear in places where an existing 32-bit value was expanded to 64 bits on 64-bit Windows.

## Hungarian Notation

*Hungarian notation* is the practice of adding prefixes to the names of variables, to give additional information about the variable. (The notation's inventor, Charles Simonyi, was Hungarian, hence its name).

In its original form, Hungarian notation gives *semantic* information about a variable, telling you the intended use. For example, *i* means an index, *cb* means a size in bytes ("count of bytes"), and *rw* and *col* mean row and column numbers. These prefixes are designed to avoid the accidental use of a variable in the wrong context. For example, if you saw the expression `rwPosition +  cbTable`, you would know that a row number is being added to a size, which is almost certainly a bug in the code

A more common form of Hungarian notation uses prefixes to give *type* information—for example, *dw* for **DWORD** and *w* for **WORD**.

Note, the cpp core guildines discourage practices like Hungarian notation, see [NL.5: Avoid encoding type information in names](https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md#nl5-avoid-encoding-type-information-in-names), and
internally, the Windows team no longer uses it. It's use remains in many samples.

## Next

[Working with Strings](working-with-strings.md)

 

 
