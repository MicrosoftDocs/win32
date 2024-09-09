---
description: Using the DMO Class Template
ms.assetid: 5193ad08-aaee-47e3-93eb-a126a66d8f23
title: Using the DMO Class Template
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using the DMO Class Template

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

DirectShow includes a class template, [**IMediaObjectImpl**](imediaobjectimpl-class-template.md), for implementing DMOs. The template handles many of the "bookkeeping" tasks, such as validating input parameters. By using the template, you can focus on the functionality that is specific to your DMO. In addition, the template helps to ensure that you create a robust implementation. The template is defined in the header file Dmoimpl.h, located in the Include directory of the SDK.

The **IMediaObjectImpl** template inherits the [**IMediaObject**](/previous-versions/windows/desktop/api/Mediaobj/nn-mediaobj-imediaobject) interface. To create a DMO using the template, define a new class that derives from **IMediaObjectImpl**. The template implements all of the **IMediaObject** methods. In most cases, the template calls a corresponding private method on the derived class. The template provides the following features:

-   Basic parameter checking. The template methods verify that required parameters are not **NULL**, that stream indexes are within range, and that flags are valid.
-   Locking. The template methods call two internal methods, **Lock** and **Unlock**, to serialize operations on the DMO. This feature ensures that the DMO is thread-safe.
-   Media types. The template stores the media types set by the client, and provides accessor methods for the media types.
-   Streaming. The template prevents streaming until the client has set media types for all non-optional streams. It also ensures that the [**IMediaObject::AllocateStreamingResources**](/previous-versions/windows/desktop/api/Mediaobj/nf-mediaobj-imediaobject-allocatestreamingresources) method is called before streaming begins, which guarantees that resources are allocated.

The derived class must implement the **IUnknown** interface; the template does not provide this interface. You can use the Active Template Library (ATL) to implement **IUnknown**, or you can provide some other implementation. The template also does not implement the locking mechanism. The derived class must implement the **Lock** and **Unlock** methods. If you create your class using ATL, you can use the default ATL implementations.

**Declaring the Derived Class**

The **IMediaObjectImpl** class template is declared as follows:


```C++
template <class _DERIVED_, int NUMBEROFINPUTS, int NUMBEROFOUTPUTS>
class IMediaObjectImpl : public ImediaObject
```



The three template parameters are \_DERIVED\_, NUMBEROFINPUTS, and NUMBEROFOUTPUTS. Set \_DERIVED\_ equal to the name of your class. The other two parameters define the number of input streams and output streams on the DMO. For example, to create a DMO class named CMyDmo that supports one input stream and two output streams, use the following declaration:


```C++
class CMyDmo : public IMediaObjectImpl<CMyDmo, 1, 2>
```



The remainder of this section describes how the template implements the various methods in **IMediaObject**.

**Methods for Setting Media Types**

The following methods set or retrieve media types on the DMO:

-   **GetInputType**, **GetOutputType**. These methods return preferred media types, by stream number and type index. The template calls **InternalGetInputType** or **InternalGetOutputType** on the derived class.
-   **SetInputType**, **SetOutputType**. These methods set the media type on a stream, test a media type, or clear a media type. To validate the media type, the template calls **InternalCheckInputType** or **InternalCheckOutputType** on the derived class. The derived class returns S\_OK to accept the type or DMO\_E\_INVALIDTYPE to reject the type. The template handles setting or clearing the media type.
-   **GetInputCurrentType**, **GetOutputCurrentType**. These methods return the current media type for a stream, or DMO\_E\_TYPE\_NOT\_SET if no type is set. The template completely implements these methods.

**Informational Methods**

The following methods provide information about the DMO.

-   **GetInputMaxLatency**, **SetInputMaxLatency**. These methods retrieve or set the maximum latency. The template calls **InternalGetInputMaxLatency** or **InternalSetInputMaxLatency** on the derived class.
-   **GetInputSizeInfo**, **GetOutputSizeInfo**. These methods return the DMO's buffer requirements for a specified stream. If no media type has been set on that stream, the template returns DMO\_E\_TYPE\_NOT\_SET. Otherwise, it calls **InternalGetInputSizeInfo** or **InternalGetOutputSizeInfo** on the derived class.
-   **GetInputStreamInfo**, **GetOutputStreamInfo**. These methods return various flags that indicate how the client should format the data. The template calls **InternalGetInputStreamInfo** or **InternalGetOutputStreamInfo** on the derived class.
-   **GetStreamCount**. This method returns the number of input and output streams. The template implements this method, using the template parameters.

**Methods for Resource Allocation**

-   The **AllocateStreamingResources** method allocates any resources the DMO needs before streaming begins. The **FreeStreamingResources** method releases the same resources. The template calls **InternalAllocateStreamingResources** and **InternalFreeStreamingResources**, respectively.

The client of the DMO is not required to call these methods, but the template automatically calls **AllocateStreamingResources** before streaming starts. Therefore, the DMO can assume that resources are have been allocated correctly by the time **ProcessInput** is called. The DMO should call **FreeStreamingResources** in its destructor.

Also, when the template calls **InternalAllocateStreamingResources**, it sets an internal flag, so that it does not call that method again until calling **InternalFreeStreamingResources**. This ensures that resources are not re-allocated accidentally, which could cause memory leaks.

**Methods for Streaming**

The following methods are used to stream data:

-   **GetInputStatus**. This method indicates whether the DMO can accept input at this time. The template calls **InternalAcceptingInput** on the derived class. If the DMO can accept input, the derived class returns S\_OK and the template sets the DMO\_INPUT\_STATUSF\_ACCEPT\_DATA bit in the *dwFlags* parameter. Otherwise, the derived class returns S\_FALSE and the template sets *dwFlags* to zero.
-   **ProcessInput**. This method processes an input buffer. The template calls **AllocateStreamingResources**, described previously. Then it calls **InternalAcceptingInput** on the derived class. If the DMO can accept new input, the template calls **InternalProcessInput**.
-   **ProcessOutput**. This method processes a set of output buffers, one buffer for each output stream. The template calls **AllocateStreamingResources** and then **InternalProcessOutput**.
-   **Discontinuity**. This method signals a discontinuity in an input stream. The template calls **InternalAcceptingInput** on the derived class. If that method returns S\_OK, the template calls **InternalDiscontinuity** on the derived class.
-   **Flush**. This method flushes the DMO. The template calls **InternalFlush** on the derived class. The DMO should discard any input buffers that it still holds to be processed.

The template does not provide any direct support for the [**IMediaObjectInPlace**](/previous-versions/windows/desktop/api/mediaobj/nn-mediaobj-imediaobjectinplace) interface.

**Methods for Locking**

Locking is used to protect the DMO's state in a multithreaded environment. In an ATL project, the [**IMediaObject::Lock**](/previous-versions/windows/desktop/api/Mediaobj/nf-mediaobj-imediaobject-lock) method causes a name conflict with the ATL **Lock** method. To resolve the conflict, the template renames the **IMediaObject** method to **DMOLock**. When you compile the derived class, define FIX\_LOCK\_NAME before including the header file Dmo.h:


```C++
#define FIX_LOCK_NAME
#include <dmo.h>
```



This directive causes the preprocessor to substitute **DMOLock** for **Lock** in the declaration of the **IMediaObject** interface. Applications can still invoke the method using the name **Lock**, because the vtable order does not change. The **DMOLock** method calls **Lock** or **Unlock** on the derived class. If you are using ATL to implement the derived class, these methods are already defined by ATL, so no additional code is necessary. If you are not using ATL, you must provide **Lock** and **Unlock** methods in your derived class.

The template automatically locks the DMO in each of the **IMediaObject** methods. The derived class might need to lock the DMO inside other public methods that it implements (for example, if it supports **IMediaObjectInPlace**). The class template also provides an internal helper class, [**IMediaObjectImpl::LockIt**](imediaobjectimpl-lockit.md), which is useful for locking and unlocking the DMO.

**Summary**

For the following **IMediaObject** methods, the template calls a corresponding method with the same signature on the derived class. The derived class must implement each of the methods shown in the second column.



| IMediaObject Method            | Derived Class Method                   |
|--------------------------------|----------------------------------------|
| **AllocateStreamingResources** | **InternalAllocateStreamingResources** |
| **Discontinuity**              | **InternalDiscontinuity**              |
| **Flush**                      | **InternalFlush**                      |
| **FreeStreamingResources**     | **InternalFreeStreamingResources**     |
| **GetInputMaxLatency**         | **InternalGetInputMaxLatency**         |
| **GetInputSizeInfo**           | **InternalGetInputSizeInfo**           |
| **GetInputStreamInfo**         | **InternalGetInputStreamInfo**         |
| **GetInputType**               | **InternalGetInputType**               |
| **GetOutputSizeInfo**          | **InternalGetOutputSizeInfo**          |
| **GetOutputStreamInfo**        | **InternalGetOutputStreamInfo**        |
| **GetOutputType**              | **InternalGetOutputType**              |
| **ProcessInput**               | **InternalProcessInput**               |
| **ProcessOutput**              | **InternalProcessOutput**              |
| **SetInputMaxLatency**         | **InternalSetInputMaxLatency**         |



 

For the remaining **IMediaObject** methods, there is not a one-to-one correspondence between template methods and derived-class methods. The following table summarizes which methods are fully implemented by the template, and which methods call other methods on the derived class.



| IMediaObject Method                   | Derived Class Method                                                             |
|---------------------------------------|----------------------------------------------------------------------------------|
| **GetInputCurrentType**               | Fully implemented                                                                |
| **GetOutputCurrentType**              | Fully implemented                                                                |
| **GetStreamCount**                    | Fully implemented                                                                |
| **GetInputStatus**                    | [**InternalAcceptingInput**](/previous-versions/ms809095(v=msdn.10))        |
| **Lock** (implemented as **DMOLock**) | [**Lock**](/previous-versions/ms809100(v=msdn.10)), [**Unlock**](/previous-versions/ms809101(v=msdn.10)) |
| **SetInputType**                      | [**InternalCheckInputType**](/previous-versions/ms809096(v=msdn.10))        |
| **SetOutputType**                     | [**InternalCheckOutputType**](/previous-versions/ms809098(v=msdn.10))      |



 

## Related topics

<dl> <dt>

[**IMediaObjectImpl Class Template**](imediaobjectimpl-class-template.md)
</dt> <dt>

[Writing a DMO](writing-a-dmo.md)
</dt> </dl>

 

 
