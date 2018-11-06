---
Description: The RealTimeStylus object does not inherently collect ink. To use the RealTimeStylus to collect ink, create an ink-collector plug-in.
ms.assetid: 9a29525d-714a-431e-bb6f-4705d658537b
title: Ink-Collection Plug-ins
ms.topic: article
ms.date: 05/31/2018
---

# Ink-Collection Plug-ins

The [**RealTimeStylus**](realtimestylus-class.md) object does not inherently collect ink. To use the **RealTimeStylus** to collect ink, create an ink-collector plug-in.

The following is a minimal scenario for using the [**RealTimeStylus**](realtimestylus-class.md) object on a form that collects ink.

1.  Create a form that implements the [**IStylusAsyncPlugin**](https://msdn.microsoft.com/en-us/library/ms702522(v=VS.85).aspx) interface.
2.  Create a [**RealTimeStylus**](realtimestylus-class.md) object, and attach it to a control on the form.
3.  Set interest in the StylusDown, Packets, and StylusUp notifications in the form's [DataInterest](https://msdn.microsoft.com/library/ms574886(v=VS.90).aspx) property.
4.  In the form's [**StylusDown**](/windows/desktop/api/RTSCom/nf-rtscom-istylusplugin-stylusdown), [**Packets**](/windows/desktop/api/RTSCom/nf-rtscom-istylusplugin-packets), and [**StylusUp**](/windows/desktop/api/RTSCom/nf-rtscom-istylusplugin-stylusup) methods, add code to handle the stylus down, packets, and stylus up notifications that are sent from the form's [**RealTimeStylus**](realtimestylus-class.md) object. This code should store the pen data, and create and store the strokes.

For a sample of such an application, see the [RealTimeStylus Ink Collection Sample](realtimestylus-ink-collection-sample.md) sample.

> [!Note]  
> When a [DisplaySettingsChanged](https://msdn.microsoft.com/library/xfdbbfk5(v=VS.90).aspx) event occurs, call the [**ModifyDrawingAttributes**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkstrokes-modifydrawingattributes) method of the collected strokes in a DisplaySettingsChanged event handler to recalculate the [Width](https://msdn.microsoft.com/library/ms582112(v=VS.90).aspx) and [Height](https://msdn.microsoft.com/library/ms582106(v=VS.90).aspx) properties. This is necessary to account for possible dots per inch (dpi) changes that result from the DisplaySettingsChanged event.

 

## Ink Collection and Recognizers

Neither ink analysis nor handwriting recognition is a function of the [**RealTimeStylus**](realtimestylus-class.md) object. As the ink-collector plug-in collects ink-or as you want to recognize the ink-you can copy the ink to a [RecognizerContext](https://msdn.microsoft.com/library/ms552546(v=VS.90).aspx) or [Divider](https://msdn.microsoft.com/library/ms583616(v=VS.90).aspx) object. For more information about recognition and ink analysis, see [About Handwriting Recognition](about-handwriting-recognition.md) or [The Divider Object](the-divider-object.md).

## Static Rendering

To render ink as it is being collected, attach a [DynamicRenderer](https://msdn.microsoft.com/library/ms575176(v=VS.90).aspx) object to the [**RealTimeStylus**](realtimestylus-class.md) object. To render ink after it has been collected, use a [Renderer](https://msdn.microsoft.com/library/ms552630(v=VS.90).aspx) object to draw the strokes to the appropriate [Graphics](https://msdn.microsoft.com/library/ac148eb3(v=VS.90).aspx) object. For more information about the DynamicRenderer object, see [Dynamic-Renderer Plug-ins](dynamic-renderer-plug-ins.md). For a sample of both static and dynamic rendering, see [RealTimeStylus Ink Collection Sample](realtimestylus-ink-collection-sample.md).

 

 



