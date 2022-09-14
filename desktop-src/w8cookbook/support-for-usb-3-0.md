---
title: Support for USB 3.0
description: Support for USB 3.0
ms.assetid: AACE4B57-A03F-40C7-AFDD-514D29F24521
ms.topic: article
ms.date: 05/31/2018
---

# Support for USB 3.0

## Platforms

**Clients** – Windows 8  
**Servers** – Windows Server 2012  


## Description

In Windows 8 and Windows Server 2012, we added support for USB 3.0. We did this by adding a new software stack to power the USB 3.0 host controller, called an eXtensible Host Controller (XHC). We maintained interface parity, IRQL level, caller context, error status, retry frequency, and so on. There should be no difference for you when interacting with a device connected over USB 2.0 versus USB 3.0.

However, if you are writing a driver for a new, USB 3.0 device, definitely opt for new USB 3.0 capabilities.

## Manifestation

Device transfers are faster and less power is consumed from a PC by USB devices overall. There is a risk that existing USB devices may not function correctly when connected to a USB 3.0 port. This should not happen, and is not expected, but, because the software that powers USB 3.0 is new, it is a risk.

 

 




