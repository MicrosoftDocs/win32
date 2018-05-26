---
title: To Create a Synchronous Reader and Open a File
description: To Create a Synchronous Reader and Open a File
ms.assetid: 6349d05e-20db-4ce8-83fd-cad4cec666f2
keywords:
- Advanced Systems Format (ASF),creating readers
- ASF (Advanced Systems Format),creating readers
- Advanced Systems Format (ASF),opening files
- ASF (Advanced Systems Format),opening files
- synchronous readers,creating
- synchronous readers,opening files
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To Create a Synchronous Reader and Open a File

Before you can do any work with the synchronous reader, you will need to create a synchronous reader object and load a file for reading. To initialize the synchronous reader and open a file, perform the following steps.

1.  Create a synchronous reader object by calling the [**WMCreateSyncReader**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreatesyncreader?branch=master) function. You must specify the desired level of rights management for the new reader object. The available modes are listed in the **WMT\_RIGHTS** enumeration type.
2.  Specify a file to read by calling [**IWMSyncReader::Open**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-open?branch=master).

The synchronous reader also supports the use of the **IStream** COM interface for opening files. You can implement the **IStream** interface any way you choose. After the desired file is opened in **IStream**, you can follow the steps listed above, except that you must call [**IWMSyncReader::OpenStream**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-openstream?branch=master) instead of **IWMSyncReader::Open** in step 2.

## Related topics

<dl> <dt>

[**IWMSyncReader Interface**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmsyncreader?branch=master)
</dt> <dt>

[**Reading Files with the Synchronous Reader**](reading-files-with-the-synchronous-reader.md)
</dt> </dl>

 

 




