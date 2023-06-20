---
title: Using the Callback Methods
description: Using the Callback Methods
ms.assetid: 098cb90b-8c21-4692-a4f9-bacce042520a
keywords:
- Windows Media Format SDK,callback methods
- Windows Media Format SDK,methods called asynchronously
- callback methods
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using the Callback Methods

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Several interfaces in the Windows Media Format SDK contain methods that are called asynchronously. Most of these methods use callback functions to pass information to the controlling application.

The following sections describe some of the general issues regarding the use of callback methods with the Windows Media Format SDK.



| Section                                                                          | Description                                                                                                                                                                                          |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Using the OnStatus Callback](using-the-onstatus-callback.md)                   | Describes how to implement the [**IWMStatusCallback::OnStatus**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus) callback method, which is used by several objects to advise applications of SDK operation progress. |
| [Using Events with Asynchronous Calls](using-events-with-asynchronous-calls.md) | Describes a common technique to handle asynchronous method calls in an application.                                                                                                                  |
| [Using the Context Parameter](using-the-context-parameter.md)                   | Introduces the *pvContext* parameter, shared by several callbacks and their calling methods, and explains how to use it.                                                                             |



 

## Related topics

<dl> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 




