---
description: Overview of Error Logging
ms.assetid: 1037f354-0415-4a5c-a96c-20ae714981af
title: Overview of Error Logging
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Overview of Error Logging

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[This API is not supported and may be altered or unavailable in the future.\]

To give applications maximum flexibility in handling errors, [DirectShow Editing Services](directshow-editing-services.md) uses a callback mechanism. Your application implements a method for logging an error. At run time, if an error occurs, DES calls the method you have provided. The method takes parameters that describe the error. What the method does with this information is up to you. (It should return as quickly as possible, however, or it might interfere with the execution of the program.)

The error logging callback method is contained in a COM interface, [**IAMErrorLog**](iamerrorlog.md). Your application must implement this interface. Like all COM interfaces, **IAMErrorLog** inherits the **IUnknown** interface, so your application must implement that as well.

You have several choices for implementing these COM interfaces. You can use the Active Template Library (ATL), which provides stock implementations of the **IUnknown** methods. DirectShow also provides a C++ base class, [**CUnknown**](cunknown.md), that makes it easy to implement a COM interface. For information on using **CUnknown**, see [How to Implement IUnknown](how-to-implement-iunknown.md).

The sample code in this article defines a self-contained C++ class, which implements both **IUnknown** and **IAMErrorLog**. The result is not a true COM object, because it does not support **CoCreateInstance**. However, this approach is adequate for the purpose of the example.

## Related topics

<dl> <dt>

[Logging Errors](logging-errors.md)
</dt> </dl>

 

 



