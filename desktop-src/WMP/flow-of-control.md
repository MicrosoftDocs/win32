---
title: Flow of Control
description: Flow of Control
ms.assetid: b91c0191-1908-4d62-96ce-927d09c70f9a
keywords:
- visualizations,program flow
- custom visualizations,program flow
- visualizations,flow of control
- custom visualizations,flow of control
- visualizations,timed events
- custom visualizations,timed events
- visualizations,Render function
- custom visualizations,Render function
- visualizations,RenderWindow function
- custom visualizations,RenderWindow function
- Render function,visualization program flow
- RenderWindow function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Flow of Control

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Audio data comes into Windows Media Player continuously through a file or a stream. That data is passed to your visualization. You draw on a defined surface and pass that surface back to Windows Media Player. This interchange happens several times a second, and to the user, the result is a pleasing animation that moves in time to the music.

Here is the specific sequence of the visualization program flow:

1.  At a timed interval, Windows Media Player takes a snapshot of the audio that is playing.
2.  Windows Media Player supplies the data from that snapshot to your visualization through the **Render** function and the **RenderWindowed** function.
3.  You must write code that will run when **Render** and **RenderWindowed** is called. Your code draws by using a device context defined by Windows Media Player when rendering windowless, or by using a window that you create when rendering windowed.
4.  In a region specified by the current skin, Windows Media Player displays what your code drew.
5.  This process repeats several times a second, creating graphical animations that are timed to the music. When the music stops playing, the visualization stops.

## Related topics

<dl> <dt>

[**Developer Overview**](developer-overview.md)
</dt> </dl>

 

 




