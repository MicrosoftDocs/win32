---
title: IWMPControls currentMarker property
description: The currentMarker property gets or sets the current marker number.
ms.assetid: faf8c32a-66de-47ce-aa3d-6699d9f9bdda
keywords:
- currentMarker property Windows Media Player
- currentMarker property Windows Media Player , IWMPControls interface
- IWMPControls interface Windows Media Player , currentMarker property
topic_type:
- apiref
api_name:
- IWMPControls.currentMarker
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPControls::currentMarker property

The **currentMarker** property gets or sets the current marker number.

## Syntax


```CSharp
public System.Int32 currentMarker {get; set;}
```


```VB

Public Property currentMarker As System.Int32
```





## Property value

A **System.Int32** that is the marker number.

## Remarks

Setting **currentMarker** causes playback to start from the specified marker. Before attempting to set **currentMarker**, determine whether a file has markers and how many it has by using **IWMPMedia.markerCount**. If a file has no markers, setting **currentMarker** to anything but zero results in an error. Setting **currentMarker** to a number higher than **markerCount** also results in an error.

The **currentMarker** property always returns the current or last marker, which means the actual file position can be either at the current marker or before the next marker. Markers are numbered beginning at 1, so if a file has markers, you can set **currentMarker** to zero to change the file position to zero.

Until the current media item is set (using **AxWindowsMediaPlayer.URL** or **AxWindowsMediaPlayer.currentMedia**), **currentMarker** returns zero.

## Examples

The following example uses **currentMarker** to start video playback from the marker that corresponds to the SelectedIndex property of a list box which has been filled with marker identifiers. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
// Fill the list box with the marker identifiers of the current media item.
markers.Items.Add("Begining");
markers.Items.Add("Sunrise");
markers.Items.Add("Car chase");
markers.Items.Add("Happy ending");

// Set the currentMarker to the marker selected from the list box.
private void markers_OnSelectedIndexChanged(object sender, System.EventArgs e)
{
    int selectedMarker = ((System.Windows.Forms.ListBox)sender).SelectedIndex;

    player.Ctlcontrols.currentMarker = selectedMarker;
}
```


```VB

' Fill the list box with the marker identifiers of the current media item.
markers.Items.Add(&quot;Begining&quot;)
markers.Items.Add(&quot;Sunrise&quot;)
markers.Items.Add(&quot;Car chase&quot;)
markers.Items.Add(&quot;Happy ending&quot;)

&#39; Set the currentMarker to the marker selected from the list box.
Public Sub markers_SelectedIndexChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles markers.SelectedIndexChanged

    Dim lb As System.Windows.Forms.ListBox = sender
    Dim selectedMarker As Integer = lb.SelectedIndex

    player.Ctlcontrols.currentMarker = selectedMarker

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

[**AxWindowsMediaPlayer.currentMedia (VB and C#)**](axwmplib-axwindowsmediaplayer-currentmedia--vb-and-c.md)
</dt> <dt>

[**AxWindowsMediaPlayer.URL (VB and C#)**](axwmplib-axwindowsmediaplayer-url--vb-and-c.md)
</dt> <dt>

[**IWMPControls Interface (VB and C#)**](iwmpcontrols--vb-and-c.md)
</dt> <dt>

[**IWMPMedia.markerCount (VB and C#)**](wmplibiwmpmedia-iwmpmedia-markercount--vb-and-c.md)
</dt> </dl>

 

 





