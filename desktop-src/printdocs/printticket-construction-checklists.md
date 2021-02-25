---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: ed53d1a8-d302-4855-9858-0f37dfbbd1d3
title: PrintTicket Construction Checklists
ms.topic: article
ms.date: 05/31/2018
---

# PrintTicket Construction Checklists

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

This section demonstrates how the author of a PrintTicket client can use the element types defined in the Print Schema Framework to create a PrintTicket that describes intents for a device. The PrintTicket can be generic (not tied to a specific device), or it can be device-specific. The semantics of the PrintTicket are presented in greater detail. In addition, this section contains an overview of concepts and terminology that are covered in more depth in subsequent sections.

There are two fundamentally different approaches to constructing a PrintTicket. Either approach can be used.

-   Target the PrintTicket to an unknown or generic device by [Creating a Generic PrintTicket](creating-a-generic-printticket.md).

    If your primary objective is to preserve the end user's intent, you might want to take this approach, by constructing and storing an unvalidated generic PrintTicket with the document.

-   Target the PrintTicket to a specific device, by [Creating a Device-Specific PrintTicket](creating-a-device-specific-printticket.md).

    If you are more interested in taking advantage of all of the features offered by a particular device, you might want to take this approach, by constructing a PrintTicket for the specific device and storing the validated PrintTicket with the document.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



