---
description: "Learn more about: Connecting to a Device"
ms.assetid: 16ff280d-818b-4a4e-b5a6-16e81f5b35c6
title: Connecting to a Device
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Connecting to a Device

> [!Note]  
> This scripting system has been replaced with Windows Image Acquisition (WIA) Automation Layer. See [Windows Image Acquisition Automation Layer](/previous-versions/windows/desktop/wiaaut/-wiaaut-startpage).

 

The first step in any application or script that uses the Windows Image Acquisition (WIA) scripting model is creating the [**Wia**](-wia-wia.md) object. This object provides methods for to obtain a collection of [**DeviceInfo**](-wia-deviceinfo.md) objects and connect these objects to devices. It also provides the ability to listen for WIA hardware events.

The following line of Microsoft Visual Basic Scripting Edition (VBScript) code creates the [**Wia**](-wia-wia.md) object:


```
objWia = CreateObject("Wia.Script")
```



After creating the [**Wia**](-wia-wia.md) object, use its [**Create**](-wia-iwia-create.md) method to connect to a WIA hardware device.

You can also use the [**Wia**](-wia-wia.md) object's [**Devices**](-wia-iwia-devices.md) property to obtain a collection of [**DeviceInfo**](-wia-deviceinfo.md) objects. Enumerate this collection and use the [**Create**](-wia-iwiadeviceinfo-create.md) method to connect to a device.

 

 
