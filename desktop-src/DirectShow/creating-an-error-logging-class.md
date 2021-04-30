---
description: This topic describes how to implement error logging in DirectShow Editing Services.
ms.assetid: c0b3b25c-ed03-4f78-9c53-0c0bcff1c60c
title: Creating an Error Logging Class
ms.topic: article
ms.date: 05/31/2018
---

# Creating an Error Logging Class

\[This API is not supported and may be altered or unavailable in the future.\]

This topic describes how to implement error logging in [DirectShow Editing Services](directshow-editing-services.md).

First, declare a class that will implement error logging. The class inherits the [**IAMErrorLog**](iamerrorlog.md) interface. It contains declarations for the three **IUnknown** methods, and for the single method in [IAMErrorLog](implementing-iamerrorlog.md). The class declaration is as follows:


```C++
class CErrReporter : public IAMErrorLog
{
protected:
    long    m_lRef; // Reference count.

public:
    CErrReporter() { m_lRef = 0; }

    // IUnknown
    STDMETHOD(QueryInterface(REFIID, void**));
    STDMETHOD_(ULONG, AddRef());
    STDMETHOD_(ULONG, Release());

    // IAMErrorLog
    STDMETHOD(LogError(LONG, BSTR, LONG, HRESULT, VARIANT*));
};
```



The only member variable in the class is m\_lRef, which holds the object's reference count.

Next, define the methods in **IUnknown**. The following example shows a standard implementation for these methods:


```C++
STDMETHODIMP CErrReporter::QueryInterface(REFIID riid, void **ppv)
{
    if (ppv == NULL) return E_POINTER;

    *ppv = NULL;
    if (riid == IID_IUnknown)
        *ppv = static_cast<IUnknown*>(this);
    else if (riid == IID_IAMErrorLog)
        *ppv = static_cast<IAMErrorLog*>(this);
        
    else 
    return E_NOINTERFACE;

    AddRef();
    return S_OK;
}

STDMETHODIMP_(ULONG) CErrReporter::AddRef()
{
    return InterlockedIncrement(&m_lRef);
}

STDMETHODIMP_(ULONG) CErrReporter::Release()
{
    // Store the decremented count in a temporary
    // variable. 
    ULONG uCount = InterlockedDecrement(&m_lRef);
    if (uCount == 0)
    {
        delete this;
    }
    // Return the temporary variable, not the member
    // variable, for thread safety.
    return uCount;
}
```



With the COM framework in place, you can now implement the **IAMErrorLog** interface. The next section describes how to do this.

## Related topics

<dl> <dt>

[Logging Errors](logging-errors.md)
</dt> </dl>

 

 



