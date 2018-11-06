---
Description: You can use the registry functions to collect performance data.
ms.assetid: feac7b8d-1dee-462c-89dc-bec1ba045da2
title: Using the Registry Functions to Consume Counter Data
ms.topic: article
ms.date: 05/31/2018
---

# Using the Registry Functions to Consume Counter Data

You can use the [registry functions](https://msdn.microsoft.com/library/windows/desktop/ms724875) to collect performance data. However, the performance data is not actually stored in the registry database. Instead, calling the registry functions causes the system to collect the data from the appropriate performance counter provider.

> [!Note]  
> You should not use the registry functions to consume counter data. Instead, you should use the Performance Data Helper (PDH) functions to consume counter data. The PDH functions are easier to use, oriented more towards operations on single counters rather than groups of counters, and can be used to access counter data from current activity or log files.

 

To obtain performance data from the local system, call the [**RegQueryValueEx**](https://msdn.microsoft.com/library/windows/desktop/ms724911) function. Use **HKEY\_PERFORMANCE\_DATA** as the key. The first call opens the key; you do not need to explicitly open the key first.

To obtain performance data from a remote system, call the [**RegConnectRegistry**](https://msdn.microsoft.com/library/windows/desktop/ms724840) function. Use the computer name of the remote system and the **HKEY\_PERFORMANCE\_DATA** key. This call retrieves a key representing the performance data for the remote system. Use this key, rather than the **HKEY\_PERFORMANCE\_DATA** key to retrieve the data.

Be sure to use the [**RegCloseKey**](https://msdn.microsoft.com/library/windows/desktop/ms724837) function to close the handle to the key when you are finished obtaining the performance data. Do not call **RegCloseKey(HKEY\_PERFORMANCE\_DATA)** during DLL\_PROCESS\_DETACH.

You use the *lpszValueName* parameter of the [**RegQueryValueEx**](https://msdn.microsoft.com/library/windows/desktop/ms724911) function to indicate the amount of information to retrieve. Retrieving the performance data is expensive in terms of processor and memory requirements. The following table lists the values you can specify for *lpszValueName*. Note that the value strings are case-insensitive. If a string includes more than one word, the words must be separated by a space.



| Value         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Global**    | Retrieves performance data for all performance objects registered on the computer, except for those included in the **Costly** category.                                                                                                                                                                                                                                                                                                                                                    |
| *nnn xxx yyy* | Retrieves performance data for the specified performance objects. Specify the index value associated with the objects that you want to retrieve. For example, if you want to retrieve System and Memory objects, specify "2 4". Note that the query can return more objects than you requested if the specified object depends on another object type. For example, threads depend on processes, so if you specify the Thread object, the query also returns the Process object.<br/> |
| **Costly**    | Retrieves performance data for object types whose data is expensive to collect in terms of processor time or memory usage. You should start a worker thread if your application needs to respond to the user during this lengthy data collection.                                                                                                                                                                                                                                           |



 

For an example that gets the names and descriptions of the registered counters on the computer, see [Retrieving Counter Names and Help Text](retrieving-counter-names-and-explanations.md).

For an example that accesses the components of the performance data, see [Displaying Object, Instance, and Counter Names](displaying-object-instance-and-counter-names.md).

For an example that retrieves, computes, and prints counter values, see [Retrieving Counter Data](retrieving-counter-data.md) and [Calculating Counter Values](calculating-counter-values.md).

For details on the format of the counter data that the registry returns, see [Performance Data Format](performance-data-format.md).

 

 




