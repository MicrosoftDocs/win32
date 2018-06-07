---
title: Text Service Registration
description: In addition to the standard COM in-proc server registry entries, a text service must register itself with the Text Services Framework (TSF) so that it can be available for use with an application.
ms.assetid: 95676067-ab5c-470b-a4be-117ab6810d48
keywords:
- Text Services Framework (TSF),registration
- TSF (Text Services Framework),registration
- text services,registration
- Text Services Framework (TSF),language profiles
- TSF (Text Services Framework),language profiles
- text services,language profiles
- Text Services Framework (TSF),categories
- TSF (Text Services Framework),categories
- text services,categories
- registering text services
- registering language profiles
- registering categories
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Text Service Registration

In addition to the standard COM in-proc server registry entries, a text service must register itself with the Text Services Framework (TSF) so that it can be available for use with an application. TSF supplies the [ITfInputProcessorProfiles](https://msdn.microsoft.com/library/windows/desktop/ms538984) and [ITfCategoryMgr](https://msdn.microsoft.com/library/windows/desktop/ms538500) interface to simplify the registration process.

Text service providers should also provide digital signatures with their binary executables. See [Introduction to Code Signing](https://msdn.microsoft.com/library/ms537361).

## Registering the Text Service

A text service registers itself with TSF by calling [ITfInputProcessorProfiles::Register](https://msdn.microsoft.com/library/windows/desktop/ms628573) with the class identifier of the text service. An instance of the **ITfInputProcessorProfiles** interface is obtained by calling **CoCreateInstance** with CLSID\_TF\_InputProcessorProfiles.

The following example demonstrates how to create an **ITfInputProcessorProfiles** object and register the text service.


```C++
BOOL RegisterTextService(CLSID clsidTextService)
{
    HRESULT hr;
    ITfInputProcessorProfiles *pInputProcessProfiles;

    hr = CoCreateInstance(  CLSID_TF_InputProcessorProfiles, 
                            NULL, 
                            CLSCTX_INPROC_SERVER,
                            IID_ITfInputProcessorProfiles, 
                            (LPVOID*)&amp;pInputProcessProfiles);

    if (hr != S_OK)
    {
        return FALSE;
    }

    hr = pInputProcessProfiles->Register(clsidTextService);

    pInputProcessProfiles->Release();
    
    return (S_OK == hr);
}
```



[ITfInputProcessorProfiles::Unregister](https://msdn.microsoft.com/library/windows/desktop/ms628581)

## Registering Language Profiles

A text service is only available when an application has the focus and the proper language is selected in the language bar. To facilitate this, TSF requires that a text service register itself for all of the languages that it supports. The text service registers its language profiles by calling [ITfInputProcessorProfiles::AddLanguageProfile](https://msdn.microsoft.com/library/windows/desktop/ms628545) with the text service class identifier, that language identifier of the profile, and a text service defined **GUID** that identifies the language profile.

A language profile can be removed by calling [ITfInputProcessorProfiles::RemoveLanguageProfile](https://msdn.microsoft.com/library/windows/desktop/ms628574). **ITfInputProcessorProfiles::Unregister** removes all language profiles for the text service; when a text service is uninstalled, it does require removal of the individual language profiles.

## Registering Categories

A text service must also register the category that the text service applies to. For example, if the text service supplies display attribute information, it must register itself as a display attribute provider by calling [ITfCategoryMgr::RegisterCategory](/windows/desktop/api/Msctf/nf-msctf-itfcategorymgr-registercategory) with the class identifier of the text service for the first parameter, GUID\_TFCAT\_DISPLAYATTRIBUTEPROVIDER for the second parameter and the class identifier of the text service again for the third parameter. The possible categories are listed under [Predefined Category Values](predefined-category-values.md).

Remove previously registered categories by calling [ITfCategoryMgr::UnregisterCategory](/windows/desktop/api/Msctf/nf-msctf-itfcategorymgr-unregistercategory). ITfInputProcessorProfiles::Unregister removes all categories for the text service; when a text service is uninstalled, it must remove the individual categories.

 

 




