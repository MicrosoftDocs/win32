---
description: The SwitchTerminalToSubStream method sets a terminal to the participant substream.
ms.assetid: 39e1d4b9-2e39-4b36-9a6a-89e41cd59153
title: ITParticipantSubStreamControl::SwitchTerminalToSubStream method (Confpriv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITParticipantSubStreamControl::SwitchTerminalToSubStream method

\[**SwitchTerminalToSubStream** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **SwitchTerminalToSubStream** method sets a terminal to the participant substream.

## Syntax


```C++
HRESULT SwitchTerminalToSubStream(
  [in] ITTerminal  *pITTerminal,
  [in] ITSubStream *pITSubStream
);
```



## Parameters

<dl> <dt>

*pITTerminal* \[in\]
</dt> <dd>

Pointer to [**ITTerminal**](/windows/win32/api/tapi3if/nn-tapi3if-itterminal) interface.

</dd> <dt>

*pITSubStream* \[in\]
</dt> <dd>

Pointer to [**ITSubStream**](/windows/win32/api/tapi3if/nn-tapi3if-itsubstream) interface.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                     | Description                                                                                        |
|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>            | Method succeeded.<br/>                                                                       |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>    | Participant information for the stream could not be accessed.<br/>                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>    | The *pParticipant* or the *pITSubStream* parameter does not point to a valid interface.<br/> |
| <dl> <dt>**TAPI\_E\_NOITEMS**</dt> </dl> | The substream is not ready.<br/>                                                             |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>   | Insufficient memory exists to perform the operation.<br/>                                    |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Confpriv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ITParticipantSubStreamControl**](itparticipantsubstreamcontrol.md)
</dt> <dt>

[**ITParticipant**](itparticipant.md)
</dt> <dt>

[**ITSubStream**](/windows/win32/api/tapi3if/nn-tapi3if-itsubstream)
</dt> <dt>

[**ITTerminal**](/windows/win32/api/tapi3if/nn-tapi3if-itterminal)
</dt> </dl>

 

