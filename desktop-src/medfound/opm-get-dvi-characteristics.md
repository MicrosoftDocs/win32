---
Description: 'Queries whether a digital video interface (DVI) connector supports DVI version 1.1 or later.'
ms.assetid: 'b6c450c0-e97f-472d-ae09-fa1e062aeb9e'
title: 'OPM\_GET\_DVI\_CHARACTERISTICS'
---

# OPM\_GET\_DVI\_CHARACTERISTICS

Queries whether a digital video interface (DVI) connector supports DVI version 1.1 or later.



|              |                                                                             |
|--------------|-----------------------------------------------------------------------------|
| Request GUID | OPM\_GET\_DVI\_CHARACTERISTICS                                              |
| Input data   | None                                                                        |
| Return data  | An [**OPM\_STANDARD\_INFORMATION**](opm-standard-information.md) structure |



 

## Remarks

If this query succeeds, the **ulInformation** member of the [**OPM\_STANDARD\_INFORMATION**](opm-standard-information.md) structure contains one of the following values.



| Value                                     | Description               |
|-------------------------------------------|---------------------------|
| OPM\_DVI\_CHARACTERISTIC\_1\_0            | DVI version 1.0.          |
| OPM\_DVI\_CHARACTERISTIC\_1\_1\_OR\_ABOVE | DVI version 1.1 or later. |



 

This query is supported only when the physical connector type is OPM\_CONNECTOR\_TYPE\_DVI. To get the connector type, send the [**OPM\_GET\_CONNECTOR\_TYPE**](opm-get-connector-type.md) query.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Opmapi.h</dt> </dl> |



## See also

<dl> <dt>

[**IOPMVideoOutput::GetInformation**](iopmvideooutput-iopmvideooutput--getinformation.md)
</dt> <dt>

[OPM Status Requests](opm-status-requests.md)
</dt> </dl>

 

 




