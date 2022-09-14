---
description: The sample application described in this topic demonstrates how certain NLS functions can be used to mitigate some of the security issues associated with internationalized domain names (IDNs).
ms.assetid: 73a96129-5234-4c70-b36a-baa5cb4daa0a
title: 'NLS: Internationalized domain name mitigation sample'
ms.topic: article
ms.date: 05/31/2018
---

# NLS: Internationalized domain name mitigation sample

The sample application described in this topic demonstrates how certain NLS functions can be used to mitigate some of the security issues associated with [internationalized domain names (IDNs)](handling-internationalized-domain-names--idns.md). This sample demonstrates the following NLS API functions:

-   [**GetLocaleInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex), with the *LCType* parameter set to [LOCALE\_SSCRIPTS](locale-sscripts.md)
-   [**GetStringScripts**](/windows/desktop/api/Winnls/nf-winnls-getstringscripts)
-   [**VerifyScripts**](/windows/desktop/api/Winnls/nf-winnls-verifyscripts)


```C++
// THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF 
// ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO 
// THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A 
// PARTICULAR PURPOSE. 
// 
// Copyright (c) Microsoft Corporation. All rights reserved. 
// 
// IdnMitigation.cpp 

#include "stdafx.h"
#include "windows.h"
#include <stdio.h>
#include <tchar.h>
#include "malloc.h"

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

// Test a string to see if its expected for a locale 
void TestString(LPCWSTR strTest, LPCWSTR strLocale)
{
    // We could count the strings, but we really don't expect large script combinations 
    WCHAR pLocaleScripts[255];
    WCHAR pStringScripts[255];

    // Show the inputs 
    wprintf(L"Testing string with locale %s:\n", strLocale);
    DumpString(strTest);
    
    // Get the expected scripts 
    if (GetLocaleInfoEx(strLocale, LOCALE_SSCRIPTS, pLocaleScripts, 255) == 0)
    {
        // Unexpected Error 
        wprintf(L"ERROR in GetLocaleInfoEx: %d\n", GetLastError());
        return;
    }
    
    // Get the actual scripts.  We're expecting inherited and common characters (like ,:, etc.) 
    if (GetStringScripts(0, strTest, -1, pStringScripts, 255) == 0 &&
        GetLastError() != ERROR_SUCCESS)
    {
        // Unexpected Error 
        wprintf(L"ERROR in GetStringScripts: %d\n", GetLastError());
        return;
    }

    // Show what we found 
    wprintf(L"Locale Scripts: %s\n", pLocaleScripts);
    wprintf(L"String Scripts: %s\n", pStringScripts);

    // Test the output 
    if (VerifyScripts(NULL, pLocaleScripts, -1, pStringScripts, -1))
    {
        wprintf(L"These script(s) are expected in this locale\n");
    }
    else
    {
        if (VerifyScripts(VS_ALLOW_LATIN, pLocaleScripts, -1, pStringScripts, -1))
        {
            wprintf(L"These script(s) are not expected for this locale, unless Latin is allowed\n");
        }
        else
        {
            wprintf(L"These script(s) are not expected in this locale\n");
        }
    }

    wprintf(L"\n");
}

int __cdecl wmain(int argc, WCHAR* argv[])
{
    LPWSTR strLatin = L"This is an entirely Latn string, even with characters like these: &#192;&#228;&#235;&#234;&#240;&#261;&#272;&#317;&#332;&#326;&#470;&#510;&#509;&#7912;";
    LPWSTR strMixed = L"This string has &#1057;&#1091;&#1075;&#1110;&#1472;&#1472;&#1110;&#1089;, Hebrew, and GR&#917;&#917;&#922; &#21313; Chinese &#24037;&#21475; and PUA &#63705; characters.  Depending on font it may look like Latin";
    LPWSTR strChinese = L"&#39321;&#28207;&#29305;&#21029;&#34892;&#25919;&#21312;";
    LPWSTR strCyrillic = L"&#1088;&#1091;&#1089;&#1089;&#1082;&#1080;&#1081;";
    LPWSTR strCyrlLatn = L"&#1088;&#1091;&#1089;&#1089;&#1082;&#1080;&#1081; (Russian)";

    TestString(strLatin, L"en-US");
    TestString(strMixed, L"en-US");
    TestString(strChinese, L"zh-HK");
    TestString(strCyrillic, L"ru-RU");
    TestString(strCyrlLatn, L"ru-RU");
    TestString(strCyrlLatn, L"en-US");
}

/* This code example produces the following output:

Testing string with locale en-US:
This is an entirely Latn string, even with characters like these: \x00c0\x00e4\x00eb\x00ea\x00f0\x0105\x0110\x013d\x014c\x0146\x01d6\x01fe\x01fd\x1ee8
Locale Scripts: Latn;
String Scripts: Latn;
These script(s) are expected in this locale

Testing string with locale en-US:
This string has \x0421\x0443\x0433\x0456\x05c0\x05c0\x0456\x0441, Hebrew, and GR\x0395\x0395\x039a \x5341 Chinese \x5de5\x53e3 and PUA \xf8d9 characters.  Depending on font it may look like Latin
Locale Scripts: Latn;
String Scripts: Cyrl;Grek;Hani;Hebr;Latn;Zzzz;
These script(s) are not expected in this locale

Testing string with locale zh-HK:
\x9999\x6e2f\x7279\x5225\x884c\x653f\x5340
Locale Scripts: Hani;
String Scripts: Hani;
These script(s) are expected in this locale

Testing string with locale ru-RU:
\x0440\x0443\x0441\x0441\x043a\x0438\x0439
Locale Scripts: Cyrl;
String Scripts: Cyrl;
These script(s) are expected in this locale

Testing string with locale ru-RU:
\x0440\x0443\x0441\x0441\x043a\x0438\x0439 (Russian)
Locale Scripts: Cyrl;
String Scripts: Cyrl;Latn;
These script(s) are not expected for this locale, unless Latin is allowed

Testing string with locale en-US:
\x0440\x0443\x0441\x0441\x043a\x0438\x0439 (Russian)
Locale Scripts: Latn;
String Scripts: Cyrl;Latn;
These script(s) are not expected in this locale
*/

```



 

 



