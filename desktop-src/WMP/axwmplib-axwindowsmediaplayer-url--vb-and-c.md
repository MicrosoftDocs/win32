---
title: AxWindowsMediaPlayer.URL property
description: The URL property gets or sets the name of the media item to play.
ms.assetid: 521a3b39-efd6-45a7-895b-a9ae69e0bf39
keywords:
- URL property Windows Media Player
- URL property Windows Media Player , AxWindowsMediaPlayer class
- AxWindowsMediaPlayer class Windows Media Player , URL property
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.URL
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# AxWindowsMediaPlayer.URL property

The URL property gets or sets the name of the media item to play.

## Syntax


```CSharp
public System.String URL {get; set;}
```


```VB

Public Property URL As System.String
```





## Property value

A System.String that is the URL of the media item.

## Remarks

This property can only be set to a URL in a security zone that is the same or is less restrictive than the security zone of the calling program or webpage.

Applications that open media items from behind a firewall will have better performance if the address is specified using the domain name server (DNS) name instead of the IP address.

Do not call this method from event handler code. Calling **URL** from an event handler may yield unexpected results.

## Examples

The following example allows the user to specify a media file by entering a file path in a text box. When a button is clicked, the URL property is set to the specified file and the file is played. The AxWMPLib.AxWindowsMediaPlayer object is represented by the variable named player.


```CSharp
private void openMedia_Click(object sender, System.EventArgs e)
{
    // Set the URL property to the file path obtained from the text box. 
    player.URL = inputURL.Text;

    // Play the media file. 
    player.Ctlcontrols.play();
}
```


```VB

Public Sub openMedia_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles openMedia.Click

    &#39; Set the URL property to the file path obtained from the text box. 
    player.URL = inputURL.Text

    &#39; Play the media file. 
    player.Ctlcontrols.play()

End Sub
```





## Requirements



| Requirement | Value |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                          |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                                    |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib.dll (AxInterop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> </dl>

 

 





