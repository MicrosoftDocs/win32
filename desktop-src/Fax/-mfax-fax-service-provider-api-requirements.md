---
Description: 'This topic describes the required components to support the functionality of the fax service provider API.'
ms.assetid: 'f6137f24-2b83-4d5d-b6ab-a0ecffd20c91'
title: Fax Service Provider API Requirements
---

# Fax Service Provider API Requirements

The fax service provider (FSP) API supports multiple fax devices and provides a device-independent interface for performing fax procedures. The components described below are required to support the functionality of the FSP API:

-   The fax device manufacturer must supply a FSP DLL that exposes a well-defined interface for performing fax procedures. There must be one FSP DLL for each fax device class.

-   The fax service is a support-service application that provides an execution context for the FSP DLL. The fax service uses the DLL to communicate with the FSP. The fax service manages fax devices and configuration data, provides print services, and sends and receives fax documents. The fax service creates all fax documents as Tagged Image File Format Class F (TIFF Class F) files.

-   The Telephony Application Programming Interface (TAPI) establishes inbound and outbound fax calls, and it provides enumeration, status, and change notification about fax devices. For more information about TAPI, see the *Telephony Application Programming Interface (TAPI) Programmer's Reference*.

-   Each FSP that presents only physical fax devices must also supply a telephony service provider (TSP) for device abstraction. The TSP identifies all the fax devices that the FSP controls, and enables the fax service to use the exposed fax devices. If a FSP presents virtual fax devices, a TSP is not required. For more information about the Telephony Service Provider Interface (TSPI) and service providers, see the Windows Software Development Kit (SDK) documentation on *Telephony Service Provider Interface (TSPI)*.

In addition, you must include the FSP header in your source code files. FaxDev.h contains function prototypes, structure definitions, and fax status constants.

All UI features and configuration storage are the responsibility of the FSP.

 

 



