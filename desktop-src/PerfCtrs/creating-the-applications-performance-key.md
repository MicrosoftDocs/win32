---
Description: 'An application that supports performance counters must have a Performance key under the Services key. The following example shows the values that you must include for this key.'
ms.assetid: 'b6cdf130-699f-49bd-97b6-a580818b3fab'
title: 'Creating the Application's Performance Key'
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating the Application's Performance Key

An application that supports performance counters must have a **Performance** key under the **Services** key. The following example shows the values that you must include for this key.

```
HKEY_LOCAL_MACHINE
   \SYSTEM
      \CurrentControlSet
         \Services
            \application-name
               \Performance
                  Library = Name of your performance DLL
                  Open = Name of your Open function in your DLL
                  Collect = Name of your Collect function in your DLL
                  Close = Name of your Close function in your DLL
```

The **Library** value provides the name of the performance DLL, and the **Open**, **Collect**, and **Close** values provide the names of the functions exported from the performance DLL. The data type of these values is **REG\_SZ**. When a consumer requests performance data, the system uses these values to determine which performance DLLs to load and which DLL functions to call.

The **Library** value can contain the DLL name or a full path to the DLL. If you use the **REG\_EXPAND\_SZ** data type for **Library**, you can specify environment variables in your path.

The application's service key must exist before you can run **lodctr** to load your counter names and help strings.

For additional registry values that you can create, such as specifying time out values for the [**OpenPerformanceData**](https://msdn.microsoft.com/en-us/library/Aa372200(v=VS.85).aspx) and [**CollectPerformanceData**](https://msdn.microsoft.com/en-us/library/Aa371898(v=VS.85).aspx) functions, see [Creating Other Registry Entries](creating-other-registry-entries.md).

 

 



