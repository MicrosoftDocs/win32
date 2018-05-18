---
Description: 'Requests a Media Foundation transform (MFT) to flush all stored data.'
ms.assetid: 'c799a962-da79-46df-a37f-4016c8c1701e'
title: 'MFT\_MESSAGE\_COMMAND\_FLUSH'
---

# MFT\_MESSAGE\_COMMAND\_FLUSH

Requests a Media Foundation transform (MFT) to flush all stored data.

## Message Parameter

None.

## Remarks

To send this message, call [**IMFTransform::ProcessMessage**](imftransform-processmessage.md).

After this message is sent, the MFT can accept new input samples. The current media types are not invalidated.

### Implementation

All MFTs must implement this message. When it receives this message, the MFT should discard any media samples it is holding.

[Asynchronous MFTs](asynchronous-mfts.md): The MFT does not send another [METransformNeedInput](metransformneedinput.md) event until it receives an [**MFT\_MESSAGE\_NOTIFY\_START\_OF\_STREAM**](mft-message-notify-start-of-stream.md) message from the client.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[**MFT\_MESSAGE\_TYPE**](mft-message-type.md)
</dt> </dl>

 

 




