---
description: Using the Media Locator
ms.assetid: 07840a37-7065-41e8-aee5-855c9f89fb77
title: Using the Media Locator
ms.topic: article
ms.date: 05/31/2018
---

# Using the Media Locator

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

 

 



