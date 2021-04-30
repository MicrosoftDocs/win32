---
description: Step 1.
ms.assetid: 1912af22-11dc-4864-8c20-91675d4f45d9
title: Step 1. Define a Mechanism for Setting the Property
ms.topic: article
ms.date: 05/31/2018
---

# Step 1. Define a Mechanism for Setting the Property

The filter must support a way for the property page to communicate with it, so that the property page can set and retrieve properties on the filter. Possible mechanisms include the following:

-   Expose a custom COM interface.
-   Support Automation properties, through **IDispatch**.
-   Expose the **IPropertyBag** interface and define a set of named properties.

This example uses a custom COM interface, named ISaturation. This is not an actual DirectShow interface; it is defined only for this example. Start by declaring the interface in a header file, along with the interface identifier (IID):


```C++
// Always create new GUIDs! Never copy a GUID from an example.
DEFINE_GUID(IID_ISaturation, 0x19412d6e, 0x6401, 
0x475c, 0xb0, 0x48, 0x7a, 0xd2, 0x96, 0xe1, 0x6a, 0x19);

interface ISaturation : public IUnknown
{
    STDMETHOD(GetSaturation)(long *plSat) = 0;
    STDMETHOD(SetSaturation)(long lSat) = 0;
};
```



You can also define the interface with IDL and use the MIDL compiler to create the header file. Next, implement the custom interface in the filter. This example uses "Get" and "Set" methods for the filter's saturation value. Notice that both methods protect the m\_lSaturation member with a critical section.


```C++
class CGrayFilter : public ISaturation, /* Other inherited classes. */
{
private:
    CCritSec  m_csShared;    // Protects shared data.
    long      m_lSaturation; // Saturation level.
public:
    STDMETHODIMP GetSaturation(long *plSat)
    {
        if (!plSat) return E_POINTER;
        CAutoLock lock(&m_csShared);
        *plSat = m_lSaturation;
        return S_OK;
    }
    STDMETHODIMP SetSaturation(long lSat)
    {
        CAutoLock lock(&m_csShared);
        if (lSat < SATURATION_MIN || lSat > SATURATION_MAX)
        {
            return E_INVALIDARG;
        }
        m_lSaturation = lSat;
        return S_OK;
    }
};
```



Of course, the details of your own implementation will differ from the example shown here.

Next: [Step 2. Implement ISpecifyPropertyPages](step-2--implement-ispecifypropertypages.md).

## Related topics

<dl> <dt>

[**CCritSec Class**](ccritsec.md)
</dt> <dt>

[Creating a Filter Property Page](creating-a-filter-property-page.md)
</dt> </dl>

 

 



