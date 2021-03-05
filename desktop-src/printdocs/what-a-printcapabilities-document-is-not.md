---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 87a897cd-d3aa-488a-b129-9837d3500d0d
title: What a PrintCapabilities Document Is Not
ms.topic: article
ms.date: 05/31/2018
---

# What a PrintCapabilities Document Is Not

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

It is worthwhile to list some of the functionality and information the PrintCapabilities document is not intended to provide.

A PrintCapabilities document:

-   Does not represent multivalued (configuration-dependent) data.

    Each PrintCapabilities document is constructed for a specific configuration. No Property or ScoredProperty in the document can have a Value that depends on the particular configuration. In the initial schema version, the PrintCapabilities provider must process the input PrintTicket and create a PrintCapabilities document that contains Property values appropriate for the configuration specified in the PrintTicket.

-   Does not contain constraint information.

    The PrintCapabilities document does not indicate which configurations are allowed and which are not allowed. In the initial schema version, the PrintCapabilities provider must store any information needed to validate configurations, supply a method that validates the input PrintTicket, and return a corrected PrintTicket in the event that the specified PrintTicket violates one or more constraints.

-   Does not contain dynamic device information.

    There is too much overhead involved in constructing the PrintCapabilities document for it to be used to hold rapidly changing status information, such as ink levels, paper remaining in each tray, or paper jam status.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



