---
Description: The fax service associates a fax file list with each fax document it receives and processes.
ms.assetid: 6aa919ad-3c99-4e27-a462-5ad670cfb4e9
title: Fax File Lists
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Fax File Lists

The fax service associates a *fax file list* with each fax document it receives and processes. A fax routing method can add files to the file list, delete files from the list, and enumerate the files in the list using the fax routing functions.

Before the first fax routing method runs, the only file in the fax file list is the received fax file. This is a Tagged Image File Format Class F (TIFF Class F) file. Fax routing methods can use the received Tagged Image File Format (TIFF) file as a read-only resource to create and add one or more files to the fax file list. The fax service can then route received faxes through multiple fax routing extensions and through multiple routing methods in each extension. The result of this added functionality is, in effect, a custom file filter.

For example, a fax routing method for one fax routing extension could include the following steps:

1.  Convert the received TIFF file to text using optical character recognition (OCR) technology.
2.  Create a Microsoft Word document from the text.
3.  Add the Word document file to the fax file list associated with the received fax.

After this example method executes, any fax routing method could access the Word document in the fax file list. If a method routes received faxes using an email application, it could include both the Word document and the TIFF file in a user's electronic mail message. For more information, see [Managing a Fax File List](-mfax-managing-a-fax-file-list.md) and [Routing a Fax](-mfax-routing-a-fax.md).

A fax routing method cannot modify the initial TIFF file or remove it from the fax file list. For more information about TIFF files, see [Fax Image Format](-mfax-fax-image-format.md).

 

 



