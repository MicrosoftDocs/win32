---
description: You can use the registry functions to collect performance data.
ms.assetid: feac7b8d-1dee-462c-89dc-bec1ba045da2
title: Using the Registry Functions to Consume Counter Data
ms.topic: article
ms.date: 08/17/2020
---

# Using the Registry Functions to Consume Counter Data

Use the [registry functions](/windows/desktop/SysInfo/registry-functions) to collect performance data from the special `HKEY_PERFORMANCE_DATA` registry key.

Performance data is not actually stored in the registry. Calling the registry functions causes the system to collect the data from the appropriate performance data provider.

> [!Note]
> You should not normally use the registry functions to consume counter data. Instead, you should [use the Performance Data Helper (PDH) functions](using-the-pdh-functions-to-consume-counter-data.md). The PDH functions are easier to use and avoid many performance and reliability problems that can occur through incorrect use of the registry functions.

> [!Note]
> You cannot use the registry functions if you are writing Windows OneCore apps. Instead, use [PerfLib V2 Consumer functions](using-the-perflib-functions-to-consume-counter-data.md).

The registry functions are the low-level API for collecting data from **V1 providers**. The registry functions also support collecting data from **V2 providers** via a translation layer that calls into the [V2 Consumer functions](using-the-perflib-functions-to-consume-counter-data.md).

To obtain performance data from the local system, call the [**RegQueryValueEx**](/windows/win32/api/winreg/nf-winreg-regqueryvalueexw) function. Use `HKEY_PERFORMANCE_DATA` as the key. The first call opens the key. You do not need to explicitly open the key first.

To obtain performance data from a remote system, call the [**RegConnectRegistry**](/windows/desktop/api/winreg/nf-winreg-regconnectregistryw) function. Use the computer name of the remote system and use `HKEY_PERFORMANCE_DATA` as the key. This call retrieves a key representing the performance data for the remote system. Use this key rather than `HKEY_PERFORMANCE_DATA` key to retrieve the data.

Be sure to use the [**RegCloseKey**](/windows/desktop/api/winreg/nf-winreg-regclosekey) function to close the handle to the key when you are finished obtaining the performance data. This is important for both the local and remote cases:

- `RegCloseKey(HKEY_PERFORMANCE_DATA)` does not actually close a registry handle, but it clears all cached data and frees the loaded performance DLLs.
- `RegCloseKey(hkeyRemotePerformanceData)` closes the handle to the remote machine's registry.

> [!IMPORTANT]
> Do not call `RegCloseKey(HKEY_PERFORMANCE_DATA)` during `DLL_PROCESS_DETACH`.

You use the `lpValueName` parameter of the [**RegQueryValueEx**](/windows/desktop/api/winreg/nf-winreg-regqueryvalueexa) function to indicate the information to retrieve. The following table lists the values you can specify for `lpValueName`. Note that the value strings are not case-sensitive.

|Value|Description
|-----|-----------
|`Global`| Retrieves performance data for all performance objects registered on the computer except for those included in the `Costly` category.
|`OLD_Global`| **Windows Vista and later:** Retrieves performance data for all **V1** performance objects registered on the computer except for those included in the `Costly` category. Use this instead of `Global` to avoid collecting unnecessary V2 provider data when you know that the data of interest comes from a V1 provider.
|`n1 n2 ...`| Retrieves performance data for one or more performance objects. Specify the decimal index associated with each object that you want to retrieve in a space-separated list. For example, if you want to retrieve System and Memory objects and you have determined that the indexes of the corresponding name strings are 2 and 4, specify the string `"2 4"`. Note that the query can return a different number of objects than you requested. This can happen if the specified object is unavailable, if the specified object depends on another object type, or if a provider otherwise returns data that was not directly requested. For example, threads depend on processes, so if you request data from the `Thread` object, the results will include data from the `Process` object.
|`Counter n`| Retrieves name strings for the specified language identifier, e.g. English for `Counter 9`. Use the returned name strings to find the index corresponding to a given name or to find the name corresponding to a given index. See [Retrieving Counter Names and Help Text](retrieving-counter-names-and-help-text.md) for details. Note that the returned list includes both object (counterset) names and counter names -- there is no simple way to determine whether a name is an object name or a counter name.
|`Help n`| Retrieves help strings for the specified language identifier, e.g. English for `Help 9`. Use the returned help strings to find descriptions corresponding to object (counterset) or counter help indexes. See [Retrieving Counter Names and Help Text](retrieving-counter-names-and-help-text.md) for details.
|`Costly`| **Deprecated:** Retrieves performance data for object types whose data is expensive to collect in terms of processor time or memory usage. This collection may take several minutes on a heavily-loaded machine. You should perform the collection on a worker thread if your application needs to respond to the user during this data collection.

For details on the format of the performance data that the registry returns, see [Performance Data Format](performance-data-format.md).

For an example that gets the names and descriptions of the registered counters on the computer, see [Retrieving Counter Names and Help Text](retrieving-counter-names-and-help-text.md).

For an example that accesses the components of the performance data, see [Displaying Object, Instance, and Counter Names](displaying-object-instance-and-counter-names.md).

For an example that retrieves, computes, and prints counter values, see [Retrieving Counter Data](retrieving-counter-data.md) and [Calculating Counter Values](calculating-counter-values.md).
