---
description: The Common Information Model (CIM) is an extensible, object-oriented data model that contains information about different parts of an enterprise.
ms.assetid: 3e619cb7-18a9-40ff-82fe-c10eb5090a93
ms.tgt_platform: multiple
title: Common Information Model
ms.topic: article
ms.date: 05/31/2018
---

# Common Information Model

The Common Information Model (CIM) is an extensible, object-oriented data model that contains information about different parts of an enterprise. The [CIM](https://www.dmtf.org/standards/cim) is a cross-platform standard maintained by the Distributed Management Task Force ([DMTF](https://www.dmtf.org/)). Through WMI, a developer can use the CIM to create classes that represent hard disk drives, applications, network routers, or even user-defined technologies, such as a networked air conditioner. By viewing and making changes to a CIM class, a manager can control different aspects of the enterprise. For example, a manager could query a CIM class instance representing a desktop workstation. The manager could then run a script to modify the CIM workstation instance. WMI would translate any change to the workstation CIM class instance into a change to the actual workstation.

The CIM is a language-independent programming model that uses object-oriented techniques to describe an enterprise. Using three levels of parent/child inheritance, the CIM can describe both general and specific aspects of an enterprise. The CIM also uses a technique called "association" to link different parts of the enterprise model together, and uses schemas to distinguish different management environments.

The CIM is designed to present a consistent view of logical and physical objects in a management environment. The CIM represents managed objects using an object-oriented construct called a "class." Like a C++ or COM class, a CIM class can include properties to describe data and methods to describe behavior. Like a set of COM classes, the CIM is not tied to any platform. However, WMI includes an extension to the CIM that describes the Microsoft Windows operating system platforms.

The CIM defines three levels of classes:

-   Core

    Core classes represent managed objects that apply to all areas of management. These classes provide a basic vocabulary for analyzing and describing managed systems. The [**\_\_Parameters**](--parameters.md) and [**\_\_SystemSecurity**](--systemsecurity.md) classes are examples of core classes.

-   Common

    Common classes represent managed objects that apply to specific management areas. However, common classes are independent from a particular implementation or technology. Common classes are an extension of the core classes. The [**CIM\_UnitaryComputerSystem**](/windows/desktop/CIMWin32Prov/cim-unitarycomputersystem) class is an example of a common class.

-   Extended

    Extended classes represent managed objects that are technology-specific additions to the common classes. An extended class typically applies to a specific platform, such as UNIX or the Microsoft Win32 environment. The [**Win32\_ComputerSystem**](/windows/desktop/CIMWin32Prov/win32-computersystem) class is an example of an extended class.

A developer can derive a class from another class. A derived class represents a special case of the parent class, and inherits all of the properties and methods of the parent. For example, [**Win32\_ComputerSystem**](/windows/desktop/CIMWin32Prov/win32-computersystem) inherits from [**CIM\_UnitaryComputerSystem**](/windows/desktop/CIMWin32Prov/cim-unitarycomputersystem). Inheritance relationships may be determined using the system properties **\_\_Derivation**, **\_\_Dynasty**, and **\_\_SuperClass**. The **\_\_Derivation** system property is an array of strings listing the entire chain of inheritance up to and including the root class, which is also included in **\_\_Dynasty**. The **\_\_SuperClass** system property shows the immediate parent of the current class.

WMI also supports associations. An association is a relationship between two or more different WMI classes. For example, a running workstation usually has a processor. The WMI association class [Win32\_ComputerSystemProcessor](/windows/desktop/CIMWin32Prov/win32-computersystemprocessor) associates the workstation class [**Win32\_ComputerSystem**](/windows/desktop/CIMWin32Prov/win32-computersystem) with the processor class [**Win32\_Processor**](/windows/desktop/CIMWin32Prov/win32-processor). However, an association class does not have to tie two dependent classes together. In fact, the primary purpose of an association class is to show relationships between classes that are not necessarily dependent on each other. For more information, see [Declaring an Association Class](declaring-an-association-class.md).

Finally, WMI supports the concept of schemas. In the context of WMI, a schema is a group of classes that describe a particular management environment. The Microsoft Windows Software Development Kit (SDK) uses two schemas: the CIM schema and the Win32 schema. The CIM schema class names begin with [CIM\_](cimclas.md), and the Win32 schema class names begin with [**Win32\_**](/windows/desktop/CIMWin32Prov/win32-provider). The CIM schema contains the definitions for the core and common classes, while the Win32 schema contains the definitions for the extended classes that are common to the Win32 environment. However, a third-party vendor can create their own schemas to describe vendor-specific requirements. Because schemas are designed to be infinitely extensible, a developer can always add new classes to describe new managed objects in an existing environment. For simplicity, however, most vendors choose to create schemas that inherit properties from the CIM or Win32 schemas.

 

 
