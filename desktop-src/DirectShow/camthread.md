---
description: The CAMThread class is an abstract class for managing worker threads.
ms.assetid: c217d879-0203-4566-96ad-7463b05bc990
title: CAMThread class (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMThread
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMThread class

The `CAMThread` class is an abstract class for managing worker threads.



| Protected Member Variables                                 | Description                                                                  |
|------------------------------------------------------------|------------------------------------------------------------------------------|
| [**m\_hThread**](camthread-m-hthread.md)                  | Handle to the thread.                                                        |
| Public Member Variables                                    | Description                                                                  |
| [**m\_AccessLock**](camthread-m-accesslock.md)            | Critical section that locks the thread from being accessed by other threads. |
| [**m\_WorkerLock**](camthread-m-workerlock.md)            | Critical section that locks data shared among threads.                       |
| Public Methods                                             | Description                                                                  |
| [**CAMThread**](camthread-camthread.md)                   | Constructor method.                                                          |
| [**~ CAMThread**](camthread--camthread.md)                | Destructor method. Virtual.                                                  |
| [**InitialThreadProc**](camthread-initialthreadproc.md)   | Calls the ThreadProc method when the thread is created.                      |
| [**Create**](camthread-create.md)                         | Creates the thread.                                                          |
| [**CallWorker**](camthread-callworker.md)                 | Signals the thread with a request.                                           |
| [**Close**](camthread-close.md)                           | Waits for the thread to exit, then releases its resources.                   |
| [**ThreadExists**](camthread-threadexists.md)             | Queries whether the thread exists.                                           |
| [**GetRequest**](camthread-getrequest.md)                 | Waits for the next request.                                                  |
| [**CheckRequest**](camthread-checkrequest.md)             | Checks if there is a request, without blocking.                              |
| [**Reply**](camthread-reply.md)                           | Replies to a request.                                                        |
| [**GetRequestHandle**](camthread-getrequesthandle.md)     | Retrieves a handle to the event signaled by the CallWorker method.           |
| [**GetRequestParam**](camthread-getrequestparam.md)       | Retrieves the latest request.                                                |
| [**CoInitializeHelper**](camthread-coinitializehelper.md) | Calls CoInitializeEx at the start of the thread.                             |
| Pure Virtual Methods                                       | Description                                                                  |
| [**ThreadProc**](camthread-threadproc.md)                 | Thread procedure.                                                            |



 

## Remarks

This class provides methods for creating a worker thread, passing requests to the thread, and waiting for the thread to exit. To use this class, do the following:

-   Derive a class from `CAMThread` and override the pure virtual method [**CAMThread::ThreadProc**](camthread-threadproc.md). This method is the thread procedure that gets called at the start of the thread.
-   In your application, create an instance of your derived class. Creating the object does not create the thread. To create the thread, call the [**CAMThread::Create**](camthread-create.md) method.
-   To send requests to the thread, call the [**CAMThread::CallWorker**](camthread-callworker.md) method. This method takes a DWORD parameter, whose meaning is defined by your class. The method blocks until the thread responds (see below).
-   In your thread procedure, respond to requests by calling either [**CAMThread::GetRequest**](camthread-getrequest.md) or [**CAMThread::CheckRequest**](camthread-checkrequest.md). The GetRequest method blocks until another thread calls CallWorker. The CheckRequest method is non-blocking, which enables the thread to check for new requests while working asynchronously.
-   When the thread receives a request, call [**CAMThread::Reply**](camthread-reply.md) to unblock the calling thread. The Reply method takes a DWORD parameter, which is passed to the calling thread as the return value for CallWorker.

When you are done with the thread, call the [**CAMThread::Close**](camthread-close.md) method. This method waits for the thread to exit, and then closes the thread handle. Your ThreadProc message must be guaranteed to exit, either on its own or in response to a CallWorker request. The destructor method also calls Close.

The following example illustrates these steps:


```C++
class MyThread : public CAMThread
{
protected:
    DWORD ThreadProc(void);
};

DWORD MyThread::ThreadProc()
{
    BOOL bShutDown = FALSE;
    while (!bShutDown)
    {
        DWORD req = GetRequest();
        printf("Request: %d\n", req);
        bShutDown = (req == 0);
        Reply(bShutDown ? S_FALSE : S_OK);
    }
    printf("Quitting Thread\n");
    return 1;
}

void main()
{
    MyThread thread;
    DWORD reply;
    
    thread.Create();
    reply = thread.CallWorker(3);
    reply = thread.CallWorker(0); // Thread exits.
}
```



In your derived class, you can also define member functions that validate the parameters to CallWorker. The following example shows a typical way to do this:


```C++
enum Command {CMD_INIT, CMD_RUN, CMD_STOP, CMD_EXIT};

HRESULT Init(void)  { return CallWorker(CMD_INIT); }
HRESULT Run(void)   { return CallWorker(CMD_RUN); }
HRESULT Stop(void)  { return CallWorker(CMD_STOP); }
HRESULT Exit(void)  { return CallWorker(CMD_EXIT); }
```



The `CAMThread` class provides two critical sections as public member variables. Use `CAMThread::m_AccessLock` to lock the thread from being accessed by other threads. (For example, the Create and CallWorker methods hold this lock, to serialize operations on the thread.) Use [**CAMThread::m\_WorkerLock**](camthread-m-workerlock.md) to lock data that is shared among threads.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




