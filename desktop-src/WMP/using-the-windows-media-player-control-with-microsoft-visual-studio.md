---
title: Using the Windows Media Player Control with Microsoft Visual Studio
description: Using the Windows Media Player Control with Microsoft Visual Studio
ms.assetid: e007876e-f215-4976-8a70-018fedc0e67d
keywords:
- Windows Media Player,embedding ActiveX control
- Windows Media Player object model,embedding ActiveX control
- object model,embedding ActiveX control
- Windows Media Player Mobile,embedding ActiveX control
- Windows Media Player ActiveX control,embedding
- Windows Media Player Mobile ActiveX control,embedding
- ActiveX control,embedding
- Windows Media Player,.NET Framework
- Windows Media Player object model,.NET Framework
- object model,.NET Framework
- Windows Media Player Mobile,.NET Framework
- Windows Media Player ActiveX control,.NET Framework
- Windows Media Player Mobile ActiveX control,.NET Framework
- ActiveX control,.NET Framework
- Windows Media Player ActiveX control,Visual Studio
- Windows Media Player Mobile ActiveX control,Visual Studio
- ActiveX control,Visual Studio
- .NET Framework,Visual Studio program embedding
- embedding,Visual Studio programs
- Visual Studio,program embedding
ms.topic: article
ms.date: 05/31/2018
---

# Using the Windows Media Player Control with Microsoft Visual Studio

You can add the Windows Media Player 9 Series or later ActiveX control to a .NET Framework application through the Toolbox in Visual Studio.

## Adding the Windows Media Player Control

Before creating a new project, make sure that the latest version of Windows Media Player and the Windows Media Player SDK is installed on your computer.

Start Visual Studio, then create a new project.

In Visual Studio, open the Toolbox.

If Windows Media Player does not appear in the **Components** portion of the Toolbox, do the following:

1.  Right-click within the Toolbox, and then select **Choose Items**. This opens the **Customize Toolbox** dialog box.
2.  On the **COM Components** tab, select Windows Media Player.

    If Windows Media Player does not appear in the list, click **Browse**, and then open Wmp.dll, which should be in the Windows\\System32 folder.

3.  Click **OK**. The Windows Media Player control will be placed on the current Toolbox tab.

You can now select Windows Media Player in the Toolbox and add it to a form.

Visual Studio gives the Windows Media Player control a default name such as "axWindowsMediaPlayer1". You may want to change the name to something more easily remembered, such as "Player".

Adding the Windows Media Player control from the Toolbox also adds references to two libraries created by Visual Studio, AxWMPLib and WMPLib. You can find them in the Solution Explorer under **References**.

To make using the objects in the Player namespace easier, you should include the namespace in the using or imports directives of your files, as follows:


```Csharp
using WMPLib;
```




```VB
imports WMPLib

```



The directive ensures that you can refer to **Player** objects without fully qualifying their names.

> [!Note]  
> The Windows Media Player control is an **AxWindowsMediaPlayer** object from the **AxWMPLib** namespace. However, the **AxWindowsMediaPlayer** class uses data types, interfaces, and other elements from the **WMPLib** namespace.

 

## Configuring Visibility of the Control

When you first add the Windows Media Player control to a form, it will be visible. If you do not want to use the visible image of the Player in your application, hide the default Player by setting any one of the following properties:



| Property        | Value                                                 |
|-----------------|-------------------------------------------------------|
| **uiMode**      | "invisible" (See [Player.uiMode](player-uimode.md).) |
| **Visible**     | "false"                                               |
| **Size.Width**  | 0                                                     |
| **Size.Height** | 0                                                     |



 

You can set these properties either in code or in the **Properties** window when the Windows Media Player control is selected in the form designer.

## Object Model Compatibility of the Control

The object model for the Windows Media Player control is basically the same in the .NET Framework as in unmanaged code and script. However, there are differences in how elements are exposed:

-   Most objects are exposed under the name of their underlying COM interface. For example, the **Playlist** object is exposed as **IWMPPlaylist**.
-   Some interfaces have later versions. For example, **IWMPMedia** was given additional functionality in **IWMPMedia2** and **IWMPMedia3**. If you declare an object as **IWMPMedia**, you usually have access to the functionality of all versions of the interface. However, IntelliSense® will not recognize the methods or properties of the later-version interfaces, and the Visual Basic .NET editor will not automatically correct capitalization. To get the full benefit of IntelliSense and other features of Visual Studio, declare the object by using the latest version of the interface, such as **IWMPMedia3**.
-   There are no indexed properties (C#) or default properties (Visual Basic .NET). For example, to retrieve a **Playlist.item**, you must call the **IWMPlaylist.get\_Item** accessor method in C# or retrieve the **IWMPlayist.Item** property in Visual Basic .NET.
-   Because of a naming conflict between the Windows Media Player **Controls** property and the **Controls** property exposed by every control, the Player version of this property is called **CtlControls** in the context of the ActiveX control. (However, this is not the case when you create the Player programmatically rather than as an ActiveX control.)

Use the Object Browser in Visual Studio to locate the correct API names for methods and objects in the **AxWMPLib** and **WMPLib** namespaces.

## Distributing Your Application

When you distribute your application, be sure to install AxInterop.WMPLib.dll and Interop.WMPLib.dll in the application folder. You will also need to make sure that the required Windows Media Player version is installed on the user's computer.

## Related topics

<dl> <dt>

[**Creating the Windows Media Player Control Programmatically**](creating-the-windows-media-player-control-programmatically.md)
</dt> <dt>

[**Embedding the Windows Media Player Control in a C# Solution**](embedding-the-windows-media-player-control-in-a-c--solution.md)
</dt> <dt>

[**Embedding the Windows Media Player Control in a Visual Basic .NET Solution**](embedding-the-windows-media-player-control-in-a-visual-basic--net-solution.md)
</dt> </dl>

 

 




