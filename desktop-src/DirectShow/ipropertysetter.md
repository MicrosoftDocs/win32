---
description: The IPropertySetter interface sets properties on an effect or transition in DirectShow Editing Services (DES).To use this interface, create an instance of a property setter object (CLSID\_PropertySetter), and associate it with an effect or transition by calling the IAMTimelineObj::SetPropertySetter method. For more information, see Working with Effects and Transitions.Usually an application needs to call only the IPropertySetter::ClearProps method to clear existing properties, and the IPropertySetter::AddProp method to add new properties. The other methods on this interface are called by other DES components.
ms.assetid: bee2abf2-0abc-4890-b1f2-7d0011444fbd
title: IPropertySetter interface (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPropertySetter
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IPropertySetter interface

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IPropertySetter` interface sets properties on an effect or transition in [DirectShow Editing Services](directshow-editing-services.md) (DES).

To use this interface, create an instance of a property setter object (CLSID\_PropertySetter), and associate it with an effect or transition by calling the [**IAMTimelineObj::SetPropertySetter**](iamtimelineobj-setpropertysetter.md) method. For more information, see [Working with Effects and Transitions](working-with-effects-and-transitions.md).

Usually an application needs to call only the [**IPropertySetter::ClearProps**](ipropertysetter-clearprops.md) method to clear existing properties, and the [**IPropertySetter::AddProp**](ipropertysetter-addprop.md) method to add new properties. The other methods on this interface are called by other DES components.

## Members

The **IPropertySetter** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IPropertySetter** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPropertySetter** interface has these methods.



| Method                                               | Description                                                                                                                                   |
|:-----------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddProp**](ipropertysetter-addprop.md)           | Adds a property to the property setter, with an array of time-value pairs defining the value of the property over a range of time.<br/> |
| [**ClearProps**](ipropertysetter-clearprops.md)     | Clears all property data from the property setter.<br/>                                                                                 |
| [**CloneProps**](ipropertysetter-cloneprops.md)     | Clones a set of properties from this property setter and adds them to a new property setter.<br/>                                       |
| [**FreeProps**](ipropertysetter-freeprops.md)       | Frees resources allocated by the [**IPropertySetter::GetProps**](ipropertysetter-getprops.md) method.<br/>                             |
| [**GetProps**](ipropertysetter-getprops.md)         | Retrieves the properties set on this object, with their corresponding values.<br/>                                                      |
| [**LoadFromBlob**](ipropertysetter-loadfromblob.md) | Loads property data from a persistence format.<br/>                                                                                     |
| [**LoadXML**](ipropertysetter-loadxml.md)           | Loads property data expressed in Extensible Markup Language (XML).<br/>                                                                 |
| [**PrintXML**](ipropertysetter-printxml.md)         | Converts property data into an XML string.<br/>                                                                                         |
| [**SaveToBlob**](ipropertysetter-savetoblob.md)     | Saves the property data to a persistence format.<br/>                                                                                   |
| [**SetProps**](ipropertysetter-setprops.md)         | Sets the properties of the target object to the appropriate state for the specified time.<br/>                                          |



 

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



 

 
