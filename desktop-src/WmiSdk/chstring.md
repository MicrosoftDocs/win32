---
Description: 'The following table lists the CHString methods.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'e2e4378f-d842-4bca-bffc-a60e718caed3'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: CHString class
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
| [**CHString**](chstring-chstring.md) | Constructs **CHString** strings in various ways.<br/> |



 

### Methods

The **CHString** class has these methods.



| Method                                                    | Description                                                                                                    |
|:----------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|
| [**AllocSysString**](chstring-allocsysstring.md)         | Allocates a BSTR from **CHString** data.<br/>                                                            |
| [**Collate**](chstring-collate.md)                       | Compares two strings (case sensitive; uses locale-specific information).<br/>                            |
| [**Compare**](chstring-compare.md)                       | Compares two strings (case sensitive).<br/>                                                              |
| [**CompareNoCase**](chstring-comparenocase.md)           | Compares two strings (case insensitive).<br/>                                                            |
| [**Empty**](chstring-empty.md)                           | Forces a string to have 0 (zero) length.<br/>                                                            |
| [**Find**](chstring-find.md)                             | Overloaded. Finds a character or substring inside a larger string.<br/>                                  |
| [**FindOneOf**](chstring-findoneof.md)                   | Finds the first matching character from a set.<br/>                                                      |
| [**Format**](chstring-format.md)                         | Overloaded. Formats the string as **sprintf** does.<br/>                                                 |
| [**FormatMessageW**](chstring-formatmessagew.md)         | Overloaded. Formats a message string.<br/>                                                               |
| [**FormatV**](chstring-formatv.md)                       | Formats the string as **vsprintf** does.<br/>                                                            |
| [**FreeExtra**](chstring-freeextra.md)                   | Removes any overhead of this string by freeing any extra memory previously allocated to the string.<br/> |
| [**GetAllocLength**](chstring-getalloclength.md)         | Returns the size of the string buffer.<br/>                                                              |
| [**GetAt**](chstring-getat.md)                           | Overloaded. Returns the character at a given position.<br/>                                              |
| [**GetBuffer**](chstring-getbuffer.md)                   | Returns a pointer to the characters in the **CHString** string.<br/>                                     |
| [**GetBufferSetLength**](chstring-getbuffersetlength.md) | Returns a pointer to the characters in the **CHString** string, truncating to the specified length.<br/> |
| [**GetData**](chstring-getdata.md)                       | Returns a pointer to the data in the **CHString** string.<br/>                                           |
| [**GetLength**](chstring-getlength.md)                   | Returns the number of Unicode characters in a **CHString** string.<br/>                                  |
| [**IsEmpty**](chstring-isempty.md)                       | Tests whether a **CHString** string contains no characters.<br/>                                         |
| [**Left**](chstring-left.md)                             | Extracts the left part of a string (like the Basic **LEFT$** function).<br/>                             |
| [**LoadStringW**](chstring-loadstringw.md)               | Loads an existing **CHString** string from a resource file.<br/>                                         |
| [**LockBuffer**](chstring-lockbuffer.md)                 | Disables reference counting and protects the string in the buffer.<br/>                                  |
| [**MakeLower**](chstring-makelower.md)                   | Converts all of the characters in this string to lowercase characters.<br/>                              |
| [**MakeReverse**](chstring-makereverse.md)               | Reverses the characters in this string.<br/>                                                             |
| [**MakeUpper**](chstring-makeupper.md)                   | Converts all of the characters in this string to uppercase characters.<br/>                              |
| [**Mid**](chstring-mid.md)                               | Overloaded. Extracts the middle part of a string (like the Basic **MID$** function).<br/>                |
| [**ReleaseBuffer**](chstring-releasebuffer.md)           | Releases control of the buffer returned by [**GetBuffer**](chstring-getbuffer.md).<br/>                 |
| [**ReverseFind**](chstring-reversefind.md)               | Finds a character inside a larger string; starts from the end.<br/>                                      |
| [**Right**](chstring-right.md)                           | Extracts the right part of a string (like the Basic **RIGHT$** function).<br/>                           |
| [**SetAt**](chstring-setat.md)                           | Sets a character at a given position.<br/>                                                               |
| [**SpanExcluding**](chstring-spanexcluding.md)           | Extracts a substring that contains only the characters that are not in the set.<br/>                     |
| [**SpanIncluding**](chstring-spanincluding.md)           | Extracts a substring that contains only the characters in a set.<br/>                                    |
| [**TrimLeft**](chstring-trimleft.md)                     | Trims leading whitespace characters from the string.<br/>                                                |
| [**TrimRight**](chstring-trimright.md)                   | Trims trailing whitespace characters from the string.<br/>                                               |
| [**UnlockBuffer**](chstring-unlockbuffer.md)             | Enables reference counting and releases the string in the buffer.<br/>                                   |



 

### Operators

The **CHString** class has these operators.



| Operator                                                                                            | Description                                                                                                       |
|:----------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------|
| [**operator != (CHString, CHString)**](chstring-operator-notequal-chstring-chstring.md)            | Compares two **CHStrings** for inequality.<br/>                                                             |
| [**operator != (CHString, LPCWSTR)**](chstring-operator-notequal-chstring-lpcwstr.md)              | Compares a **CHString** with a **LPCWSTR** for inequality.<br/>                                             |
| [**operator \[\]**](chstring--operator-brackets.md)                                                | Returns the character at a given position — operator substitution for [**GetAt**](chstring-getat.md).<br/> |
| [**operator +**](chstring--operator-plus.md)                                                       | Concatenates two strings and returns a new string.<br/>                                                     |
| [**operator +=**](chstring--operator-plus-equal.md)                                                | Concatenates a new string to the end of an existing string.<br/>                                            |
| [**operator &lt; (CHString, LPCWSTR)**](chstring-operator-lessthan-chstring-lpcwstr.md)            | Compares a **CHString** with a **LPCWSTR**.<br/>                                                            |
| [**operator &lt; (CHString, CHString)**](chstring-operator-lessthan-chstring-chstring.md)          | Compares two **CHStrings**.<br/>                                                                            |
| [**operator &lt;= (CHString, CHString)**](chstring-operator-lessthanequal-chstring-chstring.md)    | Compares two **CHStrings**.<br/>                                                                            |
| [**operator &lt;= (CHString, LPCWSTR)**](chstring-operator-lessthanequal-chstring-lpcwstr.md)      | Compares a **CHString** with a **LPCWSTR**.<br/>                                                            |
| [**operator =**](chstring--operator-equal.md)                                                      | Assigns a new value to a **CHString** string.<br/>                                                          |
| [**operator == (CHString, CHString)**](chstring-operator-equalequal-chstring-chstring.md)          | Compares two **CHStrings** for equality.<br/>                                                               |
| [**operator == (CHString, LPCWSTR)**](chstring-operator-equalequal-chstring-lpcwstr.md)            | Compares a **CHString** with a **LPCWSTR** for equality.<br/>                                               |
| [**operator &gt; (CHString, CHString)**](chstring-operator-greaterthan-chstring-chstring.md)       | Compares two **CHStrings**.<br/>                                                                            |
| [**operator &gt; (CHString, LPCWSTR)**](chstring-operator-greaterthan-chstring-lpcwstr.md)         | Compares a **CHString** with a **LPCWSTR**.<br/>                                                            |
| [**operator &gt;= (CHString, CHString)**](chstring-operator-greaterthanequal-chstring-chstring.md) | Compares two **CHStrings**.<br/>                                                                            |
| [**operator &gt;= (CHString, LPCWSTR)**](chstring-operator-greaterthanequal-chstring-lpcwstr.md)   | Compares a **CHString** with a **LPCWSTR**.<br/>                                                            |
| [**operator LPCWSTR**](chstring-operator-lpcwstr.md)                                               | Directly accesses characters stored in a **CHString** string as a C-style string.<br/>                      |



 

## Remarks

The destructor for the class is **CHString::~CHString**.

## Requirements



|                                     |                                                                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                                                                |
| Header<br/>                   | <dl> <dt>ChString.h (include FwCommon.h)</dt> </dl>                                                    |
| Library<br/>                  | <dl> <dt>FrameDyn.lib</dt> </dl>                                                                       |
| DLL<br/>                      | <dl> <dt>FrameDynOS.dll; </dt> <dt>FrameDyn.dll</dt> </dl> |



 

 




