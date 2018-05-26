---
title: Tune Requests
description: Tune Requests
ms.assetid: f1014741-120c-4a6a-81fd-282444ad33bc
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Tune Requests

In digital television, tuning involves not only locating the signal on which a transport stream is being carried, but also finding the audio, video, and data elementary streams within that transport stream. In all tuning operations, the tune request object has a central role because it contains (or provides access to) all the information necessary for tuning.

The only way to create a tune request is by using the [**CreateTuneRequest**](/windows/previous-versions/tuner/nf-tuner-ituningspace-createtunerequest?branch=master) method on the tuning space where the program is to be found. Both tune requests and tuning spaces are associated with a particular network type. For example, an ATSC tuning space object is used to create ATSC tune requests, a DVB-S tuning space object is used to create DVB-S tune requests, and so on. All tune requests contain references to the tuning space that was used to create it.

Tune requests for digital network types also contain references to a Locator object that contains further information necessary for tuning, and to a Components object that describes all the audio, video and data substreams that are available as part of the program. (These objects are discussed in detail later in this section.) All tune requests contain additional properties depending on their network type. For example, ATSC tune requests have a MajorChannel and MinorChannel property, and DVB-S tune requests have properties for getting and setting the transport stream ID (TSID) and original network ID (ONID).

 

 




