---
Description: Returns the global protection level for a specified protection mechanism.
ms.assetid: 3dd4f6f0-2305-4470-bbd4-7737fa2d8eae
title: OPM\_GET\_ACTUAL\_PROTECTION\_LEVEL
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# OPM\_GET\_ACTUAL\_PROTECTION\_LEVEL

Returns the global protection level for a specified protection mechanism.



|              |                                                                                                                                                                           |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Request GUID | OPM\_GET\_ACTUAL\_PROTECTION\_LEVEL                                                                                                                                       |
| Input data   | The protection mechanism to query, specified as a 32-bit integer. The value is interpreted as a member of the [OPM Protection Type Flags](opm-protection-type-flags.md). |
| Return data  | An [**OPM\_STANDARD\_INFORMATION**](/windows/win32/ksopmapi/ns-ksopmapi-_opm_standard_information?branch=master) structure                                                                                               |



 

## Remarks

The global protection level is the protection level that is currently being applied on the connector, regardless of how the graphics driver was instructed to apply the protection. For example, an application can set the ACP protection level by calling the **ChangeDisplaySettingsEx** function. In that case, the global protection level would reflect this setting, even though it was not requested through Output Protection Manager (OPM).

The protection level is returned in the **ulInformation** member of the [**OPM\_STANDARD\_INFORMATION**](/windows/win32/ksopmapi/ns-ksopmapi-_opm_standard_information?branch=master) structure. The meaning of this value depends on the protection mechanism that is queried. For each protection mechanism, the value of **ulInformation** is a flag from a different enumeration, as shown in the following table.



| Protection mechanism | Enumeration                                                       |
|----------------------|-------------------------------------------------------------------|
| ACP                  | [**OPM\_ACP\_PROTECTION\_LEVEL**](/windows/win32/opmapi/ne-opmapi-_opm_acp_protection_level?branch=master)   |
| CGMS-A               | [CGMS-A Protection Flags](cgms-a-protection-flags.md)            |
| DPCP                 | [**OPM\_DPCP\_PROTECTION\_LEVEL**](/windows/win32/opmapi/ne-opmapi-_opm_dpcp_protection_level?branch=master) |
| HDCP                 | [**OPM\_HDCP\_PROTECTION\_LEVEL**](/windows/win32/opmapi/ne-opmapi-_opm_hdcp_protection_level?branch=master) |



 

This query is equivalent to the DXVA\_COPPQueryGlobalProtectionLevel query used in Certified Output Protection Protocol (COPP).

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Opmapi.h</dt> </dl> |



## See also

<dl> <dt>

[**IOPMVideoOutput::COPPCompatibleGetInformation**](/windows/win32/opmapi/nf-opmapi-iopmvideooutput-coppcompatiblegetinformation?branch=master)
</dt> <dt>

[**IOPMVideoOutput::GetInformation**](/windows/win32/opmapi/nf-opmapi-iopmvideooutput-getinformation?branch=master)
</dt> <dt>

[OPM Status Requests](opm-status-requests.md)
</dt> </dl>

 

 




