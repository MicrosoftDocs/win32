---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 2f6c51a3-003c-4d68-9e4d-9be5d325a477
title: Connecting PrintCapabilities with the Print Schema
ms.topic: article
ms.date: 05/31/2018
---

# Connecting PrintCapabilities with the Print Schema

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

The general PrintCapabilities Schema covers the structure, purpose, and use of the various element types. It specifies the name attribute that is used to define specific instances of each element type. It specifies that PrintCapabilities authors may use instances of elements defined by the Print Schema Keywords, or they may introduce their own privately-defined instances, as long as these privately-defined instances are defined in a namespace that is clearly identified as their own. (PrintCapabilities authors may also use instances previously defined in another private namespace.)

The Print Schema Keywords document defines the specific instances of each element type available for use in PrintCapabilities documents and in PrintTickets. It also documents their purpose and usage. The Print Schema Keywords document also defines instances of several element types, as follows:

-   Property and subproperty instances that reside at the root of the PrintCapabilities document

    -   These elements describe the various aspects and capabilities of the device, and provide a common vocabulary for describing devices.

-   Property and subproperty instances that are children of Feature elements

    -   These elements describe various aspects related to a specific Feature.

-   Property and subproperty instances that are children of Option elements

    -   These elements describe the various aspects and capabilities of the device that are dependent on the Option selected for a specific Feature. These could be replaced by Property instances located at the root of the PrintCapabilities document, but offer additional convenience in some cases. For more information, see [Adding Property Instances](adding-property-instances.md).

<!-- -->

-   ScoredProperty instances

    -   ScoredProperty instances define the language that is used to characterize an Option. The ScoredProperty instances defined in the Print Schema Keywords make it possible for Option instances written by many different parties for many devices to be portable, and to be understood by any other device driver or PrintCapabilities or PrintTicket provider.

-   ScoredProperty Value instances

    -   These Value instances are provided for the same reason that ScoredProperty instances are provided.

-   Feature instances

    -   Each Option must belong to a specific Feature, thereby requiring the Feature itself to be defined.

-   ParameterDef instances

    -   A Print Schema Keywords-supplied ParameterDef instance also defines a Value for each Property contained in it. The PrintCapabilities provider is free to modify the Value instances for those Property instances that can be changed. For information about which Property instances can be changed, and which cannot be changed (are immutable), see [ParameterDef and ParameterInit Elements](parameterdef-and-parameterinit-elements.md).

It is important to note the PrintCapabilities Schema does not name any Option instances. Option instances are characterized solely by their ScoredProperty instances taken as a whole. A common misconception is that using the 'name' attribute to define an Option identifies Option instances, but this is incorrect. Option elements are not required to be unique for sibling Option instances, nor is using the 'name' attribute to define an Option required.

The Print Schema Keywords document defines a standard namespace to which all instance name attributes in the PrintCapabilities and PrintTicket schemas belong. All element type tags and XML Attributes used by the element types also belong to this namespace.

For each instance defined in the PrintCapabilities Schema, the PrintCapabilities Schema specifies both the name attribute and the location of the instance. The provider and client must preserve both when using this instance in their PrintCapabilities document or PrintTicket.

The Print Schema Keywords document designates some instances as mandatory. These instances must appear in every PrintCapabilities document and must be properly initialized with valid Values. All instances in the Print Schema Keywords that are not designated as mandatory are optional.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



