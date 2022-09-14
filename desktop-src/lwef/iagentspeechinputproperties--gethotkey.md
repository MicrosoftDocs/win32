---
title: IAgentSpeechInputProperties GetHotKey
description: IAgentSpeechInputProperties GetHotKey
ms.assetid: b93e5b46-b8f8-4ca4-8417-7626b97d8928
ms.topic: article
ms.date: 05/31/2018
---

# IAgentSpeechInputProperties::GetHotKey

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetHotKey(
BSTR * pbszHotCharKey  // address of variable for listening key 
);                        
```

Retrieves the current keyboard assignment for the speech input Listening key.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbszHotCharKey"></span><span id="pbszhotcharkey"></span><span id="PBSZHOTCHARKEY"></span>*pbszHotCharKey*
</dt> <dd>

Address of a BSTR that receives the current hotkey setting used to open the audio channel for speech input.

</dd> </dl>

If [**GetEnabled**](iagentspeechinputproperties--getenabled.md) returns **False**, querying this setting raises an error.

## See Also

[**IAgentSpeechInputProperties::GetEnabled**](iagentspeechinputproperties--getenabled.md)


 

 




