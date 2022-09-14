---
title: IAgentNotifySink Bookmark
description: IAgentNotifySink Bookmark
ms.assetid: 172042af-a524-4ea4-955d-4e3dee079344
ms.topic: article
ms.date: 05/31/2018
---

# IAgentNotifySink::Bookmark

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Bookmark(
   long dwBookMarkID  // bookmark ID
);                          
```

Notifies a client application when its bookmark completes.

-   No return value.

<dl> <dt>

<span id="dwBookMarkID"></span><span id="dwbookmarkid"></span><span id="DWBOOKMARKID"></span>*dwBookMarkID*
</dt> <dd>

Identifier of the bookmark that resulted in triggering the event.

</dd> </dl>

When you include bookmark tags in a [**Speak**](speak-method.md) method, you can track when they occur with this event.

## See Also

[**IAgentCharacter::Speak**](iagentcharacter--speak.md), [Microsoft Agent Speech Output Tags](microsoft-agent-speech-output-tags.md)


 

 




