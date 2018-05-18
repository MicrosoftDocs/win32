---
Description: 'Returns the virtual protection level for a specified protection mechanism.'
ms.assetid: '635d54de-2735-4390-8bac-ba63b9503909'
title: 'OPM\_GET\_VIRTUAL\_PROTECTION\_LEVEL'
---

# OPM\_GET\_VIRTUAL\_PROTECTION\_LEVEL

Returns the virtual protection level for a specified protection mechanism.

The *virtual* protection level is the level requested by the application during the current Output Protection Manager (OPM) session. The driver might apply a higher level, due to events outside of this OPM session. To find the actual protection level that is in effect, send the [**OPM\_GET\_ACTUAL\_PROTECTION\_LEVEL**](opm-get-actual-protection-level.md) query.



|              |                                                                                                                                                                               |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Request GUID | OPM\_GET\_VIRTUAL\_PROTECTION\_LEVEL                                                                                                                                          |
| Input data   | The protection mechanism to query, specified as a 32-bit integer. The value is interpreted as a member of the [**OPM Protection Type Flags**](opm-protection-type-flags.md). |
| Return data  | An [**OPM\_STANDARD\_INFORMATION**](opm-standard-information.md) structure                                                                                                   |



 

## Remarks

The protection level is returned in the **ulInformation** member of the [**OPM\_STANDARD\_INFORMATION**](opm-standard-information.md) structure. The meaning of this value depends on the protection mechanism that is queried. For each protection mechanism, the value of **ulInformation** is a flag from a different enumeration, as shown in the following table.



| Protection mechanism | Enumeration                                                       |
|----------------------|-------------------------------------------------------------------|
| ACP                  | [**OPM\_ACP\_PROTECTION\_LEVEL**](opm-acp-protection-level.md)   |
| CGMS-A               | [**CGMS-A Protection Flags**](cgms-a-protection-flags.md)        |
| DPCP                 | [**OPM\_DPCP\_PROTECTION\_LEVEL**](opm-dpcp-protection-level.md) |
| HDCP                 | [**OPM\_HDCP\_PROTECTION\_LEVEL**](opm-hdcp-protection-level.md) |



 

This query is equivalent to the DXVA\_COPPQueryLocalProtectionLevel query used in Certified Output Protection Protocol (COPP).

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Opmapi.h</dt> </dl> |



## See also

<dl> <dt>

[**IOPMVideoOutput::COPPCompatibleGetInformation**](iopmvideooutput-iopmvideooutput--coppcompatiblegetinformation.md)
</dt> <dt>

[**IOPMVideoOutput::GetInformation**](iopmvideooutput-iopmvideooutput--getinformation.md)
</dt> <dt>

[OPM Status Requests](opm-status-requests.md)
</dt> </dl>

 

 




