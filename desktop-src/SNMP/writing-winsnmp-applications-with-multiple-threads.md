---
title: Writing WinSNMP Applications with Multiple Threads
description: The Microsoft WinSNMP implementation ensures that the WinSNMP operations of one process do not modify the WinSNMP settings of another process.
ms.assetid: faa98704-f55f-4450-9f6e-d2bbbc7a50b4
ms.topic: article
ms.date: 05/31/2018
---

# Writing WinSNMP Applications with Multiple Threads

The Microsoft WinSNMP implementation ensures that the WinSNMP operations of one process do not modify the WinSNMP settings of another process.

A WinSNMP application with multiple threads must ensure that WinSNMP operations that set application-level parameters are thread-safe. The functions that set application-level parameters are [**SnmpSetTranslateMode**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsettranslatemode) and [**SnmpSetRetransmitMode**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetretransmitmode). These functions modify settings for the entity and context translation mode and the retransmission mode.

For more information, see [Multiple Threads](/windows/desktop/ProcThread/multiple-threads) and [Thread Security and Access Rights](/windows/desktop/ProcThread/thread-security-and-access-rights).

 

 