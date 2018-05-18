---
Description: 'Returns the type of I/O bus used by the video output.'
ms.assetid: '1aff4c81-ffa0-4116-b7ea-60b1b83042df'
title: 'OPM\_GET\_ADAPTER\_BUS\_TYPE'
---

# OPM\_GET\_ADAPTER\_BUS\_TYPE

Returns the type of I/O bus used by the video output.



|              |                                                                             |
|--------------|-----------------------------------------------------------------------------|
| Request GUID | OPM\_GET\_ADAPTER\_BUS\_TYPE                                                |
| Input data   | None                                                                        |
| Return data  | An [**OPM\_STANDARD\_INFORMATION**](opm-standard-information.md) structure |



 

## Remarks

The bus type is returned in the **ulInformation** member of the [**OPM\_STANDARD\_INFORMATION**](opm-standard-information.md) structure. The value is a bitwise **OR** of [**OPM Bus Type Flags**](opm-bus-type-flags.md).

This query is equivalent to the DXVA\_COPPQueryBusData query used in Certified Output Protection Protocol (COPP).

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

 

 




