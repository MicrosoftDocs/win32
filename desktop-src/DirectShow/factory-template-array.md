---
description: Factory Template Array
ms.assetid: 310afccd-42a6-426e-b455-7bf98062bf36
title: Factory Template Array
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Factory Template Array

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The factory template contains the following public member variables:

``` syntax
const WCHAR *              m_Name;                // Name
const CLSID *              m_ClsID;               // CLSID
LPFNNewCOMObject           m_lpfnNew;             // Function to create an instance
                                                  //   of the component
LPFNInitRoutine            m_lpfnInit;            // Initialization function (optional)
const AMOVIESETUP_FILTER * m_pAMovieSetup_Filter; // Set-up information (for filters)
```

The two function pointers, [**m\_lpfnNew**](cfactorytemplate-m-lpfnnew.md) and [**m\_lpfnInit**](cfactorytemplate-m-lpfninit.md), use the following type definitions:

``` syntax
typedef CUnknown *(CALLBACK *LPFNNewCOMObject)(LPUNKNOWN pUnkOuter, HRESULT *phr);
typedef void (CALLBACK *LPFNInitRoutine)(BOOL bLoading, const CLSID *rclsid);
```

The first is the instantiation function for the component. The second is an optional initialization function. If you provide an initialization function, it is called from inside the DLL entry-point function. (The DLL entry-point function is discussed later in this article.)

Suppose you are creating a DLL that contains a component named CMyComponent, which inherits from [**CUnknown**](cunknown.md). You must provide the following items in your DLL:

-   The initialization function, a public method that returns a new instance of CMyComponent.
-   A global array of factory templates, named *g\_Templates.* This array contains the factory template for CMyComponent.
-   A global variable named *g\_cTemplates* that specifies the size of the array.

The following example shows how to declare these items:


```C++
// Public method that returns a new instance. 
CUnknown * WINAPI CMyComponent::CreateInstance(LPUNKNOWN pUnk, HRESULT *pHr) 
{
    CMyComponent *pNewObject = new CMyComponent(NAME("My Component"), pUnk, pHr );
    if (pNewObject == NULL) {
        *pHr = E_OUTOFMEMORY;
    }
    return pNewObject;
} 

CFactoryTemplate g_Templates[1] = 
{
    { 
      L"My Component",                // Name
      &CLSID_MyComponent,             // CLSID
      CMyComponent::CreateInstance,   // Method to create an instance of MyComponent
      NULL,                           // Initialization function
      NULL                            // Set-up information (for filters)
    }
};
int g_cTemplates = sizeof(g_Templates) / sizeof(g_Templates[0]);    
```



The `CreateInstance` method calls the class constructor and returns a pointer to the new class instance. The parameter *pUnk* is a pointer to the aggregating [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown). You can simply pass this parameter to the class constructor. The parameter *pHr* is a pointer to an HRESULT value. The class constructor sets this to an appropriate value, but if the constructor fails, set the value to E\_OUTOFMEMORY.

The [**NAME**](name.md) macro generates a string in debug builds but resolves to **NULL** in retail builds. It is used in this example to give the component a name that appears in debug logs but does not occupy memory in the final version.

The `CreateInstance` method can have any name, because the class factory refers to the function pointer in the factory template. However, *g\_Templates* and *g\_cTemplates* are global variables that the class factory expects to find, so they must have exactly those names.

## Related topics

<dl> <dt>

[How to Create a DirectShow Filter DLL](how-to-create-a-dll.md)
</dt> </dl>

 

 
