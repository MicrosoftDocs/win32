---
description: Returns the type of I/O bus used by the video output.
ms.assetid: 1aff4c81-ffa0-4116-b7ea-60b1b83042df
title: OPM_GET_ADAPTER_BUS_TYPE (Opmapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# OPM\_GET\_ADAPTER\_BUS\_TYPE

Returns the type of I/O bus used by the video output.



| Requirement | Value |
|--------------|-----------------------------------------------------------------------------|
| Request GUID | OPM\_GET\_ADAPTER\_BUS\_TYPE                                                |
| Input data   | None                                                                        |
| Return data  | An [**OPM\_STANDARD\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_standard_information) structure |



 

## Remarks

The bus type is returned in the **ulInformation** member of the [**OPM\_STANDARD\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_standard_information) structure. The value is a bitwise **OR** of [**OPM Bus Type Flags**](opm-bus-type-flags.md).

This query is equivalent to the DXVA\_COPPQueryBusData query used in Certified Output Protection Protocol (COPP).

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

 

 




