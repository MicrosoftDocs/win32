---
description: DirectShow implements IUnknown in a base class called CUnknown.
ms.assetid: 1fc74db6-c23a-464f-b9fa-b19d7e8672b7
title: Using CUnknown
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using CUnknown

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

DirectShow implements [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) in a base class called [**CUnknown**](cunknown.md). You can use **CUnknown** to derive other classes, overriding only the methods that change across components. Most of the other base classes in DirectShow derive from **CUnknown**, so your component can inherit directly from **CUnknown** or from another base class.

## INonDelegatingUnknown

[**CUnknown**](cunknown.md) implements [**INonDelegatingUnknown**](inondelegatingunknown.md). It manages reference counts internally, and in most situations your derived class can inherit the two reference-counting methods with no change. Be aware that **CUnknown** deletes itself when the reference count drops to zero. On the other hand, you must override [**CUnknown::NonDelegatingQueryInterface**](cunknown-nondelegatingqueryinterface.md), because the method in the base class returns E\_NOINTERFACE if it receives any IID other than IID\_IUnknown. In your derived class, test for the IIDs of interfaces that you support, as shown in the following example:


```C++
STDMETHODIMP NonDelegatingQueryInterface(REFIID riid, void **ppv)
{
    if (riid == IID_ISomeInterface)
    {
        return GetInterface((ISomeInterface*)this, ppv);
    }
    // Default: Call parent class method. 
    // The CUnknown class must be in the inheritance chain.
    return CParentClass::NonDelegatingQueryInterface(riid, ppv);
}
```



The utility function [**GetInterface**](getinterface.md) (see [**COM Helper Functions**](com-helper-functions.md)) sets the pointer, increments the reference count in a thread-safe way, and returns S\_OK. In the default case, call the base class method and return the result. If you derive from another base class, call its [**NonDelegatingQueryInterface**](cunknown-nondelegatingqueryinterface.md) method instead. This enables you to support all the interfaces that the parent class supports.

## IUnknown

As mentioned earlier, the delegating version of [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) is the same for every component, because it does nothing more than invoke the correct instance of the nondelegating version. For convenience, the header file Combase.h contains a macro, [**DECLARE\_IUNKNOWN**](declare-iunknown.md), which declares the three delegating methods as inline methods. It expands to the following code:


```C++
STDMETHODIMP QueryInterface(REFIID riid, void **ppv) {      
    return GetOwner()->QueryInterface(riid,ppv);            
};                                                          
STDMETHODIMP_(ULONG) AddRef() {                             
    return GetOwner()->AddRef();                            
};                                                          
STDMETHODIMP_(ULONG) Release() {                            
    return GetOwner()->Release();                           
};
```



The utility function [**CUnknown::GetOwner**](cunknown-getowner.md) retrieves a pointer to the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface of the component that owns this component. For an aggregated component, the owner is the outer component. Otherwise, the component owns itself. Include the DECLARE\_IUNKNOWN macro in the public section of your class definition.

## Class Constructor

Your class constructor should invoke the constructor method for the parent class, in addition to anything it does that is specific to your class. The following example is a typical constructor method:


```C++
CMyComponent(TCHAR *tszName, LPUNKNOWN pUnk, HRESULT *phr) 
    : CUnknown(tszName, pUnk, phr)
{ 
    /* Other initializations */ 
};
```



The method takes the following parameters, which it passes directly to the [**CUnknown**](cunknown.md) constructor method.

-   *tszName* specifies a name for the component.
-   *pUnk* is a pointer to the aggregating [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown).
-   *pHr* is a pointer to an HRESULT value, indicating the success or failure of the method.

## Summary

The following example shows a derived class that supports [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) and a hypothetical interface named ISomeInterface:


```C++
class CMyComponent : public CUnknown, public ISomeInterface
{
public:

    DECLARE_IUNKNOWN;

    STDMETHODIMP NonDelegatingQueryInterface(REFIID riid, void **ppv)
    {
        if( riid == IID_ISomeInterface )
        {
            return GetInterface((ISomeInterface*)this, ppv);
        }
        return CUnknown::NonDelegatingQueryInterface(riid, ppv);
    }

    CMyComponent(TCHAR *tszName, LPUNKNOWN pUnk, HRESULT *phr) 
        : CUnknown(tszName, pUnk, phr)
    { 
        /* Other initializations */ 
    };

    // More declarations will be added later.
};
```



This example illustrates the following points:

-   The [**CUnknown**](cunknown.md) class implements the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. The new component inherits from **CUnknown** and from any interfaces that the component supports. The component could derive instead from another base class that inherits from **CUnknown**.
-   The [**DECLARE\_IUNKNOWN**](declare-iunknown.md) macro declares the delegating [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) methods as inline methods.
-   The [**CUnknown**](cunknown.md) class provides the implementation for [**INonDelegatingUnknown**](inondelegatingunknown.md).
-   To support an interface other than [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown), the derived class must override the [**NonDelegatingQueryInterface**](cunknown-nondelegatingqueryinterface.md) method and test for the IID of the new interface.
-   The class constructor invokes the constructor method for [**CUnknown**](cunknown.md).

The next step in writing a filter is to enable an application to create new instances of the component. This requires an understanding of DLLs and their relation to class factories and class constructor methods. For more information, see [How to Create a DirectShow Filter DLL](how-to-create-a-dll.md).

## Related topics

<dl> <dt>

[How to Implement IUnknown](how-to-implement-iunknown.md)
</dt> </dl>

 

 
