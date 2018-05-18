---
Description: 'Use the following functions to consume and provide performance data.'
ms.assetid: 'a2c97b8b-b1b1-4dd8-8f23-edffaa74d028'
title: Performance Counters Functions
---

# Performance Counters Functions

Use the following functions to consume and provide performance data.

## Consumer functions

Use the following Performance Data Helper abstraction-layer functions to consume performance data from both version 1 and version 2 performance counters:

-   [**CounterPathCallBack**](counterpathcallback.md)
-   [**PdhAddCounter**](pdhaddcounter.md)
-   [**PdhAddEnglishCounter**](pdhaddenglishcounter.md)
-   [**PdhBindInputDataSource**](pdhbindinputdatasource.md)
-   [**PdhBrowseCounters**](pdhbrowsecounters.md)
-   [**PdhBrowseCountersH**](pdhbrowsecountersh.md)
-   [**PdhCalculateCounterFromRawValue**](pdhcalculatecounterfromrawvalue.md)
-   [**PdhCloseLog**](pdhcloselog.md)
-   [**PdhCloseQuery**](pdhclosequery.md)
-   [**PdhCollectQueryData**](pdhcollectquerydata.md)
-   [**PdhCollectQueryDataEx**](pdhcollectquerydataex.md)
-   [**PdhCollectQueryDataWithTime**](pdhcollectquerydatawithtime.md)
-   [**PdhComputeCounterStatistics**](pdhcomputecounterstatistics.md)
-   [**PdhConnectMachine**](pdhconnectmachine.md)
-   [**PdhEnumLogSetNames**](pdhenumlogsetnames.md)
-   [**PdhEnumMachines**](pdhenummachines.md)
-   [**PdhEnumMachinesH**](pdhenummachinesh.md)
-   [**PdhEnumObjectItems**](pdhenumobjectitems.md)
-   [**PdhEnumObjectItemsH**](pdhenumobjectitemsh.md)
-   [**PdhEnumObjects**](pdhenumobjects.md)
-   [**PdhEnumObjectsH**](pdhenumobjectsh.md)
-   [**PdhExpandCounterPath**](pdhexpandcounterpath.md)
-   [**PdhExpandWildCardPath**](pdhexpandwildcardpath.md)
-   [**PdhExpandWildCardPathH**](pdhexpandwildcardpathh.md)
-   [**PdhFormatFromRawValue**](pdhformatfromrawvalue.md)
-   [**PdhGetCounterInfo**](pdhgetcounterinfo.md)
-   [**PdhGetCounterTimeBase**](pdhgetcountertimebase.md)
-   [**PdhGetDataSourceTimeRange**](pdhgetdatasourcetimerange.md)
-   [**PdhGetDataSourceTimeRangeH**](pdhgetdatasourcetimerangeh.md)
-   [**PdhGetDefaultPerfCounter**](pdhgetdefaultperfcounter.md)
-   [**PdhGetDefaultPerfCounterH**](pdhgetdefaultperfcounterh.md)
-   [**PdhGetDefaultPerfObject**](pdhgetdefaultperfobject.md)
-   [**PdhGetDefaultPerfObjectH**](pdhgetdefaultperfobjecth.md)
-   [**PdhGetDllVersion**](pdhgetdllversion.md)
-   [**PdhGetFormattedCounterArray**](pdhgetformattedcounterarray.md)
-   [**PdhGetFormattedCounterValue**](pdhgetformattedcountervalue.md)
-   [**PdhGetLogFileSize**](pdhgetlogfilesize.md)
-   [**PdhGetRawCounterArray**](pdhgetrawcounterarray.md)
-   [**PdhGetRawCounterValue**](pdhgetrawcountervalue.md)
-   [**PdhIsRealTimeQuery**](pdhisrealtimequery.md)
-   [**PdhLookupPerfIndexByName**](pdhlookupperfindexbyname.md)
-   [**PdhLookupPerfNameByIndex**](pdhlookupperfnamebyindex.md)
-   [**PdhMakeCounterPath**](pdhmakecounterpath.md)
-   [**PdhOpenLog**](pdhopenlog.md)
-   [**PdhOpenQuery**](pdhopenquery.md)
-   [**PdhOpenQueryH**](pdhopenqueryh.md)
-   [**PdhParseCounterPath**](pdhparsecounterpath.md)
-   [**PdhParseInstanceName**](pdhparseinstancename.md)
-   [**PdhReadRawLogRecord**](pdhreadrawlogrecord.md)
-   [**PdhRemoveCounter**](pdhremovecounter.md)
-   [**PdhSelectDataSource**](pdhselectdatasource.md)
-   [**PdhSetCounterScaleFactor**](pdhsetcounterscalefactor.md)
-   [**PdhSetDefaultRealTimeDataSource**](pdhsetdefaultrealtimedatasource.md)
-   [**PdhSetQueryTimeRange**](pdhsetquerytimerange.md)
-   [**PdhUpdateLog**](pdhupdatelog.md)
-   [**PdhUpdateLogFileCatalog**](pdhupdatelogfilecatalog.md)
-   [**PdhValidatePath**](pdhvalidatepath.md)
-   [**PdhValidatePathEx**](pdhvalidatepathex.md)

> [!Note]  
> You cannot use the Performance Data Helper abstraction-layer functions if you are writing Windows OneCore apps.

 

Use the following low-level functions to consume performance data from version 2 performance counters if you cannot use the Performance Data Helper abstraction-layer functions:

-   [**PerfAddCounters**](perfaddcounters.md)
-   [**PerfCloseQueryHandle**](perfclosequeryhandle.md)
-   [**PerfDeleteCounters**](perfdeletecounters.md)
-   [**PerfEnumerateCounterSet**](perfenumeratecounterset.md)
-   [**PerfEnumerateCounterSetInstances**](perfenumeratecountersetinstances.md)
-   [**PerfOpenQueryHandle**](perfopenqueryhandle.md)
-   [**PerfQueryCounterData**](perfquerycounterdata.md)
-   [**PerfQueryCounterInfo**](perfquerycounterinfo.md)
-   [**PerfQueryCounterSetRegistrationInfo**](perfquerycountersetregistrationinfo.md)

## Provider functions

Performance providers use the following functions:

-   [*AllocateMemory*](allocatememory.md)
-   [*ControlCallback*](controlcallback-perflibv2.md)
-   [**CounterCleanup**](countercleanup.md)
-   [**CounterInitialize**](counterinitialize.md)
-   [*FreeMemory*](freememory.md)
-   [**PerfCreateInstance**](perfcreateinstance.md)
-   [**PerfDecrementULongCounterValue**](perfdecrementulongcountervalue.md)
-   [**PerfDecrementULongLongCounterValue**](perfdecrementulonglongcountervalue.md)
-   [**PerfDeleteInstance**](perfdeleteinstance.md)
-   [**PerfIncrementULongCounterValue**](perfincrementulongcountervalue.md)
-   [**PerfIncrementULongLongCounterValue**](perfincrementulonglongcountervalue.md)
-   [**PerfQueryInstance**](perfqueryinstance.md)
-   [**PerfSetCounterSetInfo**](perfsetcountersetinfo.md)
-   [**PerfSetULongCounterValue**](perfsetulongcountervalue.md)
-   [**PerfSetULongLongCounterValue**](perfsetulonglongcountervalue.md)
-   [**PerfSetCounterRefValue**](perfsetcounterrefvalue.md)
-   [**PerfStartProvider**](perfstartprovider.md)
-   [**PerfStartProviderEx**](perfstartproviderex.md)
-   [**PerfStopProvider**](perfstopprovider.md)

> [!Note]  
> Performance data providers that use the functions in the previous list are called version 2 providers.

 

A [performance extension DLL](providing-counter-data-using-a-performance-dll.md) that provides performance data implements the following functions:

-   [**ClosePerformanceData**](closeperformancedata.md)
-   [**CollectPerformanceData**](collectperformancedata.md)
-   [**OpenPerformanceData**](openperformancedata.md)

> [!Note]  
> A performance extension DLL is also called a version1 provider. Although you still can use a performance extension DLL to provide counter data, you are encouraged to use the new architecture for new providers instead. You also are encouraged to replace existing version 1 provides with version 2 providers.

 

You can use the following optional functions to register and unregister the .ini data for version 1 providers:

-   [**LoadPerfCounterTextStrings**](loadperfcountertextstrings.md)
-   [**UnloadPerfCounterTextStrings**](unloadperfcountertextstrings.md)

> [!Note]  
> To register and unregister version 2 performance counters, use the lodctr and unlodctr tools. You cannot register and unregister version 2 counter by using the functions for the version 1 providers.

 

 

 



