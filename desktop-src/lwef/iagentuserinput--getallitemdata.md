---
title: IAgentUserInput GetAllItemData
description: IAgentUserInput GetAllItemData
ms.assetid: d1857b28-c745-4ed2-b49e-774f247e7348
ms.topic: article
ms.date: 05/31/2018
---

# IAgentUserInput::GetAllItemData

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetAllItemData(
   VARIANT * pdwItemIndices,  // address of variable for alternative IDs
   VARIANT * plConfidences,   // address of variable for confidence scores
   VARIANT * pbszText         // address of variable for voice text
);
```

Retrieves the data for all [**Command**](command-event.md) alternatives passed to an [**IAgentNotifySink::Command**](iagentnotifysink--command.md) callback.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pdwItemIndices"></span><span id="pdwitemindices"></span><span id="PDWITEMINDICES"></span>*pdwItemIndices*
</dt> <dd>

Address of a variable that receives the IDs of [**Commands**](command-event.md) passed to the [**IAgentNotifySink::Command**](iagentnotifysink--command.md) callback.

</dd> <dt>

<span id="plConfidences"></span><span id="plconfidences"></span><span id="PLCONFIDENCES"></span>*plConfidences*
</dt> <dd>

Address of a variable that receives the confidence scores for [**Command**](command-event.md) alternatives passed to the [**IAgentNotifySink::Command**](iagentnotifysink--command.md) callback.

</dd> <dt>

<span id="pbszText"></span><span id="pbsztext"></span><span id="PBSZTEXT"></span>*pbszText*
</dt> <dd>

Address of a variable that receives the voice text for [**Command**](command-event.md) alternatives passed to the [**IAgentNotifySink::Command**](iagentnotifysink--command.md) callback.

</dd> </dl>

If speech input triggers [**IAgentNotifySink::Command**](iagentnotifysink--command.md), the server returns the best match, the second-best match, and the third-best match, if these are provided by the speech engine. It provides the relative confidence scores, in the range of -100 to 100, and actual text "heard" by the speech engine. If the best match was a server-supplied command, the server sends a NULL ID, but still sends a confidence score and the [**Voice**](voice-property.md) text.

If speech input was not the source for the event; for example, if the user selected the command from the character's pop-up menu, the Microsoft Agent server returns the ID of the [**Command**](command-event.md) selected, with a confidence score of 100 and voice text as NULL. The other alternatives return as NULL with confidence scores of zero (0) and voice text as NULL.

> [!Note]  
> Not all speech recognition engines may return all the values for all the parameters of this event. Check with your engine vendor to determine whether the engine supports the Microsoft Speech API interface for returning alternatives and confidence scores.

 

## See Also

[**IAgentUserInput::GetItemConfidence**](iagentuserinput--getitemconfidence.md), [**IAgentUserInput::GetItemText**](iagentuserinput--getitemtext.md), [**IAgentUserInput::GetItemID**](iagentuserinput--getitemid.md)


 

 




