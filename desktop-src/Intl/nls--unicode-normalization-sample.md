---
description: The sample application described in this topic demonstrates the representation of strings using Unicode normalization.
ms.assetid: f1f789f9-f12b-465c-8c84-33a8efa6fbc5
title: 'NLS: Unicode Normalization Sample'
ms.topic: article
ms.date: 05/31/2018
---

# NLS: Unicode Normalization Sample

The sample application described in this topic demonstrates the representation of strings using [Unicode normalization](using-unicode-normalization-to-represent-strings.md).

The sample application calls all four Unicode normalization forms with the same input string. A call is then made with invalid Unicode to demonstrate how the index of bad character code works. Finally the application passes a string that expands to be abnormally long, requiring multiple string normalization calls to to get an appropriate buffer size.

This sample demonstrates the following NLS API functions:

-   [**IsNormalizedString**](/windows/desktop/api/Winnls/nf-winnls-isnormalizedstring)
-   [**NormalizeString**](/windows/desktop/api/Winnls/nf-winnls-normalizestring)


```C++
// THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF 
// ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO 
// THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A 
// PARTICULAR PURPOSE. 
// 
// Copyright (c) Microsoft Corporation. All rights reserved. 

// ============ Demonstration of Normalization APIs ============ 

#include "stdafx.h"
#include "windows.h"
#include <stdio.h>
#include <tchar.h>
#include "malloc.h"

// Print out a string using code points for the non-ASCII values 
void DumpString(LPWSTR pInput)
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

// Check if normalized and display normalized output for a particular normalization form 
void TryNormalization(NORM_FORM form, LPWSTR strInput)
{
    // Test if the string is normalized 
    if (IsNormalizedString(form, strInput, -1))
    {
        wprintf(L"Already normalized in this form\n");
    }
    else
    {
        // It was not normalized, so normalize it 
        int    iSizeGuess;
        LPWSTR pBuffer;

        // How big is our buffer (quick guess, usually enough) 
        iSizeGuess = NormalizeString(form, strInput, -1, NULL, 0);

        if (iSizeGuess == 0)
        {
            wprintf(L"Error %d checking for size\n", GetLastError());
        }

        while(iSizeGuess > 0)
        {
            pBuffer = (LPWSTR)malloc(iSizeGuess * sizeof(WCHAR));
            if (pBuffer)
            {
                // Normalize the string 
                int iActualSize = NormalizeString(form, strInput, -1, pBuffer, iSizeGuess);
                iSizeGuess = 0;
                if (iActualSize <= 0 && GetLastError() != ERROR_SUCCESS)
                {
                    // Error during normalization 
                    wprintf(L"Error %d during normalization\n", GetLastError());
                    if (GetLastError() == ERROR_INSUFFICIENT_BUFFER)
                    {
                        // If the buffer is too small, try again with a bigger buffer. 
                        wprintf(L"Insufficient buffer, new suggested buffer size %d\n", -iActualSize);
                        iSizeGuess = -iActualSize;
                    }
                    else if (GetLastError() == ERROR_NO_UNICODE_TRANSLATION)
                    {
                        wprintf(L"Invalid Unicode found at input character index %d\n", -iActualSize);
                    }
                }
                else
                {
                    // Display the normalized string 
                    DumpString(pBuffer);
                }

                // Free the buffer 
                free (pBuffer);
            }
            else
            {
                wprintf(L"Error allocating buffer\n");
                iSizeGuess = 0;
            }
        }
    }
}

int __cdecl wmain(int argc, WCHAR* argv[])
{
     // Tèst string ｔｏ nørmälize 
     LPWSTR strInput = L"T\u00e8st string \uFF54\uFF4F n\u00f8rm\u00e4lize";

    wprintf(L"Comparison of Normalization Forms, input string::\n");
    DumpString(strInput);

    // Try it in the 4 forms 
    wprintf(L"\n");
    wprintf(L"String in Form C:\n  ");
    TryNormalization(NormalizationC, strInput);

    wprintf(L"\n");
    wprintf(L"String in Form KC:\n  ");
    TryNormalization(NormalizationKC, strInput);

    wprintf(L"\n");
    wprintf(L"String in Form D:\n  ");
    TryNormalization(NormalizationD, strInput);

    wprintf(L"\n");
    wprintf(L"String in Form KD:\n  ");
    TryNormalization(NormalizationKD, strInput);

    // Note that invalid Unicode would show an error (illegal lone surrogate in this case) 
    wprintf(L"\n");
    wprintf(L"Attempt to normalize illegal lone surrogate:\n");
    TryNormalization(NormalizationC, L"Bad surrogate is here: '\xd800'");

    // Contrived strings can cause the initial size guess to be low 
    wprintf(L"\n");
    wprintf(L"Attempt to normalize a string that expands beyond the initial guess\n");
    TryNormalization(NormalizationC,
        // These all expand to 2 characters 
        L"\u0958\u0958\u0958\u0958\u0958\u0958\u0958\u0958\u0958\u0958\u0958\u0958"
        L"\u0958\u0958\u0958\u0958\u0958\u0958\u0958\u0958\u0958\u0958\u0958\u0958"
        L"\u0958\u0958\u0958\u0958\u0958\u0958\u0958\u0958\u0958\u0958\u0958\u0958"
        L"\u0958\u0958\u0958\u0958\u0958\u0958\u0958\u0958\u0958\u0958\u0958\u0958"
        // These all expand to 3 characters 
        L"\ufb2c\ufb2c\ufb2c\ufb2c\ufb2c\ufb2c\ufb2c\ufb2c\ufb2c\ufb2c\ufb2c\ufb2c"
        L"\ufb2c\ufb2c\ufb2c\ufb2c\ufb2c\ufb2c\ufb2c\ufb2c\ufb2c\ufb2c\ufb2c\ufb2c");
}

```



 

 



