---
title: Dynamic Linking
description: Graphics developers sometimes create large, general-purpose shaders that can be used by a wide variety of scene items.
ms.assetid: 2f5f7852-0f0a-4fad-a412-9a0d634c73b6
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Dynamic Linking

Graphics developers sometimes create large, general-purpose shaders that can be used by a wide variety of scene items. At runtime, the shader conditionally runs code appropriate for the given situation. Unfortunately, these large, general-purpose shaders use general-purpose registers (GPRs) inefficiently, and can be much slower than smaller, more targeted shaders.

Shader model 5 addresses this performance problem by introducing dynamic shader linking. Dynamic linking separates shader code fragments by using interfaces and virtual functions and allows the application to select the fragment to use at draw time. This improves performance by binding only the shader code needed and not the entire large, general-purpose shader.

## In This Section



| Item                                                                                                                                                                                                                                                                                                                         | Description                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| <span id="Storing_Variables_and_Types_for_Shaders_to_Share"></span><span id="storing_variables_and_types_for_shaders_to_share"></span><span id="STORING_VARIABLES_AND_TYPES_FOR_SHADERS_TO_SHARE"></span>[Storing Variables and Types for Shaders to Share](storing-variables-and-types-for-shaders-to-share.md)<br/> | Describes the class linkage object for storing variables and types that multiple shaders can share.<br/> |
| <span id="Interfaces_and_Classes"></span><span id="interfaces_and_classes"></span><span id="INTERFACES_AND_CLASSES"></span>[Interfaces and Classes](overviews-direct3d-11-hlsl-dynamic-linking-class.md)<br/>                                                                                                         | Describes using HLSL interfaces and classes to implement dynamic linking.<br/>                           |
| <span id="Interface_Usage_Restrictions"></span><span id="interface_usage_restrictions"></span><span id="INTERFACE_USAGE_RESTRICTIONS"></span>[Interface Usage Restrictions](overviews-direct3d-11-hlsl-dynamic-linking-expression.md)<br/>                                                                            | Describes restrictions on the use of interfaces in shader code.<br/>                                     |



 

## Related topics

<dl> <dt>

[HLSL](overviews-direct3d-11-hlsl.md)
</dt> </dl>

 

 





