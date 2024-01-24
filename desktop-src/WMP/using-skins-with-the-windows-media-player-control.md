---
title: Using Skins with the Windows Media Player Control
description: Using Skins with the Windows Media Player Control
ms.assetid: 0381e0e4-c686-4ab4-b947-b883b6f4e06e
keywords:
- Windows Media Player,embedding ActiveX control
- Windows Media Player object model,embedding ActiveX control
- object model,embedding ActiveX control
- Windows Media Player Mobile,embedding ActiveX control
- Windows Media Player ActiveX control,embedding
- Windows Media Player Mobile ActiveX control,embedding
- ActiveX control,embedding
- Windows Media Player,C++
- Windows Media Player object model,C++
- object model,C++
- Windows Media Player Mobile,C++
- Windows Media Player ActiveX control,C++
- Windows Media Player Mobile ActiveX control,C++
- ActiveX control,C++
- C++ program embedding
- embedding,C++ programs
- Windows Media Player ActiveX control,skins
- Windows Media Player Mobile ActiveX control,skins
- ActiveX control,skins
- skins,embedding ActiveX control
- Windows Media Player skins,embedding ActiveX control
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using Skins with the Windows Media Player Control

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When you embed the Windows Media Player control in a C++ program, you can customize the Player user interface (UI) by applying a skin definition file to it. A skin definition file is an XML-based document specifying the layout of standard and customizable UI components and any accompanying graphics. Using Microsoft JScript, you can specify the behavior of these components and manipulate the Windows Media Player control without the overhead of C++ and COM syntax.

Skins provide an easy way to keep your user interface code and your main program code separate so that they can be maintained and developed independently. You can also reuse skins originally designed for use by the standalone Player in skin mode. Skin code that you design specifically for C++ programs can interact with your programs through a scriptable object that your program can provide.

To enable skin mode for the Windows Media Player control, your program must implement the **IWMPRemoteMediaServices** interface. Although you can use skins with the control and remote the control at the same time, you can use this interface to enable either feature without enabling the other. To disable remoting, simply pass a value of "Local" as the out parameter of the **GetServiceType** method, and return an HRESULT of E\_NOTIMPL from the **GetApplicationName** method.

To switch the Windows Media Player control to skin mode, call the **IWMPPlayer::put\_uiMode** method, passing in a value of "custom". Specify the path and file name of the skin definition file to use by returning it from the **IWMPRemoteMediaServices::GetCustomUIMode** method.

If you want to provide a scriptable object for communication between your skin and your program, pass a name and a pointer to an **IDispatch** pointer as the two out parameters of the **IWMPRemoteMediaServices::GetScriptableObject** method. Your skin can then make calls to the scriptable object by using the name specified as though it were a global attribute similar to the **player** global attribute.

A skin applied to a remoted Windows Media Player control can access the **PlayerApplication** object using another global attribute called **playerApplication**. Because the **Player.playerApplication** property cannot be accessed by skins, you must use this global attribute when you want your skin code to manage docking and undocking.

## Samples

The Windows Media Player SDK setup package installs a sample that demonstrates applying a skin to the Windows Media Player control. See the RemoteSkin sample for more information.

## Related topics

<dl> <dt>

[**Samples**](samples.md)
</dt> <dt>

[**Using the Windows Media Player Control in a C++ Program**](using-the-windows-media-player-control-in-a-c---program.md)
</dt> </dl>

 

 




