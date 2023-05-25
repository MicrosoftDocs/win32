---
title: Using the Windows Media Player Control with Microsoft Office
description: Using the Windows Media Player Control with Microsoft Office
ms.assetid: bc7b2623-8e6d-4af6-b4d0-8087c0159273
keywords:
- Windows Media Player,embedding ActiveX control
- Windows Media Player object model,embedding ActiveX control
- object model,embedding ActiveX control
- Windows Media Player Mobile,embedding ActiveX control
- Windows Media Player ActiveX control,embedding
- Windows Media Player Mobile ActiveX control,embedding
- ActiveX control,embedding
- Windows Media Player,Office
- Windows Media Player object model,Office
- object model,Office
- Windows Media Player Mobile,Office
- Windows Media Player ActiveX control,Office
- Windows Media Player Mobile ActiveX control,Office
- ActiveX control,Office
- Office document embedding
- embedding,Office documents
- Windows Media Player ActiveX control,Excel
- Windows Media Player Mobile ActiveX control,Excel
- ActiveX control,Excel
- embedding,Excel spreadsheets
- Excel spreadsheet embedding
- Windows Media Player ActiveX control,PowerPoint
- Windows Media Player Mobile ActiveX control,PowerPoint
- ActiveX control,PowerPoint
- embedding,PowerPoint slide shows
- PowerPoint slide show embedding
- Windows Media Player ActiveX control,Word
- Windows Media Player Mobile ActiveX control,Word
- ActiveX control,Word
- Word document embedding
- embedding,Word documents
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using the Windows Media Player Control with Microsoft Office

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes how to embed the Windows Media Player 9 Series or later ActiveX control in various documents created using Microsoft Office XP.

In Microsoft Word, Excel, and PowerPoint®, you embed the control by selecting **Object** from the **Insert** menu, then choosing **Windows Media Player** from the list of available object types. The Windows Media Player control appears in the document at the current location. You can then select **Format Control** ( **Format Object** in Excel) from the shortcut menu for the control to adjust the layout, text wrapping style, and other format options. In Word and Excel, you must be in design mode to do this.

Once you have positioned and formatted the control, you can configure it using the **Properties** dialog box, which is accessible from the **Control Toolbox** or from the shortcut menu in design mode for Word and Excel. Here you can specify basic Player control properties such as the control name, the URL of a digital media file, and the user interface mode. Setting the **uiMode** property to "none" hides everything in the control except the video or visualization window, allowing you to add your own buttons and write script code using Visual Basic for Applications (VBA) to handle the button clicks and Player control events.

From the basic **Properties** dialog box, you can also access the more sophisticated **Windows Media Player Control Properties** dialog box by double-clicking the "(Custom)" row or by clicking the ellipsis ("...") button after selecting that row. From this dialog box, you can modify all available Player control properties.

> [!Note]  
> You must be careful not to take actions in Player control event handlers that will result in the control being destroyed. For example, if you embed the Windows Media Player control on a slide in a PowerPoint presentation, do not call the PowerPoint **Next** method from the Player **openStateChange** event or any other event.

 

> [!Note]  
> In addition, you should not set the **Player.URL** property from a Player control event handler.

 

In FrontPage, add the Windows Media Player control to a webpage by selecting **Web Component** from the **Insert** menu. In the **Insert Web Component** dialog box, select **Advanced Controls** from the **Component type** list, then select **ActiveX Control** from the list of control choices. In the next window of the dialog box, select **Windows Media Player**. If it is not listed, click **Customize** and select the **Windows Media Player** check box in the **Control** list.

After the Windows Media Player control is embedded, you can position and resize it, and modify its properties by selecting **ActiveX Control Properties** from the shortcut menu for the control. In the HTML view, the property values that you specify appear in the OBJECT element representing the Windows Media Player control. The object name appears as the ID attribute, and the control properties appear as PARAM tags. The object name gives you access to the Windows Media Player control object model, which you can program using Microsoft JScript. For more information, see [Using the Windows Media Player Control in a Web Page](using-the-windows-media-player-control-in-a-web-page.md).

## Related topics

<dl> <dt>

[**Player Control Guide**](player-control-guide.md)
</dt> </dl>

 

 




