---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 2377763b-9b3b-49ec-ab6c-476b8009ddcb
title: Responsibilities of Consumers of the PrintCapabilities Document
ms.topic: article
ms.date: 05/31/2018
---

# Responsibilities of Consumers of the PrintCapabilities Document

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

Consumers of PrintCapabilities documents have certain obligations they must uphold before they can use a PrintCapabilities document. The following requirements apply to clients of a PrintCapabilities document.

-   They must not reject or fail to process any syntactically valid PrintCapabilities; that is, any PrintCapabilities document that conforms to the PrintCapabilities Schema.

-   They must be able to work around the unexpected presence or absence of privately-defined content. This includes privately-defined content that appears within instances of Print Schema-defined elements.

-   They must be able to work around optional Print Schema content that is absent.

-   They must be aware of when to request a new document.

    -   Values of Property instances are configuration-dependent (hence, snapshot-dependent). You must update the snapshot when you access a Property instance.

    -   Feature, Option and ScoredProperty instances that are to be copied to a PrintTicket are by definition static. That is, they are not (and must not be) dependent on the device configuration. If you access any instances of these types, you do not need to obtain a new PrintCapabilities document when the configuration changes.

-   Consumers of PrintCapabilities that are user interface (UI) clients must be able to use information in a PrintCapabilities document to construct a user interface and to construct a valid PrintTicket from the user selections. This includes knowing which ParameterInit instances must be specified, and validating those instances that are specified.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



