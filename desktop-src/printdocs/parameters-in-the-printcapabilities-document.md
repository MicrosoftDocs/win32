---
description: Understand parameters in the PrintCapabilities document. This topic isn't current. For the most current information, see the Print Schema Specification.
ms.assetid: d317d052-c207-412a-896e-09cb57b0dd5f
title: Parameters in the PrintCapabilities Document
ms.topic: article
ms.date: 05/31/2018
---

# Parameters in the PrintCapabilities Document

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

As discussed in [Parameter Reference Elements](parameter-reference-elements.md), ParameterInit elements may be referenced from within Option instances, but the parameter construct also has a use that is independent of this type of element.

An example of a device configuration attribute that is well suited for parameter representation is CopyCount. The allowed values for this device configuration attribute can be easily and concisely defined without listing each of them explicitly. Although it would be possible, though tedious, to list each CopyCount value in its own Option, some device configuration attributes simply cannot be represented using a Feature/Option construct. As an example, consider a device that accepts a text string that is then used to produce a virtual watermark on each output page. The set of all possible text strings cannot easily be explicitly enumerated, but the text string can easily be described using a ParameterDef element.

The Print Schema Keywords document defines a number of commonly used parameter constructs, but PrintCapabilities providers are free to define additional ones of their own. However, these privately-defined parameter constructs are not portable to other devices, due to the fact that a PrintCapabilities document provided by another party does not define such a parameter construct. Whether schema-defined or privately-defined, the ParameterDef instance must be present in the PrintCapabilities document before the parameter is recognized and used by clients. These parameters are referred to as *designated parameters*.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



