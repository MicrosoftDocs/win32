---
title: Using the OnStatus Callback
description: Using the OnStatus Callback
ms.assetid: 598e2d13-709b-42a3-ae06-b8c7d208ca9e
keywords:
- Windows Media Format SDK,OnStatus callback method
- Windows Media Format SDK,IWMStatusCallback interface
- OnStatus callback method,about
- IWMStatusCallback
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using the OnStatus Callback

The [**IWMStatusCallback::OnStatus**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus?branch=master) callback method is called by several objects in the Windows Media Format SDK. **OnStatus** receives messages that represent changes in the status of SDK operations.

To use the **OnStatus** callback method, you must implement a class in your application that inherits from the [**IWMStatusCallback**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmstatuscallback?branch=master) interface. Include code for your version of **OnStatus** in the class. Several examples of **OnStatus** implementations can be found in the samples included with this SDK. For more information about the samples, see [Sample Applications](sample-applications.md).

You must associate your implementation of the status callback with various objects of the Windows Media Format SDK. Each object has a different way of making this association. For a list of the methods that associate specific objects, see the **IWMStatusCallback** reference page.

The status messages that can be received by **OnStatus** are defined in the [**WMT\_STATUS**](/windows/win32/Wmsdkidl/ne-wmsdkidl-wmt_status?branch=master) enumeration type.

You can choose which messages to trap and which to ignore. However, responding to some status messages is required for certain features. For example, when using the asynchronous reader, the [**IWMReader::Open**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmreader-open?branch=master) method opens a file asynchronously. The only way to tell when the file has been opened is to trap the MWT\_OPENED message. Typically, the messages you respond to are notifications of the completion of asynchronous tasks.

## Related topics

<dl> <dt>

[**Using the Callback Methods**](using-the-callback-methods.md)
</dt> </dl>

 

 




