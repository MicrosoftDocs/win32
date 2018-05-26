---
title: Local Policy Module
description: The Local Policy Module (LPM) is a QOS component responsible for retrieving and returning policy-based decisions used by the Admission Control Service (ACS).
ms.assetid: 292496fc-cf5f-4c6c-8abb-9b3abe73a22b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Local Policy Module

The Local Policy Module (LPM) is a QOS component responsible for retrieving and returning policy-based decisions used by the [Admission Control Service](admission-control-service.md) (ACS). A default LPM provides an interface to policy information that is configured and stored in Windows 2000 Active Directory services. LPM is a generic term used to supply policy-based admission control decisions for ACS. An LPM makes these decisions using policies that are generally configured by network administrators, and stored in policy databases. An LPM is usually implemented as a DLL.

LPMs are used on the ACS server. Client QOS components that generate the policy element reside on the client, and are capable of creating policy information that is carried in RSVP messages to the ACS (which then gets forwarded down to the LPM). It is possible to install an LPM on the ACS server for which there is no corresponding component on the client; for example, an ACS-based LPM could enforce "time-of-day" policies, or could be capable of communicating with a COPS server.

It is important to note the difference between IETF-draft technologies and the Microsoft implementation of them. Subnet Bandwidth Manager (SBM), for example, is a technology derived from an IETF-draft proposal for regulating access to 802 subnets (draft-ietf-issll-is802-sbm-08.txt). ACS is a Windows 2000 service (and a QOS component) that incorporates SBM technology within its fold to incorporate regulation of access to 802 subnets in accordance with policy control.

 

 




