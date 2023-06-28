---
title: Remoting the Windows Media Player Control
description: Remoting the Windows Media Player Control
ms.assetid: d543b2a0-a2cb-47e2-b50e-4513fc061b46
keywords:
- Windows Media Player,embedding ActiveX control
- Windows Media Player object model,embedding ActiveX control
- object model,embedding ActiveX control
- Windows Media Player Mobile,embedding ActiveX control
- Windows Media Player ActiveX control,embedding
- Windows Media Player Mobile ActiveX control,embedding
- ActiveX control,embedding
- Windows Media Player,remoting ActiveX control
- Windows Media Player object model,remoting ActiveX control
- object model,remoting ActiveX control
- Windows Media Player Mobile,remoting ActiveX control
- Windows Media Player ActiveX control,remoting
- Windows Media Player Mobile ActiveX control,remoting
- ActiveX control,remoting
- remoting Windows Media Player ActiveX control
- embedding,remoting ActiveX control
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Remoting the Windows Media Player Control

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When you embed the Windows Media Player control in a C++ program, you can use it as a remote extension of the full mode of the Player. This is called "remoting" the Windows Media Player control, and it lets you provide all the features of the full mode Player without implementing them yourself.

When you remote the control, it shares the same playback engine as the full mode of the Player and your users can switch back and forth between embedded mode (the "docked" state) and full mode (the "undocked" state) while digital media playback continues uninterrupted.

## Enabling Remote Embedding

To enable remote embedding of the Windows Media Player control, your program must implement the **IServiceProvider** and [IWMPRemoteMediaServices](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpremotemediaservices) interfaces. **IServiceProvider** is a standard Component Object Model (COM) interface with a single method called **QueryService**. Windows Media Player calls this method to retrieve a pointer to an **IWMPRemoteMediaServices** interface.

**IWMPRemoteMediaServices** has several methods, but only two of them are directly relevant to remoting. In [GetApplicationName](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpremotemediaservices-getapplicationname), you return the name of your program, which Windows Media Player adds to the **Switch to Other Program** list on the **View** menu. In [GetServiceType](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpremotemediaservices-getservicetype), you indicate the embedding mode of the control by returning a value of either "Remote" or "Local". If a remote connection is successfully established, the [get\_isRemote](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpplayer4-get_isremote) method of the [IWMPPlayer4](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplayer4) interface returns true.

## Specifying an Exclusive Online Store

With Windows Media Player 11, an application that embeds the Player control remotely can specify an exclusive online store. In that case, the service selector in Windows Media Player is disabled and only the specified online store is available to the user. For detailed information about how to specify an exclusive online store, see [Exclusive Online Stores](exclusive-online-stores.md).

## Docking and Undocking

The **IWMPPlayer4** interface also provides access to the [IWMPPlayerApplication](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplayerapplication) interface through the [get\_playerApplication](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpplayer4-get_playerapplication) method. Use **IWMPPlayerApplication** to switch between the docked and undocked states and to determine the current docked state and the location of the video or visualization display.

The [IWMPPlayerApplication::switchToPlayerApplication](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpplayerapplication-switchtoplayerapplication) method undocks the control by opening the full mode of Windows Media Player and transferring the video or visualization display to the **Now Playing** pane. The [IWMPPlayerApplication::switchToControl](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpplayerapplication-switchtocontrol) method docks the control by transferring the video or visualization display to your program and closing the full mode of the Player, if it is open. The control can also be docked by selecting a program from the **Switch to Other Program** list or by closing the full mode of the Player. In both cases, any digital media that is playing continues uninterrupted.

## Transferring the Video or Visualization Display

When several programs with embedded, remoted Windows Media Player controls run simultaneously, all of the controls share the same playback engine. They also share the same instance of the full mode of the Player in the undocked state. In the docked state, however, only one control can display the video or visualization. In the undocked state, only the full mode of the Player displays the video or visualization. The **switchToControl** method works in both the docked and undocked states and will transfer the video or visualization display to whichever program calls it.

The only difference between the docked and undocked states is the presence of the full mode of Windows Media Player and its ownership of the video or visualization display. In the undocked state, all embedded, remoted controls currently running are still visible and their user interfaces are still fully functional. If a video or visualization window is present, however, it is empty. In the docked state, only one of the embedded, remoted controls owns the display, but all user interfaces continue to function.

## Hiding or Changing the Control in the Undocked State

You must provide your own implementation if you want to hide or alter the user interface of an embedded control in the undocked state or when your program does not own the display. You can make these alterations when you dock and undock the control, or you can make them in response to Windows Media Player events. Because the Player can be docked through the **Switch to Other Program** menu option, however, it is usually better to provide this functionality in response to events.

You can implement event handlers for the [SwitchedToPlayerApplication](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpevents-switchedtoplayerapplication) and [SwitchedToControl](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpevents-switchedtocontrol) events, or you can implement a single event handler for the [PlayerDockedStateChange](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpevents-playerdockedstatechange) event. In the latter case, you can determine the docked state by calling [IWMPPlayerApplication::get\_playerDocked](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpplayerapplication-get_playerdocked). In both cases, use [IWMPPlayerApplication::get\_hasDisplay](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpplayerapplication-get_hasdisplay) to determine whether your program owns the video or visualization display.

## Re-establishing a Remote Connection

In certain circumstances, the connection between a remoted, embedded control and the standalone Player will fail, invalidating your pointers to the Windows Media Player interfaces. Windows Media Player will automatically attempt to reconnect, and will fire the [PlayerReconnect](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpevents-playerreconnect) event to signal this attempt. Although the reconnection is automatic, you must provide an event handler for this event if you want to release your invalid pointers and retrieve new ones so that you can access the standalone Player through the new connection.

## Controlling the Undocked Player

All remoted instances of the Windows Media Player control can manipulate the full mode of the Player regardless of the docked state. Features that have no relevance to the full mode of the Player, however, are ignored until the Windows Media Player control is docked. This includes properties of the [IWMPPlayer](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplayer) and derived interfaces, such as **enabled**, **enableContextMenu**, **uiMode**, and **windowlessVideo**.

## Error Dialog Boxes

From a remoted Windows Media Player control instance, the *Settings*.**enableErrorDialogs** property behaves in a specific manner. The following rules apply:

-   When Windows Media Player is undocked (the Windows Media Player UI is visible), the **enableErrorDialogs** property is ignored and error dialog boxes are handled by the Player.
-   When Windows Media Player is docked, the value specified by each remoted instance of the control for **enableErrorDialogs** applies only to the individual control instance. That is, if a particular control instance specifies a value of "true" for **enableErrorDialogs**, only that instance will display a dialog box when an error occurs if all other instances of the control have specified a value of "false".

## Remoting in the Background

You should avoid keeping a remoted instance of the Player running in the background during times when the control is not in use. Because the remoted Player control instance shares its playback engine with the full mode Player, keeping a background instance running can cause unexpected behavior. For example, the user might close the full mode Player while a file is playing. The user would expect that file playback would completely stop when the Player closes, but audio might continue to play because the playback engine is still active.

## Samples

The Windows Media Player SDK setup package installs samples that demonstrate remoting. See the RemoteSkin and WMPML samples for more information.

## Related topics

<dl> <dt>

[**Samples**](samples.md)
</dt> <dt>

[**Using the Windows Media Player Control in a C++ Program**](using-the-windows-media-player-control-in-a-c---program.md)
</dt> </dl>

 

 




