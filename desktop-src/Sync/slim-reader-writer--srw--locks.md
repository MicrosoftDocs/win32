---
Description: Slim reader/writer (SRW) locks enable the threads of a single process to access shared resources; they are optimized for speed and occupy very little memory.
ms.assetid: 2d439b21-291f-4ff0-910a-c1c27e800019
title: Slim Reader/Writer (SRW) Locks
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Slim Reader/Writer (SRW) Locks

Slim reader/writer (SRW) locks enable the threads of a single process to access shared resources; they are optimized for speed and occupy very little memory. Slim reader-writer locks cannot be shared across processes.

Reader threads read data from a shared resource whereas writer threads write data to a shared resource. When multiple threads are reading and writing using a shared resource, exclusive locks such as a critical section or mutex can become a bottleneck if the reader threads run continuously but write operations are rare.

SRW locks provide two modes in which threads can access a shared resource:

-   **Shared mode**, which grants shared read-only access to multiple reader threads, which enables them to read data from the shared resource concurrently. If read operations exceed write operations, this concurrency increases performance and throughput compared to critical sections.
-   **Exclusive mode**, which grants read/write access to one writer thread at a time. When the lock has been acquired in exclusive mode, no other thread can access the shared resource until the writer releases the lock.

A single SRW lock can be acquired in either mode; reader threads can acquire it in shared mode whereas writer threads can acquire it in exclusive mode. There is no guarantee about the order in which threads that request ownership will be granted ownership; SRW locks are neither fair nor FIFO.

An SRW lock is the size of a pointer. The advantage is that it is fast to update the lock state. The disadvantage is that very little state information can be stored, so SRW locks cannot be acquired recursively. In addition, a thread that owns an SRW lock in shared mode cannot upgrade its ownership of the lock to exclusive mode.

The caller must allocate an SRWLOCK structure and initialize it by either calling [**InitializeSRWLock**](/windows/win32/WinBase/nf-synchapi-initializesrwlock?branch=master) (to initialize the structure dynamically) or assign the constant **SRWLOCK\_INIT** to the structure variable (to initialize the structure statically).

The following are the SRW lock functions.



| SRW lock function                                                | Description                                                                                                                                       |
|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AcquireSRWLockExclusive**](/windows/win32/WinBase/nf-synchapi-acquiresrwlockexclusive?branch=master)       | Acquires an SRW lock in exclusive mode.                                                                                                           |
| [**AcquireSRWLockShared**](/windows/win32/WinBase/nf-synchapi-acquiresrwlockshared?branch=master)             | Acquires an SRW lock in shared mode.                                                                                                              |
| [**InitializeSRWLock**](/windows/win32/WinBase/nf-synchapi-initializesrwlock?branch=master)                   | Initialize an SRW lock.                                                                                                                           |
| [**ReleaseSRWLockExclusive**](/windows/win32/WinBase/nf-synchapi-releasesrwlockexclusive?branch=master)       | Releases an SRW lock that was opened in exclusive mode.                                                                                           |
| [**ReleaseSRWLockShared**](/windows/win32/WinBase/nf-synchapi-releasesrwlockshared?branch=master)             | Releases an SRW lock that was opened in shared mode.                                                                                              |
| [**SleepConditionVariableSRW**](/windows/win32/WinBase/nf-synchapi-sleepconditionvariablesrw?branch=master)   | Sleeps on the specified condition variable and releases the specified lock as an atomic operation.                                                |
| [**TryAcquireSRWLockExclusive**](/windows/win32/WinBase/nf-synchapi-tryacquiresrwlockexclusive?branch=master) | Attempts to acquire a slim reader/writer (SRW) lock in exclusive mode. If the call is successful, the calling thread takes ownership of the lock. |
| [**TryAcquireSRWLockShared**](/windows/win32/WinBase/nf-synchapi-tryacquiresrwlockshared?branch=master)       | Attempts to acquire a slim reader/writer (SRW) lock in shared mode. If the call is successful, the calling thread takes ownership of the lock.    |



 

 

 



