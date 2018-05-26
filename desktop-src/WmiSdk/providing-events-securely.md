---
Description: You can prevent unauthorized users from receiving events to which they should not have access.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 59788643-f57d-458f-91ab-26552218523b
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Providing Events Securely
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Providing Events Securely

You can prevent unauthorized users from receiving events to which they should not have access. Your event provider can supply instances of its own event classes, just as the [System Registry Provider](https://msdn.microsoft.com/library/aa393886) supplies classes such as [**RegistryKeyChangeEvent**](https://msdn.microsoft.com/library/aa393040). Your event provider can also deliver intrinsic events such as [**\_\_InstanceCreationEvent**](--instancecreationevent.md). For more information, see [Writing an Event Provider](writing-an-event-provider.md).

An event provider can control access to event recipients in the following ways:

-   Using access control by implementing [**IWbemEventProviderSecurity::AccessCheck**](/windows/win32/Wbemprov/nn-wbemprov-iwbemeventprovidersecurity?branch=master) is the most efficient way.

    The provider determines whether the consumer has privileges to receive a requested event. If the consumer lacks sufficient privileges to register, WMI returns an access denied error. Use this mode when the provider can make the decision about who can receive events. For example, a provider may supply security related events and can require that the consumer have administrator privileges with the **SeSecurityPrivilege** privilege enabled.

-   Implementing [**IWbemEventSink::SetSinkSecurity**](/windows/win32/Wbemprov/nf-wbemprov-iwbemeventsink-setsinksecurity?branch=master) on the sink used to raise events allows the setting of a security descriptor (SD) on a sink for all the events passing through.

    WMI performs access checks based on the SD. Use this mode when the provider cannot make the decision regarding who is allowed to consume its events, but can decide on an SD for a specific sink. For example, use [**IWbemEventSink::SetSinkSecurity**](/windows/win32/Wbemprov/nf-wbemprov-iwbemeventsink-setsinksecurity?branch=master) if your event provider obtained several sinks by calls to [**IWbemEventSink::GetRestrictedSink**](/windows/win32/Wbemprov/nf-wbemprov-iwbemeventsink-getrestrictedsink?branch=master) and you want a security descriptor for each sink.

-   Setting the **SECURITY\_DESCRIPTOR** property of an event allows for the setting of an SD for each event.

    Use this approach when each event delivered to the sink can have different security descriptors. To use this approach, derive any of the extrinsic event classes defined by your provider from [**\_\_Event**](--event.md) or [**\_\_ExtrinsicEvent**](--extrinsicevent.md) so that your class contains the **SECURITY\_DESCRIPTOR** property. For example, your event provider may publish both secure and normal events through a sink. In this case, use the Administrators account security descriptor for secure events and a **NULL** security descriptor for normal events that can be received by anyone.

## Securing Events by Decoupled Event Providers

Decoupled event providers differ from nondecoupled event providers in the way that they register with WMI. The call to [**IWbemEventProviderSecurity::AccessCheck**](/windows/win32/Wbemprov/nf-wbemprov-iwbemeventprovidersecurity-accesscheck?branch=master) for events from a decoupled provider never propagates the client access token. WMI handles the access control in the same manner as for nondecoupled event providers. For more information about writing a decoupled provider, see [Incorporating a Provider in an Application](incorporating-a-provider-in-an-application.md).

Only administrators with the **FULL\_WRITE** privilege set in **WMI Control** of the **Control Panel** are allowed to raise events for a namespace. For more information, see [Setting Namespace Security with the WMI Control](setting-namespace-security-with-the-wmi-control.md).

## Related topics

<dl> <dt>

[Securing WMI Events](securing-wmi-events.md)
</dt> </dl>

 

 



