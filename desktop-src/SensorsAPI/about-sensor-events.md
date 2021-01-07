---
description: The Sensor API can provide event notifications.
ms.assetid: 2400619c-ee9c-4662-ae57-6d4bc317e730
title: About Sensor API Events
ms.topic: article
ms.date: 05/31/2018
---

# About Sensor API Events

The Sensor API can provide event notifications.

When you register to receive events, through either [**ISensor::SetEventSink**](/windows/win32/api/sensorsapi/nf-sensorsapi-isensor-seteventsink) or [**ISensorManager::SetEventSink**](/windows/win32/api/sensorsapi/nf-sensorsapi-isensormanager-seteventsink), you must provide a pointer to a callback interface. You must implement the methods of the callback interface in your code. The Sensor API defines the following callback interfaces:

-   [**ISensorEvents**](/windows/desktop/api/sensorsapi/nn-sensorsapi-isensorevents). Implement this interface to receive events from sensors. Sensors can notify your application about new data, changes in sensor state, sensor disconnection, and custom events defined by the sensor manufacturer.
-   [**ISensorManagerEvents**](/windows/desktop/api/sensorsapi/nn-sensorsapi-isensormanagerevents). Implement this interface to receive events from the sensor manager. The sensor manager can notify your application when a sensor connects, and therefore may be available for use.

You can cancel event notifications by calling [**SetEventSink**](/windows/win32/api/sensorsapi/nf-sensorsapi-isensor-seteventsink) again, this time passing a **NULL** value through the parameter.

## Related topics

<dl> <dt>

[Using Sensor API Events](using-sensor-api-events.md)
</dt> </dl>

 

 
