---
description: The IDxtJpeg interface sets properties on the SMPTE Wipe transition.This interface is used internally by DirectShow Editing Services (DES) when it renders the SMPTE Wipe transition.
ms.assetid: ce1920d4-ebe5-42d1-a2eb-d71ddeaf14fe
title: IDxtJpeg interface (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDxtJpeg
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IDxtJpeg interface

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IDxtJpeg` interface sets properties on the [SMPTE Wipe](smpte-wipe-transition.md) transition.

This interface is used internally by DirectShow Editing Services (DES) when it renders the SMPTE Wipe transition. DES applications do not need to use this interface. To set the properties on a transition in DES, use the [**IPropertySetter**](ipropertysetter.md) interface.

## Members

The **IDxtJpeg** interface inherits from **IDXEffect**. **IDxtJpeg** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDxtJpeg** interface has these methods.



| Method                                                     | Description                                                                               |
|:-----------------------------------------------------------|:------------------------------------------------------------------------------------------|
| [**ApplyChanges**](idxtjpeg-applychanges.md)              | Applies any properties that have changed.<br/>                                      |
| [**get\_BorderColor**](idxtjpeg-get-bordercolor.md)       | Retrieves the color of the border around the edges of the wipe pattern.<br/>        |
| [**get\_BorderSoftness**](idxtjpeg-get-bordersoftness.md) | Retrieves the width of the blurry region around the edges of the wipe pattern.<br/> |
| [**get\_BorderWidth**](idxtjpeg-get-borderwidth.md)       | Retrieves the width of the solid border along the edges of the wipe pattern.<br/>   |
| [**get\_MaskName**](idxtjpeg-get-maskname.md)             | Retrieves the name of a JPEG file to be used as the wipe mask.<br/>                 |
| [**get\_MaskNum**](idxtjpeg-get-masknum.md)               | Retrieves the SMPTE wipe code of the wipe.<br/>                                     |
| [**get\_OffsetX**](idxtjpeg-get-offsetx.md)               | Retrieves the horizontal offset of the wipe origin.<br/>                            |
| [**get\_OffsetY**](idxtjpeg-get-offsety.md)               | Retrieves the vertical offset of the wipe origin.<br/>                              |
| [**get\_ReplicateX**](idxtjpeg-get-replicatex.md)         | Retrieves the number of times the wipe pattern is replicated horizontally.<br/>     |
| [**get\_ReplicateY**](idxtjpeg-get-replicatey.md)         | Retrieves the number of times the wipe pattern is replicated vertically.<br/>       |
| [**get\_ScaleX**](idxtjpeg-get-scalex.md)                 | Retrieves the amount by which the wipe is stretched horizontally.<br/>              |
| [**get\_ScaleY**](idxtjpeg-get-scaley.md)                 | Retrieves the amount by which the wipe is stretched vertically.<br/>                |
| [**LoadDefSettings**](idxtjpeg-loaddefsettings.md)        | Restores the default settings of the Wipe transition.<br/>                          |
| [**put\_BorderColor**](idxtjpeg-put-bordercolor.md)       | Specifies the color of the border around the edges of the wipe pattern.<br/>        |
| [**put\_BorderSoftness**](idxtjpeg-put-bordersoftness.md) | Specifies the width of the blurry region around the edges of the wipe pattern.<br/> |
| [**put\_BorderWidth**](idxtjpeg-put-borderwidth.md)       | Specifies the width of the solid border along the edges of the wipe pattern.<br/>   |
| [**put\_MaskName**](idxtjpeg-put-maskname.md)             | Specifies the name of a JPEG file to use as the wipe mask.<br/>                     |
| [**put\_MaskNum**](idxtjpeg-put-masknum.md)               | Specifies the SMPTE wipe code of the wipe.<br/>                                     |
| [**put\_OffsetX**](idxtjpeg-put-offsetx.md)               | Specifies the horizontal offset of the wipe origin.<br/>                            |
| [**put\_OffsetY**](idxtjpeg-put-offsety.md)               | Specifies the vertical offset of the wipe origin.<br/>                              |
| [**put\_ReplicateX**](idxtjpeg-put-replicatex.md)         | Specifies the number of times the wipe pattern is replicated horizontally.<br/>     |
| [**put\_ReplicateY**](idxtjpeg-put-replicatey.md)         | Specifies the number of times the wipe pattern is replicated vertically.<br/>       |
| [**put\_ScaleX**](idxtjpeg-put-scalex.md)                 | Specifies the amount by which the wipe is stretched horizontally.<br/>              |
| [**put\_ScaleY**](idxtjpeg-put-scaley.md)                 | Specifies the amount by which the wipe is stretched vertically.<br/>                |



 

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



 

 




