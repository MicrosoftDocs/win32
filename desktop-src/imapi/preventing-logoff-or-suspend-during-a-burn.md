---
title: Preventing Logoff or Suspend During a Burn
description: If proper precautions are not made within an application, it is possible for a user to log off during a burn operation. This leads to the interruption of the burn process, which can result in lost data and possibly render the disc unusable.
ms.assetid: 5223c9f6-30f6-43ce-b46c-267da0a53d4b
ms.topic: article
ms.date: 05/31/2018
---

# Preventing Logoff or Suspend During a Burn

If proper precautions are not made within an application, it is possible for a user to log off during a burn operation. This leads to the interruption of the burn process, which can result in lost data and possibly render the disc unusable.

To avoid this problem, the application should process the [**WM\_QUERYENDSESSION**](/windows/desktop/Shutdown/wm-queryendsession) message which is delivered prior to log off. If the application receives this message while performing a burn operation, return **FALSE** to cancel the logoff procedure. If the application allows the user to decide whether to continue logging off, a warning should be provided indicating that user will lose data.

Power transitions during the burn process can also create potential problems in the success of a burn activity. Preventing these complications during the burn process requires an application to be aware of when power transitions are about to take place. This is accomplished by by enabling the application to process the [**WM\_POWERBROADCAST**](/windows/desktop/Power/wm-powerbroadcast) message. Applications developed for Windows XP or Windows Server 2003 can return **BROADCAST\_QUERY\_DENY** in response to [**PBT\_APMQUERYSUSPEND**](/windows/desktop/Power/pbt-apmquerysuspend), preventing Suspend during the burn process.

Due to changes in the Power Management Model for Windows Vista and Windows Server 2008, the [**PBT\_APMQUERYSUSPEND**](/windows/desktop/Power/pbt-apmquerysuspend) event is no longer delivered to applications. Instead the [**PBT\_APMSUSPEND**](/windows/desktop/Power/pbt-apmsuspend) event is delivered, providing two seconds for an application to prepare for the transition.

As a result of these changes, it is recommended that applications call the [**SetThreadExecutionState**](/windows/desktop/api/winbase/nf-winbase-setthreadexecutionstate) function to prevent a system idle time-out which ordinarily results in the transition to Suspend. It is important to remember that calling this function with the appropriate flags set will only prevent system idle, not an in-progress Suspend.

## Related topics

<dl> <dt>

[Using IMAPI](using-imapi.md)
</dt> <dt>

[**SetThreadExecutionState**](/windows/desktop/api/winbase/nf-winbase-setthreadexecutionstate)
</dt> </dl>

 

 