---
description: A Winlogon notification package is a DLL that exports functions that handle Winlogon events. For example, when a user logs onto the system, Winlogon calls each notification package's logon event handler function to provide information about the event.
ms.assetid: a2a26bac-93b6-4d94-94fc-42c9821935a0
title: Creating a Winlogon Notification Package
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Winlogon Notification Package

A [*Winlogon*](/windows/desktop/SecGloss/w-gly) notification package is a DLL that exports functions that handle Winlogon events. For example, when a user logs onto the system, Winlogon calls each notification package's logon event handler function to provide information about the event.

The names of the event handler functions implemented in a notification package are left up to the developer; Winlogon checks the registry to obtain the names of the event handler functions. For example, one notification package might implement the logon event handler function as `WLEventLogon` whereas another might use `HandleLogonEvent`.

You do not have to implement and register event handlers for every Winlogon event, only for events that are useful to your application. Each event handler function must use the function prototype described in [Event Handler Function Prototype](event-handler-function-prototype.md). This prototype has a single parameter: a [**WLX\_NOTIFICATION\_INFO**](/windows/desktop/api/Winwlx/ns-winwlx-wlx_notification_info) structure that contains details about the event.

Winlogon ignores the output of event handler functions. If handling an event requires interacting with Winlogon, use the [Winlogon Support Functions](authentication-functions.md).

To use your Winlogon notification package, the DLL must be copied to the %SystemRoot%\\system32 folder, and a registry update must be made for the notification package. For information about the registry update, see [Registering a Winlogon Notification Package](registering-a-winlogon-notification-package.md).

 

 
