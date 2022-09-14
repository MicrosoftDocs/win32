---
description: Server-Side Errors
ms.assetid: ce8ddb52-237c-4d46-a088-9f592afadcd2
title: Server-Side Errors
ms.topic: article
ms.date: 05/31/2018
---

# Server-Side Errors

The listener and player work together to deal with poison messages. If a transaction that is being played back fails, [Message Queuing](/previous-versions/windows/desktop/legacy/ms711472(v=vs.85)) moves the input message back to the input queue. The player aborts the transaction if it receives a failed HRESULT from the server component or if it catches an exception. If the problem persists, the listener could loop continuously in the following pattern:

-   Dequeues the message
-   Instantiates the object
-   Suffers a rollback
-   Puts the message back on the top of the queue

The queued components service handles this failure by using a series of application-specific retry queues. Created when the component is installed, there are seven queues for each application, as follows:

1.  The normal input queue. The name of this queue is the COM+ application name. This is a Message Queuing public queue.

2.  The first retry queue. Messages are moved here if the transaction repeatedly fails when processing messages from the normal input queue. Messages on this queue are processed after one minute. A message can be retried three times on this queue before being moved to the back of the second retry queue. This queue is named *ApplicationName*\_0. This queue is a private Message Queuing queue.

3.  The second retry queue. Messages are moved here if the transaction repeatedly fails when processing messages from the first retry queue. Messages on this queue are processed after two minutes. A message can be retried three times on this queue before being moved to the back of the third retry queue. This queue is named *ApplicationName*\_1. This queue is a private Message Queuing queue.

4.  The third retry queue. Messages are moved here if the transaction repeatedly fails when processing messages from the second retry queue. Messages on this queue are processed after four minutes. A message can be retried three times on this queue before being moved to the back of the fourth retry queue. This queue is named *ApplicationName*\_2. This queue is a private Message Queuing queue.

5.  The fourth retry queue. Messages are moved here if the transaction repeatedly fails when processing messages from the third retry queue. Messages on this queue are processed after eight minutes. A message can be retried three times on this queue before being moved to the fifth retry queue. This queue is named *ApplicationName*\_3. This queue is a private Message Queuing queue.

6.  The fifth retry queue. Messages are moved here if the transaction repeatedly fails when processing messages from the fourth retry queue. Messages on this queue are processed after sixteen minutes. A message can be retried three times on this queue before being moved to the final resting queue. This queue is named *ApplicationName*\_4. This is a private Message Queuing queue.

7.  An application-specific final resting queue. Messages are moved here if the transaction repeatedly aborts when attempted on the fifth retry queue. This queue is named *ApplicationName*\_DeadQueue. This is a private Message Queuing queue. The final resting queue is not serviced by a queue listener. Messages stay here until they are manually moved (perhaps by the queued components message mover utility) or are purged by Message Queuing Explorer.

Messages that are not playable because it is clear that every retry attempt will fail can be moved directly to the application-specific final resting queue without being advanced through all the retry levels.

The player issues a COM+ event to notify interested parties that messages cannot be played. COM+ events are issued in the following situations:

-   When a transaction aborts
-   When a message is moved from one queue to another
-   When a message is deposited onto the final resting queue

Messages can be modified before moving from one queue to another. The COM+ queued components security mechanism allows a message to be moved to retry queues and then reinserted into the application's initial input queue. For more information on queued components security, see [Queued Components Security](queued-components-security.md).

Retry queues are created along with the main application queue when the application is either marked as queued by the Component Services administration tool or by using the COM+ Administrative SDK functions. The queued components service allows for flexibility in the retry mechanism by allowing retry queues to be deleted. For example, if all the retry queues are deleted, a message that persistently aborts will be moved directly from the application queue to the application-specific final resting queue. By removing one or more of the retry queues, the number and length of the retries can be reduced. If queues are removed from the retry sequence, the timing of the remaining queues correspond to the position in the sequence of retry queues. For example, if you remove retry queue *ApplicationName*\_1, *ApplicationName*\_2, and *ApplicationName*\_3, the messages on *ApplicationName*\_4 would be processed as if the queue was the second retry queue.

The retry mechanism is designed to complete a message if at all possible. In some cases, it may not be possible for the message to succeed. For example, a client may be attempting to withdraw money from an account that has insufficient funds. In these circumstances, you can handle the error in a number of ways, including the following:

-   Generate a diagnostic and issue a warning
-   Create a compensating transaction
-   Ignore the problem and dismiss the message

Like client-side persistent failures, the queued components service allows an exception class to be associated with a component. The exception class is associated with the component by using the **Advanced** tab in the component properties page of Component Services administration tool or by using the COM+ Administrative functions. The exception class allows the developer to have control after a message has been retried and before that message is moved to the application-specific final resting queue. For more information on the exception class, see [Persistent Client-Side Failures](persistent-client-side-failures.md).

The following is the sequence of events for server-side exception handling:

1.  The message is moved through the available application-specific retry queues.
2.  The final retry on the last retry queue fails.
3.  The queued components service run-time retrieves the target component from the message and checks for an exception class.
4.  The run-time instantiates the exception class.
5.  The run-time queries [**IPlaybackControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-iplaybackcontrol) on the exception class.
6.  The run-time calls [**IPlaybackControl::FinalServerRetry**](/windows/desktop/api/ComSvcs/nf-comsvcs-iplaybackcontrol-finalserverretry) in the exception class.
7.  The run-time plays back all property and method calls from the message to the exception class.
8.  If steps 4 through 6 do not succeed, the run-time moves the message onto the application-specific final resting queue.

If you need to intervene in the process described above or you need to move a poison message out of its final resting queue, use the message mover utility. For more information on the message mover utility, see [Handling Errors](handling-errors-in-queued-components.md).

## Related topics

<dl> <dt>

[Client-Side Errors](client-side-errors.md)
</dt> <dt>

[Persistent Client-Side Failures](persistent-client-side-failures.md)
</dt> </dl>

 

 



