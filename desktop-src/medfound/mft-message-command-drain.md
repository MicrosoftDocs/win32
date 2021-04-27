---
description: MFT_MESSAGE_COMMAND_DRAIN - Requests a Media Foundation transform (MFT) to flush all stored data.
ms.assetid: c48f3a88-a007-4f30-ac60-9e5a8c24e1ee
title: MFT_MESSAGE_COMMAND_DRAIN (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFT\_MESSAGE\_COMMAND\_DRAIN

Requests a Media Foundation transform (MFT) to flush all stored data.

## Message Parameter

None.

## Remarks

To send this message, call [**IMFTransform::ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage).

After this message is sent, the specified input stream does not accept input until the MFT processes all data from previous calls to [**IMFTransform::ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput).

The draining process varies slightly between synchronous MFTs and asynchronous MFTs:

**Synchronous MFTs**

1.  After the client sends this message, it calls [**IMFTransform::ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput) in a loop, until **ProcessOutput** returns the error code **MF\_E\_TRANSFORM\_NEED\_MORE\_INPUT**.
2.  As long as the MFT still has data to process, further calls to [**ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput) will fail. The MFT continues to produce output until it uses all stored data. The MFT discards any data that cannot be processed into a complete output sample. (For example, it should drop a partial video frame.)

**Asynchronous MFTs**

1.  The MFT continues to send [METransformHaveOutput](metransformhaveoutput.md) events until it has no more data to process. It does not send [METransformNeedInput](metransformneedinput.md) events during this time.
2.  After the MFT sends the last [METransformHaveOutput](metransformhaveoutput.md) event, it sends an [METransformDrainComplete](metransformdraincomplete.md) event.
3.  After draining is complete, the MFT does not send another [METransformNeedInput](metransformneedinput.md) event until it receives an [**MFT\_MESSAGE\_NOTIFY\_START\_OF\_STREAM**](mft-message-notify-start-of-stream.md) message from the client.

After the client has drained the MFT, the client can send more input data. The first sample after the drain operation must have the discontinuity attribute ([**MFSampleExtension\_Discontinuity**](mfsampleextension-discontinuity-attribute.md) attribute).

> [!Note]  
> Earlier versions of this documentation stated that the *ulParam* event parameter is a member of the [**\_MFT\_DRAIN\_TYPE**](/windows/win32/api/mftransform/ne-mftransform-_mft_drain_type) enumeration. That is not correct. The *ulParam* contains a stream identifier.

 

### Implementation

An asynchronous MFT must always return [METransformDrainComplete](metransformdraincomplete.md) after it has drained.

A synchronous MFT can ignore this message and return S\_OK if the following conditions are true:

-   The MFT never stores more than one input sample at a time.
-   Each input sample produces a single output sample.

Otherwise, a synchronous MFT must implement this message.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[**MFT\_MESSAGE\_TYPE**](/windows/desktop/api/mftransform/ne-mftransform-mft_message_type)
</dt> <dt>

[Asynchronous MFTs](asynchronous-mfts.md)
</dt> </dl>

 

 




