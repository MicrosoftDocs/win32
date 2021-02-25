---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 360325dc-51b5-44d5-981b-b69f7d6c82fd
title: Print Schema-Related Technologies
ms.topic: article
ms.date: 05/31/2018
---

# Print Schema-Related Technologies

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

For the .NET Framework 3.0, Windows Vista, and later releases, the PrintCapabilities and PrintTicket technologies extend the capabilities of the Print Schema to enable a richer printing experience.

## PrintCapabilities

The PrintCapabilities technology is a method of publishing user controllable settings description of per-job attributes and settings. PrintCapabilities are published in an eXtensible Markup Language (XML) document called the PrintCapabilities document, consisting of terms defined in the Print Schema Keywords and private extensions. The PrintCapabilities document can be thought of as a "snapshot" of the user configurable state current device configuration as well as a description of possible configurations. Devices (or device drivers) generate a PrintCapabilities document (the snapshot) of their current set of configurable options when queried by clients, which can be either applications or the printing subsystem. This document describes all of the configurable PrintCapabilities currently available on the device, such as finishing options and page layout options. The PrintCapabilities document explicitly describes all attributes of the device and the allowable settings for each attribute. Through the use of the Print Schema Framework, device attributes can be precisely described and efficiently compared. By using the keywords contained in the Print Schema Keywords document, and the structure defined in the Print Schema Framework, devices can enable clients to more effectively use PrintCapabilities. For more information, see [PrintCapabilities Schema and Document Construction](printcapabilities-schema-and-document-construction.md).

Relative to the print subsystem in Microsoft Windows Server 2003 and earlier, the PrintCapabilities technology allows client and print subsystem components to transparently view the information contained in the current Win32 system binary PrintCapabilities. This enables the client to query PrintCapabilities, receive a consistent and well-understood XML snapshot, and use it to construct a PrintTicket for a device without invoking the driver user interface (UI).

## PrintTicket

PrintTicket technology is the successor of the current DEVMODE structure. It is an eXtensible Markup Language based document that specifies and persists information about job formatting and print job configuration. A PrintTicket instance assigns particular device settings and conveys user intent. There are two types of PrintTickets: generic PrintTickets, which are not generated for a particular device; and device-specific PrintTickets, which are constructed for a particular device. Generic PrintTickets, which are intended to be portable across devices, derive their contents by selecting settings for each of the device attributes described exclusively in the Print Schema Keywords. Device-specific PrintTickets derive their contents from a PrintCapabilities document, selecting settings for each device attribute advertised by this document. These PrintTickets may also include private extensions, specific to one device model or device model family. For more information, see [PrintTicket Schema and Document Construction](printticket-schema-and-document-construction.md).

Relative to the current print subsystem, the PrintTicket technology enables all components and clients of the print subsystem to have transparent access to the information currently stored in the public and private portions of the DEVMODE structure, using a well-defined XML format. This design resolves current problems encountered in driver upgrade or downgrade and driver mismatch scenarios in drivers designed for the PrintTicket technology. These scenarios can currently result in a loss of settings and hence a negative customer experience. The PrintTicket also enables new scenarios, such as enabling a printer driver to expose its private DEVMODE settings to applications and custom plug-ins in a consistent and unambiguous manner. This enables printing components to be more transparent and handle settings migrations more cleanly. The PrintTicket interfaces will be exposed to applications through methods on managed code objects that will also be available to scripts. In the new application framework built on managed code objects in the .NET Framework 3.0, the PrintTicket is the standard way of describing document settings.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



