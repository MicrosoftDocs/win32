---
description: Specifies a window for the Media Engine to apply Output Protection Manager (OPM) protections.
ms.assetid: E5271D72-FE16-4D28-9BBA-1440C7CE0921
title: MF_MEDIA_ENGINE_OPM_HWND attribute (Mfmediaengine.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MEDIA\_ENGINE\_OPM\_HWND attribute

Specifies a window for the Media Engine to apply [Output Protection Manager](output-protection-manager.md) (OPM) protections.

## Data type

**HWND** stored as **UINT64**

## Remarks

This attribute is used with the [**IMFMediaEngineClassFactory::CreateInstance**](/windows/desktop/api/mfmediaengine/nf-mfmediaengine-imfmediaengineclassfactory-createinstance) method to initialize the Media Engine.

To enable OPM protections for video playback, the application must do one of the following:

-   Set the [MF\_MEDIA\_ENGINE\_PLAYBACK\_HWND](mf-media-engine-playback-hwnd.md) attribute when creating the Media Engine.
-   Set the MF\_MEDIA\_ENGINE\_OPM\_HWND attribute when creating the Media Engine.
-   Call [**IMFMediaEngineProtectedContent::SetOPMWindow**](/windows/desktop/api/mfmediaengine/nf-mfmediaengine-imfmediaengineprotectedcontent-setopmwindow) at any point after creating the Media Engine, but before protected content is displayed.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                                |
| Header<br/>                   | <dl> <dt>Mfmediaengine.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Engine Attributes](media-engine-attributes.md)
</dt> </dl>

 

 




