---
description: Learn about the syntax of the Print Schema, which is expressed in XML syntax and is composed of a small number of element types.
ms.assetid: d67518e3-c379-4a50-aeda-31afaa7f05dd
title: Syntax of the Print Schema
ms.topic: article
ms.date: 05/31/2018
---

# Syntax of the Print Schema

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

The Print Schema is expressed in XML syntax. Readers are therefore expected to be familiar with XML syntax and terms such as element, element tag, element content, attribute, and namespace. The Print Schema Framework is composed of a small number of element types; each element type serves a specific purpose in the technologies built on the Print Schema.

Element types are distinguished by their XML element tag. The Print Schema Framework defines the overall structure and organization of the dependent technologies, by denoting for each element type which element types are allowed as child elements.

Many element types are differentiated from others of the same type by the name attribute, which plays a significant role in the schema. The name attribute serves to identify instances of each element type. The Print Schema Keywords defines a set of values for the name attribute for many of the element types. In most cases, providers can assign their own values to the name attribute. They need only ensure the values are XML QNames qualified with a namespace that is unique to the provider.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



