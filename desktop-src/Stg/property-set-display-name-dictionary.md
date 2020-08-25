---
title: Property Set Display Name Dictionary
description: A dictionary of property display names enables property set users to attach meaning to properties - beyond those provided by the type indicator.
ms.assetid: b6813a86-39d3-4754-86e4-51035a7c91d9
ms.topic: article
ms.date: 05/31/2018
---

# Property Set Display Name Dictionary

A dictionary of property display names enables property set users to attach meaning to properties - beyond those provided by the type indicator.

## Dictionary Structure

The dictionary contains a count of entries in the list, followed by a list of dictionary entries.

``` syntax
typedef struct tagDICTIONARY 
{ 
    DWORD  cEntries ;               // Count of entries in the list 
    ENTRY  rgEntry[ cEntries ] ;    // Property ID/String pair 
} DICTIONARY ;
```

## Dictionary Entry Structure

Each dictionary entry in the list is a Property Identifier/String pair. The following is a pseudo-structure definition for a dictionary entry. It's a pseudo-structure because the sz\[\] member is variable in size.

``` syntax
typedef struct tagENTRY 
{ 
    DWORD  propid ;    // Property ID 
    DWORD  cch ;       // Count of characters in the string 
    char  sz[cch];     // Zero-terminated string 
} ENTRY ;
```

## Sample Dictionary

The following stock market data transfer example might include a displayable name "Stock Quote" for the entire set, and "Ticker Symbol" for PID\_SYMBOL. If a property set contained just a symbol and the dictionary, the property set section would have a byte stream that looked like the following.

``` syntax
Offset     Bytes 
; Start of section 
0000    5C 01 00 00    ; DWORD size of section 
0004    04 00 00 00    ; DWORD number of properties in section 
 
; Start of PropID/Offset pairs 
0008    01 00 00 00    ; DWORD Property ID (1 == code page) 
000C    28 00 00 00    ; DWORD offset to property ID 
0010    00 00 00 80    ; DWORD Property ID (0x80000000 == locale
                                                 ID) 
0014    30 00 00 00    ; DWORD offset to property ID 
0018    00 00 00 00    ; DWORD Property ID (0 == dictionary) 
001C    38 00 00 00    ; DWORD offset to property ID 
0020    07 00 00 00    ; DWORD Property ID (7 == PID_SYMBOL)
0024    5C 01 00 00    ; DWORD offset to property ID
 
; Start of Property 1 (code page)
0028    01 00 00 00    ; DWORD type indicator (VT_12)
002C    B0 04          ; USHORT codepage (0x04b0 == 1200 ==
                                                 unicode)
002E    00 00          ; Pad to 32-bit boundary
 
; Start of Property 0x80000000 (Local ID)
0030    13 00 00 00    ; DWORD type indicator (VT_U14)
0034    09 04 00 00    ; ULONG locale ID (0x0409 == American 
                                                 English)
 
; Start of Property 0 (the dictionary)
0038    08 00 00 00    ; DWORD number of entries in dictionary
                             (Note:  No type indicator)
003C    00 00 00 00    ; DWORD propid == 0 (the dictionary)
0040    0C 00 00 00    ; DWORD cch == wcslen(L"Stock Quote") +
                                                 sizeof(L'\0') == 12
0044    L"Stock Quote" ; wchar_t wsz(12)
005C    05 00 00 00    ; DWORD propid == 5 (PID_HIGH)
0060    0B 00 00 00    ; DWORD cch == wcslen(L"High Price") + 
                                                 sizeof(L'\0') == 11
0064    L"High Price\0"; wchar_t wsz(11)
007A    00 00          ; padding for 32-bit alignment (necessary
                             because the codepage is unicode)
007C    07 00 00 00    ; DWORD propid == 7 (PID_SYMBOL)
0080    0E 00 00 00    ; DWORD cch - wcslen(L"Ticker Symbol\0") 
                             == 14
0084    L"Ticker Symbol\0" ; wchar_t wsz(14)
 
    // The dictionary would continue, but may not contain entries 
    // for every possible property, and may contain entries for 
    // properties that are not present. Entries are not required  
    // to be in order.
```

Be aware of the following issues regarding property set dictionaries:

-   Property ID 0 does not have a type indicator. The **DWORD** data type that indicates the count of entries sits in the type-indicator position.
-   The count of characters in the *cch* string includes the zero character that terminates the string. When the codepage of the property set is not Unicode, this field is actually a **byte** count. For property sets with a format version of 0, this count may not exceed 256. For property sets with a format version of 1, this count may be as large as is allowed by the total property set size.
-   The dictionary is optional. Not all the names of properties in the set are required to appear in the dictionary. Conversely, not all names in the dictionary are required to correspond to properties in the set. The dictionary should omit entries for properties assumed to be universally recognized by applications manipulating the property set. Typically, names for the base property sets for widely-accepted standards are omitted, but special-purpose property sets may include dictionaries for use by browsers.
-   Property names in the dictionary are stored in the code page indicated by [Property ID 1](/windows/desktop/Stg/reserved-property-identifiers). For ANSI code pages, each dictionary entry is byte-aligned. Thus, there is no spacing between property names with Property ID 0. This is the only case where values of **DWORD** data types (the property ID and property name-length **DWORD**s) are not required to be aligned on 32-bit boundaries. For Unicode pages, each dictionary entry is 32-bit aligned.
-   Property names that begin with the binary Unicode characters 0x0001 through 0x001F are reserved for future use.
-   The property name associated with Property ID 0 represents the name of the entire property set.

 

 