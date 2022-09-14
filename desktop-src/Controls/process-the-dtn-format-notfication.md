---
title: How to Process the DTN_FORMAT Notification
description: This topic demonstrates how to process a format notification sent by the date and time picker (DTP) control.
ms.assetid: 7B559846-FE52-4181-B25D-888BE90EB038
ms.topic: article
ms.date: 05/31/2018
---

# How to Process the DTN\_FORMAT Notification

This topic demonstrates how to process a format notification sent by the date and time picker (DTP) control.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions


A DTP control sends the [DTN\_FORMAT](dtn-format.md) notification to request text that will be displayed in a callback field of the control. Your application must handle this notification to enable the DTP control to display information that it does not natively support.

The following C++ code example is an application-defined function (**DoFormat**) that processes [DTN\_FORMAT](dtn-format.md) notification codes by providing a text string for a callback field. The application calls the **GetDayNum** application-defined function to request the day number to be used in the callback string.


```C++
//  DoFormat processes DTN_FORMAT to provide the text for a callback
//  field in a DTP control. In this example, the callback field
//  contains a value for the day of year. The function calls the 
//  application-defined function GetDayNum (below) to retrieve
//  the correct value. StringCchPrintf truncates the formatted string if
//  the entire string will not fit into the destination buffer. 

void WINAPI DoFormat(HWND hwndDP, LPNMDATETIMEFORMAT lpDTFormat)
{
HRESULT hr = StringCchPrintf(lpDTFormat->szDisplay,
                sizeof(lpDTFormat->szDisplay)/sizeof(lpDTFormat->szDisplay[0]),
                L"%d",GetDayNum(&lpDTFormat->st));
if(SUCCEEDED(hr))
 {
   // Insert code here to handle the case when the function succeeds.      
 }
else
 {
   // Insert code here to handle the case when the function fails or the string 
   // is truncated.
 }
}
```



**The GetDayNum application-defined function**

The application-defined sample function **DoFormat** calls the following **GetDayNum** application-defined function to request the day number based on the current date. **GetDayNum** returns an **INT** value that represents the current day of the year, from 0 to 366. This function calls another application-defined function, **IsLeapYr**, during processing.


```C++
//  GetDayNum is an application-defined function that retrieves the 
//  correct day of year value based on the contents of a given 
//  SYSTEMTIME structure. This function calls the IsLeapYr function to 
//  check if the current year is a leap year. The function returns an 
//  integer value that represents the day of year.

int WINAPI GetDayNum(SYSTEMTIME *st)
{
    int iNormYearAccum[ ] = {31,59,90,120,151,181,
                            212,243,273,304,334,365};
    int iLeapYearAccum[ ] = {31,60,91,121,152,182,
                            213,244,274,305,335,366};
    int iDayNum;

    if(IsLeapYr(st->wYear))
        iDayNum=iLeapYearAccum[st->wMonth-2]+st->wDay;
    else
        iDayNum=iNormYearAccum[st->wMonth-2]+st->wDay;

    return (iDayNum);
}        
```



**The IsLeapYr application-defined function**

The application-defined function **GetDayNum** calls the **IsLeapYr** function to determine whether the current year is a leap year. **IsLeapYr** returns a **BOOL** value that is **TRUE** if it is a leap year and **FALSE** otherwise.


```C++
//  IsLeapYr determines if a given year value is a leap year. The
//  function returns TRUE if the current year is a leap year, and 
//  FALSE otherwise.

BOOL WINAPI IsLeapYr(int iYear)
{
    BOOL fLeapYr = FALSE;

    // If the year is evenly divisible by 4 and not by 100, but is 
    // divisible by 400, it is a leap year.
    if ((!(iYear % 4))             // each even fourth year
            && ((iYear % 100)      // not each even 100 year
            || (!(iYear % 400))))  // but each even 400 year
        fLeapYr = TRUE;

    return (fLeapYr);
}        
```



## Related topics

<dl> <dt>

[Using Date and Time Picker Controls](using-date-and-time-picker.md)
</dt> <dt>

[Date and Time Picker Control Reference](bumper-date-and-time-picker-date-and-time-picker-control-reference.md)
</dt> <dt>

[Date and Time Picker](date-and-time-picker-control-reference.md)
</dt> </dl>

 

 




