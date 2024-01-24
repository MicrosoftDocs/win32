---
description: A system power management event is a change in the system power status, the operational mode of a device or the system, or the value of a power setting.
ms.assetid: f73b072a-1f69-4e26-9712-dab428edca18
title: System Power Management Events
ms.topic: article
ms.date: 05/31/2018
---

# System Power Management Events

A system power management event is a change in the system power status, the operational mode of a device or the system, or the value of a power setting. Because these events can affect the operation of applications and installable drivers, the system notifies all applications and installable drivers by broadcasting a notification for each event. Applications and services register for notifications by using the [**RegisterPowerSettingNotification**](/windows/desktop/api/WinUser/nf-winuser-registerpowersettingnotification) function. Notifications are received via the [**WM\_POWERBROADCAST**](wm-powerbroadcast.md) message, which contains the power management event and any associated event-specific data.

## System Power Status Events

A *system power status event* occurs when there is a change in the power supply or in the system battery status. For example, the system broadcasts a [PBT\_APMPOWERSTATUSCHANGE](pbt-apmpowerstatuschange.md) event whenever the user switches from battery to AC power or vice versa. The system also broadcasts this event when remaining battery power slips below the threshold specified by the user or if the battery power changes by a specified percentage.

## Operational Mode Events

An *operational mode event* occurs when there is a change in power consumption, such as the system switching to a sleep state due to inactivity or the user manually putting the system to sleep. The system broadcasts events about these changes before the change in power consumption is made. For example, if the system determines that it is idle, it broadcasts a [PBT\_APMSUSPEND](pbt-apmsuspend.md) event that notifies applications and drivers that it is about to suspend operation and sleep to conserve power. Applications and drivers can prepare for sleep by closing files and saving data to avoid potential data loss.

When the system carries out a *critical suspension*, the system is immediately put to sleep due to a critical condition such as a critical battery alarm. In contrast to a normal sleep transition, the system does not notify applications and drivers before carrying out a critical suspension. Therefore, applications must be prepared to handle critical suspensions.

When system operation is restored after having been suspended, the system notifies all applications and drivers. It also indicates whether the system is resuming from a critical suspension so the application or driver can take appropriate steps to restore its data and continue operation.

Applications should make every attempt to handle the transition to the sleep state without any user intervention because it may not be possible for the user to respond. For example, the lid on the notebook computer may be closed. When an application receives notification that the system is about to enter sleep, it should perform any necessary operations quickly and return out of the message loop. The system allows for a maximum of two seconds per application when handling this message before timing out.

## Power Setting Change Events

A power setting change event occurs when there is a change in the value of a power setting. For example, the user changes the power plan from High Performance to Balanced in the Power Options application in Control Panel. In this case, the system would broadcast an event that indicates that the power plan has changed. This event includes the new value for the power setting.

## Related topics

<dl> <dt>

[About Power Management](about-power-management.md)
</dt> </dl>

 

 



