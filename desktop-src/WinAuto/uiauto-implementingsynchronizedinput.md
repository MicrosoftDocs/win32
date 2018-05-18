---
title: SynchronizedInput Control Pattern
description: Describes guidelines and conventions for implementing ISynchronizedInputProvider, including information about properties and methods.
ms.assetid: '3e2d65ea-8093-4e65-b43e-28478ec74607'
keywords: ["UI Automation,implementing SynchronizedInput control pattern", "UI Automation,SynchronizedInput control pattern", "UI Automation,ISynchronizedInputProvider", "ISynchronizedInputProvider", "implementing UI Automation SynchronizedInput control patterns", "SynchronizedInput control patterns", "control patterns,ISynchronizedInputProvider", "control patterns,implementing UI Automation SynchronizedInput", "control patterns,SynchronizedInput", "interfaces,ISynchronizedInputProvider"]
---

# SynchronizedInput Control Pattern

Describes guidelines and conventions for implementing [**ISynchronizedInputProvider**](uiauto-isynchronizedinputprovider.md), including information about properties and methods. The **SynchronizedInput** control pattern enables Microsoft UI Automation client applications to direct the mouse or keyboard input to a specific UI element.

This control pattern is typically used in automated test scripts to send mouse or keyboard input to a specific user-interface element, and then verify that the element received the input.

This topic contains the following sections.

-   [Implementation Guidelines and Conventions](#implementation-guidelines-and-conventions)
-   [Required Members for **ISynchronizedInputProvider**](#required-members-for-isynchronizedinputprovider)
-   [Related topics](#related-topics)

## Implementation Guidelines and Conventions

When implementing the **SynchronizedInput** control pattern, note the following guidelines and conventions:

-   When the [**ISynchronizedInputProvider::StartListening**](uiauto-isynchronizedinputprovider-startlistening.md) method is called, the UI Automation provider should start checking for input of the specified type, and then take one of the following actions:
    -   When matching input is found for the element, the provider should raise the [**UIA\_InputReachedTargetEventId**](uiauto-event-ids.md#uia-inputreachedtargeteventid) event.
    -   When matching input is found, but it reached a different element, the provider should raise the [**UIA\_InputReachedOtherElementEventId**](uiauto-event-ids.md#uia-inputreachedotherelementeventid) event.
    -   When mismatched input is found, the provider should discard the input and raise the [**UIA\_InputDiscardedEventId**](uiauto-event-ids.md#uia-inputdiscardedeventid) event.
-   The UI Automation provider must discard the input if it is for an element other than the current element.
-   When the element receives the input, or when the [**ISynchronizedInputProvider::Cancel**](uiauto-isynchronizedinputprovider-cancel.md) method is called, the provider stops checking input and continues as normal.
-   If [**ISynchronizedInputProvider::StartListening**](uiauto-isynchronizedinputprovider-startlistening.md) is called when the provider is already listening for input, the provider should return [**UIA\_E\_INVALIDOPERATION**](uiauto-error-codes.md#uia-e-invalidoperation).

## Required Members for **ISynchronizedInputProvider**

The following properties, methods, and events are required for implementing the [**ISynchronizedInputProvider**](uiauto-isynchronizedinputprovider.md) interface.



| Required members                                                                         | Member type | Notes |
|------------------------------------------------------------------------------------------|-------------|-------|
| [**StartListening**](uiauto-isynchronizedinputprovider-startlistening.md)               | Method      | None  |
| [**Cancel**](uiauto-isynchronizedinputprovider-cancel.md)                               | Method      | None  |
| [**UIA\_InputReachedTargetEventId**](uiauto-event-ids.md#uia-inputreachedtargeteventid) | Event       | None  |



 

## Related topics

<dl> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> </dl>

 

 




