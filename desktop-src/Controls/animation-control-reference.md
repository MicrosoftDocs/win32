---
title: Animation Control
description: This section contains information about the programming elements used with animation controls.
ms.assetid: 16994f93-e0fd-4c71-9c8a-15642408b8de
ms.topic: article
ms.date: 05/31/2018
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
| [**Animate\_Close**](/windows/desktop/api/Commctrl/nf-commctrl-animate_close)         | Closes an AVI clip. You can use this macro or send the [**ACM\_OPEN**](acm-open.md) message explicitly, passing in **NULL** parameters. <br/>                                                                                                              |
| [**Animate\_Create**](/windows/desktop/api/Commctrl/nf-commctrl-animate_create)       | Creates an animation control. [**Animate\_Create**](/windows/desktop/api/Commctrl/nf-commctrl-animate_create) calls the [**CreateWindow**](/windows/desktop/api/winuser/nf-winuser-createwindowa) function to create the animation control. <br/>                                                                                   |
| [**Animate\_IsPlaying**](/windows/desktop/api/Commctrl/nf-commctrl-animate_isplaying) | Checks to see if an AVI clip is playing. You can use this macro or send an [**ACM\_ISPLAYING**](acm-isplaying.md) message.<br/>                                                                                                                            |
| [**Animate\_Open**](/windows/desktop/api/Commctrl/nf-commctrl-animate_open)           | Opens an AVI clip and displays its first frame in an animation control. You can use this macro or send the [**ACM\_OPEN**](acm-open.md) message explicitly. <br/>                                                                                          |
| [**Animate\_OpenEx**](/windows/desktop/api/Commctrl/nf-commctrl-animate_openex)       | Opens an AVI clip from a resource in a specified module and displays its first frame in an animation control. You can use this macro or send the [**ACM\_OPEN**](acm-open.md) message explicitly. <br/>                                                    |
| [**Animate\_Play**](/windows/desktop/api/Commctrl/nf-commctrl-animate_play)           | Plays an AVI clip in an animation control. The control plays the clip in the background while the thread continues executing. You can use this macro or send the [**ACM\_PLAY**](acm-play.md) message explicitly. <br/>                                    |
| [**Animate\_Seek**](/windows/desktop/api/Commctrl/nf-commctrl-animate_seek)           | Directs an animation control to display a particular frame of an AVI clip. The control displays the clip in the background while the thread continues executing. You can use this macro or send the [**ACM\_PLAY**](acm-play.md) message explicitly. <br/> |
| [**Animate\_Stop**](/windows/desktop/api/Commctrl/nf-commctrl-animate_stop)           | Stops playing an AVI clip in an animation control. You can use this macro or send the [**ACM\_STOP**](acm-stop.md) message explicitly. <br/>                                                                                                               |



 

### Messages



| Topic                                   | Contents                                                                                                                                                                                                                                   |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ACM\_ISPLAYING**](acm-isplaying.md) | Checks whether an AVI clip is playing. You can send this message explicitly or use the [**Animate\_IsPlaying**](/windows/desktop/api/Commctrl/nf-commctrl-animate_isplaying) macro.<br/>                                                                                   |
| [**ACM\_OPEN**](acm-open.md)           | Opens an AVI clip and displays its first frame in an animation control. You can send this message explicitly or use the [**Animate\_Open**](/windows/desktop/api/Commctrl/nf-commctrl-animate_open) or [**Animate\_OpenEx**](/windows/desktop/api/Commctrl/nf-commctrl-animate_openex) macro. <br/>              |
| [**ACM\_PLAY**](acm-play.md)           | Plays an AVI clip in an animation control. The control plays the clip in the background while the thread continues executing. You can send this message explicitly or by using the [**Animate\_Play**](/windows/desktop/api/Commctrl/nf-commctrl-animate_play) macro.<br/> |
| [**ACM\_STOP**](acm-stop.md)           | Stops playing an AVI clip in an animation control. You can send this message explicitly or by using the [**Animate\_Stop**](/windows/desktop/api/Commctrl/nf-commctrl-animate_stop) macro.<br/>                                                                            |



 

### Notifications



| Topic                           | Contents                                                                                                                                                                                                       |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ACN\_START**](acn-start.md) | Notifies an animation control's parent window that the associated AVI clip has started playing. This notification code is sent in the form of a [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message. <br/>      |
| [**ACN\_STOP**](acn-stop.md)   | Notifies the parent window of an animation control that the associated AVI clip has stopped playing. This notification code is sent in the form of a [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message. <br/> |



 

### Constants



| Topic                                                        | Contents                                                                      |
|--------------------------------------------------------------|-------------------------------------------------------------------------------|
| [**Animation Control Styles**](animation-control-styles.md) | This section lists the window styles used with animation controls.<br/> |



 

 

