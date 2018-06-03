---
Description: The RealTimeStylus object does not inherently collect ink. To use the RealTimeStylus to collect ink, create an ink-collector plug-in.
ms.assetid: 9a29525d-714a-431e-bb6f-4705d658537b
title: Ink-Collection Plug-ins
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Ink-Collection Plug-ins

The [**RealTimeStylus**](/windows/desktop/api/RTSCom/) object does not inherently collect ink. To use the **RealTimeStylus** to collect ink, create an ink-collector plug-in.

The following is a minimal scenario for using the [**RealTimeStylus**](/windows/desktop/api/RTSCom/) object on a form that collects ink.

1.  Create a form that implements the [**IStylusAsyncPlugin**](/windows/desktop/api/RTSCom/) interface.
2.  Create a [**RealTimeStylus**](/windows/desktop/api/RTSCom/) object, and attach it to a control on the form.
3.  Set interest in the StylusDown, Packets, and StylusUp notifications in the form's [DataInterest](https://www.bing.com/search?q=DataInterest) property.
4.  In the form's [**StylusDown**](/windows/desktop/api/RTSCom/nf-rtscom-istylusplugin-stylusdown), [**Packets**](/windows/desktop/api/RTSCom/nf-rtscom-istylusplugin-packets), and [**StylusUp**](/windows/desktop/api/RTSCom/nf-rtscom-istylusplugin-stylusup) methods, add code to handle the stylus down, packets, and stylus up notifications that are sent from the form's [**RealTimeStylus**](/windows/desktop/api/RTSCom/) object. This code should store the pen data, and create and store the strokes.

For a sample of such an application, see the [RealTimeStylus Ink Collection Sample](realtimestylus-ink-collection-sample.md) sample.

> [!Note]  
> When a [DisplaySettingsChanged](https://www.bing.com/search?q=DisplaySettingsChanged) event occurs, call the [**ModifyDrawingAttributes**](/windows/desktop/api/msinkaut/) method of the collected strokes in a DisplaySettingsChanged event handler to recalculate the [Width](https://www.bing.com/search?q=Width) and [Height](https://www.bing.com/search?q=Height) properties. This is necessary to account for possible dots per inch (dpi) changes that result from the DisplaySettingsChanged event.

 

## Ink Collection and Recognizers

Neither ink analysis nor handwriting recognition is a function of the [**RealTimeStylus**](/windows/desktop/api/RTSCom/) object. As the ink-collector plug-in collects ink-or as you want to recognize the ink-you can copy the ink to a [RecognizerContext](https://www.bing.com/search?q=RecognizerContext) or [Divider](https://www.bing.com/search?q=Divider) object. For more information about recognition and ink analysis, see [About Handwriting Recognition](about-handwriting-recognition.md) or [The Divider Object](the-divider-object.md).

## Static Rendering

To render ink as it is being collected, attach a [DynamicRenderer](https://www.bing.com/search?q=DynamicRenderer) object to the [**RealTimeStylus**](/windows/desktop/api/RTSCom/) object. To render ink after it has been collected, use a [Renderer](https://www.bing.com/search?q=Renderer) object to draw the strokes to the appropriate [Graphics](https://www.bing.com/search?q=Graphics) object. For more information about the DynamicRenderer object, see [Dynamic-Renderer Plug-ins](dynamic-renderer-plug-ins.md). For a sample of both static and dynamic rendering, see [RealTimeStylus Ink Collection Sample](realtimestylus-ink-collection-sample.md).

 

 



