---
description: Expose a filter's new interfaces to clients as part of creating a filter property page for a custom DirectShow filter.
ms.assetid: a0e52ba9-9f7c-4cf3-ba5f-b0035ed1794c
title: Step 3. Support QueryInterface
ms.topic: article
ms.date: 05/31/2018
---

# Step 3. Support QueryInterface

To expose the filter's new interfaces to clients, do the following:

-   Include the [**DECLARE\_IUNKNOWN**](declare-iunknown.md) macro in the public declaration section of your filter:
    ```C++
    public:
        DECLARE_IUNKNOWN;
    ```

    

-   Override [**CUnknown::NonDelegatingQueryInterface**](cunknown-nondelegatingqueryinterface.md) to check for the IIDs of the two interfaces:
    ```C++
    STDMETHODIMP CGrayFilter::NonDelegatingQueryInterface(REFIID riid, void **ppv)
    {
        if (riid == IID_ISpecifyPropertyPages)
        {
            return GetInterface(
               static_cast<ISpecifyPropertyPages*>(this),
               ppv);
        }
        else if (riid == IID_ISaturation)
        {
            return GetInterface(static_cast<ISaturation*>(this), ppv);
        }
        else
        {
            // Call the parent class.
            return CBaseFilter::NonDelegatingQueryInterface(riid, ppv);

            // NOTE: This example assumes that the filter inherits directly
            // from CBaseFilter. If your filter inherits from another class,
            // call the NonDelegatingQueryInterface method of that class.
        }
    }
    ```

    

Next: [Step 4. Create the Property Page](step-4--create-the-property-page.md).

## Related topics

<dl> <dt>

[Creating a Filter Property Page](creating-a-filter-property-page.md)
</dt> <dt>

[How to Implement IUnknown](how-to-implement-iunknown.md)
</dt> </dl>

 

 



