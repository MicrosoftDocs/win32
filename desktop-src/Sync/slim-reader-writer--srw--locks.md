---
description: Slim reader/writer (SRW) locks enable the threads of a single process to access shared resources; they are optimized for speed and occupy very little memory.
ms.assetid: 2d439b21-291f-4ff0-910a-c1c27e800019
title: Slim Reader/Writer (SRW) Locks
ms.topic: article
ms.date: 05/31/2018
---

# Slim Reader/Writer (SRW) Locks

Slim reader/writer (SRW) locks enable the threads of a single process to access shared resources; they are optimized for speed and occupy very little memory. Slim reader-writer locks cannot be shared across processes.

Reader threads read data from a shared resource whereas writer threads write data to a shared resource. When multiple threads are reading and writing using a shared resource, exclusive locks such as a critical section or mutex can become a bottleneck if the reader threads run continuously but write operations are rare.

SRW locks provide two modes in which threads can access a shared resource:

-   **Shared mode**, which grants shared read-only access to multiple reader threads, which enables them to read data from the shared resource concurrently. If read operations exceed write operations, this concurrency increases performance and throughput compared to critical sections.
    > [!NOTE]
    > Shared mode SRW locks should not be acquired recursively as this can lead to deadlocks when combined with exclusive acquisition.

-   **Exclusive mode**, which grants read/write access to one writer thread at a time. When the lock has been acquired in exclusive mode, no other thread can access the shared resource until the writer releases the lock.
    > [!NOTE]
    > Exclusive mode SRW locks cannot be acquired recursively. If a thread tries to acquire a lock that it already holds, that attempt will fail (for [**TryAcquireSRWLockExclusive**](/windows/win32/api/synchapi/nf-synchapi-tryacquiresrwlockexclusive)) or deadlock (for [**AcquireSRWLockExclusive**](/windows/win32/api/synchapi/nf-synchapi-acquiresrwlockexclusive))

A single SRW lock can be acquired in either mode; reader threads can acquire it in shared mode whereas writer threads can acquire it in exclusive mode. There is no guarantee about the order in which threads that request ownership will be granted ownership; SRW locks are neither fair nor FIFO.

An SRW lock is the size of a pointer. The advantage is that it is fast to update the lock state. The disadvantage is that very little state information can be stored, so SRW locks do not detect incorrect recursive use in shared mode. In addition, a thread that owns an SRW lock in shared mode cannot upgrade its ownership of the lock to exclusive mode.

The caller must allocate an SRWLOCK structure and initialize it by either calling [**InitializeSRWLock**](/windows/win32/api/synchapi/nf-synchapi-initializesrwlock) (to initialize the structure dynamically) or assign the constant **SRWLOCK\_INIT** to the structure variable (to initialize the structure statically).

You can use [Application Verifier](/windows-hardware/drivers/devtest/application-verifier) to find recursive (reentrant) use of SRW locks.

The following are the SRW lock functions.

| SRW lock function                                                | Description                                                                                                                                       |
|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AcquireSRWLockExclusive**](/windows/win32/api/synchapi/nf-synchapi-acquiresrwlockexclusive)       | Acquires an SRW lock in exclusive mode.                                                                                                           |
| [**AcquireSRWLockShared**](/windows/win32/api/synchapi/nf-synchapi-acquiresrwlockshared)             | Acquires an SRW lock in shared mode.                                                                                                              |
| [**InitializeSRWLock**](/windows/win32/api/synchapi/nf-synchapi-initializesrwlock)                   | Initialize an SRW lock.                                                                                                                           |
| [**ReleaseSRWLockExclusive**](/windows/win32/api/synchapi/nf-synchapi-releasesrwlockexclusive)       | Releases an SRW lock that was opened in exclusive mode.                                                                                           |
| [**ReleaseSRWLockShared**](/windows/win32/api/synchapi/nf-synchapi-releasesrwlockshared)             | Releases an SRW lock that was opened in shared mode.                                                                                              |
| [**SleepConditionVariableSRW**](/windows/win32/api/synchapi/nf-synchapi-sleepconditionvariablesrw)   | Sleeps on the specified condition variable and releases the specified lock as an atomic operation.                                                |
| [**TryAcquireSRWLockExclusive**](/windows/win32/api/synchapi/nf-synchapi-tryacquiresrwlockexclusive) | Attempts to acquire a slim reader/writer (SRW) lock in exclusive mode. If the call is successful, the calling thread takes ownership of the lock. |
| [**TryAcquireSRWLockShared**](/windows/win32/api/synchapi/nf-synchapi-tryacquiresrwlockshared)       | Attempts to acquire a slim reader/writer (SRW) lock in shared mode. If the call is successful, the calling thread takes ownership of the lock.    |

 
