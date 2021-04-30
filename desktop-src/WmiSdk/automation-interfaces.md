---
description: Makes the interfaces of the Scripting API for WMI available to C/C++ programmers, in place of the COM API versions.
ms.assetid: 18f6cc70-9df1-4d43-a2e0-af03e2f9e2c5
ms.tgt_platform: multiple
title: Automation Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Automation Interfaces

The Automation API makes the interfaces of the Scripting API for WMI available to C/C++ programmers, in place of the COM API versions.

The following table lists WMI objects and how they are used in the Automation API. The cross-references link to the interface documentation for the Scripting API for WMI equivalents.



| Automation Object                                 | Description                                                                                                                 |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| [**ISWbemEventSource**](swbemeventsource.md)     | Retrieves events in conjunction with [**ISWbemServices.ExecNotificationQuery**](swbemservices-execnotificationquery.md).   |
| [**ISWbemLastError**](swbemlasterror.md)         | Provides extended error information when an error occurs.                                                                   |
| [**ISWbemLocator**](swbemlocator.md)             | Obtains a reference to an [**ISWbemServices**](swbemservices.md) object that can access WMI on a particular host computer. |
| [**ISWbemMethod**](swbemmethod.md)               | Contains a single method definition.                                                                                        |
| [**ISWbemMethodSet**](swbemmethodset.md)         | Gets access to a collection of [**ISWbemMethod**](swbemmethod.md) objects.                                                 |
| [**ISWbemNamedValue**](swbemnamedvalue.md)       | Contains a single named value.                                                                                              |
| [**ISWbemNamedValueSet**](swbemnamedvalueset.md) | Gets access to a collection of [**ISWbemNamedValue**](swbemnamedvalue.md) objects.                                         |
| [**ISWbemObject**](swbemobject.md)               | Contains and manipulates a single Common Information Model (CIM) object class or instance.                                  |
| [**ISWbemObjectPath**](swbemobjectpath.md)       | Generates and validates an object path.                                                                                     |
| [**ISWbemObjectSet**](swbemobjectset.md)         | Gets access to a collection of [**ISWbemObject**](swbemobject.md) objects.                                                 |
| [**ISWbemPrivilege**](swbemprivilege.md)         | Sets or clears a privilege.                                                                                                 |
| [**ISWbemPrivilegeSet**](swbemprivilegeset.md)   | Gets access to a collection of [**ISWbemPrivilege**](swbemprivilege.md) objects.                                           |
| [**ISWbemProperty**](swbemproperty.md)           | Used to contain a single CIM property.                                                                                      |
| [**ISWbemPropertySet**](swbempropertyset.md)     | Get access to a collection of [**ISWbemProperty**](swbemproperty.md) objects.                                              |
| [**ISWbemQualifier**](swbemqualifier.md)         | Contains a single class qualifier.                                                                                          |
| [**ISWbemQualifierSet**](swbemqualifierset.md)   | Gets access to a collection of [**ISWbemQualifier**](swbemqualifier.md) objects.                                           |
| [**ISWbemSecurity**](swbemsecurity.md)           | Manages security settings such as Component Object Model (COM) Privilege, AuthenticationLevel, and ImpersonationLevel.      |
| [**ISWbemServices**](swbemservices.md)           | Creates, updates, and retrieves instances or classes.                                                                       |
| [**ISWbemSink**](swbemsink.md)                   | Receives the results of client application asynchronous operations and event notifications.                                 |



 

 

 



