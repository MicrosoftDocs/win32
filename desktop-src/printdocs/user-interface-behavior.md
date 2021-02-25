---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: dc19a568-3673-4061-b19a-50d5df0485d0
title: User Interface Behavior
ms.topic: article
ms.date: 05/31/2018
---

# User Interface Behavior

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

Assume that you are creating a PrintCapabilities client that reads in a PrintCapabilities document and selects one or more Options from each Feature and uses those to construct a PrintTicket that specifies the configuration that is to be used to process the Job. For each Feature of interest, the client must examine each Option, and decide whether that Option is appropriate for the task at hand. For an Option that is not parameterized, it can be evaluated by accessing the Value of each ScoredProperty. In the case of a nonparameterized media size Option, the client determines whether the width and height dimensions of the media reported in each Option match the dimensions required.

In the case of the parameterized Option, the client must access the ParameterDef instance that is indicated in the ParameterRef instance contained in one of the ScoredProperty instances. The ParameterDef typically defines the range of values allowed for the parameter, as well as the units (inches, mm, and so on) represented by the value. If the required dimensions fall within the range of values permitted for each of the parameters, the client has the additional task of initializing the parameters (by means of a ParameterInit instance) in the PrintTicket. This is a particularly important task. For example, a PrintTicket should not specify a custom media size without specifying the dimensions of the media, because the resulting PrintTicket will be ambiguous and ill-defined.

A similar set of circumstances must be handled if the client is a user interface. The user interface typically displays the values of the ScoredProperty instances defined for each Option. For clarity, it is essential to display the allowed range and units for the parameters in a parameterized Option. In addition, if the user selects the parameterized Option, the user interface (UI) must prompt the user to enter the value to be used to initialize each parameter. Finally, the UI must compose a PrintTicket that reflects all of the user's selections.

For the details of PrintTicket construction and specification of parameter initialization, see [Creating a Device-Specific PrintTicket](creating-a-device-specific-printticket.md). For information about dereferencing ParameterRef instances and interpreting ParameterDef instances, see [Using Parameters](using-parameters.md).

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



