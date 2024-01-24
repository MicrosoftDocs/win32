---
title: Using the Windows Media Player Control with Visual Basic
description: Using the Windows Media Player Control with Visual Basic
ms.assetid: 83e5440b-096b-42e1-9038-d779895d9519
keywords:
- Windows Media Player,embedding ActiveX control
- Windows Media Player object model,embedding ActiveX control
- object model,embedding ActiveX control
- Windows Media Player Mobile,embedding ActiveX control
- Windows Media Player ActiveX control,embedding
- Windows Media Player Mobile ActiveX control,embedding
- ActiveX control,embedding
- Windows Media Player,Visual Basic
- Windows Media Player object model,Visual Basic
- object model,Visual Basic
- Windows Media Player Mobile,Visual Basic
- Windows Media Player ActiveX control,Visual Basic
- Windows Media Player Mobile ActiveX control,Visual Basic
- ActiveX control,Visual Basic
- Visual Basic-based program embedding
- embedding,Visual Basic-based programs
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using the Windows Media Player Control with Visual Basic

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes how to use the Windows Media Player 9 Series or later ActiveX control in applications created with Microsoft Visual Basic 6.0.

## Getting Started

To add the Windows Media Player control to the toolbox, first select **Components** from the **Project** menu. In the Components dialog box, select the check box next to "Windows Media Player". At the bottom of the dialog box, confirm that the selected file is wmp.dll. After closing the dialog box, you can place an instance of the Windows Media Player control on your form in the usual ways.

You can set many control properties using the Properties window. To set some properties you must use the Windows Media Player Properties dialog box, which you open using the "(Custom)" item in the Properties window.

## Object References

You use certain Player control properties to get references to particular objects. For example, the **cdromCollection** property returns a reference to a **CdromCollection** object. You must assign such a reference to a variable that you declared as the corresponding interface. In the case of the **cdromCollection** property, for example, you assign its return value to a variable of type **IWMPCdromCollection**.

Read the [Interfaces](interfaces.md) topic in the [Object Model Reference for C++](object-model-reference-for-c.md) to identify which objects implement multiple interfaces. In those cases, you must declare an object variable as the highest-numbered interface documented in this SDK to have access to all of the properties and methods of that object. For example, you should assign the value of the Windows Media Player control **currentMedia** property to a variable declared as **IWMPMedia3** to assure that you have access to the **getAttributeCountByType** and **getItemInfoByType** methods.

> [!Note]  
> The **WindowsMediaPlayer** object implements all of the properties and methods of the **IWMPCore**, **IWMPCore2**, **IWMPCore3**, **IWMPPlayer**, **IWMPPlayer2**, **IWMPPlayer3**, and **IWMPPlayer4** interfaces. You do not need to declare separate variables for any of these interfaces. You can access all of their members using the name you assigned to your **WindowsMediaPlayer** instance.

 

In the Visual Basic Object Browser you will see many interfaces that are intended for private use by the Windows Media Player control, including some that support skin developers. You should use only the objects, properties, methods, and events that are documented in this SDK.

## Additional Tips

-   The reference documentation shows JScript syntax. In JScript, arguments passed to methods are always enclosed in parentheses. In Visual Basic 6.0, arguments passed to methods that do not return a value must not be enclosed in parentheses.
-   Some properties or methods may not appear in the Auto List code-completion feature in the Visual Basic code editor. You can still use those members by typing their names exactly as they appear in this documentation.
-   Manage the visual appearance of the control using the **uimode** property. You can do so in two ways. You can use the **Select a mode** drop-down list in the Windows Media Player Properties dialog box, or you can type the correct value in the Properties window.

    In particular, do not use the **visible** property to hide the control; instead, assign the value "invisible" to the **uimode** property.

## Related topics

<dl> <dt>

[**Player Control Guide**](player-control-guide.md)
</dt> </dl>

 

 




