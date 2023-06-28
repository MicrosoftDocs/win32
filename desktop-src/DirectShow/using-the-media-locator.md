---
description: Using the Media Locator
ms.assetid: 07840a37-7065-41e8-aee5-855c9f89fb77
title: Using the Media Locator
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using the Media Locator

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[This API is not supported and may be altered or unavailable in the future.\]

The media locator is a helper object that verifies file names and searches for missing files on local or network directories. The media detector keeps a cache of directory paths where it has successfully found files in past searches. To locate a file, it searches the directories in its cache. Failing that, the media detector can display an Open File dialog for the user to locate a file manually. Assuming the user locates the file, the media locator adds the new directory to its cache. The media locator exposes the [**IMediaLocator**](imedialocator.md) interface.

Typically, your application does not directly create an instance of the media locator. Instead, the timeline and the render engine provide the following methods for validating file names using the media detector.

-   To validate file names in the timeline, call [**IAMTimeline::ValidateSourceNames**](iamtimeline-validatesourcenames.md). Optionally, this method also updates the source objects with the correct file names.
-   To validate file names when the project is rendered, call [**IRenderEngine::SetSourceNameValidation**](irenderengine-setsourcenamevalidation.md).

Both methods take flags that control the behavior of the media locator. For example, you can restrict the search to local directories.

## Related topics

<dl> <dt>

[Working with Sources](working-with-sources.md)
</dt> </dl>

 

 



