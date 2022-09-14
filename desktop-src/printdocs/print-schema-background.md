---
description: The Print Schema addresses opaqueness and ambiguity in communication between components of the print subsystem and between print subsystem and applications.
ms.assetid: 193dd600-7cbb-4f4e-bb7d-7f7117e9d16a
title: Print Schema Background
ms.topic: article
ms.date: 05/31/2018
---

# Print Schema Background

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

The Print Schema is intended to address the problems of opaqueness and ambiguity associated with internal communication between the components of the print subsystem, and external communication between the print subsystem and applications.

The current print subsystem interaction with applications and hardware vendors' plug-ins uses the binary, index-based DEVMODE structure and binary DevCaps. Settings made by each component are largely opaque to other components, preventing portability of settings between devices or even between different driver versions on the same device. Furthermore, PrintCapabilities cannot easily be leveraged by client applications without either proprietary knowledge of the device or using the driver user interface (UI). In addition to these limitations, in a broader sense there is no well-defined language to describe general device attributes, PrintCapabilities, device configurations, or job formatting. The Print Schema and its related technologies are designed to address these limitations, providing a consistent, unambiguous and extensible method of communication of settings and capabilities in a consolidated and logical manner.

The conceptual foundations of the Print Schema Keywords and the Print Schema Framework are consistency, lack of ambiguity and extensibility. Consistency is achieved through the use of the Print Schema Keywords and Print Schema Framework as the building blocks for the communication between next-generation printing components. Applications, the Microsoft Windows printing subsystem, and IHV plug-ins and drivers interact using this common mechanism. These keywords, their structure and their meaning will be well-defined by the public schema. This prevents ambiguity in the meaning of a particular keyword, and prevents redundant or duplicate keywords. All components can rely on using a particular keyword to convey a certain intent and have that intent be well-understood by the recipient. Extensibility is vital to be the longevity of the Print Schema Keywords, ensuring that the public schema is a dynamic entity. The structure also allows private extensions, which grants IHVs the flexibility to innovate as desired, keeping in mind future inclusion of a private keyword into the public schema is essential to preserving consistency and preventing ambiguity.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



