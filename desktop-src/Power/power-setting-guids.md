---
Description: Power setting GUIDs identify power change events.
ms.assetid: 39D432A7-54F8-4135-B98C-7290F95B054A
title: Power Setting GUIDs
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Power Setting GUIDs

Power setting **GUID**s identify power change events. This topic lists power setting **GUID**s for notifications that are most useful to applications. An application should register for each power change event that might impact its behavior. Notification is sent each time a setting changes.

Power setting **GUID**s are defined in WinNT.h.

<dl> <dt>

<span id="GUID_ACDC_POWER_SOURCE"></span><span id="guid_acdc_power_source"></span>**GUID\_ACDC\_POWER\_SOURCE**
</dt> <dd> <dl> <dt>

5d3e9a59-e9D5-4b00-a6bd-ff34ff516548
</dt> <dt>



The system power source has changed. The **Data** member is a **DWORD** with values from the [**SYSTEM\_POWER\_CONDITION**](/windows/desktop/api/WinNT/ne-winnt-system_power_condition) enumeration that indicates the current power source.

<dl> <dt>

**PoAc** (0) - The computer is powered by an AC power source (or similar, such as a laptop powered by a 12V automotive adapter).
</dt> <dt>

**PoDc** (1) - The computer is powered by an onboard battery power source.
</dt> <dt>

**PoHot** (2) - The computer is powered by a short-term power source such as a UPS device.
</dt> </dl>

</dl> </dd> <dt>

<span id="GUID_BATTERY_PERCENTAGE_REMAINING"></span><span id="guid_battery_percentage_remaining"></span>**GUID\_BATTERY\_PERCENTAGE\_REMAINING**
</dt> <dd> <dl> <dt>

a7ad8041-b45a-4cae-87a3-eecbb468a9e1
</dt> <dt>



The remaining battery capacity has changed. The granularity varies from system to system but the finest granularity is 1 percent. The **Data** member is a **DWORD** that indicates the current battery capacity remaining as a percentage from 0 through 100.


</dt> </dl> </dd> <dt>

<span id="GUID_CONSOLE_DISPLAY_STATE"></span><span id="guid_console_display_state"></span>**GUID\_CONSOLE\_DISPLAY\_STATE**
</dt> <dd> <dl> <dt>

6fe69556-704a-47a0-8f24-c28d936fda47
</dt> <dt>



The current monitor's display state has changed.

**Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This notification is available starting with Windows 8 and Windows Server 2012.

The **Data** member is a **DWORD** with one of the following values.

<dl> <dt>

0x0 - The display is off.
</dt> <dt>

0x1 - The display is on.
</dt> <dt>

0x2 - The display is dimmed.
</dt> </dl>

</dl> </dd> <dt>

<span id="GUID_GLOBAL_USER_PRESENCE"></span><span id="guid_global_user_presence"></span>**GUID\_GLOBAL\_USER\_PRESENCE**
</dt> <dd> <dl> <dt>

786E8A1D-B427-4344-9207-09E70BDCBEA9
</dt> <dt>



The user status associated with any session has changed. This represents the combined status of user presence across all local and remote sessions on the system.

This notification is sent only services and other programs running in session 0. User-mode applications should register for **GUID\_SESSION\_USER\_PRESENCE** instead.

**Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This notification is available starting with Windows 8 and Windows Server 2012.

The **Data** member is a **DWORD** with one of the following values.

<dl> <dt>

**PowerUserPresent** (0) - The user is present in any local or remote session on the system.
</dt> <dt>

**PowerUserInactive** (2) - The user is not present in any local or remote session on the system.
</dt> </dl>

</dl> </dd> <dt>

<span id="GUID_IDLE_BACKGROUND_TASK"></span><span id="guid_idle_background_task"></span>**GUID\_IDLE\_BACKGROUND\_TASK**
</dt> <dd> <dl> <dt>

515c31d8-f734-163d-a0fd-11a0-8c91e8f1
</dt> <dt>



The system is busy. This indicates that the system will not be moving into an idle state in the near future and that the current time is a good time for components to perform background or idle tasks that would otherwise prevent the computer from entering an idle state.

There is no notification when the system is able to move into an idle state. The idle background task notification does not indicate whether a user is present at the computer. The **Data** member has no information and can be ignored.


</dt> </dl> </dd> <dt>

<span id="GUID_MONITOR_POWER_ON"></span><span id="guid_monitor_power_on"></span>**GUID\_MONITOR\_POWER\_ON**
</dt> <dd> <dl> <dt>

02731015-4510-4526-99e6-e5a17ebd1aea
</dt> <dt>



The primary system monitor has been powered on or off. This notification is useful for components that actively render content to the display device, such as media visualization. These applications should register for this notification and stop rendering graphics content when the monitor is off to reduce system power consumption. The **Data** member is a **DWORD** that indicates the current monitor state.

<dl> <dt>

0x0 - The monitor is off.
</dt> <dt>

0x1 - The monitor is on.
</dt> </dl>

**Windows 8 and Windows Server 2012:** New applications should use **GUID\_CONSOLE\_DISPLAY\_STATE** instead of this notification.

</dl> </dd> <dt>

<span id="GUID_POWER_SAVING_STATUS"></span><span id="guid_power_saving_status"></span>**GUID\_POWER\_SAVING\_STATUS**
</dt> <dd> <dl> <dt>

E00958C0-C213-4ACE-AC77-FECCED2EEEA5
</dt> <dt>



Battery saver has been turned off or on in response to changing power conditions. This notification is useful for components that participate in energy conservation. These applications should register for this notification and save power when battery saver is on.

The **Data** member is a **DWORD** that indicates battery saver state.

<dl> <dt>

0x0 - Battery saver is off.
</dt> <dt>

0x1 - Battery saver is on. Save energy where possible.
</dt> </dl>

For general information about battery saver, see [battery saver (in the hardware component guidelines)](https://msdn.microsoft.com/library/windows/hardware/mt186374).

</dl> </dd> <dt>

<span id="GUID_POWERSCHEME_PERSONALITY"></span><span id="guid_powerscheme_personality"></span>**GUID\_POWERSCHEME\_PERSONALITY**
</dt> <dd> <dl> <dt>

245d8541-3943-4422-b025-13A7-84F679B7
</dt> <dt>



The active power scheme personality has changed. All power schemes map to one of these personalities. The **Data** member is a **GUID** that indicates the new active power scheme personality.

<dl> <dt>



**GUID\_MIN\_POWER\_SAVINGS** (8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c)

High Performance - The scheme is designed to deliver maximum performance at the expense of power consumption savings.


</dt> <dt>



**GUID\_MAX\_POWER\_SAVINGS** (a1841308-3541-4fab-bc81-f71556f20b4a)

Power Saver - The scheme is designed to deliver maximum power consumption savings at the expense of system performance and responsiveness.


</dt> <dt>



**GUID\_TYPICAL\_POWER\_SAVINGS** (381b4222-f694-41f0-9685-ff5bb260df2e)

Automatic - The scheme is designed to automatically balance performance and power consumption savings.


</dt> </dl>

</dl> </dd> <dt>

<span id="GUID_SESSION_DISPLAY_STATUS"></span><span id="guid_session_display_status"></span>**GUID\_SESSION\_DISPLAY\_STATUS**
</dt> <dd> <dl> <dt>

2B84C20E-AD23-4ddf-93DB-05FFBD7EFCA5
</dt> <dt>



The display associated with the application's session has been powered on or off.

**Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This notification is available starting with Windows 8 and Windows Server 2012.

This notification is sent only to user-mode applications. Services and other programs running in session 0 do not receive this notification. The **Data** member is a **DWORD** with one of the following values.

<dl> <dt>

0x0 - The display is off.
</dt> <dt>

0x1 - The display is on.
</dt> <dt>

0x2 - The display is dimmed.
</dt> </dl>

</dl> </dd> <dt>

<span id="GUID_SESSION_USER_PRESENCE"></span><span id="guid_session_user_presence"></span>**GUID\_SESSION\_USER\_PRESENCE**
</dt> <dd> <dl> <dt>

3C0F4548-C03F-4c4d-B9F2-237EDE686376
</dt> <dt>



The user status associated with the application's session has changed.

**Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This notification is available starting with Windows 8 and Windows Server 2012.

This notification is sent only to user-mode applications running in an interactive session. Services and other programs running in session 0 should register for **GUID\_GLOBAL\_USER\_PRESENCE**. The **Data** member is a **DWORD** with one of the following values.

<dl> <dt>

**PowerUserPresent** (0) - The user is providing input to the session.
</dt> <dt>

**PowerUserInactive** (2) - The user activity timeout has elapsed with no interaction from the user.
</dt> </dl>

> [!Note]  
> All applications that run in an interactive user-mode session should use this setting. When kernel mode applications register for monitor status they should use **GUID\_CONSOLE\_DISPLAY\_STATUS** instead.

 

</dl> </dd> <dt>

<span id="GUID_SYSTEM_AWAYMODE"></span><span id="guid_system_awaymode"></span>**GUID\_SYSTEM\_AWAYMODE**
</dt> <dd> <dl> <dt>

98a7f580-01f7-48aa-9c0f-44352c29e5C0
</dt> <dt>



The system is entering or exiting away mode. The **Data** member is a **DWORD** that indicates the current away mode state.

<dl> <dt>

0x0 - The computer is exiting away mode.
</dt> <dt>

0x1 - The computer is entering away mode.
</dt> </dl>

</dl> </dd> </dl>

## Requirements



|                   |                                                                                    |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>WinNT.h</dt> </dl> |



 

 




