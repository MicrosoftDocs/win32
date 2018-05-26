---
title: System.Sound.playSound method
description: Plays a sound file.
ms.assetid: 81bdea7a-6c73-4979-8601-a6943dc23f99
keywords:
- playSound method Windows Sidebar
- playSound method Windows Sidebar , System.Sound object
- System.Sound object Windows Sidebar , playSound method
topic_type:
- apiref
api_name:
- System.Sound.playSound
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

# System.Sound.playSound method

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Plays a sound file.

## Syntax


```JScript
strRetVal = System.Sound.playSound(
  strSound
)
```



## Parameters

<dl> <dt>

*strSound* \[in\]
</dt> <dd>

**String** that specifies the UNC path to the sound file. The maximum length, including the null terminator, is 256 characters.

</dd> </dl>

## Remarks

**playSound** is asynchronous; to stop the currently playing sound, call **playSound** with *strSound* set to **null**.

The sound is assigned to the system notification volume control.

## Examples

The following example demonstrates how to play a sound file.


```JScript
<script>
var mytext = "Sound: chimes.wav";

// --------------------------------------------------------------------
// Initialize the gadget.
// --------------------------------------------------------------------
function Init()
{    
    gadgetContent.innerText = mytext;
    System.Sound.playSound("\\windows\\media\\chimes.wav");
}
</script>
    
</head>
<body onload="Init()">
    <span id="gadgetContent"></span>
</body>
</html>
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





