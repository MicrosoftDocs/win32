---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 487f294f-dfe0-48f8-9077-06c55c3af8f1
title: Creating a Device-Specific PrintTicket
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Device-Specific PrintTicket

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

A device-specific PrintTicket targets a particular device and is therefore not generally portable across multiple devices.

The steps shown in the following list should be used when you create a device-specific PrintTicket.

1.  Obtain a PrintCapabilities document containing only the relevant Feature instances for the device. Request a default PrintCapabilities document. This does not require you to specify an input PrintTicket because the device attributes (Feature and Option instances and parameters) that are used to construct the PrintTicket are independent of the configuration.

2.  Create an empty XML document containing the PrintTicket root. Assign a namespace prefix to the Print Schema namespace, and assign prefixes for all other namespaces that will be used by the PrintTicket. Specify the PrintTicket Schema version.

3.  You may define settings in the PrintTicket for every Feature and ParameterDef instance reported in the PrintCapabilities document, or only those of interest to you. If a partial PrintTicket is presented to the PrintTicket interface, defaults are automatically provided for omitted Feature and ParameterDef instances during PrintTicket validation.

4.  Examine the PrintCapabilities document for Feature instances and determine which of these you want defined in your PrintTicket. Add these Feature instances to the PrintTicket, but do not transfer the contents of the Feature instances to your PrintTicket. If you transfer a subfeature, the parent Feature must also be transferred, and the parent-child relationship must be preserved in the PrintTicket.

    For each Feature that you transfer, determine which Option instances are applicable to your PrintTicket. Transfer the entire Option as defined in the PrintCapabilities document, and then remove any Property instances that are present. The Property instances are used within PrintCapabilities documents, but serve no purpose in the PrintTicket. Keep all of the ScoredProperty instances, making sure that you preserve their location; they are an intrinsic part of the Option definition.

5.  You may also add Property instances to any ScoredProperty instance. Property instances are used only if the PrintTicket provider explicitly supports their use. Each provider should document the purpose and use of all supported Property instances. Note that during validation, any Property instances contained within an Option instance are stripped off, unless the namespace of the Property is recognized by the target PrintCapabilities or PrintTicket provider, and a candidate Option is found in the PrintCapabilities document whose ScoredProperty instances perfectly match those defined in the reference Option.

6.  If the Print Schema Keywords set the SelectionType Property to PickMany for a particular Feature, you may select more than one Option for that Feature, provided that the Option designated as IdentityOption is not one of those selected. IdentityOption in the Print Schema has the same effect as the None option in Postscript PPD files and Unidrv GPD files; it serves as a no-op.

7.  Examine the PrintCapabilities document for ParameterDef instances that should be set in your PrintTicket. For each such ParameterDef instance, select a Value to be used in the ParameterInit instance in the PrintTicket. This Value must be of the correct data type and must fall within the range defined in the ParameterDef instance, and must meet all of the other requirements specified in the ParameterDef instance. Use a ParameterInit instance to initialize the parameter to the Value you have selected.

8.  Examine the contents of each Option instance that appears in the PrintTicket for occurrences of ParameterRef instances. If a corresponding ParameterInit instance does not already appear in the PrintTicket, follow the previous step to create a ParameterInit instance in the PrintTicket. The purpose of this ParameterInit instance is to initialize the parameter referenced by the ParameterRef instance.

9.  Keep in mind that constraint conflicts might prevent the device from applying the configuration you have specified in the PrintTicket. If necessary, the validation process modifies the configuration defined in the PrintTicket to one that is free of conflicts.

10. Examine the Print Schema Keywords for Property instances that must be present in your PrintTicket. Add a Property instance to your PrintTicket for each that is required, and provide a suitable value for it using the Value element type. Make sure that Property instances are located properly within the PrintTicket.

11. Examine the optional Property instances in the PrintTicket Schema. If there are any such Property instances that should be in your PrintTicket, create them in your PrintTicket.

12. You may also add privately-defined Property instances at the root level, or to any Feature, Option, or Property instance. Note however, that these privately-defined Property instances are stripped off during validation, unless the namespace they belong to is recognized by the target PrintCapabilities or PrintTicket provider. In addition, Property instances that appear anywhere within an Option instance are stripped off during validation, unless the PrintCapabilities document contains an Option that is a perfect match. Two Option instances are a perfect match if every ScoredProperty in one Option instance has a corresponding ScoredProperty in the other, and the Values of the ScoredProperty instances are the same. Consult the PrintTicket provider's Private Schema for a list of recognized private Property instances and their uses.

13. Children of the same element type may not nest to a depth of more than 10 elements. This rule applies independently to each type of element that can be defined.

> [!Note]  
> PrintTicket XML content MUST be encoded using either UTF-8 or UTF-16.

 

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



