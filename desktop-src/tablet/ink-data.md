---
description: After the ink is collected, applications can manage, manipulate, and/or transfer that data to other media.
ms.assetid: 5a8c370e-79cb-47f0-a7b3-a631874ad757
title: Ink Data
ms.topic: article
ms.date: 05/31/2018
---

# Ink Data

After the ink is collected, applications can manage, manipulate, and/or transfer that data to other media. The actions of selecting, copying, moving, saving, viewing, and altering of the ink take place on the [**Ink**](inkdisp-class.md) object and its contained members, such as the [**Strokes**](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection and [**Stroke**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) objects.

> [!Note]  
> Using Real-Time Stylus, applications may choose to maintain data in its own format (such as saving strokes).

 

## Ink, Strokes, and Packets

An [**Ink**](inkdisp-class.md) object is the fundamental data type that manages, manipulates, and stores the input collected from the [**InkCollector**](inkcollector-class.md) object. An **Ink** object contains one or more [**Stroke**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) objects and common methods and properties to manage and manipulate those strokes. A stroke is defined as the set of data that is captured in a single pen-down, pen-move, and pen-up sequence. The stroke data contains a collection of packets. A packet is the set of data that the tablet device sends at each sample point. This data contains information such as coordinates, pen pressure, pen angle, and anything else that the hardware can transmit. The [**PacketDescription**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkstrokedisp-get_packetdescription) property of the **Stroke** object describes the packets that a [**Tablet**](/windows/desktop/api/msinkaut/nn-msinkaut-iinktablet) generates.

## Strokes

You can obtain a snapshot of the strokes in a [**Ink**](inkdisp-class.md) object by using the **Ink** object's [**Strokes**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-get_strokes) property. The **Strokes** property is a collection of references to the strokes in the **Ink** object at the time the **Strokes** property is read. If strokes are subsequently added to or deleted from the **Ink** object, a previously obtained [**Strokes**](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection is not updated. Furthermore, the **Strokes** property is a value and, like any value, goes out of scope unless it is assigned to a variable.

To keep a [**Strokes**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-get_strokes) property synchronized with an [**Ink**](inkdisp-class.md) object, wrap it in an event handler for the [**StrokesAdded**](inkstrokes-strokesadded.md) and [**StrokesRemoved**](inkstrokes-strokesremoved.md) events on the [**Strokes**](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection. The handler should obtain a new copy of the **Strokes** property when either event is fired. Be careful not to add the event handler to a **Strokes** collection that is out of scope before the event is fired.

Notice in this example that `theAddedStrokesIDs` is updated with a new copy of the strokes property in the `StrokesAdded_Event` handler.


```C++
public void StrokesAdded_Event(object sender, StrokesEventArgs e)
{
    int [] theAddedStrokesIDs = e.StrokeIds;
    theListBox.Items.Clear();
    foreach (int i in theAddedStrokesIDs)
    {
        theListBox.Items.Add("Added Stroke ID: " + i.ToString());
    }
}
```



## PacketDescription Property

The [**Ink**](inkdisp-class.md) object's [**PacketDescription**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkstrokedisp-get_packetdescription) property defines the set of information in each packet that the application gets from a Tablet PC device. The information typically includes coordinates, but it can include much more detailed information (depending on what the capabilities of Tablet PC digitizer) such as pen pressure or pen angle. By setting packet descriptions on the [**InkCollector**](inkcollector-class.md) or [**InkOverlay**](inkoverlay-class.md) object before any ink is collected (using the DesiredPacketDescription property), you have full control over which of the Tablet PC devices properties you want to receive.

## Extended Properties

Extended properties provide a mechanism for attaching application-defined data to [**Ink**](inkdisp-class.md) and other objects. For more information about extended properties, see the [**ExtendedProperties**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkextendedproperties) collection.

## Ink Rendering

The [**Renderer**](inkrenderer-class.md) object is responsible for rendering [**Ink**](inkdisp-class.md). Given an appropriate tablet context, the **Renderer** object can map ink space coordinates to pixels, apply view transforms, and display ink on screens and printers. The [**Draw**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-draw) and [**DrawStroke**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-drawstroke) methods are the primary methods for rendering ink. For more information about displaying ink in a window, see the **Renderer** object.

## Cusps

A stroke normally begins when the pen is lowered to the drawing surface and ends when the pen is raised. Within a stroke, the peaks, angles, and radical changes of direction are called cusps. The endpoints of a stroke are also considered cusps. For example, the capital letter "L" has three cusps, one in the middle and one at each end.

As a stroke is entered, it is normally smoothed and rendered using a Bezier (or polyline) curve. Bezier curves may turn cusps into small loops. For example, the peak of the cursive letter "i" might be smoothed to resemble the cursive "e". To prevent this, Microsoft renderers have a "pre-Bezier" phase that handles the cusps differently.

Cusps can also be used to subdivide [**Stroke**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) objects into erasable units. For example, selecting the vertical side of a capital "L" could indicate erasing just that side. The part of the stroke to be erased would be the part between two cusps.

 

 
