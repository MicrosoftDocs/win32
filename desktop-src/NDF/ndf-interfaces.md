---
title: NDF Interfaces
description: The following interfaces can be used to extend the functionality of Microsoft Helper Classes that are identified as extensible.
ms.assetid: '55e58eb8-d04e-4398-a892-8c343a88adc1'
---

# NDF Interfaces

The following interfaces can be used to extend the functionality of Microsoft Helper Classes that are identified as extensible. Although this functionality is not required for most applications, it can provide more specific diagnoses and resolutions in some cases.

> [!Note]  
> These interfaces and their associated methods are for developers implementing their own third party helper classes that extend NDF functionality.

 



| Interface Name                                                 | Description                                                                                                              |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [**INetDiagHelper**](inetdiaghelper.md)                       | Called by the NDF for most activities that occur during a diagnosis.                                                     |
| [**INetDiagHelperEx**](inetdiaghelperex.md)                   | Called by the NDF to capture and provide information associated with diagnoses and resolution of network-related issues. |
| [**INetDiagHelperInfo**](inetdiaghelperinfo.md)               | Called by the NDF to validate that it has required information                                                           |
| [**INetDiagHelperUtilFactory**](inetdiaghelperutilfactory.md) | Reserved for system use.                                                                                                 |



 

 

 




