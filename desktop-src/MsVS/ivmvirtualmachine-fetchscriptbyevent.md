---
title: IVMVirtualMachine FetchScriptByEvent method
description: The FetchScriptByEvent method retrieves the script command line associated with the specified event type.
ms.assetid: d46b553b-d760-4d3c-9b9a-e4c971380566
keywords:
- FetchScriptByEvent method Virtual Server
- FetchScriptByEvent method Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , FetchScriptByEvent method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.FetchScriptByEvent
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

# IVMVirtualMachine::FetchScriptByEvent method

The **FetchScriptByEvent** method retrieves the script command line associated with the specified event type.

## Syntax


```C++
HRESULT FetchScriptByEvent(
  [in]  VMEventType eventType,
  [out] BSTR        *scriptCommandLine
);
```



## Parameters

<dl> <dt>

*eventType* \[in\]
</dt> <dd>

The event type.

</dd> <dt>

*scriptCommandLine* \[out\]
</dt> <dd>

Command line that will be executed when the specified event occurs.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                         | Description                                               |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt> **S\_OK** </dt> </dl>              | The operation was successful.<br/>                  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>        | The *eventType* parameter is not valid.<br/>        |
| <dl> <dt> **E\_POINTER** </dt> </dl>         | The *scriptCommandLine* parameter is **NULL**.<br/> |
| <dl> <dt> **VM\_E\_VM\_UNKNOWN** </dt> </dl> | The configuration is unknown.<br/>                  |
| <dl> <dt> **DISP\_E\_EXCEPTION** </dt> </dl> | An unexpected error has occurred.<br/>              |



 

## Remarks

The output command line string will be **NULL** if there is no command attached to the specified event type. Scripts attached to an event will be launched automatically by Virtual Server when the event occurs.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> <dt>

[**VMEventType**](vmeventtype.md)
</dt> </dl>

 

 





