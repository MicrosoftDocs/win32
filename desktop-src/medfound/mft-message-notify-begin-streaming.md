---
Description: Notifies a Media Foundation transform (MFT) that streaming is about to begin.
ms.assetid: a7f02e92-a747-4ac6-aa83-60897acb2bc5
title: MFT\_MESSAGE\_NOTIFY\_BEGIN\_STREAMING
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFT\_MESSAGE\_NOTIFY\_BEGIN\_STREAMING

Notifies a Media Foundation transform (MFT) that streaming is about to begin.

## Message Parameter

None.

## Remarks

To send this message, call [**IMFTransform::ProcessMessage**](/windows/win32/mftransform/nf-mftransform-imftransform-processmessage?branch=master).

The client is not required to send this message. If the client sends this message, it must do so after setting all of the media types on the MFT, and before calling [**ProcessInput**](/windows/win32/mftransform/nf-mftransform-imftransform-processinput?branch=master). The MFT can respond by allocating buffers or other resources. If the client does not send this message, the MFT allocates resources on the first call to **ProcessInput**. Therefore, sending this message can reduce the initial latency when streaming begins.

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

[**MFT\_MESSAGE\_TYPE**](/windows/win32/mftransform/ne-mftransform-_mft_message_type?branch=master)
</dt> </dl>

 

 




