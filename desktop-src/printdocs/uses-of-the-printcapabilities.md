---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: ea75a7ac-d4d7-42b6-91e9-e28607fd684c
title: Uses of the PrintCapabilities
ms.topic: article
ms.date: 05/31/2018
---

# Uses of the PrintCapabilities

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

The PrintCapabilities are intended to represent configurable device attributes as either Feature/Option constructs or parameter constructs. This information defines the configuration space of the device and can be used by a user interface (UI) client to construct a UI. The Print Schema Keywords define a set of standard Feature instances, Option instances for the standard Feature instances, and ParameterDef instances.

The Feature/Option or parameter constructs in the PrintCapabilities are intended to hold Property or ScoredProperty instances that describe a device, and that are supported by the spooler subsystem. These Property and ScoredProperty instances are of general interest to clients of the device, and contain the information that is provided by the Win32 DevCaps functions. The Print Schema Keywords define a set of standard Property and ScoredProperty instances.

It should be emphasized that the PrintCapabilities document is intended to represent only single-valued data: data that does not depend on a particular configuration of the device. The PrintCapabilities document provides only a snapshot of configuration-dependent data.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



