---
title: ISoftKbd AdviseSoftKeyboardEventSink method (Softkbdc.h)
description: The ISoftKbd AdviseSoftKeyboardEventSink method installs a soft keyboard event sink to handle OnKeySelection notifications from the soft keyboard.
ms.assetid: f7a441dc-7bef-4fc0-bc62-c153a55a844c
keywords:
- AdviseSoftKeyboardEventSink method Text Services Framework
- AdviseSoftKeyboardEventSink method Text Services Framework , ISoftKbd interface
- ISoftKbd interface Text Services Framework , AdviseSoftKeyboardEventSink method
topic_type:
- apiref
api_name:
- ISoftKbd.AdviseSoftKeyboardEventSink
api_location:
- Softkbd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ISoftKbd::AdviseSoftKeyboardEventSink method

The **ISoftKbd::AdviseSoftKeyboardEventSink** method installs a soft keyboard event sink to handle OnKeySelection notifications from the soft keyboard.

## Syntax


```C++
HRESULT AdviseSoftKeyboardEventSink(
  [in]  DWORD    dwKeyboardId,
  [in]  REFIID   riid,
  [in]  IUnknown *punk,
  [out] DWORD    *pdwCookie
);
```



## Parameters

<dl> <dt>

*dwKeyboardId* \[in\]
</dt> <dd>

Identifier of the soft keyboard.

</dd> <dt>

*riid* \[in\]
</dt> <dd>

Interface identifier for the sink interface.

</dd> <dt>

*punk* \[in\]
</dt> <dd>

Pointer to [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) for the sink interface specified by *riid*. This parameter cannot be set to **NULL**.

</dd> <dt>

*pdwCookie* \[out\]
</dt> <dd>

Pointer to the buffer in which this method retrieves the soft keyboard "cookie" used for connection to the client. The cookie must be unique for each connection.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                        | Description                                    |
|----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method was successful.<br/>          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | One or more parameters are invalid.<br/> |



 

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

[**ISoftKbd::UnadviseSoftKeyboardEventSink**](isoftkbd-unadvisesoftkeyboardeventsink.md)
</dt> </dl>

 

