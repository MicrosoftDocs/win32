---
title: IVMVirtualMachine AttachScriptToEvent method
description: The AttachScriptToEvent method specifies a script to run when an event occurs.
ms.assetid: '8663440c-35cc-4d77-a499-afb879227118'
keywords: ["AttachScriptToEvent method Virtual Server", "AttachScriptToEvent method Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , AttachScriptToEvent method"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.AttachScriptToEvent
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::AttachScriptToEvent method

The **AttachScriptToEvent** method specifies a script to run when an event occurs.

## Syntax


```C++
HRESULT AttachScriptToEvent(
  [in] VMEventType eventType,
  [in] BSTR        scriptCommandLine
);
```



## Parameters

<dl> <dt>

*eventType* \[in\]
</dt> <dd>

The event type.

</dd> <dt>

*scriptCommandLine* \[in\]
</dt> <dd>

Command line that will be executed when the specified event occurs.

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                                                 | Description                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>                                       | The operation was successful.<br/>                                                      |
| <dl> <dt> **E\_INVALIDARG**</dt> </dl>                               | The *scriptCommandLine* parameter is **NULL** or empty, or *eventType* is invalid.<br/> |
| <dl> <dt> **VM\_E\_VM\_UNKNOWN**</dt> </dl>                          | The configuration is unknown.<br/>                                                      |
| <dl> <dt> **VM\_E\_SCRIPT\_ALREADY\_ATTACHED\_TO\_EVENT**</dt> </dl> | A script is already attached to this event.<br/>                                        |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl>                          | An unexpected error has occurred.<br/>                                                  |



 

## Remarks

Scripts attached to an event will be launched automatically by Virtual Server when the event occurs.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> <dt>

[**VMEventType**](vmeventtype.md)
</dt> </dl>

 

 





