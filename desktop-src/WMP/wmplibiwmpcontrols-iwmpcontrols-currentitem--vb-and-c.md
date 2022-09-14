---
title: IWMPControls currentItem property
description: The currentItem property gets or sets the current media item in a playlist.
ms.assetid: 0a331b1f-95bd-48ea-b951-1ca35cc96865
keywords:
- currentItem property Windows Media Player
- currentItem property Windows Media Player , IWMPControls interface
- IWMPControls interface Windows Media Player , currentItem property
topic_type:
- apiref
api_name:
- IWMPControls.currentItem
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPControls::currentItem property

The **currentItem** property gets or sets the current media item in a playlist.

## Syntax


```CSharp
public IWMPMedia currentItem {get; set;}
```


```VB

Public Property currentItem As IWMPMedia
```





## Property value

A **WMPLib.IWMPMedia** interface that represents the media item.

## Remarks

This property works only with items in the current playlist. Setting **currentItem** to the interface of a saved media item is not supported.

## Examples

The following example uses **currentItem** to set the player's current media item to an item selected from a list box. The list box has been filled with all of the items in the current playlist. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
private void playItem_OnSelectedIndexChanged(object sender, System.EventArgs e)
{
    int selectedItem = ((System.Windows.Forms.ListBox)sender).SelectedIndex;

    // Ensure that the previous media item is stopped.
    player.Ctlcontrols.stop();

    // Set the current item to the item selected from the list box.
    player.Ctlcontrols.currentItem = player.currentPlaylist.get_Item(selectedItem);
    
    // Play the current item.
    player.Ctlcontrols.play();
}
```


```VB

Public Sub playItem_SelectedIndexChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles playItem.SelectedIndexChanged

    Dim lb As System.Windows.Forms.ListBox = sender
    Dim selectedItem As Integer = lb.SelectedIndex

    &#39; Ensure that the previous media item is stopped.
    player.Ctlcontrols.stop()

    &#39; Set the current item to the item selected from the list box.
    player.Ctlcontrols.currentItem = player.currentPlaylist.Item(selectedItem)

    &#39; Play the current item.
    player.Ctlcontrols.play()

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

[**IWMPControlsInterface (VB and C#)**](iwmpcontrols--vb-and-c.md)
</dt> <dt>

[**IWMPMediaInterface (VB and C#)**](iwmpmedia--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylistCollection.getByName(VB and C#)**](wmplibiwmpplaylistcollection-iwmpplaylistcollection-getbyname--vb-and-c.md)
</dt> </dl>

 

 





