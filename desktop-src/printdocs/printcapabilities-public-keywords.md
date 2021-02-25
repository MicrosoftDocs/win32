---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 7f08747f-f7ff-4381-b2b9-1917e4708ee3
title: PrintCapabilities Public Keywords
ms.topic: article
ms.date: 05/31/2018
---

# PrintCapabilities Public Keywords

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

The following section specifies both user configurable elements and parameter definitions which may be applicable to a PrintCapabilities document.

## User Configurable Elements Usage

User Configurable Elements represent Print Schema Public Keywords which may appear in either a PrintCapabilities document or a PrintTicket. They are intended to represent configurable device attributes supported by a specific device or communicate print setting intent by an application or user.

User Configurable Elements may reference Parameter Reference Elements. For more information, please refer to [Parameter Reference Elements](parameter-reference-elements.md) section.

## Parameter Definitions Usage

Parameters definitions take the form of ParameterDef element types in a Print Capabilities document. ParameterDef element types are initialized in a PrintTicket using the ParameterInit element type. The value of the parameter will be specified using the ParameterInit element. A user configurable keyword may reference a parameter definition using the ParameterRef element type. For more information, please refer to [Parameter Constructs](parameter-constructs.md) section.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



