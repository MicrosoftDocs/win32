---
description: Overview of considerations for designing an application that uses the StylusInput application programming interfaces (APIs).
ms.assetid: cb68a6bb-dd38-4dfb-bbbb-b5d846e5aa0a
title: Design Considerations for the StylusInput API
ms.topic: article
ms.date: 05/31/2018
---

# Design Considerations for the StylusInput API

The following are design considerations for the StylusInput API.

-   You can update the [**WindowInputRectangle**](/windows/desktop/api/RTSCom/nf-rtscom-irealtimestylus-get_windowinputrectangle) property of the [**RealTimeStylus**](realtimestylus-class.md) object and the [**ClipRectangle**](/windows/desktop/api/RTSCom/nf-rtscom-idynamicrenderer-get_cliprectangle) property of the [**DynamicRenderer**](/previous-versions/windows/desktop/legacy/ms701168(v=vs.85)) object while the pen is down. This can be useful when you want to have a dynamic drawing area while the application is collecting ink.
-   To optimize reuse and maintenance of plug-in code, plug-ins should not make calls directly to the application but should use the [**CustomStylusData**](/windows/desktop/api/RTSCom/nf-rtscom-istylusplugin-customstylusdataadded) ([CustomeStylusData](/previous-versions/ms824747(v=msdn.10)) object in managed code) to communicate with the application.
-   The [**RealTimeStylus**](realtimestylus-class.md) object's plug-in collections are ordered. The relative position of your plug-ins within these collections can be very important. For example, a plug-in that modifies packet information should probably be added to the synchronous plug-in collection before a dynamic-renderer plug-in.
-   The ability to add custom stylus data to the tablet pen's data stream should be used sparingly. Use this feature only if another plug-in needs to receive this information as part of the data stream. Also, avoid adding custom stylus data in response to other custom stylus data coming into the plug-in, as this can create an infinite loop.
-   Plug-in collections can be modified while the [**RealTimeStylus**](realtimestylus-class.md) object is enabled; however, this can make the behavior of your application harder to predict. When a plug-in is added while the **RealTimeStylus** object is enabled, the **RealTimeStylus** object calls the plug-in's Microsoft.StylusInput.IStylusSyncPlugin. [**RealTimeStylusEnabled**](/windows/desktop/api/RTSCom/nf-rtscom-istylusplugin-realtimestylusenabled) method (either the [Microsoft.StylusInput.IStylusSyncPlugin.RealTimeStylusEnabled](/previous-versions/ms824758(v=msdn.10)) or the [Microsoft.StylusInput.IStylusAsyncPlugin.RealTimeStylusEnabled](/previous-versions/ms824775(v=msdn.10)) method in managed code). When a plug-in is removed while the **RealTimeStylus** object is enabled, the **RealTimeStylus** object calls the plug-in's [**RealTimeStylusDisabled**](/windows/desktop/api/RTSCom/nf-rtscom-istylusplugin-realtimestylusdisabled) method (either the [Microsoft.StylusInput.IStylusSyncPlugin.RealTimeStylusDisabled](/previous-versions/ms824757(v=msdn.10)) or the [Microsoft.StylusInput.IStylusAsyncPlugin.RealTimeStylusDisabled](/previous-versions/ms824774(v=msdn.10)) method in managed code). This allows the plug-in to maintain its proper state without having to check the [**Enabled**](/windows/desktop/api/RTSCom/nf-rtscom-irealtimestylus-get_enabled) property of the **RealTimeStylus** object.When a plug-in is added while the **RealTimeStylus** object is enabled, the plug-in data that the plug-in receives may not contain enough information to adequately establish the context of the initial data. For example, the newly added plug-in could start receiving packet data from a pen that is mid-stroke. Similarly, when a plug-in removed while the **RealTimeStylus** object is enabled, the plug-in data that the plug-in has received may be insufficient to finish processing the data.
    > [!Note]  
    > For overall stability, reset a plug-in's internal state when either its [**RealTimeStylusEnabled**](/windows/desktop/api/RTSCom/nf-rtscom-istylusplugin-realtimestylusenabled) or [**RealTimeStylusDisabled**](/windows/desktop/api/RTSCom/nf-rtscom-istylusplugin-realtimestylusdisabled) method is called.

     

-   The [**RealTimeStylus**](realtimestylus-class.md) object throws an exception if a plug-in modifies the plug-in collection to which it is attached. This happens only when the plug-in does so while it is being called by the **RealTimeStylus** object as a member of that collection.

 

 
