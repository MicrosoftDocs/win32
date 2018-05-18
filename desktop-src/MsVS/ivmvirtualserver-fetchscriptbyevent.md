---
title: IVMVirtualServer FetchScriptByEvent method
description: The FetchScriptByEvent method retrieves the script command line associated with the specified event type.
ms.assetid: '8452840d-cc7f-4cec-994c-98fdae9f2170'
keywords: ["FetchScriptByEvent method Virtual Server", "FetchScriptByEvent method Virtual Server , IVMVirtualServer interface", "IVMVirtualServer interface Virtual Server , FetchScriptByEvent method"]
topic_type:
- apiref
api_name:
- IVMVirtualServer.FetchScriptByEvent
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualServer::FetchScriptByEvent method

The **FetchScriptByEvent** method retrieves the script command line associated with the specified event type.

## Syntax


```C++
HRESULT FetchScriptByEvent(
  [in]  VMEventType eventType,
  [out] BSTR        *outCommandLine
);
```



## Parameters

<dl> <dt>

*eventType* \[in\]
</dt> <dd>

The event type.

</dd> <dt>

*outCommandLine* \[out\]
</dt> <dd>

Command line executed when the specified event occurs. Set to **NULL** if no command is attached to the event type specified by the *eventType* parameter.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                        | Description                                             |
|----------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>              | The operation was successful.<br/>                |
| <dl> <dt>**E\_POINTER**</dt> </dl>          | The *outCommandLine* parameter was **NULL**.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | The *event* parameter is not valid.<br/>          |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>  | The configuration is unknown.<br/>                |
| <dl> <dt> **DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error occurred.<br/>                |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> <dt>

[**VMEventType**](vmeventtype.md)
</dt> </dl>

 

 





