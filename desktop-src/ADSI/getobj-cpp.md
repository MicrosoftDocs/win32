---
title: GETOBJ.CPP
description: In the example provider component, appears a code example used to find and bind objects is in Getobj.cpp. Supported routines are listed in the following table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: d202e5ec-27b5-4809-a7fa-4a2e39c65295
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GETOBJ.CPP

In the example provider component, appears a code example used to find and bind objects is in Getobj.cpp. Supported routines are listed in the following table.



| Item                                | Description                                                                                                                                                                                                                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **RelativeGetObject**               | Gets an object relative to a given ADsPath.                                                                                                                                                                                                                                                       |
| **GetObject**                       | Calls **ADsObject** (Parse.cpp) to verify the path syntax, validates that the path has the right provider token and validate the object type. If no errors exist, create an instance of the correct type of object, and retrieve a pointer to the object [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) interface. |
| **BuildADsPathFromDSPath**          | Built an ADsPath string from the native directory path.                                                                                                                                                                                                                                           |
| **BuildDSTreeNameFromADsPath**      | Use the ADsPath to create a possible tree directory path for the native directory path.                                                                                                                                                                                                           |
| **BuildDSPathFromADsPath**          | Uses ADsPath and DSPathName.                                                                                                                                                                                                                                                                      |
| **BuildADsParentPath**              | Build the ADsPath to the parent for this object.                                                                                                                                                                                                                                                  |
| **GetNamespaceObject**              | Validate and [**CoCreateInstance**](https://msdn.microsoft.com/en-us/library/ms686615(v=VS.85).aspx) an example namespace object.                                                                                                                                                                                                           |
| **ValidateNamespaceObject**         | Verify that the namespace object matches the current provider name.                                                                                                                                                                                                                               |
| **ValidateProvider**                | Validate provider name (case-sensitive).                                                                                                                                                                                                                                                          |
| **GetSchemaObject**                 | Validate and open the appropriate schema object type. Then create the correct one, and retrieve the [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) interface pointer on it.                                                                                                                                        |
| **ValidateSchemaObject**            | Verify that it is a valid schema object type.                                                                                                                                                                                                                                                     |
| **ValidateObjectType**              | Verify that the object type exists in the schema.                                                                                                                                                                                                                                                 |
| **BuildSampleDSRootRDNFromADsPath** | Build the ADsPath to the root node for the example provider component.                                                                                                                                                                                                                            |
| **BuildDSPathFromADsPath**          | Uses ADsPath, DSRootRDN, and DSPathName.                                                                                                                                                                                                                                                          |



 

 

 




