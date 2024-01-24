---
description: "Learn more about: OPM_GET_CONNECTED_HDCP_DEVICE_INFORMATION"
ms.assetid: 71fa9a99-83e4-4b27-9fd1-5a9dc3070820
title: OPM_GET_CONNECTED_HDCP_DEVICE_INFORMATION (Opmapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# OPM\_GET\_CONNECTED\_HDCP\_DEVICE\_INFORMATION

Gets information about a High-Bandwidth Digital Content Protection (HDCP) device attached to the video output. The following information is returned:

-   The device's HDCP key selection vector (KSV).
-   Whether the device is an HDCP repeater.



| Requirement | Value |
|--------------|---------------------------------------------------------------------------------------------------------|
| Request GUID | OPM\_GET\_CONNECTED\_HDCP\_DEVICE\_INFORMATION                                                          |
| Input data   | None                                                                                                    |
| Return data  | An [**OPM\_CONNECTED\_HDCP\_DEVICE\_INFORMATION**](/windows/desktop/api/opmapi/ns-opmapi-opm_connected_hdcp_device_information) structure |



 

## Remarks

This query can be used only with *COPP emulation mode*. If the [**IOPMVideoOutput**](/windows/desktop/api/opmapi/nn-opmapi-iopmvideooutput) interface uses Output Protection Manager (OPM) semantics, this status request is not supported.

The KSV is an identifier provided to the device manufacturer, and is used in the HDCP authentication and setup process. In COPP emulation mode, the application uses the KSV to determine whether the HDCP device is revoked. If it is, the application should not play protected content. Also, the application should not play protected content if the device is an HDCP repeater, because COPP does not support HDCP repeaters.

This query is not needed when OPM semantics are used, because OPM supports device revocation and HDCP repeaters.

This query is equivalent to the DXVA\_COPPQueryHDCPKeyData query used in Certified Output Protection Protocol (COPP).

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

[OPM Status Requests](opm-status-requests.md)
</dt> </dl>

 

 




