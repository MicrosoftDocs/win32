---
title: Licenses
description: Licenses
ms.assetid: '74717519-bfd5-4a64-88eb-680d4bdfe74a'
keywords:
- Windows Media Format SDK,digital rights management (DRM)
- Windows Media Format SDK,DRM licenses
- Windows Media Format SDK,licenses for DRM
- digital rights management (DRM),licenses
- DRM (digital rights management),licenses
- digital rights management (DRM),protected file licensing
- DRM (digital rights management),protected file licensing
- licenses,DRM
ms.topic: article
ms.date: 05/31/2018
---

# Licenses

A license is a set of data that describes the conditions under which data in protected files can be read. Each license applies to a key identifier, which is typically assigned to a single media file. This identifier is what is used to identify the protected content in the license.

Each license specifies one or more actions that can be performed with the protected content. These actions, also called rights, can be limited in a number of ways. By combining start dates, end dates, counts, and time limits, the license issuer can create almost any imaginable limitation on a right.

Licenses are issued by a Web service. When a license is acquired, it is stored on the client computer in the local license store, which is a protected file that contains licenses and other DRM data. When protected content is accessed by an application, the DRM subsystem searches the local license store for a license that grants the appropriate right. If no license is found, the application can acquire one based on information stored in the DRM header of the file.

Multiple licenses can be issued for the same protected file. When the DRM subsystem determines whether an action is allowed, it aggregates the rights from all licenses that apply. Each license can be assigned a priority. If more than one license applies to an action, the highest priority license is checked to determine whether counts need to be decremented.

## Related topics

<dl> <dt>

[**Concepts**](drmconcepts.md)
</dt> </dl>

 

 




