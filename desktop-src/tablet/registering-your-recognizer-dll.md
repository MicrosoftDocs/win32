---
description: Your recognizer DLL must be registered for the Tablet PC Platform to use it. The recognizer must make the following changes to the registry at installation.
ms.assetid: 1f1d826b-3968-424b-8da8-b69590058ff1
title: Registering Your Recognizer DLL
ms.topic: article
ms.date: 05/31/2018
---

# Registering Your Recognizer DLL

Your recognizer DLL must be registered for the Tablet PC Platform to use it. The recognizer must make the following changes to the registry at installation.

Add a new key for each of the CLSIDs of your recognizer under the HKEY\_LOCAL\_MACHINE/SOFTWARE/Microsoft/TPG/Recognizers/ registry key. Add one CLSID per language. The following table describes the values that should be added underneath each of the keys containing your CLSIDs.

> [!Note]  
> The names of these values are case sensitive.

 



| Value name                             | Value type             | Value description                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Recognizer Capability Flags<br/> | REG\_DWORD<br/>  | DWORD used to determine the capabilities of the recognizer.<br/>                                                                                                                                                                                                                                                                                                                             |
| Recognizer DLL<br/>              | REG\_SZ<br/>     | Full path to the installed recognizer DLL.<br/>                                                                                                                                                                                                                                                                                                                                              |
| Recognized Languages<br/>        | REG\_BINARY<br/> | Binary array describing the language or languages that a recognizer is designed to work with.<br/> In rectypes.h, the MAX\_LANGUAGES define specifies the maximum number of languages supported by a recognizer, and each language takes a WORD to store in the "Recognized Languages" item. The size of the REG\_BINARY registry entry should be MAX\_LANGUAGES \* sizeof(WORD).<br/> |



 

 

 




