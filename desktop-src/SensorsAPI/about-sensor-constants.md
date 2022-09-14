---
description: About Sensor Constants
ms.assetid: ba85ccd8-5251-4e47-84da-80899fe84c39
title: About Sensor Constants
ms.topic: article
ms.date: 05/31/2018
---

# About Sensor Constants

The Windows Sensor and Location platform uses constants in many ways. The platform defines different constants that you can use in your sensor driver code. Sensor manufacturers can define custom constants. You can find the definitions of platform-defined constants in the Sensors.h file. For detailed information about platform-defined sensor constants, see [Constants](constants.md).

### Sensor and Data Organization

The platform organizes sensors and data in the following ways.

-   Categories represent broad classes of sensor devices. Categories let you group sensors that are likely to provide similar kinds of information, or are otherwise related in some way. Each category is represented by a **GUID** constant. For example, sensors that report latitude and longitude coordinates belong to the location sensor category. This is representented by the SENSOR\_CATEGORY\_LOCATION constant.
-   Sensor types represent specific kinds of sensors. Each sensor type fits into a particular category. Two sensors of different types can belong to the same category or different categories. Each sensor type is represented by a **GUID** constant. For example, a global positioning system sensor would be identified by the SENSOR\_TYPE\_LOCATION\_GPS constant. However, a sensor that provides the current location by using an IP address would be identified by the SENSOR\_TYPE\_LOCATION\_LOOKUP constant. However, both sensors would belong to the location sensor category.
-   Data types represent specific kinds of information that the sensor can provide. Sensor data types can contain the actual measurement value, such as altitude; information about the units used to express the data, such as meters; and reference points for the data, such as sea level. Each data type is represented by a **PROPERTYKEY** constant. For example, the data type that represents altitude above sea level, in meters, would be identified by the SENSOR\_DATA\_TYPE\_ALTITUDE\_SEALEVEL\_METERS constant.
-   When reporting data, a value is said to be contained in a data field, and a collection of related data fields make up a data report. Data reports are packaged together by using the [IPortableDeviceValues](/previous-versions//ms740012(v=vs.85)) interface. Each data report must contain at least one valid data field and a time stamp that identifies when the data report was created. Time stamps are represented by the SENSOR\_DATA\_TYPE\_TIMESTAMP constant.

### Other Constants

Your program must use other constants, also. These constants include the following:

-   Sensor properties, such as SENSOR\_PROPERTY\_DESCRIPTION. Usually, these constants are used to describe a sensor. Some sensor properties must be provided by the sensor, some properties can be set by client applications, and some must always return the same value from the sensor. The [**Sensor Properties**](sensor-properties.md) reference section provides this information for each property.
-   Event constants, such as SENSOR\_EVENT\_STATE\_CHANGED. Event constants include **GUID**s, which represent types of events, and **PROPERTYKEY**s, which represent event parameter types. You will use these constants for method calls, such as [**ISensor::SetEventInterest**](/windows/win32/api/sensorsapi/nf-sensorsapi-isensor-seteventinterest) and [**ISensor::GetEventInterest**](/windows/win32/api/sensorsapi/nf-sensorsapi-isensor-geteventinterest).

### Custom Constants

Sensor manufacturers can define custom constants. For example, a sensor can belong in a category not defined by the platform. Before you can use a sensor that defines custom constants, the sensor manufacturer must publish the values, for example by publishing a header file. For more information, see the documentation that is provided with the sensor.

 

 
