---
description: Describes document conventions for reading WMI Scripting API topics.
ms.assetid: 889e6322-96f6-4a24-a084-e3b7bfa94a40
ms.tgt_platform: multiple
title: Document Conventions for the Scripting API
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Document Conventions for the Scripting API

The [Scripting API for WMI](scripting-api-for-wmi.md) reference uses the following document conventions:

-   Parameter types are defined using a prefix: b (Boolean), str (string), I (integer), obj (Automation object), var (Variant).
-   Optional parameters are placed in square brackets with their default values shown by assignment.
-   In the case of object parameters, the characters after the "obj" prefix indicate the type of object expected.



| Object parameter      | Object type                                          |
|-----------------------|------------------------------------------------------|
| *WbemDatetime*        | [**SWbemDateTime**](swbemdatetime.md)               |
| *WbemEventSource*     | [**SWbemEventSource**](swbemeventsource.md)         |
| *WbemLocator*         | [**SWbemLocator**](swbemlocator.md)                 |
| *WbemMethod*          | [**SWbemMethod**](swbemmethod.md)                   |
| *WbemMethodSet*       | [**SWbemMethodSet**](swbemmethodset.md)             |
| *WbemNamedValueSet*   | [**SWbemNamedValueSet**](swbemnamedvalueset.md)     |
| *WbemObject*          | [**SWbemObject**](swbemobject.md)                   |
| *WbemObjectEx*        | [**SWbemObjectEx**](swbemobjectex.md)               |
| *WbemObjectPath*      | [**SWbemObjectPath**](swbemobjectpath.md)           |
| *WbemObjectSet*       | [**SWbemObjectSet**](swbemobjectset.md)             |
| *WbemPrivilege*       | [**SWbemPrivilege**](swbemprivilege.md)             |
| *WbemPrivilegeSet*    | [**SWbemPrivilegeSet**](swbemprivilegeset.md)       |
| *WbemProperty*        | [**SWbemProperty**](swbemproperty.md)               |
| *WbemPropertySet*     | [**SWbemPropertySet**](swbempropertyset.md)         |
| *WbemQualifier*       | [**SWbemQualifier**](swbemqualifier.md)             |
| *WbemQualifierSet*    | [**SWbemQualifierSet**](swbemqualifierset.md)       |
| *WbemRefreshableItem* | [**SWbemRefreshableItem**](swbemrefreshableitem.md) |
| *WbemRefresher*       | [**SWbemRefresher**](swbemrefresher.md)             |
| *WbemServices*        | [**SWbemServices**](swbemservices.md)               |
| *WbemServicesEx*      | [**SWbemServicesEx**](swbemservicesex.md)           |



 

For example, the following code shows how to name variables for different types of objects:


```VB
strComputerName  ' a string value for a computer name
bStatusFlag  ' a boolean value used for a status
objServices  ' an object value used to store an SWbemServices value
```



 

 



