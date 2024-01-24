---
title: IWMPSettings baseURL property
description: The baseURL property gets or sets the base URL used for relative path resolution with URL script commands that are embedded in digital media content.
ms.assetid: e136303f-ba08-434f-ad7e-9fffa66785c4
keywords:
- baseURL property Windows Media Player
- baseURL property Windows Media Player , IWMPSettings interface
- IWMPSettings interface Windows Media Player , baseURL property
topic_type:
- apiref
api_name:
- IWMPSettings.baseURL
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPSettings::baseURL property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **baseURL** property gets or sets the base URL used for relative path resolution with URL script commands that are embedded in digital media content.

## Syntax


```CSharp
public System.String baseURL {get; set;}
```


```VB

Public Property baseURL As System.String
```





## Property value

A **System.String** that is the base URL.

## Remarks

This property specifies the base HTTP URL that is passed as the command parameter by the **AxWindowsMediaPlayer\_WMPOCXEvents\_ScriptCommandEvent** event. The base URL is concatenated with the relative URL as follows:

1.  A trailing forward slash (/) is added to the value retrieved by the **baseURL** property.
2.  A leading period, backward slash, or forward slash character (., \\, and /) is deleted from the relative URL.
3.  The relative URL is added to the end of the base URL.
4.  All slash characters in the resulting fully qualified URL are pointed in the same direction (converted to forward or backward slashes) based on the direction of the first slash character encountered in the new URL.

**Note**

The Windows Media Player control does not support the use of two periods (..) in the relative URL to indicate the parent of the current location.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer.ScriptCommand Event (VB and C#)**](axwmplib-axwindowsmediaplayer-scriptcommand.md)
</dt> <dt>

[**IWMPSettings Interface (VB and C#)**](iwmpsettings--vb-and-c.md)
</dt> </dl>

 

 





