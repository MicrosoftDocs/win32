---
title: NAP Error Constants (WinError.h)
description: The following NAP error constants are defined in WinError.h.
ms.assetid: b2fba990-75d9-4153-8058-c01e97700d00
topic_type:
- apiref
api_name:
- NAP_E_INVALID_PACKET
- NAP_E_MISSING_SOH
- NAP_E_CONFLICTING_ID
- NAP_E_NO_CACHED_SOH
- NAP_E_STILL_BOUND
- NAP_E_NOT_REGISTERED
- NAP_E_NOT_INITIALIZED
- NAP_E_MISMATCHED_ID
- NAP_E_NOT_PENDING
- NAP_E_ID_NOT_FOUND
- NAP_E_MAXSIZE_TOO_SMALL
- NAP_E_SERVICE_NOT_RUNNING
- NAP_S_CERT_ALREADY_PRESENT
- NAP_E_ENTITY_DISABLED
- NAP_E_NETSH_GROUPPOLICY_ERROR
- NAP_E_TOO_MANY_CALLS
- NAP_E_SHV_CONFIG_EXISTED
- NAP_E_SHV_CONFIG_NOT_FOUND
- NAP_E_SHV_TIMEOUT
api_location:
- WinError.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# NAP Error Constants

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The following NAP error constants are defined in WinError.h.

<dl> <dt>

<span id="NAP_E_INVALID_PACKET"></span><span id="nap_e_invalid_packet"></span>**NAP\_E\_INVALID\_PACKET**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80270001L)
</dt> <dt>



The NAP [**SoH**](/windows/win32/api/naptypes/ns-naptypes-soh) packet is invalid.


</dt> </dl> </dd> <dt>

<span id="NAP_E_MISSING_SOH"></span><span id="nap_e_missing_soh"></span>**NAP\_E\_MISSING\_SOH**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80270002L)
</dt> <dt>



An [**SoH**](/windows/win32/api/naptypes/ns-naptypes-soh) was missing from the NAP packet.


</dt> </dl> </dd> <dt>

<span id="NAP_E_CONFLICTING_ID"></span><span id="nap_e_conflicting_id"></span>**NAP\_E\_CONFLICTING\_ID**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80270003L)
</dt> <dt>



The entity ID conflicts with an already-registered entity ID.


</dt> </dl> </dd> <dt>

<span id="NAP_E_NO_CACHED_SOH"></span><span id="nap_e_no_cached_soh"></span>**NAP\_E\_NO\_CACHED\_SOH**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80270004L)
</dt> <dt>



No cached [**SoH**](/windows/win32/api/naptypes/ns-naptypes-soh) is present.


</dt> </dl> </dd> <dt>

<span id="NAP_E_STILL_BOUND"></span><span id="nap_e_still_bound"></span>**NAP\_E\_STILL\_BOUND**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80270005L)
</dt> <dt>



The entity is still bound to the NAP system.


</dt> </dl> </dd> <dt>

<span id="NAP_E_NOT_REGISTERED"></span><span id="nap_e_not_registered"></span>**NAP\_E\_NOT\_REGISTERED**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80270006L)
</dt> <dt>



The entity is not registered with the NAP system.


</dt> </dl> </dd> <dt>

<span id="NAP_E_NOT_INITIALIZED"></span><span id="nap_e_not_initialized"></span>**NAP\_E\_NOT\_INITIALIZED**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80270007L)
</dt> <dt>



The entity is not initialized with the NAP system.


</dt> </dl> </dd> <dt>

<span id="NAP_E_MISMATCHED_ID"></span><span id="nap_e_mismatched_id"></span>**NAP\_E\_MISMATCHED\_ID**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80270008L)
</dt> <dt>



The correlation IDs in the [**SoH**](/windows/win32/api/naptypes/ns-naptypes-soh) request and **SoH** response do not match up.


</dt> </dl> </dd> <dt>

<span id="NAP_E_NOT_PENDING"></span><span id="nap_e_not_pending"></span>**NAP\_E\_NOT\_PENDING**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80270009L)
</dt> <dt>



Completion was indicated on a request that is not currently pending.


</dt> </dl> </dd> <dt>

<span id="NAP_E_ID_NOT_FOUND"></span><span id="nap_e_id_not_found"></span>**NAP\_E\_ID\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x8027000AL)
</dt> <dt>



The NAP component's ID was not found.


</dt> </dl> </dd> <dt>

<span id="NAP_E_MAXSIZE_TOO_SMALL"></span><span id="nap_e_maxsize_too_small"></span>**NAP\_E\_MAXSIZE\_TOO\_SMALL**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x8027000BL)
</dt> <dt>



The maximum size of the connection is too small for an SoH packet.


</dt> </dl> </dd> <dt>

<span id="NAP_E_SERVICE_NOT_RUNNING"></span><span id="nap_e_service_not_running"></span>**NAP\_E\_SERVICE\_NOT\_RUNNING**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x8027000CL)
</dt> <dt>



The NapAgent service is not running.


</dt> </dl> </dd> <dt>

<span id="NAP_S_CERT_ALREADY_PRESENT"></span><span id="nap_s_cert_already_present"></span>**NAP\_S\_CERT\_ALREADY\_PRESENT**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x0027000DL) 
</dt> <dt>



A certificate is already present in the certificate store.


</dt> </dl> </dd> <dt>

<span id="NAP_E_ENTITY_DISABLED"></span><span id="nap_e_entity_disabled"></span>**NAP\_E\_ENTITY\_DISABLED**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x8027000EL)
</dt> <dt>



The entity is disabled with the NapAgent service.


</dt> </dl> </dd> <dt>

<span id="NAP_E_NETSH_GROUPPOLICY_ERROR"></span><span id="nap_e_netsh_grouppolicy_error"></span>**NAP\_E\_NETSH\_GROUPPOLICY\_ERROR**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x8027000FL)
</dt> <dt>



Group Policy is not configured.


</dt> </dl> </dd> <dt>

<span id="NAP_E_TOO_MANY_CALLS"></span><span id="nap_e_too_many_calls"></span>**NAP\_E\_TOO\_MANY\_CALLS**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80270010L)
</dt> <dt>



Too many simultaneous calls.


</dt> </dl> </dd> <dt>

<span id="NAP_E_SHV_CONFIG_EXISTED"></span><span id="nap_e_shv_config_existed"></span>**NAP\_E\_SHV\_CONFIG\_EXISTED**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80270011L)
</dt> <dt>



SHV configuration already exists.

> [!Note]  
> Supported in Windows 7 or later.

 


</dt> </dl> </dd> <dt>

<span id="NAP_E_SHV_CONFIG_NOT_FOUND"></span><span id="nap_e_shv_config_not_found"></span>**NAP\_E\_SHV\_CONFIG\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80270012L)
</dt> <dt>



SHV configuration is not found.

> [!Note]  
> Supported in Windows 7 or later.

 


</dt> </dl> </dd> <dt>

<span id="NAP_E_SHV_TIMEOUT"></span><span id="nap_e_shv_timeout"></span>**NAP\_E\_SHV\_TIMEOUT**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80270013L)
</dt> <dt>



SHV timed out on the request.

> [!Note]  
> Supported in Windows 7 or later.

 


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>WinError.h</dt> </dl> |



## See also

<dl> <dt>

[**NAP Constants**](nap-constants.md)
</dt> </dl>

 

 





