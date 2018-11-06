---
title: Engine Adapter Wrappers
description: Functions that you can use to call functions on your engine adapter. These functions are defined in Winbio\_adapter.h.
ms.assetid: b3d6d617-e423-4ed5-9d29-be72c5dd8b49
ms.topic: article
ms.date: 05/31/2018
---

# Engine Adapter Wrappers

The following wrapper functions are defined in Winbio\_adapter.h. You can use them to call functions on your engine adapter.



| Function                                           | Description                                                                                                                                                                                           |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WbioEngineAcceptSampleData<br/>              | Calls the [**EngineAdapterAcceptSampleData**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_accept_sample_data_fn) function.<br/>                                                                                                 |
| WbioEngineActivate<br/>                      | Calls the [**EngineAdapterActivate**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_activate_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                                           |
| WbioEngineAttach<br/>                        | Calls the [**EngineAdapterAttach**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_attach_fn) function.<br/>                                                                                                                     |
| WbioEngineCheckForDuplicate<br/>             | Calls the [**EngineAdapterCheckForDuplicate**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_check_for_duplicate_fn) function.<br/>                                                                                               |
| WbioEngineClearContext<br/>                  | Calls the [**EngineAdapterClearContext**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_clear_context_fn) function.<br/>                                                                                                         |
| WbioEngineCommitEnrollment<br/>              | Calls the [**EngineAdapterCommitEnrollment**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_commit_enrollment_fn) function.<br/>                                                                                                 |
| WbioEngineControlUnit<br/>                   | Calls the [**EngineAdapterControlUnit**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_control_unit_fn) function.<br/>                                                                                                           |
| WbioEngineControlUnitPrivileged<br/>         | Calls the [**EngineAdapterControlUnitPrivileged**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_control_unit_privileged_fn) function.<br/>                                                                                       |
| WbioEngineCreateEnrollment<br/>              | Calls the [**EngineAdapterCreateEnrollment**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_create_enrollment_fn) function.<br/>                                                                                                 |
| WbioEngineDeactivate<br/>                    | Calls the [**EngineAdapterDeactivate**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_deactivate_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                                       |
| WbioEngineDetach<br/>                        | Calls the [**EngineAdapterDetach**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_detach_fn) function.<br/>                                                                                                                     |
| WbioEngineDiscardEnrollment<br/>             | Calls the [**EngineAdapterDiscardEnrollment**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_discard_enrollment_fn) function.<br/>                                                                                               |
| WbioEngineExportEngineData<br/>              | Calls the [**EngineAdapterExportEngineData**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_export_engine_data_fn) function.<br/>                                                                                                 |
| WbioEngineGetEnrollmentHash<br/>             | Calls the [**EngineAdapterGetEnrollmentHash**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_get_enrollment_hash_fn) function.<br/>                                                                                               |
| WbioEngineGetEnrollmentStatus<br/>           | Calls the [**EngineAdapterGetEnrollmentStatus**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_get_enrollment_status_fn) function.<br/>                                                                                           |
| WbioEngineIdentifyAll<br/>                   | Calls the [**EngineAdapterIdentifyAll**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_identify_all_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                                     |
| WbioEngineIdentifyFeatureSet<br/>            | Calls the [**EngineAdapterIdentifyFeatureSet**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_identify_feature_set_fn) function.<br/>                                                                                             |
| WbioEngineNotifyPowerChange<br/>             | Calls the [*EngineAdapterNotifyPowerChange*](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_notify_power_change_fn) function.<br/> This wrapper function is supported starting in Windows 8.<br/>                            |
| WbioEnginePipelineCleanup<br/>               | Calls the [**EngineAdapterPipelineCleanup**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_pipeline_cleanup_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                             |
| WbioEnginePipelineInit<br/>                  | Calls the [**EngineAdapterPipelineInit**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_pipeline_init_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                                   |
| WbioEngineQueryCalibrationData<br/>          | Calls the [**EngineAdapterQueryCalibrationData**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_query_calibration_data_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                   |
| WbioEngineQueryExtendedEnrollmentStatus<br/> | Calls the [**EngineAdapterQueryExtendedEnrollmentStatus**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_query_extended_enrollment_status_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/> |
| WbioEngineQueryExtendedInfo<br/>             | Calls the [**EngineAdapterQueryExtendedInfo**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_query_extended_info_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                         |
| WbioEngineQueryHashAlgorithms<br/>           | Calls the [**EngineAdapterQueryHashAlgorithms**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_query_hash_algorithms_fn) function.<br/>                                                                                           |
| WbioEngineQueryIndexVectorSize<br/>          | Calls the [**EngineAdapterQueryIndexVectorSize**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_query_index_vector_size_fn) function.<br/>                                                                                         |
| WbioEngineQueryPreferredFormat<br/>          | Calls the [**EngineAdapterQueryPreferredFormat**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_query_preferred_format_fn) function.<br/>                                                                                         |
| WbioEngineQuerySampleHint<br/>               | Calls the [**EngineAdapterQuerySampleHint**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_query_sample_hint_fn) function.<br/>                                                                                                   |
| WbioEngineRefreshCache<br/>                  | Calls the [**EngineAdapterRefreshCache**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_refresh_cache_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                                   |
| WbioEngineSelectCalibrationFormat<br/>       | Calls the [**EngineAdapterSelectCalibrationFormat**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_select_calibration_format_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>             |
| WbioEngineSetAccountPolicy<br/>              | Calls the [**EngineAdapterSetAccountPolicy**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_set_account_policy_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                           |
| WbioEngineSetEnrollmentParameters<br/>       | Calls the [**EngineAdapterSetEnrollmentParameters**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_set_enrollment_parameters_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>             |
| WbioEngineSetEnrollmentSelector<br/>         | Calls the [**EngineAdapterSetEnrollmentSelector**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_set_enrollment_selector_fn) function.<br/> This wrapper function is supported starting in Windows 10.<br/>                 |
| WbioEngineSetHashAlgorithm<br/>              | Calls the [**EngineAdapterSetHashAlgorithm**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_set_hash_algorithm_fn) function.<br/>                                                                                                 |
| WbioEngineUpdateEnrollment<br/>              | Calls the [**EngineAdapterUpdateEnrollment**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_update_enrollment_fn) function.<br/>                                                                                                 |
| WbioEngineVerifyFeatureSet<br/>              | Calls the [**EngineAdapterVerifyFeatureSet**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_verify_feature_set_fn) function.<br/>                                                                                                 |



 

## Related topics

<dl> <dt>

[Engine Adapter Functions](engine-adapter-functions.md)
</dt> <dt>

[Plug-in Functions](plug-in-functions.md)
</dt> </dl>

 

 





