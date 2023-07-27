---
description: MSWebDVD Events
ms.assetid: e43ea4ad-8ebe-4096-a9f3-a8f618b46877
title: MSWebDVD Events
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MSWebDVD Events

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

> [!Note]  
> This API is deprecated. For information about DVD playback and navigation in DirectShow, see [DVD Applications](dvd-applications.md).

 

The MSWebDVD Microsoft® ActiveX® control notifies your application when various types of internal events occur or when certain information is encountered on the disc.

Most of the events relate to user operation (UOP) controls. DVD authors can encode the disc so that any DVD command (such as **PlayForwards**, **Pause**, **ShowMenu**, and so on) can be disabled at any time. For example, most discs will not allow users to fast forward or show a menu while the FBI warning is playing. After the warning is over, the disc permits these operations. By handling the UOP events, your application can update its user interface to show the user which commands are currently permitted by the disc. The most common way to do this is by disabling a button. For example, if your application received a PlayForwards event with **bEnabled** set to **FALSE**, you could disable the Play button. When it received that event with **bEnabled** set to **TRUE**, you could enable the button again.

There are three events that do not relate to UOP controls. The **DVDNotify** event notifies your application of many different types of DVD-related events, which are identified in the *EventCode* parameter. Some events have additional information in the *Param1* and *Param2* parameters. The **ReadyStateChange** event notifies your application of changes in the MSWebDVD ReadyState property, which is a property common to all ActiveX controls. The **UpdateOverlay** event is sent to applications only if they are hosting MSWebDVD in windowless mode. Applications need to respond to this event only if they are displaying floating buttons over the video rectangle in full screen mode.



| Event                                                                  | Description                                                                           |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [**ChangeCurrentAngle**](changecurrentangle.md)                       | Sent when the disc enables or disables changing the angle.                            |
| [**ChangeCurrentAudioStream**](changecurrentaudiostream.md)           | Sent when the disc enables or disables changing the audio stream.                     |
| [**ChangeCurrentSubpictureStream**](changecurrentsubpicturestream.md) | Sent when the **ChangeCurrentSubpictureStream** command has been enabled or disabled. |
| [**DVDNotify**](dvdnotify.md)                                         | Notifies an application of many different DVD events and disc instructions.           |
| [**PauseOn**](pauseon.md)                                             | Sent when the **Pause** command has been enabled or disabled.                         |
| [**PlayAtTime**](playattime.md)                                       | Sent when the **PlayAtTime** command has been enabled or disabled.                    |
| [**PlayAtTimeInTitle**](playattimeintitle.md)                         | Sent when the **PlayAtTimeInTitle** command has been enabled or disabled.             |
| [**PlayBackwards**](playbackwards.md)                                 | Sent when the **PlayBackwards** command has been enabled or disabled.                 |
| [**PlayChapter**](playchapter.md)                                     | Sent when the **PlayChapter** command has been enabled or disabled.                   |
| [**PlayChapterInTitle**](playchapterintitle.md)                       | Sent when the **PlayChapterInTitle** command has been enabled or disabled.            |
| [**PlayForwards**](playforwards.md)                                   | Sent when the **PlayForwards** command has been enabled or disabled.                  |
| [**PlayNextChapter**](playnextchapter.md)                             | Sent when the **PlayNextChapter** command has been enabled or disabled.               |
| [**PlayPrevChapter**](playprevchapter.md)                             | Sent when the **PlayPrevChapter** command has been enabled or disabled.               |
| [**PlayTitle**](playtitle.md)                                         | Sent when the **PlayTitle** command has been enabled or disabled.                     |
| [**ReadyStateChange**](readystatechange.md)                           | Sent when the **ReadyState** property of the MSWebDVD control has changed.            |
| [**ReplayChapter**](replaychapter.md)                                 | Sent when the **ReplayChapter** command has been enabled or disabled.                 |
| [**Resume**](resume.md)                                               | Sent when the **Resume** command has been enabled or disabled.                        |
| [**ReturnFromSubmenu**](returnfromsubmenu.md)                         | Sent when the **ReturnFromSubmenu** command has been enabled or disabled.             |
| [**SelectOrActivatButton**](selectoractivatbutton.md)                 | Sent when the disc enables or disables the selection or activation of menu buttons.   |
| [**ShowMenu**](showmenu.md)                                           | Sent when the disc enables or disables the showing of a menu.                         |
| [**StillOff**](stilloff.md)                                           | Sent when the **StillOff** command has been enabled or disabled.                      |
| [**Stop**](stop.md)                                                   | Sent when the **Stop** command has been enabled or disabled.                          |
| [**UpdateOverlay**](updateoverlay.md)                                 | Sent when the overlay surface has been moved or resized or its color key has changed. |



 

## Related topics

<dl> <dt>

[MSWebDVD Object](mswebdvd-object.md)
</dt> </dl>

 

 



