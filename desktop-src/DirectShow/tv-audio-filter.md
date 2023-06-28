---
description: TV Audio Filter
ms.assetid: 882e03d4-5574-4b0f-b965-63ff9dbb7852
title: TV Audio Filter
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# TV Audio Filter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The TV Audio filter provides control of television audio decoding, stereo or monoaural selection, and secondary audio program (SAP) selection.



| Label | Value |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Filter Interfaces                        | [**IAMTVAudio**](/windows/desktop/api/Strmif/nn-strmif-iamtvaudio), **IPersistPropertyBag**, **ISpecifyPropertyPages**, [**IKsPropertySet**](ikspropertyset.md) |
| Input Pin Media Types                    | MEDIATYPE\_AnalogAudio                                                                                                         |
| Input Pin Interfaces                     | **IKsPropertySet**                                                                                                             |
| Output Pin Media Types                   | MEDIATYPE\_AnalogAudio                                                                                                         |
| Output Pin Interfaces                    | **IKsPropertySet**                                                                                                             |
| Filter CLSID                             | CLSID\_TVAudioFilter                                                                                                           |
| Property Page CLSID                      | AM\_KSCATEGORY\_TVAUDIO                                                                                                        |
| [Merit](merit.md)                       | MERIT\_DO\_NOT\_USE                                                                                                            |
| [Filter Category](filter-categories.md) | CLSID\_AudioInputDeviceCategory                                                                                                |



 

## Related topics

<dl> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



