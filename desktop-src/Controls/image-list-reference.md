---
title: Image List Reference
description: This section contains information about the programming elements used with image lists.
ms.assetid: '8a2bdc59-747c-47bb-b125-9b0b97af205e'
---

# Image List Reference

This section contains information about the programming elements used with image lists.

### Overviews



| Topic                          | Contents                                                                                                            |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [Image Lists](image-lists.md) | An image list is a collection of images of the same size, each of which can be referred to by its index.<br/> |



 

### Functions



| Topic                                                                 | Contents                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**HIMAGELIST\_QueryInterface**](himagelist-queryinterface.md)       | Retrieves a pointer to an [**IImageList**](iimagelist.md) or [**IImageList2**](iimagelist2.md) object that corresponds to the image list's HIMAGELIST handle.<br/>                                                                                                           |
| [**ImageList\_Add**](imagelist-add.md)                               | Adds an image or images to an image list. <br/>                                                                                                                                                                                                                                |
| [**ImageList\_AddMasked**](imagelist-addmasked.md)                   | Adds an image or images to an image list, generating a mask from the specified bitmap.<br/>                                                                                                                                                                                    |
| [**ImageList\_BeginDrag**](imagelist-begindrag.md)                   | Begins dragging an image. <br/>                                                                                                                                                                                                                                                |
| [**ImageList\_CoCreateInstance**](imagelist-cocreateinstance.md)     | Creates a single instance of an imagelist and returns an interface pointer to it.<br/>                                                                                                                                                                                         |
| [**ImageList\_Copy**](imagelist-copy.md)                             | Copies images within a given image list. <br/>                                                                                                                                                                                                                                 |
| [**ImageList\_Create**](imagelist-create.md)                         | Creates a new image list. <br/>                                                                                                                                                                                                                                                |
| [**ImageList\_Destroy**](imagelist-destroy.md)                       | Destroys an image list.<br/>                                                                                                                                                                                                                                                   |
| [**ImageList\_DragEnter**](imagelist-dragenter.md)                   | Displays the drag image at the specified position within the window. <br/>                                                                                                                                                                                                     |
| [**ImageList\_DragLeave**](imagelist-dragleave.md)                   | Unlocks the specified window and hides the drag image, allowing the window to be updated. <br/>                                                                                                                                                                                |
| [**ImageList\_DragMove**](imagelist-dragmove.md)                     | Moves the image that is being dragged during a drag-and-drop operation. This function is typically called in response to a [**WM\_MOUSEMOVE**](https://msdn.microsoft.com/library/windows/desktop/ms645616) message. <br/>                                                                                           |
| [**ImageList\_DragShowNolock**](imagelist-dragshownolock.md)         | Shows or hides the image being dragged. <br/>                                                                                                                                                                                                                                  |
| [**ImageList\_Draw**](imagelist-draw.md)                             | Draws an image list item in the specified device context. <br/>                                                                                                                                                                                                                |
| [**ImageList\_DrawEx**](imagelist-drawex.md)                         | Draws an image list item in the specified device context. The function uses the specified drawing style and blends the image with the specified color. <br/>                                                                                                                   |
| [**ImageList\_DrawIndirect**](imagelist-drawindirect.md)             | Draws an image list image based on an [**IMAGELISTDRAWPARAMS**](imagelistdrawparams.md) structure. <br/>                                                                                                                                                                      |
| [**ImageList\_Duplicate**](imagelist-duplicate.md)                   | Creates a duplicate of an existing image list. <br/>                                                                                                                                                                                                                           |
| [**ImageList\_EndDrag**](imagelist-enddrag.md)                       | Ends a drag operation. <br/>                                                                                                                                                                                                                                                   |
| [**ImageList\_GetBkColor**](imagelist-getbkcolor.md)                 | Retrieves the current background color for an image list. <br/>                                                                                                                                                                                                                |
| [**ImageList\_GetDragImage**](imagelist-getdragimage.md)             | Retrieves the temporary image list that is used for the drag image. The function also retrieves the current drag position and the offset of the drag image relative to the drag position. <br/>                                                                                |
| [**ImageList\_GetIcon**](imagelist-geticon.md)                       | Creates an icon from an image and mask in an image list. <br/>                                                                                                                                                                                                                 |
| [**ImageList\_GetIconSize**](imagelist-geticonsize.md)               | Retrieves the dimensions of images in an image list. All images in an image list have the same dimensions. <br/>                                                                                                                                                               |
| [**ImageList\_GetImageCount**](imagelist-getimagecount.md)           | Retrieves the number of images in an image list. <br/>                                                                                                                                                                                                                         |
| [**ImageList\_GetImageInfo**](imagelist-getimageinfo.md)             | Retrieves information about an image. <br/>                                                                                                                                                                                                                                    |
| [**ImageList\_LoadImage**](imagelist-loadimage.md)                   | Creates an image list from the specified bitmap.<br/>                                                                                                                                                                                                                          |
| [**ImageList\_Merge**](imagelist-merge.md)                           | Creates a new image by combining two existing images. The function also creates a new image list in which to store the image. <br/>                                                                                                                                            |
| [**ImageList\_Read**](imagelist-read.md)                             | Reads an image list from a stream. <br/>                                                                                                                                                                                                                                       |
| [**ImageList\_ReadEx**](imagelist-readex.md)                         | Reads an image list from a stream, and returns an interface to the image list. <br/>                                                                                                                                                                                           |
| [**ImageList\_Remove**](imagelist-remove.md)                         | Removes an image from an image list. <br/>                                                                                                                                                                                                                                     |
| [**ImageList\_Replace**](imagelist-replace.md)                       | Replaces an image in an image list with a new image. <br/>                                                                                                                                                                                                                     |
| [**ImageList\_ReplaceIcon**](imagelist-replaceicon.md)               | Replaces an image with an icon or cursor.<br/>                                                                                                                                                                                                                                 |
| [**ImageList\_SetBkColor**](imagelist-setbkcolor.md)                 | Sets the background color for an image list. This function only works if you add an icon or use [**ImageList\_AddMasked**](imagelist-addmasked.md) with a black and white bitmap. Without a mask, the entire image is drawn; hence the background color is not visible. <br/> |
| [**ImageList\_SetColorTable**](imagelist-setcolortable.md)           | Sets the color table for an image list.<br/>                                                                                                                                                                                                                                   |
| [**ImageList\_SetDragCursorImage**](imagelist-setdragcursorimage.md) | Creates a new drag image by combining the specified image (typically a mouse cursor image) with the current drag image. <br/>                                                                                                                                                  |
| [**ImageList\_SetIconSize**](imagelist-seticonsize.md)               | Sets the dimensions of images in an image list and removes all images from the list. <br/>                                                                                                                                                                                     |
| [**ImageList\_SetImageCount**](imagelist-setimagecount.md)           | Resizes an existing image list. <br/>                                                                                                                                                                                                                                          |
| [**ImageList\_SetOverlayImage**](imagelist-setoverlayimage.md)       | Adds a specified image to the list of images to be used as overlay masks. An image list can have up to four overlay masks in version 4.70 and earlier and up to 15 in version 4.71. The function assigns an overlay mask index to the specified image. <br/>                   |
| [**ImageList\_Write**](imagelist-write.md)                           | Writes an image list to a stream. <br/>                                                                                                                                                                                                                                        |
| [**ImageList\_WriteEx**](imagelist-writeex.md)                       | Writes an image list to a stream. <br/>                                                                                                                                                                                                                                        |



 

### Macros



| Topic                                                   | Contents                                                                                                                                                                         |
|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ImageList\_AddIcon**](imagelist-addicon.md)         | Adds an icon or cursor to an image list. [**ImageList\_AddIcon**](imagelist-addicon.md) calls the [**ImageList\_ReplaceIcon**](imagelist-replaceicon.md) function. <br/> |
| [**ImageList\_ExtractIcon**](imagelist-extracticon.md) | Calls the [**ImageList\_GetIcon**](imagelist-geticon.md) function to create an icon or cursor based on an image and mask in an image list. <br/>                          |
| [**ImageList\_LoadBitmap**](imagelist-loadbitmap.md)   | Calls the [**ImageList\_LoadImage**](imagelist-loadimage.md) function to create an image list from the specified bitmap resource. <br/>                                   |
| [**ImageList\_RemoveAll**](imagelist-removeall.md)     | Calls the [**ImageList\_Remove**](imagelist-remove.md) function to remove all of the images from an image list. <br/>                                                     |
| [**INDEXTOOVERLAYMASK**](indextooverlaymask.md)        | Prepares the index of an overlay mask so that the [**ImageList\_Draw**](imagelist-draw.md) function can use it. <br/>                                                     |



 

### Interfaces



| Topic                            | Contents                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IImageList**](iimagelist.md) | Exposes methods that manipulate and interact with image lists. <br/> To use [**IImageList**](iimagelist.md), specify Comctl32.dll version 6 in the manifest. If you do not do this, Comctl32.dll version 5 will be used by default, with which **IImageList** could display unpredictable behavior. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).<br/> |



 

### Methods



| Topic                                                       | Contents                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](iimagelist-add.md)                               | Adds an image or images to an image list.<br/>                                                                                                                                                                                                                                                                |
| [**AddMasked**](iimagelist-addmasked.md)                   | Adds an image or images to an image list, generating a mask from the specified bitmap. <br/>                                                                                                                                                                                                                  |
| [**BeginDrag**](iimagelist-begindrag.md)                   | Begins dragging an image. <br/>                                                                                                                                                                                                                                                                               |
| [**Clone**](iimagelist-clone.md)                           | Clones an existing image list. <br/>                                                                                                                                                                                                                                                                          |
| [**Copy**](iimagelist-copy.md)                             | Copies images from a given image list. <br/>                                                                                                                                                                                                                                                                  |
| [**DragEnter**](iimagelist-dragenter.md)                   | Locks updates to the specified window during a drag operation and displays the drag image at the specified position within the window. <br/>                                                                                                                                                                  |
| [**DragLeave**](iimagelist-dragleave.md)                   | Unlocks the specified window and hides the drag image, which enables the window to update. <br/>                                                                                                                                                                                                              |
| [**DragMove**](iimagelist-dragmove.md)                     | Moves the image that is being dragged during a drag-and-drop operation. This function is typically called in response to a [**WM\_MOUSEMOVE**](https://msdn.microsoft.com/library/windows/desktop/ms645616) message. <br/>                                                                                                                          |
| [**DragShowNolock**](iimagelist-dragshownolock.md)         | Shows or hides the image being dragged. <br/>                                                                                                                                                                                                                                                                 |
| [**Draw**](iimagelist-draw.md)                             | Draws an image list item in the specified device context. <br/>                                                                                                                                                                                                                                               |
| [**EndDrag**](iimagelist-enddrag.md)                       | Ends a drag operation. <br/>                                                                                                                                                                                                                                                                                  |
| [**GetBkColor**](iimagelist-getbkcolor.md)                 | Gets the current background color for an image list. <br/>                                                                                                                                                                                                                                                    |
| [**GetDragImage**](iimagelist-getdragimage.md)             | Gets the temporary image list that is used for the drag image. The function also retrieves the current drag position and the offset of the drag image relative to the drag position. <br/>                                                                                                                    |
| [**GetIcon**](iimagelist-geticon.md)                       | Creates an icon from an image and a mask in an image list. <br/>                                                                                                                                                                                                                                              |
| [**GetIconSize**](iimagelist-geticonsize.md)               | Gets the dimensions of images in an image list. All images in an image list have the same dimensions. <br/>                                                                                                                                                                                                   |
| [**GetImageCount**](iimagelist-getimagecount.md)           | Gets the number of images in an image list. <br/>                                                                                                                                                                                                                                                             |
| [**GetImageInfo**](iimagelist-getimageinfo.md)             | Gets information about an image. <br/>                                                                                                                                                                                                                                                                        |
| [**GetImageRect**](iimagelist-getimagerect.md)             | Gets an image's bounding rectangle. <br/>                                                                                                                                                                                                                                                                     |
| [**GetItemFlags**](iimagelist-getitemflags.md)             | Gets the flags of an image.<br/>                                                                                                                                                                                                                                                                              |
| [**GetOverlayImage**](iimagelist-getoverlayimage.md)       | Retrieves a specified image from the list of images used as overlay masks. <br/>                                                                                                                                                                                                                              |
| [**Merge**](iimagelist-merge.md)                           | Creates a new image by combining two existing images. This method also creates a new image list in which to store the image. <br/>                                                                                                                                                                            |
| [**Remove**](iimagelist-remove.md)                         | Removes an image from an image list. <br/>                                                                                                                                                                                                                                                                    |
| [**Replace**](iimagelist-replace.md)                       | Replaces an image in an image list with a new image.<br/>                                                                                                                                                                                                                                                     |
| [**ReplaceIcon**](iimagelist-replaceicon.md)               | Replaces an image with an icon or cursor. <br/>                                                                                                                                                                                                                                                               |
| [**SetBkColor**](iimagelist-setbkcolor.md)                 | Sets the background color for an image list. This method only functions if you add an icon to the image list or use the [**IImageList::AddMasked**](iimagelist-addmasked.md) method to add a black and white bitmap. Without a mask, the entire image draws, and the background color is not visible. <br/>  |
| [**SetDragCursorImage**](iimagelist-setdragcursorimage.md) | Creates a new drag image by combining the specified image, which is typically a mouse cursor image, with the current drag image. <br/>                                                                                                                                                                        |
| [**SetIconSize**](iimagelist-seticonsize.md)               | Sets the dimensions of images in an image list and removes all images from the list. <br/>                                                                                                                                                                                                                    |
| [**SetImageCount**](iimagelist-setimagecount.md)           | Resizes an existing image list. <br/>                                                                                                                                                                                                                                                                         |
| [**SetOverlayImage**](iimagelist-setoverlayimage.md)       | Adds a specified image to the list of images used as overlay masks. An image list can have up to four overlay masks in Common Controls [version 4.70](common-control-versions.md) and earlier, and up to 15 in version 4.71 or later. The method assigns an overlay mask index to the specified image. <br/> |



 

### Structures



| Topic                                              | Contents                                                                                                                                                                |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IMAGEINFO**](imageinfo.md)                     | Contains information about an image in an image list. This structure is used with the [**IImageList::GetImageInfo**](iimagelist-getimageinfo.md) function. <br/> |
| [**IMAGELISTDRAWPARAMS**](imagelistdrawparams.md) | Contains information about an image list draw operation and is used with the [**IImageList::Draw**](iimagelist-draw.md) function. <br/>                          |



 

 

 





