---
title: IAgentCharacterEx GetAnimationNames
description: IAgentCharacterEx GetAnimationNames
ms.assetid: d565b258-dc12-422b-a13d-aeec56057f64
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacterEx::GetAnimationNames

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetAnimationNames(
   IUnknown ** punkEnum // address of IUnknown interface
);
```

Retrieves the animation names for a character.

-   Returns **S\_OK** to indicate the operation was successful.

<dl> <dt>

<span id="IUnknown"></span><span id="iunknown"></span><span id="IUNKNOWN"></span>*IUnknown*
</dt> <dd>

The address of the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface for the character's animation collection.

</dd> </dl>

This function enables you to enumerate the names of the animations for a character. Items in the collection have no properties, so individual items cannot be accessed directly. To access the collection, query punkEnum for the IEnumVARIANT interface:


```c++
IEnumVARIANT pEnum;
VARIANT vAnimName;
DWORD dwRetrieved;

hRes = punkEnum->QueryInterface(IID_IEnumVARIANT, (LPVOID *)&pEnum);

if (SUCCEEDED(hRes)) {

    while (TRUE) {

         hRes = pEnum->Next(1, &vAnimName, &dwRetrieved);

         if (hRes != NOERROR)
            break;

         // vAnimName.bstrVal is the animation name

         VariantClear(&vAnimName);
    } 

    pEnum->Release();
}

punkEnum->Release();
```



> [!Note]  
> For ACF characters, the collection returns all the animations that have been defined for the character, adding to the ones that have been retrieved with the [**Get**](https://www.bing.com/search?q=**Get**) method.
