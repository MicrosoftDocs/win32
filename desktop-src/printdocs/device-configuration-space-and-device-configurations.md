---
title: Device Configuration Space
description: A device's configuration space is the set of all possible values that can be assigned to all of the attributes of the device.
ms.assetid: 598299c3-159f-4cad-b6a5-d282cd5bb4a1
ms.topic: article
ms.date: 05/31/2018
---

# Device Configuration Space and Device Configurations

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

A device's *configuration space* is the set of all possible values that can be assigned to all of the attributes of the device. The two most important reasons to describe the configuration space of the device in the PrintCapabilities are as follows.

1.  The information contributes significantly to an increased understanding of the device's capabilities. This information makes it easier for a client of the PrintCapabilities to generate user interface (UI) elements, which makes it easier for the end user to select a particular configuration to process a job. By providing more details of the device's capabilities to the application and ultimately to the end user, the user's printing intent can be more effectively fulfilled.

2.  Certain device properties presented in the PrintCapabilities might be dependent on the particular configuration selected by the client.

Some information should not be incorporated into the PrintCapabilities. This includes information that does not affect the way a job is created, does not impose constraints on the way a job is created, nor otherwise affects the device properties. For example, a device might be able to report status information, such as the set of jobs waiting to be processed. This information has no effect on the information needed to format the job, nor does it provide any indication of the capabilities available in the device. For this reason, this type of information does not need to be present in the PrintCapabilities.

## Device Constraints

Many devices do not support all possible configurations in the configuration space due to a constraint on the device. For example, a device can be constrained from performing duplex printing on transparent media. A constraint can represent a physical limitation: some media types are simply too rigid to travel through certain paper paths in the device, and so cannot be placed in some input slots or be routed to some output bins. Currently it is the responsibility of the PrintCapabilities or PrintTicket provider to validate the configuration represented by the input PrintTicket, to verify that it does not represent an invalid configuration. If the configuration is invalid, the PrintCapabilities or PrintTicket provider should modify the configuration in such a way that it becomes valid.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



