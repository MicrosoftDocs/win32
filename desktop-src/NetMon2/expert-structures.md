---
description: Expert helper functions provided by Network Monitor and common helper functions use the structures described in the following table.
ms.assetid: 3c49dd0a-836f-43f1-b383-357e8ba6545f
title: Expert Structures
ms.topic: article
ms.date: 05/31/2018
---

# Expert Structures

Expert helper functions provided by Network Monitor and common helper functions use the structures described in the following table.



| Structure                                              | Description                                                                                            |
|--------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**CONFIGUREDEXPERT**](configuredexpert.md)           | Associates an expert DLL with its configuration.                                                       |
| [**EXPERTCONFIG**](expertconfig.md)                   | Provides raw configuration data.                                                                       |
| [**EXPERTENUMINFO**](expertenuminfo.md)               | Provides information about the expert DLL. Network Monitor uses the information.                       |
| [**EXPERTFRAMEDESCRIPTOR**](expertframedescriptor.md) | Provides information about a frame.                                                                    |
| [**EXPERTSTARTUPINFO**](expertstartupinfo.md)         | Provides startup information about the expert.                                                         |
| [**EXPERTSTATUS**](expertstatus.md)                   | Provides the current status of a running expert.                                                       |
| [**FILTEROBJECT**](filterobject.md)                   | Defines the display filter characteristics for an expert.                                              |
| [**NMEVENTDATA**](nmeventdata.md)                     | Provides information about a line displayed in the expert viewer.                                      |
| [**NMCOLUMNINFO**](nmcolumninfo.md)                   | Provides information that defines a column in the Event Viewer.                                        |
| [**NMCOLUMNVARIANT**](nmcolumnvariant.md)             | Provides a container for all possible data inserted into a column on one line in the Event Viewer.     |
| [**NMCOLUMNTYPE**](nmcolumntype.md)                   | The entry point in the variant that indicates which element of the union to use, and how to format it. |



 

Network Monitor also provides export functions (helper functions that the expert can call) and enumerations.



| For information about                                          | See                                                                          |
|----------------------------------------------------------------|------------------------------------------------------------------------------|
| Export Functions that provide entry points to your expert DLL. | [Expert DLL Export Functions](expert-dll-export-functions.md)               |
| Helper functions that can be called by experts and parsers.    | [Expert and Parser Common Functions](expert-and-parser-common-functions.md) |
| Helper functions that are called only by experts.              | [Expert Functions](expert-functions.md)                                     |
| Enumerations used by expert structures and functions.          | [Expert Enumerations](expert-enumerations.md)                               |



 

 

 



