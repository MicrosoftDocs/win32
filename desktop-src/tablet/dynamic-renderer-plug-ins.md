---
Description: 'A dynamic-renderer plug-in is an object that displays the tablet pen data in real-time as it is being handled by the RealTimeStylus object.'
ms.assetid: 'ac6d15f3-0917-4cc1-8c83-e34d3d063289'
title: 'Dynamic-Renderer Plug-ins'
---

# Dynamic-Renderer Plug-ins

A dynamic-renderer plug-in is an object that displays the tablet pen data in real-time as it is being handled by the [**RealTimeStylus**](realtimestylus-class.md) object. Later, for events such as a form refresh, the dynamic-renderer plug-in or an ink-collector plug-in may redraw the ink.

## The DynamicRenderer Object

The [**RealTimeStylus**](realtimestylus-class.md) object implements the [**IStylusSyncPlugin**](istylussyncplugin.md) interface. The [**DynamicRenderer**](dynamicrenderer-class.md) object renders the ink in real-time, as it is being drawn. When the [**Refresh**](idynamicrenderer-refresh.md) method is called while the **DynamicRenderer** object is enabled, the **DynamicRenderer** object redraws the stroke currently being collected. The **DynamicRenderer** object's [**Enabled**](idynamicrenderer-enabled.md) property is initially set to **FALSE**.

> [!Note]  
> When calling the [**DynamicRenderer**](frlrfMicrosoftStylusInputDynamicRendererClassTopic) object's [**Refresh**](frlrfMicrosoftStylusInputDynamicRendererClassRefreshTopic) method from within a [Paint](frlrfSystemWindowsFormsControlClassPaintTopic) event handler in managed code, set the **DynamicRenderer** object's [**ClipRectangle**](frlrfMicrosoftStylusInputDynamicRendererClassClipRectangleTopic) property to the [PaintEventArgs](T:System.Windows.Forms.PaintEventArgs) object's [ClipRectangle](frlrfSystemWindowsFormsPaintEventArgsClassClipRectangleTopic) property.

 

The [**DynamicRenderer**](dynamicrenderer-class.md) object can temporarily cache ink data. To use this feature in managed code, set the [EnableDataCache](frlrfMicrosoftStylusInputDynamicRendererClassEnableDataCacheTopic) property to **TRUE**. When the [**DynamicRenderer**](frlrfmicrosoftstylusinputdynamicrendererclasstopic) object receives a call to its [**IStylusSyncPlugin.StylusUp**](frlrfmicrosoftstylusinputdynamicrendererclassmicrosoftstylusinputistylussyncpluginstylusuptopic) method, it caches the stroke data and adds custom stylus data to the Input queue in response to the [**StylusUpData**](frlrfmicrosoftstylusinputplugindatastylusupdataclasstopic) object for the stroke. The [**CustomStylusData**](frlrfmicrosoftstylusinputplugindatacustomstylusdataclasstopic) object's [CustomDataId](frlrfmicrosoftstylusinputplugindatacustomstylusdataclassdatatopic) property is set to the [DynamicRendererCachedDataGuid](frlrfmicrosoftstylusinputplugindatadynamicrenderercacheddataclasstopic) value, and the **CustomStylusData** object's Data property contains a DynamicRendererCachedData object. Call the **DynamicRenderer** object's [ReleaseCachedData](frlrfmicrosoftstylusinputdynamicrendererclassreleasecacheddatatopic) method once the stroke has been collected and can be statically rendered. When the [**Refresh**](idynamicrenderer-refresh.md) method is called while the **DynamicRenderer** object is enabled, the **DynamicRenderer** object redraws all strokes that are cached. When the [**DataCacheEnabled**](idynamicrenderer-datacacheenabled.md) property is set to **false**, the cached stroke data is deleted.

The following diagram illustrates how the [**DynamicRenderer**](dynamicrenderer-class.md) object adds data to the tablet pen data when the **DynamicRenderer** object's [**DataCacheEnabled**](idynamicrenderer-datacacheenabled.md) property is set.

![illustration showing the dynamicrenderer data flow](images/75f4ee7b-160c-410e-bfae-dfc676a9829c.gif)

In this diagram the circle lettered "SD" represents a [**StylusDown**](istylusplugin-stylusdown.md) object and the circles lettered "P" represent [**Packets**](istylusplugin-packets.md) objects that have already been added to the [**RealTimeStylus**](realtimestylus-class.md) object's output queue and that have not yet been sent to the asynchronous plug-in collection. The circle lettered "SU" represents a [**StylusUp**](istylusplugin-stylusup.md) object that the **RealTimeStylus** object is currently processing. It is sent to the synchronous plug-in collection and then placed on the output queue. The circles lettered "DR" represent custom stylus data that is added to the input queue by the [**DynamicRenderer**](dynamicrenderer-class.md) plug-in in response to the stylus up notification associated with "SU". The custom stylus data lettered "DR" is then passed to the synchronous plug-ins and then to the output queue before the next tablet pen data is processed. The empty circle represents the position in the output queue where future tablet pen data is added. Also represented on the diagram is the ink-collector plug-in calling the **DynamicRenderer** object's [**ReleaseCachedData**](idynamicrenderer-releasecacheddata.md) method to release the cached stroke data after the ink-collection plug-in has processed the stroke.

### Special Considerations

The following list describes other points to take into consideration when using the [**DynamicRenderer**](dynamicrenderer-class.md) object.

-   You should not attach a [**DynamicRenderer**](dynamicrenderer-class.md) object to more than one [**RealTimeStylus**](realtimestylus-class.md) object. Once two **RealTimeStylus** objects to which the **DynamicRenderer** object is attached are enabled, the following occurs.

    -   The [**DynamicRenderer**](dynamicrenderer-class.md) object throws an exception in response to the second call to its [**RealTimeStylusEnabled**](istylusplugin-realtimestylusenabled.md) method.
    -   The second [**RealTimeStylus**](realtimestylus-class.md) object that was enabled generates an [**Error**](istylusplugin-error.md) object and notifies the remaining plug-ins in its plug-in collections of the error.
    -   The [**DynamicRenderer**](dynamicrenderer-class.md) object stops rendering tablet pen data.

-   The [**RealTimeStylus**](realtimestylus-class.md) object throws an exception when its [**AddCustomStylusDataToQueue**](irealtimestylus-addcustomstylusdatatoqueue.md) method is called with the *guid* parameter set to the DynamicRendererCachedDataGuid globally unique identifier (GUID).
-   The [**DynamicRenderer**](dynamicrenderer-class.md) object is implemented as a Component Object Model (COM) wrapper, and you cannot call its [**IStylusSyncPlugin**](istylussyncplugin.md) interface methods directly. For more information about COM operation and the [**RealTimeStylus**](realtimestylus-class.md) object, see [Implementation Notes for the StylusInput APIs](implementation-notes-for-the-stylusinput-apis.md).

## Custom Rendering

You can create your own dynamic-renderer plug-in by creating a synchronous plug-in that subscribes to the [**StylusDown**](istylusplugin-stylusdown.md), [**Packets**](istylusplugin-packets.md), and [**StylusUp**](istylusplugin-stylusup.md) notifications. Your plug-in can then render the stroke as it is being drawn. This may be one way of implementing a selection tool that uses a free-form selection or selection box, for example.

 

 



