---
description: The sample application described in this topic demonstrates how certain NLS functions can be used to convert internationalized domain names (IDNs).
ms.assetid: 9739efa5-8b88-4f9c-983d-806968caf9d5
title: 'NLS: Internationalized Domain Name Conversion Sample'
ms.topic: article
ms.date: 05/31/2018
---

# NLS: Internationalized Domain Name Conversion Sample

The sample application described in this topic demonstrates how certain NLS functions can be used to convert [internationalized domain names (IDNs)](handling-internationalized-domain-names--idns.md). This application demonstrates the following NLS API functions:

-   [**IdnToAscii**](/windows/desktop/api/Winnls/nf-winnls-idntoascii)
-   [**IdnToNameprepUnicode**](/windows/desktop/api/Winnls/nf-winnls-idntonameprepunicode)
-   [**IdnToUnicode**](/windows/desktop/api/Winnls/nf-winnls-idntounicode)

In the sample output, note that, "ExAmPlE.cOm" is converted to "русский.example.com" for the Cyrillic example.


```C++

// THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF 
// ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO 
// THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A 
// PARTICULAR PURPOSE. 
// 
// Copyright (c) Microsoft Corporation. All rights reserved. 
// 
// IdnConversion.cpp 

#include "stdafx.h"
#include "windows.h"
#include <stdio.h>
#include <tchar.h>

#define IDN_MAX_LENGTH 255

// Print out a string using code points for the non-ASCII values 
void DumpString(LPCWSTR pInput)
{
    while (*pInput != 0)
    {
        if (*pInput < 0x80)
            wprintf(L"%c", *pInput);
        else
            wprintf(L"\\x%4.4x", *pInput);
        pInput++;
    }
    wprintf(L"\n");
}

// Convert some IDN strings 
void IdnConvert(LPCWSTR strInput)
{
    // Show string we're converting 
    wprintf(L"Converting string: ");
    DumpString(strInput);

    // Convert it to IDN "Punycode" form.  Note that IDN names have a maximum length, 
    // so we'll just use a hard coded buffer size.  
    WCHAR pPunycode[IDN_MAX_LENGTH];
    if (IdnToAscii(0, strInput, -1, pPunycode, IDN_MAX_LENGTH) == 0)
    {
        wprintf(L"ERROR %d converting to Punycode\n", GetLastError());
    }
    else
    {
        // Output it, safe to just wprintf to console because it has to be ASCII 
        wprintf(L"   Punycode value: %s\n", pPunycode);

        // Convert it to IDN normalized Unicode 
        WCHAR pUnicode[IDN_MAX_LENGTH];
        if (IdnToNameprepUnicode(0, strInput, -1, pUnicode, IDN_MAX_LENGTH) == 0)
        {
            wprintf(L"ERROR %d converting to nameprep Unicode\n", GetLastError());
        }
        else
        {
            wprintf(L"   Nameprep value: ");
            DumpString(pUnicode);
        }

        // Convert the punycode string back to Unicode 
        if (IdnToUnicode(0, pPunycode, -1, pUnicode, IDN_MAX_LENGTH) == 0)
        {
            wprintf(L"ERROR %d converting back to Unicode\n", GetLastError());
        }
        else
        {
            // Note that this round-trip value should be the same as the nameprep value above 
            wprintf(L"    Unicode value: ");
            DumpString(pUnicode);
        }
    }

    wprintf(L"\n");
}

int __cdecl wmain(int argc, WCHAR* argv[])
{
    // Non-IDN names do not change 
    IdnConvert(L"ExAmPlE.cOm");
    
    // Show some idn conversions.  Note that some characters change 
    IdnConvert(L"&#1088;&#1091;&#1089;&#1089;&#1082;&#1080;&#1081;.ExAmPlE.cOm");
    IdnConvert(L"&#26085;&#26412;&#35486;.example.com");
    IdnConvert(L"&#65318;&#65365;&#65356;&#65356;&#65367;&#65353;&#65348;&#65364;&#65352;&#12290;example&#12290;com&#12290;");

    // Some characters are illegal in IDN names 
    IdnConvert(L"\x9fa5\x9fff\x00\x7f");
}

/* This code example produces the following output:

Converting string: ExAmPlE.cOm
   Punycode value: ExAmPlE.cOm
   Nameprep value: ExAmPlE.cOm
    Unicode value: ExAmPlE.cOm

Converting string: \x0440\x0443\x0441\x0441\x043a\x0438\x0439.ExAmPlE.cOm
   Punycode value: xn--h1acbxfam.example.com
   Nameprep value: \x0440\x0443\x0441\x0441\x043a\x0438\x0439.example.com
    Unicode value: \x0440\x0443\x0441\x0441\x043a\x0438\x0439.example.com

Converting string: \x65e5\x672c\x8a9e.example.com
   Punycode value: xn--wgv71a119e.example.com
   Nameprep value: \x65e5\x672c\x8a9e.example.com
    Unicode value: \x65e5\x672c\x8a9e.example.com

Converting string: \xff26\xff55\xff4c\xff4c\xff57\xff49\xff44\xff54\xff48\x3002example\x3002com\x3002
   Punycode value: fullwidth.example.com.
   Nameprep value: fullwidth.example.com.
    Unicode value: fullwidth.example.com.

Converting string: \x9fa5\x9fff
ERROR 123 converting to Punycode

*/
```



 

 



