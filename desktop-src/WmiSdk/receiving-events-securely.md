---
description: Temporary and permanent consumers have different methods of securing event delivery.
ms.assetid: cd02e5db-f9e2-438b-9632-0a1387a6d4e3
ms.tgt_platform: multiple
title: Receiving Events Securely
ms.topic: article
ms.date: 05/31/2018
---

# Receiving Events Securely

Temporary and permanent consumers have different methods of securing event delivery.

The following sections are discussed in this topic:

-   [Securing Temporary Consumers](#securing-temporary-consumers)
-   [Securing Permanent Consumers](#securing-permanent-consumers)
-   [Securing the Permanent Subscription](#securing-the-permanent-subscription)
-   [Setting an Administrator-Only SD](#setting-an-administrator-only-sd)
-   [Impersonating the Event Provider Identity](#impersonating-the-event-provider-identity)
-   [SIDs and Permanent Subscriptions](#sids-and-permanent-subscriptions)
-   [Creating Permanent Subscriptions Using Domain Accounts](#creating-permanent-subscriptions-using-domain-accounts)
-   [Related topics](#related-topics)

## Securing Temporary Consumers

A [*temporary consumers*](gloss-t.md) runs until the system is rebooted or WMI is stopped but cannot be started if a specific event is raised. For example, a call to [**SWbemServices.ExecNotificationQueryAsync**](swbemservices-execnotificationqueryasync.md) creates a temporary consumer.

The calls [**SWbemServices.ExecNotificationQuery**](swbemservices-execnotificationquery.md) or [**IWbemServices::ExecNotificationQuery**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execnotificationquery) create temporary event consumers. Temporary consumers cannot control who provides events to the event [*sink*](gloss-s.md) they create.

Calls to [**ExecNotificationQuery**](swbemservices-execnotificationquery.md) methods can be made synchronously, [*semisynchronously*](gloss-s.md), or asynchronously. For example, [**SWbemServices.ExecNotificationQuery**](swbemservices-execnotificationquery.md) is a synchronous method that can be called semisynchronously, depending on how the *iflags* parameter is set. [**SWbemServices.ExecNotificationQueryAsync**](swbemservices-execnotificationqueryasync.md) is an asynchronous call.

Be aware that the callback to the sink for the asynchronous versions of these calls might not be returned at the same authentication level as the call the script made. Therefore, it is recommended that you use semisynchronous instead of asynchronous calls. If you require asynchronous communication, see [Calling a Method](calling-a-method.md) and [Setting Security on an Asynchronous Call](setting-security-on-an-asynchronous-call.md).

Scripting subscribers cannot check the access rights of an event provider to provide events to the sink created by the script. Therefore, it is recommended that calls to [**SWbemServices.ExecNotificationQuery**](swbemservices-execnotificationquery.md) use the semisynchronous form of the call and use specific security settings. For more information, see [Making a Semisynchronous Call with VBScript](making-a-semisynchronous-call-with-vbscript.md).

## Securing Permanent Consumers

A [*permanent consumers*](gloss-p.md) has a permanent subscription to events from an event provider that will persist after the operating system is restarted. An event provider that supports permanent consumers is a [*event consumer provider*](gloss-e.md). If the event provider is not running when an event occurs, then WMI starts the provider when it needs to deliver events. WMI identifies which consumer provider the events should be delivered to, based on the [**\_\_EventConsumerProviderRegistration**](--eventconsumerproviderregistration.md) instance, which associates the consumer provider [**\_\_Win32Provider**](--win32provider.md) instance with a [*logical consumer class*](gloss-l.md) defined by the consumer provider. For more information about the role of consumer providers, see [Writing an Event Consumer Provider](writing-an-event-consumer-provider.md).

Permanent consumers can control who sends them events and event providers can control who accesses their events.

Client scripts and applications create instances of the logical consumer class as part of a subscription. The logical consumer class defines what information the event contains, what the client can do with the event, and how the event is delivered.

The WMI [Standard Consumer Classes](standard-consumer-classes.md) provide examples of the role of logical consumer classes. For more information, see [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md).

## Securing the Permanent Subscription

Permanent subscriptions have greater potential to cause security problems in WMI and therefore have the following security requirements:

-   The logical consumer instance, the [**\_\_EventFilter**](--eventfilter.md), and the [**\_\_FilterToConsumerBinding**](--filtertoconsumerbinding.md) instances must have the same individual security identifier (SID) in the **CreatorSID** property. For more information, see [Keeping the same SID in all instances of a permanent subscription](#sids-and-permanent-subscriptions).
-   The account that creates the subscription must be either a domain account with local administrator privileges or the local Administrators group account. Using the Administrators group SID allows the subscription to continue to work on the local computer, even if it is disconnected from the network. Using a domain account allows exact identification of the user.

    However, if the computer is not connected and the creating account is a domain account, the consumer fails because WMI cannot verify the identity of the account. To avoid subscription failure if the computer is disconnected from the network, use the Administrators group SID for a subscription. In this case, you should ensure that the LocalSystem account can access group membership data on the domain. Some event consumer providers have particularly high security requirements, since a rogue subscription can cause great damage. Examples are the standard consumers, [**ActiveScriptEventConsumer**](activescripteventconsumer.md) and [**CommandLineEventConsumer**](commandlineeventconsumer.md).

-   You can configure the permanent subscription to only accept events from specific event provider identities. Set the security descriptor in the **EventAccess** property of the [**\_\_EventFilter**](--eventfilter.md) instance to the event provider identities. WMI compares the identity of the event provider to the security descriptor to determine if the provider has **WBEM\_RIGHT\_PUBLISH** access. For more information, see [WMI Security Constants](wmi-security-constants.md).

    If the filter allows access to the event provider identity, then it also trusts the event. This allows the consumer that received the event to raise a delegated event.

    **Note**  The default for the security descriptor in **EventAccess** is **NULL**, which allows access to everyone. Limiting access in the subscription instance of [**\_\_EventFilter**](--eventfilter.md) is recommended for better event security.

## Setting an Administrator-Only SD

The following C++ code example creates an administrator-only security descriptor on the [**\_\_EventFilter**](--eventfilter.md) instance. This example creates the security descriptor using [Security Descriptor Definition Language](/windows/desktop/SecAuthZ/security-descriptor-definition-language) (SDDL). For more information about **WBEM\_RIGHT\_SUBSCRIBE**, see [WMI Security Constants](wmi-security-constants.md).


```C++
// Create SD that allows only administrators 
//    to send events to this filter. 
// The SDDL settings are O:BAG:BAD:(A;;0x80;;;BA)
// Set the EventAccess property in the 
//    IWbemClassObject of the __EventFilter instance. 
   long lMask = WBEM_RIGHT_PUBLISH;
     WCHAR wBuf[MAX_PATH];
     _ltow( lMask, wBuf, 16 );
 
HRESULT hRes = pEventFilterInstance->Put( L"EventAccess", 0,
    &_variant_t( L"O:BAG:BAD:(A;;0x80;;;BA)" ), NULL );
```



The previous code example requires the following reference and \#include statements.


```C++
#define _WIN32_DCOM
#include <wbemidl.h>
#include <comdef.h>

#pragma comment(lib, "wbemuuid.lib")
```



## Impersonating the Event Provider Identity

A permanent consumer may need to impersonate the event provider to process the event. Permanent consumers can only impersonate the event provider when the following conditions exist:

-   The instance of [**\_\_FilterToConsumerBinding**](--filtertoconsumerbinding.md) has the **MaintainSecurityContext** property set to **True**.
-   An event is delivered in the same security context that the provider was in when it generated the event. Only a consumer implemented as a DLL, an in-process consumer, can receive events in the security context of the provider. For more information about security of in-process providers and consumers, see [Provider Hosting and Security](provider-hosting-and-security.md).
-   The event provider is running in a process that allows impersonation.

The account running the consumer process must have **FULL\_WRITE** access to the WMI repository (also known as the CIM repository). In the subscription, the [**\_\_FilterToConsumerBinding**](--filtertoconsumerbinding.md), [**\_\_EventConsumer**](--eventconsumer.md), and [**\_\_EventFilter**](--eventfilter.md) instances must have the same individual security identifier (SID) value in the **CreatorSID** property. WMI stores the SID in the **CreatorSID** for each instance.

## SIDs and Permanent Subscriptions

A permanent subscription does not work when the binding, the consumer, and the filter are not created by the same user, which means that the [**\_\_FilterToConsumerBinding**](--filtertoconsumerbinding.md), [**\_\_EventConsumer**](--eventconsumer.md), and [**\_\_EventFilter**](--eventfilter.md) must have the same individual security identifier (SID) value in the **CreatorSID** property. Windows Management Instrumentation (WMI) stores this value.

## Creating Permanent Subscriptions Using Domain Accounts

Several issues must be considered when using domain accounts to create permanent subscriptions. Every permanent subscription should still work when no user is logged on, which means they function under the built-in LocalSystem account.

If a domain user is the creator of a permanent subscription for security sensitive consumers ([**ActiveScriptEventConsumer**](activescripteventconsumer.md), [**CommandLineEventConsumer**](commandlineeventconsumer.md)), then WMI verifies whether the **CreatorSID** property of the [**\_\_EventFilter**](--eventfilter.md) class, [**\_\_FilterToConsumerBinding**](--filtertoconsumerbinding.md) class, and the consumer instances belong to a user who is member of local Administrators group.

The following code example shows how you can specify the **CreatorSID** property.

``` syntax
 instance of __EventFilter as $FILTER
    {
        // this is the Administrators SID in array of bytes format
        CreatorSID = {1,2,0,0,0,0,0,5,32,0,0,0,32,2,0,0};    
        // Add filter code here ...
    }

    instance of ActiveScriptEventConsumer as $CONSUMER
    {
       CreatorSID = {1,2,0,0,0,0,0,5,32,0,0,0,32,2,0,0};
       // Add consumer code here ...
    }

    instance of __FilterToConsumerBinding
    {
       CreatorSID = {1,2,0,0,0,0,0,5,32,0,0,0,32,2,0,0};
       Consumer = $CONSUMER;
       Filter = $FILTER;
       // Add binding code here ...
    }
```

For cross domain situations, add Authenticated Users to the "Windows Authorization Access Group".

## Related topics

<dl> <dt>

[Securing WMI Events](securing-wmi-events.md)
</dt> <dt>

[Receiving a WMI Event](receiving-a-wmi-event.md)
</dt> </dl>

 

 
