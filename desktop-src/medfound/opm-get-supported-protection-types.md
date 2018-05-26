---
Description: Returns the list of protection mechanisms that are supported by the connector.
ms.assetid: dd4cdd3c-6bb5-4427-827d-f3e909e752e5
title: OPM\_GET\_SUPPORTED\_PROTECTION\_TYPES
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# OPM\_GET\_SUPPORTED\_PROTECTION\_TYPES

Returns the list of protection mechanisms that are supported by the connector.



|              |                                                                             |
|--------------|-----------------------------------------------------------------------------|
| Request GUID | OPM\_GET\_SUPPORTED\_PROTECTION\_TYPES                                      |
| Input data   | None                                                                        |
| Return data  | An [**OPM\_STANDARD\_INFORMATION**](/windows/win32/ksopmapi/ns-ksopmapi-_opm_standard_information?branch=master) structure |



 

## Remarks

The protection mechanisms are returned in the **ulInformation** member of the [**OPM\_STANDARD\_INFORMATION**](/windows/win32/ksopmapi/ns-ksopmapi-_opm_standard_information?branch=master) structure. The value is a bitwise **OR** of [OPM Protection Type Flags](opm-protection-type-flags.md).

This query is equivalent to the DXVA\_COPPQueryProtectionType query used in Certified Output Protection Protocol (COPP).

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

 

 




