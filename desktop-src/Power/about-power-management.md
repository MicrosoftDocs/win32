---
description: The Windows operating system provides a comprehensive and system-wide set of power management features. This enables systems to extend battery life and save energy, reduce heat and noise, and help ensure data reliability.
ms.assetid: 01ce4d21-1a0c-44a8-91ef-5e300e7c6c9a
title: About Power Management
ms.topic: concept-article
ms.date: 07/16/2026
---

# About Power Management

The Windows operating system provides a comprehensive and system-wide set of power management features. This enables systems to extend battery life and save energy, reduce heat and noise, and help ensure data reliability.

## Modern Standby and application design

Modern Standby (S0 low-power idle) is the default sleep model on most Windows 11 devices. Unlike traditional S3 sleep, the system remains partially running—network connectivity can be maintained, and the system can wake instantly. This changes how applications should handle background work.

> [!IMPORTANT]
> **Common anti-patterns that drain battery in Modern Standby:**
>
> - **Holding `ES_SYSTEM_REQUIRED` continuously** — This prevents the system from entering low-power idle. Only hold this flag while actively performing work, then clear it immediately.
> - **Periodic timer wake-ups** — Timers that fire every few seconds keep the CPU active. Use [coalescing timers](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-setthreadpooltimerex) or event-driven designs instead.
> - **Unbounded network polling** — For packaged apps, use push notifications (WNS). For unpackaged Win32 apps, use event-driven sockets or [network list change notifications](/windows/win32/api/netlistmgr/nn-netlistmgr-inetworklistmanagerevents) rather than polling an endpoint.
> - **Audio/media streams left open** — Even silent streams prevent audio-device power-down. Release audio devices when not actively rendering.

### Best practices for Modern Standby

1. **Register for power notifications** to detect transitions. Use [PowerSettingRegisterNotification](/windows/desktop/api/Powersetting/nf-powersetting-powersettingregisternotification) with `GUID_MONITOR_POWER_ON` and `GUID_POWER_SAVING_STATUS`.
2. **Defer non-critical work** until the device is on AC power. Check with [GetSystemPowerStatus](/windows/desktop/api/Winbase/nf-winbase-getsystempowerstatus) before starting large operations.
3. **Use SetThreadExecutionState sparingly** — Call with `ES_CONTINUOUS | ES_SYSTEM_REQUIRED` only for active operations (file transfers, media recording), and always clear with `SetThreadExecutionState(ES_CONTINUOUS)` once the operation finishes.
4. **Batch network operations** — Combine multiple small requests into one session to minimize radio wake time.
5. **Respect battery saver** — When `GUID_POWER_SAVING_STATUS` indicates battery saver is active, reduce or eliminate background activity.

The power management functions and messages retrieve the system power status, notify applications of power management events, and notify the system of each application's power requirements. This overview contains the following topics:

-   [Windows Power Management](windows-power-management.md)
-   [System Power Status](system-power-status.md)
-   [System Power States](system-power-states.md)
-   [System Power Management Events](system-power-management-events.md)
-   [WM\_POWERBROADCAST Messages](wm-powerbroadcast-messages.md)
-   [System Sleep Criteria](system-sleep-criteria.md)
-   [System Wake-up Events](system-wake-up-events.md)
-   [Battery Information](battery-information.md)
-   [Backlight Control Interface](backlight-control-interface.md)
-   [Power Schemes](power-schemes.md)
-   [Device Power Management](device-power-management.md)

## Related topics

<dl> <dt>

[Power Management](power-management-portal.md)
</dt> </dl>

 

 



