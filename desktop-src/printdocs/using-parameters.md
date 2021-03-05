---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 4a596604-8a0d-4971-96f3-643727312cfc
title: Using Parameters
ms.topic: article
ms.date: 05/31/2018
---

# Using Parameters

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

In addition to properly scoring an Option that contains ParameterRef instances (see [Referencing Parameters](referencing-parameters.md)), PrintCapabilities or PrintTicket providers and clients must be prepared to handle the following situations involving parameters.

User interface (UI) clients must prompt the user to provide parameter initializers (values for ParameterInit elements) for designated parameters at the appropriate time so that the appropriate ParameterInit elements are inserted into the PrintTicket. UI clients must be able to distinguish the two types of parameters, unconditionally mandatory, and conditionally mandatory, and must be able to handle each type appropriately. For an unconditionally mandatory parameter, the UI must ensure that a ParameterInit element is provided for this type of parameter. For a conditionally mandatory parameter, the UI must provide a ParameterInit value if the parameter is referenced by an Option that is selected in the PrintTicket. The Mandatory status of a parameter is specified in a ParameterDef instance. For more information, see [ParameterDef and ParameterInit Elements](parameterdef-and-parameterinit-elements.md). UI clients should validate user-supplied ParameterInit values to verify that they satisfy the requirements specified in the ParameterDef instance.

PrintTicket providers should also check the ParameterInit instances supplied by the PrintTicket to verify that all needed parameters are present, and that they satisfy the requirements specified in the ParameterDef instance. The validation code should supply reasonable defaults in the event that ParameterInit values are invalid or missing. Notice that a ParameterDef permits a default value to be supplied for this purpose. Also, if there are constraints involving the parameters, for example, "if *CopyCount* is larger than N, then do not use a small capacity input bin," the PrintTicket validation code should detect this constraint and modify the PrintTicket to avoid activating the constraint.

If there is any dependency of the PrintCapabilities on the parameters specified in the PrintTicket, PrintCapabilities providers must monitor the ParameterInit values and produce an appropriate PrintCapabilities document.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



