---
description: In WMI, a class is an object that describes some aspect of an enterprise, such as a special type of disk drive.
ms.assetid: 06b75910-f126-48b6-8e43-4a9ed4661732
ms.tgt_platform: multiple
title: Creating a WMI Class
ms.topic: article
ms.date: 05/31/2018
---

# Creating a WMI Class

In WMI, a class is an object that describes some aspect of an enterprise, such as a special type of disk drive. After you have created a class definition, write your provider DLL to supply instances of the class, property data, and execute methods defined for the class. Scripts and applications can then obtain data or control the device. For more information, see [Developing a WMI Provider](developing-a-wmi-provider.md).

> [!Note]  
> To ensure that all your WMI class definitions for managed objects are restored to the [*WMI repository*](gloss-w.md) if WMI has a failure and restarts, use the [**\#pragma autorecover**](pragma-autorecover.md) statement preprocessor instruction in your MOF file.

 

## Base Class

A base class represents some general concept. For example, the [**CIM\_CDROMDrive**](/windows/desktop/CIMWin32Prov/cim-cdromdrive) class represents all types of CD-ROM drives in WMI, and contains general properties that describe all kinds of CD-ROM drives. For more information, see [Creating a Base Class](creating-a-base-class.md).

A derived class inherits properties and methods from another class. A derived class usually represents a specific case of a base class. For example, the [**Win32\_CDROMDrive**](/windows/desktop/CIMWin32Prov/win32-cdromdrive) class represents a CD-ROM drive on a Windows system. The **Win32\_CDROMDrive** class is based on and inherits many of properties from [**CIM\_CDROMDrive**](/windows/desktop/CIMWin32Prov/cim-cdromdrive). However, **Win32\_CDROMDrive**, like other derived classes, can have additional properties that make the derived class unique. For more information, see [Creating a Derived Class](creating-a-derived-class.md).

## Properties and Methods

Creating a class means defining the properties that describe that class. You can also define methods that manipulate the object represented by the class.

Generally, a property represents an aspect of the object, such as a serial number for a device or a size in bytes for a process, while a method represents an action that changes the state or behavior of the device or logical entity.

Each class must have at least one key property. While a class may have multiple keys, you cannot create an instance of a class with more than 256 keys.

## Related topics

<dl> <dt>

[Designing Managed Object Format (MOF) Classes](designing-managed-object-format--mof--classes.md)
</dt> </dl>

 

 
