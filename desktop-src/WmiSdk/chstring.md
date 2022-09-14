---
description: The following table lists the CHString methods.
ms.assetid: e2e4378f-d842-4bca-bffc-a60e718caed3
ms.tgt_platform: multiple
title: CHString class (ChString.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CHString
- ??1CHString@@QAE@XZ
- ??1CHString@@QEAA@XZ
api_type: 
- COM
api_location: 
- FrameDynOS.dll
- FrameDyn.dll
---

# CHString class

\[The **CHString** class is part of the WMI Provider Framework which is now considered in final state, and no further development, enhancements, or updates will be available for non-security related issues affecting these libraries. The [MI APIs](/previous-versions/windows/desktop/wmi_v2/windows-management-infrastructure) should be used for all new development.\]

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
| [**CHString**](/windows/desktop/api/ChString/nf-chstring-chstring-chstring(constchstring_)) | Constructs **CHString** strings in various ways.<br/> |



 

### Methods

The **CHString** class has these methods.



| Method                                                    | Description                                                                                                    |
|:----------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|
| [**AllocSysString**](/windows/desktop/api/ChString/nf-chstring-chstring-allocsysstring)         | Allocates a BSTR from **CHString** data.<br/>                                                            |
| [**Collate**](/windows/desktop/api/ChString/nf-chstring-chstring-collate)                       | Compares two strings (case sensitive; uses locale-specific information).<br/>                            |
| [**Compare**](/windows/desktop/api/ChString/nf-chstring-chstring-compare)                       | Compares two strings (case sensitive).<br/>                                                              |
| [**CompareNoCase**](/windows/desktop/api/ChString/nf-chstring-chstring-comparenocase)           | Compares two strings (case insensitive).<br/>                                                            |
| [**Empty**](/windows/desktop/api/ChString/nf-chstring-chstring-empty)                           | Forces a string to have 0 (zero) length.<br/>                                                            |
| [**Find**](/windows/win32/api/chstring/nf-chstring-chstring-find(wchar))                        | Overloaded. Finds a character or substring inside a larger string.<br/>                                  |
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
| [**Mid**](/windows/win32/api/chstring/nf-chstring-chstring-mid(int))                               | Overloaded. Extracts the middle part of a string (like the Basic **MID$** function).<br/>                |
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
`
The **CHString** class has these operators.`



| Operator                                                                                            | Description                                                                                                       |
|:----------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------|
| [**operator != (CHString, CHString)**](/previous-versions/windows/desktop/legacy/aa385704(v=vs.85))            | Compares two **CHStrings** for inequality.<br/>                                                             |
| [**operator != (CHString, LPCWSTR)**](/previous-versions/windows/desktop/legacy/aa385763(v=vs.85))              | Compares a **CHString** with a **LPCWSTR** for inequality.<br/>                                             |
| [**operator \[\]**](/previous-versions/windows/desktop/legacy/aa386162(v=vs.85))                                                | Returns the character at a given position   operator substitution for [**GetAt**](/windows/desktop/api/ChString/nf-chstring-chstring-getat(int)).<br/> |
| [**operator +**](chstring--operator-plus.md)                                                       | Concatenates two strings and returns a new string.<br/>                                                     |
| [**operator +=**](chstring--operator-plus-equal.md)                                                | Concatenates a new string to the end of an existing string.<br/>                                            |
| [**operator < (CHString, LPCWSTR)**](/previous-versions/windows/desktop/legacy/aa385695(v=vs.85))            | Compares a **CHString** with a **LPCWSTR**.<br/>                                                            |
| [**operator < (CHString, CHString)**](/previous-versions/windows/desktop/legacy/aa385689(v=vs.85))          | Compares two **CHStrings**.<br/>                                                                            |
| [**operator <= (CHString, CHString)**](/previous-versions/windows/desktop/legacy/aa385676(v=vs.85))    | Compares two **CHStrings**.<br/>                                                                            |
| [**operator <= (CHString, LPCWSTR)**](/previous-versions/windows/desktop/legacy/aa385683(v=vs.85))      | Compares a **CHString** with a **LPCWSTR**.<br/>                                                            |
| [**operator =**](chstring--operator-equal.md)                                                      | Assigns a new value to a **CHString** string.<br/>                                                          |
| [**operator == (CHString, CHString)**](/previous-versions/windows/desktop/legacy/aa385641(v=vs.85))          | Compares two **CHStrings** for equality.<br/>                                                               |
| [**operator == (CHString, LPCWSTR)**](/previous-versions/windows/desktop/legacy/aa385645(v=vs.85))            | Compares a **CHString** with a **LPCWSTR** for equality.<br/>                                               |
| [**operator > (CHString, CHString)**](/previous-versions/windows/desktop/legacy/aa385665(v=vs.85))       | Compares two **CHStrings**.<br/>                                                                            |
| [**operator > (CHString, LPCWSTR)**](/previous-versions/windows/desktop/legacy/aa385672(v=vs.85))         | Compares a **CHString** with a **LPCWSTR**.<br/>                                                            |
| [**operator >= (CHString, CHString)**](/previous-versions/windows/desktop/legacy/aa385652(v=vs.85)) | Compares two **CHStrings**.<br/>                                                                            |
| [**operator >= (CHString, LPCWSTR)**](/previous-versions/windows/desktop/legacy/aa385661(v=vs.85))   | Compares a **CHString** with a **LPCWSTR**.<br/>                                                            |
| [**operator LPCWSTR**](/windows/desktop/api/ChString/nf-chstring-chstring-operatorlpcwstr)                                               | Directly accesses characters stored in a **CHString** string as a C-style string.<br/>                      |



 

## Remarks

The destructor for the class is **CHString::~CHString**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                                                                |
| Header<br/>                   | <dl> <dt>ChString.h (include FwCommon.h)</dt> </dl>                                                    |
| Library<br/>                  | <dl> <dt>FrameDyn.lib</dt> </dl>                                                                       |
| DLL<br/>                      | <dl> <dt>FrameDynOS.dll; </dt> <dt>FrameDyn.dll</dt> </dl> |



