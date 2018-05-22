---
title: Animation Control
description: This section contains information about the programming elements used with animation controls.
ms.assetid: '16994f93-e0fd-4c71-9c8a-15642408b8de'
---

# Animation Control

This section contains information about the programming elements used with animation controls.

### Overviews



| Topic                                                      | Contents                                                                                                                                                                                                                           |
|------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About Animation Controls](animation-control-overview.md) | An *animation control* is a window that displays an Audio-Video Interleaved (AVI) clip. An AVI clip is a series of bitmap frames like a movie. Animation controls can only display AVI clips that do not contain audio.<br/> |
| [Using Animation Controls](using-animation-control.md)    | This section gives implementation details and example code for animation controls.<br/>                                                                                                                                      |



 

### Macros



| Topic                                           | Contents                                                                                                                                                                                                                                                          |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Animate\_Close**](animate-close.md)         | Closes an AVI clip. You can use this macro or send the [**ACM\_OPEN**](acm-open.md) message explicitly, passing in **NULL** parameters. <br/>                                                                                                              |
| [**Animate\_Create**](animate-create.md)       | Creates an animation control. [**Animate\_Create**](animate-create.md) calls the [**CreateWindow**](https://msdn.microsoft.com/library/windows/desktop/ms632679) function to create the animation control. <br/>                                                                                   |
| [**Animate\_IsPlaying**](animate-isplaying.md) | Checks to see if an AVI clip is playing. You can use this macro or send an [**ACM\_ISPLAYING**](acm-isplaying.md) message.<br/>                                                                                                                            |
| [**Animate\_Open**](animate-open.md)           | Opens an AVI clip and displays its first frame in an animation control. You can use this macro or send the [**ACM\_OPEN**](acm-open.md) message explicitly. <br/>                                                                                          |
| [**Animate\_OpenEx**](animate-openex.md)       | Opens an AVI clip from a resource in a specified module and displays its first frame in an animation control. You can use this macro or send the [**ACM\_OPEN**](acm-open.md) message explicitly. <br/>                                                    |
| [**Animate\_Play**](animate-play.md)           | Plays an AVI clip in an animation control. The control plays the clip in the background while the thread continues executing. You can use this macro or send the [**ACM\_PLAY**](acm-play.md) message explicitly. <br/>                                    |
| [**Animate\_Seek**](animate-seek.md)           | Directs an animation control to display a particular frame of an AVI clip. The control displays the clip in the background while the thread continues executing. You can use this macro or send the [**ACM\_PLAY**](acm-play.md) message explicitly. <br/> |
| [**Animate\_Stop**](animate-stop.md)           | Stops playing an AVI clip in an animation control. You can use this macro or send the [**ACM\_STOP**](acm-stop.md) message explicitly. <br/>                                                                                                               |



 

### Messages



| Topic                                   | Contents                                                                                                                                                                                                                                   |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ACM\_ISPLAYING**](acm-isplaying.md) | Checks whether an AVI clip is playing. You can send this message explicitly or use the [**Animate\_IsPlaying**](animate-isplaying.md) macro.<br/>                                                                                   |
| [**ACM\_OPEN**](acm-open.md)           | Opens an AVI clip and displays its first frame in an animation control. You can send this message explicitly or use the [**Animate\_Open**](animate-open.md) or [**Animate\_OpenEx**](animate-openex.md) macro. <br/>              |
| [**ACM\_PLAY**](acm-play.md)           | Plays an AVI clip in an animation control. The control plays the clip in the background while the thread continues executing. You can send this message explicitly or by using the [**Animate\_Play**](animate-play.md) macro.<br/> |
| [**ACM\_STOP**](acm-stop.md)           | Stops playing an AVI clip in an animation control. You can send this message explicitly or by using the [**Animate\_Stop**](animate-stop.md) macro.<br/>                                                                            |



 

### Notifications



| Topic                           | Contents                                                                                                                                                                                                       |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ACN\_START**](acn-start.md) | Notifies an animation control's parent window that the associated AVI clip has started playing. This notification code is sent in the form of a [**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591) message. <br/>      |
| [**ACN\_STOP**](acn-stop.md)   | Notifies the parent window of an animation control that the associated AVI clip has stopped playing. This notification code is sent in the form of a [**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591) message. <br/> |



 

### Constants



| Topic                                                        | Contents                                                                      |
|--------------------------------------------------------------|-------------------------------------------------------------------------------|
| [**Animation Control Styles**](animation-control-styles.md) | This section lists the window styles used with animation controls.<br/> |



 

 

 





