---
title: IAgentCharacterEx GetAnimationNames
description: IAgentCharacterEx GetAnimationNames
ms.assetid: d565b258-dc12-422b-a13d-aeec56057f64
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

The address of the [**IUnknown**](lwef-iagentcharacterex__iunknown) interface for the character's animation collection.

</dd> </dl>

This function enables you to enumerate the names of the animations for a character. Items in the collection have no properties, so individual items cannot be accessed directly. To access the collection, query punkEnum for the IEnumVARIANT interface:


```
   IEnumVARIANT pEnum;
   VARIANT vAnimName;
   DWORD dwRetrieved;

   hRes = punkEnum-&amp;gt;QueryInterface(IID_IEnumVARIANT, (LPVOID *)&amp;amp;pEnum);

   if (SUCCEEDED(hRes)) {

      while (TRUE) {

         hRes = pEnum-&amp;gt;Next(1, &amp;amp;vAnimName, &amp;amp;dwRetrieved);

         if (hRes != NOERROR)
            break;

         // vAnimName.bstrVal is the animation name

         VariantClear(&amp;amp;vAnimName);
      } 

      pEnum-&amp;gt;Release();
   }

   punkEnum-&amp;gt;Release();
```



> [!Note]  
> For ACF characters, the collection returns all the animations that have been defined for the character, adding to the ones that have been retrieved with the [**Get**](lwef-iagentcharacterex__get) method.

 

 

 




