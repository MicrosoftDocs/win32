---
title: IAgentUserInput
description: IAgentUserInput
ms.assetid: 59ce7337-6031-4449-8b29-fd0c6737c3e8
ms.topic: article
ms.date: 05/31/2018
---

# IAgentUserInput

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

When the server notifies the input-active client with [**IAgentNotifySink::Command**](iagentnotifysink--command.md), it returns information through the [**IAgentUserInput**](/windows/desktop/lwef/iagentuserinput) object. **IAgentUserInput** defines an interface that allows applications to query these values.

**Methods in Vtable Order**



| IAgentUserInput Methods                                         | Description                                                                                                                              |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetCount**](iagentuserinput--getcount.md)                   | Returns the number of command alternatives returned in a [**Command**](command-event.md) event.                                         |
| [**GetItemID**](iagentuserinput--getitemid.md)                 | Returns the ID for a specific [**Command**](command-event.md) alternative.                                                              |
| [**GetItemConfidence**](iagentuserinput--getitemconfidence.md) | Returns the value of the [**Confidence**](confidence-property.md) property for a specific [**Command**](command-event.md) alternative. |
| [**GetItemText**](iagentuserinput--getitemtext.md)             | Returns the value of [**Voice**](voice-property.md) text for a specific [**Command**](command-event.md) alternative.                   |
| [**GetAllItemData**](iagentuserinput--getallitemdata.md)       | Returns the data for all [**Command**](command-event.md) alternatives.                                                                  |



 

 

 