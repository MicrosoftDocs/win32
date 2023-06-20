---
title: IWMPControls.isAvailable (VB and C )
description: The isAvailable property (the get\_isAvailable method in C\ ) gets a value indicating whether a specified type of information is available or a specified action can be performed.
ms.assetid: 00812d5c-513e-49d5-93ba-750b81a852dd
keywords:
- IWMPControls.isAvailable (VB and C ) Windows Media Player
topic_type:
- apiref
api_name:
- IWMPControls.isAvailable (VB and C )
api_location:
- Interop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPControls.isAvailable (VB and C#)

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **isAvailable** property (the **get\_isAvailable** method in C#) gets a value indicating whether a specified type of information is available or a specified action can be performed.


```
[Visual Basic]
ReadOnly Property isAvailable(
  bstrItem As System.String
) As System.Boolean
```




```
[C#]
bool get_isAvailable (
  System.String bstrItem
);
```



## Parameters

*bstrItem*

A System.String that is one of the following values.



| Value           | Description                                                                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| currentItem     | Discovers whether the user can set the **IWMPControls.currentItem** property.                                                                                     |
| currentMarker   | Discovers whether the user can seek to a specific marker.                                                                                                         |
| currentPosition | Discovers whether the user can seek to a specific position in the file. Some files do not support seeking.                                                        |
| fastForward     | Discovers whether the file supports fast forwarding and whether that functionality can be invoked. Many file types (and live streams) do not support fastForward. |
| fastReverse     | Discovers whether the file supports fastReverse and whether that functionality can be invoked. Many file types (and live streams) do not support fastReverse.     |
| next            | Discovers whether the user can seek to the next entry in a playlist.                                                                                              |
| pause           | Discovers whether the **IWMPControls.pause** method is available.                                                                                                 |
| play            | Discovers whether the **IWMPControls.play** method is available.                                                                                                  |
| previous        | Discovers whether the user can seek to the previous entry in a playlist.                                                                                          |
| step            | Discovers whether the **IWMPControls2.step** method is available during playback.                                                                                 |
| stop            | Discovers whether the **IWMPControls.stop** method is available.                                                                                                  |



 

## Property Value

**System.Boolean**

A **System.Boolean** that indicates whether a specified type of information is available or a specified action can be performed.

## Remarks

**IWMPControls.isAvailable** is a property in Visual Basic that takes a parameter. In C# it is referred to as the **IWMPControls.get\_isAvailable** method.

## Examples

The following example uses the **isAvailable** property (the **get\_isAvailable** method in C#) to verify that the current media item supports the **currentPosition** property. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
// If the currentPosition property is supported, seek to position 0.
if (player.Ctlcontrols.get_isAvailable("currentPosition"))
{
    player.Ctlcontrols.currentPosition = 0;
}
```


```VB

' If the currentPosition property is supported, seek to position 0.
If (player.Ctlcontrols.isAvailable(&quot;currentPosition&quot;)) Then

    player.Ctlcontrols.currentPosition = 0

End If
```





## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPControls Interface (VB and C#)**](iwmpcontrols--vb-and-c.md)
</dt> <dt>

[**IWMPControls.currentItem (VB and C#)**](wmplibiwmpcontrols-iwmpcontrols-currentitem--vb-and-c.md)
</dt> <dt>

[**IWMPControls.pause (VB and C#)**](wmplibiwmpcontrols-iwmpcontrols-pause--vb-and-c.md)
</dt> <dt>

[**IWMPControls.play (VB and C#)**](wmplibiwmpcontrols-iwmpcontrols-play--vb-and-c.md)
</dt> <dt>

[**IWMPControls.stop (VB and C#)**](wmplibiwmpcontrols-iwmpcontrols-stop--vb-and-c.md)
</dt> <dt>

[**IWMPControls2.step (VB and C#)**](wmplibiwmpcontrols2-iwmpcontrols2-step--vb-and-c.md)
</dt> </dl>

 

 





