---
description: The SWbemDateTime object is a helper object to parse and set Common Information Model (CIM) datetime values.
ms.assetid: 3dd34c73-3c2b-4d59-827b-169cf8020213
ms.tgt_platform: multiple
title: SWbemDateTime object (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemDateTime
- ISWbemDateTime
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemDateTime object

The **SWbemDateTime** object is a helper object to parse and set Common Information Model (CIM) [datetime](datetime.md) values. It plays a role similar to [**SWbemObjectPath**](swbemobjectpath.md), which provides assistance to format and interpret object paths. You can use the VBScript [CreateObject](/previous-versions//xzysf6hc(v=vs.85)) call to create the **SWbemDateTime** object.

An **SWbemDateTime** object can be initialized from and formatted in either **VT\_DATE** or **FILETIME** values using methods on the object. Using properties of the object, the value can be parsed into component year, month, day, hour, minutes, seconds, or microseconds. The **SWbemDateTime** object can be formatted into either local or Coordinated Universal Time (UTC) values. For more information, see [Date and Time Format](date-and-time-format.md).

**SWbemDateTime** is the only Windows Management Instrumentation (WMI) scripting object that is marked safe for initialization and scripts running on HTML pages in Internet Explorer.

## Members

The **SWbemDateTime** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SWbemDateTime** object has these methods.



| Method                                           | Description                                                                                                          |
|:-------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------|
| [**GetFileTime**](swbemdatetime-getfiletime.md) | Converts a **FILETIME** date and time, expressed as a **BSTR**, to a WMI [DATETIME](datetime.md) format.<br/> |
| [**GetVarDate**](swbemdatetime-getvardate.md)   | Converts a WMI [DATETIME](datetime.md) formatted date and time value to a **VT\_DATE**.<br/>                  |
| [**SetFileTime**](swbemdatetime-setfiletime.md) | Converts a WMI [DATETIME](datetime.md) format to a **FILETIME** date and time, expressed as a **BSTR**.<br/>  |
| [**SetVarDate**](swbemdatetime-setvardate.md)   | Converts a **VT\_DATE** formatted date and time to a WMI [DATETIME](datetime.md).<br/>                        |



 

### Properties

The **SWbemDateTime** object has these properties.



| Property                                                                        | Access type           | Description                                                                                                                     |
|:--------------------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------|
| [**Day**](swbemdatetime-day.md)<br/>                                     | Read/write<br/> | The day component of a CIM [datetime](datetime.md) value.<br/>                                                           |
| [**DaySpecified**](swbemdatetime-dayspecified.md)<br/>                   | Read/write<br/> | Indicates whether the day is specified or left as a wildcard.<br/>                                                        |
| [**Hours**](swbemdatetime-hours.md)<br/>                                 | Read/write<br/> | The hours of the day component of a CIM [datetime](datetime.md) value.<br/>                                              |
| [**HoursSpecified**](swbemdatetime-hoursspecified.md)<br/>               | Read/write<br/> | Indicates whether the hour is specified or left as a wildcard.<br/>                                                       |
| [**IsInterval**](swbemdatetime-isinterval.md)<br/>                       | Read/write<br/> | Indicates that at least one component of the CIM [datetime](datetime.md) represents an interval rather than a date.<br/> |
| [**Microseconds**](swbemdatetime-microseconds.md)<br/>                   | Read/write<br/> | The microseconds component of a CIM [datetime](datetime.md) value.<br/>                                                  |
| [**MicrosecondsSpecified**](swbemdatetime-microsecondsspecified.md)<br/> | Read/write<br/> | Indicates whether the microseconds component is specified or left as a wildcard.<br/>                                     |
| [**Minutes**](swbemdatetime-minutes.md)<br/>                             | Read/write<br/> | The minutes component of a CIM [datetime](datetime.md) value.<br/>                                                       |
| [**MinutesSpecified**](swbemdatetime-minutesspecified.md)<br/>           | Read/write<br/> | Indicates whether the minutes component is specified or left as a wildcard.<br/>                                          |
| [**Month**](swbemdatetime-month.md)<br/>                                 | Read/write<br/> | The month component of a CIM [datetime](datetime.md) value.<br/>                                                         |
| [**MonthSpecified**](swbemdatetime-monthspecified.md)<br/>               | Read/write<br/> | Indicates whether the month is specified or left as a wildcard.<br/>                                                      |
| [**Seconds**](swbemdatetime-seconds.md)<br/>                             | Read/write<br/> | The seconds component of a CIM [datetime](datetime.md) value.<br/>                                                       |
| [**SecondsSpecified**](swbemdatetime-secondsspecified.md)<br/>           | Read/write<br/> | Indicates whether the seconds component is specified or left as a wildcard.<br/>                                          |
| [**UTC**](swbemdatetime-utc.md)<br/>                                     | Read/write<br/> | The UTC component of a CIM [datetime](datetime.md) value.<br/>                                                           |
| [**UTCSpecified**](swbemdatetime-utcspecified.md)<br/>                   | Read/write<br/> | Indicates whether the UTC component is specified or left as a wildcard.<br/>                                              |
| [**Value**](swbemdatetime-value.md)<br/>                                 | Read/write<br/> | The full CIM [datetime](datetime.md) value.<br/>                                                                         |
| [**Year**](swbemdatetime-year.md)<br/>                                   | Read/write<br/> | The year component of a CIM [datetime](datetime.md) value.<br/>                                                          |
| [**YearSpecified**](swbemdatetime-yearspecified.md)<br/>                 | Read/write<br/> | Indicates whether or not the year is specified or left as a wildcard.<br/>                                                |



 

## Remarks

WMI records timestamps in universal time coordinate (UTC) format. UTC is not the format that most developers and IT administrators use. Therefore, a common issue is determining how to translate UTC into something more readable. For more information on how to work with UTC, see [WMI Tasks: Dates and Times](wmi-tasks--dates-and-times.md) and [Working with Dates and Times using WMI](/previous-versions/tn-archive/ee198928(v=technet.10)). You can also read the [It s About Time (Oh, and About Dates, Too)](/previous-versions/technet-magazine/cc160973(v=msdn.10)) and [How Can I Subtract a Specified Number of Days from a UTC Value?](https://blogs.technet.com/b/heyscriptingguy/archive/2006/07/21/how-can-i-subtract-a-specified-number-of-days-from-a-utc-value.aspx) blog posts for additional information.

Any numeric field can have a wildcard value if the [**IsInterval**](swbemdatetime-isinterval.md) property is set to **FALSE**. Fields with wildcard values contain asterisks in the entire field.

Each property, for example [**Day**](swbemdatetime-day.md), has a corresponding specified Boolean value, such as [**DaySpecified**](swbemdatetime-dayspecified.md). When **DaySpecified** is **FALSE**, then the value is interpreted as an interval rather than a number between 01 and 31. If an interval is used anywhere in the CIM [datetime](datetime.md) value, then [**IsInterval**](swbemdatetime-isinterval.md) is also set to **TRUE**. The default is for a CIM datetime value to contain a date rather than one or more intervals.

For example, if [**SWbemDateTime.DaySpecified**](swbemdatetime-dayspecified.md) is **TRUE**, then [**SWbemDateTime.Value**](swbemdatetime-value.md) includes the current value of [**SWbemDateTime.Day**](swbemdatetime-day.md), otherwise it is a wildcard value. The [**IsInterval**](swbemdatetime-isinterval.md) property is **FALSE** in either case.

## Examples

The following script code example shows how to use an **SWbemDateTime** object to parse a datetime property value read from the WMI repository, the **InstallDate** property in [**Win32\_OperatingSystem**](/windows/desktop/CIMWin32Prov/win32-operatingsystem).


```VB
' Create a new datetime object.
Set dateTime = CreateObject("WbemScripting.SWbemDateTime")

' Retrieve a WMI object that contains a datetime value.
for each os in GetObject( _
    "winmgmts:").InstancesOf ("Win32_OperatingSystem")

    ' The InstallDate property is a CIM_DATETIME. 
    MsgBox os.InstallDate
    dateTime.Value = os.InstallDate

    ' Display the year of installation.
    MsgBox "This OS was installed in the year " & dateTime.Year

    ' Display the installation date using the VT_DATE format.
    MsgBox "Full installation date (VT_DATE format) is " _
    & dateTime.GetVarDate

    ' Display the installation date using the FILETIME format.
    MsgBox "Full installation date (FILETIME format) is " _
    & dateTime.GetFileTime 
next
Set datetime = Nothing
```



The following example shows how to create an **SWbemDateTime** object, store a date value in the object, display the date as local and Coordinated Universal Time (UTC), and store the value in a newly created class and property. For more information about the constant **wbemCimtypeDatetime**, see [WbemCimtypeEnum](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemcimtypeenum).


```VB
' Create an SWbemDateTime object.
Set dateTime = CreateObject("WbemScripting.SWbemDateTime")
' Set the value 
Const wbemCimTypeDatetime = 101

' Construct a datetime value using the intrinsic VBScript CDate
' function interpreting this as a local date/time in
' the Pacific time zone (-8 hrs GMT). Convert to CIM datetime
' using SetVarDate method. The year defaults to current year.
dateTime.SetVarDate (CDate ("January 20 11:56:32"))

' The value in dateTime displays as 
' 20000120195632.000000-480. This is the equivalent time
' in GMT with the specified offset for PST of -8 hrs.
MsgBox "CIM datetime " & dateTime

' The value now displays as B=0/2000 11:56:32 AM because the
' parameter contains the default TRUE value causing the value to be
' interpreted as a local time.
MsgBox "Local datetime " & dateTime.GetVarDate ()

' The value now displays as B=0/2000 7:56:32 PM because the
' parameter value is FALSE, which indicates a GMT time.
' non-local time.
MsgBox "Datetime in GMT " & dateTime.GetVarDate (false)

' Create a new class and add a DateTime property value.
' SWbemServices.Get returns an empty SWbemObject
' which can become a new class. SWbemObject.Path_ returns an
' SWbemObjectPath object. 
set NewObject = GetObject("winmgmts:root\default").Get
NewObject.Path_.Class = "NewClass"

' Add a new property named "InterestingDate" to the NewObject class
' and define its datatype as a CIM datetime value.
NewObject.Properties_.Add "InterestingDate", wbemCimtypeDatetime

' Set the new value of the SWbemDateTime object in the InterestingDate
' property.
NewObject.InterestingDate = dateTime.Value
MsgBox "Datetime in new object " & NewObject.InterestingDate

' Write the new class (named "NewClass") containing
' the SWbemDateTime object to the repository.
NewObject.Put_
WScript.Echo "NewClass is now in WMI repository"

' Clean up the example by deleting the new class from the repository
NewObject.Delete_
```



The following script code example shows how to use an **SWbemDateTime** object to modify an interval value on a property that is read from the WMI repository.


```VB
' Construct an interval value of 100 days, 1 hour, and 3 seconds.
dateTime.IsInterval = true 
dateTime.Day = 100
dateTime.Hours = 1
dateTime.Seconds = 3

' The datetime displays as 00000100010003.000000:000.
MsgBox "Constructed interval value " & datetime

' Retrieve an empty WMI object and add a datetime property. 
Const wbemCimTypeDatetime = 101
Set NewObject = GetObject("winmgmts:root\default").Get
NewObject.Path_.Class = "Empty"
NewObject.Properties_.Add "InterestingDate", wbemCimtypeDatetime

' Set the new value in the property and update. 
NewObject.InterestingDate = dateTime.Value
MsgBox "NewObject.InterestingDate = " & NewObject.InterestingDate

' Write the new SWbemDateTime object to the repository.
NewObject.Put_

' Delete the object.
NewObject.Delete_
```



The following script code example shows how to use an **SWbemDate** object to read a **FILETIME** value.


```VB
' Create a new datetime object.
Set datetime = CreateObject("WbemScripting.SWbemDateTime")

' Set from a FILETIME value (non-local).
' Assume a timezone -7 hrs. GMT.
MsgBox "FILETIME value " & "126036951652030000"
datetime.SetFileTime "126036951652030000", false

' Displays as 5/24/2000 7:26:05 PM.
MsgBox "GMT time " & dateTime.GetVarDate   

' Set from a FILETIME value (local).
datetime.SetFileTime "126036951652030000"

' Displays as 5/25/2000 2:26:05 AM.
MsgBox "Same value in local time " & dateTime.GetVarDate
Set datetime = Nothing
```



The following PowerShell code creates an instance of a SWbemDateTime object, retrieves the OS install date, and converts the date to a different format


```PowerShell
# Create swbemdatetime object
$datetime = New-Object -ComObject WbemScripting.SWbemDateTime

#  Get OS installation time and assign to datetime object
$os = Get-WmiObject -Class Win32_OperatingSystem
$dateTime.Value = $os.InstallDate

# Now display the time
"This OS was installed in the year {0}"           -f $dateTime.Year
"Full installation date (VT_DATE format) is {0}"  -f $dateTime.GetVarDate()
"Full installation date (FILETIME format) is {0}" -f $dateTime.GetFileTime() 
```



The following Powershell code translates the code into a format ready to be consumed by a CIM provider.


```PowerShell
 $time = (Get-Date)
 $objScriptTime = New-Object -ComObject WbemScripting.SWbemDateTime
 $objScriptTime.SetVarDate($time)
 $cimTime = $objScriptTime.Value
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemDateTime<br/>                                                         |
| IID<br/>                      | IID\_ISWbemDateTime<br/>                                                          |



## See also

<dl> <dt>

[WbemCimtypeEnum](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemcimtypeenum)
</dt> <dt>

[DATETIME](datetime.md)
</dt> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> </dl>

 

