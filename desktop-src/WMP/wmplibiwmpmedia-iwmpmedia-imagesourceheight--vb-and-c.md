---
title: IWMPMedia imageSourceHeight property
description: The imageSourceHeight property gets the height of the current media item in pixels.
ms.assetid: d60f1713-7110-4605-9009-45825c380546
keywords:
- imageSourceHeight property Windows Media Player
- imageSourceHeight property Windows Media Player , IWMPMedia interface
- IWMPMedia interface Windows Media Player , imageSourceHeight property
topic_type:
- apiref
api_name:
- IWMPMedia.imageSourceHeight
- IWMPMedia.get_imageSourceHeight
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPMedia::imageSourceHeight property

The **imageSourceHeight** property gets the height of the current media item in pixels.

This property is read-only.

## Syntax


```CSharp
public System.Int32 imageSourceHeight {get;}
```


```VB

Public ReadOnly Property imageSourceHeight As System.Int32
```





## Property value

A **System.Int32** that is the height of the media item.

## Remarks

If the media item is not the current one, this property returns zero.

Before using this property, you must have read access to the library. For more information, see [Library Access](library-access.md).

## Examples

The following example uses **imageSourceHeight** to display the image size, in pixels, of the current media item in a text box. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
// Create an event handler for the OpenStateChange event.
private void player_OpenStateChange(object sender, AxWMPLib._WMPOCXEvents_OpenStateChangeEvent e)
{
    // Test whether the current media item is open.
    if (e.newState == (int)WMPLib.WMPOpenState.wmposMediaOpen)
    {
         // Store the height and width of the new media item.
         int height = player.currentMedia.imageSourceHeight;
         int width = player.currentMedia.imageSourceWidth;

         // Clear all the information in the text box.
         videoSize.Clear();

         // Test whether an image is visible.
         if (height != 0 && width != 0)
         {
            // Display the image size information.
            videoSize.Text = (width.ToString() + " x " + height.ToString());
         }
    }
}
```


```VB

' Create an event handler for the OpenStateChange event.
Public Sub player_OpenStateChange(ByVal sender As Object, ByVal e As AxWMPLib._WMPOCXEvents_OpenStateChangeEvent) Handles player.OpenStateChange

    &#39; Test whether the current media item is open.
    If (e.newState = WMPLib.WMPOpenState.wmposMediaOpen) Then

        &#39; Store the height and width of the new media item.
        Dim Height As Integer = player.currentMedia.imageSourceHeight
        Dim Width As Integer = player.currentMedia.imageSourceWidth

        &#39; Clear all the information in the text box.
        videoSize.Clear()

        &#39; Test whether an image is visible.
        If (Height <> 0 And Width <> 0) Then

            &#39; Display the image size information.
            videoSize.Text = (Width.ToString() + &quot; x &quot; + Height.ToString())

        End If

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

[**IWMPMedia Interface (VB and C#)**](iwmpmedia--vb-and-c.md)
</dt> </dl>

 

 





