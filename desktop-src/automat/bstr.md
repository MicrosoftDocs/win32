---
title: BSTR
description: A BSTR (Basic string or binary string) is a string data type that is used by COM, Automation, and Interop functions.
ms.assetid: '1b2d7d2c-47af-4389-a6b6-b01b7e915228'
keywords: ["OLECHAR", "BSTR", "LPBSTR"]
---

# BSTR

A BSTR (Basic string or binary string) is a string data type that is used by COM, Automation, and Interop functions. Use the BSTR data type in all interfaces that will be accessed from script.


```C++
typedef WCHAR OLECHAR;
typedef OLECHAR* BSTR;
typedef BSTR* LPBSTR;
```



## Remarks

A BSTR is a composite data type that consists of a length prefix, a data string, and a terminator. The following table describes these components.



| Item          | Description                                                                                                                                                                                           |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Length prefix | A four-byte integer that contains the number of bytes in the following data string. It appears immediately before the first character of the data string. This value does not include the terminator. |
| Data string   | A string of Unicode characters. May contain multiple embedded null characters.                                                                                                                        |
| Terminator    | A NULL (0x0000) WCHAR.                                                                                                                                                                                |



 

Previously, some versions of Mac operating systems defined this data type in a different way, and some Microsoft code running on Mac computers used this data type. This documentation no longer describes these obsolete details.

A BSTR is a pointer. The pointer points to the first character of the data string, not to the length prefix.

BSTRs are allocated using COM memory allocation functions, so they can be returned from methods without concern for memory allocation.

The following code is incorrect:

`BSTR  MyBstr = L"I am a happy BSTR";`

This code builds (compiles and links) correctly, but it will not function properly because the string does not have a length prefix. If you use a debugger to examine the memory location of this variable, you will not see a four-byte length prefix preceding the data string.

Instead, use the following code:

`BSTR  MyBstr = SysAllocString(L"I am a happy BSTR");`

A debugger that examines the memory location of this variable will now reveal a length prefix containing the value 34. This is the expected value for a 17-byte character string that is represented as a wide-string literal through the inclusion of the "L" string prefix. The debugger will also show the terminator that appears after the data string.

If you pass a wide-string literal as an argument to a COM function that is expecting a BSTR, the COM function behaves unexpectedly.

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>WTypes.h</dt> </dl> |



 

 





