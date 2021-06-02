---
description: PROPERTYKEYs and GUIDs in Windows Portable Devices
ms.assetid: 3f9e9f29-37dd-47b0-997e-de81966efce2
title: PROPERTYKEYs and GUIDs in Windows Portable Devices
ms.topic: article
ms.date: 05/31/2018
---

# PROPERTYKEYs and GUIDs in Windows Portable Devices

A property or command is identified by a PROPERTYKEY structure. A PROPERTYKEY structure is made up of two parts: a GUID (the fmtid member) and a DWORD (the pid member). The GUID part is used to indicate the category the property or command belongs to (that is, related properties belong to the same category and related commands belong to the same category; therefore they will have the same fmtid). The DWORD part indicates the property or command ID, and is used to distinguish the individual properties or commands within a property or command category (that is, the pid values for properties or commands in the same category will be different).

The reference section of this document describes all the PROPERTYKEY values defined by WPD; these values correspond to commands, properties, and resources. If you create a custom PROPERTYKEY value, you should define a new **GUID** category; do not reuse the WPD **GUID** values or you risk conflicting with existing and future WPD-specified PROPERTYKEYs.

## Related topics

<dl> <dt>

[**Application Overview**](application-overview.md)
</dt> <dt>

[**Commands**](commands.md)
</dt> <dt>

[**Object Format GUIDs**](object-format-guids.md)
</dt> <dt>

[**Properties and Attributes**](properties-and-attributes.md)
</dt> <dt>

[**Requirements for Objects**](requirements-for-objects.md)
</dt> </dl>

 

 



