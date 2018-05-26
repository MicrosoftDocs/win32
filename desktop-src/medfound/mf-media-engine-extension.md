---
Description: Contains a pointer to the IMFMediaEngineExtension interface.
ms.assetid: D2F3F41D-086A-4DEB-99D0-07574BC8F0D7
title: MF\_MEDIA\_ENGINE\_EXTENSION attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MEDIA\_ENGINE\_EXTENSION attribute

Contains a pointer to the [**IMFMediaEngineExtension**](/windows/win32/mfmediaengine/nn-mfmediaengine-imfmediaengineextension?branch=master) interface.

## Data type

**IMFMediaEngineExtension\*** stored as **IUnknown\***

## Get/set

To get this attribute, call [**IMFAttributes::GetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getunknown?branch=master).

To set this attribute, call [**IMFAttributes::SetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setunknown?branch=master).

## Remarks

This attribute is used with the [**IMFMediaEngineClassFactory::CreateInstance**](/windows/win32/mfmediaengine/nf-mfmediaengine-imfmediaengineclassfactory-createinstance?branch=master) method to initialize the Media Engine.

This attribute is optional. Use it to provide an object that implements the [**IMFMediaEngineExtension**](/windows/win32/mfmediaengine/nn-mfmediaengine-imfmediaengineextension?branch=master) interface. This interface enables the application to load custom media resources.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                                |
| Header<br/>                   | <dl> <dt>Mfmediaengine.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




