---
Description: To remove your applications performance counters from the system, perform the following steps.
ms.assetid: 40fc9831-1025-4052-a941-70767ee4e10f
title: Deleting Performance Counters
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Deleting Performance Counters

To remove your application's performance counters from the system, perform the following steps.

1.  Use the **unlodctr** tool included with the computer to remove the counter related data from the registry. Note that the application's **Performance** key must exist for the **unlodctr** tool to succeed. For details, see [Removing Counter Names and Descriptions from the Registry](removing-counter-names-and-descriptions-from-the-registry.md).
2.  Delete the **Performance** and **Linkage** keys under the application's **Services** key. To delete these keys, use either the Regedt32.exe utility or call [**RegDeleteKey**](https://msdn.microsoft.com/library/windows/desktop/ms724845).

 

 



