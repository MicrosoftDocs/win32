---
title: System.Sound.beep method
description: Plays a simple waveform sound.
ms.assetid: 18bf81df-0c10-4ff9-b69d-7284d9bbb239
keywords:
- beep method Windows Sidebar
- beep method Windows Sidebar , System.Sound object
- System.Sound object Windows Sidebar , beep method
topic_type:
- apiref
api_name:
- System.Sound.beep
api_location:
- Sidebar.Exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Sound.beep method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Plays a simple waveform sound.

## Syntax


```JScript
System.Sound.beep()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

After queuing the sound, control is returned to the calling function and the sound plays asynchronously.

Muting and volume control have no effect on **System.Sound.beep**.

## Examples

The following example demonstrates how to play the beep sound every second.


```JScript
var tHours;
var tMinutes;
var tSeconds;
var oSelectedTimeZone = System.Time.currentTimeZone;

// --------------------------------------------------------------------
// Initialize the gadget.
// --------------------------------------------------------------------
function Init()
{    
    // Initialize the time display.
    DisplayTime();
    setInterval("DisplayTime()",1000);
}

// --------------------------------------------------------------------
// Display the system time based on selected time zone.
// --------------------------------------------------------------------
function DisplayTime()
{
    // Retrieve the local time.
    var sTimeInfo = System.Time.getLocalTime(oSelectedTimeZone);
    if (sTimeInfo != "")
    {
        System.Sound.beep();
        var dDateInfo = new Date(Date.parse(sTimeInfo));   
        tHours = dDateInfo.getHours();
        tMinutes = dDateInfo.getMinutes();
        tMinutes = ((tMinutes < 10) ? ":0" : ":") + tMinutes
        tSeconds = dDateInfo.getSeconds();
        tSeconds = ((tSeconds < 10) ? ":0" : ":") + tSeconds;
        timeDisplay.innerHTML = tHours + tMinutes + tSeconds;
    }
    else
    {
        // Display something else.
    }
}

```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Utilapiset.h</dt> </dl>                        |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





