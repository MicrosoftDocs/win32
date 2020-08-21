---
title: Biometric Framework overview
description: Native support for biometric devices is incorporated into Windows.
ms.assetid: 616ba95a-27a3-4eac-b802-5217954ed04e
ms.topic: article
ms.date: 05/31/2018
---

# Biometric Framework overview

Every individual has unique characteristics that can be used for identification. Typically these characteristics are physical and include traits such as fingerprints, but they can also include behavioral traits such as gait and typing rhythm. The term biometrics encompasses both meanings. Biometric information is increasingly replacing passwords to identify and verify users. It is more secure and often more convenient for both user and administrator.

Sensors are used to capture biometric information. The information is captured by the sensor as a biometric sample. A single sample contains data that represents a single biometric characteristic for one individual. Multiple samples are averaged to create a biometric template, and the template is securely stored. Later, a sample from an unknown user is compared to the stored templates to establish and verify user identity. The Windows Biometric service, part of the Windows Biometric Framework (WBF), provides the following functionality. You can use the Windows Biometric Framework API to leverage this functionality.

-   Captures biometric samples and uses them to create a template.
-   Securely saves and retrieves biometric templates.
-   Maps each template to a unique identifier such as a GUID or SID.

You can also use this API to extend the framework and create biometric sensor adapters, matching engines, and storage components. For more information about creating sensor adapters, matching engines, and storage components, see [Creating Adapter Plug-ins](creating-adapter-plug-ins.md).

## Core platform components

### Windows Biometric Driver Interface (WBDI)

WBDI is a programming interface that a biometric driver can use to expose the biometric device through the Windows Biometric Service (WBS). You can implement a WBDI driver by using any supported driver technology, including the following. We recommend, however, that you use UMDF when possible to improve driver quality and system stability.

-   User Mode Driver Framework (UMDF)
-   Kernel Mode Driver Framework (KMDF)
-   Windows Driver Model (WDM)

A WBDI biometric driver must also support the WBDI driver interface GUID and all mandatory I/O controls (IOCTLs). Driver developers should review the documentation and sample code in the Windows Driver Kit (WDK).

### Windows Biometric Service (WBS)

The Windows Biometric Service manages installed biometric drivers and supports the Windows Biometric Framework API to provide device access to client applications. WBS performs the following functions:

-   It protects user confidentiality by separating client applications from biometric data.
-   It protects biometric data from unprivileged client applications by requiring that applications gain access to data by using unique identifiers.
-   It uses a software component called a [Biometric Unit](/previous-versions//dd401512(v=vs.85)) to expose the capabilities of a particular biometric device through a standardized interface.
-   It manages biometric units by grouping them into system, private, or unassigned [Sensor Pools](sensor-pools.md).
-   It supports the use of biometric unit [Adapters](/previous-versions//dd401508(v=vs.85)) for physical devices that lack onboard processing or storage capabilities.

### Windows Biometric Framework API

The Windows Biometric Framework API enables you to create client applications that can interact with the Windows Biometric Service to perform the following actions:

-   Identify and verify users.
-   Locate biometric devices and query their capabilities.
-   Manage sessions and monitor events.

## User Experience Components

### Discovery Points

End users can locate biometric devices by any of the following means:

-   Typing the words biometrics, fingerprint, face, or other related phrases into the Start Search text box to start the biometric devices control panel. The results list for biometrics can contain items such as the following on a Windows 10 image.
    -   Setup fingerprint sign-in
    -   Setup face sign-in

### Supported Scenarios

The following scenarios are supported:

-   Users can log on to a local computer, a workgroup, or to a domain by using a fingerprint reader, or IR camera focused on the face.
-   A user with administrative privileges can elevate applications through User Account Control (UAC) by using a fingerprint or face.

## Management components

A biometric system can be managed using Group Policy or mobile device management (MDM).

### Biometric System Management

You can manage biometric capabilities using Group Policy or MDM. Group Policy can further be used to perform the following actions:

-   Specify the timeout period for fast user switching, if implemented by the ISV.
-   Prevent biometric device installation.
-   Force the removal of drivers for biometric devices.
-   Disable the biometric service.

 

 