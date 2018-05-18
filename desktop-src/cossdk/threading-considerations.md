---
Description: Threading Considerations
ms.assetid: '4d27f0b3-3e30-4e88-b2b2-d57218da4ffa'
title: Threading Considerations
---

# Threading Considerations

The COM+ queued components recorder is capable of running in the process's multithreaded apartment (MTA) or in a single-threaded apartment (STA). When the recorder is run in the STA, COM+ requires that each apartment containing objects must have a [Message Queuing](_mq_Message_Queuing_MSMQ_Start_Page) queue to handle calls from other processes and apartments within the same process. This means that the thread's work function must have a message loop. When a queued component is instantiated, the interface pointer returned is always a proxy interface pointer rather than a direct interface pointer. The pointer is actually a reference to an instance of the recorder. If this recorder interface reference is passed to another thread, the original thread must still be running the Windows message loop so that the receiving thread can unmarshal the interface. If this is not the case, the receiving thread hangs in a call to [**CoUnmarshalInterface**](https://msdn.microsoft.com/library/windows/desktop/ms693382).

If you are using primitives to synchronize the threads, consider using [**MsgWaitForMultipleObjects**](https://msdn.microsoft.com/library/windows/desktop/ms684242) instead of other synchronization functions. This checks for messages in the queue as well as the state of the synchronization object.

 

 



