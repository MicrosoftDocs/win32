---
Description: 'Returns the list of protection mechanisms that are supported by the connector.'
ms.assetid: 'dd4cdd3c-6bb5-4427-827d-f3e909e752e5'
title: 'OPM\_GET\_SUPPORTED\_PROTECTION\_TYPES'
---

# OPM\_GET\_SUPPORTED\_PROTECTION\_TYPES

Returns the list of protection mechanisms that are supported by the connector.



|              |                                                                             |
|--------------|-----------------------------------------------------------------------------|
| Request GUID | OPM\_GET\_SUPPORTED\_PROTECTION\_TYPES                                      |
| Input data   | None                                                                        |
| Return data  | An [**OPM\_STANDARD\_INFORMATION**](opm-standard-information.md) structure |



 

## Remarks

The protection mechanisms are returned in the **ulInformation** member of the [**OPM\_STANDARD\_INFORMATION**](opm-standard-information.md) structure. The value is a bitwise **OR** of [OPM Protection Type Flags](opm-protection-type-flags.md).

This query is equivalent to the DXVA\_COPPQueryProtectionType query used in Certified Output Protection Protocol (COPP).

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

 

 




