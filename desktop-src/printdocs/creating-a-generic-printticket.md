---
description: Learn how to construct a generic PrintTicket, in case the PrintCapabilities document for the device is unavailable.
ms.assetid: 1f991b6b-8443-4234-ad46-dc4220e34c5c
title: Creating a Generic PrintTicket
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Generic PrintTicket

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

If the PrintCapabilities document for the device is unavailable, or if the target device is unknown, you should construct a generic PrintTicket. Because there is no PrintCapabilities document that provides a set of Feature and Option elements, or parameters, the supported instances of these element types must be obtained directly from the Print Schema Keywords.

The steps shown in the following list should be used when you create a generic PrintTicket.

1.  Create an empty XML document that contains the PrintTicket root. Assign a namespace prefix to the Print Schema namespace. Specify the Schema version.

2.  Examine the Feature instances in the Print Schema Keywords and determine which of these you want defined in your PrintTicket. Add these Feature instances to your PrintTicket. When you transfer a subfeature, you must transfer the parent Feature, and preserve the parent-child relationship between the Feature and subfeature in the PrintTicket.

    For each Feature instance that you transfer, determine which Option instances are applicable to your PrintTicket. From this set of Option instances, transfer each entire Option instance as it appears in the Print Schema, and then remove any Property instances that are present, with the possible exception of those that have significance to your PrintTicket. Keep all of the ScoredProperty instances, making sure that you preserve their location; they are an intrinsic part of the Option definition.

3.  You may also add Property instances to any ScoredProperty. Property elements are applicable only if the PrintTicket provider explicitly supports their use. Each provider should document the purpose and use of all supported Property instances. Because you have no idea which provider will process the PrintTicket, you might wish to append only the Property instances that are explicitly supported by the system PrintTicket provider.

4.  If the Print Schema Keywords set the SelectionType Property to PickMany for a particular Feature, you may select more than one Option for that Feature, provided that the Option designated as IdentityOption is not one of those selected. IdentityOption in the Print Schema has the same effect as the None option in Postscript PPD files and Unidrv GPD files; it serves as a no-op.

5.  Examine the Print Schema Keywords for ParameterDef instances that should be initialized in your PrintTicket. For each such ParameterDef instance, select the Value to be used in the ParameterInit instance in the PrintTicket. This Value must be of the correct data type, must fall within the range defined in the ParameterDef instance, and must meet all of the other requirements specified in the ParameterDef instance. Use a ParameterInit instance to initialize the parameter to the Value you have selected.

    If you are developing a user interface (UI) component, design your PrintTicket generation methods so that users can enter the Value for the ParameterInit element. In addition, the UI entry method should observe and comply with any input restrictions specified by the associated ParameterDef element.

6.  Examine the contents of each Option instance that appears in the PrintTicket for occurrences of ParameterRef. If a corresponding ParameterInit instance does not already appear in the PrintTicket, follow the previous step to create a ParameterInit instance in the PrintTicket. The purpose of this ParameterInit instance is to initialize the parameter referenced by the ParameterRef instance.

7.  Keep in mind that the device that processes the job might not support every Feature specified in the PrintTicket. Keep in mind also, that a named Feature might be supported, but a specified Option of that Feature might not be. The same caveats apply to parameters. Even if a device supports a named parameter, the Value specified in the ParameterInit instance might not be within the valid range for the device.

8.  Examine the Print Schema Keywords for Property instances that must be present in your PrintTicket. Add a Property instance for each of these to your PrintTicket, and provide a suitable value for it using the Value element type. Make sure that Property instances are located properly within the PrintTicket. Make sure that you consult the PrintTicket Schema rather than the PrintCapabilities Schema.

9.  Examine the optional Property instances defined in the PrintTicket Schema. If there are any such Property instances that should be in your PrintTicket, create them in your PrintTicket.

10. Children of the same element type may not nest to a depth of more than 10 elements. This rule applies independently to each type of element that can be defined.

> [!Note]  
> PrintTicket XML content MUST be encoded using either UTF-8 or UTF-16.

 

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



