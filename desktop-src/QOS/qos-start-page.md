---
title: Quality of Service
description: Quality of Service (QOS), an industry-wide initiative, enables more efficient use of the network.
ms.assetid: 2a017166-eba4-4dd9-b623-f0d696e11de2
keywords:
- Quality of Service QOS , start page
- QOS QOS See Quality of Service QOS
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Quality of Service

## Purpose

Quality of Service (QOS), an industry-wide initiative, enables more efficient use of the network. The Internet Engineering Task Force (IETF) has provided many documents in the form of Internet Drafts and Request for Comments (RFC) that outline such capabilities including those provided by the Intserv, Diffserv, ISSLL, and RAP IETF working groups, among others.

The goal of Quality of Service is to provide preferential treatment to certain subsets of data, enabling that data to traverse the traditionally best-effort Internet or intranet with higher quality transmission. Quality of Service in Windows is a collection of components that enable differentiation and management of higher quality data transmissions across the network. The collection of QOS components included in Windows constitutes the Microsoft implementation of the IETF vision of Quality of Service.

## Where applicable

Developers can use Quality of Service to:

-   Create or retrofit mission-critical applications to operate as if network traffic conditions were ideal, even when the network is extremely congested.
-   Create real-time applications, such as IP telephones or streaming multimedia, that receive transmission service that enables optimal functioning, regardless of traffic conditions between sender and receiver.
-   Create or retrofit applications that are efficient network users, so that their transmissions adhere to agreed-upon characteristics. By doing so, every corner of a QOS-enabled network becomes more manageable and more efficiently used, taming the traditional TCP approach of "send all of it out as fast as possible" and its associated clogging effects.

Quality of Service achieves these capabilities through programmatic interfaces, the cooperation of multiple components, and communication with network devices throughout the end-to-end network solution.

## Developer audience

Programmable QOS components are designed for use by C/C++ programmers. Familiarity with Windows networking and Windows Sockets 2 programming is required.

## Run-time requirements

Quality of Service requires Windows 2000 or later. RSVP Signaling and Admission Control Service (ACS) are supported only on Windows 2000 and are not implemented on subsequent versions of Windows. Also, certain QOS functions require administrative privilege to execute; such component requirements are specified where appropriate.

The Quality Windows Audio/Video Experience (qWAVE) API is available only in Windows Vista and later.

## In this section



| Topic                                                                                                           | Description                                                                                            |
|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [About Quality of Service (QOS)](about-quality-of-service-qos-.md)<br/>                                  | General information about Quality of Service.<br/>                                               |
| [QOS Reference](qos-reference.md)<br/>                                                                   | Documentation of QOS functions, structures, and objects.<br/>                                    |
| [Quality Windows Audio/Video Experience (qWAVE)](quality-windows-audio-video-experience--qwave-.md)<br/> | General information about qWAVE and documentation of its functions, structure, and objects.<br/> |



 

## Related topics

<dl> <dt>

[Windows Sockets 2](https://msdn.microsoft.com/library/windows/desktop/ms740673)
</dt> </dl>

 

 





