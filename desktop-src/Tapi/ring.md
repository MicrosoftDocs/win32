---
description: A single phone may be able to ring with different ring modes.
ms.assetid: 'c5ddcb3c-183c-4f97-9429-977d5cc32668'
title: Ring
ms.topic: article
ms.date: 05/31/2018
---

# Ring

A single phone may be able to ring with different ring modes. Given the wide variety of ring modes available, ring modes are identified by means of their ring mode number. A ring mode number ranges from zero to the number of available ring modes minus one.

The functions an application would use to control a phone device's ring modes are [**phoneSetRing**](/windows/desktop/api/Tapi/nf-tapi-phonesetring), which rings an open phone device according to a given ring mode, and [**phoneGetRing**](/windows/desktop/api/Tapi/nf-tapi-phonegetring), which returns the current ring mode of an opened phone device.

When the ring mode of a phone device is changed, a [**PHONE\_STATE**](phone-state.md) message is sent to the application to notify the application about the state change. Parameters to this message provide an indication of the change.

 

 



