---
description: PrintCapabilities providers must support a minimum set of capabilities, which are implied by the PrintTicket/PrintCapabilities Provider Interface.
ms.assetid: 92e9bce1-d58e-40a4-9721-832d7c3bc2b2
title: Responsibilities of PrintCapabilities Providers
ms.topic: article
ms.date: 05/31/2018
---

# Responsibilities of PrintCapabilities Providers

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

PrintCapabilities providers must support a minimum set of capabilities, which are implied by the PrintTicket/PrintCapabilities Provider Interface. These capabilities are listed here.

-   They must follow the direction of the propagate??XML attribute, when it appears in the appropriate context and contains a valid value for that context.

-   They must generate a PrintCapabilities document that conforms to the PrintCapabilities Schema and satisfies the requirements specified in the Print Schema.

-   They must be able to recognize a valid PrintTicket.

-   They must be able to interpret a PrintTicket and understand the specific configuration it represents.

-   They must be able to determine whether that configuration contains constraint conflicts.

-   They must be able to modify an invalid or conflicting PrintTicket by making the least significant change necessary to make it both valid and without conflicts.

-   They must be able to generate a PrintCapabilities document for a particular device configuration.

-   They must be able to generate a default configuration or PrintTicket.

-   They must be able to generate a PrintCapabilities document that corresponds to the default configuration.

-   They must implement an Option-scoring process defined by the device driver capable of determining the closeness of match between two Option instances that belong to the same Feature. This algorithm is used in the PrintTicket validation process.

In addition to the foregoing requirements, the PrintCapabilities document must contain valid and correct values for each XML attribute (for example, constrained) of each Option.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



