---
title: Settings.rate
description: The rate property specifies or retrieves the current playback rate of video media.
ms.assetid: 0f95f7ac-1bb6-4c80-89eb-eb300a03a0f1
keywords:
- Settings.rate Windows Media Player
topic_type:
- apiref
api_name:
- Settings.rate
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Settings.rate

The **rate** property specifies or retrieves the current playback rate of video media.

## Syntax

player.settings.rate

## Possible Values

This property is a read/write **Number** (**double**) with a default value of 1.0.

## Remarks

This property acts as a multiplier value that allows you to play a clip at a faster or slower rate. The default value of 1.0 indicates the authored speed. Note that an audio track becomes difficult to understand at rates lower than 0.5 or higher than 1.5. A playback rate of 2 equates to twice the normal playback speed.

Windows Media Player will attempt to use the most effective of four different playback modes. These modes are smooth video playback with audio pitch maintained, smooth video playback with audio pitch not maintained, smooth video playback with no audio, and keyframe video playback with no audio. The mode chosen by the Player depends on numerous factors including file type and location, operating system, network, and server.

Other considerations apply as well, depending on media type:

-   Windows Media Format (WMV) and ASF files: Optimal values for this property are from 1 to 10, or from  1 to  10 for reverse play. Values from 0.5 to 1.0 or from -0.5 to -1.0 may also work well in cases where audio pitch can be maintained, for example, when playing files located on the local computer. Values with an absolute magnitude greater than 10 are allowed, but are not very meaningful.
-   Other Video Media Types: This property can range from 0 to 9. Negative values are not allowed. Values less than 1 represent slow motion. Values above 9 are allowed, but are not very meaningful.

The *Controls*.**fastForward** method changes the value of **rate** to 5.0, while the *Controls*.**fastReverse** method changes **rate** to  5.0.

The playback rate of some media types cannot be altered. Use the *Settings*.**isAvailable** method to determine whether this property can be specified for a particular media item.

**Windows Media Player 10 Mobile**: This property only accepts or returns values of -5.0, 1.0, or 5.0.

## Examples

The following example creates an HTML SELECT element that allows the user to change the playback speed of the current media. The SELECT options offer normal speed, half -speed and double-speed playback rates. The **Player** object was created with ID = "Player".


```
<!-- Create the HTML SELECT element. -->
<SELECT  ID = pbRATE  NAME = "pbRATE"  LANGUAGE="JScript"
         onChange="
                   /* Test whether playback rate can be set. */
                   if(Player.settings.IsAvailable('Rate'))

                   /* Set the playback rate based on the current
                      value of the SELECT element. */
                   Player.settings.rate = this.value
">

/* Create the OPTION list. */
<OPTION VALUE = 1>NORMAL</OPTION>
<OPTION VALUE = .5>half speed</OPTION>
<OPTION VALUE = 2>2 speed</OPTION>
</SELECT>

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Controls.fastForward**](controls-fastforward.md)
</dt> <dt>

[**Controls.fastReverse**](controls-fastreverse.md)
</dt> <dt>

[**Settings Object**](settings-object.md)
</dt> <dt>

[**Settings.isAvailable**](settings-isavailable.md)
</dt> </dl>

 

 





