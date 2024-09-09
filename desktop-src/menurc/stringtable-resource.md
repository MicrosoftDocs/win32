---
title: STRINGTABLE resource
description: Defines one or more string resources for an application. String resources are simply null-terminated Unicode or ASCII strings that can be loaded when needed from the executable file, using the LoadString function.
ms.assetid: 5868245d-3445-4792-86f5-253945310d36
keywords:
- STRINGTABLE resource Menus and Other Resources
topic_type:
- apiref
api_name:
- STRINGTABLE
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# STRINGTABLE resource

Defines one or more string resources for an application. String resources are simply null-terminated Unicode or ASCII strings that can be loaded when needed from the executable file, using the [**LoadString**](/windows/win32/api/winuser/nf-winuser-loadstringa) function.

There are two ways to format a **STRINGTABLE** statement:

``` syntax
STRINGTABLE  [optional-statements] {stringID string  ...}
```

\- or -

``` syntax
STRINGTABLE
  [optional-statements]
BEGIN
stringID string
. . .
END
```

## Parameters

<dl> <dt>

<span id="optional-statements"></span><span id="OPTIONAL-STATEMENTS"></span>*optional-statements*
</dt> <dd>

This parameter can be zero or more of the following statements.



| Statement                                                        | Description                                                                                                                                                                             |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CHARACTERISTICS**](characteristics-statement.md) *dword*     | User-defined information about a resource that can be used by tools that read and write resource files. For more information, see [**CHARACTERISTICS**](characteristics-statement.md). |
| [**LANGUAGE**](language-statement.md) *language*, *sublanguage* | Specifies the language for the resource. For more information, see [**LANGUAGE**](language-statement.md).                                                                              |
| [**VERSION**](version-statement.md) *dword*                     | User-defined version number for the resource that can be used by tools that read and write resource files. For more information, see [**VERSION**](version-statement.md).              |



 

</dd> <dt>

<span id="stringID"></span><span id="stringid"></span><span id="STRINGID"></span>*stringID*
</dt> <dd>

Unsigned 16-bit integer that identifies the resource.

</dd> <dt>

<span id="string"></span><span id="STRING"></span>*string*
</dt> <dd>

One or more strings, enclosed in quotation marks. The string must be no longer than 4097 characters and must occupy a single line in the source file (unless a '\\' is used as a line continuation). To add a carriage return to the string, use this character sequence: \\012. For example, "Line one\\012Line two" defines a string that is displayed as follows:

``` syntax
Line one
Line two
```

To embed quotes in the string, use the following sequence: "". For example, """Line three""" defines a string that is displayed as follows:

``` syntax
"Line three"
```

To encode Unicode characters, use an "L" followed by the Unicode characters enclosed by quotes. See the Examples section for an example.

The resource compiler also supports line continuations in *string*. See the Examples section for an example.

</dd> </dl>

Certain attributes are also supported for backward compatibility. For more information, see [Common Resource Attributes](common-resource-attributes.md).

## Remarks

RC allocates 16 strings per section and uses the identifier value to determine which section is to contain the string. Strings whose identifiers differ only in the bottom 4 bits are placed in the same section.

## Examples

The following example demonstrates the use of the **STRINGTABLE** statement to display ASCII strings:

``` syntax
#define IDS_HELLO    1
#define IDS_GOODBYE  2

STRINGTABLE
{
    IDS_HELLO,   "Hello"
    IDS_GOODBYE, "Goodbye"
} 
```

The following example shows how to encode Unicode characters:

``` syntax
STRINGTABLE
BEGIN
IDS_CHINESESTRING L"\x5e2e\x52a9"
IDS_RUSSIANSTRING L"\x0421\x043f\x0440\x0430\x0432\x043a\x0430"
IDS_ARABICSTRING L"\x062a\x0639\x0644\x064a\x0645\x0627\x062a"
END
```

The following example shows strings with both ASCII and Unicode. Note that strings without the initial "L" use the 2-digit escape format:

``` syntax
STRINGTABLE
BEGIN
IDS_1 L"5\x00BC-Inch Floppy Disk"
IDS_1a "5\xBC-Inch Floppy Disk"
IDS_2 L"Don't confuse \x2229 (intersection) with \x222A (union)"
IDS_3 "Copyright \xA92001"
IDS_3a L"Copyright \x00a92001"
END
```

The following example shows how line continuations can be used:

``` syntax
STRINGTABLE
BEGIN
IDS_VERYLONGSTRING "blah blah blah blah blah blah \
blah blah blah blah blah blah \
blah blah blah blah blah blah \
blah blah blah blah blah blah"
END
```

## See also

<dl> <dt>

[**LoadString**](/windows/win32/api/winuser/nf-winuser-loadstringa)
</dt> <dt>

[**ACCELERATORS**](accelerators-resource.md)
</dt> <dt>

[**CHARACTERISTICS**](characteristics-statement.md)
</dt> <dt>

[**LANGUAGE**](language-statement.md)
</dt> <dt>

[**MENU**](menu-resource.md)
</dt> <dt>

[**RCDATA**](rcdata-resource.md)
</dt> <dt>

[**VERSION**](version-statement.md)
</dt> </dl>

 

 
