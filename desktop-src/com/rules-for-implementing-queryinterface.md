---
title: Rules for Implementing QueryInterface
description: Rules for Implementing QueryInterface
ms.assetid: 6db17ed8-06e4-4bae-bc26-113176cc7e0e
ms.topic: article
ms.date: 05/31/2018
---

# Rules for Implementing QueryInterface

There are three main rules that govern implementing the [**IUnknown::QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)) method on a COM object:

-   Objects must have identity.
-   The set of interfaces on an object instance must be static.
-   It must be possible to query successfully for any interface on an object from any other interface.

## Objects Must Have Identity

For any given object instance, a call to [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)) with IID\_IUnknown must always return the same physical pointer value. This allows you to call **QueryInterface** on any two interfaces and compare the results to determine whether they point to the same instance of an object.

## The Set of Interfaces on an Object Instance Must Be Static

The set of interfaces accessible on an object through [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)) must be static, not dynamic. Specifically, if **QueryInterface** returns S\_OK for a given IID once, it must never return E\_NOINTERFACE on subsequent calls on the same object; and if **QueryInterface** returns E\_NOINTERFACE for a given IID, subsequent calls for the same IID on the same object must never return S\_OK.

## It Must Be Possible to Query Successfully for Any Interface on an Object from Any Other Interface

That is, given the following code:

``` syntax
IA * pA = (some function returning an IA *); 
IB * pB = NULL; 
HRESULT   hr; 
hr = pA->QueryInterface(IID_IB, &pB); 
 
```

the following rules apply:

-   If you have a pointer to an interface on an object, a call like the following to [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)) for that same interface must succeed:

    ``` syntax
    pA->QueryInterface(IID_IA, ...) 
     
    ```

-   If a call to [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)) for a second interface pointer succeeds, a call to **QueryInterface** from that pointer for the first interface must also succeed. If pB was successfully obtained, the following must also succeed:

    ``` syntax
    pB->QueryInterface(IID_IA, ...) 
     
    ```

-   Any interface must be able to query for any other interface on an object. If pB was successfully obtained and you successfully query for a third interface (IC) using that pointer, you must also be able to query successfully for IC using the first pointer, pA. In this case, the following sequence must succeed:

    ``` syntax
    IC * pC = NULL; 
    hr = pB->QueryInterface(IID_IC, &pC); 
    pA->QueryInterface(IID_IC, ...) 
     
    ```

Interface implementations must maintain a counter of outstanding pointer references to all the interfaces on a given object. You should use an **unsigned integer** for the counter.

If a client needs to know that resources have been freed, it must use a method in some interface on the object with higher-level semantics before calling [**IUnknown::Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release).

## Related topics

<dl> <dt>

[Using and Implementing IUnknown](using-and-implementing-iunknown.md)
</dt> </dl>

 

 