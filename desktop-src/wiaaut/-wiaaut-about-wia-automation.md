---
title: About Microsoft Windows Image Acquisition Automation Layer
description: The Windows Image Acquisition (WIA) Automation Layer is a high-quality, full-featured image manipulation component that provides end-to-end image processing capabilities for Microsoft Visual Basic 6.0, Active Server Pages (ASP), and scripting languages.
ms.assetid: 808b575e-e3ba-4229-9625-651b33e77c3f
keywords:
- Windows Image Acquisition (WIA),about
- WIA (Windows Image Acquisition),about
- Windows Image Acquisition Automation Layer,about
- WIA Automation Layer,about
- Image Acquisition Automation Layer,about
- Windows Image Acquisition (WIA),objects
- WIA (Windows Image Acquisition),objects
- Windows Image Acquisition Automation Layer,objects
- WIA Automation Layer,objects
- Image Acquisition Automation Layer,objects
- Windows Image Acquisition (WIA),accessing imaging devices
- WIA (Windows Image Acquisition),accessing maging devices
- Windows Image Acquisition Automation Layer,accessing imaging devices
- WIA Automation Layer,accessing imaging devices
- Image Acquisition Automation Layer,accessing imaging devices
- accessing imaging devices
- Windows Image Acquisition (WIA),examples
- WIA (Windows Image Acquisition),examples
- Windows Image Acquisition Automation Layer,examples
- WIA Automation Layer,examples
- Image Acquisition Automation Layer,examples
- Windows Image Acquisition (WIA),sample code
- WIA (Windows Image Acquisition),sample code
- Windows Image Acquisition Automation Layer,sample code
- WIA Automation Layer,sample code
- Image Acquisition Automation Layer,sample code
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About Microsoft Windows Image Acquisition Automation Layer

The Windows Image Acquisition (WIA) Automation Layer is a high-quality, full-featured image manipulation component that provides end-to-end image processing capabilities for Microsoft Visual Basic 6.0, Active Server Pages (ASP), and scripting languages. The WIA Automation Layer exposes features in Windows XP Service Pack 1 (SP1) or later to make it easy to acquire images on digital cameras, scanners, or Web cameras, and to rotate, scale, and annotate your image files. Earlier versions of Windows are not supported.

Other new features include the ability to:

-   Access the properties of image files.
-   Read and write image files and their properties to databases.
-   Modify pixels including alpha values.
-   Write ASP pages that generate thumbnail images on the fly.
-   Take pictures with your Web camera.
-   Automatically download pictures from cameras as soon as they are connected, even if a script is not already running.

This overview includes the following topics.

-   [Object Hierarchy](#object-hierarchy)
-   [Accessing Imaging Devices](#accessing-imaging-devices)
-   [Manipulating Image Files](#manipulating-image-files)
-   [Example Code](#example-code)

## Object Hierarchy

The WIA Automation Layer is broken down into two types of objects. The first type of object is a creatable object. This is an object that can be directly created by calling the Microsoft Visual Basic function [CreateObject](http://msdn.microsoft.com/library/7t9k08y5(VS.71).aspx). In addition, three creatable objects ([**DeviceManager**](-wiaaut-devicemanager.md), [**CommonDialog**](-wiaaut-commondialog.md), and [**VideoPreview**](-wiaaut-videopreview.md)) are also controls that can be dropped on a form in Visual Basic. The second type of object is the supporting object. This object is not directly creatable but instead is returned from properties or methods. For example, the [**Connect**](-wiaaut-ideviceinfo-connect.md) method on a [**DeviceInfo**](-wiaaut-deviceinfo.md) object returns a [**Device**](-wiaaut-device.md) object.

The following object hierarchy diagrams show the relationship between objects, collections, and reused objects for both creatable and supporting objects. The hierarchy diagrams use these symbols.

![hierarchy key](images/art-wiaaut-hierarchy-key.gif)

![creatable and supporting objects](images/art-wiaaut-hierarchy.gif)

As you can see in the previous illustrations, the WIA Automation Layer reuses objects wherever possible to reduce the number of different objects you need to learn to use. For example, the [**Device**](-wiaaut-device.md), [**DeviceInfo**](-wiaaut-deviceinfo.md), [**Filter**](-wiaaut-filter.md), [**FilterInfo**](-wiaaut-filterinfo.md), [**Item**](-wiaaut-item.md), and [**ImageFile**](-wiaaut-imagefile.md) objects all reuse the [**Properties**](-wiaaut-properties.md) collection to expose their properties. Once you learn how to use the **Properties** collection on one object you will be able to use it on all the others.

Notice the naming convention in which a collection of objects uses the plural of that object name. For example, a [**Filters**](-wiaaut-filters.md) collection holds [**Filter**](-wiaaut-filter.md) objects.

## Accessing Imaging Devices

The [**DeviceManager**](-wiaaut-devicemanager.md) object and, to a limited degree, the [**VideoPreview**](-wiaaut-videopreview.md) object are the primary ways to access Imaging Devices. The [**Device**](-wiaaut-device.md) object represents an active connection to an Imaging Device. From the **Device** object you can access its properties, access the items that might be stored on it, transfer those items to files on the computer, and run commands that cause the Imaging Device to do something. For example, you could access a digital camera's date and time, transfer all its pictures to your computer or cause it to [take a picture](https://www.bing.com/search?q=take a picture). These actions can be done in one of two ways, programmatically without any user intervention, or using the [**CommonDialog**](-wiaaut-commondialog.md) object to present dialog boxes that enable the user to precisely control the actions.

## Manipulating Image Files

Once you have transferred pictures to your computer, you can use the [**ImageFile**](-wiaaut-imagefile.md) object to access the pictures. You can display them on forms, return them as binary data in ASP pages, or access their properties. Many digital cameras store a number of detailed properties in their pictures, from useful information like the date the picture was taken and a thumbnail image to interesting technical details like the model of camera, the focal length, aperture setting, and shutter speed. For more information about detailed properties, see [Display all ImageFile Properties](https://www.bing.com/search?q=Display all ImageFile Properties) and [Display Detailed Image Information](https://www.bing.com/search?q=Display Detailed Image Information).

In order to protect the original pictures that represent digital memories, the [**ImageFile**](-wiaaut-imagefile.md) object cannot directly modify the pictures. You can, however, use an [**ImageProcess**](-wiaaut-imageprocess.md) object and one or more [**Filter**](-wiaaut-filter.md) objects to create a modified copy of the picture. The WIA Automation Layer provides filters that rotate, flip, crop, scale, stamp, modify properties, modify the individual pixels or change the file format to Tagged Image File Format (TIFF), JPEG, Portable Network Graphics (PNG), bitmap (BMP), or Graphics Interchange Format (GIF). For more information about filters, see [How To Use Filters](-wiaaut-howto-use-filters.md).

## Example Code

All reference pages in this documentation set include example code or a link to examples in the Overviews/Tutorials section that illustrate how to use the API. Begin by reading [Getting Started with Samples](-wiaaut-getting-started-samples.md). This topic has the template code for a variety of development environments into which you can paste the reference examples. [Shared Samples](-wiaaut-shared-samples.md) includes a number of examples that are applicable to a variety of applications.

The following examples are complete samples that you do not need to paste into template code.

-   [Download New Items as They are Created](https://www.bing.com/search?q=Download New Items as They are Created)
-   [Use VideoPreview Control in HTML](https://www.bing.com/search?q=Use VideoPreview Control in HTML)
-   [Implement a Web Camera ASP Page](https://www.bing.com/search?q=Implement a Web Camera ASP Page)
-   [Implement a Windows Script Host Script that Runs Automatically](https://www.bing.com/search?q=Implement a Windows Script Host Script that Runs Automatically)

 

 




