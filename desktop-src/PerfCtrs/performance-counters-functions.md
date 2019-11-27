---
Description: Use the following functions to consume and provide performance data.
ms.assetid: a2c97b8b-b1b1-4dd8-8f23-edffaa74d028
title: Performance Counters Functions
ms.topic: article
ms.date: 05/31/2018
---

# Performance Counters Functions

Use the following functions to consume and provide performance data.

## Consumer functions

Use the following Performance Data Helper abstraction-layer functions to consume performance data from both version 1 and version 2 performance counters:

-   [**CounterPathCallBack**](/windows/desktop/api/Pdh/nc-pdh-counterpathcallback)
-   [**PdhAddCounter**](/windows/desktop/api/Pdh/nf-pdh-pdhaddcountera)
-   [**PdhAddEnglishCounter**](/windows/desktop/api/Pdh/nf-pdh-pdhaddenglishcountera)
-   [**PdhBindInputDataSource**](/windows/desktop/api/Pdh/nf-pdh-pdhbindinputdatasourcea)
-   [**PdhBrowseCounters**](/windows/desktop/api/Pdh/nf-pdh-pdhbrowsecountersa)
-   [**PdhBrowseCountersH**](/windows/desktop/api/Pdh/nf-pdh-pdhbrowsecountersha)
-   [**PdhCalculateCounterFromRawValue**](/windows/desktop/api/Pdh/nf-pdh-pdhcalculatecounterfromrawvalue)
-   [**PdhCloseLog**](/windows/desktop/api/Pdh/nf-pdh-pdhcloselog)
-   [**PdhCloseQuery**](/windows/desktop/api/Pdh/nf-pdh-pdhclosequery)
-   [**PdhCollectQueryData**](/windows/desktop/api/Pdh/nf-pdh-pdhcollectquerydata)
-   [**PdhCollectQueryDataEx**](/windows/desktop/api/Pdh/nf-pdh-pdhcollectquerydataex)
-   [**PdhCollectQueryDataWithTime**](/windows/desktop/api/Pdh/nf-pdh-pdhcollectquerydatawithtime)
-   [**PdhComputeCounterStatistics**](/windows/desktop/api/Pdh/nf-pdh-pdhcomputecounterstatistics)
-   [**PdhConnectMachine**](/windows/desktop/api/Pdh/nf-pdh-pdhconnectmachinea)
-   [**PdhEnumLogSetNames**](/windows/desktop/api/Pdh/nf-pdh-pdhenumlogsetnamesa)
-   [**PdhEnumMachines**](/windows/desktop/api/Pdh/nf-pdh-pdhenummachinesa)
-   [**PdhEnumMachinesH**](/windows/desktop/api/Pdh/nf-pdh-pdhenummachinesha)
-   [**PdhEnumObjectItems**](/windows/desktop/api/Pdh/nf-pdh-pdhenumobjectitemsa)
-   [**PdhEnumObjectItemsH**](/windows/desktop/api/Pdh/nf-pdh-pdhenumobjectitemsha)
-   [**PdhEnumObjects**](/windows/desktop/api/Pdh/nf-pdh-pdhenumobjectsa)
-   [**PdhEnumObjectsH**](/windows/desktop/api/Pdh/nf-pdh-pdhenumobjectsha)
-   [**PdhExpandCounterPath**](/windows/desktop/api/Pdh/nf-pdh-pdhexpandcounterpatha)
-   [**PdhExpandWildCardPath**](/windows/desktop/api/Pdh/nf-pdh-pdhexpandwildcardpatha)
-   [**PdhExpandWildCardPathH**](/windows/desktop/api/Pdh/nf-pdh-pdhexpandwildcardpathha)
-   [**PdhFormatFromRawValue**](/windows/desktop/api/Pdh/nf-pdh-pdhformatfromrawvalue)
-   [**PdhGetCounterInfo**](/windows/desktop/api/Pdh/nf-pdh-pdhgetcounterinfoa)
-   [**PdhGetCounterTimeBase**](/windows/desktop/api/Pdh/nf-pdh-pdhgetcountertimebase)
-   [**PdhGetDataSourceTimeRange**](/windows/desktop/api/Pdh/nf-pdh-pdhgetdatasourcetimerangea)
-   [**PdhGetDataSourceTimeRangeH**](/windows/desktop/api/Pdh/nf-pdh-pdhgetdatasourcetimerangeh)
-   [**PdhGetDefaultPerfCounter**](/windows/desktop/api/Pdh/nf-pdh-pdhgetdefaultperfcountera)
-   [**PdhGetDefaultPerfCounterH**](/windows/desktop/api/Pdh/nf-pdh-pdhgetdefaultperfcounterha)
-   [**PdhGetDefaultPerfObject**](/windows/desktop/api/Pdh/nf-pdh-pdhgetdefaultperfobjecta)
-   [**PdhGetDefaultPerfObjectH**](/windows/desktop/api/Pdh/nf-pdh-pdhgetdefaultperfobjectha)
-   [**PdhGetDllVersion**](/windows/desktop/api/Pdh/nf-pdh-pdhgetdllversion)
-   [**PdhGetFormattedCounterArray**](/windows/desktop/api/Pdh/nf-pdh-pdhgetformattedcounterarraya)
-   [**PdhGetFormattedCounterValue**](/windows/desktop/api/Pdh/nf-pdh-pdhgetformattedcountervalue)
-   [**PdhGetLogFileSize**](/windows/desktop/api/Pdh/nf-pdh-pdhgetlogfilesize)
-   [**PdhGetRawCounterArray**](/windows/desktop/api/Pdh/nf-pdh-pdhgetrawcounterarraya)
-   [**PdhGetRawCounterValue**](/windows/desktop/api/Pdh/nf-pdh-pdhgetrawcountervalue)
-   [**PdhIsRealTimeQuery**](/windows/desktop/api/Pdh/nf-pdh-pdhisrealtimequery)
-   [**PdhLookupPerfIndexByName**](/windows/desktop/api/Pdh/nf-pdh-pdhlookupperfindexbynamea)
-   [**PdhLookupPerfNameByIndex**](/windows/desktop/api/Pdh/nf-pdh-pdhlookupperfnamebyindexa)
-   [**PdhMakeCounterPath**](/windows/desktop/api/Pdh/nf-pdh-pdhmakecounterpatha)
-   [**PdhOpenLog**](/windows/desktop/api/Pdh/nf-pdh-pdhopenloga)
-   [**PdhOpenQuery**](/windows/desktop/api/Pdh/nf-pdh-pdhopenquerya)
-   [**PdhOpenQueryH**](/windows/desktop/api/Pdh/nf-pdh-pdhopenqueryh)
-   [**PdhParseCounterPath**](/windows/desktop/api/Pdh/nf-pdh-pdhparsecounterpatha)
-   [**PdhParseInstanceName**](/windows/desktop/api/Pdh/nf-pdh-pdhparseinstancenamea)
-   [**PdhReadRawLogRecord**](/windows/desktop/api/Pdh/nf-pdh-pdhreadrawlogrecord)
-   [**PdhRemoveCounter**](/windows/desktop/api/Pdh/nf-pdh-pdhremovecounter)
-   [**PdhSelectDataSource**](/windows/desktop/api/Pdh/nf-pdh-pdhselectdatasourcea)
-   [**PdhSetCounterScaleFactor**](/windows/desktop/api/Pdh/nf-pdh-pdhsetcounterscalefactor)
-   [**PdhSetDefaultRealTimeDataSource**](/windows/desktop/api/Pdh/nf-pdh-pdhsetdefaultrealtimedatasource)
-   [**PdhSetQueryTimeRange**](/windows/desktop/api/Pdh/nf-pdh-pdhsetquerytimerange)
-   [**PdhUpdateLog**](/windows/desktop/api/Pdh/nf-pdh-pdhupdateloga)
-   [**PdhUpdateLogFileCatalog**](/windows/desktop/api/Pdh/nf-pdh-pdhupdatelogfilecatalog)
-   [**PdhValidatePath**](/windows/desktop/api/Pdh/nf-pdh-pdhvalidatepatha)
-   [**PdhValidatePathEx**](/windows/desktop/api/Pdh/nf-pdh-pdhvalidatepathexa)

> [!Note]  
> You cannot use the Performance Data Helper abstraction-layer functions if you are writing Windows OneCore apps.

 

Use the following low-level functions to consume performance data from version 2 performance counters if you cannot use the Performance Data Helper abstraction-layer functions:

-   [**PerfAddCounters**](/windows/desktop/api/Perflib/nf-perflib-perfaddcounters)
-   [**PerfCloseQueryHandle**](/windows/desktop/api/Perflib/nf-perflib-perfclosequeryhandle)
-   [**PerfDeleteCounters**](/windows/desktop/api/Perflib/nf-perflib-perfdeletecounters)
-   [**PerfEnumerateCounterSet**](/windows/desktop/api/Perflib/nf-perflib-perfenumeratecounterset)
-   [**PerfEnumerateCounterSetInstances**](/windows/desktop/api/Perflib/nf-perflib-perfenumeratecountersetinstances)
-   [**PerfOpenQueryHandle**](/windows/desktop/api/Perflib/nf-perflib-perfopenqueryhandle)
-   [**PerfQueryCounterData**](/windows/desktop/api/Perflib/nf-perflib-perfquerycounterdata)
-   [**PerfQueryCounterInfo**](/windows/desktop/api/Perflib/nf-perflib-perfquerycounterinfo)
-   [**PerfQueryCounterSetRegistrationInfo**](/windows/desktop/api/Perflib/nf-perflib-perfquerycountersetregistrationinfo)

## Provider functions

Performance providers use the following functions:

-   [*AllocateMemory*](/windows/desktop/api/Perflib/nc-perflib-perf_mem_alloc)
-   [*ControlCallback*](/windows/desktop/api/Perflib/nc-perflib-perflibrequest)
-   [**CounterCleanup**](countercleanup.md)
-   [**CounterInitialize**](counterinitialize.md)
-   [*FreeMemory*](/windows/desktop/api/Perflib/nc-perflib-perf_mem_free)
-   [**PerfCreateInstance**](/windows/desktop/api/Perflib/nf-perflib-perfcreateinstance)
-   [**PerfDecrementULongCounterValue**](/windows/desktop/api/Perflib/nf-perflib-perfdecrementulongcountervalue)
-   [**PerfDecrementULongLongCounterValue**](/windows/desktop/api/Perflib/nf-perflib-perfdecrementulonglongcountervalue)
-   [**PerfDeleteInstance**](/windows/desktop/api/Perflib/nf-perflib-perfdeleteinstance)
-   [**PerfIncrementULongCounterValue**](/windows/desktop/api/Perflib/nf-perflib-perfincrementulongcountervalue)
-   [**PerfIncrementULongLongCounterValue**](/windows/desktop/api/Perflib/nf-perflib-perfincrementulonglongcountervalue)
-   [**PerfQueryInstance**](/windows/desktop/api/Perflib/nf-perflib-perfqueryinstance)
-   [**PerfSetCounterSetInfo**](/windows/desktop/api/Perflib/nf-perflib-perfsetcountersetinfo)
-   [**PerfSetULongCounterValue**](/windows/desktop/api/Perflib/nf-perflib-perfsetulongcountervalue)
-   [**PerfSetULongLongCounterValue**](/windows/desktop/api/Perflib/nf-perflib-perfsetulonglongcountervalue)
-   [**PerfSetCounterRefValue**](/windows/desktop/api/Perflib/nf-perflib-perfsetcounterrefvalue)
-   [**PerfStartProvider**](/windows/desktop/api/Perflib/nf-perflib-perfstartprovider)
-   [**PerfStartProviderEx**](/windows/desktop/api/Perflib/nf-perflib-perfstartproviderex)
-   [**PerfStopProvider**](/windows/desktop/api/Perflib/nf-perflib-perfstopprovider)

> [!Note]  
> Performance data providers that use the functions in the previous list are called version 2 providers.

 

A [performance extension DLL](providing-counter-data-using-a-performance-dll.md) that provides performance data implements the following functions:

-   [**ClosePerformanceData**](https://msdn.microsoft.com/library/Aa371895(v=VS.85).aspx)
-   [**CollectPerformanceData**](https://msdn.microsoft.com/library/Aa371898(v=VS.85).aspx)
-   [**OpenPerformanceData**](https://msdn.microsoft.com/library/Aa372200(v=VS.85).aspx)

> [!Note]  
> A performance extension DLL is also called a version1 provider. Although you still can use a performance extension DLL to provide counter data, you are encouraged to use the new architecture for new providers instead. You also are encouraged to replace existing version 1 provides with version 2 providers.

 

You can use the following optional functions to register and unregister the .ini data for version 1 providers:

-   [**LoadPerfCounterTextStrings**](/windows/desktop/api/Loadperf/nf-loadperf-loadperfcountertextstringsa)
-   [**UnloadPerfCounterTextStrings**](/windows/desktop/api/Loadperf/nf-loadperf-unloadperfcountertextstringsa)

> [!Note]  
> To register and unregister version 2 performance counters, use the lodctr and unlodctr tools. You cannot register and unregister version 2 counter by using the functions for the version 1 providers.

 

 

 



