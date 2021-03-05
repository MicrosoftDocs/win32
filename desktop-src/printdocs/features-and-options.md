---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 8084fa15-85e5-4c8d-b585-8c349482a6eb
title: Features and Options
ms.topic: article
ms.date: 05/31/2018
---

# Features and Options

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

Feature/Option and parameter constructs are used in a PrintCapabilities document to represent device attributes that contribute to the definition of the device configuration. For an example of a Feature/Option construct, consider a printing device that is capable of printing in several resolutions. The device attribute that defines the resolution can be represented as a Feature instance, with each of the possible output resolution values represented as an individual Option instance. One Option instance can represent a resolution of 300 dpi, another can represent a resolution of 600 dpi, and so on.

It should be noted that the Print Schema requires that the list of Feature, Option, and ParameterDef instances reported in each PrintCapabilities document must remain constant, independent of the configuration. This allows configurations and dependencies on configurations to be expressed in an unambiguous way. The implication of this requirement is that every Feature and subfeature must have a well-defined setting, regardless of the setting of any other Feature or subfeature. Therefore, each subfeature must have an Option that is equivalent to a no-op (an Off, Disabled, or None setting), that is automatically selected for all subfeatures when the user selects the no-op Option in the parent Feature. Conversely, when one of the subfeatures is set to an enabled Option, the parent Feature and other associated subfeatures are also enabled. In the meantime, the PrintTicket provider must ensure (during PrintTicket validation) that settings for all Feature and subfeature instances are defined, regardless of the device configuration, and that the subfeature settings are consistent with the settings of the parent Feature. This ensures that the device is not given an inconsistent PrintTicket where some subfeatures indicate that, for example, stapling is enabled, but other subfeatures indicate that stapling is disabled.

Note that PrintCapabilities authors are not required to utilize the nesting capabilities of Feature elements. If they prefer, they can present all Feature instances in a flat structure, as siblings of each other. Note also that a nested collection of Feature instances can be flattened simply by moving all of the subfeatures out to the root level. The only precaution that must be taken is to ensure that the name attributes of these Feature instances are unique.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



