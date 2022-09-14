---
description: To gain more detailed control over the autocomplete behavior, or to add a custom source of autocomplete strings, you must manage the autocomplete object yourself.
ms.assetid: E1A7B1B0-2879-452E-9EBB-73F02B932200
title: How to Enable Autocomplete Manually
ms.topic: article
ms.date: 05/31/2018
---

# How to Enable Autocomplete Manually

To gain more detailed control over the autocomplete behavior, or to add a custom source of autocomplete strings, you must manage the autocomplete object yourself. You can enable autocomplete manually in the following ways.

## Instructions

### Creating a Simple Autocomplete Object

The following steps show how to create and initialize a simple autocomplete object. A simple autocomplete object completes strings from a single source. Error checking has been intentionally omitted in this example.

1.  Create the autocomplete object.

    ```C++
    IAutoComplete *pac;

    HRESULT hr = CoCreateInstance(CLSID_AutoComplete, 
                                    NULL, 
                                  CLSCTX_INPROC_SERVER,
                                  IID_PPV_ARGS(&pac));
    ```

    

2.  Create the autocomplete source. You can use a [predefined autocomplete source](ac-ovw.md) or you can write your own custom source.

    The following code uses one of the predefined autocomplete sources.

    ```C++
    IUnknown *punkSource;

    hr = CoCreateInstance(CLSID_ACListISF, 
                          NULL, 
                          CLSCTX_INPROC_SERVER,
                          IID_PPV_ARGS(&punkSource));
    ```

    

    The following code uses a custom autocomplete source. You can write your own autocomplete source by implementing an object that exposes the [**IEnumString**](/windows/win32/api/objidlbase/nn-objidlbase-ienumstring) interface. The object can also optionally implement the [**IACList**](/windows/win32/api/shlobj_core/nn-shlobj_core-iaclist) and [**IACList2**](/windows/win32/api/shlobj_core/nn-shlobj_core-iaclist2) interfaces.

    ```C++
    CCustomAutoCompleteSource *pcacs = new CCustomAutoCompleteSource();

    hr = pcacs->QueryInterface(IID_PPV_ARGS(&punkSource));
    if(SUCCEEDED(hr))
    {
        // ...
    }

    pcacs->Release();
    ```

    

3.  Set the options on the autocomplete source (optional).

    You can customize the behavior of the autocomplete source by setting its options if the source exposes the [**IACList2**](/windows/win32/api/shlobj_core/nn-shlobj_core-iaclist2) interface. When using the predefined autocomplete sources, only CLSID\_ACListISF exports **IACList2**. For a complete list of options and their values, see [**IACList2::SetOptions**](/windows/win32/api/shlobj_core/nf-shlobj_core-iaclist2-setoptions).

    ```C++
    IACList2 *pal2;

    hr = punkSource->QueryInterface(IID_PPV_ARGS(&pal2));
    if (SUCCEEDED(hr))
    {
        hr = pal2->SetOptions(ACLO_FILESYSONLY);
        pal2->Release();
    }
    ```

    

4.  Initialize the autocomplete object.

    In this example, **hwndEdit** is the handle of the edit control window for which autocomplete is to be enabled. See [**IAutoComplete::Init**](/windows/desktop/api/Shldisp/nf-shldisp-iautocomplete-init) for a description of the final two unused parameters.

    ```C++
    hr = pac->Init(hwndEdit, punkSource, NULL, NULL);
    ```

    

5.  Set the options of the autocomplete object (optional).

    You can customize the behavior of the autocomplete object by setting its options. For a complete list of options and their values, see the documentation for [**IACList2::SetOptions**](/windows/win32/api/shlobj_core/nf-shlobj_core-iaclist2-setoptions).

    ```C++
    IAutoComplete2 *pac2;

    hr = pac->QueryInterface(IID_PPV_ARGS(&pac2));

    if (SUCCEEDED(hr))
    {
        hr = pac2->SetOptions(ACO_AUTOSUGGEST);
        pac2->Release();
    }
    ```

    

6.  Release the objects.

    > [!Note]  
    > The autocomplete object remains attached to the edit control even after you release it. If you foresee a need to access these objects later—if you want to change the autocomplete options at a later time, for example—it is not required that you release them at this point.

     

    ```C++
    punkSource->Release();
    pac->Release();
    ```

    

### Creating a Compound Autocomplete Object

A compound autocomplete object matches against strings from multiple sources. For example, the Windows Internet Explorer Address bar uses a compound autocomplete object because the user might begin typing the name of a file or a URL. Most of the steps involved in creating a compound autocomplete object are identical to the steps in "Creating a Simple Autocomplete Object." Those steps are indicated as such.

1.  Create the autocomplete object. This is the same as step 1 above.

2.  Create the autocomplete compound source object manager.

    The autocomplete compound source object allows multiple autocomplete sources to be combined into a single autocomplete source.

    ```C++
    IObjMgr *pom;

    hr = CoCreateInstance(CLSID_ACLMulti, 
                          NULL, 
                          CLSCTX_INPROC_SERVER,
                          IID_PPV_ARGS(&pom));
    ```

    

3.  Create and set options for each of the autocomplete sources. Repeat steps 2 and 3 above for each source.

4.  Attach each autocomplete source to the source object manager.

    ```C++
    hr = pom->Append(punkSource1);
    hr = pom->Append(punkSource2);
    ```

    

5.  Initialize the autocomplete object.

    This is the same as step 4 above, except that instead of passing the simple autocomplete source to [**IAutoComplete::Init**](/windows/desktop/api/Shldisp/nf-shldisp-iautocomplete-init), you pass the compound source object manager.

    ```C++
    hr = pac->Init(hwndEdit, pom, NULL, NULL);
    ```

    

6.  Set the options of the autocomplete object. This is the same as step 5 above.

7.  Release the objects.

    As in the simple case, you can release the objects as soon as you are finished using them, but you can also retain them to change options later.

    ```C++
    pac->Release();
    pom->Release();

    // Release each individual source.
    punkSource1->Release(); 
    punkSource2->Release();
    ```

    

 

 
