---
description: The sensor object represents a particular sensor.
ms.assetid: b969a153-d957-4323-bafe-6f8d62b0a627
title: The Sensor Object
ms.topic: article
ms.date: 05/31/2018
---

# The Sensor Object

The sensor object represents a particular sensor.

The Sensor API represents each sensor as a sensor object. You can work with a particular sensor object through its [**ISensor**](/windows/desktop/api/sensorsapi/nn-sensorsapi-isensor) interface. This interface enables you to:

-   Retrieve metadata about the sensor, such as its ID, type, or friendly name.
-   Retrieve information about the specific data the sensor can provide.
-   Retrieve the data, synchronously.
-   Retrieve state information, such as whether the sensor is ready.
-   Specify which events your program will receive.
-   Specify the callback interface that the Sensor API can use to provide your program with event notifications.

 

 



