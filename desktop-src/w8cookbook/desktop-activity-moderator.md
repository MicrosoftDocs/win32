---
title: Desktop Activity Moderator
description: Desktop Activity Moderator
ms.assetid: F1C54DB0-0AFC-4A1B-9697-6CEB519C2663
keywords:
- battery life
- connected standby
- suspension
- throttling
ms.topic: article
ms.date: 05/31/2018
---

# Desktop Activity Moderator

## Platform

**Clients** – Windows 8 


> [!Note]  
> The DAM is present only on Windows 8 client machines that support connected standby. The DAM is not present on server SKUs.

 

  

> [!Note]  
> Windows Store apps built for Windows 8 are not impacted by the DAM.

 

  
</dl>

## Description

Our customers are shifting towards lighter, smaller, more mobile platforms to satisfy their computing needs. As part of the shift to mobile devices, users have become increasingly concerned about battery life of their devices. The Desktop Activity Moderator (DAM) is one of several new features in Windows 8 designed to ensure consistent, long battery life for devices that support connected standby.

Connected standby occurs when the device is powered on, but the screen is turned off. In this power state, the system is technically always “on” (to support key scenarios like mail, VoIP, social networking, and instant messaging with Windows Store apps). It is analogous to the state a smart phone is in when the user presses the power button.

As such, software (including apps and operating system software) must be well-behaved during connected standby. The DAM was created to suppress desktop app execution in a manner similar to the Sleep state (S3 on ACPI devices). It does this by suspending or throttling desktop software processes across the system upon connected standby entry. This enables systems that support connected standby to deliver minimized resource usage and long, consistent battery life while enabling Windows Store apps to deliver the connected experiences they promise.

## Details

The DAM is a kernel -mode driver that is loaded and initialized at system boot if the system supports connected standby. (This is determined by evaluating if the AOAC field in the SYSTEM\_POWER\_CAPABILITIES structure returned by CallNtPowerInformation is set to TRUE).

When the DAM is enabled and your desktop process is created, the DAM adds your process to system-managed job objects:

-   If the process was created in session 0, DAM adds the process to a job object subject to **throttling**
-   If the process was created in an interactive session (session 1 or higher), DAM adds the process to a job object subject to **suspension**

> [!Note]  
> For Windows 8, job objects can be nested. This means that the DAM’s usage of job objects does not interfere with an app’s existing usage of job objects.

 

When the screen is on, the DAM is disengaged and does not impact any processes on the system. When the system is in connected standby, depending on activity on the system, DAM might throttle or suspend processes.

-   Processes that are subject to suspension have all their threads suspended (not allowed to run under any circumstances); app state (process memory) is maintained
-   Processes that are subject to throttling cycle between suspended and unsuspended (a large majority of time is spent in the suspended state)
    -   Be aware that Windows might also detect that critical activities are occurring and might unsuspend throttled services for longer periods of time during this activity
    -   Also, note that while in connected standby, sensors and networks might not be available, so throttled processes should be designed to be resilient to poor network conditions (for most processes, this doesn’t require any change)

When DAM suspension is engaged or disengaged, DAM triggers delivery of a WM\_POWERBROADCAST message to those processes subject to suspension that have opted-in to message delivery (via API call or compatibility shim, described later). After a few seconds delay, DAM suspends the process.

There are no notifications when DAM throttling is engaged or disengaged. Processes should not need modification; processes continue to function, albeit at a slower rate.

## Manifestation

Processes are often suspended or throttled during the connected standby state. To the majority of suspended apps, this should be very similar to an S3 suspend / resume or S4 hibernate / resume transition. Manifestations might include but are not limited to inconsistencies in uptime / runtime vs. wall clock time, inconsistencies in timer behavior, or dramatic changes in operating system state before and after the suspend completes.

Suspension and throttling happens as a unit (all suspendable processes are suspended and unsuspended in unison, and all processes that can be throttled are throttled and unthrottled in unison), so communication between two suspended processes or two throttled processes does not pose a problem.

Software that relies on cross-process communication might need special consideration:

-   **Communication between processes in session 0 (throttled) and session 1+ (suspended)** – examples include tray icons or UI components that represent current service state
-   **Communication between components in user mode (session 0 or 1) and drivers (which are neither throttled nor suspended)** – examples include services that do work on behalf of a driver

In these cases, if cross-process communication is not handled correctly, apps can appear hung or unresponsive (though the user might not see this impact directly, as the screen will be off when in connected standby). In most cases, however, services and drivers should already be developed to be robust against cross-process communication issues.

Vendors who create software for, or dependent on, the web should consider how process suspension affects connection lifetimes and handshakes. Additionally, because network connectivity might not be available when in Connected Standby mode, developers of processes created in session 0 should be especially aware of how intermittent network connections affect the process.

## Solution

Windows Store apps are not impacted by the DAM. If your desktop app is impacted by the DAM, you can request notifications before suspension is engaged (for example, to save state or close network connections) using one of these methods:

-   If your app has a window (HWND) and you want to handle these notifications through your window procedure, call [RegisterSuspendResumeNotification](/windows/win32/api/winuser/nf-winuser-registersuspendresumenotification) to register for these messages (or [UnregisterSuspendResumeNotification](/windows/win32/api/winuser/nf-winuser-unregistersuspendresumenotification) to unregister). You can use DEVICE\_NOTIFY\_WINDOW\_HANDLE in the Flags parameter, and pass your window’s HWND in as the Recipient parameter. The message received is the WM\_POWERBROADCAST message.
-   If your app does not have a window (HWND) or you want a direct callback, call [PowerRegisterSuspendResumeNotification](/windows/win32/api/powerbase/nf-powerbase-powerregistersuspendresumenotification) to register for these messages (or [PowerUnregisterSuspendResumeNotification](/windows/win32/api/powerbase/nf-powerbase-powerunregistersuspendresumenotification) to unregister). You must use DEVICE\_NOTIFY\_CALLBACK in the Flags parameter and pass a value of type PDEVICE\_NOTIFY\_SUBSCRIBE\_PARAMETERS in the Recipient parameter.
-   If your app cannot be recompiled, you can opt in to receive these WM\_POWERBROADCAST messages via the [AppCompat toolkit](../win7appqual/application-compatibility-toolkit--act-.md) (using the PromoteDAM shim).

The suspend message is WM\_POWERBROADCAST with wParam=PBT\_APMSUSPEND; this message is broadcast concurrently to all opted in processes on the system. Your app must perform any work on the suspend path quickly and efficiently. The timeout after the broadcast notification is global, not per process, so your process might be contending for system resources if the work required in this path is extensive.

The resume message is WM\_POWERBROADCAST with wParam=PBT\_APMRESUME; this message is broadcast concurrently to all opted in processes after a resume. Relative time of delivery to the system exit from connected standby is not guaranteed.

For camera related applications, when power state transition is taking place, during the suspension notification, applications must release all references to the camera (all capture pipeline objects must be shutdown and disposed of).  To avoid possible battery drain, on Windows 10 RS3+ systems Windows Camera Frame Server service will close all capture sessions if the application does not handle the suspension notification properly.  The side effect of this is that when the system comes out of standby or S3/S4 state, the application’s capture pipeline is no longer in a working state.

## Tests

Test your software across connected standby transitions.

## Resources

-   [Mobile Battery Life Solutions for Windows 7](/previous-versions/windows/hardware/design/dn641606(v=vs.85))
-   [SYSTEM\_POWER\_CAPABILITIES](/windows/win32/api/winnt/ns-winnt-system_power_capabilities)
-   [CallNtPowerInformation function](/windows/win32/api/powerbase/nf-powerbase-callntpowerinformation)
-   [Job Objects](../procthread/job-objects.md)
-   [RegisterSuspendResumeNotification](/windows/win32/api/winuser/nf-winuser-registersuspendresumenotification)
-   [UnregisterSuspendResumeNotification](/windows/win32/api/winuser/nf-winuser-unregistersuspendresumenotification)
-   [PowerRegisterSuspendResumeNotification](/windows/win32/api/powerbase/nf-powerbase-powerregistersuspendresumenotification)
-   [PowerUnregisterSuspendResumeNotification](/windows/win32/api/powerbase/nf-powerbase-powerunregistersuspendresumenotification)
-   [AppCompat toolkit](../win7appqual/application-compatibility-toolkit--act-.md)

 

 