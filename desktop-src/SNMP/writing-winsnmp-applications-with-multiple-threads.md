---
title: Writing WinSNMP Applications with Multiple Threads
description: The Microsoft WinSNMP implementation ensures that the WinSNMP operations of one process do not modify the WinSNMP settings of another process.
ms.assetid: 'faa98704-f55f-4450-9f6e-d2bbbc7a50b4'
---

# Writing WinSNMP Applications with Multiple Threads

The Microsoft WinSNMP implementation ensures that the WinSNMP operations of one process do not modify the WinSNMP settings of another process.

A WinSNMP application with multiple threads must ensure that WinSNMP operations that set application-level parameters are thread-safe. The functions that set application-level parameters are [**SnmpSetTranslateMode**](snmpsettranslatemode.md) and [**SnmpSetRetransmitMode**](snmpsetretransmitmode.md). These functions modify settings for the entity and context translation mode and the retransmission mode.

For more information, see [Multiple Threads](https://msdn.microsoft.com/library/windows/desktop/ms684254) and [Thread Security and Access Rights](https://msdn.microsoft.com/library/windows/desktop/ms686769).

 

 




