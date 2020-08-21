---
title: Accessibility parameters
description: The system maintains a set of accessibility parameters that indicate whether the user has special needs or preferences that require applications to change their default behavior.
ms.assetid: efa289bb-5965-4002-93df-116ab2621efc
ms.topic: article
ms.date: 05/31/2018
---

# Accessibility parameters

The system maintains a set of accessibility parameters that indicate whether the user has special needs or preferences that require applications to change their default behavior. The user controls the state of these parameters, typically using the Ease of Access Center in Control Panel. Control Panel applications or other programs that allow the user to customize the environment can use the [**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa) function to set the accessibility parameters.

If a user changes these parameters, the Control Panel sends the [**WM\_SETTINGCHANGE**](/windows/desktop/winmsg/wm-settingchange) message. Applications should respond to this message and use [**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa) to determine the state of the accessibility parameters. When an accessibility parameter is enabled, the application should modify its user interface, if necessary, to accommodate the user's preferences.

Windows supports the following accessibility parameters.



| Parameter                                                                    | Description                                                                                                                                                                    |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [High contrast](high-contrast-parameter.md)                                 | Indicates that applications should provide high contrast between foreground and background visuals.                                                                            |
| [Keyboard preference](keyboard-preference-parameter.md)                     | Indicates that applications should display keyboard interfaces that would otherwise be hidden.                                                                                 |
| [Screen reader](screen-reader-parameter.md)                                 | Indicates that applications should provide textual information in situations where it would otherwise present the information graphically.                                     |
| [Show sounds (and audio description flag)](showsounds-parameter.md) | Indicates that applications should also provide a visual alert or cue when it uses sound to convey important information, or provide an audio description for visual elements. |
| [Client area animation](client-area-animation.md)                           | Indicates that applications should respect user preferences for displaying animation in the client area.                                                                       |
| [Message duration](message-duration.md)                                     | Indicates that applications that provide pop up notifications must monitor flags about message duration and adjust their notification length.                                  |



 

The following system parameters are useful for accessibility applications. For more information, see [**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa) function.



| Parameter group      | Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Desktop parameters   | SPI\_GETWORKAREA, SPI\_SETWORKAREA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Input parameters     | SPI\_GETKEYBOARDCUES, SPI\_GETKEYBOARDDELAY, SPI\_GETKEYBOARDPREF, SPI\_GETKEYBOARDSPEED, SPI\_GETMESSAGEDURATION, SPI\_GETMOUSE, SPI\_GETMOUSEHOVERHEIGHT, SPI\_GETMOUSEHOVERTIME, SPI\_GETMOUSEHOVERWIDTH, SPI\_GETMOUSESPEED, SPI\_GETMOUSETRAILS, SPI\_GETSNAPTODEFBUTTON, SPI\_GETWHEELSCROLLLINES, SPI\_SETDOUBLECLICKTIME, SPI\_SETDOUBLECLKHEIGHT, SPI\_SETDOUBLECLKWIDTH, SPI\_SETKEYBOARDCUES, SPI\_SETKEYBOARDDELAY, SPI\_SETKEYBOARDPREF, SPI\_SETKEYBOARDSPEED, SPI\_SETMOUSE, SPI\_SETMOUSEHOVERHEIGHT, SPI\_SETMOUSEHOVERTIME, SPI\_SETMOUSEHOVERWIDTH, SPI\_SETMOUSESPEED, SPI\_SETMOUSETRAILS, SPI\_SETSNAPTODEFBUTTON, SPI\_SETWHEELSCROLLLINES |
| UI effect parameters | SPI\_GETMENUUNDERLINES, SPI\_SETMENUUNDERLINES                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Window parameters    | SPI\_GETCARETWIDTH, SPI\_GETFOREGROUNDFLASHCOUNT, SPI\_GETFOREGROUNDLOCKTIMEOUT, SPI\_SETCARETWIDTH, SPI\_SETDRAGHEIGHT, SPI\_SETDRAGWIDTH, SPI\_SETFOREGROUNDFLASHCOUNT, SPI\_SETFOREGROUNDLOCKTIMEOUT                                                                                                                                                                                                                                                                                                                                                                                                                                                           |



 

## Related topics

<dl> <dt>

[About Windows accessibility features](about-windows-accessibility-features.md)
</dt> </dl>

 

 