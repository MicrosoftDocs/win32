---
description: A group of methods that is used to manipulate locks.
ms.assetid: ba4cc37c-bd2f-446f-8b3d-bc2a2e2e4de4
title: CShareLockNH Methods
ms.topic: reference
ms.date: 05/31/2018
---

# CShareLockNH Methods

A group of methods that is used to manipulate locks.

## Methods

The following are methods exported by Rwnh.dll.



| Method                                                                   | Description                                                     |
|--------------------------------------------------------------------------|-----------------------------------------------------------------|
| [**ExclusiveLock**](csharelocknh--exclusivelock.md)                     | Acquires a reader/writer lock.                                  |
| [**ExclusiveToPartial**](csharelocknh--exclusivetopartial.md)           | Changes the state.                                              |
| [**ExclusiveUnlock**](csharelocknh--exclusiveunlock.md)                 | Releases a lock.                                                |
| [**FirstPartialToExclusive**](csharelocknh--firstpartialtoexclusive.md) | Used in converting a partial lock to an exclusive lock.         |
| [**PartialLock**](csharelocknh--partiallock.md)                         | Prevents more than one thread from completing acquiring a lock. |
| [**PartialUnlock**](csharelocknh--partialunlock.md)                     | Releases a partial lock.                                        |
| [**ShareLock**](csharelocknh--sharelock.md)                             | Obtains a lock for shared mode.                                 |
| [**ShareUnlock**](csharelocknh--shareunlock.md)                         | Releases a lock from shared mode.                               |
| [**SharedToPartial**](csharelocknh--sharedtopartial.md)                 | Obtains a partial lock.                                         |
| [**TryExclusiveLock**](csharelocknh--tryexclusivelock.md)               | Obtains a lock exclusively.                                     |



 

 

 



