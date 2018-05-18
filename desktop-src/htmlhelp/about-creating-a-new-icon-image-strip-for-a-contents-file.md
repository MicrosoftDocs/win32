---
title: About Creating a New Icon Image Strip for a Contents File
description: About Creating a New Icon Image Strip for a Contents File
ms.assetid: 'A3D7131D-2490-4ffc-B93F-A2DEBC8ED608'
---

# About Creating a New Icon Image Strip for a Contents File

The first 8 images on your [new icon strip](to-create-a-new-icon-strip-for-a-contents-file.md) should communicate the concepts in the list below. The order of the first 8 images is important because the images change to reflect user actions.

For example, if you assign the Closed Item 1 icon to a topic in your table of contents, and a user clicks it, the image will automatically change to Open Item 1.

1.  Closed Item 1
2.  Open Item 1
3.  New Closed Item 1
4.  New Open Item 1
5.  Closed Item 2
6.  Open Item 2
7.  New Closed Item 2
8.  New Open Item 2
9.  Item 3
10. Item 4
11. Item 5
12. Item 6
13. Item 7
14. Item 8

### Notes

-   If the bitmap for the image strip is compiled into the .chm file, this feature will not work. This is due to a limitation in the HTML Help API. As a workaround, you can place the bitmap in the same directory as the .chm. On Windows NT version 4 and Windows 2000, the bitmap can be placed in the %SYSTEMROOT% directory (this will not work on Windows 95 or Windows 98).
-   Items 3 through 8 can convey any concept you want, but they must be present in your custom icon strip for the new images to display correctly. You must include at lest 14 images in your custom icon strip.
-   You are not, however, limited to 14 images. You can include up to 42 images in your custom icon strip.
-   Custom icons are not supported in a [binary table of contents](about-binary-contents-files.md).

## Related topics

<dl> <dt>

[About Creating Table of Contents Files](create-a-table-of-contents-file.md)
</dt> </dl>

 

 




