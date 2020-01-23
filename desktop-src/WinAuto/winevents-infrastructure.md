---
title: WinEvents Infrastructure
description: The Microsoft Windows operating system includes a feature, called WinEvents, that enables processes and applications running on the Windows desktop to exchange certain types of information.
ms.assetid: ba97b00b-4a4c-4889-ae9c-8e92eb742849
ms.topic: article
ms.date: 05/31/2018
---

# WinEvents

The Microsoft Windows operating system includes a feature, called *WinEvents*, that enables processes and applications running on the Windows desktop to exchange certain types of information. Accessibility tools that use Microsoft UI Automation and Microsoft Active Accessibility are among the primary users of the WinEvents.

In the context of accessibility, UI Automation providers and Microsoft Active Accessibility servers use WinEvents to notify clients of changes in an application UI, such as when a UI element has been created or destroyed, or when an element name, state, or value has changed.

This section provides suggestions, guidelines, and examples to help clients handle WinEvents and to help servers determine when to trigger the appropriate WinEvent.

## In this section

-   [What Are WinEvents?](what-are-winevents.md)
-   [Registering a Hook Function](registering-a-hook-function.md)
-   [System-Level and Object-Level Events](system-level-and-object-level-events.md)
-   [In-Context and Out-of-Context Hook Functions](in-context-and-out-of-context-hook-functions.md)
-   [Guarding Against Reentrancy in Hook Functions](guarding-against-reentrancy-in-hook-functions.md)
-   [Allocation of WinEvent IDs](allocation-of-winevent-ids.md)

For an overview of the event notification process in Microsoft Active Accessibility, see [WinEvents](winevents-overview.md) in the [Technical Overview](technical-overview.md).

## Related topics

<dl> <dt>

[Common Infrastructure](common-infrastructure.md)
</dt> </dl>

 

 




