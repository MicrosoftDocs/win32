---
title: IAgentUserInput GetItemText
description: IAgentUserInput GetItemText
ms.assetid: 69653806-c001-4015-bd05-3c261a312ede
ms.topic: article
ms.date: 05/31/2018
---

# IAgentUserInput::GetItemText

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetItemText(
   Long dwItemIndex,  // index of Command alternative
   BSTR * pbszText    // address of voice text for Command 
);
```

Retrieves the voice text for a [**Command**](command-event.md) alternative passed to the [**IAgentNotifySink::Command**](iagentnotifysink--command.md) callback.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="dwItemIndex"></span><span id="dwitemindex"></span><span id="DWITEMINDEX"></span>*dwItemIndex*
</dt> <dd>

The index of a [**Command**](command-event.md) alternative passed to the [**IAgentNotifySink::Command**](iagentnotifysink--command.md) callback.

</dd> <dt>

<span id="pbszText"></span><span id="pbsztext"></span><span id="PBSZTEXT"></span>*pbszText*
</dt> <dd>

Address of a BSTR that receives the value of the voice text for the [**Command**](command-event.md).

</dd> </dl>

If voice input was not the source for the command, for example, if the user selected the command from the character's pop-up menu, the server returns **NULL** for the [**Command**](command-event.md)'s voice text.

## See Also

[**IAgentUserInput::GetItemConfidence**](iagentuserinput--getitemconfidence.md), [**IAgentUserInput::GetItemID**](iagentuserinput--getitemid.md), [**IAgentUserInput::GetAllItemData**](iagentuserinput--getallitemdata.md)


 

 




