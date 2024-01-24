---
description: Provides a template for creating class factories.
ms.assetid: 3dbe6402-15f8-4490-9fe2-bebaa4e79170
title: CFactoryTemplate class (Combase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CFactoryTemplate
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CFactoryTemplate class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Provides a template for creating class factories.

In DirectShow, class factories are specialized using the **CFactoryTemplate** class, also called the *factory template*. Each class factory holds a pointer to a factory template. The factory template contains information about a COM object, including the object's class identifier (CLSID) and a pointer to a function that creates the object.

In your DLL, declare a global array of factory templates named *g\_Templates*. Include one factory template for each object in the DLL. When the [**DllGetClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-dllgetclassobject) function makes a new class factory, it searches the array for a template with a matching CLSID. Assuming it finds one, it creates a class factory that holds a pointer to the matching template. When the client calls **IClassFactory::CreateInstance**, the class factory calls the instantiation function defined in the template.

For more information, see [How to Create a DirectShow Filter DLL](how-to-create-a-dll.md).



| Public Member Variables                                                   | Description                                                                |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------|
| [**m\_Name**](cfactorytemplate-m-name.md)                                | Name of the filter.                                                        |
| [**m\_ClsID**](cfactorytemplate-m-clsid.md)                              | Pointer to the CLSID of the object.                                        |
| [**m\_lpfnNew**](cfactorytemplate-m-lpfnnew.md)                          | Pointer to a function that creates an instance of the object.              |
| [**m\_lpfnInit**](cfactorytemplate-m-lpfninit.md)                        | Pointer to a function that gets called from the DLL entry point.           |
| [**m\_pAMovieSetup\_Filter**](cfactorytemplate-m-pamoviesetup-filter.md) | Pointer to an [**AMOVIESETUP\_FILTER**](amoviesetup-filter.md) structure. |
| Public Methods                                                            | Description                                                                |
| [**IsClassID**](cfactorytemplate-isclassid.md)                           | Determines whether a CLSID matches this class template.                    |
| [**CreateInstance**](cfactorytemplate-createinstance.md)                 | Calls the object-creation function for the class.                          |



 

## Requirements



| Requirement | Value |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib; </dt> <dt>Strmbasd.lib</dt> </dl> |



## See also

<dl> <dt>

[Base Class Reference](base-class-reference.md)
</dt> </dl>

 

