---
title: Locators
description: Locators
ms.assetid: e2aaba05-0a1b-41d0-895d-1f54b1b9d9ce
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Locators

Locator objects contain additional information about the signal and the transport stream that the Network Provider and tuner need in order to locate the service. Like tuning spaces and tune requests, locators are specific to a network type. A DVB-S tune request has a reference to a DVB-S locator, an ATSC tune request has a reference to an ATSC locator, and so on. Analog TV tuning spaces do not require locators because analog TV graphs are not based on Broadcast Driver Architecture and a tune request is never actually submitted to an analog TV tuner device.

Locators for DVB tuning spaces, especially for DVB-S providers, are more complex because these providers typically transmit many services on multiple transport streams simultaneously. Typically, the Guide Store Loader should be responsible for creating and configuring locators; it is only necessary to set those properties that will actually be used in the tuning process. A DVB-S provider may install a default locator along with its custom tuning space. This locator should contain the information to enable a tuner to locate the default transport stream on the network.

 

 




