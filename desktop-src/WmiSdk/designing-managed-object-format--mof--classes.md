---
description: A WMI provider consists of a Managed Object Format (MOF) file and DLL file. The MOF file defines the classes for which the provider implementation supplies data.
ms.assetid: 20ef6b88-2aaa-4e86-bc4a-bebc34069672
ms.tgt_platform: multiple
title: Designing Managed Object Format (MOF) Classes
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Designing Managed Object Format (MOF) Classes

A [*WMI provider*](gloss-p.md) consists of a Managed Object Format (MOF) file and DLL file. The MOF file defines the classes for which the provider implementation supplies data.

The MOF class definitions are compiled by the [**mofcomp**](mofcomp.md) utility and stored in the [*WMI repository*](gloss-w.md), also known as the Common Information Model (CIM) repository. A less common way to create classes is through the methods of the [COM API for WMI](com-api-for-wmi.md).

> [!Note]  
> To ensure that all your WMI class definitions for managed objects are restored to the [*WMI repository*](gloss-w.md) if WMI has a failure and restarts, use the [**\#pragma autorecover**](pragma-autorecover.md) preprocessor instruction in your MOF file.

 

The following sections are discussed in this topic:

-   [Defining the Objects to Manage](#defining-the-objects-to-manage)
-   [Defining Properties or Methods](#defining-properties-or-methods)
-   [Relating Objects to Each Other](#relating-objects-to-each-other)
-   [Related topics](#related-topics)

## Defining the Objects to Manage

After you identify the part of your enterprise to manage, define the objects to manage. The definition must include the required data, and allow you to implement the relevant business rules accurately. You can define objects at a granular level, but it is best to decide between the level of detail contained in the definition, and the need to provide enough detail to be useful. Shortcuts early in the process may save time, but may be cause more work in the future.

The CIM Tutorial at the Distributed Management Task Force (DMTF) website contains excellent information about the design process. For more information, see [www.dmtf.org](https://www.dmtf.org/).

Consider the following factors when you develop and implement a schema design:

-   Qualifiers

    Qualifiers provide information about how to describe classes, objects, properties, methods, and parameters; and they are applied to class and property definitions. In MOF code, qualifiers are enclosed in brackets and may include \[key\] or \[association\]. For more information, see [Adding a Qualifier](adding-a-qualifier.md) and [WMI Qualifiers](wmi-qualifiers.md).

-   Namespace

    A namespace is a logical unit to group classes and objects, and control scope and visibility. Typically, a namespace contains a set of classes and objects that represent managed objects in a specific environment. For more information, see [Creating Hierarchies Within WMI](creating-hierarchies-within-wmi.md).

-   Object

    A modeled object might be a physical or logical element of the schema. For example, you can model a physical disk drive such as a hard disk drive, or a logical disk that can be a partition on a physical disk. A design that uses a class to model a physical disk drive, and then extends that class to model a logical disk is more extensible than one that attempts to create a separate class for each type of disk.

-   Data

    Data may be dynamic or static. If the data is dynamic, you must create a class provider for it.

    To enable the user to modify data, you must determine whether or not you want a property to be directly writable or modifiable only by using a method that the user calls.

## Defining Properties or Methods

Generally, a WMI class property is similar to a property in a C++ class. If the only actions your code implements for the piece of data is to get the value or set the value, then the data should be defined as a property of the WMI class.

A WMI method generally performs an action that changes the state of a managed object. For example, if the action is to enable or disable the operation of a hardware object, then a method is probably preferable to creating a read/write property. You may decide also to create a property that displays the state of the hardware.

When you create a class or an instance, you can include comments. Use this technique to document your class or explain your programming techniques. For more information, see [Creating a Comment](creating-a-comment.md). In addition, you can add data to qualify the purpose of a data object. For more information, see [Adding a Qualifier](adding-a-qualifier.md).

## Relating Objects to Each Other

There are two ways to relate objects to each other: by creating separate objects and an association object that relates them, or by embedding one object in the other. CIM does not support embedded objects, so to be CIM-compliant you must use the first method. However, WMI supports embedded objects so use either method to represent a relationship between objects. You can find examples of embedded objects in the [Win32 Classes](/windows/desktop/CIMWin32Prov/win32-provider). For example, [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor) has the embedded object [**Win32\_ACE**](/previous-versions/windows/desktop/secrcw32prov/win32-ace), which has another embedded object, [**Win32\_Trustee**](/previous-versions/windows/desktop/secrcw32prov/win32-trustee).

Consider the following when deciding how to represent relationships between objects:

-   If an instance is useful by itself, then an association works best. For example, [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process) and [**Win32\_UserAccount**](/windows/desktop/CIMWin32Prov/win32-useraccount). For more information, see [Declaring an Association Class](declaring-an-association-class.md).
-   If an instance does not exist outside of the parent object, an embedded object works best. For example, [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor) and [**Win32\_ACE**](/previous-versions/windows/desktop/secrcw32prov/win32-ace). For more information, see [Embedding Objects in a Class](embedded-objects.md).

## Related topics

<dl> <dt>

[Developing a WMI Provider](developing-a-wmi-provider.md)
</dt> <dt>

[Providing Data to WMI](providing-data-to-wmi.md)
</dt> <dt>

[MOF Data Types](mof-data-types.md)
</dt> </dl>

 

 
