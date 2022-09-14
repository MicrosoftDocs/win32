---
description: Sensor API
ms.assetid: a6ea76e6-9721-453a-a657-96f53660e09d
title: Sensor API
ms.topic: article
ms.date: 05/31/2018
---

# Sensor API

## Purpose

Windows 7 includes native support for sensors, which are devices that can measure physical phenomena such as temperature or location. This documentation describes the Sensor API, which enables applications to get and use data from sensors in a standardized way.

As humans, we rely on our senses to provide us with information about the world around us. When we create machines to take on some of our work, we add sensor mechanisms so the machines can respond appropriately to changing conditions.

For example, automobile engines typically use a variety of sensors. These sensors are monitored by an onboard computer that continuously adjusts settings, such as engine timing, to maximize power and efficiency. A television may use an ambient light sensor to adjust the brightness of the picture to match changing room conditions. Even something as simple as a doorbell button acts as a rudimentary sensor to detect a human presence at the door.

While the purely mechanical doorbell fulfills its purpose, the information provided by complex sensors becomes far more powerful when it is combined with software. Modern sensors can provide a lot of data very quickly, and in a variety of formats, so software provides a natural mechanism for making sense of sensor data.

Today, software developers can write programs that use sensors, but a lack of standardization makes programming for sensors an arduous task. After a sensor-based program is completed, it is usually forever dependent on a particular type of hardware. Using one or more vertical solutions to enable deployment of a software-based system has limited the integration of sensors with computer hardware and, until now, Windows-based computers have been no exception.

Windows 7 includes native support for sensors, expanded by a new development platform for working with sensors, including location sensors, such as GPS devices. The Windows Sensor and Location platform provides a standard way for device manufacturers to expose sensor devices to software developers and consumers, while providing developers with a standardized application programming interface (API) for working with sensors and sensor data.

Sensors are devices or mechanisms that can measure physical phenomena, provide descriptive data, or provide information about the state of a physical object or environment. Computers can make use of built-in sensors, sensors that are connected through wired or wireless connections, or sensors that provide data through a network or the Internet.

The Sensor API provides a standard way to programmatically access data that sensors provide. The Sensor API standardizes:

-   Sensor categories, types, and properties.
-   Data formats for standard sensor types.
-   COM interfaces for working with sensors and collections of sensors.
-   Event mechanisms for asynchronously receiving sensor data.

The Sensor API also enables you to define custom sensor categories, types, properties, data formats, and events.

## Developer audience

The Sensor API provides its functionality through a set of COM interfaces. This documentation assumes that you have a working knowledge of programming using the C++ programming language, and you have a basic understanding of how to use COM objects and interfaces. For the sake of brevity, many code examples in this documentation (as well as in the code samples) use Active Template Library (ATL) objects to implement COM functionality.

## In this section

-   [Getting Started](getting-started.md)
-   [About the Sensor API](about-the-sensor-api.md)
-   [Sensor API Programming Guide](sensor-api-programming-guide.md)
-   [Sensor API Programming Reference](sensor-api-programming-reference.md)

 

 



