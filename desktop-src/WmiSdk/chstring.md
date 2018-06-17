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
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
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
| [**CHString**](/windows/desktop/api/ChString/nf-chstring-chstring-chstring(const chstring &)) | Constructs **CHString** strings in various ways.<br/> |



 

### Methods

The **CHString** class has these methods.



| Method                                                    | Description                                                                                                    |
|:----------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|
| [**AllocSysString**](/windows/desktop/api/ChString/nf-chstring-chstring-allocsysstring)         | Allocates a BSTR from **CHString** data.<br/>                                                            |
| [**Collate**](/windows/desktop/api/ChString/nf-chstring-chstring-collate)                       | Compares two strings (case sensitive; uses locale-specific information).<br/>                            |
| [**Compare**](/windows/desktop/api/ChString/nf-chstring-chstring-compare)                       | Compares two strings (case sensitive).<br/>                                                              |
| [**CompareNoCase**](/windows/desktop/api/ChString/nf-chstring-chstring-comparenocase)           | Compares two strings (case insensitive).<br/>                                                            |
| [**Empty**](/windows/desktop/api/ChString/nf-chstring-chstring-empty)                           | Forces a string to have 0 (zero) length.<br/>                                                            |
| [**Find**](/windows/desktop/api/ChString/nf-chstring-chstring-find)                             | Overloaded. Finds a character or substring inside a larger string.<br/>                                  |
| [**FindOneOf**](/windows/desktop/api/ChString/nf-chstring-chstring-findoneof)                   | Finds the first matching character from a set.<br/>                                                      |
| [**Format**](/windows/desktop/api/ChString/nf-chstring-chstring-format(uint_---))                         | Overloaded. Formats the string as **sprintf** does.<br/>                                                 |
| [**FormatMessageW**](/windows/desktop/api/ChString/nf-chstring-chstring-formatmessagew(uint_---))         | Overloaded. Formats a message string.<br/>                                                               |
| [**FormatV**](/windows/desktop/api/ChString/nf-chstring-chstring-formatv)                       | Formats the string as **vsprintf** does.<br/>                                                            |
| [**FreeExtra**](/windows/desktop/api/ChString/nf-chstring-chstring-freeextra)                   | Removes any overhead of this string by freeing any extra memory previously allocated to the string.<br/> |
| [**GetAllocLength**](/windows/desktop/api/ChString/nf-chstring-chstring-getalloclength)         | Returns the size of the string buffer.<br/>                                                              |
| [**GetAt**](/windows/desktop/api/ChString/nf-chstring-chstring-getat(int))                           | Overloaded. Returns the character at a given position.<br/>                                              |
| [**GetBuffer**](/windows/desktop/api/ChString/nf-chstring-chstring-getbuffer)                   | Returns a pointer to the characters in the **CHString** string.<br/>                                     |
| [**GetBufferSetLength**](/windows/desktop/api/ChString/nf-chstring-chstring-getbuffersetlength) | Returns a pointer to the characters in the **CHString** string, truncating to the specified length.<br/> |
| [**GetData**](/windows/desktop/api/ChString/nf-chstring-chstring-getdata)                       | Returns a pointer to the data in the **CHString** string.<br/>                                           |
| [**GetLength**](/windows/desktop/api/ChString/nf-chstring-chstring-getlength)                   | Returns the number of Unicode characters in a **CHString** string.<br/>                                  |
| [**IsEmpty**](/windows/desktop/api/ChString/nf-chstring-chstring-isempty)                       | Tests whether a **CHString** string contains no characters.<br/>                                         |
| [**Left**](/windows/desktop/api/ChString/nf-chstring-chstring-left)                             | Extracts the left part of a string (like the Basic **LEFT$** function).<br/>                             |
| [**LoadStringW**](/windows/desktop/api/ChString/nf-chstring-chstring-loadstringw(uint))               | Loads an existing **CHString** string from a resource file.<br/>                                         |
| [**LockBuffer**](/windows/desktop/api/ChString/nf-chstring-chstring-lockbuffer)                 | Disables reference counting and protects the string in the buffer.<br/>                                  |
| [**MakeLower**](/windows/desktop/api/ChString/nf-chstring-chstring-makelower)                   | Converts all of the characters in this string to lowercase characters.<br/>                              |
| [**MakeReverse**](/windows/desktop/api/ChString/nf-chstring-chstring-makereverse)               | Reverses the characters in this string.<br/>                                                             |
| [**MakeUpper**](/windows/desktop/api/ChString/nf-chstring-chstring-makeupper)                   | Converts all of the characters in this string to uppercase characters.<br/>                              |
| [**Mid**](/windows/desktop/api/ChString/nf-chstring-chstring-mid)                               | Overloaded. Extracts the middle part of a string (like the Basic **MID$** function).<br/>                |
| [**ReleaseBuffer**](/windows/desktop/api/ChString/nf-chstring-chstring-releasebuffer)           | Releases control of the buffer returned by [**GetBuffer**](/windows/desktop/api/ChString/nf-chstring-chstring-getbuffer).<br/>                 |
| [**ReverseFind**](/windows/desktop/api/ChString/nf-chstring-chstring-reversefind)               | Finds a character inside a larger string; starts from the end.<br/>                                      |
| [**Right**](/windows/desktop/api/ChString/nf-chstring-chstring-right)                           | Extracts the right part of a string (like the Basic **RIGHT$** function).<br/>                           |
| [**SetAt**](/windows/desktop/api/ChString/nf-chstring-chstring-setat)                           | Sets a character at a given position.<br/>                                                               |
| [**SpanExcluding**](/windows/desktop/api/ChString/nf-chstring-chstring-spanexcluding)           | Extracts a substring that contains only the characters that are not in the set.<br/>                     |
| [**SpanIncluding**](/windows/desktop/api/ChString/nf-chstring-chstring-spanincluding)           | Extracts a substring that contains only the characters in a set.<br/>                                    |
| [**TrimLeft**](/windows/desktop/api/ChString/nf-chstring-chstring-trimleft)                     | Trims leading whitespace characters from the string.<br/>                                                |
| [**TrimRight**](/windows/desktop/api/ChString/nf-chstring-chstring-trimright)                   | Trims trailing whitespace characters from the string.<br/>                                               |
| [**UnlockBuffer**](/windows/desktop/api/ChString/nf-chstring-chstring-unlockbuffer)             | Enables reference counting and releases the string in the buffer.<br/>                                   |



 

### Operators

The **CHString** class has these operators.



| Operator                                                                                            | Description                                                                                                       |
|:----------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------|
| [**operator != (CHString, CHString)**](https://msdn.microsoft.com/en-us/library/Aa385704(v=VS.85).aspx)            | Compares two **CHStrings** for inequality.<br/>                                                             |
| [**operator != (CHString, LPCWSTR)**](https://msdn.microsoft.com/en-us/library/Aa385763(v=VS.85).aspx)              | Compares a **CHString** with a **LPCWSTR** for inequality.<br/>                                             |
| [**operator \[\]**](https://msdn.microsoft.com/en-us/library/Aa386162(v=VS.85).aspx)                                                | Returns the character at a given position   operator substitution for [**GetAt**](/windows/desktop/api/ChString/nf-chstring-chstring-getat(int)).<br/> |
| [**operator +**](chstring--operator-plus.md)                                                       | Concatenates two strings and returns a new string.<br/>                                                     |
| [**operator +=**](chstring--operator-plus-equal.md)                                                | Concatenates a new string to the end of an existing string.<br/>                                            |
| [**operator &lt; (CHString, LPCWSTR)**](https://msdn.microsoft.com/en-us/library/Aa385695(v=VS.85).aspx)            | Compares a **CHString** with a **LPCWSTR**.<br/>                                                            |
| [**operator &lt; (CHString, CHString)**](https://msdn.microsoft.com/en-us/library/Aa385689(v=VS.85).aspx)          | Compares two **CHStrings**.<br/>                                                                            |
| [**operator &lt;= (CHString, CHString)**](https://msdn.microsoft.com/en-us/library/Aa385676(v=VS.85).aspx)    | Compares two **CHStrings**.<br/>                                                                            |
| [**operator &lt;= (CHString, LPCWSTR)**](https://msdn.microsoft.com/en-us/library/Aa385683(v=VS.85).aspx)      | Compares a **CHString** with a **LPCWSTR**.<br/>                                                            |
| [**operator =**](chstring--operator-equal.md)                                                      | Assigns a new value to a **CHString** string.<br/>                                                          |
| [**operator == (CHString, CHString)**](https://msdn.microsoft.com/en-us/library/Aa385641(v=VS.85).aspx)          | Compares two **CHStrings** for equality.<br/>                                                               |
| [**operator == (CHString, LPCWSTR)**](https://msdn.microsoft.com/en-us/library/Aa385645(v=VS.85).aspx)            | Compares a **CHString** with a **LPCWSTR** for equality.<br/>                                               |
| [**operator &gt; (CHString, CHString)**](https://msdn.microsoft.com/en-us/library/Aa385665(v=VS.85).aspx)       | Compares two **CHStrings**.<br/>                                                                            |
| [**operator &gt; (CHString, LPCWSTR)**](https://msdn.microsoft.com/en-us/library/Aa385672(v=VS.85).aspx)         | Compares a **CHString** with a **LPCWSTR**.<br/>                                                            |
| [**operator &gt;= (CHString, CHString)**](https://msdn.microsoft.com/en-us/library/Aa385652(v=VS.85).aspx) | Compares two **CHStrings**.<br/>                                                                            |
| [**operator &gt;= (CHString, LPCWSTR)**](https://msdn.microsoft.com/en-us/library/Aa385661(v=VS.85).aspx)   | Compares a **CHString** with a **LPCWSTR**.<br/>                                                            |
| [**operator LPCWSTR**](/windows/desktop/api/ChString/nf-chstring-chstring-operator lpcwstr)                                               | Directly accesses characters stored in a **CHString** string as a C-style string.<br/>                      |



 

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



 

 




