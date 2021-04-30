---
description: Condition variables are synchronization primitives that enable threads to wait until a particular condition occurs. Condition variables are user-mode objects that cannot be shared across processes.
ms.assetid: fef9bab0-cd69-4812-869a-b43a10772d86
title: Condition Variables
ms.topic: article
ms.date: 05/31/2018
---

# Condition Variables

Condition variables are synchronization primitives that enable threads to wait until a particular condition occurs. Condition variables are user-mode objects that cannot be shared across processes.

Condition variables enable threads to atomically release a lock and enter the sleeping state. They can be used with critical sections or slim reader/writer (SRW) locks. Condition variables support operations that "wake one" or "wake all" waiting threads. After a thread is woken, it re-acquires the lock it released when the thread entered the sleeping state.

Note that the caller must allocate a **CONDITION\_VARIABLE** structure and initialize it by either calling [**InitializeConditionVariable**](/windows/win32/api/synchapi/nf-synchapi-initializeconditionvariable) (to initialize the structure dynamically) or assign the constant **CONDITION\_VARIABLE\_INIT** to the structure variable (to initialize the structure statically).

**Windows Server 2003 and Windows XP:** Condition variables are not supported.

The following are the condition variable functions.



| Condition variable function                                        | Description                                                                                                    |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**InitializeConditionVariable**](/windows/win32/api/synchapi/nf-synchapi-initializeconditionvariable) | Initializes a condition variable.                                                                              |
| [**SleepConditionVariableCS**](/windows/win32/api/synchapi/nf-synchapi-sleepconditionvariablecs)       | Sleeps on the specified condition variable and releases the specified critical section as an atomic operation. |
| [**SleepConditionVariableSRW**](/windows/win32/api/synchapi/nf-synchapi-sleepconditionvariablesrw)     | Sleeps on the specified condition variable and releases the specified SRW lock as an atomic operation.         |
| [**WakeAllConditionVariable**](/windows/win32/api/synchapi/nf-synchapi-wakeallconditionvariable)       | Wakes all threads waiting on the specified condition variable.                                                 |
| [**WakeConditionVariable**](/windows/win32/api/synchapi/nf-synchapi-wakeconditionvariable)             | Wakes a single thread waiting on the specified condition variable.                                             |



 

The following pseudocode demonstrates the typical usage pattern of condition variables.

``` syntax
CRITICAL_SECTION CritSection;
CONDITION_VARIABLE ConditionVar;

void PerformOperationOnSharedData()
{ 
   EnterCriticalSection(&CritSection);

   // Wait until the predicate is TRUE

   while( TestPredicate() == FALSE )
   {
      SleepConditionVariableCS(&ConditionVar, &CritSection, INFINITE);
   }

   // The data can be changed safely because we own the critical 
   // section and the predicate is TRUE

   ChangeSharedData();

   LeaveCriticalSection(&CritSection);

   // If necessary, signal the condition variable by calling
   // WakeConditionVariable or WakeAllConditionVariable so other
   // threads can wake
}
```

For example, in an implementation of a reader/writer lock, the `TestPredicate` function would verify that the current lock request is compatible with the existing owners. If it is, acquire the lock; otherwise, sleep. For a more detailed example, see [Using Condition Variables](using-condition-variables.md).

Condition variables are subject to spurious wakeups (those not associated with an explicit wake) and stolen wakeups (another thread manages to run before the woken thread). Therefore, you should recheck a predicate (typically in a **while** loop) after a sleep operation returns.

You can wake other threads using [**WakeConditionVariable**](/windows/win32/api/synchapi/nf-synchapi-wakeconditionvariable) or [**WakeAllConditionVariable**](/windows/win32/api/synchapi/nf-synchapi-wakeallconditionvariable) either inside or outside the lock associated with the condition variable. It is usually better to release the lock before waking other threads to reduce the number of context switches.

It is often convenient to use more than one condition variable with the same lock. For example, an implementation of a reader/writer lock might use a single critical section but separate condition variables for readers and writers.

## Related topics

<dl> <dt>

[Using Condition Variables](using-condition-variables.md)
</dt> </dl>

 

 
