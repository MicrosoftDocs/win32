---
Description: Contains a pointer to the callback interface for the Media Engine.
ms.assetid: 5FAEF29A-B978-410A-8F5B-EB6F7E35EE6D
title: MF\_MEDIA\_ENGINE\_CALLBACK attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_MEDIA\_ENGINE\_CALLBACK attribute

Contains a pointer to the callback interface for the Media Engine.

## Data type

**IMFMediaEngineNotify\*** stored as **IUnknown\***

## Get/set

To get this attribute, call [**IMFAttributes::GetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getunknown?branch=master).

To set this attribute, call [**IMFAttributes::SetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setunknown?branch=master).

## Remarks

The value of this attribute is a pointer to the [**IMFMediaEngineNotify**](/windows/win32/mfmediaengine/nn-mfmediaengine-imfmediaenginenotify?branch=master) interface, implemented by the application.

This attribute is used with the [**IMFMediaEngineClassFactory::CreateInstance**](/windows/win32/mfmediaengine/nf-mfmediaengine-imfmediaengineclassfactory-createinstance?branch=master) method to initialize the Media Engine. The attribute is required.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                                |
| Header<br/>                   | <dl> <dt>Mfmediaengine.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFMediaEngineClassFactory::CreateInstance**](/windows/win32/mfmediaengine/nf-mfmediaengine-imfmediaengineclassfactory-createinstance?branch=master)
</dt> <dt>

[**IMFMediaEngineNotify**](/windows/win32/mfmediaengine/nn-mfmediaengine-imfmediaenginenotify?branch=master)
</dt> </dl>

 

 




