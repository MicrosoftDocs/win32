---
description: This article provides a checklist that authors of PrintCapabilities documents can use to create a PrintCapabilities document that describes a device.
ms.assetid: 4b8fa1a4-6461-4722-861b-354f206b2a73
title: PrintCapabilities Document Construction Checklist
ms.topic: article
ms.date: 05/31/2018
---

# PrintCapabilities Document Construction Checklist

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

The [Summary of Element Types](summary-of-element-types.md) discusses the various elements that make up a PrintCapabilities document. This section provides a checklist that authors of PrintCapabilities documents can use to create a PrintCapabilities document that describes a device.

1.  Identify all device attributes that contribute to the device configuration. For each such device attribute, determine whether it should be represented as a Feature/Option construct or as a parameter construct.

2.  For each device feature, determine whether it can be represented by a Feature defined in the Print Schema Keywords. If not, you will need to introduce a new privately-defined Feature (and a corresponding name attribute).

    -   For Print Schema Keywords-defined Feature instances, identify each of the available states that this Feature can be set to. Each state corresponds to an Option of the Feature instance. Determine which of these states correspond to Print Schema-defined Option instances associated with this Feature, and which states require a customized Option instance. The [Option Definitions](option-definitions.md) topic presents information on how to construct new Option instances, and how to derive new Option instances from existing Option instances.

    -   For nonstandard Feature instances, identify the characteristics that can be used to distinguish one Option from another. Represent each such characteristic by a ScoredProperty element, and in each Option instance, assign each ScoredProperty a Value that is specific to that Option. Ensure that there are enough ScoredProperty elements so that each Option for a given Feature is unique. Nonstandard Feature and Option instances are by their nature nonportable. That is, another driver will not be able to find any equivalent Feature or Option to match a nonstandard Feature or Option specified in the PrintTicket that your driver creates.

3.  Determine whether any Option must contain ParameterRef elements. For more information, see [Parameter Constructs](parameter-constructs.md) and [Parameter Reference Elements](parameter-reference-elements.md).

4.  For parameters, determine whether one of the ParameterDef instances defined in the Print Schema Keywords is an adequate match. If so, copy the ParameterDef instance from the Print Schema Keywords and adjust the Value of each mutable Property instance for the best fit. If none of the ParameterDef instances in the Print Schema Keywords is an adequate match, create your own ParameterDef instance. For more information, see [Parameters in the PrintCapabilities Document](parameters-in-the-printcapabilities-document.md).

5.  Ensure that all Property and ScoredProperty instances required by the Print Schema Keywords document are present in your PrintCapabilities document, and that they are properly initialized.

6.  Add additional Property and subproperty instances as desired. You may introduce privately-defined Property instances if there are aspects of the device that you need to characterize that are not covered by the Property instances defined in the Print Schema Keywords.

7.  Observe the Namespace Convention for name attributes. This applies to privately-defined name attributes as well as to those defined in the Print Schema Keywords.

8.  Children of the same element type may not nest to a depth of more than 10 elements. This rule applies independently to each type of element that can be defined.

Note that Print Capabilities document XML content MUST be encoded using either UTF-8 or UTF-16.

Note that the set of Feature, Option and ParameterDef instances reported must not change, regardless of the snapshot. The ScoredProperty instances that make up each Option instance and the Value assigned to each ScoredProperty element also must not change. The same holds true for the Property instances that make up each ParameterDef instance.

For a list of additional Property instances that must be supplied to fully define Feature/Option constructs and parameters, see [ParameterDef](parameterdef.md) and [ParameterInit](parameterinit.md). For example, each Feature must specify its user interface (UI) behavior, specifically whether exactly one or multiple Option instances may be selected for each Feature at one time. The Print Schema Keywords document defines these Property instances, where they must appear within the PrintCapabilities document, and which Value instances defined in the Print Schema Keywords are available.

The PrintCapabilities provider is responsible for emitting the appropriate Value for all configuration-dependent Property instances. For example, if the print rate depends on both the color mode and the resolution used, the PrintCapabilities provider must note the color mode and resolution settings specified in the client-supplied PrintTicket, and must report the proper value for the print rate. Note that every ScoredProperty instance must be single valued; its Value instance cannot change when the device configuration changes.

Note also that Property instances defined in the Print Schema Keywords must appear at the location specified there. They cannot appear at arbitrary locations within a PrintCapabilities document. Privately-defined Property instances may appear anywhere, even as subproperties within Schema-defined Property instances.

Note that a functional conflict between settings is defined as two, non-conflicting Print Schema elements that have similar function but are different features. An example would be JobDuplexAllDocumentsContiguously and DocumentDuplex; both represent the duplex function of the device but differ in the application of the function, one applying to the entire job contiguously, and one to documents. In the case two such Elements are specified, precedence is determined by the PrintCapabilities producer and PrintTicket consumer. It is the responsibility of the PrintCapabilities producer to properly indicate constraints between conflicting Elements through the "constrained" attribute. Elements in the public Print Schema that exhibit this semantic conflict are identified in their definition.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



