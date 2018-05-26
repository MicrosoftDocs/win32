---
Description: Applications can better adapt their behavior to the current power state of the computer by registering for power events.
ms.assetid: 840390ca-d32a-4cf3-9e75-66322c7cdee0
title: Registering for Power Events
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Registering for Power Events

Applications can better adapt their behavior to the current power state of the computer by registering for power events. An application should register for each power change event that might impact its behavior.

An application or service uses the [**RegisterPowerSettingNotification**](/windows/win32/WinUser/nf-winuser-registerpowersettingnotification?branch=master) function to register for notifications. When the corresponding power setting changes, the system sends notifications as follows:

-   An application receives a [**WM\_POWERBROADCAST**](wm-powerbroadcast.md) message with a *wParam* of [PBT\_POWERSETTINGCHANGE](pbt-powersettingchange.md) and an *lParam* that points to a [**POWERBROADCAST\_SETTING**](/windows/win32/WinUser/ns-winuser-powerbroadcast_setting?branch=master) structure.
-   A service receives a call to the [*HandlerEx*](https://msdn.microsoft.com/library/windows/desktop/ms683241) callback function it registered by calling the [**RegisterServiceCtrlHandlerEx**](https://msdn.microsoft.com/library/windows/desktop/ms685058) function. The *lpEventData* parameter sent to the *HandlerEx* callback function points to a [**POWERBROADCAST\_SETTING**](/windows/win32/WinUser/ns-winuser-powerbroadcast_setting?branch=master) structure.

In the [**POWERBROADCAST\_SETTING**](/windows/win32/WinUser/ns-winuser-powerbroadcast_setting?branch=master) structure, the **PowerSetting** member contains the GUID that identifies the notification and the **Data** member contains the new value of the power setting.

For a list of power setting GUIDs for notifications that are most useful to applications, see [**Power Setting GUIDs**](power-setting-guids.md).

 

 



