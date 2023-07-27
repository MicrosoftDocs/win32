---
description: How IUnknown Works
ms.assetid: 926778a5-e941-4424-8bc0-b50c925fd08b
title: How IUnknown Works
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# How IUnknown Works

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The methods in **IUnknown** enable an application to query for interfaces on the component and manage the component's reference count.

**Reference Count**

The reference count is an internal variable, incremented in the **AddRef** method and decremented in the **Release** method. The base classes manage the reference count and synchronize access to the reference count among multiple threads.

**Interface Queries**

Querying for an interface is also straightforward. The caller passes two parameters: an interface identifier (IID), and the address of a pointer. If the component supports the requested interface, it sets the pointer to the interface, increments its own reference count, and returns S\_OK. Otherwise, it sets the pointer to **NULL** and returns E\_NOINTERFACE. The following pseudocode shows the general outline of the **QueryInterface** method. Component aggregation, described in the next section, introduces some additional complexity.


```C++
if (IID == IID_IUnknown)
    set pointer to (IUnknown *)this
    AddRef
    return S_OK

else if (IID == IID_ISomeInterface)
    set pointer to (ISomeInterface *)this
    AddRef
    return S_OK

else if ... 

else
    set pointer to NULL
    return E_NOINTERFACE
```



The only difference between the **QueryInterface** method of one component and the **QueryInterface** method of another is the list of IIDs that each component tests. For every interface that the component supports, the component must test for the IID of that interface.

**Aggregation and Delegation**

Component aggregation must be transparent to the caller. Therefore, the aggregate must expose a single **IUnknown** interface, with the aggregated component deferring to the outer component's implementation. Otherwise, the caller would see two different **IUnknown** interfaces in the same aggregate. If the component is not aggregated, it uses its own implementation.

To support this behavior, the component must add a level of indirection. A *delegating IUnknown* delegates the work to the appropriate place: to the outer component, if there is one, or to the component's internal version. A *nondelegating IUnknown* does the work, as described in the previous section.

The delegating version is public and keeps the name **IUnknown**. The nondelegating version is renamed [**INonDelegatingUnknown**](inondelegatingunknown.md). This name is not part of the COM specification, because it is not a public interface.

When the client creates an instance of the component, it calls the **IClassFactory::CreateInstance** method. One parameter is a pointer to the aggregating component's **IUnknown** interface, or **NULL** if the new instance is not aggregated. The component uses this parameter to store a member variable indicating which **IUnknown** interface to use, as shown in the following example:


```C++
CMyComponent::CMyComponent(IUnknown *pOuterUnkown)
{
    if (pOuterUnknown == NULL)
        m_pUnknown = (IUnknown *)(INonDelegatingUnknown *)this;
    else
        m_pUnknown = pOuterUnknown;

    [ ... more constructor code ... ]
}
```



Each method in the delegating **IUnknown** calls its nondelegating counterpart, as shown in the following example:


```C++
HRESULT QueryInterface(REFIID iid, void **ppv) 
{
    return m_pUnknown->QueryInterface(iid, ppv);
}
```



By the nature of delegation, the delegating methods look identical in every component. Only the nondelegating versions change.

## Related topics

<dl> <dt>

[How to Implement IUnknown](how-to-implement-iunknown.md)
</dt> </dl>

 

 



