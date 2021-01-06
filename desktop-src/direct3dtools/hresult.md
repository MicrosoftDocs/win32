---
description: Custom HRESULT values for the graphics diagnostics capture interface.
MS-HAID: vspixengine.Hresult
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: Hresult enumeration
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 246FA53F-FF5B-44E1-BABB-F45AE0212687
api_name: 
 - Hresult
api_type: 
 - HeaderDef
api_location: 
 - vspixengine.h
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="vspixengine.hresult"></span>Hresult enumeration

Custom HRESULT values for the graphics diagnostics capture interface.

## Syntax


```C++
};
```

## Constants

<span id="PIX_S_OK"></span><span id="pix_s_ok"></span>**PIX\_S\_OK**  
A common HRESULT which indicates that the operation succeeded as expected.

<span id="PIX_S_FALSE"></span><span id="pix_s_false"></span>**PIX\_S\_FALSE**  
A common HRESULT which indicates that the operation succeeded, but in a different way than was expected.

<span id="PIX_ERROR_FILE_NOT_FOUND"></span><span id="pix_error_file_not_found"></span>**PIX\_ERROR\_FILE\_NOT\_FOUND**  
A custom HRESULT that echos ERROR\_FILE\_NOT\_FOUND.

<span id="PIX_ERROR_BAD_ENVIRONMENT"></span><span id="pix_error_bad_environment"></span>**PIX\_ERROR\_BAD\_ENVIRONMENT**  
A custom HRESULT that echos ERROR\_BAD\_ENVIRONMENT.

<span id="PIX_ERROR_BAD_FORMAT"></span><span id="pix_error_bad_format"></span>**PIX\_ERROR\_BAD\_FORMAT**  
A custom HRESULT that echos ERROR\_BAD\_FORMAT.

<span id="PIX_ERROR_SHARING_VIOLATION"></span><span id="pix_error_sharing_violation"></span>**PIX\_ERROR\_SHARING\_VIOLATION**  
A custom HRESULT that echos ERROR\_SHARING\_VIOLATION.

<span id="PIX_ERROR_DISK_FULL"></span><span id="pix_error_disk_full"></span>**PIX\_ERROR\_DISK\_FULL**  
A custom HRESULT that echos ERROR\_DISK\_FULL.

<span id="PIX_ERROR_MORE_DATA"></span><span id="pix_error_more_data"></span>**PIX\_ERROR\_MORE\_DATA**  
A custom HRESULT that echos ERROR\_MORE\_DATA.

<span id="PIX_E_MISSING_DEBUG_KITS_POLICY"></span><span id="pix_e_missing_debug_kits_policy"></span>**PIX\_E\_MISSING\_DEBUG\_KITS\_POLICY**  
A custom HRESULT which indicates that the Debug Kits policy is missing.

<span id="PIX_E_INVALID_VERSION"></span><span id="pix_e_invalid_version"></span>**PIX\_E\_INVALID\_VERSION**  
A custom HRESULT which indicates that an invalid version is being used.

<span id="PIX_E_USING_DCOMP"></span><span id="pix_e_using_dcomp"></span>**PIX\_E\_USING\_DCOMP**  
A custom HRESULT which indicates that DirectComposition is in use (capture of DirectComposition is not supported.)

<span id="PIX_E_USING_DIRECTWRITE"></span><span id="pix_e_using_directwrite"></span>**PIX\_E\_USING\_DIRECTWRITE**  
A custom HRESULT which indicates that DirectWrite is in use (capture of DirectWrite is not supported.)

<span id="PIX_E_USING_D3D9"></span><span id="pix_e_using_d3d9"></span>**PIX\_E\_USING\_D3D9**  
A custom HRESULT which indicates that Direct3D9 is in use (capture of Direct3D9 is not supported in Windows 10.)

<span id="PIX_E_CANT_CREATE_SHADER"></span><span id="pix_e_cant_create_shader"></span>**PIX\_E\_CANT\_CREATE\_SHADER**  
A custom HRESULT which indicates that a specified shader can't be created.

<span id="PIX_E_USING_D2D"></span><span id="pix_e_using_d2d"></span>**PIX\_E\_USING\_D2D**  
A custom HRESULT which indicates that Direct2D is in use (capture of Direct2D is not supported.)

<span id="PIX_E_NO_FRAMES"></span><span id="pix_e_no_frames"></span>**PIX\_E\_NO\_FRAMES**  
A custom HRESULT which indicates that no frames have been captured.

<span id="PIX_E_DISABLE_SPY"></span><span id="pix_e_disable_spy"></span>**PIX\_E\_DISABLE\_SPY**  

<span id="PIX_E_WIN8LOG_ON_WIN7"></span><span id="pix_e_win8log_on_win7"></span>**PIX\_E\_WIN8LOG\_ON\_WIN7**  
A custom HRESULT which indicates that a Windows 8 vsglog cannot be played back on Windows 7.

<span id="PIX_E_BUILD_SHADER_TRACE"></span><span id="pix_e_build_shader_trace"></span>**PIX\_E\_BUILD\_SHADER\_TRACE**  
A custom HRESULT which indicates that there was an error building the shader trace.

<span id="PIX_E_NO_CS_DATA_VISUALIZATION"></span><span id="pix_e_no_cs_data_visualization"></span>**PIX\_E\_NO\_CS\_DATA\_VISUALIZATION**  
A custom HRESULT which indicates that there is no compute shader data visualization.

<span id="PIX_E_MISMATCH_SDK"></span><span id="pix_e_mismatch_sdk"></span>**PIX\_E\_MISMATCH\_SDK**  
A custom HRESULT which indicates that there is a mismatch with the current SDK.

<span id="PIX_E_POSSIBLE_MISMATCH_SDK"></span><span id="pix_e_possible_mismatch_sdk"></span>**PIX\_E\_POSSIBLE\_MISMATCH\_SDK**  
A custom HRESULT which indicates that there is a possible mismatch with the current SDK.

<span id="PIX_E_UNDETECTABLE_PIXEL"></span><span id="pix_e_undetectable_pixel"></span>**PIX\_E\_UNDETECTABLE\_PIXEL**  
A custom HRESULT which indicates that there is an undetectable pixel.

<span id="PIX_E_CANT_DEBUG_SHADER_USING_SYSTEM_VALUE_SEMANTICS"></span><span id="pix_e_cant_debug_shader_using_system_value_semantics"></span>**PIX\_E\_CANT\_DEBUG\_SHADER\_USING\_SYSTEM\_VALUE\_SEMANTICS**  
A custom HRESULT which indicates that the sahder can't be debugged using system value semantics.

<span id="PIX_S_UPDATEAVAILABLE"></span><span id="pix_s_updateavailable"></span>**PIX\_S\_UPDATEAVAILABLE**  
A custom HRESULT which indicates that there is an update available.

<span id="PIX_DXGI_STATUS_NO_REDIRECTION"></span><span id="pix_dxgi_status_no_redirection"></span>**PIX\_DXGI\_STATUS\_NO\_REDIRECTION**  
A custom HRESULT that echos DXGI\_STATUS\_NO\_REDIRECTION.

<span id="PIX_DXGI_STATUS_NO_DESKTOP_ACCESS"></span><span id="pix_dxgi_status_no_desktop_access"></span>**PIX\_DXGI\_STATUS\_NO\_DESKTOP\_ACCESS**  
A custom HRESULT that echos DXGI\_STATUS\_NO\_DESKTOP\_ACCESS.

<span id="PIX_DXGI_STATUS_GRAPHICS_VIDPN_SOURCE_IN_USE"></span><span id="pix_dxgi_status_graphics_vidpn_source_in_use"></span>**PIX\_DXGI\_STATUS\_GRAPHICS\_VIDPN\_SOURCE\_IN\_USE**  
A custom HRESULT that echos DXGI\_STATUS\_GRAPHICS\_VIDPN\_SOURCE\_IN\_USE.

<span id="PIX_DXGI_STATUS_MODE_CHANGED"></span><span id="pix_dxgi_status_mode_changed"></span>**PIX\_DXGI\_STATUS\_MODE\_CHANGED**  
A custom HRESULT that echos DXGI\_STATUS\_MODE\_CHANGED.

<span id="PIX_DXGI_STATUS_MODE_CHANGE_IN_PROGRESS"></span><span id="pix_dxgi_status_mode_change_in_progress"></span>**PIX\_DXGI\_STATUS\_MODE\_CHANGE\_IN\_PROGRESS**  
A custom HRESULT that echos DXGI\_STATUS\_MODE\_CHANGE\_IN\_PROGRESS.

<span id="PIX_DXGI_STATUS_UNOCCLUDED"></span><span id="pix_dxgi_status_unoccluded"></span>**PIX\_DXGI\_STATUS\_UNOCCLUDED**  
A custom HRESULT that echos DXGI\_STATUS\_UNOCCLUDED.

<span id="PIX_DXGI_STATUS_DDA_WAS_STILL_DRAWING"></span><span id="pix_dxgi_status_dda_was_still_drawing"></span>**PIX\_DXGI\_STATUS\_DDA\_WAS\_STILL\_DRAWING**  
A custom HRESULT that echos DXGI\_STATUS\_DDA\_WAS\_STILL\_DRAWING.

<span id="PIX_E_NOTIMPL"></span><span id="pix_e_notimpl"></span>**PIX\_E\_NOTIMPL**  
A custom HRESULT that echos E\_NOTIMPL.

<span id="PIX_E_NOINTERFACE"></span><span id="pix_e_nointerface"></span>**PIX\_E\_NOINTERFACE**  
A custom HRESULT that echos E\_NOINTERFACE.

<span id="PIX_E_POINTER"></span><span id="pix_e_pointer"></span>**PIX\_E\_POINTER**  
A custom HRESULT that echos E\_POINTER.

<span id="PIX_E_ABORT"></span><span id="pix_e_abort"></span>**PIX\_E\_ABORT**  
A custom HRESULT that echos E\_ABORT.

<span id="PIX_E_FAIL"></span><span id="pix_e_fail"></span>**PIX\_E\_FAIL**  
A custom HRESULT that echos E\_FAIL.

<span id="PIX_E_UNEXPECTED"></span><span id="pix_e_unexpected"></span>**PIX\_E\_UNEXPECTED**  
A custom HRESULT that echos E\_UNEXPECTED.

<span id="PIX_E_ACCESSDENIED"></span><span id="pix_e_accessdenied"></span>**PIX\_E\_ACCESSDENIED**  
A custom HRESULT that echos E\_ACCESSDENIED.

<span id="PIX_E_HANDLE"></span><span id="pix_e_handle"></span>**PIX\_E\_HANDLE**  
A custom HRESULT that echos E\_HANDLE.

<span id="PIX_E_OUTOFMEMORY"></span><span id="pix_e_outofmemory"></span>**PIX\_E\_OUTOFMEMORY**  
A custom HRESULT that echos E\_OUTOFMEMORY.

<span id="PIX_E_INVALIDARG"></span><span id="pix_e_invalidarg"></span>**PIX\_E\_INVALIDARG**  
A custom HRESULT that echos E\_INVALIDARG.

<span id="PIX_XBOX_ERROR_DISK_FULL"></span><span id="pix_xbox_error_disk_full"></span>**PIX\_XBOX\_ERROR\_DISK\_FULL**  
A custom HRESULT which indicates that the disk is full.

<span id="PIX_WS_E_ADDRESS_IN_USE"></span><span id="pix_ws_e_address_in_use"></span>**PIX\_WS\_E\_ADDRESS\_IN\_USE**  
A custom HRESULT which indicates that the address is already in use.

<span id="PIX_WS_E_MISSING_KITS_POLICY"></span><span id="pix_ws_e_missing_kits_policy"></span>**PIX\_WS\_E\_MISSING\_KITS\_POLICY**  
A custom HRESULT which indicates that the address is not available.

<span id="PIX_TE_FAILEDTOLOADSOFTWAREMODULE"></span><span id="pix_te_failedtoloadsoftwaremodule"></span>**PIX\_TE\_FAILEDTOLOADSOFTWAREMODULE**  
A custom HRESULT which indicates that a necessary software module failed to load.

<span id="PIX_TE_USEDSOFTWAREMODULETHATWASNTWARPORREF"></span><span id="pix_te_usedsoftwaremodulethatwasntwarporref"></span>**PIX\_TE\_USEDSOFTWAREMODULETHATWASNTWARPORREF**  
A custom HRESULT which indicates that the used software module was not the WARP or REF driver.

<span id="PIX_TE_CORRUPTEDFILE"></span><span id="pix_te_corruptedfile"></span>**PIX\_TE\_CORRUPTEDFILE**  
A custom HRESULT which indicates that the file is corrupted.

<span id="PIX_TE_FAILEDTOOPENFILE"></span><span id="pix_te_failedtoopenfile"></span>**PIX\_TE\_FAILEDTOOPENFILE**  
A custom HRESULT which indicates that the file failed to open.

<span id="PIX_TE_CALLFAILEDONPLAYBACK"></span><span id="pix_te_callfailedonplayback"></span>**PIX\_TE\_CALLFAILEDONPLAYBACK**  
A custom HRESULT which indicates that a call failed during playback.

<span id="PIX_TE_UNKNOWNUUID"></span><span id="pix_te_unknownuuid"></span>**PIX\_TE\_UNKNOWNUUID**  
A custom HRESULT which indicates that an unknown UUID was encountered; this should never occur.

<span id="PIX_TE_NOTCAPTUREFILEORCORRUPTED"></span><span id="pix_te_notcapturefileorcorrupted"></span>**PIX\_TE\_NOTCAPTUREFILEORCORRUPTED**  
A custom HRESULT which indicates that the file is not a capture file or is corrupted.

<span id="PIX_TE_NEWERFILE"></span><span id="pix_te_newerfile"></span>**PIX\_TE\_NEWERFILE**  

<span id="PIX_TE_OLDERFILE"></span><span id="pix_te_olderfile"></span>**PIX\_TE\_OLDERFILE**  

<span id="PIX_TE_INVALIDMOMENT"></span><span id="pix_te_invalidmoment"></span>**PIX\_TE\_INVALIDMOMENT**  

<span id="PIX_TE_BAD_DRIVER"></span><span id="pix_te_bad_driver"></span>**PIX\_TE\_BAD\_DRIVER**  
A custom HRESULT which indicates that the driver is bad.

<span id="PIX_ERROR_CANT_ACCESS_DEPTHSTENCIL_IN_CPU"></span><span id="pix_error_cant_access_depthstencil_in_cpu"></span>**PIX\_ERROR\_CANT\_ACCESS\_DEPTHSTENCIL\_IN\_CPU**  
A custom HRESULT which indicates that the CPU attempted to access the depth-stencil buffer, resulting in an error.

<span id="PIX_ERROR_CANT_RESOLVE_MULTISAMPLED_TEXTURE"></span><span id="pix_error_cant_resolve_multisampled_texture"></span>**PIX\_ERROR\_CANT\_RESOLVE\_MULTISAMPLED\_TEXTURE**  
A custom HRESULT which indicates that there was an attempt to resolve a multi-sampled texture, resulting in an error.

<span id="PIX_DXGI_ERROR_INVALID_CALL"></span><span id="pix_dxgi_error_invalid_call"></span>**PIX\_DXGI\_ERROR\_INVALID\_CALL**  
A custom HRESULT that echos DXGI\_ERROR\_INVALID\_CALL.

<span id="PIX_DXGI_ERROR_NOT_FOUND"></span><span id="pix_dxgi_error_not_found"></span>**PIX\_DXGI\_ERROR\_NOT\_FOUND**  
A custom HRESULT that echos DXGI\_ERROR\_NOT\_FOUND.

<span id="PIX_DXGI_ERROR_MORE_DATA"></span><span id="pix_dxgi_error_more_data"></span>**PIX\_DXGI\_ERROR\_MORE\_DATA**  
A custom HRESULT that echos DXGI\_ERROR\_MORE\_DATA.

<span id="PIX_DXGI_ERROR_UNSUPPORTED"></span><span id="pix_dxgi_error_unsupported"></span>**PIX\_DXGI\_ERROR\_UNSUPPORTED**  
A custom HRESULT that echos DXGI\_ERROR\_UNSUPPORTED.

<span id="PIX_DXGI_ERROR_DEVICE_REMOVED"></span><span id="pix_dxgi_error_device_removed"></span>**PIX\_DXGI\_ERROR\_DEVICE\_REMOVED**  
A custom HRESULT that echos DXGI\_ERROR\_DEVICE\_REMOVED.

<span id="PIX_DXGI_ERROR_DEVICE_HUNG"></span><span id="pix_dxgi_error_device_hung"></span>**PIX\_DXGI\_ERROR\_DEVICE\_HUNG**  
A custom HRESULT that echos DXGI\_ERROR\_DEVICE\_HUNG.

<span id="PIX_DXGI_ERROR_DEVICE_RESET"></span><span id="pix_dxgi_error_device_reset"></span>**PIX\_DXGI\_ERROR\_DEVICE\_RESET**  
A custom HRESULT that echos DXGI\_ERROR\_DEVICE\_RESET.

<span id="PIX_DXGI_ERROR_WAS_STILL_DRAWING"></span><span id="pix_dxgi_error_was_still_drawing"></span>**PIX\_DXGI\_ERROR\_WAS\_STILL\_DRAWING**  
A custom HRESULT that echos DXGI\_ERROR\_WAS\_STILL\_DRAWING.

<span id="PIX_DXGI_ERROR_FRAME_STATISTICS_DISJOINT"></span><span id="pix_dxgi_error_frame_statistics_disjoint"></span>**PIX\_DXGI\_ERROR\_FRAME\_STATISTICS\_DISJOINT**  
A custom HRESULT that echos DXGI\_ERROR\_FRAME\_STATISTICS\_DISJOINT.

<span id="PIX_DXGI_ERROR_GRAPHICS_VIDPN_SOURCE_IN_USE"></span><span id="pix_dxgi_error_graphics_vidpn_source_in_use"></span>**PIX\_DXGI\_ERROR\_GRAPHICS\_VIDPN\_SOURCE\_IN\_USE**  
A custom HRESULT that echos DXGI\_ERROR\_GRAPHICS\_VIDPN\_SOURCE\_IN\_USE.

<span id="PIX_DXGI_ERROR_DRIVER_INTERNAL_ERROR"></span><span id="pix_dxgi_error_driver_internal_error"></span>**PIX\_DXGI\_ERROR\_DRIVER\_INTERNAL\_ERROR**  
A custom HRESULT that echos DXGI\_ERROR\_DRIVER\_INTERNAL\_ERROR.

<span id="PIX_DXGI_ERROR_NONEXCLUSIVE"></span><span id="pix_dxgi_error_nonexclusive"></span>**PIX\_DXGI\_ERROR\_NONEXCLUSIVE**  
A custom HRESULT that echos DXGI\_ERROR\_NONEXCLUSIVE.

<span id="PIX_DXGI_ERROR_NOT_CURRENTLY_AVAILABLE"></span><span id="pix_dxgi_error_not_currently_available"></span>**PIX\_DXGI\_ERROR\_NOT\_CURRENTLY\_AVAILABLE**  
A custom HRESULT that echos DXGI\_ERROR\_NOT\_CURRENTLY\_AVAILABLE.

<span id="PIX_DXGI_ERROR_REMOTE_CLIENT_DISCONNECTED"></span><span id="pix_dxgi_error_remote_client_disconnected"></span>**PIX\_DXGI\_ERROR\_REMOTE\_CLIENT\_DISCONNECTED**  
A custom HRESULT that echos DXGI\_ERROR\_REMOTE\_CLIENT\_DISCONNECTED.

<span id="PIX_DXGI_ERROR_REMOTE_OUTOFMEMORY"></span><span id="pix_dxgi_error_remote_outofmemory"></span>**PIX\_DXGI\_ERROR\_REMOTE\_OUTOFMEMORY**  
A custom HRESULT that echos DXGI\_ERROR\_REMOTE\_OUTOFMEMORY.

<span id="PIX_DXGI_ERROR_MODE_CHANGE_IN_PROGRESS"></span><span id="pix_dxgi_error_mode_change_in_progress"></span>**PIX\_DXGI\_ERROR\_MODE\_CHANGE\_IN\_PROGRESS**  
A custom HRESULT that echos DXGI\_ERROR\_MODE\_CHANGE\_IN\_PROGRESS.

<span id="PIX_DXGI_ERROR_ACCESS_LOST"></span><span id="pix_dxgi_error_access_lost"></span>**PIX\_DXGI\_ERROR\_ACCESS\_LOST**  
A custom HRESULT that echos DXGI\_ERROR\_ACCESS\_LOST.

<span id="PIX_DXGI_ERROR_WAIT_TIMEOUT"></span><span id="pix_dxgi_error_wait_timeout"></span>**PIX\_DXGI\_ERROR\_WAIT\_TIMEOUT**  
A custom HRESULT that echos DXGI\_ERROR\_WAIT\_TIMEOUT.

<span id="PIX_DXGI_ERROR_SESSION_DISCONNECTED"></span><span id="pix_dxgi_error_session_disconnected"></span>**PIX\_DXGI\_ERROR\_SESSION\_DISCONNECTED**  
A custom HRESULT that echos DXGI\_ERROR\_SESSION\_DISCONNECTED.

<span id="PIX_DXGI_ERROR_RESTRICT_TO_OUTPUT_STALE"></span><span id="pix_dxgi_error_restrict_to_output_stale"></span>**PIX\_DXGI\_ERROR\_RESTRICT\_TO\_OUTPUT\_STALE**  
A custom HRESULT that echos DXGI\_ERROR\_RESTRICT\_TO\_OUTPUT\_STALE.

<span id="PIX_DXGI_ERROR_CANNOT_PROTECT_CONTENT"></span><span id="pix_dxgi_error_cannot_protect_content"></span>**PIX\_DXGI\_ERROR\_CANNOT\_PROTECT\_CONTENT**  
A custom HRESULT that echos DXGI\_ERROR\_CANNOT\_PROTECT\_CONTENT.

<span id="PIX_DXGI_ERROR_ACCESS_DENIED"></span><span id="pix_dxgi_error_access_denied"></span>**PIX\_DXGI\_ERROR\_ACCESS\_DENIED**  
A custom HRESULT that echos DXGI\_ERROR\_ACCESS\_DENIED.

<span id="PIX_DXGI_ERROR_NAME_ALREADY_EXISTS"></span><span id="pix_dxgi_error_name_already_exists"></span>**PIX\_DXGI\_ERROR\_NAME\_ALREADY\_EXISTS**  
A custom HRESULT that echos DXGI\_ERROR\_NAME\_ALREADY\_EXISTS.

<span id="PIX_DXGI_ERROR_SDK_COMPONENT_MISSING"></span><span id="pix_dxgi_error_sdk_component_missing"></span>**PIX\_DXGI\_ERROR\_SDK\_COMPONENT\_MISSING**  
A custom HRESULT that echos DXGI\_ERROR\_SDK\_COMPONENT\_MISSING.

<span id="PIX_DXGI_DDI_ERR_WASSTILLDRAWING"></span><span id="pix_dxgi_ddi_err_wasstilldrawing"></span>**PIX\_DXGI\_DDI\_ERR\_WASSTILLDRAWING**  
A custom HRESULT that echos DXGI\_DDI\_ERR\_WASSTILLDRAWING.

<span id="PIX_DXGI_DDI_ERR_UNSUPPORTED"></span><span id="pix_dxgi_ddi_err_unsupported"></span>**PIX\_DXGI\_DDI\_ERR\_UNSUPPORTED**  
A custom HRESULT that echos DXGI\_DDI\_ERR\_UNSUPPORTED.

<span id="PIX_DXGI_DDI_ERR_NONEXCLUSIVE"></span><span id="pix_dxgi_ddi_err_nonexclusive"></span>**PIX\_DXGI\_DDI\_ERR\_NONEXCLUSIVE**  
A custom HRESULT that echos DXGI\_DDI\_ERR\_NONEXCLUSIVE.

<span id="PIX_D3D10_ERROR_TOO_MANY_UNIQUE_STATE_OBJECTS"></span><span id="pix_d3d10_error_too_many_unique_state_objects"></span>**PIX\_D3D10\_ERROR\_TOO\_MANY\_UNIQUE\_STATE\_OBJECTS**  
A custom HRESULT that echos D3D10\_ERROR\_TOO\_MANY\_UNIQUE\_STATE\_OBJECTS.

<span id="PIX_D3D10_ERROR_FILE_NOT_FOUND"></span><span id="pix_d3d10_error_file_not_found"></span>**PIX\_D3D10\_ERROR\_FILE\_NOT\_FOUND**  
A custom HRESULT that echos D3D10\_ERROR\_FILE\_NOT\_FOUND.

<span id="PIX_D3D11_ERROR_TOO_MANY_UNIQUE_STATE_OBJECTS"></span><span id="pix_d3d11_error_too_many_unique_state_objects"></span>**PIX\_D3D11\_ERROR\_TOO\_MANY\_UNIQUE\_STATE\_OBJECTS**  
A custom HRESULT that echos D3D11\_ERROR\_TOO\_MANY\_UNIQUE\_STATE\_OBJECTS.

<span id="PIX_D3D11_ERROR_FILE_NOT_FOUND"></span><span id="pix_d3d11_error_file_not_found"></span>**PIX\_D3D11\_ERROR\_FILE\_NOT\_FOUND**  
A custom HRESULT that echos D3D11\_ERROR\_FILE\_NOT\_FOUND.

<span id="PIX_D3D11_ERROR_TOO_MANY_UNIQUE_VIEW_OBJECTS"></span><span id="pix_d3d11_error_too_many_unique_view_objects"></span>**PIX\_D3D11\_ERROR\_TOO\_MANY\_UNIQUE\_VIEW\_OBJECTS**  
A custom HRESULT that echos D3D11\_ERROR\_TOO\_MANY\_UNIQUE\_VIEW\_OBJECTS.

<span id="PIX_D3D11_ERROR_DEFERRED_CONTEXT_MAP_WITHOUT_INITIAL_DISCARD"></span><span id="pix_d3d11_error_deferred_context_map_without_initial_discard"></span>**PIX\_D3D11\_ERROR\_DEFERRED\_CONTEXT\_MAP\_WITHOUT\_INITIAL\_DISCARD**  
A custom HRESULT that echos D3D11\_ERROR\_DEFERRED\_CONTEXT\_MAP\_WITHOUT\_INITIAL\_DISCARD.

<span id="PIX_ERROR_OCCLUDED_DRAW_CALL"></span><span id="pix_error_occluded_draw_call"></span>**PIX\_ERROR\_OCCLUDED\_DRAW\_CALL**  
A custom HRESULT which indicates that a draw call was entirely occluded, resulting in an error.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

 

 



