---
Description: The following example calls ScriptGetProperties to find out if the script of each of several successive items requires glyph shaping.
ms.assetid: 75c5946b-de38-48d9-a5e2-1e0b2dc9f3c7
title: Determining If a Script Requires Glyph Shaping
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Determining If a Script Requires Glyph Shaping

The following example calls [**ScriptGetProperties**](/windows/win32/Usp10/nf-usp10-scriptgetproperties?branch=master) to find out if the script of each of several successive [items](uniscribe-glossary.md) requires glyph shaping.


```C++
const SCRIPT_PROPERTIES **g_ppScriptProperties;
int g_iMaxScript;

WCHAR *pwcInChars = L"Unicode string to itemize";
int cInChars = wcslen(pwcInChars);
const int cMaxItems = 20;
SCRIPT_ITEM si[cMaxItems + 1];
SCRIPT_ITEM *pItems = si;
int cItems;

ScriptGetProperties(&amp;g_ppScriptProperties,
                    &amp;g_iMaxScript);

HRESULT hResult = ScriptItemize(pwcInChars,
                                cInChars,
                                cMaxItems,
                                NULL,
                                NULL,
                                pItems,
                                &amp;cItems);
if (hResult == 0) {
    for (int i=0; i<cItems; i++) {
        if (g_ppScriptProperties[pItems[i].a.eScript]->fComplex) {

            // Item [i] is complex script text
            // requiring glyph shaping.

        } else {

            // The text may be rendered legibly without using Uniscribe. 
            // However, Uniscribe may still be used as a means of accessing 
            // font typographic features. 
        }
    }
} else {
    // Handle the error.
}
```



## Related topics

<dl> <dt>

[Using Uniscribe](using-uniscribe.md)
</dt> </dl>

 

 



