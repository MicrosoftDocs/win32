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
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Create a Synchronous Reader and Open a File

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Before you can do any work with the synchronous reader, you will need to create a synchronous reader object and load a file for reading. To initialize the synchronous reader and open a file, perform the following steps.

1.  Create a synchronous reader object by calling the [**WMCreateSyncReader**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreatesyncreader) function. You must specify the desired level of rights management for the new reader object. The available modes are listed in the **WMT\_RIGHTS** enumeration type.
2.  Specify a file to read by calling [**IWMSyncReader::Open**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-open).

The synchronous reader also supports the use of the **IStream** COM interface for opening files. You can implement the **IStream** interface any way you choose. After the desired file is opened in **IStream**, you can follow the steps listed above, except that you must call [**IWMSyncReader::OpenStream**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmsyncreader-openstream) instead of **IWMSyncReader::Open** in step 2.

## Related topics

<dl> <dt>

[**IWMSyncReader Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmsyncreader)
</dt> <dt>

[**Reading Files with the Synchronous Reader**](reading-files-with-the-synchronous-reader.md)
</dt> </dl>

 

 




