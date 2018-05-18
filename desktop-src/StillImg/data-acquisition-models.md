---
title: Data Acquisition Models
description: Applications typically control still-image acquisition devices through imaging APIs such as TWAIN or ISIS.
ms.assetid: '217a3fa3-1f3e-44b5-b845-50f30d6a9d7b'
keywords: ["Still Image (STI),data acquisition models", "STI (Still Image),data acquisition models", "Still Image API,data acquisition models", "still images,data acquisition models", "data acquisition models", "Still Image (STI),TWAIN", "STI (Still Image),TWAIN", "Still Image API,TWAIN", "still images,TWAIN", "TWAIN", "Still Image (STI),ISIS", "STI (Still Image),ISIS", "Still Image API,ISIS", "still images,ISIS", "ISIS", "Still Image (STI),pull model", "STI (Still Image),pull model", "Still Image API,pull model", "still images,pull model", "pull model", "Still Image (STI),push model", "STI (Still Image),push model", "Still Image API,push model", "still images,push model", "push model"]
---

# Data Acquisition Models

Applications typically control still-image acquisition devices through imaging APIs such as TWAIN or ISIS. For the most part, applications that use these APIs operate under the pull model of data acquisition. In the pull model, you locate and select a source of data. The application then uses the imaging API to acquire data from the device. In effect, the application pulls data from the device toward itself. The following figure illustrates the pull model of data acquisition.

![pull model of data acquisition](images/stipull.gif)

Microsoft Still Image API supports the use of both the pull model and the push model of data acquisition. Using the push model, still image devices notify applications of their status. You then use the standard TWAIN or ISIS APIs to acquire data. The following figure shows the push model of data acquisition.

![push model of data acquisition](images/stipush.gif)

The advantage of the push model of data acquisition is that it significantly simplifies the user model. The user model is the manner in which the user interacts with the image capture system. Under the push model of image capture, you only need to activate the image capture device to initiate image capture. When the device is activated, it generates a push model event. This in turn causes the appropriate application to be launched, and, depending on the application, image capture to be initiated. If it is already running, you just need to select **Rescan** from the application's menu system to acquire more images.

This simplified user model enables developers to create hardware and software combinations that operate much more intuitively. For example, a kiosk for creating security badges has a very intuitive user model under the push model of data acquisition. You only need to step up to the kiosk and press a button on the digital camera or kiosk to take a picture for the badge. The kiosk's digital camera generates a device event. The device event in turn launches an application to acquire the data and produce the badge. The only action that you need take in the process is to press a button. Under the pull model of data acquisition, you would have had to interact with a graphical user interface (GUI).

 

 




