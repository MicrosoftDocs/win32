---
description: Stores and retrieves information about event subscriptions. This interface extends the IEventSubscription2 interface.
ms.assetid: fd1c136e-6e4e-42ca-a951-4aa5fcdfaa49
title: IEventSubscription3 interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IEventSubscription3
api_type: 
- COM
api_location: 
---

# IEventSubscription3 interface

Stores and retrieves information about event subscriptions. This interface extends the [**IEventSubscription2**](ieventsubscription2.md) interface.

## When to implement

You do not need to implement the **IEventSubscription3** interface. A system-supplied event object class (CLSID\_CEventSubscription) implements **IEventSubscription3**.

## When to use

The [COM+ Events](com--events.md) system uses this interface to obtain information about individual subscriptions.

## Members

The **IEventSubscription3** interface inherits from **IEventSubscription2**. **IEventSubscription3** also has these types of members:

-   [Properties](#properties)

### Properties

The **IEventSubscription3** interface has these properties.



| Property                                                                                  | Access type           | Description                                                |
|:------------------------------------------------------------------------------------------|:----------------------|:-----------------------------------------------------------|
| [**EventClassApplicationID**](ieventsubscription3-eventclassapplicationid.md)<br/> | Read/write<br/> | The application GUID of the event class object.<br/> |
| [**EventClassPartitionID**](ieventsubscription3-eventclasspartitionid.md)<br/>     | Read/write<br/> | The partition GUID of the event class object.<br/>   |
| [**SubscriberApplicationID**](ieventsubscription3-subscriberapplicationid.md)<br/> | Read/write<br/> | The application GUID of the subscriber.<br/>         |
| [**SubscriberPartitionID**](ieventsubscription3-subscriberpartitionid.md)<br/>     | Read/write<br/> | The partition GUID of the subscriber.<br/>           |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[**IEventSubscription2**](ieventsubscription2.md)
</dt> </dl>

 

 




