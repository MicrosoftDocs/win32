---
title: IAgentNotifySink Command
description: IAgentNotifySink Command
ms.assetid: d54fb2e8-27d6-47a4-8a1e-5419a94ea26d
ms.topic: article
ms.date: 05/31/2018
---

# IAgentNotifySink::Command

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Command(
   long dwCommandID,         // Command ID of the best match
   IUnknown * punkUserInput  // address of IAgentUserInput object 
);                          
```

Notifies a client application that a [**Command**](/windows/desktop/lwef/the-command-object) was selected by the user.

-   No return value.

<dl> <dt>

<span id="dwCommandID"></span><span id="dwcommandid"></span><span id="DWCOMMANDID"></span>*dwCommandID*
</dt> <dd>

Identifier of the best match command alternative.

</dd> <dt>

<span id="punkUserInput"></span><span id="punkuserinput"></span><span id="PUNKUSERINPUT"></span>*punkUserInput*
</dt> <dd>

Address of the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface for the [**IAgentUserInput**](iagentuserinput.md) object.

</dd> </dl>

Use [**QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) to retrieve the [**IAgentUserInput**](iagentuserinput.md) interface.

The server notifies the input-active client when the user chooses a command by voice or by selecting a command from the character's pop-up menu. The event occurs even when the user selects one of the server's commands. In this case the server returns a null command ID, the confidence score, and the voice text returned by the speech engine for that entry.

## See Also

[**IAgentUserInput**](iagentuserinput.md)


 

 