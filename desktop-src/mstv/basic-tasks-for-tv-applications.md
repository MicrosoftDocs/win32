---
title: Basic Tasks for TV Applications
description: Basic Tasks for TV Applications
ms.assetid: '90549f4a-3814-4c63-8858-2f15d2dbdf96'
---

# Basic Tasks for TV Applications

This topic applies to Windows XP or later.

Application development using Microsoft TV Technologies is based on a few fundamental tasks. Some of these tasks are optional, depending on what type of application you are developing. This section gives a brief desciption of each task. It is not specific to any programming language; later sections give detailed information for script, Visual Basic, and C++.

1.  **Create an instance of the Video Control.** The Video Control provides access to the TV tuner devices, audio and video rendering devices, and various features such as closed captioning and IP data services. For more information, see [Using the Video Control](using-the-video-control.md).
2.  **Activate the desired features.** IP data services and closed captioning are exposed to applications as "features" by the Video Control. The Video Control exposes a **FeaturesAvailable** collection, which contains the features that are available. To enable some or all of these features, the application creates a new collection object, adds the desired features from the **FeaturesAvailable** collection, and sets the new collection as the Video Control's **FeaturesActive** property.
3.  **Obtain or create a tune request.** A *tune request* contains tuning information for a particular network type. The recommended approach is to implement an object called a *guide store loader* that reads electronic program guide (EPG) data and uses it to populate a database with tune requests. With this approach, the application does not depend on the underlying network type. Instead, it simply pulls generic tune request objects from the data base.

    An alternate approach is for the application to create the tune request. This approach requires the application to target specific network types, because different network types have different requirements for tune requests.

4.  **Submit the tune request to the Video Control.** The application gives the tune request to the Video Control by calling the Video Control's **View** method.
5.  **Configure the Video Mixing Renderer for custom rendering.** (Optional) The Video Mixing Renderer (VMR) enables you to create custom mixing effects, such as alpha-blending a bitmap over the video rectangle. The application configures the VMR through the **MSVidVideoRenderer** object, which is obtained through the Video Control's **VideoRendererActive** property.
6.  **Set up event notication.** (Optional) For most applications, it is useful to receive event notifications from the Video Control. The mechanism for receiving events depends on the programming language; details are given in the language-specific sections of the documentation.
7.  **Access IP data in the broadcast stream.** (Optional) If the Data Services feature is enabled, IP data in the broadcast stream is routed to the NDIS stack. To receive this data, the application must open a socket using Winsock and listen on the specified multicast address, as it would for any other IP data.
8.  **Create a default tune request.** (Required for script applications only) When Microsoft Internet Explorer encounters a "TV:" URL in a Web page, it automatically loads the Video Control and tunes it to the default tune request, which is stored in the system registry. This registry entry must be created by a C++ application, using the [**ICreatePropBagOnRegKey**](icreatepropbagonregkey.md) interface.

## Related topics

<dl> <dt>

[Overview of Microsoft TV Technologies](overview-of-microsoft-tv-technologies.md)
</dt> <dt>

[TV Applications in C++ (Video Control)](tv-applications-in-c--video-control.md)
</dt> </dl>

 

 




