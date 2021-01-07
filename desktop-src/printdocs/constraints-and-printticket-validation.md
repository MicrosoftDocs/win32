---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: f4c66812-8782-4a85-8a74-3505c4e73e56
title: Constraints and PrintTicket Validation
ms.topic: article
ms.date: 05/31/2018
---

# Constraints and PrintTicket Validation

This topic is not current. For the most current information, see the [Print Schema Specification](https://www.microsoft.com/whdc/xps/printschema.mspx).

As discussed in the PrintCapabilities Schema section, some of the possible configuration outcomes expressed in a PrintCapabilities document are invalid for the device. Configurations that are invalid are said to contain constraint conflicts (a term used in the world of PPD/GPD files). In order to prevent constraint conflicts, PrintTicket providers must support a PrintTicket validation operation that clients use to perform validation on their PrintTicket. This operation should detect whether the specified configuration can occur on the device. If the configuration cannot occur (because the Feature and Option elements specified do not exist in the current device, or because the configuration is constrained), the operation should modify the input PrintTicket so that it contains valid, unconstrained settings. The operation might remove or validate other information in the PrintTicket as well. Note that when a constraint conflict is encountered, the validation code must change the setting of one of the device attributes in order to avoid the constraint conflict. [Option Definitions](option-definitions.md) suggests that a device driver defined scoring process should be used to determine which device attribute should be changed in order to best preserve the user's original intent. The validation code might hardcode the scoring process to favor one device attribute over another, or it might use information supplied by a particular Property instance in the PrintTicket to guide resolution. Because there is no Property defined in the Print Schema Keywords that allows clients to specify the relative priority of each device attribute, any private PrintTicket Property elements used for this purpose are likely to be ignored by other PrintTicket providers.

## Related topics

<dl> <dt>

[Print Schema Specification](https://www.microsoft.com/whdc/xps/printschema.mspx)
</dt> </dl>

 

 



