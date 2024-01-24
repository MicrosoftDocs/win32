---
description: These articles provide more detailed information on the meaning and usage of the Print Schema element types.
ms.assetid: 05c7fd07-1c32-409d-8ca5-820038af3440
title: Print Schema Framework
ms.topic: article
ms.date: 05/31/2018
---

# Print Schema Framework

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

This section provides more detailed information on the meaning and usage of the Print Schema element types. The main focus of the initial version of the Print Schema Framework is to represent configurations and capabilities of device attributes. At a high level, this framework offers two different styles of describing a device attribute: as a Feature/Option construct, or as a parameter construct. If a device attribute has a small number of available values or states, then the attribute should be characterized as a Feature with the allowed values or states referred to as Option elements. Conversely, if a device attribute has a large number of available values or states and the set of all possible values is easily defined without resorting to explicit enumeration, the device attribute should be characterized as a parameter. (A parameter is defined by means of a ParameterDef element, and a parameter instance is initialized by means of a ParameterInit element.) Property elements are used within Feature/Option and parameter constructs to provide a finer level of differentiation.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



