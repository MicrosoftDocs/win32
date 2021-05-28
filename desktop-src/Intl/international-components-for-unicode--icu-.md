---
description: International Components for Unicode (ICU) is a mature, widely used set of open-source globalization APIs.
ms.assetid: 4AEBE391-4121-44B2-B15B-0032645D7053
title: International Components for Unicode (ICU)
ms.topic: article
ms.date: 05/31/2018
---

# International Components for Unicode (ICU)

International Components for Unicode (ICU) is a mature, widely used set of open-source globalization APIs. ICU utilizes Unicode's vast Common Locale Data Repository (CLDR) as its data library, providing globalization support for software applications. ICU is widely portable and gives applications the same results across on all platforms.

## Highlights of the Globalization API services provided by ICU

-   **Code Page Conversion**: Convert text data to or from Unicode and nearly any other character set or encoding. ICU's conversion tables are based on charset data collected by IBM over the course of many decades, and is the most complete available anywhere.
-   **Collation**: Compare strings according to the conventions and standards of a particular language, region or country. ICU's collation is based on the Unicode Collation Algorithm plus locale-specific comparison rules from CLDR.
-   **Formatting**: Format numbers, dates, times and currency amounts according the conventions of a chosen locale. This includes translating month and day names into the selected language, choosing appropriate abbreviations, ordering fields correctly, etc. This data also comes from the Common Locale Data Repository.
-   **Time Calculations**: Multiple types of calendars are provided beyond the traditional Gregorian. A thorough set of time zone calculation APIs are provided.
-   **Unicode Support**: ICU closely tracks the Unicode standard, providing easy access to all of the many Unicode character properties, Unicode Normalization, Case Folding, and other fundamental operations as specified by the [Unicode Standard](https://www.unicode.org/).
-   **Regular Expression**: ICU's regular expressions fully support Unicode while providing very competitive performance.
-   **Bidi**: Support for handling text containing a mixture of left to right (English) and right to left (Arabic or Hebrew) data.

For more information, you can visit the ICU website: <http://site.icu-project.org/>

## Overview

In Windows 10 Creators Update, ICU was integrated into Windows, making the C APIs and data publicly accessible.

> [!IMPORTANT]
> The version of ICU in Windows only exposes the C APIs. It does not expose any of the C++ APIs. Unfortunately, it is impossible to ever expose the C++ APIs due to the lack of a stable ABI in C++.

For documentation on the ICU C APIs, please refer to the official ICU documentation page here: <http://icu-project.org/apiref/icu4c/index.html#Module>

## History of changes to the ICU library in Windows

### Version 1703 (Creators Update)
The ICU library was first added to the Windows 10 OS in this version.
It was added as:
- Two system DLLs:
    -   **icuuc.dll** (this is the ICU "common" library)
    -   **icuin.dll** (this is the ICU "i18n" library)
- Two header files in the Windows 10 SDK:
    -   **icucommon.h**
    -   **icui18n.h**
- Two import libs in the Windows 10 SDK:
    -   **icuuc.lib**
    -   **icuin.lib**

### Version 1709 (Fall Creators Update)
A combined header file, **icu.h**, was added, which contains the contents of both header files above (icucommon.h and icui18n.h), and also changes the type of `UCHAR` to `char16_t`.

### Version 1903 (May 2019 Update)
A new combined DLL, **icu.dll**, was added, which contains both the "common" and "i18n" libraries. Also, a new import library was added to the Windows 10 SDK: **icu.lib**.

Going forward, no new APIs will be added to the old headers (icucommon.h and icui18n.h) or to the old import libs (icuuc.lib and icuin.lib). New APIs will only be added to the combined header (icu.h) and the combined import lib (icu.lib).

## Getting Started

There are three main steps to follow: (Windows 10 Creators Update or higher)

<dl>

1. Your application needs to target Windows 10 Version 1703 (Creators Update) or higher.

2. Add in the headers:

   ``` syntax
   #include <icucommon.h>
   #include <icui18n.h>
   ```

   On Windows 10 Version 1709 and above, you should include the combined header instead:

   ``` syntax
   #include <icu.h>
   ```
  
3. Link to the two libraries:

   -   icuuc.lib
   -   icuin.lib

   On Windows 10 Version 1903 and above, you should use the combined library instead:

   -   icu.lib

</dl>

Then, you can call whatever ICU C API from these libraries you want. (No C++ APIs are exposed.)

> [!IMPORTANT]
> If you are using the legacy import libraries, icuuc.lib and icuin.lib, ensure they're listed before the umbrella libraries, like onecoreuap.lib or WindowsApp.lib, in the Additional Dependencies Linker setting (see the image below). Otherwise, the linker will link to icu.lib, which will result in an attempt to load icu.dll during run time. That DLL is present only starting with version 1903. So, if a user upgrades the Windows 10 SDK on a pre-version 1903 Windows machine, the app will fail to load and run. For a history of the ICU libraries in Windows, see [History of changes to the ICU library in Windows](#history-of-changes-to-the-icu-library-in-windows).

![icu example](images/icu-example.png)

> [!Note]  
>
> - This is the configuration for “All Platforms”.
> - For Win32 apps to use ICU on Windows versions before 1903, they need to call [CoInitializeEx](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex) first.
> - Not all data returned by ICU APIs will align with the Windows OS, as this alignment work is still in progress. 

## ICU Example App

### Example code snippet

The following is an example illustrating the use of ICU APIs from within a C++ UWP application. (It is not intended to be a full stand-alone application, rather it is just an example of calling an ICU method.)

The following small example assumes that there are methods **ErrorMessage** and **OutputMessage** that output the strings to the user in some manner.

``` syntax
// On Windows 10 Creators Update, include the following two headers. With Windows 10 Fall Creators Update and later, you can just include the single header <icu.h>.
#include <icucommon.h>
#include <icui18n.h>

void FormatDateTimeICU()
{
    UErrorCode status = U_ZERO_ERROR;

    // Create a ICU date formatter, using only the 'short date' style format.
    UDateFormat* dateFormatter = udat_open(UDAT_NONE, UDAT_SHORT, nullptr, nullptr, -1, nullptr, 0, &status);

    if (U_FAILURE(status))
    {
        ErrorMessage(L"Failed to create date formatter.");
        return;
    }

    // Get the current date and time.
    UDate currentDateTime = ucal_getNow();

    int32_t stringSize = 0;
    
    // Determine how large the formatted string from ICU would be.
    stringSize = udat_format(dateFormatter, currentDateTime, nullptr, 0, nullptr, &status);

    if (status == U_BUFFER_OVERFLOW_ERROR)
    {
        status = U_ZERO_ERROR;
        // Allocate space for the formatted string.
        auto dateString = std::make_unique<UChar[]>(stringSize + 1);

        // Format the date time into the string.
        udat_format(dateFormatter, currentDateTime, dateString.get(), stringSize + 1, nullptr, &status);

        if (U_FAILURE(status))
        {
            ErrorMessage(L"Failed to format the date time.");
            return;
        }

        // Output the formatted date time.
        OutputMessage(dateString.get());
    }
    else
    {
        ErrorMessage(L"An error occured while trying to determine the size of the formatted date time.");
        return;
    }

    // We need to close the ICU date formatter.
    udat_close(dateFormatter);
}
```

 

 



