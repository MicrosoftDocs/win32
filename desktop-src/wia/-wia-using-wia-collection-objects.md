---
description: A collection is an object that contains one or more objects. Collections provide an efficient way of grouping similar objects. Windows Image Acquisition (WIA) provides collections for the DeviceInfo and Item objects.
ms.assetid: 26918f15-4ef9-425b-8565-e64fc2c72063
title: Using WIA Collection Objects
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Using WIA Collection Objects

A collection is an object that contains one or more objects. Collections provide an efficient way of grouping similar objects. Windows Image Acquisition (WIA) provides collections for the [**DeviceInfo**](-wia-deviceinfo.md) and [**Item**](-wia-item.md) objects.

Use collections to enumerate the objects they contain. For example, the following VBScript example obtains a collection of [**DeviceInfo**](-wia-deviceinfo.md) objects from the [**Devices**](-wia-iwia-devices.md) method and then uses a **For...Each** loop to iterate through the collection:


```
<SCRIPT LANGUAGE="VBScript">
Dim objWia
Dim objDeviceInfoCollection
Dim objDeviceInfo
 
Set objWIA = CreateObject("Wia.Script")
 
Set objDeviceInfoCollection = objWia.Devices
 
For Each objDeviceInfo In objDeviceInfoCollection
    ' Do something with the DeviceInfo object.
Next
</SCRIPT>
```



> [!Note]  
> WIA collection objects are 0-based.

 

 

 



