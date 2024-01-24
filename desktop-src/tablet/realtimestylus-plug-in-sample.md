---
description: This application demonstrates working with the RealTimeStylus class.
ms.assetid: 0ba753d1-d81a-4f7a-942c-2967c46febec
title: RealTimeStylus Plug-in Sample
ms.topic: article
ms.date: 05/31/2018
---

# RealTimeStylus Plug-in Sample

This application demonstrates working with the [**RealTimeStylus**](realtimestylus-class.md) class. For a detailed overview of the StylusInput APIs, including the **RealTimeStylus** class, see [Accessing and Manipulating Stylus Input](accessing-and-manipulating-stylus-input.md). For information about synchronous and asynchronous plug-ins, see [Plug-ins and the RealTimeStylus Class](plug-ins-and-the-realtimestylus-class.md).

## Overview of the Sample

Plug-ins, objects that implement the [**IStylusSyncPlugin**](/windows/win32/api/rtscom/nn-rtscom-istylussyncplugin) or [**IStylusAsyncPlugin**](/windows/win32/api/rtscom/nn-rtscom-istylusasyncplugin) interface can be added to a [**RealTimeStylus**](realtimestylus-class.md) object. This sample application uses several types of plug-in:

-   Packet Filter Plug-in: Modifies packets. The packet filter plug-in in this sample modifies packet information by constraining all (x,y) packet data within a rectangular area.
-   Custom Dynamic Renderer Plug-in: Modifies dynamic rendering qualities. The custom dynamic rendering plug-in in this sample modifies the way ink is rendered by drawing a small circle around each (x,y) point on a stroke.
-   Dynamic Renderer Plug-in: Modifies dynamic rendering qualities. This sample demonstrates use of the [**DynamicRenderer**](/previous-versions/windows/desktop/legacy/ms701168(v=vs.85)) object as a plug-in to handle dynamic rendering of ink.
-   Gesture Recognizer Plug-in: Recognizes application gestures. This sample demonstrates use of the [**GestureRecognizer**](gesturerecognizer-class.md) object as a plug-in to recognize application gestures (when running on a system with the Microsoft gesture recognizer present).

In addition, this sample provides a user interface that enables the user to add, remove, and change the order of each plug-in in the collection. The sample solution contains two projects, RealTimeStylusPluginApp and RealTimeStylusPlugins. RealTimeStylusPluginApp contains the user interface for the sample. RealTimeStylusPlugins contains the implementations of the plug-ins. The RealTimeStylusPlugins project defines the RealTimeStylusPlugins namespace, which contains the packet filter and custom dynamic renderer plug-ins. This namespace is referenced by the RealTimeStylusPluginApp project. The RealTimeStylusPlugins project uses the [Microsoft.Ink](/previous-versions/ms826516(v=msdn.10)), [Microsoft.StylusInput](/previous-versions/ms824750(v=msdn.10)), and [Microsoft.StylusInput.PluginData](/previous-versions/ms823992(v=msdn.10)) namespaces.

For an overview of the [Microsoft.StylusInput](/previous-versions/ms824750(v=msdn.10)) and [Microsoft.StylusInput.PluginData](/previous-versions/ms823992(v=msdn.10)) namespaces see [Architecture of the StylusInput APIs](architecture-of-the-stylusinput-apis.md).

## Packet Filter Plug-in

The packet filter plug-in is a synchronous plug-in that demonstrates packet modification. Specifically, it defines a rectangle on the form. Any packets that are drawn outside the region are rendered inside the region. The plug-in class, `PacketFilterPlugin`, registers for notification of `StylusDown`, `StylusUp`, and `Packets` pen input events. The class implements the [StylusDown](/previous-versions/ms824761(v=msdn.10)), [StylusUp](/previous-versions/ms824764(v=msdn.10)), and [Packets](/previous-versions/ms824756(v=msdn.10)) methods defined on [**IStylusSyncPlugin**](/windows/win32/api/rtscom/nn-rtscom-istylussyncplugin) class.

The public constructor for `PacketFilterPlugin` requires a [Rectangle](/dotnet/api/system.drawing.rectangle?view=netcore-3.1&preserve-view=true) structure. This rectangle defines the rectangular area, in ink space coordinates (.01mm = 1 HIMETRIC unit), in which packets will be contained. The rectangle is held in a private field, `rectangle`.


```C++
public class PacketFilterPlugin:IStylusSyncPlugin  
{
    private System.Drawing.Rectangle rectangle = System.Drawing.Rectangle.Empty;
    public PacketFilterPlugin(Rectangle r)
    {
        rectangle = r;
    }
    // ...
```



The `PacketFilterPlugin` class registers for event notifications by implementing the get accessor for the [DataInterest](/previous-versions/ms824752(v=msdn.10)) property. In this case, the plug-in has interested in responding to the `StylusDown`, `Packets`, `StylusUp`, and `Error` notifications. The sample returns these values as defined in the [DataInterestMask](/previous-versions/ms824787(v=msdn.10)) enumeration. The [StylusDown](/previous-versions/ms824761(v=msdn.10)) method is called when the pen tip contacts the digitizer surface. The [StylusUp](/previous-versions/ms824764(v=msdn.10)) method is called when the pen tip leaves the digitizer surface. The [Packets](/previous-versions/ms824756(v=msdn.10)) method is called when the [**RealTimeStylus**](realtimestylus-class.md) object receives packets. The [Error](/previous-versions/ms585069(v=vs.100)) method is called when the current plug-in or a previous plug-in throws an exception.


```C++
public DataInterestMask DataInterest
{
    get
    {
        return DataInterestMask.StylusDown | 
               DataInterestMask.Packets | 
               DataInterestMask.StylusUp | 
               DataInterestMask.Error;
    }
}           
    //...
```



The `PacketFilterPlugin` class handles most of these notifications in a helper method, `ModifyPacketData`. The `ModifyPacketData` method gets the x and y values for each new packet from the [PacketsData](/previous-versions/ms824590(v=msdn.10)) class. If either value is outside the rectangle, the method replaces the value with the nearest point that still falls within the rectangle. This is an example of how a plug-in can replace packet data as it is received from the pen-input stream.


```C++
private void ModifyPacketData(StylusDataBase data)
{
    for (int i = 0; i < data.Count ; i += data.PacketPropertyCount)
    {
        // packet data always has x followed by y followed by the rest
        int x = data[i];
        int y = data[i+1];

        // Constrain points to the input rectangle
        x = Math.Max(x, rectangle.Left);
        x = Math.Min(x, rectangle.Right);
        y = Math.Max(y, rectangle.Top);
        y = Math.Min(y, rectangle.Bottom);

        // If necessary, modify the x,y packet data
        if (x != data[i])
        {
            data[i] = x;
        }
        if (y != data[i+1])
        {
            data[i+1] = y;
        } 
    }
}
```



## Custom Dynamic Renderer Plug-in

The `CustomDynamicRenderer` class also implements the [**IStylusSyncPlugin**](/windows/win32/api/rtscom/nn-rtscom-istylussyncplugin) class to receive pen-input notifications. It then handles the `Packets` notification to draw a small circle around each new packet point.

The class contains a [Graphics](/dotnet/api/system.drawing.graphics?view=dotnet-plat-ext-3.1&preserve-view=true) variable that holds a reference to the graphics object passed into the class constructor. This is the graphics object used for dynamic rendering.


```C++
private Graphics myGraphics;

public CustomDynamicRendererPlugin(Graphics g)
{
    myGraphics = g;
}
        //...
            
```



When the custom dynamic renderer plug-in receives a Packets notification, it extracts the (x,y) data and draws a small green circle around the point. This is an example of custom rendering based on the pen-input stream.


```C++
public void Packets(RealTimeStylus sender,  PacketsData data)
{           
    for (int i = 0; i < data.Count; i += data.PacketPropertyCount)
    {
        // Packet data always has x followed by y followed by the rest
        Point point = new Point(data[i], data[i+1]);

        // Since the packet data is in Ink Space coordinates, we need to convert to Pixels...
        point.X = (int)Math.Round((float)point.X * (float)myGraphics.DpiX/2540.0F);
        point.Y = (int)Math.Round((float)point.Y * (float)myGraphics.DpiY/2540.0F);

        // Draw a circle corresponding to the packet
        myGraphics.DrawEllipse(Pens.Green, point.X - 2, point.Y - 2, 4, 4);
    }
}
```



## The RealTimeStylusPluginApp Project

The RealTimeStylusPluginApp project demonstrates the plug-ins previously described, as well as the [**GestureRecognizer**](gesturerecognizer-class.md) and [**DynamicRenderer**](/previous-versions/windows/desktop/legacy/ms701168(v=vs.85)) plug-ins. The project's user interface consists of:

-   A Form that contains a [GroupBox](/dotnet/api/system.windows.forms.groupbox?view=netcore-3.1&preserve-view=true) control used to define the ink entry area.
-   A [CheckedListBox](/dotnet/api/system.windows.forms.checkedlistbox?view=netcore-3.1&preserve-view=true) control to list and select the available plug-ins.
-   A pair of [Button objects](/dotnet/api/system.windows.forms.button?view=netcore-3.1&preserve-view=true) to enable re-ordering the plug-ins.

The project defines a structure, `PlugInListItem`, to make managing the plug-ins used in the project easier. The `PlugInListItem` structure contains the plug-in and a description.

The `RealTimeStylusPluginApp` class itself implements the [**IStylusAsyncPlugin**](/windows/win32/api/rtscom/nn-rtscom-istylusasyncplugin) class. This is necessary so that the `RealTimeStylusPluginApp` class can be notified when the [**GestureRecognizer**](gesturerecognizer-class.md) plug-in adds gesture data to the output queue. The application registers for notification of [CustomStylusDataAdded](/previous-versions/ms824753(v=msdn.10)). When gesture data is received, `RealTimeStylusPluginApp` places a description of it on the status bar at the bottom of the form.


```C++
public void CustomStylusDataAdded(RealTimeStylus sender, CustomStylusData data)
{
    if (data.CustomDataId == GestureRecognizer.GestureRecognitionDataGuid)
    {
        GestureRecognitionData grd = data.Data as GestureRecognitionData;
        if (grd != null)
        {
            if (grd.Count > 0)
            {
                GestureAlternate ga = grd[0];
                sbGesture.Text = "Gesture=" + ga.Id + ", Confidence=" + ga.Confidence;
            }
        }
    }
}
```



> [!Note]  
> In the [CustomStylusDataAdded](/previous-versions/ms824753(v=msdn.10)) implementation, it is interesting that you can identify the custom gesture data in the output queue either by GUID (by using the [GestureRecognitionDataGuid](/previous-versions/ms826344(v=msdn.10)) field) or by type (by using the result from the as statement). The sample uses both identification techniques for demonstration purposes. Either approach alone is also valid.

 

In the Form's Load event handler, the application creates instances of the `PacketFilter` and `CustomDynamicRenderer` classes and adds them to the list box. The application then attempts to create an instance of the [**GestureRecognizer**](gesturerecognizer-class.md) class and, if successful, adds it to the list box. This fails if the gesture recognizer is not present on the system. Next, the application instantiates a [**DynamicRenderer**](/previous-versions/windows/desktop/legacy/ms701168(v=vs.85)) object and adds it to the list box. Finally, the application enables each of the plug-ins and the [**RealTimeStylus**](realtimestylus-class.md) object itself.

Another important thing to note about the sample is that in the helper methods, the [**RealTimeStylus**](realtimestylus-class.md) object is first disabled before plug-ins are added or removed and then re-enabled after the addition or removal is complete.


```C++
private void RemoveFromPluginCollection(int index)
{
    IStylusSyncPlugin plugin = ((PluginListItem)chklbPlugins.Items[index]).Plugin;

    bool rtsEnabled = myRealTimeStylus.Enabled;
    myRealTimeStylus.Enabled = false;
    myRealTimeStylus.SyncPluginCollection.Remove(plugin);
    myRealTimeStylus.Enabled = rtsEnabled;
}
```



## Related topics

<dl> <dt>

[Microsoft.StylusInput.DynamicRenderer](/previous-versions/ms575176(v=vs.100))
</dt> <dt>

[Microsoft.StylusInput.GestureRecognizer](/previous-versions/ms826046(v=msdn.10))
</dt> <dt>

[Microsoft.StylusInput.RealTimeStylus](/previous-versions/ms824830(v=msdn.10))
</dt> <dt>

[Microsoft.StylusInput.DataInterestMask](/previous-versions/ms575174(v=vs.100))
</dt> <dt>

[Microsoft.StylusInput.IStylusSyncPlugin](/previous-versions/ms824751(v=msdn.10))
</dt> <dt>

[Microsoft.StylusInput.IStylusAsyncPlugin](/previous-versions/ms824768(v=msdn.10))
</dt> <dt>

[Microsoft.StylusInput.PluginData.PacketsData](/previous-versions/ms575281(v=vs.100))
</dt> <dt>

[Accessing and Manipulating Stylus Input](accessing-and-manipulating-stylus-input.md)
</dt> <dt>

[Plug-ins and the RealTimeStylus Class](plug-ins-and-the-realtimestylus-class.md)
</dt> <dt>

[RealTimeStylus Ink Collection Sample](realtimestylus-ink-collection-sample.md)
</dt> </dl>

 

 
