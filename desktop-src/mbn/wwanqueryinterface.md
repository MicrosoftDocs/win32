---
Description: The WwanQueryInterface function queries the mobile broadband service for info about a mobile broadband interface.
ms.assetid: DA1BC1DC-ACC2-4677-95A6-C87D757578BB
title: WwanQueryInterface function
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WwanQueryInterface
api_type: 
- DllExport
api_location: 
- WwApi.dll
- Ext-MS-Win-WWAN-WwAPI-l1-1-0.dll
- Ext-MS-Win-WWAN-WwAPI-l1-1-1.dll
---

# WwanQueryInterface function

The **WwanQueryInterface** function queries the mobile broadband service for info about a [mobile broadband interface](mobile-broadband-networks-api-interfaces.md).

> [!Note]  
> The **WwanQueryInterface** function may be altered or unavailable for releases after Windows 8.1. Instead, use the [mobile broadband interfaces](mobile-broadband-networks-api-interfaces.md).

 

## Syntax


```C++
DWORD WwanQueryInterface(
  _In_             HANDLE           hClientHandle,
  _In_       const GUID             *pInterfaceGuid,
  _In_             WWAN_INTF_OPCODE opCode,
  _Reserved_       VOID             *pReserved,
  _Out_            DWORD            *pdwDataSize,
  _Out_            BYTE             **ppData,
  _Out_            ULONG            *pRequestId,
  _Out_            WWAN_STATUS      *pStatus
);
```



## Parameters

<dl> <dt>

*hClientHandle* \[in\]
</dt> <dd>

The client's session handle that was obtained by a previous call to the [**WwanOpenHandle**](wwanopenhandle.md) function.

</dd> <dt>

*pInterfaceGuid* \[in\]
</dt> <dd>

A pointer to the **GUID** of the interface to be queried.

</dd> <dt>

*opCode* \[in\]
</dt> <dd>

The wireless wide area network (WWAN) interface operational code to query about. Only this value is valid:



| Value                                                                                                                                                                                                                                                        | Meaning                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| <span id="WwanIntfOpcodeInterfaceObject"></span><span id="wwanintfopcodeinterfaceobject"></span><span id="WWANINTFOPCODEINTERFACEOBJECT"></span><dl> <dt>**WwanIntfOpcodeInterfaceObject**</dt> </dl> | Returns interface info.<br/> |



 

</dd> <dt>

*pReserved* 
</dt> <dd>

Reserved for future use. This pointer must be **NULL**.

</dd> <dt>

*pdwDataSize* \[out\]
</dt> <dd>

A pointer to a variable that receives a 32-bit value that specifies the size of the data returned.

</dd> <dt>

*ppData* \[out\]
</dt> <dd>

A pointer to a memory block that receives a pointer to the data returned.

</dd> <dt>

*pRequestId* \[out\]
</dt> <dd>

A pointer to a variable that receives a request ID for the query.

</dd> <dt>

*pStatus* \[out\]
</dt> <dd>

A pointer to a variable that receives a status value for the query operation. Here are possible values.

<dl> <dt>

<span id="WWAN_STATUS_SUCCESS"></span><span id="wwan_status_success"></span>**WWAN\_STATUS\_SUCCESS** (STATUS\_SUCCESS)
</dt> <dt>

<span id="WWAN_STATUS_BUSY"></span><span id="wwan_status_busy"></span>**WWAN\_STATUS\_BUSY** (0xC0040002)
</dt> <dt>

<span id="WWAN_STATUS_FAILURE"></span><span id="wwan_status_failure"></span>**WWAN\_STATUS\_FAILURE** (0xC0040003)
</dt> <dt>

<span id="WWAN_STATUS_SIM_NOT_INSERTED"></span><span id="wwan_status_sim_not_inserted"></span>**WWAN\_STATUS\_SIM\_NOT\_INSERTED** (0xC0040004)
</dt> <dt>

<span id="WWAN_STATUS_BAD_SIM"></span><span id="wwan_status_bad_sim"></span>**WWAN\_STATUS\_BAD\_SIM** (0xC0040005)
</dt> <dt>

<span id="WWAN_STATUS_PIN_REQUIRED"></span><span id="wwan_status_pin_required"></span>**WWAN\_STATUS\_PIN\_REQUIRED** (0xC0040006)
</dt> <dt>

<span id="WWAN_STATUS_PIN_DISABLED"></span><span id="wwan_status_pin_disabled"></span>**WWAN\_STATUS\_PIN\_DISABLED** (0xC0040007)
</dt> <dt>

<span id="WWAN_STATUS_NOT_REGISTERED"></span><span id="wwan_status_not_registered"></span>**WWAN\_STATUS\_NOT\_REGISTERED** (0xC0040008)
</dt> <dt>

<span id="WWAN_STATUS_PROVIDERS_NOT_FOUND"></span><span id="wwan_status_providers_not_found"></span>**WWAN\_STATUS\_PROVIDERS\_NOT\_FOUND** (0xC0040009)
</dt> <dt>

<span id="WWAN_STATUS_NO_DEVICE_SUPPORT"></span><span id="wwan_status_no_device_support"></span>**WWAN\_STATUS\_NO\_DEVICE\_SUPPORT** (0xC004000a)
</dt> <dt>

<span id="WWAN_STATUS_PROVIDER_NOT_VISIBLE"></span><span id="wwan_status_provider_not_visible"></span>**WWAN\_STATUS\_PROVIDER\_NOT\_VISIBLE** (0xC004000b)
</dt> <dt>

<span id="WWAN_STATUS_DATA_CLASS_NOT_AVAILABLE"></span><span id="wwan_status_data_class_not_available"></span>**WWAN\_STATUS\_DATA\_CLASS\_NOT\_AVAILABLE** (0xC004000c)
</dt> <dt>

<span id="WWAN_STATUS_PACKET_SVC_DETACHED"></span><span id="wwan_status_packet_svc_detached"></span>**WWAN\_STATUS\_PACKET\_SVC\_DETACHED** (0xC004000d)
</dt> <dt>

<span id="WWAN_STATUS_MAX_ACTIVATED_CONTEXTS"></span><span id="wwan_status_max_activated_contexts"></span>**WWAN\_STATUS\_MAX\_ACTIVATED\_CONTEXTS** (0xC004000e)
</dt> <dt>

<span id="WWAN_STATUS_NOT_INITIALIZED"></span><span id="wwan_status_not_initialized"></span>**WWAN\_STATUS\_NOT\_INITIALIZED** (0xC004000f)
</dt> <dt>

<span id="WWAN_STATUS_VOICE_CALL_IN_PROGRESS"></span><span id="wwan_status_voice_call_in_progress"></span>**WWAN\_STATUS\_VOICE\_CALL\_IN\_PROGRESS** (0xC0040010)
</dt> <dt>

<span id="WWAN_STATUS_CONTEXT_NOT_ACTIVATED"></span><span id="wwan_status_context_not_activated"></span>**WWAN\_STATUS\_CONTEXT\_NOT\_ACTIVATED** (0xC0040011)
</dt> <dt>

<span id="WWAN_STATUS_SERVICE_NOT_ACTIVATED"></span><span id="wwan_status_service_not_activated"></span>**WWAN\_STATUS\_SERVICE\_NOT\_ACTIVATED** (0xC0040012)
</dt> <dt>

<span id="WWAN_STATUS_INVALID_ACCESS_STRING"></span><span id="wwan_status_invalid_access_string"></span>**WWAN\_STATUS\_INVALID\_ACCESS\_STRING** (0xC0040013)
</dt> <dt>

<span id="WWAN_STATUS_INVALID_USER_NAME_PWD"></span><span id="wwan_status_invalid_user_name_pwd"></span>**WWAN\_STATUS\_INVALID\_USER\_NAME\_PWD** (0xC0040014)
</dt> <dt>

<span id="WWAN_STATUS_RADIO_POWER_OFF"></span><span id="wwan_status_radio_power_off"></span>**WWAN\_STATUS\_RADIO\_POWER\_OFF** (0xC0040015)
</dt> <dt>

<span id="WWAN_STATUS_INVALID_PARAMETERS"></span><span id="wwan_status_invalid_parameters"></span>**WWAN\_STATUS\_INVALID\_PARAMETERS** (0xC0040016)
</dt> <dt>

<span id="WWAN_STATUS_READ_FAILURE"></span><span id="wwan_status_read_failure"></span>**WWAN\_STATUS\_READ\_FAILURE** (0xC0040017)
</dt> <dt>

<span id="WWAN_STATUS_WRITE_FAILURE"></span><span id="wwan_status_write_failure"></span>**WWAN\_STATUS\_WRITE\_FAILURE** (0xC0040018)
</dt> <dt>

<span id="WWAN_STATUS_DENIED_POLICY"></span><span id="wwan_status_denied_policy"></span>**WWAN\_STATUS\_DENIED\_POLICY** (0xC0040019)
</dt> <dt>

<span id="WWAN_STATUS_INVALID_DEVICE_SERVICE_OPERATION"></span><span id="wwan_status_invalid_device_service_operation"></span>**WWAN\_STATUS\_INVALID\_DEVICE\_SERVICE\_OPERATION** (0xC004001a)
</dt> <dt>

<span id="WWAN_STATUS_MORE_DATA"></span><span id="wwan_status_more_data"></span>**WWAN\_STATUS\_MORE\_DATA** (0xC004001b)
</dt> </dl> </dd> </dl>

## Return value

Returns **ERROR\_SUCCESS** if the operation was successful; otherwise, an error value.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | None supported<br/>                                                            |
| DLL<br/>                      | <dl> <dt>WwApi.dll</dt> </dl> |



 

 




