---
description: Notifies a Media Foundation transform (MFT) that an input stream has ended.
ms.assetid: 2d6cdf45-1bb4-4915-bd27-efa041089100
title: MFT_MESSAGE_NOTIFY_END_OF_STREAM (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFT\_MESSAGE\_NOTIFY\_END\_OF\_STREAM

Notifies a Media Foundation transform (MFT) that an input stream has ended.

## Message Parameter

The *ulParam* parameter contains the identifier of the input stream, specified as a **DWORD** value. In 64-bit applications, place this value in the lower 32-bits of the **ULONG\_PTR**.

## Remarks

To send this message, call [**IMFTransform::ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage).

The client is not required to send this message.

After a stream ends, the client may call [**ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput) again to send new data for that stream. If so, the client must set the discontinuity attribute ([**MFSampleExtension\_Discontinuity**](mfsampleextension-discontinuity-attribute.md) attribute) on the first input sample after the stream ends. (The client should always set this attribute on the first new sample after a stream ends, regardless of whether the client sent the **MFT\_MESSAGE\_NOTIFY\_END\_OF\_STREAM** message. For more information about handling discontinuities, see [Basic MFT Processing Model](basic-mft-processing-model.md).)

After sending this message for every input stream, the client typically sends an **MFT\_MESSAGE\_COMMAND\_DRAIN** command and then collects the remaining output. However, the client is not required to drain the MFT. If the client does not drain the MFT, the MFT will typically discard any unprocessed data on the next call to [**ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput), when it detects the stream discontinuity. Alternatively, the client might flush the MFT before calling **ProcessInput**.

This message does not remove the input stream or reset the media type.

### Implementation

An MFT is not required to respond to this message.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[**MFT\_MESSAGE\_TYPE**](/windows/desktop/api/mftransform/ne-mftransform-mft_message_type)
</dt> </dl>

 

 




