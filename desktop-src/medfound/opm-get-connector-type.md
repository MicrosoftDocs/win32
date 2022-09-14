---
description: Returns the physical connector type of the video output.
ms.assetid: c5862758-0125-4dbe-af72-5ed4a85bd702
title: OPM_GET_CONNECTOR_TYPE (Opmapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# OPM\_GET\_CONNECTOR\_TYPE

Returns the physical connector type of the video output.



| Requirement | Value |
|--------------|-----------------------------------------------------------------------------|
| Request GUID | OPM\_GET\_CONNECTOR\_TYPE                                                   |
| Input data   | None                                                                        |
| Return data  | An [**OPM\_STANDARD\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_standard_information) structure |



 

## Remarks

The connector type is returned in the **ulInformation** member of the [**OPM\_STANDARD\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_standard_information) structure. The value of **ulInformation** is equal to one of the connector types listed in [**OPM Connector Type Flags**](opm-connector-type-flags.md).

In COPP emulation mode, the connector type might be combined with the **OPM\_COPP\_COMPATIBLE\_CONNECTOR\_TYPE\_INTERNAL** flag. Use a bitwise **AND** to extract the connector type:

`ulInformation & ~OPM_COPP_COMPATIBLE_CONNECTOR_TYPE_INTERNAL`

Applications should ignore the **OPM\_COPP\_COMPATIBLE\_CONNECTOR\_TYPE\_INTERNAL** flag. For more information, see the Remarks section of [**OPM Connector Type Flags**](opm-connector-type-flags.md).

This query is equivalent to the DXVA\_COPPQueryConnectorType query used in Certified Output Protection Protocol (COPP).

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

 

 




