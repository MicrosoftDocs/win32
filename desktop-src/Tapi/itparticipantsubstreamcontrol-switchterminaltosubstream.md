---
Description: The SwitchTerminalToSubStream method sets a terminal to the participant substream.
ms.assetid: 39e1d4b9-2e39-4b36-9a6a-89e41cd59153
title: ITParticipantSubStreamControl::SwitchTerminalToSubStream method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ITParticipantSubStreamControl::SwitchTerminalToSubStream method

\[**SwitchTerminalToSubStream** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **SwitchTerminalToSubStream** method sets a terminal to the participant substream.

## Syntax


```C++
);
```



## Parameters

<dl> <dt>

*pITTerminal* \[in\]
</dt> <dd>

Pointer to [**ITTerminal**](https://msdn.microsoft.com/en-us/library/ms732646(v=VS.85).aspx) interface.

</dd> <dt>

*pITSubStream* \[in\]
</dt> <dd>

Pointer to [**ITSubStream**](https://msdn.microsoft.com/en-us/library/ms732440(v=VS.85).aspx) interface.

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



|                         |                                                                                       |
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

[**ITSubStream**](https://msdn.microsoft.com/en-us/library/ms732440(v=VS.85).aspx)
</dt> <dt>

[**ITTerminal**](https://msdn.microsoft.com/en-us/library/ms732646(v=VS.85).aspx)
</dt> </dl>

 

 




