---
description: The performance DLLs OpenPerformanceData function takes a string argument as input.
ms.assetid: 8ec0ea45-5789-4801-b486-555779a7303e
title: Creating Other Registry Entries
ms.topic: article
ms.date: 05/31/2018
---

# Creating Other Registry Entries

The performance DLL's [**OpenPerformanceData**](/previous-versions/windows/desktop/legacy/aa372200(v=vs.85)) function takes a string argument as input. To provide an input string to your open function, include a **Linkage** key under your **Services** key. The **Linkage** key contains an **Export** value. Set the value data for **Export** to the input string that you want to pass to your open function. The data type of **Export** is **REG\_MULTI\_SZ**.

If **Export** is not defined (**Export** is optional), the system passes **NULL** to your [**OpenPerformanceData**](/previous-versions/windows/desktop/legacy/aa372200(v=vs.85)) function.

Typically, if more than one application shares the same performance DLL, each application includes a **Linkage** key and **Export** value to provide context as to which application is calling the DLL.

The following shows the registry entries:

```
HKEY_LOCAL_MACHINE
   \SYSTEM
      \CurrentControlSet
         \Services
            \application-name-1
               \Linkage
                  Export = app-1 context strings
               \Performance
                  Library = perfctrs.dll
            \application-name-2
               \Linkage
                  Export = app-2 context strings
               \Performance
                  Library = perfctrs.dll
```

By default, the performance DLL's [**OpenPerformanceData**](/previous-versions/windows/desktop/legacy/aa372200(v=vs.85)) and [**CollectPerformanceData**](/windows/win32/api/winperf/nc-winperf-pm_collect_proc) functions must return within 10,000 milliseconds. If not, the system does not use the data that the DLL returns. The application can increase or decrease the timeout value by specifying an **Open Timeout** or **Collect Timeout** registry value under their **Performance** key as shown in the following example.

```
HKEY_LOCAL_MACHINE
   \SYSTEM
      \CurrentControlSet
         \Services
            \application-name
               \Performance
                  Open Timeout = Timeout value for your open function, in milliseconds
                  Collect Timeout = Timeout value for your collect function, in milliseconds
```

To obtain the performance data for some applications (those that return counters using the [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) function), it is necessary to use the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) function to open the device associated with the application. In this case, the name specified in **CreateFile** must also be installed in the DOS Devices node of the registry, as shown here:

```
HKEY_LOCAL_MACHINE
   \SYSTEM
      \CurrentControlSet
         \Control
            \Session Manager
               \DOS Devices
```

 

 
