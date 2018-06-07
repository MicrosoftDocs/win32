---
title: Accessibility Structures
description: This section describes the structures used to implement Windows accessibility features.Microsoft Win32 accessibility features.
ms.assetid: 0ff480ae-18e3-413d-b208-a67fbae28c25
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Accessibility Structures

This section describes the structures used to implement Windows accessibility features.

## In this section



| Structure                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ACCESSTIMEOUT**](/windows/desktop/api/Winuser/ns-winuser-tagaccesstimeout)<br/> | Contains information about the time-out period associated with the Microsoft Win32 accessibility features. <br/> The accessibility time-out period is the length of time that must pass without keyboard and mouse input before the operating system automatically turns off accessibility features. The accessibility time-out is designed for computers that are shared by several users so that options selected by one user do not inconvenience a subsequent user.<br/> The accessibility features affected by the time-out are the FilterKeys features (SlowKeys, BounceKeys, and RepeatKeys), MouseKeys, ToggleKeys, and StickyKeys. The accessibility time-out also affects the high contrast mode setting.<br/> |
| [**FILTERKEYS**](/windows/desktop/api/Winuser/ns-winuser-tagfilterkeys)<br/>       | Contains information about the FilterKeys accessibility feature, which enables a user with disabilities to set the keyboard repeat rate (RepeatKeys), acceptance delay (SlowKeys), and bounce rate (BounceKeys). <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [**HIGHCONTRAST**](/windows/desktop/api/Winuser/ns-winuser-taghighcontrasta)<br/>   | Contains information about the high contrast accessibility feature.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**MOUSEKEYS**](/windows/desktop/api/Winuser/ns-winuser-tagmousekeys)<br/>         | Contains information about the MouseKeys accessibility feature. When the MouseKeys feature is active, the user can use the numeric keypad to control the mouse pointer, and to click, double-click, drag, and drop. By pressing NUMLOCK, the user can toggle the numeric keypad between mouse control mode and normal operation. <br/>                                                                                                                                                                                                                                                                                                                                                                                               |
| [**SERIALKEYS**](/windows/desktop/api/Winuser/ns-winuser-tagserialkeysa)<br/>       | Contains information about the SerialKeys accessibility feature, which interprets data from a communication aid attached to a serial port as commands causing the system to simulate keyboard and mouse input. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**SOUNDSENTRY**](/windows/desktop/api/Winuser/ns-winuser-tagsoundsentrya)<br/>     | Contains information about the SoundSentry accessibility feature. When the SoundSentry feature is on, the computer displays a visual indication only when a sound is generated.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**STICKYKEYS**](/windows/desktop/api/Winuser/ns-winuser-tagstickykeys)<br/>       | Contains information about the StickyKeys accessibility feature. When the StickyKeys feature is on, the user can press a modifier key (SHIFT, CTRL, or ALT) and then another key in sequence rather than at the same time, to enter shifted (modified) characters and other key combinations.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [**TOGGLEKEYS**](/windows/desktop/api/Winuser/ns-winuser-tagtogglekeys)<br/>       | Contains information about the ToggleKeys accessibility feature. When the ToggleKeys feature is on, the computer emits a high-pitched tone whenever the user turns on the CAPS LOCK, NUM LOCK, or SCROLL LOCK key, and a low-pitched tone whenever the user turns off one of those keys. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                       |



 

## Related topics

<dl> <dt>

[Windows Accessibility Features](windows-accessibility-features.md)
</dt> </dl>

 

 





