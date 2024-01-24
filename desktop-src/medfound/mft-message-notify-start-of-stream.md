---
description: Notifies a Media Foundation transform (MFT) that the first sample is about to be processed.
ms.assetid: 579df695-02c4-4332-b1b4-c7bd9da50c0f
title: MFT_MESSAGE_NOTIFY_START_OF_STREAM (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFT\_MESSAGE\_NOTIFY\_START\_OF\_STREAM

Notifies a Media Foundation transform (MFT) that the first sample is about to be processed.

## Message Parameter

None.

## Remarks

To send this message, call [**IMFTransform::ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage).

For synchronous MFTs, it is optional to send this message.

For asynchronous MFTs, the client must send this message.

### Implementation

A synchronous MFT is not required to respond to the message.

An asynchronous MFT must implement this message, as described in [Asynchronous MFTs](asynchronous-mfts.md).

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

 

 




