---
title: IWMPSettings rate property
description: The rate property gets or sets the current playback rate for video.
ms.assetid: 7baa667b-52e5-4419-8e12-c3627a417b20
keywords:
- rate property Windows Media Player
- rate property Windows Media Player , IWMPSettings interface
- IWMPSettings interface Windows Media Player , rate property
topic_type:
- apiref
api_name:
- IWMPSettings.rate
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPSettings::rate property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **rate** property gets or sets the current playback rate for video.

## Syntax


```CSharp
public System.Double rate {get; set;}
```


```VB

Public Property rate As System.Double
```





## Property value

A **System.Double** that is the playback rate, with a default value of 1.0.

## Remarks

The value retrieved by this property acts as a multiplier value that enables you to play a media item at a faster or slower rate. The default value of 1.0 indicates the authored speed.

Note that an audio track becomes difficult to understand at rates lower than 0.5 or higher than 1.5. A playback rate of 2 indicates twice the normal playback speed.

Windows Media Player will attempt to use the most effective of the following four different playback modes

-   Smooth video playback with audio pitch maintained
-   Smooth video playback with audio pitch not maintained
-   Smooth video playback with no audio
-   Keyframe video playback with no audio

The mode chosen by Windows Media Player depends on numerous factors including file type and location, operating system, network, and server.

Other considerations apply as well, depending on the digital media format used to create the content:

-   **Windows Media Video (WMV) and ASF.** Optimal values for the **rate** property are from 1 to 10, or from  1 to  10 for reverse play. Values from 0.5 to 1.0 or from -0.5 to -1.0 may also work well in cases where audio pitch can be maintained, such as when playing files located on the local computer. Values with an absolute magnitude greater than 10 are allowed, but are not very meaningful.
-   **Other video formats.** The **rate** property can range from 0 to 9. Negative values are not allowed. Values less than 1 represent slow motion. Values above 9 are allowed, but are not very meaningful.

The **IWMPControls.fastForward** method changes the value of **rate** to 5.0, while the **IWMPControls.fastReverse** method changes the value of **rate** to  5.0.

The playback rate of some digital media formats cannot be altered. Use the **IWMPSettings.isAvailable** property (In C# the **IWMPSettings.get\_isAvailable** method) to discover whether this property can be specified for a particular media item.

## Examples

The following example uses a numeric updown control that allows the user to change the playback speed of the current media. When the user clicks the up or down arrows of the control, the **rate** property is set to the new value. The possible range of values in the control are 0.5 (half-speed) to 2.0 (double-speed). The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
private void playbackRate_Click(object sender, System.EventArgs e)
{
    // Get the new value of the control, and cast it from decimal to double.
    double newRate = (double)((System.Windows.Forms.NumericUpDown)sender).Value;

    // Test whether playback rate can be set. 
    if( player.settings.get_isAvailable("Rate") )
    {
        // Set the playback rate to the new value.
        player.settings.rate = newRate;
    }
}
```


```VB

Public Sub playbackRate_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles playbackRate.Click

    &#39;  Get the new value of the control as a double.
    Dim nUpDown As System.Windows.Forms.NumericUpDown = sender
    Dim newRate As Double = nUpDown.Value

    &#39;  Test whether playback rate can be set. 
    If (player.settings.isAvailable(&quot;Rate&quot;)) Then

        &#39;  Set the playback rate to the new value.
        player.settings.rate = newRate

    End If

End Sub
```





## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPControls.fastForward (VB and C#)**](wmplibiwmpcontrols-iwmpcontrols-fastforward--vb-and-c.md)
</dt> <dt>

[**IWMPControls.fastReverse (VB and C#)**](wmplibiwmpcontrols-iwmpcontrols-fastreverse--vb-and-c.md)
</dt> <dt>

[**IWMPSettings Interface (VB and C#)**](iwmpsettings--vb-and-c.md)
</dt> <dt>

[**IWMPSettings.isAvailable (VB and C#)**](iwmpsettings-isavailable--vb-and-c.md)
</dt> <dt>

[**IWMPSettings.mute (VB and C#)**](wmplibiwmpsettings-iwmpsettings-mute--vb-and-c.md)
</dt> </dl>

 

 





