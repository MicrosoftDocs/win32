---
title: ISoftKbd UnadviseSoftKeyboardEventSink method (Softkbdc.h)
description: The ISoftKbd UnadviseSoftKeyboardEventSink method removes a soft keyboard event sink.
ms.assetid: 785340bd-c4f6-4c80-a492-6e60d1c1d552
keywords:
- UnadviseSoftKeyboardEventSink method Text Services Framework
- UnadviseSoftKeyboardEventSink method Text Services Framework , ISoftKbd interface
- ISoftKbd interface Text Services Framework , UnadviseSoftKeyboardEventSink method
topic_type:
- apiref
api_name:
- ISoftKbd.UnadviseSoftKeyboardEventSink
api_location:
- Softkbd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ISoftKbd::UnadviseSoftKeyboardEventSink method

The **ISoftKbd::UnadviseSoftKeyboardEventSink** method removes a soft keyboard event sink.

## Syntax


```C++
HRESULT UnadviseSoftKeyboardEventSink(
  [in] TfClientId tid
);
```



## Parameters

<dl> <dt>

*tid* \[in\]
</dt> <dd>

Identifier of the client that owns the soft keyboard event sink. This value was passed when the event sink was installed using [ISoftKbd::AdviseSoftKeyboardEventSink](isoftkbd-advisesoftkeyboardeventsink.md).

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                                   | Description                                                   |
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | The method was successful.<br/>                         |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | The *tid* parameter is invalid.<br/>                    |
| <dl> <dt>**CONNECT\_E\_NOCONNECTION**</dt> </dl> | The advise sink identified by *tid* was not found.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                        |
| Header<br/>                   | <dl> <dt>Softkbdc.h</dt> </dl>  |
| IDL<br/>                      | <dl> <dt>Softkbd.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Softkbd.dll</dt> </dl> |



## See also

<dl> <dt>

[**ISoftKbd**](isoftkbd.md)
</dt> <dt>

[ISoftKbd::AdviseSoftKeyboardEventSink](isoftkbd-advisesoftkeyboardeventsink.md)
</dt> </dl>

 

 





