---
description: This section covers the use of ambient light sensor data, and how user interface features and program content can be optimized for many lighting conditions.
ms.assetid: c84075b2-ae41-4915-a0f6-3a9c017ae0b8
title: Creating Light-Aware User Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Creating Light-Aware User Interfaces

This section covers the use of ambient light sensor data, and how user interface features and program content can be optimized for many lighting conditions.

Ambient light sensors expose data that can be used to determine various aspects of the lighting conditions where the sensor is located. Ambient light sensors can expose the overall brightness of an environment (illuminance) and other aspects of the surrounding light, such as chromaticity or color temperature.

Computers can be more useful in several ways when the system is responsive to lighting conditions. These include controlling the brightness of the computer display (a new, fully supported feature in Windows 7), automatically adjusting the lighting level of illuminated keyboards, and even brightness control for other lights (such as button illumination, activity lights, and so on).

End-user programs can also benefit from light sensors. Programs can apply a theme that is appropriate for a particular lighting condition, such as a specific outdoor theme and indoor theme. Perhaps the most important aspect of light sensor integration with programs is readability and legibility optimizations that are based on lighting conditions.

The Sensor API enables you to create such programs. Consider the following scenario.

## Scenario: Using your Laptop to Navigate to a Restaurant

Suppose you want to use your computer to help you navigate to a new restaurant. You start out in your house, looking up the address of the restaurant and planning your route. The following screen shot shows how your navigation program could optimize its UI to show detailed information in indoor lighting conditions.

![ui designed for indoor lighting.](images/nav-normal.png)

When you go outside to your car, you encounter direct sunlight, which makes the laptop's screen difficult to read. The following screen shot shows how your program could alter its UI to maximize legibility/readability in direct light. In this view, much of the detail has been omitted and contrast is maximized.

![ui designed for direct lighting conditions.](images/nav-contrast.png)

As you get closer to the restaurant, evening approaches and it gets dark outside. In the following screen shot, the UI for the navigation program has been optimized for low-light viewing. By using darker colors overall, this UI is easy to glance at in the dark car.

![ui designed for low-light viewing.](images/nav-lowlight.png)

In the remainder of this section, you will explore some things that you can do to optimize your programs for various lighting conditions and how you can use the Sensor API to help enable light-aware UI.

## In This Section

-   [Fundamentals of Light-Aware User Interfaces](fundamentals-of-light-aware-user-interfaces.md)
-   [Examples of Light-Aware User Interfaces](examples-of-light-aware-user-interfaces.md)
-   [Optimizing the User Experience](optimizing-the-user-experience.md)
-   [Understanding and Interpreting Lux Values](understanding-and-interpreting-lux-values.md)
-   [Using Light Sensor Data](handling-data-from-multiple-light-sensors.md)

 

 



