---
description: Marks a point in the stream. This message applies only to Asynchronous MFTs.
ms.assetid: eae1d066-64af-45e2-b8bb-eddf9147ad8b
title: MFT_MESSAGE_COMMAND_MARKER (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFT\_MESSAGE\_COMMAND\_MARKER

Marks a point in the stream. This message applies only to [Asynchronous MFTs](asynchronous-mfts.md).

## Message Parameter

An arbitrary value. The MFT returns the value to the client in the [METransformMarker](metransformmarker.md) event.

## Remarks

To send this message, call [**IMFTransform::ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage).

The MFT responds to this messageas follows:

1.  The MFT generates as many output samples as it can from the existing input data, sending an [METransformHaveOutput](metransformhaveoutput.md) event for each output sample.
2.  After all of the output is generated, the MFT sends an [METransformMarker](metransformmarker.md) event. This event must be sent after all of the [METransformHaveOutput](metransformhaveoutput.md) events.

The client is not required to send this message, and should send this message only to asynchronous MFTs. A synchronous MFT will not send an [METransformMarker](metransformmarker.md) event in response to this message.

### Implementation

Asynchronous MFTs must respond to this message as described. Synchronous MFTs should ignore this message.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[**MFT\_MESSAGE\_TYPE**](/windows/desktop/api/mftransform/ne-mftransform-mft_message_type)
</dt> </dl>

 

 




