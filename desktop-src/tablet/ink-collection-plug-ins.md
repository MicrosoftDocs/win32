---
Description: The RealTimeStylus object does not inherently collect ink. To use the RealTimeStylus to collect ink, create an ink-collector plug-in.
ms.assetid: 9a29525d-714a-431e-bb6f-4705d658537b
title: Ink-Collection Plug-ins
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Ink-Collection Plug-ins

The [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object does not inherently collect ink. To use the **RealTimeStylus** to collect ink, create an ink-collector plug-in.

The following is a minimal scenario for using the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object on a form that collects ink.

1.  Create a form that implements the [**IStylusAsyncPlugin**](/windows/win32/RTSCom/?branch=master) interface.
2.  Create a [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object, and attach it to a control on the form.
3.  Set interest in the StylusDown, Packets, and StylusUp notifications in the form's [DataInterest](P:Microsoft.StylusInput.IStylusAsyncPlugin.DataInterest) property.
4.  In the form's [**StylusDown**](/windows/win32/RTSCom/nf-rtscom-istylusplugin-stylusdown?branch=master), [**Packets**](/windows/win32/RTSCom/nf-rtscom-istylusplugin-packets?branch=master), and [**StylusUp**](/windows/win32/RTSCom/nf-rtscom-istylusplugin-stylusup?branch=master) methods, add code to handle the stylus down, packets, and stylus up notifications that are sent from the form's [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object. This code should store the pen data, and create and store the strokes.

For a sample of such an application, see the [RealTimeStylus Ink Collection Sample](realtimestylus-ink-collection-sample.md) sample.

> [!Note]  
> When a [DisplaySettingsChanged](E:Microsoft.Win32.SystemEvents.DisplaySettingsChanged) event occurs, call the [**ModifyDrawingAttributes**](/windows/win32/msinkaut/?branch=master) method of the collected strokes in a DisplaySettingsChanged event handler to recalculate the [Width](P:Microsoft.Ink.DrawingAttributes.Width) and [Height](P:Microsoft.Ink.DrawingAttributes.Height) properties. This is necessary to account for possible dots per inch (dpi) changes that result from the DisplaySettingsChanged event.

 

## Ink Collection and Recognizers

Neither ink analysis nor handwriting recognition is a function of the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object. As the ink-collector plug-in collects ink-or as you want to recognize the ink-you can copy the ink to a [RecognizerContext](T:Microsoft.Ink.RecognizerContext) or [Divider](T:Microsoft.Ink.Divider) object. For more information about recognition and ink analysis, see [About Handwriting Recognition](about-handwriting-recognition.md) or [The Divider Object](the-divider-object.md).

## Static Rendering

To render ink as it is being collected, attach a [DynamicRenderer](T:Microsoft.StylusInput.DynamicRenderer) object to the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object. To render ink after it has been collected, use a [Renderer](T:Microsoft.Ink.Renderer) object to draw the strokes to the appropriate [Graphics](T:System.Drawing.Graphics) object. For more information about the DynamicRenderer object, see [Dynamic-Renderer Plug-ins](dynamic-renderer-plug-ins.md). For a sample of both static and dynamic rendering, see [RealTimeStylus Ink Collection Sample](realtimestylus-ink-collection-sample.md).

 

 



