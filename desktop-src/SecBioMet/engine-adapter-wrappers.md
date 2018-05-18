---
title: Engine Adapter Wrappers
description: Functions that you can use to call functions on your engine adapter. These functions are defined in Winbio\_adapter.h.
ms.assetid: 'b3d6d617-e423-4ed5-9d29-be72c5dd8b49'
---

# Engine Adapter Wrappers

The following wrapper functions are defined in Winbio\_adapter.h. You can use them to call functions on your engine adapter.



| Function                                           | Description                                                                                                                                                                                           |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WbioEngineAcceptSampleData<br/>              | Calls the [**EngineAdapterAcceptSampleData**](engineadapteracceptsampledata.md) function.<br/>                                                                                                 |
| WbioEngineActivate<br/>                      | Calls the [**EngineAdapterActivate**](engineadapteractivate.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                                           |
| WbioEngineAttach<br/>                        | Calls the [**EngineAdapterAttach**](engineadapterattach.md) function.<br/>                                                                                                                     |
| WbioEngineCheckForDuplicate<br/>             | Calls the [**EngineAdapterCheckForDuplicate**](engineadaptercheckforduplicate.md) function.<br/>                                                                                               |
| WbioEngineClearContext<br/>                  | Calls the [**EngineAdapterClearContext**](engineadapterclearcontext.md) function.<br/>                                                                                                         |
| WbioEngineCommitEnrollment<br/>              | Calls the [**EngineAdapterCommitEnrollment**](engineadaptercommitenrollment.md) function.<br/>                                                                                                 |
| WbioEngineControlUnit<br/>                   | Calls the [**EngineAdapterControlUnit**](engineadaptercontrolunit.md) function.<br/>                                                                                                           |
| WbioEngineControlUnitPrivileged<br/>         | Calls the [**EngineAdapterControlUnitPrivileged**](engineadaptercontrolunitprivileged.md) function.<br/>                                                                                       |
| WbioEngineCreateEnrollment<br/>              | Calls the [**EngineAdapterCreateEnrollment**](engineadaptercreateenrollment.md) function.<br/>                                                                                                 |
| WbioEngineDeactivate<br/>                    | Calls the [**EngineAdapterDeactivate**](engineadapterdeactivate.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                                       |
| WbioEngineDetach<br/>                        | Calls the [**EngineAdapterDetach**](engineadapterdetach.md) function.<br/>                                                                                                                     |
| WbioEngineDiscardEnrollment<br/>             | Calls the [**EngineAdapterDiscardEnrollment**](engineadapterdiscardenrollment.md) function.<br/>                                                                                               |
| WbioEngineExportEngineData<br/>              | Calls the [**EngineAdapterExportEngineData**](engineadapterexportenginedata.md) function.<br/>                                                                                                 |
| WbioEngineGetEnrollmentHash<br/>             | Calls the [**EngineAdapterGetEnrollmentHash**](engineadaptergetenrollmenthash.md) function.<br/>                                                                                               |
| WbioEngineGetEnrollmentStatus<br/>           | Calls the [**EngineAdapterGetEnrollmentStatus**](engineadaptergetenrollmentstatus.md) function.<br/>                                                                                           |
| WbioEngineIdentifyAll<br/>                   | Calls the [**EngineAdapterIdentifyAll**](engineadapteridentifyall.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                                     |
| WbioEngineIdentifyFeatureSet<br/>            | Calls the [**EngineAdapterIdentifyFeatureSet**](engineadapteridentifyfeatureset.md) function.<br/>                                                                                             |
| WbioEngineNotifyPowerChange<br/>             | Calls the [*EngineAdapterNotifyPowerChange*](engineadapternotifypowerchange.md) function.<br/> This wrapper function is supported starting in Windows 8.<br/>                            |
| WbioEnginePipelineCleanup<br/>               | Calls the [**EngineAdapterPipelineCleanup**](engineadapterpipelinecleanup.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                             |
| WbioEnginePipelineInit<br/>                  | Calls the [**EngineAdapterPipelineInit**](engineadapterpipelineinit.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                                   |
| WbioEngineQueryCalibrationData<br/>          | Calls the [**EngineAdapterQueryCalibrationData**](engineadapterquerycalibrationdata.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                   |
| WbioEngineQueryExtendedEnrollmentStatus<br/> | Calls the [**EngineAdapterQueryExtendedEnrollmentStatus**](engineadapterqueryextendedenrollmentstatus.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/> |
| WbioEngineQueryExtendedInfo<br/>             | Calls the [**EngineAdapterQueryExtendedInfo**](engineadapterqueryextendedinfo.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                         |
| WbioEngineQueryHashAlgorithms<br/>           | Calls the [**EngineAdapterQueryHashAlgorithms**](engineadapterqueryhashalgorithms.md) function.<br/>                                                                                           |
| WbioEngineQueryIndexVectorSize<br/>          | Calls the [**EngineAdapterQueryIndexVectorSize**](engineadapterqueryindexvectorsize.md) function.<br/>                                                                                         |
| WbioEngineQueryPreferredFormat<br/>          | Calls the [**EngineAdapterQueryPreferredFormat**](engineadapterquerypreferredformat.md) function.<br/>                                                                                         |
| WbioEngineQuerySampleHint<br/>               | Calls the [**EngineAdapterQuerySampleHint**](engineadapterquerysamplehint.md) function.<br/>                                                                                                   |
| WbioEngineRefreshCache<br/>                  | Calls the [**EngineAdapterRefreshCache**](engineadapterrefreshcache.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                                   |
| WbioEngineSelectCalibrationFormat<br/>       | Calls the [**EngineAdapterSelectCalibrationFormat**](engineadapterselectcalibrationformat.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>             |
| WbioEngineSetAccountPolicy<br/>              | Calls the [**EngineAdapterSetAccountPolicy**](engineadaptersetaccountpolicy.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                           |
| WbioEngineSetEnrollmentParameters<br/>       | Calls the [**EngineAdapterSetEnrollmentParameters**](engineadaptersetenrollmentparameters.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>             |
| WbioEngineSetEnrollmentSelector<br/>         | Calls the [**EngineAdapterSetEnrollmentSelector**](engineadaptersetenrollmentselector.md) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                 |
| WbioEngineSetHashAlgorithm<br/>              | Calls the [**EngineAdapterSetHashAlgorithm**](engineadaptersethashalgorithm.md) function.<br/>                                                                                                 |
| WbioEngineUpdateEnrollment<br/>              | Calls the [**EngineAdapterUpdateEnrollment**](engineadapterupdateenrollment.md) function.<br/>                                                                                                 |
| WbioEngineVerifyFeatureSet<br/>              | Calls the [**EngineAdapterVerifyFeatureSet**](engineadapterverifyfeatureset.md) function.<br/>                                                                                                 |



 

## Related topics

<dl> <dt>

[Engine Adapter Functions](engine-adapter-functions.md)
</dt> <dt>

[Plug-in Functions](plug-in-functions.md)
</dt> </dl>

 

 





