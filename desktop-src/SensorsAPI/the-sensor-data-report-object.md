---
description: The sensor data report object contains sensor data.
ms.assetid: 8a812860-338b-4ada-8f5f-ea693e038941
title: The Sensor Data Report Object
ms.topic: article
ms.date: 05/31/2018
---

# The Sensor Data Report Object

The sensor data report object contains sensor data.

For a sensor to be useful, it must provide meaningful data. The amount and frequency of data generation varies from sensor to sensor. For example, a sensor that detects whether a door is open would generate a small amount of **Boolean** data, while a motion sensor might continuously generate multiple data items. To standardize the way your program receives data, the Sensor API uses the sensor data report object.

You can access the information in a sensor data report through the [**ISensorDataReport**](/windows/desktop/api/sensorsapi/nn-sensorsapi-isensordatareport) interface. This interface lets you retrieve the data report's time stamp so that you can determine whether the information in the report is useful. You can retrieve the data itself in two ways: as an individual data field value or as a set of values. To retrieve data as an individual value, call the [**GetSensorValue**](/windows/win32/api/sensorsapi/nf-sensorsapi-isensordatareport-getsensorvalue) method. To retrieve multiple values, call the [**GetSensorValues**](/windows/win32/api/sensorsapi/nf-sensorsapi-isensordatareport-getsensorvalues) method.

You specify the type of data, or data fields, that you want to retrieve from the report by using a **PROPERTYKEY** constant. Property keys for data fields of common sensor types are defined in Sensors.h.

 

 
