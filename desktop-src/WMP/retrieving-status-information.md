---
title: Retrieving Status Information
description: Retrieving Status Information
ms.assetid: 61561520-705a-4d06-a72c-c1cc6315f54e
keywords:
- Windows Media Player online stores,Download Manager
- online stores,Download Manager
- type 2 online stores,Download Manager
- Windows Media Player online stores,retrieving status
- online stores,retrieving status
- type 2 online stores,retrieving status
- Windows Media Player,Download Manager
- Windows Media Player Download Manager
- Download Manager
- retrieving status
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Retrieving Status Information

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Status information is updated using the timer created in the **Init** function. All status is updated using the same timer. The name of the function for the timer event is **OnTimer**.

**OnTimer** determines the information to display based upon the user selection, which is stored in the global variable named g\_oCurrentDLItem. The function first tests whether the size or progress values are valid and creates a string for each case.


```C++
var Size = g_oCurrentDLItem.size <=0 ? "Waiting..." : g_oCurrentDLItem.size + " bytes";
var Progress = g_oCurrentDLItem.progress <=0 ? "Waiting..." : g_oCurrentDLItem.progress + " bytes";

```



If a value is valid, the string represents the byte count. If the value is not valid, such as -1, the string provides a message to inform the user that the information is not yet available.

Next, a **switch** block determines whether the download for the selected item is completed or canceled. If either case is true, the value of the variables Size or Progress is updated accordingly.


```C++
switch(g_oCurrentDLItem.downloadState)
{
    case 3:            
        Size = "Completed";
        Progress = "Completed";
        break;
        
    case 4:
        Size = "Canceled";
        Progress = "Canceled";
        break;
        
    default:
        break;                
}

```



Finally, the status information is displayed in the DIV element named dlstate.

## Related topics

<dl> <dt>

[**Using the Download Manager**](using-the-download-manager.md)
</dt> </dl>

 

 




