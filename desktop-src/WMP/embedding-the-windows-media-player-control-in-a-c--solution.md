---
title: Embedding the Windows Media Player Control in a C Solution
description: Embedding the Windows Media Player Control in a C\ Solution
ms.assetid: 0889cfd8-ed1f-4d0c-aff8-bff2f55ffccb
keywords:
- Windows Media Player,embedding ActiveX control
- Windows Media Player object model,embedding ActiveX control
- object model,embedding ActiveX control
- Windows Media Player Mobile,embedding ActiveX control
- Windows Media Player ActiveX control,embedding
- Windows Media Player Mobile ActiveX control,embedding
- ActiveX control,embedding
- Windows Media Player,C
- Windows Media Player object model,C
- object model,C
- Windows Media Player Mobile,C
- Windows Media Player ActiveX control,C
- Windows Media Player Mobile ActiveX control,C
- ActiveX control,C
- embedding,C programs
- C program embedding
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Embedding the Windows Media Player Control in a C# Solution

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To use the functionality of Windows Media Player in a C# application, first add the component to a form as described in [Using the Windows Media Player Control with Microsoft Visual Studio](using-the-windows-media-player-control-with-microsoft-visual-studio.md)

The following sections describe how to create an application that plays video and uses custom play and stop buttons.

## Add the Video Window

Add the Windows Media Player ActiveX control to a form. Resize the control, and then place it where you want the video window to appear.

Select the Windows Media Player control, then change the **uiMode** property to "none". This setting hides the UI controls. When the user plays a video, it will appear in the window. For audio-only content, a visualization will appear.

## Add Two Buttons and Adjust the Form

Now, add two buttons to the form. Select the first button and change the **Text** property to "Play". Select the second button and change its **Text** property to "Stop".

## Add the Play Code

Double-click the **Play** button to reveal the Code window. In C#, the following code will be displayed:


```CSharp
private void button1_Click(object sender, System.EventArgs e)
{

}

```



Add this line between the two curly braces:


```CSharp
axWindowsMediaPlayer1.URL = @"c:\mediafile.wmv";

```



In the preceding code example, "axWindowsMediaPlayer1" is the default name of the Windows Media Player control, and "c:\\mediafile.wmv" is a placeholder for the name of the media item you want to play. Any valid file path can be used. The @ symbol instructs the compiler to not interpret backslashes as escape characters.

If you have added the digital media content from the Windows Media Player SDK to the library in Windows Media Player, you can use this code instead:


```CSharp
axWindowsMediaPlayer1.currentPlaylist = axWindowsMediaPlayer1.mediaCollection.getByName("mediafile");

```



Because the **autoStart** property is true by default, Windows Media Player will start playing when you set the **currentPlaylist** or **URL** property.

## Add the Stop Code

Double-click the **Stop** button to reveal the Code window. In C#, the following code will be displayed:


```CSharp
private void button2_Click(object sender, System.EventArgs e)
{

}

```



Add this line between the two curly braces:


```CSharp
axWindowsMediaPlayer1.Ctlcontrols.stop();

```



> [!Note]  
> The managed-code wrapper for the Windows Media Player control exposes the **Controls** object as **Ctlcontrols** to avoid collision with the **Controls** property inherited from **System.Windows.Forms.Control**.

 

## Add Error-handling

The Windows Media Player control does not raise an exception when it encounters an error such as an invalid URL. Instead, it signals an event. Your application should handle error events sent by the Player.

To create an event handler, first open the Properties window for the Windows Media Player control. In the list of events, double-click **MediaError**. The following code is displayed:


```CSharp
private void Player_MediaError(object sender, _WMPOCXEvents_MediaErrorEvent e)
{
}

```



The following code could be inserted in the method to provide minimal error-handling capability. Note that information about the error can be retrieved from the **\_WMPOCXEvents\_MediaErrorEvent** argument.


```CSharp
try
// If the Player encounters a corrupt or missing file, 
// show the hexadecimal error code and URL.
{
    IWMPMedia2 errSource = e.pMediaObject as IWMPMedia2;
    IWMPErrorItem errorItem = errSource.Error;
    MessageBox.Show("Error " + errorItem.errorCode.ToString("X") 
                    + " in " + errSource.sourceURL);
}
catch(InvalidCastException)
// In case pMediaObject is not an IWMPMedia item.
{
    MessageBox.Show("Error.");
} 

```



## Related topics

<dl> <dt>

[**Embedding the Windows Media Player Control in a .NET Framework Solution**](using-the-windows-media-player-control-in-a--net-framework-solution.md)
</dt> </dl>

 

 




