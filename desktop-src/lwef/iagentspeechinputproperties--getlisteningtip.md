---
title: IAgentSpeechInputProperties GetListeningTip
description: IAgentSpeechInputProperties GetListeningTip
ms.assetid: b0488a54-03f8-43ce-935c-dd49c6ed5dbc
ms.topic: article
ms.date: 05/31/2018
---

# IAgentSpeechInputProperties::GetListeningTip

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetListeningTip(
long * pbListeningTip  // address of variable for listening tip flag
);                       
```

Retrieves a value indicating whether the Listening Tip is enabled for display.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbListeningTip"></span><span id="pblisteningtip"></span><span id="PBLISTENINGTIP"></span>*pbListeningTip*
</dt> <dd>

Address of a variable that receives **True** if the Listening Tip is enabled for display, or **False** if the Listening Tip is disabled.

</dd> </dl>

If [**GetEnabled**](iagentspeechinputproperties--getenabled.md) returns **False**, querying any other speech input properties returns an error.

## See Also

[**IAgentSpeechInputProperties::GetEnabled**](iagentspeechinputproperties--getenabled.md)


 

 




