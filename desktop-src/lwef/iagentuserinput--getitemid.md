---
title: IAgentUserInput GetItemID
description: IAgentUserInput GetItemID
ms.assetid: 3afd4d9d-51bb-4086-bf7b-7c9a2ddcd807
ms.topic: article
ms.date: 05/31/2018
---

# IAgentUserInput::GetItemID

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetItemID(
   long dwItemIndex,    // index of Command alternative
   long * pdwCommandID  // address of a variable for number of alternatives 
);
```

Retrieves the identifier of a [**Command**](command-event.md) alternative passed to an [**IAgentNotifySink::Command**](iagentnotifysink--command.md) callback.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="dwItemIndex"></span><span id="dwitemindex"></span><span id="DWITEMINDEX"></span>*dwItemIndex*
</dt> <dd>

The index of the [**Command**](command-event.md) alternative passed to the [**IAgentNotifySink::Command**](iagentnotifysink--command.md) callback.

</dd> <dt>

<span id="pdwCommandID"></span><span id="pdwcommandid"></span><span id="PDWCOMMANDID"></span>*pdwCommandID*
</dt> <dd>

Address of a variable that receives the ID of a [**Command**](command-event.md).

</dd> </dl>

If voice input triggers the [**IAgentNotifySink::Command**](iagentnotifysink--command.md) callback, the server returns the IDs for any matching [**Commands**](command-event.md) defined by your application.

## See Also

[**IAgentUserInput::GetItemConfidence**](iagentuserinput--getitemconfidence.md), [**IAgentUserInput::GetItemText**](iagentuserinput--getitemtext.md), [**IAgentUserInput::GetAllItemData**](iagentuserinput--getallitemdata.md)


 

 




