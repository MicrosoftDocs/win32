---
title: IAgentSpeechInputProperties
description: IAgentSpeechInputProperties
ms.assetid: 87bfc8c4-473b-4df9-becd-e90db12dae51
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IAgentSpeechInputProperties

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

IAgentSpeechInputProperties provides access to the speech input properties maintained by the server. Most of the properties are read-only for client applications, but the user can change them in the Microsoft Agent property sheet. The Microsoft Agent server returns values only if a compatible speech engine has been installed and is enabled. Querying these properties attempts to start the speech engine.

**Methods in Vtable Order**



| IAgentSpeechInputProperties Methods                                     | Description                                               |
|-------------------------------------------------------------------------|-----------------------------------------------------------|
| [**GetEnabled**](iagentspeechinputproperties--getenabled.md)           | Returns whether the speech recognition engine is enabled. |
| [**GetHotKey**](iagentspeechinputproperties--gethotkey.md)             | Returns the current key assignment of the Listening key.  |
| [**GetListeningTip**](iagentspeechinputproperties--getlisteningtip.md) | Returns whether the Listening Tip is enabled.             |



 

[**GetInstalled**](lwef-getinstalled), [**GetLCID**](lwef-getlcid), [**GetEngine**](lwef-getengine), and [**SetEngine**](lwef-setengine) methods (supported in earlier versions of Microsoft Agent) are still supported for backward compatibility. However, the methods are not stubbed and do not return useful values. Use [**GetSRModeID**](lwef-getsrmodeid) and [**SetSRModeID**](lwef-setsrmodeid) to query and set the speech recognition engine to be used with the character. Keep in mind that the engine must match the character's current language setting.

 

 




