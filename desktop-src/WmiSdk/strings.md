---
title: MOF strings
description: A string is a data type that contains a string of characters usually intended as human-readable text.
ms.assetid: 08a07184-6d23-4988-a3de-e5bfc3e177f8
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# MOF strings

A string is a data type that contains a string of characters usually intended as human-readable text. MOF describes two types of strings, which use to hold single or multiple characters. MOF also has a series of rules describing the use of quotes within a string.

The following table lists the string data types for MOF.



| Data type  | Automation type | Description                                                                            |
|------------|-----------------|----------------------------------------------------------------------------------------|
| **char16** | **VT\_I2**      | Single 16-bit Unicode character in Universal Character Set 2 (UCS-2) format<br/> |
| **string** | **VT\_BSTR**    | Unicode character string<br/>                                                    |



 

Use the following guidelines when writing strings for MOF:

-   Surround single-character constants with single quotes.

    If you do not use single quotes with single character constants, you must use the integer representation of the Unicode character value. Optionally, you could specify the character literally with the \\x escape sequence from the American National Standards Institute (ANSI) C standard, as shown:

    ``` syntax
    char16  TestChar1 = '\x4133';
    char16  Testchar2 = 'A';
    ```

    Because MOF is based on Unicode, you can also specify 16-bit values.

    Be aware that single-character constants in ANSI C format are surrounded by double quotes.

-   Surround character strings with double quotes.

    ``` syntax
    DTime    = "19940107140332.000000-300";
    ```

-   Concatenate successive quote strings with one or more white spaces.

    ``` syntax
    DString = "This" "becomes a long string";
    ```

-   Use an escape sequence beginning with a backslash to embed quotes into a string.

    ``` syntax
    DMyString = "This is an \"embedded quote\" example."
    ```

The following example describes how to initialize string properties and a string parameter:

``` syntax
class  StringDataClass
{
    [key]  String    Dstring;
    DateTime         DTime;
    char16           CharVal1;
    char16           CharVal2;
    sint32 DiskMethod ([in, Id(0)] string Description = "Disk 1");
};

instance of StringDataClass
{
    Dstring = "this can go on for " " some time"
       " before it is complete";
    DTime    = "19940107140332.000000-300";
    CharVal1 = '\x16';
    CharVal2 = '\x32';
};
```

 

 




