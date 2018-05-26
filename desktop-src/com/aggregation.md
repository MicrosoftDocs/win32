---
title: Aggregation
description: Aggregation is the object reuse mechanism in which the outer object exposes interfaces from the inner object as if they were implemented on the outer object itself.
ms.assetid: 6845b114-8f43-47ad-acdf-b63d6008d221
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Aggregation

Aggregation is the object reuse mechanism in which the outer object exposes interfaces from the inner object as if they were implemented on the outer object itself. This is useful when the outer object delegates every call to one of its interfaces to the same interface in the inner object. Aggregation is available as a convenience to avoid extra implementation overhead in the outer object in this case. Aggregation is actually a specialized case of [containment/delegation](containment-delegation.md).

Aggregation is almost as simple to implement as containment is, except for the three [**IUnknown**](/windows/win32/Unknwn/nn-unknwn-iunknown?branch=master) functions: [**QueryInterface**](/windows/win32/Unknwn/nf-unknwn-iunknown-queryinterface(q,)?branch=master), [**AddRef**](/windows/win32/unknwnbase/nf-unknwn-iunknown-addref?branch=master), and [**Release**](/windows/win32/unknwnbase/nf-unknwn-iunknown-release?branch=master). The catch is that from the client's perspective, any **IUnknown** function on the outer object must affect the outer object. That is, **AddRef** and **Release** affect the outer object and **QueryInterface** exposes all the interfaces available on the outer object. However, if the outer object simply exposes an inner object's interface as its own, that inner object's **IUnknown** members called through that interface will behave differently than those **IUnknown** members on the outer object's interfaces, an absolute violation of the rules and properties governing **IUnknown**.

The solution is that aggregation requires an explicit implementation of [**IUnknown**](/windows/win32/Unknwn/nn-unknwn-iunknown?branch=master) on the inner object and delegation of the **IUnknown** methods of any other interface to the outer object's **IUnknown** methods.

## Creating Aggregable Objects

Creating objects that can be aggregated is optional; however, it is simple to do and provides significant benefits. The following rules apply to creating an aggregable object:

-   The aggregable (or inner) object's implementation of [**QueryInterface**](/windows/win32/Unknwn/nf-unknwn-iunknown-queryinterface(q,)?branch=master), [**AddRef**](/windows/win32/unknwnbase/nf-unknwn-iunknown-addref?branch=master), and [**Release**](/windows/win32/unknwnbase/nf-unknwn-iunknown-release?branch=master) for its [**IUnknown**](/windows/win32/Unknwn/nn-unknwn-iunknown?branch=master) interface controls the inner object's reference count, and this implementation must not delegate to the outer object's unknown (the controlling **IUnknown**).
-   The aggregable (or inner) object's implementation of [**QueryInterface**](/windows/win32/Unknwn/nf-unknwn-iunknown-queryinterface(q,)?branch=master), [**AddRef**](/windows/win32/unknwnbase/nf-unknwn-iunknown-addref?branch=master), and [**Release**](/windows/win32/unknwnbase/nf-unknwn-iunknown-release?branch=master) for its other interfaces must delegate to the controlling [**IUnknown**](/windows/win32/Unknwn/nn-unknwn-iunknown?branch=master) and must not directly affect the inner object's reference count.
-   The inner [**IUnknown**](/windows/win32/Unknwn/nn-unknwn-iunknown?branch=master) must implement [**QueryInterface**](/windows/win32/Unknwn/nf-unknwn-iunknown-queryinterface(q,)?branch=master) only for the inner object.
-   The aggregable object must not call [**AddRef**](/windows/win32/unknwnbase/nf-unknwn-iunknown-addref?branch=master) when holding a reference to the controlling [**IUnknown**](/windows/win32/Unknwn/nn-unknwn-iunknown?branch=master) pointer.
-   When the object is created, if any interface other than [**IUnknown**](/windows/win32/Unknwn/nn-unknwn-iunknown?branch=master) is requested, the creation must fail with E\_NOINTERFACE.

The following code fragment illustrates a correct implementation of an aggregable object by using the nested class method of implementing interfaces:


```C++
// CSomeObject is an aggregable object that implements 
// IUnknown and ISomeInterface 
class CSomeObject : public IUnknown 
{ 
    private: 
        DWORD        m_cRef;         // Object reference count 
        IUnknown*    m_pUnkOuter;    // Controlling IUnknown, no AddRef 
 
        // Nested class to implement the ISomeInterface interface 
        class CImpSomeInterface : public ISomeInterface 
        { 
            friend class CSomeObject ; 
            private: 
                DWORD    m_cRef;    // Interface ref-count, for debugging 
                IUnknown*    m_pUnkOuter;    // Controlling IUnknown 
            public: 
                CImpSomeInterface() { m_cRef = 0;   }; 
                ~ CImpSomeInterface(void) {}; 
 
                // IUnknown members delegate to the outer unknown 
                // IUnknown members do not control lifetime of object 
                STDMETHODIMP     QueryInterface(REFIID riid, void** ppv) 
                {    return m_pUnkOuter->QueryInterface(riid,ppv);   }; 
 
                STDMETHODIMP_(DWORD) AddRef(void) 
                {    return m_pUnkOuter->AddRef();   }; 
 
                STDMETHODIMP_(DWORD) Release(void) 
                {    return m_pUnkOuter->Release();   }; 
 
                // ISomeInterface members 
                STDMETHODIMP SomeMethod(void) 
                {    return S_OK;   }; 
        } ; 
        CImpSomeInterface m_ImpSomeInterface ; 
    public: 
        CSomeObject(IUnknown * pUnkOuter) 
        { 
            m_cRef=0; 
            // No AddRef necessary if non-NULL as we're aggregated. 
            m_pUnkOuter=pUnkOuter; 
            m_ImpSomeInterface.m_pUnkOuter=pUnkOuter; 
        } ; 
        ~CSomeObject(void) {} ; 
 
        // Static member function for creating new instances (don't use 
        // new directly). Protects against outer objects asking for 
        // interfaces other than Iunknown. 
        static HRESULT Create(IUnknown* pUnkOuter, REFIID riid, void **ppv) 
        { 
            CSomeObject*        pObj; 
            if (pUnkOuter != NULL &amp;&amp; riid != IID_IUnknown) 
                return CLASS_E_NOAGGREGATION; 
            pObj = new CSomeObject(pUnkOuter); 
            if (pObj == NULL) 
                return E_OUTOFMEMORY; 
            // Set up the right unknown for delegation (the non-
            // aggregation case) 
            if (pUnkOuter == NULL) 
            {
                pObj->m_pUnkOuter = (IUnknown*)pObj ; 
                pObj->m_ImpSomeInterface.m_pUnkOuter = (IUnknown*)pObj;
            }
            HRESULT hr; 
            if (FAILED(hr = pObj->QueryInterface(riid, (void**)ppv))) 
                delete pObj ; 
            return hr; 
        } 
 
        // Inner IUnknown members, non-delegating 
        // Inner QueryInterface only controls inner object 
        STDMETHODIMP QueryInterface(REFIID riid, void** ppv) 
        { 
            *ppv=NULL; 
            if (riid == IID_IUnknown) 
                *ppv=this; 
            if (riid == IID_ISomeInterface) 
                *ppv=&amp;m_ImpSomeInterface; 
            if (NULL==*ppv) 
                return ResultFromScode(E_NOINTERFACE); 
            ((IUnknown*)*ppv)->AddRef(); 
            return NOERROR; 
        } ; 
        STDMETHODIMP_(DWORD) AddRef(void) 
        {    return ++m_cRef; }; 
        STDMETHODIMP_(DWORD) Release(void) 
        { 
            if (--m_cRef != 0) 
                return m_cRef; 
            delete this; 
            return 0; 
        }; 
}; 
 
```



## Aggregating Objects

When developing an aggregable object, the following rules apply:

-   When creating the inner object, the outer object must explicitly ask for its [**IUnknown**](/windows/win32/Unknwn/nn-unknwn-iunknown?branch=master).
-   The outer object must protect its implementation of [**Release**](/windows/win32/unknwnbase/nf-unknwn-iunknown-release?branch=master) from reentrancy with an artificial reference count around its destruction code.
-   The outer object must call its controlling [**IUnknown**](/windows/win32/Unknwn/nn-unknwn-iunknown?branch=master)Â [**Release**](/windows/win32/unknwnbase/nf-unknwn-iunknown-release?branch=master) method if it queries for a pointer to any of the inner object's interfaces. To free this pointer, the outer object calls its controlling **IUnknown**Â [**AddRef**](/windows/win32/unknwnbase/nf-unknwn-iunknown-addref?branch=master) method, followed by **Release** on the inner object's pointer.
    ```C++
    // Obtaining inner object interface pointer 
    pUnkInner->QueryInterface(IID_ISomeInterface, &amp;pISomeInterface); 
    pUnkOuter->Release(); 
     
    // Releasing inner object interface pointer 
    pUnkOuter->AddRef(); 
    pISomeInterface->Release(); 
     
    ```

    

-   The outer object must not blindly delegate a query for any unrecognized interface to the inner object, unless that behavior is specifically the intention of the outer object.

## Related topics

<dl> <dt>

[Containment/Delegation](containment-delegation.md)
</dt> </dl>

 

 




