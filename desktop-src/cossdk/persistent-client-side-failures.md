---
description: Persistent Client-Side Failures
ms.assetid: f991db71-8319-414d-8a25-2d02bc7c8b51
title: Persistent Client-Side Failures
ms.topic: article
ms.date: 05/31/2018
---

# Persistent Client-Side Failures

In some cases, [Message Queuing](/previous-versions/windows/desktop/legacy/ms711472(v=vs.85)) can move a message to the destination queue. For example, if the queue access controls do not permit the message to be moved from client to server, the offending message is moved to the client-side dead letter queue. When this occurs, the COM+ queued components service allows an exception class to be associated with a component. To associate the exception class with the component, use the **Advanced** tab in the component properties page of the Component Services administration tool. You can also associate the exception class programmatically, by using the ExceptionClass catalog component attribute of the COM+ Administrative functions.

The exception class is defined as either the ProgID or the CLSID of a component implementing [**IPlaybackControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-iplaybackcontrol). The queued components service has a dead letter queue monitor that scans the Xact dead letter queue. If there is a message on the queue, the dead letter queue monitor instantiates the exception handler associated with the target component and calls [**IPlaybackControl::FinalClientRetry**](/windows/desktop/api/ComSvcs/nf-comsvcs-iplaybackcontrol-finalclientretry), indicating that there has been a client-side, unrecoverable error.

In addition to [**IPlaybackControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-iplaybackcontrol), the exception handler should implement the same set of interfaces as the server component for which it is handling exceptions. When [**IPlaybackControl::FinalClientRetry**](/windows/desktop/api/ComSvcs/nf-comsvcs-iplaybackcontrol-finalclientretry) is called, the queued components run-time plays back the failing message to the exception handler. This allows the exception handler to implement an alternative behavior for messages that cannot be moved to the server—for example, by generating a compensating transaction.

If the exception handler completes all the method calls played back, the message is removed from the Xact dead letter queue and is dismissed. If, however, the exception handler aborts the message by returning a failure status from one of the method calls, the message is returned to the Xact dead letter queue. The following sequence of events shows how client-side exceptions are handled:

1.  Message Queuing fails to deliver a message to the server and puts the message onto the Xact dead letter queue.
2.  The dead letter queue listener (DLQL) finds a message on the Xact dead letter queue.
3.  The DLQL retrieves the target component CLSID from the message and checks for an exception class.
4.  The DLQL instantiates the exception class.
5.  The DLQL queries for [**IPlaybackControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-iplaybackcontrol) for the exception class.
6.  The DLQL calls the [**IPlaybackControl::FinalClientRetry**](/windows/desktop/api/ComSvcs/nf-comsvcs-iplaybackcontrol-finalclientretry) method in the exception class.
7.  The DLQL plays back all property and method calls from the message to the exception class.
8.  The DLQL deletes the message if the exception handler completes the transaction successfully. The exception handler may issue [**IObjectContext::SetAbort**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setabort), and the message will remain on the dead letter queue.

If any of the preceding steps fail, the message is left on the Xact dead letter queue.

When started, the DLQL reads each message on the Message Queuing transactional dead letter queue and instantiates the exception class for each queued components message. After one pass through the queue, it waits for new messages. It then processes each new dead letter queue message as it arrives.

If you need to intervene in the process described here or if you need to move a poison message out of its final resting queue, use the message mover utility. For more information on the message mover utility, see [Handling Errors](handling-errors-in-queued-components.md).

## Related topics

<dl> <dt>

[Client-Side Errors](client-side-errors.md)
</dt> <dt>

[Server-Side Errors](server-side-errors.md)
</dt> </dl>

 

 



