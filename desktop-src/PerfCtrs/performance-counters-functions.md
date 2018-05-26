---
Description: Use the following functions to consume and provide performance data.
ms.assetid: a2c97b8b-b1b1-4dd8-8f23-edffaa74d028
title: Performance Counters Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Performance Counters Functions

Use the following functions to consume and provide performance data.

## Consumer functions

Use the following Performance Data Helper abstraction-layer functions to consume performance data from both version 1 and version 2 performance counters:

-   [**CounterPathCallBack**](/windows/win32/Pdh/nc-pdh-counterpathcallback?branch=master)
-   [**PdhAddCounter**](/windows/win32/Pdh/nf-pdh-pdhaddcountera?branch=master)
-   [**PdhAddEnglishCounter**](/windows/win32/Pdh/nf-pdh-pdhaddenglishcountera?branch=master)
-   [**PdhBindInputDataSource**](/windows/win32/Pdh/nf-pdh-pdhbindinputdatasourcea?branch=master)
-   [**PdhBrowseCounters**](/windows/win32/Pdh/nf-pdh-pdhbrowsecountersa?branch=master)
-   [**PdhBrowseCountersH**](/windows/win32/Pdh/nf-pdh-pdhbrowsecountersha?branch=master)
-   [**PdhCalculateCounterFromRawValue**](/windows/win32/Pdh/nf-pdh-pdhcalculatecounterfromrawvalue?branch=master)
-   [**PdhCloseLog**](/windows/win32/Pdh/nf-pdh-pdhcloselog?branch=master)
-   [**PdhCloseQuery**](/windows/win32/Pdh/nf-pdh-pdhclosequery?branch=master)
-   [**PdhCollectQueryData**](/windows/win32/Pdh/nf-pdh-pdhcollectquerydata?branch=master)
-   [**PdhCollectQueryDataEx**](/windows/win32/Pdh/nf-pdh-pdhcollectquerydataex?branch=master)
-   [**PdhCollectQueryDataWithTime**](/windows/win32/Pdh/nf-pdh-pdhcollectquerydatawithtime?branch=master)
-   [**PdhComputeCounterStatistics**](/windows/win32/Pdh/nf-pdh-pdhcomputecounterstatistics?branch=master)
-   [**PdhConnectMachine**](/windows/win32/Pdh/nf-pdh-pdhconnectmachinea?branch=master)
-   [**PdhEnumLogSetNames**](/windows/win32/Pdh/nf-pdh-pdhenumlogsetnamesa?branch=master)
-   [**PdhEnumMachines**](/windows/win32/Pdh/nf-pdh-pdhenummachinesa?branch=master)
-   [**PdhEnumMachinesH**](/windows/win32/Pdh/nf-pdh-pdhenummachinesha?branch=master)
-   [**PdhEnumObjectItems**](/windows/win32/Pdh/nf-pdh-pdhenumobjectitemsa?branch=master)
-   [**PdhEnumObjectItemsH**](/windows/win32/Pdh/nf-pdh-pdhenumobjectitemsha?branch=master)
-   [**PdhEnumObjects**](/windows/win32/Pdh/nf-pdh-pdhenumobjectsa?branch=master)
-   [**PdhEnumObjectsH**](/windows/win32/Pdh/nf-pdh-pdhenumobjectsha?branch=master)
-   [**PdhExpandCounterPath**](/windows/win32/Pdh/nf-pdh-pdhexpandcounterpatha?branch=master)
-   [**PdhExpandWildCardPath**](/windows/win32/Pdh/nf-pdh-pdhexpandwildcardpatha?branch=master)
-   [**PdhExpandWildCardPathH**](/windows/win32/Pdh/nf-pdh-pdhexpandwildcardpathha?branch=master)
-   [**PdhFormatFromRawValue**](/windows/win32/Pdh/nf-pdh-pdhformatfromrawvalue?branch=master)
-   [**PdhGetCounterInfo**](/windows/win32/Pdh/nf-pdh-pdhgetcounterinfoa?branch=master)
-   [**PdhGetCounterTimeBase**](/windows/win32/Pdh/nf-pdh-pdhgetcountertimebase?branch=master)
-   [**PdhGetDataSourceTimeRange**](/windows/win32/Pdh/nf-pdh-pdhgetdatasourcetimerangea?branch=master)
-   [**PdhGetDataSourceTimeRangeH**](/windows/win32/Pdh/nf-pdh-pdhgetdatasourcetimerangeh?branch=master)
-   [**PdhGetDefaultPerfCounter**](/windows/win32/Pdh/nf-pdh-pdhgetdefaultperfcountera?branch=master)
-   [**PdhGetDefaultPerfCounterH**](/windows/win32/Pdh/nf-pdh-pdhgetdefaultperfcounterha?branch=master)
-   [**PdhGetDefaultPerfObject**](/windows/win32/Pdh/nf-pdh-pdhgetdefaultperfobjecta?branch=master)
-   [**PdhGetDefaultPerfObjectH**](/windows/win32/Pdh/nf-pdh-pdhgetdefaultperfobjectha?branch=master)
-   [**PdhGetDllVersion**](/windows/win32/Pdh/nf-pdh-pdhgetdllversion?branch=master)
-   [**PdhGetFormattedCounterArray**](/windows/win32/Pdh/nf-pdh-pdhgetformattedcounterarraya?branch=master)
-   [**PdhGetFormattedCounterValue**](/windows/win32/Pdh/nf-pdh-pdhgetformattedcountervalue?branch=master)
-   [**PdhGetLogFileSize**](/windows/win32/Pdh/nf-pdh-pdhgetlogfilesize?branch=master)
-   [**PdhGetRawCounterArray**](/windows/win32/Pdh/nf-pdh-pdhgetrawcounterarraya?branch=master)
-   [**PdhGetRawCounterValue**](/windows/win32/Pdh/nf-pdh-pdhgetrawcountervalue?branch=master)
-   [**PdhIsRealTimeQuery**](/windows/win32/Pdh/nf-pdh-pdhisrealtimequery?branch=master)
-   [**PdhLookupPerfIndexByName**](/windows/win32/Pdh/nf-pdh-pdhlookupperfindexbynamea?branch=master)
-   [**PdhLookupPerfNameByIndex**](/windows/win32/Pdh/nf-pdh-pdhlookupperfnamebyindexa?branch=master)
-   [**PdhMakeCounterPath**](/windows/win32/Pdh/nf-pdh-pdhmakecounterpatha?branch=master)
-   [**PdhOpenLog**](/windows/win32/Pdh/nf-pdh-pdhopenloga?branch=master)
-   [**PdhOpenQuery**](/windows/win32/Pdh/nf-pdh-pdhopenquerya?branch=master)
-   [**PdhOpenQueryH**](/windows/win32/Pdh/nf-pdh-pdhopenqueryh?branch=master)
-   [**PdhParseCounterPath**](/windows/win32/Pdh/nf-pdh-pdhparsecounterpatha?branch=master)
-   [**PdhParseInstanceName**](/windows/win32/Pdh/nf-pdh-pdhparseinstancenamea?branch=master)
-   [**PdhReadRawLogRecord**](/windows/win32/Pdh/nf-pdh-pdhreadrawlogrecord?branch=master)
-   [**PdhRemoveCounter**](/windows/win32/Pdh/nf-pdh-pdhremovecounter?branch=master)
-   [**PdhSelectDataSource**](/windows/win32/Pdh/nf-pdh-pdhselectdatasourcea?branch=master)
-   [**PdhSetCounterScaleFactor**](/windows/win32/Pdh/nf-pdh-pdhsetcounterscalefactor?branch=master)
-   [**PdhSetDefaultRealTimeDataSource**](/windows/win32/Pdh/nf-pdh-pdhsetdefaultrealtimedatasource?branch=master)
-   [**PdhSetQueryTimeRange**](/windows/win32/Pdh/nf-pdh-pdhsetquerytimerange?branch=master)
-   [**PdhUpdateLog**](/windows/win32/Pdh/nf-pdh-pdhupdateloga?branch=master)
-   [**PdhUpdateLogFileCatalog**](/windows/win32/Pdh/nf-pdh-pdhupdatelogfilecatalog?branch=master)
-   [**PdhValidatePath**](/windows/win32/Pdh/nf-pdh-pdhvalidatepatha?branch=master)
-   [**PdhValidatePathEx**](/windows/win32/Pdh/nf-pdh-pdhvalidatepathexa?branch=master)

> [!Note]  
> You cannot use the Performance Data Helper abstraction-layer functions if you are writing Windows OneCore apps.

 

Use the following low-level functions to consume performance data from version 2 performance counters if you cannot use the Performance Data Helper abstraction-layer functions:

-   [**PerfAddCounters**](/windows/win32/Perflib/nf-perflib-perfaddcounters?branch=master)
-   [**PerfCloseQueryHandle**](/windows/win32/Perflib/nf-perflib-perfclosequeryhandle?branch=master)
-   [**PerfDeleteCounters**](/windows/win32/Perflib/nf-perflib-perfdeletecounters?branch=master)
-   [**PerfEnumerateCounterSet**](/windows/win32/Perflib/nf-perflib-perfenumeratecounterset?branch=master)
-   [**PerfEnumerateCounterSetInstances**](/windows/win32/Perflib/nf-perflib-perfenumeratecountersetinstances?branch=master)
-   [**PerfOpenQueryHandle**](/windows/win32/Perflib/nf-perflib-perfopenqueryhandle?branch=master)
-   [**PerfQueryCounterData**](/windows/win32/Perflib/nf-perflib-perfquerycounterdata?branch=master)
-   [**PerfQueryCounterInfo**](/windows/win32/Perflib/nf-perflib-perfquerycounterinfo?branch=master)
-   [**PerfQueryCounterSetRegistrationInfo**](/windows/win32/Perflib/nf-perflib-perfquerycountersetregistrationinfo?branch=master)

## Provider functions

Performance providers use the following functions:

-   [*AllocateMemory*](/windows/win32/Perflib/nc-perflib-perf_mem_alloc?branch=master)
-   [*ControlCallback*](/windows/win32/Perflib/nc-perflib-perflibrequest?branch=master)
-   [**CounterCleanup**](countercleanup.md)
-   [**CounterInitialize**](counterinitialize.md)
-   [*FreeMemory*](/windows/win32/Perflib/nc-perflib-perf_mem_free?branch=master)
-   [**PerfCreateInstance**](/windows/win32/Perflib/nf-perflib-perfcreateinstance?branch=master)
-   [**PerfDecrementULongCounterValue**](/windows/win32/Perflib/nf-perflib-perfdecrementulongcountervalue?branch=master)
-   [**PerfDecrementULongLongCounterValue**](/windows/win32/Perflib/nf-perflib-perfdecrementulonglongcountervalue?branch=master)
-   [**PerfDeleteInstance**](/windows/win32/Perflib/nf-perflib-perfdeleteinstance?branch=master)
-   [**PerfIncrementULongCounterValue**](/windows/win32/Perflib/nf-perflib-perfincrementulongcountervalue?branch=master)
-   [**PerfIncrementULongLongCounterValue**](/windows/win32/Perflib/nf-perflib-perfincrementulonglongcountervalue?branch=master)
-   [**PerfQueryInstance**](/windows/win32/Perflib/nf-perflib-perfqueryinstance?branch=master)
-   [**PerfSetCounterSetInfo**](/windows/win32/Perflib/nf-perflib-perfsetcountersetinfo?branch=master)
-   [**PerfSetULongCounterValue**](/windows/win32/Perflib/nf-perflib-perfsetulongcountervalue?branch=master)
-   [**PerfSetULongLongCounterValue**](/windows/win32/Perflib/nf-perflib-perfsetulonglongcountervalue?branch=master)
-   [**PerfSetCounterRefValue**](/windows/win32/Perflib/nf-perflib-perfsetcounterrefvalue?branch=master)
-   [**PerfStartProvider**](/windows/win32/Perflib/nf-perflib-perfstartprovider?branch=master)
-   [**PerfStartProviderEx**](/windows/win32/Perflib/nf-perflib-perfstartproviderex?branch=master)
-   [**PerfStopProvider**](/windows/win32/Perflib/nf-perflib-perfstopprovider?branch=master)

> [!Note]  
> Performance data providers that use the functions in the previous list are called version 2 providers.

 

A [performance extension DLL](providing-counter-data-using-a-performance-dll.md) that provides performance data implements the following functions:

-   [**ClosePerformanceData**](/windows/win32/Winperf/nc-winperf-pm_close_proc?branch=master)
-   [**CollectPerformanceData**](/windows/win32/Winperf/nc-winperf-pm_collect_proc?branch=master)
-   [**OpenPerformanceData**](/windows/win32/Winperf/?branch=master)

> [!Note]  
> A performance extension DLL is also called a version1 provider. Although you still can use a performance extension DLL to provide counter data, you are encouraged to use the new architecture for new providers instead. You also are encouraged to replace existing version 1 provides with version 2 providers.

 

You can use the following optional functions to register and unregister the .ini data for version 1 providers:

-   [**LoadPerfCounterTextStrings**](/windows/win32/Loadperf/nf-loadperf-loadperfcountertextstringsa?branch=master)
-   [**UnloadPerfCounterTextStrings**](/windows/win32/Loadperf/nf-loadperf-unloadperfcountertextstringsa?branch=master)

> [!Note]  
> To register and unregister version 2 performance counters, use the lodctr and unlodctr tools. You cannot register and unregister version 2 counter by using the functions for the version 1 providers.

 

 

 



