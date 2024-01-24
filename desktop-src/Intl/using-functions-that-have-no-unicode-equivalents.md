---
description: Functions that have not been implemented with a Unicode version have typically been replaced by more powerful or extended functions that do support Unicode.
ms.assetid: 9e02c8fe-4fed-4b77-9b09-35850350859a
title: Using Functions That Have No Unicode Equivalents
ms.topic: article
ms.date: 05/31/2018
---

# Using Functions That Have No Unicode Equivalents

Functions that have not been implemented with a [Unicode](unicode.md) version have typically been replaced by more powerful or extended functions that do support Unicode. For example, if you are porting code that calls the [**OpenFile**](/windows/win32/api/winbase/nf-winbase-openfile) function, your application can support Unicode by using the [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) function instead.

If a function has no Unicode equivalent, the application can map characters to and from 8-bit character sets before and after the function call. For example, the number-formatting functions **atoi** and **itoa** use only the digits 0 through 9. Normally, mapping Unicode to 8-bit characters causes loss of data, but this can be avoided by making the code type-independent and making the expressions conditional. The statements in the following example, written for 8-bit characters, are type-dependent and should be changed to support Unicode.


```C++
char str[4] = "137";

int num = atoi(str);
```



These statements can be rewritten as follows to make them type-independent.


```C++
TCHAR tstr[4] = TEXT("137");

#ifdef UNICODE
size_t cCharsConverted;
CHAR strTmp[SIZE]; // SIZE equals (2*(sizeof(tstr)+1)). This ensures enough
                   // room for the multibyte characters if they are two 
                   // bytes long and a terminating null character. See Security 
                   // Alert below. 

wcstombs_s(&cCharsConverted, strTmp, sizeof(strTmp), (const wchar_t *)tstr, sizeof(strTmp));
num = atoi(strTmp);

#else

int num = atoi(tstr);

#endif 
```



In this example, the standard C library function **wcstombs** translates Unicode to ASCII. The example relies on the fact that the digits 0 through 9 can always be translated from Unicode to ASCII, even if some of the surrounding text cannot. The **atoi** function stops at any character that is not a digit.

Your application can use the National Language Support (NLS) [**LCMapString**](/windows/desktop/api/Winnls/nf-winnls-lcmapstringa) function to process text that includes the [native digits](digit-shapes.md) provided for some of the scripts in Unicode.

> [!Caution]  
> Using the **wcstombs** function incorrectly can compromise the security of your application. Make sure that the application buffer for the string of 8-bit characters is at least of size 2\*(*char\_length* +1), where *char\_length* represents the length of the Unicode string. This restriction is made because, with [double-byte character sets](double-byte-character-sets.md) (DBCSs), each Unicode character can be mapped to two consecutive 8-bit characters. If the buffer does not hold the entire string, the result string is not null-terminated, posing a security risk. For more information about application security, see [Security Considerations: International Features](security-considerations--international-features.md).

 

## Related topics

<dl> <dt>

[Using Unicode and Character Sets](using-unicode-and-character-sets.md)
</dt> </dl>

 

 
