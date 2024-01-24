---
description: Windows Image Acquisition (WIA) provides automation objects for use in scripting languages, such as Microsoft JScript and Microsoft Visual Basic Scripting Edition (VBScript) development software, and high-level programming languages such as Microsoft Visual Basic development system.
ms.assetid: 3d294db3-3349-4b26-aae1-1e3f588a0f0e
title: WIA Scripting Model
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# WIA Scripting Model

Windows Image Acquisition (WIA) provides automation objects for use in scripting languages, such as Microsoft JScript and Microsoft Visual Basic Scripting Edition (VBScript) development software, and high-level programming languages such as Microsoft Visual Basic development system.

> [!Note]  
> This scripting system has been replaced with Windows Image Acquisition (WIA) Automation Layer. See [Windows Image Acquisition Automation Layer](/previous-versions/windows/desktop/wiaaut/-wiaaut-startpage).

 

The following table describes WIA scripting objects and how they are used. 

| Object                                | Description                                                                                                                                                                                  |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Wia**](-wia-wia.md)               | The top-level WIA scripting object. Use the [**Wia**](-wia-wia.md) object to enumerate and connect to devices, and to handle hardware device events.                                        |
| [**DeviceInfo**](-wia-deviceinfo.md) | The [**DeviceInfo**](-wia-deviceinfo.md) object provides access to information about device properties.                                                                                     |
| [**Item**](-wia-item.md)             | This object represents WIA device, file, and folder items. A WIA hardware device and its images or scanning beds is represented as a hierarchical tree of [**Item**](-wia-item.md) objects. |



 

Both the [**DeviceInfo**](-wia-deviceinfo.md) object and the [**Item**](-wia-item.md) object are associated with collection objects. For information about using collection objects, see Using WIA Collection Objects.

The following topics cover general information about using the WIA scripting model:

-   [Syntax Conventions](-wia-syntax-conventions.md)
-   [Using WIA Collection Objects](-wia-using-wia-collection-objects.md)
-   [WIA Property Constant Definitions](-wia-wia-property-constant-definitions.md)

 

 
