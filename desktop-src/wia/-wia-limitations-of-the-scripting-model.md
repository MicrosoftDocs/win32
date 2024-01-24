---
description: "Learn more about: Limitations of the Scripting Model"
ms.assetid: b8ddbfac-5b5e-4aff-beea-82e7fc984790
title: Limitations of the Scripting Model
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Limitations of the Scripting Model

> [!Note]  
> This scripting system has been replaced with Windows Image Acquisition (WIA) Automation Layer. See [Windows Image Acquisition Automation Layer](/previous-versions/windows/desktop/wiaaut/-wiaaut-startpage).

 

The Windows Image Acquisition (WIA) scripting model exposes a subset of WIA functionality. The following table provides descriptions of the limitations of the scripting model. 

| WIA Functionality               | Scripting Model Limitation                                                                                                                                                                                                                                               |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Suppressing the user interface  | Cannot suppress the user interface for setting device/transfer properties.                                                                                                                                                                                               |
| Setting properties              | Cannot set (write) any device or item properties.                                                                                                                                                                                                                        |
| Registering for callback events | Can only receive notification for three specified events: [**OnTransferComplete**](-wia--iwiaevents-ontransfercomplete.md), [**OnDeviceConnected**](-wia--iwiaevents-ondeviceconnected.md), and [**OnDeviceDisconnected**](-wia--iwiaevents-ondevicedisconnected.md). |
| Handling errors                 | Cannot handle WIA errors.                                                                                                                                                                                                                                                |



 

 

 
