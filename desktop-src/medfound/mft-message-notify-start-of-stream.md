---
Description: Notifies a Media Foundation transform (MFT) that the first sample is about to be processed.
ms.assetid: 579df695-02c4-4332-b1b4-c7bd9da50c0f
title: MFT\_MESSAGE\_NOTIFY\_START\_OF\_STREAM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFT\_MESSAGE\_NOTIFY\_START\_OF\_STREAM

Notifies a Media Foundation transform (MFT) that the first sample is about to be processed.

## Message Parameter

None.

## Remarks

To send this message, call [**IMFTransform::ProcessMessage**](/windows/win32/mftransform/nf-mftransform-imftransform-processmessage?branch=master).

For synchronous MFTs, it is optional to send this message.

For asynchronous MFTs, the client must send this message.

### Implementation

A synchronous MFT is not required to respond to the message.

An asynchronous MFT must implement this message, as described in [Asynchronous MFTs](asynchronous-mfts.md).

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[**MFT\_MESSAGE\_TYPE**](/windows/win32/mftransform/ne-mftransform-_mft_message_type?branch=master)
</dt> </dl>

 

 




