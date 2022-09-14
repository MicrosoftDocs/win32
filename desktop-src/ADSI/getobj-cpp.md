---
title: GETOBJ.CPP
description: In the example provider component, appears a code example used to find and bind objects is in Getobj.cpp. Supported routines are listed in the following table.
ms.assetid: d202e5ec-27b5-4809-a7fa-4a2e39c65295
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# GETOBJ.CPP

In the example provider component, appears a code example used to find and bind objects is in Getobj.cpp. Supported routines are listed in the following table.



| Item                                | Description                                                                                                                                                                                                                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **RelativeGetObject**               | Gets an object relative to a given ADsPath.                                                                                                                                                                                                                                                       |
| **GetObject**                       | Calls **ADsObject** (Parse.cpp) to verify the path syntax, validates that the path has the right provider token and validate the object type. If no errors exist, create an instance of the correct type of object, and retrieve a pointer to the object [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. |
| **BuildADsPathFromDSPath**          | Built an ADsPath string from the native directory path.                                                                                                                                                                                                                                           |
| **BuildDSTreeNameFromADsPath**      | Use the ADsPath to create a possible tree directory path for the native directory path.                                                                                                                                                                                                           |
| **BuildDSPathFromADsPath**          | Uses ADsPath and DSPathName.                                                                                                                                                                                                                                                                      |
| **BuildADsParentPath**              | Build the ADsPath to the parent for this object.                                                                                                                                                                                                                                                  |
| **GetNamespaceObject**              | Validate and [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) an example namespace object.                                                                                                                                                                                                           |
| **ValidateNamespaceObject**         | Verify that the namespace object matches the current provider name.                                                                                                                                                                                                                               |
| **ValidateProvider**                | Validate provider name (case-sensitive).                                                                                                                                                                                                                                                          |
| **GetSchemaObject**                 | Validate and open the appropriate schema object type. Then create the correct one, and retrieve the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface pointer on it.                                                                                                                                        |
| **ValidateSchemaObject**            | Verify that it is a valid schema object type.                                                                                                                                                                                                                                                     |
| **ValidateObjectType**              | Verify that the object type exists in the schema.                                                                                                                                                                                                                                                 |
| **BuildSampleDSRootRDNFromADsPath** | Build the ADsPath to the root node for the example provider component.                                                                                                                                                                                                                            |
| **BuildDSPathFromADsPath**          | Uses ADsPath, DSRootRDN, and DSPathName.                                                                                                                                                                                                                                                          |



 

 

 