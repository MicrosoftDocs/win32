---
description: When you provide a thumbnail, the following guidelines should be followed.
title: Thumbnail Handler Guidelines
ms.topic: article
ms.date: 05/31/2018
ms.assetid: a1d29992-1347-4574-81b9-b90e2b0938f1
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Thumbnail Handler Guidelines

When you provide a thumbnail, the following guidelines should be followed.

-   Provide thumbnails that display well at a resolution of 256x256 pixels in 32-bit color. A thumbnail of this size is be used by the Windows Vista reading pane in the absence of a registered preview handler. However, a preview handler is the preferred option and should be provided whenever possible.
-   When you create multiple images of different sizes, do not create the smaller images from the larger by cropping the page, frame, or image. Scale down the entire image.
-   Do not show multiple pages, frames, or images at once; just use one. If a document consists of several pages, such as a text document or a spreadsheet that consists of several worksheets, the cover page is often the best choice, but regardless of which you use, only use one. Do not aggregate different pages, which gives a cluttered look.
-   Windows Vista is responsible for scaling down or down sampling images. If your handler is asked for a larger image than you have available, provide the closest size you have. Do not attempt to dynamically resize your own image.
-   Always return a thumbnail image from your handler instead of performing special logic to return traditional icons. Below a certain size, Windows Vista automatically displays a traditional icon in place of the thumbnail. See the *Thumbnail Cache and Sizing* section of [Thumbnail Handlers](thumbnail-providers.md) for more details.
-   Always return a thumbnail with the aspect ratio of the page, frame, or image. Do not use alpha to complete a square. Windows Vista is responsible for correctly positioning a non-square image.
-   Do not add adornments to your thumbnails. Windows Vista automatically applies drop shadows and other adornments where appropriate. It also applies special adornments for specific file types such as pictures or videos.
-   Do not overlay file type or application information on your thumbnail. Windows Vista displays a type overlay for you in the lower right corner of the image. This overlay is based on perceived type but can be set for individual file types.
-   For better performance, when your thumbnail is based on file content—a page of a document, for example—store the preview image when the file is saved (and therefore probably changed) instead of calculating it in real time. This should be done if the calculation is memory-intensive (more than one or two seconds). If this is not done, views showing a large number of files whose thumbnails are handled by different handlers is going to take some time to display—a bad user experience. Windows Vista caches thumbnails and refers to the last modified time to determine whether a thumbnail should be updated.
-   Be aware that Explorer may choose not to display a thumbnail even if a provider is available. For example, a file that has been archived to tape will not be recalled to obtain its thumbnail.

## Related topics

<dl> <dt>

[Thumbnail Handlers](thumbnail-providers.md)
</dt> <dt>

[Building Thumbnail Handlers](building-thumbnail-providers.md)
</dt> </dl>

 

 



