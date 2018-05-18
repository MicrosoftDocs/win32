---
title: RSVP SP Error Codes
description: The RSVP SP provides a rich set of error codes and error values that enable applications and service providers to get detailed feedback when errors in processing occur.
ms.assetid: 'de916db8-8840-44d8-a898-1014019e5103'
keywords: ["Quality of Service QOS , reference, RSVP error codes"]
---

# RSVP SP Error Codes

\[RSVP signaling is not supported except on Windows 2000. For more information, see [RSVP Operates Only on Windows 2000](rsvp-operates-only-on-windows-2000.md).\]

The RSVP SP provides a rich set of error codes and error values that enable applications and service providers to get detailed feedback when errors in processing occur.

RSVP SP errors (and all QOS errors) are retrieved by using the SIO\_GET\_QOS IOCTL call. SIO\_GET\_QOS returns a [**QOS**](qos.md) structure, and the error codes are returned in a [**RSVP\_STATUS\_INFO**](rsvp-status-info.md) object provided in the [ProviderSpecific](the-providerspecific-buffer.md) buffer in the **QOS** structure.

The reference pages in this section enable application and service developers to become familiar with RSVP SP error codes and error values, and they provide suggested actions when such errors arise.

 

 




