---
description: WMI supports different threading models depending on how the provider is hosted and the type of provider functionality, such as Class or Property.
ms.assetid: cce3faf5-7bfe-46fe-9205-57398ab9dae9
ms.tgt_platform: multiple
title: Choosing Correct Registration
ms.topic: article
ms.date: 05/31/2018
---

# Choosing Correct Registration

WMI supports different threading models depending on how the provider is hosted and the type of provider functionality, such as [Class](writing-a-class-provider.md) or [Property](writing-a-property-provider.md). For example, [*decoupled providers*](gloss-d.md) do not support all the types of provider functionality. For more information about different hosting models and how to configure them, see [Provider Hosting and Security](provider-hosting-and-security.md).

## In-Process Providers

In-process providers run in a shared host process, Wmiprvse.exe. Most in-process provider types use the multithreaded apartment (MTA) model.

The MTA model is supported for the following types of provider functionality:

-   [Class Provider](writing-a-class-provider.md)
-   [Instance Provider](writing-an-instance-provider.md)
-   [Method Provider](writing-a-method-provider.md)
-   [Property Provider](writing-a-property-provider.md)
-   [Event Provider](writing-an-event-provider.md)
-   [Event Consumer Provider](writing-an-event-consumer-provider.md)

The single-threaded apartment (STA) model is supported for some types of provider functionality:

-   [Instance Provider](writing-an-instance-provider.md)
-   [Method Provider](writing-a-method-provider.md)
-   [Event Provider](writing-an-event-provider.md)
-   [Event Consumer Provider](writing-an-event-consumer-provider.md)

## Out-of-Process Providers

Providers that are hosted in a different shared service host support the following provider functionality:

-   [Class Provider](writing-a-class-provider.md)
-   [Instance Provider](writing-an-instance-provider.md)
-   [Method Provider](writing-a-method-provider.md)
-   [Property Provider](writing-a-property-provider.md)
-   [Event Provider](writing-an-event-provider.md)
-   [Event Consumer Provider](writing-an-event-consumer-provider.md)

For more information about shared service hosts, see [Provider Hosting and Security](provider-hosting-and-security.md).

## Decoupled Providers

Decoupled providers are hosted in an application. For more information, see [Incorporating a Provider in an Application](incorporating-a-provider-in-an-application.md). Providers created using WMI in the .NET Framework are decoupled. Decoupled providers support the following provider functionality:

-   [Instance Provider](writing-an-instance-provider.md)
-   [Method Provider](writing-a-method-provider.md)
-   [Event Provider](writing-an-event-provider.md)
-   [Event Consumer Provider](writing-an-event-consumer-provider.md)

## Related topics

<dl> <dt>

[Developing a WMI Provider](developing-a-wmi-provider.md)
</dt> <dt>

[Provider Hosting and Security](provider-hosting-and-security.md)
</dt> </dl>

 

 



