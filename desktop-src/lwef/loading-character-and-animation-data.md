---
title: Loading Character and Animation Data
description: Loading Character and Animation Data
ms.assetid: cd674513-fd68-49bb-a43f-12b07adddf3d
ms.topic: article
ms.date: 05/31/2018
---

# Loading Character and Animation Data

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

After you have a pointer to the [**IAgentEx**](iagentex.md) interface, you can use the [**Load**](load-method.md) method to load a character and retrieve its [**IAgentCharacterEx**](iagentcharacterex.md) interface. There are three different possibilities for the Load path of a character. The first is compatible with Microsoft Agent 1.5 where the specified path is the full path and filename of a character file. The second possibility is to specify the filename only, in which case, Agent looks in its Chars directory. The last possibility is to supply an empty Variant parameter that causes the default character to be loaded.


```
   // Create a variant to store the filename of the character to load

   const LPWSTR kpwszCharacter = L"merlin.acs";

   VariantInit(&vPath);

   vPath.vt = VT_BSTR;
   vPath.bstrVal = SysAllocString(kpwszCharacter);

   // Load the character

   hRes = pAgentEx->Load(vPath, &lCharID, &lRequestID);

   // Get its IAgentCharacterEx interface

   hRes = pAgentEx->GetCharacterEx(lCharID, &pCharacterEx);
```



You can use this interface to access the character's methods:


```
   // Show the character.  The first parameter tells Microsoft
   // Agent to show the character by playing an animation.

   hRes = pCharacterEx->Show(FALSE, &lRequestID);

   // Make the character speak

   bszSpeak = SysAllocString(L"Hello World!");

   hRes = pCharacterEx->Speak(bszSpeak, NULL, &lRequestID);

   SysFreeString(bszSpeak);
```



When you no longer need Microsoft Agent services, such as when your client application shuts down, release its interfaces. Note that releasing the character interface does not unload the character. Call the [**Unload**](unload-method.md) method to do this before releasing the [**IAgentEx**](iagentex.md) interface:


```
// Clean up

if (pCharacterEx) {

   // Release the character interface

   pCharacterEx->Release();

   // Unload the character.  NOTE:  releasing the character
   // interface does NOT make the character go away.  You must
   // call Unload.

   pAgentEx->Unload(lCharID);
}
   
// Release the Agent

pAgentEx->Release();

VariantClear(&vPath);
```



 

 




