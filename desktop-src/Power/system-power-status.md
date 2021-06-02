---
description: The system power status indicates whether the source of power for a computer is a system battery or AC power. For computers that use batteries, the system power status also indicates how much battery life remains and whether the battery is charging.
ms.assetid: b9a5e7de-a603-4bd9-b854-1e58572c3b2b
title: System Power Status
ms.topic: article
ms.date: 05/31/2018
---

# System Power Status

The system power status indicates whether the source of power for a computer is a system battery or AC power. For computers that use batteries, the system power status also indicates how much battery life remains and whether the battery is charging.

Power information is retrieved by registering for power setting notifications through the [**RegisterPowerSettingNotification**](/windows/desktop/api/WinUser/nf-winuser-registerpowersettingnotification) function. This function allows applications to register for specific power settings and be notified when they change.

> [!Note]  
> To query for power status information without notifications, use [**CallNtPowerInformation**](/windows/desktop/api/Powerbase/nf-powerbase-callntpowerinformation).

 

Applications and installable drivers typically use the system power status to determine whether continued operation is feasible. For example, before an application performs background operations such as compressing or paginating a file, it should check whether the system is on batteries. As another example, an application that is beginning a lengthy operation should check the status to determine whether enough battery power exists to complete the operation.

By default, the system does not query applications or drivers during sleep transitions.

> [!Note]  
> If power is low, an application can request user intervention or request that the system suspend itself. You can suspend system operation by using the [**SetSuspendState**](/windows/desktop/api/PowrProf/nf-powrprof-setsuspendstate) function.

 

## Related topics

<dl> <dt>

[About Power Management](about-power-management.md)
</dt> </dl>

 

 



