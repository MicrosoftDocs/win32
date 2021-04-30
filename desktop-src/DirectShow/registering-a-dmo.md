---
description: Registering a DMO
ms.assetid: 9f74fc1c-b903-4725-b667-3c56a2726dbc
title: Registering a DMO
ms.topic: article
ms.date: 05/31/2018
---

# Registering a DMO

In order for clients to use your DMO, the CLSID must be registered on the user's system. This is done through the DLL's **DllRegisterServer** function. If you are using the Active Template Library (ATL), the ATL wizard automatically generates this function.

You can also register your DMO under one or more standard DMO categories. This enables clients to discover your DMO using the [**DMOEnum**](/previous-versions/windows/desktop/api/Dmoreg/nf-dmoreg-dmoenum) function. The categories are defined by GUID, and are listed in the section [DMO GUIDs](dmo-guids.md).

Registering a DMO under a category is optional. To do so, call the [**DMORegister**](/previous-versions/windows/desktop/api/Dmoreg/nf-dmoreg-dmoregister) function and specify the friendly name of the DMO, the CLSID, and the category. Optionally, you can also register a set of media types that your DMOs supports. For more information, see [DMO Media Types](dmo-media-types.md).

The following example shows how to register an audio effect DMO that supports PCM audio input and output. In this case the input types and output types are the same.


```C++
STDAPI DllRegisterServer(void)
{
    // Register the DMO as a PCM audio effect DMO
    DMO_PARTIAL_MEDIATYPE mt;
    mt.type    = MEDIATYPE_Audio;
    mt.subtype = MEDIASUBTYPE_PCM;
    HRESULT hr = DMORegister(
        L"MyDMO",                  // Friendly name
        CLSID_MyDMO,               // CLSID
        DMOCATEGORY_AUDIO_EFFECT,  // Category
        0,                         // Flags 
        1,                         // Number of input types
        &mt,                       // Array of input types
        1,                         // Number of output types
        &mt);                      // Array of output types

    if (FAILED(hr)) return hr;

    // Registers the object, with no typelib.
    return _Module.RegisterServer(FALSE);
}
```



This example assumes that ATL was used to create the project; the last line of the function calls the standard ATL method to register the COM server. If you are not using ATL, your function will look different.

**Unregistering a DMO**

Your **DllUnregisterServer** function must remove any registry entries that the **DllRegisterServer** function creates. If you call **DMORegister** when you register the DMO, you must [**DMOUnregister**](/previous-versions/windows/desktop/api/Dmoreg/nf-dmoreg-dmounregister) with the same category when you unregister the DMO.

The following example removes the registry entries created in the previous example:


```C++
STDAPI DllUnregisterServer(void)
{
    DMOUnregister(CLSID_MyDMO, DMOCATEGORY_AUDIO_EFFECT);
    return _Module.UnregisterServer(TRUE);
}
```



**DirectShow Merit Values**

For purposes of building filter graphs, DirectShow assigns a default merit value to DMOs. You can override this value by adding a registry entry to the DMO's registry key in HKEY\_CLASSES\_ROOT\\CLSID. Include a **DWORD** value named `Merit` whose value specifies the merit.

## Related topics

<dl> <dt>

[Writing a DMO](writing-a-dmo.md)
</dt> </dl>

 

 



