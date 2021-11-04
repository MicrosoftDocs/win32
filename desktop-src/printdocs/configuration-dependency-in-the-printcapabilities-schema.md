---
title: PrintCapabilities Configuration Dependency 
description: Configuration dependencies refer to the fact that some elements can be altered or even deleted from one PrintCapabilities document to the next.
ms.assetid: 9b1f3f49-2a4a-4413-9708-a430011314e6
ms.topic: article
ms.date: 05/31/2018
---

# Configuration Dependency in the PrintCapabilities Schema

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

The PrintCapabilities Schema closely parallels the Print Schema Framework, in terms of the elements used and the general structure expressed by parent and child elements. Configuration dependencies, which pertain specifically to the PrintCapabilities, are listed here as an extension to the general framework. Configuration dependencies refer to the fact that some elements, including their contents, can be altered or even deleted from one PrintCapabilities document to the next, as a result of dependencies on the configuration. Even if a parent element is required to be independent of the configuration, its child elements might have dependencies. Such dependencies are expressed using \*Switch/\*Case constructs in GPD files.

As an example of a configuration dependency, consider the values associated with each Property in the PrintCapabilities document. Each PrintCapabilities document can differ in the Property instances that are defined and in the Value instances assigned to those Property instances.



| Element Type                                                                                                                                                                             | Configuration Dependency                                                                                                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Feature <br/> Option<br/> ParameterInit<br/> ParameterRef<br/> PrintCapabilities<br/> PrintTicket<br/> Property<br/> ScoredProperty<br/> | These elements must not have configuration dependencies.<br/>                                                                                                                                                           |
| ParameterDef <br/>                                                                                                                                                                 | ParameterDef elements and elements contained within them to any nesting level must not have any configuration dependencies.<br/>                                                                                        |
| Property <br/>                                                                                                                                                                     | Property elements may have configuration dependencies, except when they appear within ParameterDef elements.<br/>                                                                                                       |
| Value <br/>                                                                                                                                                                        | Value elements that appear within ScoredProperty elements must not have any configuration dependencies. Value elements that appear within a Property element may have arbitrary dependencies on the configuration.<br/> |



 

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




