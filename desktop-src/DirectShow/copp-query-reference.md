---
description: COPP Query Reference
ms.assetid: 11eb1443-857d-4516-a5cb-c3cc02a5eba4
title: COPP Query Reference
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# COPP Query Reference

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes the status queries that are supported by Certified Output Protection Protocol (COPP). For each query, the GUID that defines the query is listed, along with the input data and return data.



| Query                   | GUID                                     |
|-------------------------|------------------------------------------|
| Bus Data                | **DXVA\_COPPQueryBusData**               |
| Connector Type          | **DXVA\_COPPQueryConnectorType**         |
| Display Data            | **DXVA\_COPPQueryDisplayData**           |
| HDCP Key Data           | **DXVA\_COPPQueryHDCPKeyData**           |
| Global Protection Level | **DXVA\_COPPQueryGlobalProtectionLevel** |
| Local Protection Level  | **DXVA\_COPPQueryLocalProtectionLevel**  |
| Protection Type         | **DXVA\_COPPQueryProtectionType**        |
| Signaling               | **DXVA\_COPPQuerySignaling**             |



 

Bus Data Query

Returns the type of I/O bus used by the graphics adapter.

-   **GUID**: DXVA\_COPPQueryBusData
-   **Input data**: None.
-   **Return data**: Returns a [**DXVA\_COPPStatusData**](/windows/desktop/api/dxva9typ/ns-dxva9typ-dxva_coppstatusdata) structure. The bus type is returned in the **dwData** member as a flag from the [**COPP\_BusType**](/windows/desktop/api/dxva9typ/ne-dxva9typ-copp_bustype) enumeration.

Connector Type Query

Returns the physical connector type.

-   **GUID**: DXVA\_COPPQueryConnectorType
-   **Input data**: None.
-   **Return data**: Returns a [**DXVA\_COPPStatusData**](/windows/desktop/api/dxva9typ/ns-dxva9typ-dxva_coppstatusdata) structure. The connector type is returned in the **dwData** member as a flag from the [**COPP\_ConnectorType**](/windows/desktop/api/dxva9typ/ne-dxva9typ-copp_connectortype) enumeration.

Display Data Query

Returns a description of the video signal that is being transmitted over the connector.

The video signal that is transmitted over the connector does not necessarily have the same format as the desktop display mode. For example, the desktop display mode might be 1024x768 pixels at 85 Hz, while the connector might be an S-Video connector that transmits a video signal at 720x480 pixels, 60/1.01 Hz interlaced. In that case, the driver would return the resolution of the S-Video signal, not the desktop resolution.

-   **GUID**: DXVA\_COPPQueryDisplayData
-   **Input data**: None.
-   **Return data**: Returns a [**DXVA\_COPPStatusDisplayData**](/windows/desktop/api/dxva9typ/ns-dxva9typ-dxva_coppstatusdisplaydata) structure.

HDCP Key Data Query

Returns the device's HDCP key selection vector (B-KSV).

The KSV is an identifier provided to the device manufacturer, and is used in the HDCP authentication and setup process. The application should check this value against the list of revoked KSVs. The mechanism for obtaining the KSV revocation list is outside the scope of the COPP protocol. For more information, consult the HDCP specification.

This query also determines whether the connected HDCP device is a monitor or an HDCP repeater. The application should not play protected content if the HDCP device is an HDCP repeater, because these are not supported by COPP.

-   **GUID**: DXVA\_COPPQueryHDCPKeyData
-   **Input data**: None.
-   **Return data**: Returns a [**DXVA\_COPPStatusHDCPKeyData**](/windows/desktop/api/dxva9typ/ns-dxva9typ-dxva_coppstatushdcpkeydata) structure.

Global Protection Level Query

Returns the global protection level for a specified protection mechanism.

The global protection level is the protection level that is currently being applied on the connector, regardless of how the graphics driver was instructed to apply the protection. For example, an application can set the ACP protection level by calling the **ChangeDisplaySettingsEx** function. In that case, the global protection level would reflect this setting, even though it was not requested through COPP.

-   **GUID**: DXVA\_COPPQueryGlobalProtectionLevel
-   **Input data**: The protection mechanism to query, specified as a 32-bit integer. See [COPP Protection Type Flags](copp-protection-type-flags.md).
-   **Return data**: Returns a [**DXVA\_COPPStatusData**](/windows/desktop/api/dxva9typ/ns-dxva9typ-dxva_coppstatusdata) structure. The current protection level is returned in the **dwData** member. The meaning of this value depends on the protection mechanism that is queried. For each protection mechanism, the value of the **dwData** member is a flag from a different enumeration, as shown in the following table.

    | Protection mechanism | Enumeration                                                           |
    |----------------------|-----------------------------------------------------------------------|
    | ACP                  | [**COPP\_ACP\_Protection\_Level**](/windows/desktop/api/dxva9typ/ne-dxva9typ-copp_acp_protection_level)     |
    | CGMS-A               | [**COPP\_CGMSA\_Protection\_Level**](/windows/desktop/api/dxva9typ/ne-dxva9typ-copp_cgmsa_protection_level) |
    | HDCP                 | [**COPP\_HDCP\_Protection\_Level**](/windows/desktop/api/dxva9typ/ne-dxva9typ-copp_hdcp_protection_level)   |

    

     

Local Protection Level Query

Returns the local protection level for a specified protection mechanism.

The local protection level is the protection level that was requested through the current COPP session. The driver might set a higher protection level.

-   **GUID**: DXVA\_COPPQueryLocalProtectionLevel
-   **Input data**: The protection mechanism to query, as a 32-bit integer. See [COPP Protection Type Flags](copp-protection-type-flags.md).
-   **Return data**: Returns a [**DXVA\_COPPStatusData**](/windows/desktop/api/dxva9typ/ns-dxva9typ-dxva_coppstatusdata) structure. The current protection level is returned in the **dwData** member. The meaning of this value depends on the protection mechanism that is queried. For each protection mechanism, the value of the **dwData** member is a flag from a different enumeration, as shown in the following table.

    | Protection mechanism | Enumeration                                                           |
    |----------------------|-----------------------------------------------------------------------|
    | ACP                  | [**COPP\_ACP\_Protection\_Level**](/windows/desktop/api/dxva9typ/ne-dxva9typ-copp_acp_protection_level)     |
    | CGMS-A               | [**COPP\_CGMSA\_Protection\_Level**](/windows/desktop/api/dxva9typ/ne-dxva9typ-copp_cgmsa_protection_level) |
    | HDCP                 | [**COPP\_HDCP\_Protection\_Level**](/windows/desktop/api/dxva9typ/ne-dxva9typ-copp_hdcp_protection_level)   |

    

     

Protection Type Query

Returns the protection mechanisms that are available for the connector.

-   **GUID**: DXVA\_COPPQueryProtectionType
-   **Input data**: None.
-   **Return data**: Returns a [**DXVA\_COPPStatusData**](/windows/desktop/api/dxva9typ/ns-dxva9typ-dxva_coppstatusdata) structure. The protection mechanisms are returned in the **dwData** member as a combination of zero or more flags. See [COPP Protection Type Flags](copp-protection-type-flags.md). If more than one protection mechanism is available, the flags are combined with a bitwise **OR**.

Signaling Query

Returns a list of all the protection standards that are supported by the driver, the standard that is currently active, and the current aspect ratio or other signaling data.

-   **GUID**: DXVA\_COPPQuerySignaling
-   **Input data**: None.
-   **Return data**: Returns a [**DXVA\_COPPStatusSignalingCmdData**](/windows/desktop/api/dxva9typ/ns-dxva9typ-dxva_coppstatussignalingcmddata) structure.

## Related topics

<dl> <dt>

[Using Certified Output Protection Protocol (COPP)](using-certified-output-protection-protocol--copp.md)
</dt> </dl>

 

 



