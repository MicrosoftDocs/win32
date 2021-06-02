---
description: After determining the capabilities of a phone device, an application must open the device before it can access functions on that phone.
ms.assetid: 0215db43-b4d7-4a1e-8d4f-d17013c14e61
title: Opening and Closing Phone Devices
ms.topic: article
ms.date: 05/31/2018
---

# Opening and Closing Phone Devices

After determining the capabilities of a phone device, an application must open the device before it can access functions on that phone. After a phone device has been successfully opened, the application is returned a handle representing the open phone. A phone device can be opened in different modes, thus providing a structured way of sharing a phone device.

The [**phoneOpen**](/windows/desktop/api/Tapi/nf-tapi-phoneopen) function opens the specified phone device to give the application access to functions on the phone. A phone device is identified to **phoneOpen** by means of its device identifier, which is passed as the *dwDeviceID* parameter.

 

 



