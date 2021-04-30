---
description: The system broadcasts a message to all applications and installable drivers whenever a power management event occurs.
ms.assetid: a64ed11a-43d6-41f7-aabd-5dca2a2b4a12
title: WM_POWERBROADCAST Messages
ms.topic: article
ms.date: 05/31/2018
---

# WM\_POWERBROADCAST Messages

The system broadcasts a message to all applications and installable drivers whenever a power management event occurs. The system broadcasts these events through the [**WM\_POWERBROADCAST**](wm-powerbroadcast.md) message, setting the *wParam* parameter to the appropriate power management event. For example, the [PBT\_APMPOWERSTATUSCHANGE](pbt-apmpowerstatuschange.md) event indicates a system power status change. You must ensure that your application responds properly to the **WM\_POWERBROADCAST** message.

The system broadcasts a [PBT\_APMSUSPEND](pbt-apmsuspend.md) event immediately before suspending operation. This gives applications and drivers one last chance to prepare for the event. In many cases, the system broadcasts these messages without requesting permission to do so. This happens, for example, if an application forces suspension with the [**SetSuspendState**](/windows/desktop/api/PowrProf/nf-powrprof-setsuspendstate) function.

The system broadcasts the [PBT\_APMRESUMESUSPEND](pbt-apmresumesuspend.md) or [PBT\_APMRESUMECRITICAL](pbt-apmresumecritical.md) event when system operation has been restored. If an application received a [PBT\_APMSUSPEND](pbt-apmsuspend.md) event before the computer was suspended, it will receive the PBT\_APMRESUMESUSPEND event. Otherwise, it will receive the PBT\_APMRESUMECRITICAL event.

The system sends a [PBT\_POWERSETTINGCHANGE](pbt-powersettingchange.md) event to applications that have registered for the specific event using [**RegisterPowerSettingNotification**](/windows/desktop/api/WinUser/nf-winuser-registerpowersettingnotification). For more information, see [Registering for Power Events](registering-for-power-events.md).

## Related topics

<dl> <dt>

[About Power Management](about-power-management.md)
</dt> </dl>

 

 



