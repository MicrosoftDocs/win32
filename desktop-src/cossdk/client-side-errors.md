---
description: Client-Side Errors
ms.assetid: 95fb2ef1-eec2-4c74-891a-617450098160
title: Client-Side Errors
ms.topic: article
ms.date: 05/31/2018
---

# Client-Side Errors

Client-side failures are handled in a way that is similar to server-side failures. [Message Queuing](/previous-versions/windows/desktop/legacy/ms711472(v=vs.85)) can move a message to its destination queue if, for example, the message cannot be moved from client to server. In this case, the message is moved to the client-side dead letter queue.

The COM+ queued components service monitors the dead letter queue. If messages have been moved, the queued components service creates an instance of the exception class and calls [**QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) to request [**IPlaybackControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-iplaybackcontrol). If this is successful, the dead letter queue monitor invokes [**IPlaybackControl::FinalClientRetry**](/windows/desktop/api/ComSvcs/nf-comsvcs-iplaybackcontrol-finalclientretry).

The object can take some action to reverse the effect of a prior transaction. If the playback commits, the message is removed from the Xact dead letter queue. If the playback fails or the required CLSID and interface are not available, the message remains on the Xact dead letter queue.

If you need to intervene in the process described above or if you need to move a poison message out of its final resting queue, use the message mover utility. For more information on the message mover utility, see [Handling Errors](handling-errors-in-queued-components.md).

## Related topics

<dl> <dt>

[Persistent Client-Side Failures](persistent-client-side-failures.md)
</dt> <dt>

[Server-Side Errors](server-side-errors.md)
</dt> </dl>

 

 
