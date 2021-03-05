---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 055e502d-631f-49d2-8577-65396373d478
title: Representing Attributes as Feature/Option Constructs or as Parameters
ms.topic: article
ms.date: 05/31/2018
---

# Representing Attributes as Feature/Option Constructs or as Parameters

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

The author of a PrintCapabilities document defines device attributes that make up the configuration. In the PrintCapabilities document, the author can choose to represent a device attribute either as a Feature/Option construct or as a parameter construct.

If a device attribute has a relatively small number of possible states that do not fall into any sort of obvious pattern, a Feature/Option construct is usually the better choice. For example, if the allowed values for the PageMediaSize device attribute are the values Letter, Legal, A4ISO, Tabloid, and Envelope10, a Feature/Option construct would be the better choice for representation. Because of the difficulty and ambiguity associated with expressing the allowable values without explicit enumeration, the parameter construct is not appropriate for the PageMediaSize attribute.

If a device attribute can be represented by a range of integers, parameter representation is usually the better choice, especially for ranges that include many values. For example, if the CopyCount device attribute for a particular model of printer can range from 1 through 99,999, then this attribute should be categorized as a parameter, by defining a ParameterDef instance. Assign values to the MinValue and MaxValue standard Property instances of the ParameterDef element to define the range of values for the JobCopyCount attribute. Because of the large number of values that must be explicitly listed as Option elements, Feature/Option representation is not appropriate for the JobCopyCount device attribute.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



