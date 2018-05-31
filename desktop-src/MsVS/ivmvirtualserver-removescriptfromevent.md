---
title: IVMVirtualServer RemoveScriptFromEvent method
description: The RemoveScriptFromEvent method detaches a script from an event.
ms.assetid: c23731d3-d8b3-49a9-86d2-3bac70dd138f
keywords:
- RemoveScriptFromEvent method Virtual Server
- RemoveScriptFromEvent method Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , RemoveScriptFromEvent method
topic_type:
- apiref
api_name:
- IVMVirtualServer.RemoveScriptFromEvent
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualServer::RemoveScriptFromEvent method

The **RemoveScriptFromEvent** method detaches a script from an event.

## Syntax


```C++
HRESULT RemoveScriptFromEvent(
  [in] VMEventType eventType
);
```



## Parameters

<dl> <dt>

*eventType* \[in\]
</dt> <dd>

The event type from which the current attached script will be removed.

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                         | Description                                        |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt> **S\_OK** </dt> </dl>              | The operation was successful.<br/>           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>        | The *eventType* parameter is not valid.<br/> |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>   | The configuration is unknown.<br/>           |
| <dl> <dt> **DISP\_E\_EXCEPTION** </dt> </dl> | An unexpected error occurred.<br/>           |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> <dt>

[**VMEventType**](vmeventtype.md)
</dt> </dl>

 

 





