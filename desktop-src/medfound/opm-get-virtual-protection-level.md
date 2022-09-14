---
description: Returns the virtual protection level for a specified protection mechanism.
ms.assetid: 635d54de-2735-4390-8bac-ba63b9503909
title: OPM_GET_VIRTUAL_PROTECTION_LEVEL (Opmapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# OPM\_GET\_VIRTUAL\_PROTECTION\_LEVEL

Returns the virtual protection level for a specified protection mechanism.

The *virtual* protection level is the level requested by the application during the current Output Protection Manager (OPM) session. The driver might apply a higher level, due to events outside of this OPM session. To find the actual protection level that is in effect, send the [**OPM\_GET\_ACTUAL\_PROTECTION\_LEVEL**](opm-get-actual-protection-level.md) query.



| Requirement | Value |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Request GUID | OPM\_GET\_VIRTUAL\_PROTECTION\_LEVEL                                                                                                                                          |
| Input data   | The protection mechanism to query, specified as a 32-bit integer. The value is interpreted as a member of the [**OPM Protection Type Flags**](opm-protection-type-flags.md). |
| Return data  | An [**OPM\_STANDARD\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_standard_information) structure                                                                                                   |



 

## Remarks

The protection level is returned in the **ulInformation** member of the [**OPM\_STANDARD\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_standard_information) structure. The meaning of this value depends on the protection mechanism that is queried. For each protection mechanism, the value of **ulInformation** is a flag from a different enumeration, as shown in the following table.



| Protection mechanism | Enumeration                                                       |
|----------------------|-------------------------------------------------------------------|
| ACP                  | [**OPM\_ACP\_PROTECTION\_LEVEL**](/windows/desktop/api/opmapi/ne-opmapi-opm_acp_protection_level)   |
| CGMS-A               | [**CGMS-A Protection Flags**](cgms-a-protection-flags.md)        |
| DPCP                 | [**OPM\_DPCP\_PROTECTION\_LEVEL**](/windows/desktop/api/opmapi/ne-opmapi-opm_dpcp_protection_level) |
| HDCP                 | [**OPM\_HDCP\_PROTECTION\_LEVEL**](/windows/desktop/api/opmapi/ne-opmapi-opm_hdcp_protection_level) |



 

This query is equivalent to the DXVA\_COPPQueryLocalProtectionLevel query used in Certified Output Protection Protocol (COPP).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Opmapi.h</dt> </dl> |



## See also

<dl> <dt>

[**IOPMVideoOutput::COPPCompatibleGetInformation**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-coppcompatiblegetinformation)
</dt> <dt>

[**IOPMVideoOutput::GetInformation**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-getinformation)
</dt> <dt>

[OPM Status Requests](opm-status-requests.md)
</dt> </dl>

 

 




