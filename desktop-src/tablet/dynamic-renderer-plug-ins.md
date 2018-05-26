---
Description: A dynamic-renderer plug-in is an object that displays the tablet pen data in real-time as it is being handled by the RealTimeStylus object.
ms.assetid: ac6d15f3-0917-4cc1-8c83-e34d3d063289
title: Dynamic-Renderer Plug-ins
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Dynamic-Renderer Plug-ins

A dynamic-renderer plug-in is an object that displays the tablet pen data in real-time as it is being handled by the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object. Later, for events such as a form refresh, the dynamic-renderer plug-in or an ink-collector plug-in may redraw the ink.

## The DynamicRenderer Object

The [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object implements the [**IStylusSyncPlugin**](/windows/win32/RTSCom/?branch=master) interface. The [**DynamicRenderer**](/windows/win32/RTSCom/?branch=master) object renders the ink in real-time, as it is being drawn. When the [**Refresh**](/windows/win32/RTSCom/nf-rtscom-idynamicrenderer-refresh?branch=master) method is called while the **DynamicRenderer** object is enabled, the **DynamicRenderer** object redraws the stroke currently being collected. The **DynamicRenderer** object's [**Enabled**](/windows/win32/RTSCom/nf-rtscom-idynamicrenderer-get_enabled?branch=master) property is initially set to **FALSE**.

> [!Note]  
> When calling the [**DynamicRenderer**](frlrfMicrosoftStylusInputDynamicRendererClassTopic) object's [**Refresh**](frlrfMicrosoftStylusInputDynamicRendererClassRefreshTopic) method from within a [Paint](frlrfSystemWindowsFormsControlClassPaintTopic) event handler in managed code, set the **DynamicRenderer** object's [**ClipRectangle**](frlrfMicrosoftStylusInputDynamicRendererClassClipRectangleTopic) property to the [PaintEventArgs](T:System.Windows.Forms.PaintEventArgs) object's [ClipRectangle](frlrfSystemWindowsFormsPaintEventArgsClassClipRectangleTopic) property.

 

The [**DynamicRenderer**](/windows/win32/RTSCom/?branch=master) object can temporarily cache ink data. To use this feature in managed code, set the [EnableDataCache](frlrfMicrosoftStylusInputDynamicRendererClassEnableDataCacheTopic) property to **TRUE**. When the [**DynamicRenderer**](frlrfmicrosoftstylusinputdynamicrendererclasstopic) object receives a call to its [**IStylusSyncPlugin.StylusUp**](frlrfmicrosoftstylusinputdynamicrendererclassmicrosoftstylusinputistylussyncpluginstylusuptopic) method, it caches the stroke data and adds custom stylus data to the Input queue in response to the [**StylusUpData**](frlrfmicrosoftstylusinputplugindatastylusupdataclasstopic) object for the stroke. The [**CustomStylusData**](frlrfmicrosoftstylusinputplugindatacustomstylusdataclasstopic) object's [CustomDataId](frlrfmicrosoftstylusinputplugindatacustomstylusdataclassdatatopic) property is set to the [DynamicRendererCachedDataGuid](frlrfmicrosoftstylusinputplugindatadynamicrenderercacheddataclasstopic) value, and the **CustomStylusData** object's Data property contains a DynamicRendererCachedData object. Call the **DynamicRenderer** object's [ReleaseCachedData](frlrfmicrosoftstylusinputdynamicrendererclassreleasecacheddatatopic) method once the stroke has been collected and can be statically rendered. When the [**Refresh**](/windows/win32/RTSCom/nf-rtscom-idynamicrenderer-refresh?branch=master) method is called while the **DynamicRenderer** object is enabled, the **DynamicRenderer** object redraws all strokes that are cached. When the [**DataCacheEnabled**](/windows/win32/RTSCom/nf-rtscom-idynamicrenderer-get_datacacheenabled?branch=master) property is set to **false**, the cached stroke data is deleted.

The following diagram illustrates how the [**DynamicRenderer**](/windows/win32/RTSCom/?branch=master) object adds data to the tablet pen data when the **DynamicRenderer** object's [**DataCacheEnabled**](/windows/win32/RTSCom/nf-rtscom-idynamicrenderer-get_datacacheenabled?branch=master) property is set.

![illustration showing the dynamicrenderer data flow](images/75f4ee7b-160c-410e-bfae-dfc676a9829c.gif)

In this diagram the circle lettered "SD" represents a [**StylusDown**](/windows/win32/RTSCom/nf-rtscom-istylusplugin-stylusdown?branch=master) object and the circles lettered "P" represent [**Packets**](/windows/win32/RTSCom/nf-rtscom-istylusplugin-packets?branch=master) objects that have already been added to the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object's output queue and that have not yet been sent to the asynchronous plug-in collection. The circle lettered "SU" represents a [**StylusUp**](/windows/win32/RTSCom/nf-rtscom-istylusplugin-stylusup?branch=master) object that the **RealTimeStylus** object is currently processing. It is sent to the synchronous plug-in collection and then placed on the output queue. The circles lettered "DR" represent custom stylus data that is added to the input queue by the [**DynamicRenderer**](/windows/win32/RTSCom/?branch=master) plug-in in response to the stylus up notification associated with "SU". The custom stylus data lettered "DR" is then passed to the synchronous plug-ins and then to the output queue before the next tablet pen data is processed. The empty circle represents the position in the output queue where future tablet pen data is added. Also represented on the diagram is the ink-collector plug-in calling the **DynamicRenderer** object's [**ReleaseCachedData**](/windows/win32/RTSCom/nf-rtscom-idynamicrenderer-releasecacheddata?branch=master) method to release the cached stroke data after the ink-collection plug-in has processed the stroke.

### Special Considerations

The following list describes other points to take into consideration when using the [**DynamicRenderer**](/windows/win32/RTSCom/?branch=master) object.

-   You should not attach a [**DynamicRenderer**](/windows/win32/RTSCom/?branch=master) object to more than one [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object. Once two **RealTimeStylus** objects to which the **DynamicRenderer** object is attached are enabled, the following occurs.

    -   The [**DynamicRenderer**](/windows/win32/RTSCom/?branch=master) object throws an exception in response to the second call to its [**RealTimeStylusEnabled**](/windows/win32/RTSCom/nf-rtscom-istylusplugin-realtimestylusenabled?branch=master) method.
    -   The second [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object that was enabled generates an [**Error**](/windows/win32/RTSCom/nf-rtscom-istylusplugin-error?branch=master) object and notifies the remaining plug-ins in its plug-in collections of the error.
    -   The [**DynamicRenderer**](/windows/win32/RTSCom/?branch=master) object stops rendering tablet pen data.

-   The [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object throws an exception when its [**AddCustomStylusDataToQueue**](/windows/win32/RTSCom/nf-rtscom-irealtimestylus-addcustomstylusdatatoqueue?branch=master) method is called with the *guid* parameter set to the DynamicRendererCachedDataGuid globally unique identifier (GUID).
-   The [**DynamicRenderer**](/windows/win32/RTSCom/?branch=master) object is implemented as a Component Object Model (COM) wrapper, and you cannot call its [**IStylusSyncPlugin**](/windows/win32/RTSCom/?branch=master) interface methods directly. For more information about COM operation and the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object, see [Implementation Notes for the StylusInput APIs](implementation-notes-for-the-stylusinput-apis.md).

## Custom Rendering

You can create your own dynamic-renderer plug-in by creating a synchronous plug-in that subscribes to the [**StylusDown**](/windows/win32/RTSCom/nf-rtscom-istylusplugin-stylusdown?branch=master), [**Packets**](/windows/win32/RTSCom/nf-rtscom-istylusplugin-packets?branch=master), and [**StylusUp**](/windows/win32/RTSCom/nf-rtscom-istylusplugin-stylusup?branch=master) notifications. Your plug-in can then render the stroke as it is being drawn. This may be one way of implementing a selection tool that uses a free-form selection or selection box, for example.

 

 



