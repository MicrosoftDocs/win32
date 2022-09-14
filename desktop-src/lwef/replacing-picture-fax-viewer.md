---
title: Replacing the Windows Picture and Fax Viewer Application Using the Preview Verb
description: As of Windows XP, users can view, rotate, print, and zoom images.
ms.assetid: cb08756b-6a5d-424d-ab6d-2e34d180ec4e
keywords:
- Windows Picture and Fax Viewer
- Preview verb
- best practices,Windows Picture and Fax Viewer
- best practices,Preview verb
- performance,Windows Picture and Fax Viewer
- performance,Preview verb
- register,Preview verb
- register,Slideshow verb
- Slideshow verb
ms.topic: article
ms.date: 05/31/2018
---

# Replacing the Windows Picture and Fax Viewer Application Using the Preview Verb

\[The Picture and Fax Viewer feature is supported only under Windows XP. \]

As of Windows XP, users can view, rotate, print, and zoom images. Some of these features are provided through the Windows Shell, and others through the Windows Picture and Fax Viewer application. While Windows Picture and Fax Viewer provides an excellent baseline of features and is a key part of the imaging experience, if you choose to, you can easily replace it with a different application. This document is designed to help you effectively replace the Windows Picture and Fax Viewer application without losing important features or degrading the user experience.

-   [Best Practices](#best-practices)
    -   [Performance](#performance)
    -   [Features](#features)
    -   [Format Support](#format-support)
-   [Registering for the Preview Verb](#registering-for-the-preview-verb)
-   [Registering for the Edit Verb](#registering-for-the-edit-verb)
-   [Registering for the Slideshow Verb](#registering-for-the-slideshow-verb)
-   [Related topics](#related-topics)

## Best Practices

In Windows XP and later, the Shell includes a verb that you can use to enable users to preview images. It is called *Preview*. This verb highlights the main user task for images, which is viewing. To make this experience work well, the Windows Picture and Fax Viewer application owns the preview association by default.

The Windows Picture and Fax Viewer, or any application that owns a file association, includes an item that launches the user's editing application. Because the Preview verb is only used to preview images rather than edit them, your application must be careful to follow the recommendations in this document when claiming that association.

You want to ensure that an application that edits images can still take over the Edit verb. For example, if a user has Microsoft Picture It! installed, when they double-click a .jpg file the computer should launch the Windows Picture and Fax Viewer application. But, when they click **Edit** in the toolbar, then the computer should launch Picture It! with that .jpg file.

There are three considerations you should take into account when you replace the Windows Picture and Fax Viewer. These are:

-   [Performance](#performance)
-   [Features](#features)
-   [Format Support](#format-support)

### Performance

The main consideration with performance is the speed at which images load. While no performance metric is provided here, you should attempt to replace Windows Picture and Fax Viewer with an application that matches or increases the performance.

The application itself should load quickly. One of the major issues users experience with applications that take over image associations is the wait time while the application loads. This often stems from having a powerful editing application load when they double-click an image file, even when the user simply wants to view the file. It is best for the user if you provide options that quickly take them to an application where they can edit the image only when that is their wish.

### Features

There is a minimal set of features your application should provide when you replace the Windows Picture and Fax Viewer application. They are as follows:



| Feature                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Show image at best fit             | This gives the user the option to see the entire image scaled to the size where i best fits into the viewable space of the application window. In this way, they can see the entire image, even if it is slightly degraded by zooming out. This should be the default setting whenever an image loads that is larger than the viewable space. Otherwise, the image should appear in its actual size. For example, a 64 x 64 pixel image should not be scaled to a 600 x 600 size simply because that is the application's window size. |
| Show image at actual size          | This gives the user the option to see the entire image at its actual resolution. This allows them to view it at its appropriate size and pan about the image. This should not be the default view unless the image is smaller than the viewable space in the application.                                                                                                                                                                                                                                                              |
| Zoom into image                    | This enables the user to zoom into a portion of the image to investigate finer details, or simply enlarge a small image. This is similar to showing the image actual size, but enables the user to control how closely they view the image.                                                                                                                                                                                                                                                                                            |
| Zoom out of image                  | This enables the user to zoom out and get a broader view. This is similar to showing the image at best fit, but enables the user to control how far back they view the image.                                                                                                                                                                                                                                                                                                                                                          |
| Next image                         | This enables the user to see the next image in the list. This list can be all the images in the current folder or all the images the user selects as part of a multiselect operation; that is, when he or she clicks and drags to highlight images or holds down the control button and clicks individual files.                                                                                                                                                                                                                       |
| Previous image                     | This enables the user to view the previous image in the list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Rotate clockwise 90 degrees        | This enables the user to rotate the image clockwise by quarters. Windows XP automatically saves the image when it rotates it to reduce the loss of image quality. The application can also rotate smaller increments, but 90 degrees is the standard as the most common rotation for digital pictures.                                                                                                                                                                                                                                 |
| Rotate counterclockwise 90 degrees | This enables the user to rotate the image counterclockwise by quarters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Print                              | This enables the user to print the image that currently appears.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Save As                            | This enables the user to save the image to a specified folder.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Delete image                       | This enables the user to delete the image.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Help                               | This provides the user with help documentation concerned with the use of the viewing application.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Properties                         | This enables the user to view or edit the properties of the image, typically the Exchangeable Image File (EXIF) information stored in each image.                                                                                                                                                                                                                                                                                                                                                                                      |
| Edit                               | This enables the user to launch their preferred editing program registered for the Edit verb on the image.                                                                                                                                                                                                                                                                                                                                                                                                                             |



 

### Format Support

Because it is difficult for an application to support all different images, it is recommended that the application use Windows GDI+ to support image formats. However, if you choose not to use GDI+, your application should take over only those file associations for which it has been tested and is known to work. Then, if the user needs to view a format that you do not handle, Windows Picture and Fax Viewer can still provide access.

For example, Windows Picture and Fax Viewer provides a number of tools for editing annotations in .tiff images. Unless this functionality is duplicated in your application, you should not register your application to handle .tiff images. The driving principle should be to ensure that the user loses no functionality whatsoever.

## Registering for the Preview Verb

Registering an application to handle the Preview verb is fairly simple. Locate the application's following value in the registry, where Application.Jpeg represents the name of the application's file association key (see [Default Programs](/windows/desktop/shell/default-programs) for more details):

```
HKEY_CLASSES_ROOT
   Application.Jpeg
      shell
         open
            command
               (Default) = app.exe %1
```

Change the name of the **open** subkey to "preview" as shown here.

```
HKEY_CLASSES_ROOT
   Application.Jpeg
      shell
         preview
            command
               (Default) = app.exe %1
```

This registers the application and makes it the default application for the Preview verb for a .jpg file. The following is also required.

**HKEY\_CLASSES\_ROOT**\\**.jpg**\(Default) = Application.Jpeg

## Registering for the Edit Verb

This registers an application for the Edit Verb and makes it the new default application for editing an image. The registered application should take over the editing capability of the existing default application at the install time and install it back as the handler at the time of uninstall. This can be achieved by registering the new application lower in the association list than the default application. The default application is registered here:

```
HKEY_CLASSES_ROOT
   SystemFileAssociations
      image
         shell
            edit
               command
                  (Default) = app.exe %1
```

New application should register here:

```
HKEY_CLASSES_ROOT
   Application.Jpeg
      shell
         edit
            command
               (Default) = app.exe %1
```

## Registering for the Slideshow Verb

As of Windows Vista, an application can also register the **slideshow** verb. Applications that implement a slide show can register to be invoked when the Slideshow verb is chosen. This registration is accomplished in exactly the same fashion as explained for the preview verb above. It is strongly recommended that applications implement the DropTarget form of the verb. In that way, they can be passed a complete set of items. The DropTarget implementation is registered as shown here:

```
HKEY_CLASSES_ROOT
   Application.Jpeg
      shell
         slideshow
            DropTarget
               CLSID = {CLSID of the implementation}
```

## Related topics

<dl> <dt>

[Introduction to File Associations](/windows/desktop/shell/fa-intro)
</dt> <dt>

[About GDI+](../gdiplus/-gdiplus-about-gdi--about.md)
</dt> </dl>

 

 