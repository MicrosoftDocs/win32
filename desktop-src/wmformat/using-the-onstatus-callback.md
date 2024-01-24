---
title: Using the OnStatus Callback
description: Using the OnStatus Callback
ms.assetid: 598e2d13-709b-42a3-ae06-b8c7d208ca9e
keywords:
- Windows Media Format SDK,OnStatus callback method
- Windows Media Format SDK,IWMStatusCallback interface
- OnStatus callback method,about
- IWMStatusCallback
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using the OnStatus Callback

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The [**IWMStatusCallback::OnStatus**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus) callback method is called by several objects in the Windows Media Format SDK. **OnStatus** receives messages that represent changes in the status of SDK operations.

To use the **OnStatus** callback method, you must implement a class in your application that inherits from the [**IWMStatusCallback**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstatuscallback) interface. Include code for your version of **OnStatus** in the class. Several examples of **OnStatus** implementations can be found in the samples included with this SDK. For more information about the samples, see [Sample Applications](sample-applications.md).

You must associate your implementation of the status callback with various objects of the Windows Media Format SDK. Each object has a different way of making this association. For a list of the methods that associate specific objects, see the **IWMStatusCallback** reference page.

The status messages that can be received by **OnStatus** are defined in the [**WMT\_STATUS**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_status) enumeration type.

You can choose which messages to trap and which to ignore. However, responding to some status messages is required for certain features. For example, when using the asynchronous reader, the [**IWMReader::Open**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-open) method opens a file asynchronously. The only way to tell when the file has been opened is to trap the MWT\_OPENED message. Typically, the messages you respond to are notifications of the completion of asynchronous tasks.

## Related topics

<dl> <dt>

[**Using the Callback Methods**](using-the-callback-methods.md)
</dt> </dl>

 

 




