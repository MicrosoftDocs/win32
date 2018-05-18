---
Description: 'Notifies a Media Foundation transform (MFT) that streaming is about to begin.'
ms.assetid: 'a7f02e92-a747-4ac6-aa83-60897acb2bc5'
title: 'MFT\_MESSAGE\_NOTIFY\_BEGIN\_STREAMING'
---

# MFT\_MESSAGE\_NOTIFY\_BEGIN\_STREAMING

Notifies a Media Foundation transform (MFT) that streaming is about to begin.

## Message Parameter

None.

## Remarks

To send this message, call [**IMFTransform::ProcessMessage**](imftransform-processmessage.md).

The client is not required to send this message. If the client sends this message, it must do so after setting all of the media types on the MFT, and before calling [**ProcessInput**](imftransform-processinput.md). The MFT can respond by allocating buffers or other resources. If the client does not send this message, the MFT allocates resources on the first call to **ProcessInput**. Therefore, sending this message can reduce the initial latency when streaming begins.

### Implementation

An MFT is not required to respond to this message.

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

 

 




