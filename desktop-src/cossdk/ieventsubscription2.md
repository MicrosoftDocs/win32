---
description: Stores and retrieves information about event subscriptions. This interface extends the IEventSubscription interface.
ms.assetid: f153afb7-c897-40f8-81ed-50308844cac5
title: IEventSubscription2 interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IEventSubscription2
api_type: 
- COM
api_location: 
---

# IEventSubscription2 interface

Stores and retrieves information about event subscriptions. This interface extends the [**IEventSubscription**](/windows/desktop/api/EventSys/nn-eventsys-ieventsubscription) interface.

## When to implement

You do not need to implement the **IEventSubscription2** interface. A system-supplied event object class (CLSID\_CEventSubscription) implements **IEventSubscription2**.

## When to use

The [COM+ Events](com--events.md) system uses this interface to obtain information about individual subscriptions.

## Members

The **IEventSubscription2** interface inherits from **IEventSubscription**. **IEventSubscription2** also has these types of members:

-   [Properties](#properties)

### Properties

The **IEventSubscription2** interface has these properties.



| Property                                                                      | Access type           | Description                                                |
|:------------------------------------------------------------------------------|:----------------------|:-----------------------------------------------------------|
| [**FilterCriteria**](ieventsubscription2-filtercriteria.md)<br/>       | Read/write<br/> | The filter criteria governing the subscription.<br/> |
| [**SubscriberMoniker**](ieventsubscription2-subscribermoniker.md)<br/> | Read/write<br/> | The subscriber's moniker.<br/>                       |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[**IEventSubscription**](/windows/desktop/api/EventSys/nn-eventsys-ieventsubscription)
</dt> </dl>

 

 




