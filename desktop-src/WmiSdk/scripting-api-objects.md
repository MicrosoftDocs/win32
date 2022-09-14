---
description: The Scripting API for WMI reference describes each scripting object using a specific syntax. For an explanation of this syntax, see Document Conventions for the Scripting API.
ms.assetid: 91bc0fad-1a4b-4b48-b5a0-1a6502d2ab26
ms.tgt_platform: multiple
title: Scripting API Objects
ms.topic: article
ms.date: 05/31/2018
---

# Scripting API Objects

The Scripting API for WMI reference describes each scripting object using a specific syntax. For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

The following table lists WMI scripting objects and how they are used.



| Object                                               | Description                                                                                                                                                                                                                                            |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SWbemDateTime**](swbemdatetime.md)               | Constructs and parses CIM [datetime](date-and-time-format.md) values.                                                                                                                                                                                 |
| [**SWbemEventSource**](swbemeventsource.md)         | Retrieves events in conjunction with [**SWbemServices.ExecNotificationQuery**](swbemservices-execnotificationquery.md).                                                                                                                               |
| [**SWbemLastError**](swbemlasterror.md)             | Provides extended error information when an error occurs.                                                                                                                                                                                              |
| [**SWbemLocator**](swbemlocator.md)                 | Obtains an [**SWbemServices**](swbemservices.md) object that can get access to WMI on a particular host computer.                                                                                                                                     |
| [**SWbemMethod**](swbemmethod.md)                   | Contains a single WMI method definition.                                                                                                                                                                                                               |
| [**SWbemMethodSet**](swbemmethodset.md)             | Gets a collection of [**SWbemMethod**](swbemmethod.md) objects.                                                                                                                                                                                       |
| [**SWbemNamedValue**](swbemnamedvalue.md)           | Contains a single named value.                                                                                                                                                                                                                         |
| [**SWbemNamedValueSet**](swbemnamedvalueset.md)     | Gets access to a collection of [**SWbemNamedValue**](swbemnamedvalue.md) objects.                                                                                                                                                                     |
| [**SWbemObject**](swbemobject.md)                   | Contains and manipulates a single WMI object class or instance.                                                                                                                                                                                        |
| [**SWbemObjectEx**](swbemobjectex.md)               | Extends the functionality of [**SWbemObject**](swbemobject.md). This object adds the [**Refresh**](swbemrefresher-refresh.md) method for [**SWbemRefresher**](swbemrefresher.md) objects.                                                           |
| [**SWbemObjectPath**](swbemobjectpath.md)           | Generates and validates an object path.                                                                                                                                                                                                                |
| [**SWbemObjectSet**](swbemobjectset.md)             | Gets access to a collection of [**SWbemObject**](swbemobject.md) objects.                                                                                                                                                                             |
| [**SWbemPrivilege**](swbemprivilege.md)             | Sets or clears a privilege.                                                                                                                                                                                                                            |
| [**SWbemPrivilegeSet**](swbemprivilegeset.md)       | Gets access to a collection of [**SWbemPrivilege**](swbemprivilege.md) objects.                                                                                                                                                                       |
| [**SWbemProperty**](swbemproperty.md)               | Contains a single WMI property.                                                                                                                                                                                                                        |
| [**SWbemPropertySet**](swbempropertyset.md)         | Gets access to a collection of [**SWbemProperty**](swbemproperty.md) objects.                                                                                                                                                                         |
| [**SWbemQualifier**](swbemqualifier.md)             | Contains a single property qualifier.                                                                                                                                                                                                                  |
| [**SWbemQualifierSet**](swbemqualifierset.md)       | Gets access to a collection of [**SWbemQualifier**](swbemqualifier.md) objects.                                                                                                                                                                       |
| [**SWbemRefresher**](swbemrefresher.md)             | Collects and updates object property values in one operation.                                                                                                                                                                                          |
| [**SWbemRefreshableItem**](swbemrefreshableitem.md) | Represents a single refreshable element in an [**SWbemRefresher**](swbemrefresher.md) object, such as a property.                                                                                                                                     |
| [**SWbemSecurity**](swbemsecurity.md)               | Manages security settings such as Component Object Model (COM) [**Privileges**](swbemsecurity-privileges.md), [**AuthenticationLevel**](swbemsecurity-authenticationlevel.md), and [**ImpersonationLevel**](swbemsecurity-impersonationlevel.md).   |
| [**SWbemServices**](swbemservices.md)               | Creates, updates, and retrieves instances or classes.                                                                                                                                                                                                  |
| [**SWbemServicesEx**](swbemservicesex.md)           | Extends the functionality of [**SWbemServices**](swbemservices.md). This object adds the [**Put**](swbemservicesex-put.md) and [**PutAsync**](swbemservicesex-putasync.md) methods to allow a class or instance to be saved to multiple namespaces. |
| [**SWbemSink**](swbemsink.md)                       | Receives the results of asynchronous operations and event notifications, which are used by client applications.                                                                                                                                        |



 

 

 



