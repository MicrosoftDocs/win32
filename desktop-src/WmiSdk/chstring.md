---
Description: The following table lists the CHString methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e2e4378f-d842-4bca-bffc-a60e718caed3
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: CHString class
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# CHString class

\[The **CHString** class is part of the WMI Provider Framework which is now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](https://msdn.microsoft.com/library/jj152383) should be used for all new development.\]

The following table lists the **CHString** methods.

## Members

The **CHString** class has these types of members:

-   [Constructors](#constructors)
-   [Methods](#methods)
-   [Operators](#operators)

### Constructors

The **CHString** class has these constructors.



| Constructor                           | Description                                                 |
|:--------------------------------------|:------------------------------------------------------------|
| [**CHString**](/windows/win32/ChString/nf-chstring-chstring-chstring(const chstring &)?branch=master) | Constructs **CHString** strings in various ways.<br/> |



 

### Methods

The **CHString** class has these methods.



| Method                                                    | Description                                                                                                    |
|:----------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|
| [**AllocSysString**](/windows/win32/ChString/nf-chstring-chstring-allocsysstring?branch=master)         | Allocates a BSTR from **CHString** data.<br/>                                                            |
| [**Collate**](/windows/win32/ChString/nf-chstring-chstring-collate?branch=master)                       | Compares two strings (case sensitive; uses locale-specific information).<br/>                            |
| [**Compare**](/windows/win32/ChString/nf-chstring-chstring-compare?branch=master)                       | Compares two strings (case sensitive).<br/>                                                              |
| [**CompareNoCase**](/windows/win32/ChString/nf-chstring-chstring-comparenocase?branch=master)           | Compares two strings (case insensitive).<br/>                                                            |
| [**Empty**](/windows/win32/ChString/nf-chstring-chstring-empty?branch=master)                           | Forces a string to have 0 (zero) length.<br/>                                                            |
| [**Find**](/windows/win32/ChString/nf-chstring-chstring-find?branch=master)                             | Overloaded. Finds a character or substring inside a larger string.<br/>                                  |
| [**FindOneOf**](/windows/win32/ChString/nf-chstring-chstring-findoneof?branch=master)                   | Finds the first matching character from a set.<br/>                                                      |
| [**Format**](/windows/win32/ChString/nf-chstring-chstring-format(uint,---)?branch=master)                         | Overloaded. Formats the string as **sprintf** does.<br/>                                                 |
| [**FormatMessageW**](/windows/win32/ChString/nf-chstring-chstring-formatmessagew(uint,---)?branch=master)         | Overloaded. Formats a message string.<br/>                                                               |
| [**FormatV**](/windows/win32/ChString/nf-chstring-chstring-formatv?branch=master)                       | Formats the string as **vsprintf** does.<br/>                                                            |
| [**FreeExtra**](/windows/win32/ChString/nf-chstring-chstring-freeextra?branch=master)                   | Removes any overhead of this string by freeing any extra memory previously allocated to the string.<br/> |
| [**GetAllocLength**](/windows/win32/ChString/nf-chstring-chstring-getalloclength?branch=master)         | Returns the size of the string buffer.<br/>                                                              |
| [**GetAt**](/windows/win32/ChString/nf-chstring-chstring-getat(int)?branch=master)                           | Overloaded. Returns the character at a given position.<br/>                                              |
| [**GetBuffer**](/windows/win32/ChString/nf-chstring-chstring-getbuffer?branch=master)                   | Returns a pointer to the characters in the **CHString** string.<br/>                                     |
| [**GetBufferSetLength**](/windows/win32/ChString/nf-chstring-chstring-getbuffersetlength?branch=master) | Returns a pointer to the characters in the **CHString** string, truncating to the specified length.<br/> |
| [**GetData**](/windows/win32/ChString/nf-chstring-chstring-getdata?branch=master)                       | Returns a pointer to the data in the **CHString** string.<br/>                                           |
| [**GetLength**](/windows/win32/ChString/nf-chstring-chstring-getlength?branch=master)                   | Returns the number of Unicode characters in a **CHString** string.<br/>                                  |
| [**IsEmpty**](/windows/win32/ChString/nf-chstring-chstring-isempty?branch=master)                       | Tests whether a **CHString** string contains no characters.<br/>                                         |
| [**Left**](/windows/win32/ChString/nf-chstring-chstring-left?branch=master)                             | Extracts the left part of a string (like the Basic **LEFT$** function).<br/>                             |
| [**LoadStringW**](/windows/win32/ChString/nf-chstring-chstring-loadstringw(uint)?branch=master)               | Loads an existing **CHString** string from a resource file.<br/>                                         |
| [**LockBuffer**](/windows/win32/ChString/nf-chstring-chstring-lockbuffer?branch=master)                 | Disables reference counting and protects the string in the buffer.<br/>                                  |
| [**MakeLower**](/windows/win32/ChString/nf-chstring-chstring-makelower?branch=master)                   | Converts all of the characters in this string to lowercase characters.<br/>                              |
| [**MakeReverse**](/windows/win32/ChString/nf-chstring-chstring-makereverse?branch=master)               | Reverses the characters in this string.<br/>                                                             |
| [**MakeUpper**](/windows/win32/ChString/nf-chstring-chstring-makeupper?branch=master)                   | Converts all of the characters in this string to uppercase characters.<br/>                              |
| [**Mid**](/windows/win32/ChString/nf-chstring-chstring-mid?branch=master)                               | Overloaded. Extracts the middle part of a string (like the Basic **MID$** function).<br/>                |
| [**ReleaseBuffer**](/windows/win32/ChString/nf-chstring-chstring-releasebuffer?branch=master)           | Releases control of the buffer returned by [**GetBuffer**](/windows/win32/ChString/nf-chstring-chstring-getbuffer?branch=master).<br/>                 |
| [**ReverseFind**](/windows/win32/ChString/nf-chstring-chstring-reversefind?branch=master)               | Finds a character inside a larger string; starts from the end.<br/>                                      |
| [**Right**](/windows/win32/ChString/nf-chstring-chstring-right?branch=master)                           | Extracts the right part of a string (like the Basic **RIGHT$** function).<br/>                           |
| [**SetAt**](/windows/win32/ChString/nf-chstring-chstring-setat?branch=master)                           | Sets a character at a given position.<br/>                                                               |
| [**SpanExcluding**](/windows/win32/ChString/nf-chstring-chstring-spanexcluding?branch=master)           | Extracts a substring that contains only the characters that are not in the set.<br/>                     |
| [**SpanIncluding**](/windows/win32/ChString/nf-chstring-chstring-spanincluding?branch=master)           | Extracts a substring that contains only the characters in a set.<br/>                                    |
| [**TrimLeft**](/windows/win32/ChString/nf-chstring-chstring-trimleft?branch=master)                     | Trims leading whitespace characters from the string.<br/>                                                |
| [**TrimRight**](/windows/win32/ChString/nf-chstring-chstring-trimright?branch=master)                   | Trims trailing whitespace characters from the string.<br/>                                               |
| [**UnlockBuffer**](/windows/win32/ChString/nf-chstring-chstring-unlockbuffer?branch=master)             | Enables reference counting and releases the string in the buffer.<br/>                                   |



 

### Operators

The **CHString** class has these operators.



| Operator                                                                                            | Description                                                                                                       |
|:----------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------|
| [**operator != (CHString, CHString)**](/windows/win32/ChString/?branch=master)            | Compares two **CHStrings** for inequality.<br/>                                                             |
| [**operator != (CHString, LPCWSTR)**](/windows/win32/ChString/?branch=master)              | Compares a **CHString** with a **LPCWSTR** for inequality.<br/>                                             |
| [**operator \[\]**](/windows/win32/ChString/?branch=master)                                                | Returns the character at a given position   operator substitution for [**GetAt**](/windows/win32/ChString/nf-chstring-chstring-getat(int)?branch=master).<br/> |
| [**operator +**](chstring--operator-plus.md)                                                       | Concatenates two strings and returns a new string.<br/>                                                     |
| [**operator +=**](chstring--operator-plus-equal.md)                                                | Concatenates a new string to the end of an existing string.<br/>                                            |
| [**operator &lt; (CHString, LPCWSTR)**](/windows/win32/ChString/?branch=master)            | Compares a **CHString** with a **LPCWSTR**.<br/>                                                            |
| [**operator &lt; (CHString, CHString)**](/windows/win32/ChString/?branch=master)          | Compares two **CHStrings**.<br/>                                                                            |
| [**operator &lt;= (CHString, CHString)**](/windows/win32/ChString/?branch=master)    | Compares two **CHStrings**.<br/>                                                                            |
| [**operator &lt;= (CHString, LPCWSTR)**](/windows/win32/ChString/?branch=master)      | Compares a **CHString** with a **LPCWSTR**.<br/>                                                            |
| [**operator =**](chstring--operator-equal.md)                                                      | Assigns a new value to a **CHString** string.<br/>                                                          |
| [**operator == (CHString, CHString)**](/windows/win32/ChString/?branch=master)          | Compares two **CHStrings** for equality.<br/>                                                               |
| [**operator == (CHString, LPCWSTR)**](/windows/win32/ChString/?branch=master)            | Compares a **CHString** with a **LPCWSTR** for equality.<br/>                                               |
| [**operator &gt; (CHString, CHString)**](/windows/win32/ChString/?branch=master)       | Compares two **CHStrings**.<br/>                                                                            |
| [**operator &gt; (CHString, LPCWSTR)**](/windows/win32/ChString/?branch=master)         | Compares a **CHString** with a **LPCWSTR**.<br/>                                                            |
| [**operator &gt;= (CHString, CHString)**](/windows/win32/ChString/?branch=master) | Compares two **CHStrings**.<br/>                                                                            |
| [**operator &gt;= (CHString, LPCWSTR)**](/windows/win32/ChString/?branch=master)   | Compares a **CHString** with a **LPCWSTR**.<br/>                                                            |
| [**operator LPCWSTR**](/windows/win32/ChString/nf-chstring-chstring-operator lpcwstr?branch=master)                                               | Directly accesses characters stored in a **CHString** string as a C-style string.<br/>                      |



 

## Remarks

The destructor for the class is **CHString::~CHString**.

## Requirements



|                                     |                                                                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                                                                |
| Header<br/>                   | <dl> <dt>ChString.h (include FwCommon.h)</dt> </dl>                                                    |
| Library<br/>                  | <dl> <dt>FrameDyn.lib</dt> </dl>                                                                       |
| DLL<br/>                      | <dl> <dt>FrameDynOS.dll; </dt> <dt>FrameDyn.dll</dt> </dl> |



 

 




