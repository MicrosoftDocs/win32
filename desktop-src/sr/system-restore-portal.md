---
title: System Restore
description: Sets system restore points and monitors key system changes from a program to enable a rollback of the system to a previous state. Write automatic recovery code or wmi script to restore system state to a registered restore point.
ms.assetid: 6861eedc-2bd9-49c7-8682-ea557fa29d28
keywords:
- System Restore
- System Restore, start page
ms.topic: article
ms.date: 05/31/2018
---

# System Restore

## Purpose

System Restore automatically monitors and records key system changes on a user's computer. It is designed to reduce support costs and increase customer satisfaction by enabling a user to undo a change that may have caused a problem with the system, or revert to a day when the system was performing optimally.

> [!Note]  
> The following documentation is targeted for developers. If you are an end-user looking for information on how to use System Restore, see [What Is System Restore?](https://windows.microsoft.com/windows/What-is-System-Restore#1TC=windows-7)

 

## Developer audience

The System Restore API is designed for use by C/C++ programmers. A familiarity with Windows Management Instrumentation (WMI) is required to use the scripting interface.

## Run-time requirements

The System Restore API is supported on client operating systems starting with Windows XP. For information about which operating systems are required to use a particular API element, see the Requirements section of its documentation.

## In this section



| Topic                                                | Description                                                                    |
|------------------------------------------------------|--------------------------------------------------------------------------------|
| [Overview](about-system-restore.md)<br/>      | An overview of how System Restore works.<br/>                            |
| [Reference](system-restore-reference.md)<br/> | Documentation of System Restore functions, structures, and classes.<br/> |
| [Samples](using-system-restore.md)<br/>       | A sample program written in C.<br/>                                      |



 

## Related topics

<dl> <dt>

[WMI](/windows/desktop/WmiSdk/wmi-start-page)
</dt> </dl>

 

