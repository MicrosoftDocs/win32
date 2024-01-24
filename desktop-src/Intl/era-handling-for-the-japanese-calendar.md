---
description: Era Handling for the Japanese Calendar
ms.assetid: a1dabf7c-6521-492e-bdc0-27cfb07cfc20
title: Era Handling for the Japanese Calendar
ms.topic: article
ms.date: 05/31/2018
---

# Era Handling for the Japanese Calendar

Many calendars have eras, such as AD/BC or CE/BCE. In the Japanese Calendar, years are described by nengō, a combination of the year number and era name. For example, 2009 is Heisei 21. In the past, Japanese era names changed frequently, but now the Japanese eras change only on imperial succession. Windows and Microsoft .NET have historically supported the four modern eras under this policy: Meiji, Taishō, Shōwa and Heisei.

With Windows 7, Windows Server 2008 R2, and the .NET Framework 4, Microsoft recognizes that additional eras may be added in the future. On these versions of Windows the era data is stored in the registry under the key:<dl> HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Nls\\Calendars\\Japanese\\Eras  
</dl>

If necessary, additional eras can be added to that key through the normal Windows Update process. This key can be viewed using the registry editor (Regedit.exe). An example of the key and values shipped in Windows 7 is:

``` syntax
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Nls\Calendars\Japanese\Eras]
"1868 01 01"="明治_明_Meiji_M"
"1912 07 30"="大正_大_Taisho_T"
"1926 12 25"="昭和_昭_Showa_S"
"1989 01 08"="平成_平_Heisei_H"
```

The name of each era value is the date the era begins in the Gregorian calendar. The value contains the era name in Japanese, the abbreviated name in Japanese, the name in English, and an abbreviated name in English:<dl> "YYYY MM DD"="JE\_AJE\_EE\_AEE"  
</dl>where

-   "YYYY MM DD" is the Gregorian date of the start of the era in year, month, day form where year is 4 digits, day is 2 digits and month is also 2 digits. A space separates each part of the date.
-   "JE" is the Japanese name of the era, and is followed by an underscore.
-   "AJE" is the abbreviated name of the era, in Japanese, and is followed by an underscore.
-   "EE" is the English name of the Japanese era, and is followed by an underscore.
-   "AEE" is the abbreviated English name of the Japanese era.

One consideration for application developers is the possibility that additional eras will be added by Windows Update or other means. In that case the application may encounter more than the expected four eras for the Japanese calendar. For testing purposes testers may add an additional era to the registry; however, that should be restricted to test machines only, as it impacts the behavior of the entire machine.

An example of such a key that could be used for test follows. This change can be made with the registry editor. (This is an example for test use only, and is not intended to predict any future additions.)

``` syntax
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Nls\Calendars\Japanese\Eras]
"2020 09 01"="仮名_仮_Test Era_X"
```

Note that this only impacts machines running Windows 7 and later or .NET Framework 4 and later. Application developers are encouraged to test their applications with such additional test eras to ensure that their applications will continue to work if additional eras are added at some future date.

## Related topics

<dl> <dt>

[Retrieving Time and Date Information](retrieving-time-and-date-information.md)
</dt> <dt>

[Calendar Identifiers](calendar-identifiers.md)
</dt> </dl>

 

 



