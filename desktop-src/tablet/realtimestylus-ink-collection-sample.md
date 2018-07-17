---
Description: This application demonstrates ink collection and rendering when using the RealTimeStylus class.
ms.assetid: f8bce153-cc5d-4087-896f-3f60afc80bc8
title: RealTimeStylus Ink Collection Sample
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RealTimeStylus Ink Collection Sample

This application demonstrates ink collection and rendering when using the [**RealTimeStylus**](realtimestylus-class.md) class.

## The InkCollection Project

This sample consists of a single solution that contains one project, InkCollection. The application defines the `InkCollection` namespace that contains a single class, also called `InkCollection`. The class inherits from the [Form](T:System.Windows.Forms.Form) class and implements the [**IStylusAsyncPlugin**](https://msdn.microsoft.com/en-us/library/ms702522(v=VS.85).aspx) interface.


```C++
namespace InkCollection
{
    public class InkCollection : Form, IStylusAsyncPlugin
    {
        //...
      
```



The InkCollection Class defines a set of private constants used to specify various ink thickness. The class also declares private instances of the [**RealTimeStylus**](realtimestylus-class.md) class, `myRealTimeStylus`, the [**DynamicRenderer**](https://msdn.microsoft.com/en-us/library/ms701168(v=VS.85).aspx) class, `myDynamicRenderer`, and the [Renderer](frlrfMicrosoftInkRendererClassTopic) class `myRenderer`. The **DynamicRenderer** renders the [Stroke](frlrfMicrosoftInkStrokeClassTopic) that is currently being collected. The Renderer object, `myRenderer`, renders Stroke objects that have already been collected.


```C++
private const float ThinInkWidth = 10;
private const float MediumInkWidth = 100;
private const float ThickInkWidth = 200;

private RealTimeStylus myRealTimeStylus;

private DynamicRenderer myDynamicRenderer;
private Renderer myRenderer;
```



The class also declares a [Hashtable](T:System.Collections.Hashtable) object, `myPackets`, which is used to store packet data that is being collected by one or more [Cursor](frlrfMicrosoftInkCursorClassTopic) objects. The [Stylus](frlrfMicrosoftStylusInputStylusClassTopic) object's [Id](frlrfMicrosoftStylusInputStylusClassIdTopic) values are used as the hashtable key to uniquely identify the packet data collected for a given Cursor object.

A private instance of the [Ink](frlrfMicrosoftInkInkClassTopic) object, `myInk`, stores [Stroke](frlrfMicrosoftInkStrokeClassTopic) objects collected by `myRealTimeStylus`.


```C++
private Hashtable myPackets;
        
private Ink myInk;
```



## The Form Load Event

In the [Load](frlrfSystemWindowsFormsFormClassLoadTopic) event handler for the form, `myDynamicRenderer` is instantiated by using the [**DynamicRenderer**](https://msdn.microsoft.com/en-us/library/ms701168(v=VS.85).aspx) that takes a control as an argument, and `myRenderer` is constructed with a no-argument constructor.


```C++
private void InkCollection_Load(object sender, System.EventArgs e)
{
    myDynamicRenderer = new DynamicRenderer(this);
    myRenderer = new Renderer();
    // ...
```



Pay attention to the comment that follows the instantiation of the renderers, because `myDynamicRenderer` uses the default values for [DrawingAttributes](frlrfMicrosoftInkDrawingAttributesClassTopic) when rendering the ink. This is standard behavior. However, if you wish to give the ink rendered by `myDynamicRenderer` a different look from ink rendered by `myRenderer`, you can change the [DrawingAttributes](frlrfMicrosoftStylusInputDynamicRendererClassDrawingAttributesTopic) property on `myDynamicRenderer`. To do so, uncomment the following lines before you build and run the application.


```C++
    // myDynamicRenderer.DrawingAttributes.PenTip = PenTip.Rectangle;
    // myDynamicRenderer.DrawingAttributes.Height = (.5F)*MediumInkWidth;
    // myDynamicRenderer.DrawingAttributes.Transparency = 128;
```



Next, the application creates the [**RealTimeStylus**](realtimestylus-class.md) object that is used to receive stylus notifications and adds the [**DynamicRenderer**](https://msdn.microsoft.com/en-us/library/ms701168(v=VS.85).aspx) object to the synchronous plug-in notification queue. Specifically, `myRealTimeStylus` adds `myDynamicRenderer` to the [SyncPluginCollection](frlrfMicrosoftStylusInputRealTimeStylusClassSyncPluginCollectionTopic) property.


```C++
    myRealTimeStylus = new RealTimeStylus(this, true);

    myRealTimeStylus.SyncPluginCollection.Add(myDynamicRenderer);
```



The form is then added to the asynchronous plug-in notification queue. Specifically, `InkCollection` is added to the [AsyncPluginCollection](frlrfMicrosoftStylusInputRealTimeStylusClassAsyncPluginCollectionTopic) property. Finally, `myRealTimeStylus` and `myDynamicRenderer` are enabled, and myPackets and myInk are instantiated.


```C++
    myRealTimeStylus.AsyncPluginCollection.Add(this);

    myRealTimeStylus.Enabled = true;
    myDynamicRenderer.Enabled = true;  
      
    myPackets = new Hashtable();
    myInk = new Ink();
}
```



Aside from hooking up the menu handlers for changing ink color and size, one more brief block of code is required before implementing the interface. The sample must handle the form's [Paint](frlrfSystemWindowsFormsControlClassPaintTopic) event. In the event handler, the application must refresh `myDynamicRenderer` because it is possible that a [Stroke](frlrfMicrosoftInkStrokeClassTopic) object is being collected at the time the Paint event occurs. In that case, the portion of the Stroke object that has already been collected needs to be redrawn. The static [Renderer](frlrfMicrosoftInkRendererClassTopic) is used to re-draw Stroke objects that have already been collected. These strokes are in the [Ink](frlrfMicrosoftInkInkClassTopic) object because they are placed there when drawn, as shown in the next section.


```C++
private void InkCollection_Paint(object sender, System.Windows.Forms.PaintEventArgs e)
{
    myDynamicRenderer.Refresh();

    myRenderer.Draw(e.Graphics, myInk.Strokes);
} 
```



## Implementing the IStylusAsyncPlugin Interface

The sample application defines the types of notifications it has interest in receiving in the implementation of the [DataInterest](frlrfMicrosoftStylusInputIStylusAsyncPluginClassDataInterestTopic) property. The DataInterest property therefore defines which notifications that the [**RealTimeStylus**](realtimestylus-class.md) object forwards to the form. For this sample, the DataInterest property defines interest in the **StylusDown**, **Packets**, **StylusUp**, and **Error** notifications through the [DataInterestMask](frlrfMicrosoftStylusInputDataInterestMaskClassTopic) enumeration.


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
```



The [StylusDown](frlrfMicrosoftStylusInputIStylusAsyncPluginClassStylusDownTopic) notification occurs when the pen touches the digitizer surface. When this happens, the sample allocates an array that is used to store the packet data for the [Stylus](frlrfMicrosoftStylusInputStylusClassTopic) object. The [StylusDownData](frlrfMicrosoftStylusInputPluginDataStylusDownDataClassTopic) from the StylusDown method is added to the array, and the array is inserted into the hashtable by using the Stylus object's [Id](frlrfMicrosoftStylusInputStylusClassIdTopic) property as a key.


```C++
public void StylusDown(RealTimeStylus sender, StylusDownData data)
{
    ArrayList collectedPackets = new ArrayList();

    collectedPackets.AddRange(data.GetData());

    myPackets.Add(data.Stylus.Id, collectedPackets);
}
```



The [Packets](frlrfMicrosoftStylusInputIStylusAsyncPluginClassPacketsTopic) notification occurs when the pen moves on the digitizer surface. When this occurs, the application adds new [StylusDownData](frlrfMicrosoftStylusInputPluginDataStylusDownDataClassTopic) into the packet array for the [Stylus](frlrfMicrosoftStylusInputStylusClassTopic) object. It does this by using the Stylus object's [Id](frlrfMicrosoftStylusInputStylusClassIdTopic) property as the key to retrieve the packet array for the stylus from the hashtable. The new packet data is then inserted into the retrieved array.


```C++
public void Packets(RealTimeStylus sender, PacketsData data)
{
    ((ArrayList)(myPackets[data.Stylus.Id])).AddRange(data.GetData());
}
```



The [StylusUp](frlrfMicrosoftStylusInputIStylusAsyncPluginClassStylusUpTopic) notification occurs when the pen leaves the digitizer surface. When this notification occurs, the sample retrieves the packet array for this [Stylus](frlrfMicrosoftStylusInputStylusClassTopic) object from the hashtable-removing it from the hashtable as it is no longer needed, adds in the new packet data, and uses the array of packet data to create a new [Stroke](frlrfMicrosoftInkStrokeClassTopic) object, `stroke`.


```C++
public void StylusUp(RealTimeStylus sender, StylusUpData data)
{
    ArrayList collectedPackets = (ArrayList)myPackets[data.Stylus.Id];
    myPackets.Remove(data.Stylus.Id);

    collectedPackets.AddRange(data.GetData());

    int[] packets = (int[])(collectedPackets.ToArray(typeof(int)));
    TabletPropertyDescriptionCollection tabletProperties =
        myRealTimeStylus.GetTabletPropertyDescriptionCollection(data.Stylus.TabletContextId);

    Stroke stroke = myInk.CreateStroke(packets, tabletProperties);
    if (stroke != null) 
    {
         stroke.DrawingAttributes.Color = myDynamicRenderer.DrawingAttributes.Color;
         stroke.DrawingAttributes.Width = myDynamicRenderer.DrawingAttributes.Width;
    } 
}
```



For an example that shows more robust use of the [**RealTimeStylus**](realtimestylus-class.md) class, including the use of custom plug-in creation, see [RealTimeStylus Plug-in Sample](realtimestylus-plug-in-sample.md).

## Related topics

<dl> <dt>

[Microsoft.Ink.Renderer](frlrfMicrosoftInkRendererClassTopic)
</dt> <dt>

[Microsoft.StylusInput.DynamicRenderer](frlrfMicrosoftStylusInputDynamicRendererClassTopic)
</dt> <dt>

[Microsoft.StylusInput.RealTimeStylus](frlrfMicrosoftStylusInputRealTimeStylusClassTopic)
</dt> <dt>

[Microsoft.StylusInput.IStylusAsyncPlugin](frlrfMicrosoftStylusInputIStylusAsyncPluginClassTopic)
</dt> <dt>

[Accessing and Manipulating Stylus Input](accessing-and-manipulating-stylus-input.md)
</dt> </dl>

 

 



