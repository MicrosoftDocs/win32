---
description: A management application using the System Registry provider can define classes with properties that represent registry data for particular keys and then stores the classes in the WMI repository.
ms.assetid: e8707a3d-a393-4be0-9e86-297f0af15d99
ms.tgt_platform: multiple
title: Defining Classes for the System Registry Provider
ms.topic: article
ms.date: 05/31/2018
---

# Defining Classes for the System Registry Provider

A management application using the System Registry provider can define classes with properties that represent registry data for particular keys and then stores the classes in the WMI repository. Most of the processes for defining a class for the system registry is identical to defining any other class. However, the System Registry provider requires that you use specific data types and qualifiers.

The following procedure describes how to define a class for the System Registry provider.

**To define a class for the System Registry provider**

1.  Create the class as you would any other class.

    For more information, see [Creating a Class](creating-a-class.md).

2.  Map the appropriate registry data types to the appropriate WMI types.

    The System Registry provider maps the registry data types to specific WMI data types. For more information, see [Mapping a Registry Data Type to a WMI Data Type](mapping-a-registry-data-type-to-a-wmi-data-type.md).

3.  Use the required qualifiers to define the location of the Registry provider and the location of the appropriate registry key.

    The System Registry provider uses three qualifiers to define the location of various classes, providers, and registry entries. For more information, see [Defining a Registry Class With Qualifiers](defining-a-registry-class-with-qualifiers.md).

 

 



