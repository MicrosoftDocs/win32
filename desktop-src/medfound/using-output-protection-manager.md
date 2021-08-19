---
description: "Learn more about: Using Output Protection Manager"
ms.assetid: 01edc17e-e71c-4772-a03c-09c9a2b8400f
title: Using Output Protection Manager
ms.topic: article
ms.date: 05/31/2018
---

# Using Output Protection Manager

This topic describes how to use Output Protection Manager (OPM) to protect video content as it travels over a physical connector to a display device. This topic contains the following sections:

-   [Video Outputs](#video-outputs)
-   [Initializing an OPM Session](#initializing-an-opm-session)
-   [Sending OPM Status Requests](#sending-opm-status-requests)
-   [Sending OPM Commands](#sending-opm-commands)
-   [Handling a Disabled Video Output](#sending-opm-commands)
-   [Using HDCP to Protect Content](#using-hdcp-to-protect-content)

Premium video content is usually encrypted to protect it from unauthorized duplication. Of course, the video must be decrypted before it is displayed. The decrypted, uncompressed frames must then travel across a physical connector to the display device. Content providers may require the video frames to be protected at this point, as they travel across the physical connector.

Various protection mechanisms exist for this purpose, including High-Bandwidth Digital Content Protection (HDCP) and DisplayPort Content Protection (DPCP) for digital outputs; and Copy Generation Management System - Analog (CGMS-A) for analog outputs. Generally, these mechanisms involve encrypting or scrambling the signal befores it goes to the display.

OPM enables an application to enforce content protection mechanisms on the video output. Using OPM, the application sends commands and status requests to the graphics driver through a trusted, secure channel. OPM enables an application to:

-   Verify that a graphics driver has been signed by Microsoft.
-   Set up a trusted communication channel with the driver.
-   Enforce content protection mechanisms on the physical output.

OPM replaces Certified Output Protection Protcol (COPP) and uses a similar API. For backward compatibility, the OPM interface can emulate the COPP interface. Differences between OPM and COPP include the following:

-   OPM uses X.509 certificates, while COPP uses a proprietary certificate format.
-   OPM supports HDCP repeaters.
-   Applications that use OPM do not have to parse HDCP system renewability messages (SRMs).
-   OPM can be used when the graphics display is using clone mode. COPP does not support clone mode.

If your application uses the protected media path (PMP) to play video content, you do not have to use the OPM API, because the PMP makes all of the required OPM calls. The OPM API is available for applications that do not use the PMP.

OPM is available in Windows Vista and later, but the API was not made public until Windows 7. To use OPM in an application, you must have the headers and library files from the Windows 7 SDK. You do not have to redistribute any DLLs to use OPM in Windows Vista or Windows Server 2008.

## Video Outputs

A graphics adapter can have more than one physical output, each with its own capabilities. Before an application plays protected content, it must set the appropriate protection mechanisms on every video output associated with the graphics card that will display the video. Which protection mechanisms to apply will depend on the usage rules for the content.

Each video output is represented by an instance of the [**IOPMVideoOutput**](/windows/desktop/api/opmapi/nn-opmapi-iopmvideooutput) interface. You can use a Direct3D device or monitor handles to get the video outputs.

Using a Direct3D device:

1.  Get the **IDirect3DDevice9** pointer for the Direct3D device that your application will use to create surfaces to hold the video frames.
2.  Call the [**OPMGetVideoOutputsFromIDirect3DDevice9Object**](/windows/desktop/api/opmapi/nf-opmapi-opmgetvideooutputsfromidirect3ddevice9object) function. This function allocates an array of [**IOPMVideoOutput**](/windows/desktop/api/opmapi/nn-opmapi-iopmvideooutput) pointers, one for each output.

Using monitor handles:

1.  Call **EnumDisplayMonitors** to get the **HMONITOR** handles that correspond to the video window. Several monitors can be associated with the same window, so you might get several **HMONITOR** handles.
2.  For each monitor handle, call [**OPMGetVideoOutputsFromHMONITOR**](/windows/desktop/api/opmapi/nf-opmapi-opmgetvideooutputsfromhmonitor). This function allocates an array of [**IOPMVideoOutput**](/windows/desktop/api/opmapi/nn-opmapi-iopmvideooutput) pointers, one for each output.

## Initializing an OPM Session

Before the application sends OPM commands or status requests, it must verify that the video output is trusted and establish a session key. The session key is used to sign the data that is exchanged between the application and the graphics driver.

The OPM API defines a handshake that establishes trust and sets the session key. You must perform this handshake for each instance of the [**IOPMVideoOutput**](/windows/desktop/api/opmapi/nn-opmapi-iopmvideooutput) interface, as follows:

1.  Call [**IOPMVideoOutput::StartInitialization**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-startinitialization). This method retrieves two pieces of data:
    -   A random number, generated by the driver. You will use this number to complete the handshake.
    -   The driver's X.509 certificate chain.
2.  Verify that the certificate chain has been signed by Microsoft.
    > [!Note]  
    > Certificate revocation is outside the scope of OPM.

     

3.  Get the driver's public key from the certificate chain.
4.  Generate a 128-bit AES session key.
5.  Generate two random 32-bit numbers:

    -   The starting sequence number for OPM status requests.
    -   The starting sequence number for OPM commands.

    These numbers must be generated using a cryptographically secure pseudo-random number generator, such as **CryptGenRandom**.

6.  Copy the driver's random number (obtained in step 1), the session key, and the two sequence numbers into an [**OPM\_ENCRYPTED\_INITIALIZATION\_PARAMETERS**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_encrypted_initialization_parameters) structure, as described in [**IOPMVideoOutput::FinishInitialization**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-finishinitialization).
7.  Encrypt the [**OPM\_ENCRYPTED\_INITIALIZATION\_PARAMETERS**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_encrypted_initialization_parameters) structure with RSAES-OAEP, using the driver's public key, which is found in the driver's certificate.
8.  Call [**IOPMVideoOutput::FinishInitialization**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-finishinitialization).

## Sending OPM Status Requests

OPM status requests return information about the video output, such as the type of physical connector and the current protection level. For a list of request types, see [OPM Status Requests](opm-status-requests.md).

To send a status request, perform the following steps.

1.  Initialize an [**OPM\_GET\_INFO\_PARAMETERS**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_get_info_parameters) structure as shown in the following table.

    | Member               | Description                                                                                                                                                                                                                                                                                                                                                                 |
    |----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | **omac**             | Skip this field for now.                                                                                                                                                                                                                                                                                                                                                    |
    | **rnRandomNumber**   | A cryptographically secure 128-bit random number. Whenever you make a status request, always generate a new random number, even if you are making the same request. Store the number in a variable, because you will need to refer to it later.                                                                                                                             |
    | **guidInformation**  | A GUID that identifies the status request. For a list of status requests, see [OPM Status Requests](opm-status-requests.md).                                                                                                                                                                                                                                               |
    | **ulSequenceNumber** | The sequence number. For the first status request, use the starting sequence number that you specified in the [**IOPMVideoOutput::FinishInitialization**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-finishinitialization) method (step 5 of [Initializing an OPM Session](#initializing-an-opm-session).) Each time you make another status request, increment this number by 1. |
    | **abParameters**     | A byte array that contains additional input data for the request. The format of the input data is listed in the reference topic for each status request.                                                                                                                                                                                                                    |
    | **cbParametersSize** | The size of the valid data in the **abParameters** array. The contents of the rest of the array are undefined.                                                                                                                                                                                                                                                              |

    

     

2.  Calculate the one-key CBC MAC (OMAC-1) to calculate a hash for the block of data that appears after the **omac** member, and then set the **omac** member to this value. See [OPM Example Code](opm-example-code.md).
3.  Call the [**IOPMVideoOutput::GetInformation**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-getinformation) method. Pass in a pointer to the [**OPM\_GET\_INFO\_PARAMETERS**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_get_info_parameters) structure and a pointer to an [**OPM\_REQUESTED\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_requested_information) structure. The driver's response is written to the **OPM\_REQUESTED\_INFORMATION** structure.
    -   The **omac** member of this structure contains an OMAC computed for the data that follows this member.
    -   The **abRequestedInformation** member is a byte array that contains output data for the response. The format of the output data is listed in the reference topic for each status request.
4.  Calculate an OMAC for the [**OPM\_REQUESTED\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_requested_information) structure, not including the **omac** member. Verify that the OMAC matches the value in the **omac** member.
5.  Make sure the **cbRequestedInformationSize** member of the [**OPM\_REQUESTED\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_requested_information) structure gives the correct size for the output data. For example, the output data for the [**OPM\_GET\_CONNECTOR\_TYPE**](opm-get-connector-type.md) query is an [**OPM\_STANDARD\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_standard_information) structure, so the value of **cbRequestedInformationSize** should be `sizeof(OPM_STANDARD_INFORMATION)`.
6.  Cast the **abRequestedInformation** member of the [**OPM\_REQUESTED\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_requested_information) structure to the correct output data structure. For example, if the status request is [**OPM\_GET\_CONNECTOR\_TYPE**](opm-get-connector-type.md), cast **abRequestedInformation** to an [**OPM\_STANDARD\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_standard_information) structure.
7.  Make sure the **rnRandomNumber** member of the output data structure matches the value of **rnRandomNumber** from step 1.
8.  Check the **ulStatusFlags** member of the output data structure, as described in [Handling a Disabled Video Output](#handling-a-disabled-video-output).

If any of the checks in steps 5–8 fails, the application must stop showing protected content.

## Sending OPM Commands

OPM commands are used to set the protection level and other settings on the video output. Sending an OPM command is similar to sending a status request, except there is no response data from the driver. For a list of commands, see [OPM Commands](opm-commands.md).

To send an OPM command, perform the following steps.

1.  Fill in an [**OPM\_CONFIGURE\_PARAMETERS**](/windows/desktop/api/opmapi/ns-opmapi-opm_configure_parameters) structure as shown in the following table.

    | Member                | Description                                                                                                                                                                                                                                                                                                                                                   |
    |-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | **omac**              | Skip this field for now.                                                                                                                                                                                                                                                                                                                                      |
    | **guidSetting**       | A GUID that identifies the command. For a list of commands, see [OPM Commands](opm-commands.md).                                                                                                                                                                                                                                                             |
    | **ulSequenceNumber**  | The sequence number. For the first command, use the starting sequence number that you specified in the [**IOPMVideoOutput::FinishInitialization**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-finishinitialization) method (step 5 of [Initializing an OPM Session](#initializing-an-opm-session).) Each time you send another command, increment this number by 1. |
    | **abParameters**      | A byte array that contains additional input data for the command. The format of the input data is listed in the reference topic for each command.                                                                                                                                                                                                             |
    | **cbSettingDataSize** | The size of the valid data in the **abParameters** array. The contents of the rest of the array are undefined.                                                                                                                                                                                                                                                |

    

     

2.  Calculate an OMAC for the block of data that appears after the **omac** member, and then set the **omac** member to this value.
3.  Call [**IOPMVideoOutput::Configure**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-configure).

For most commands, there is a corresponding status request that returns the status of the command. For example, the [**OPM\_SET\_PROTECTION\_LEVEL**](opm-set-protection-level.md) command sets the protection level, and the [**OPM\_GET\_VIRTUAL\_PROTECTION\_LEVEL**](opm-get-virtual-protection-level.md) command gets the current protection level.

## Handling a Disabled Video Output

A video output might disable itself at any time to prevent the unauthorized use of video content. This might occur because a protection mechanism stops working, because the driver detects tampering, or because the display was disconnected from the physical connector. While a video output is disabled, no video frames are displayed.

While content protection is enabled, an application should periodically (at least once every 2 seconds) perform the following steps.

1.  Call [**IOPMVideoOutput::GetInformation**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-getinformation) to send either the [**OPM\_GET\_ACTUAL\_PROTECTION\_LEVEL**](opm-get-actual-protection-level.md) or [**OPM\_GET\_VIRTUAL\_PROTECTION\_LEVEL**](opm-get-virtual-protection-level.md) status request. The return data for both commands is an [**OPM\_STANDARD\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_standard_information) structure.
2.  Check the **ulInformation** member of the [**OPM\_STANDARD\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_standard_information) structure. This member contains a flag indicating whether content protection is still enabled. If content protection is off, stop playing the video immediately.
3.  If content protection is on, check the **ulStatusFlags** member of the [**OPM\_STANDARD\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_standard_information) structure. If no flags are set, the video output is working correctly. Otherwise, the video output is disabled.

The following flags are defined for **ulStatusFlags**.




| Flag | Description | 
|------|-------------|
| <strong>OPM_STATUS_LINK_LOST</strong> | Output protection stopped working for some reason; for example, the display device might be unplugged from the conntector. Stop playback and turn off all output protection mechanisms. | 
| <strong>OPM_STATUS_RENEGOTIATION_REQUIRED</strong> | The application must reestablish the OPM session. Respond as follows:<ol><li>Stop playback.</li><li>Turn off all protection mechanisms.</li><li>Release the <a href="/windows/desktop/api/opmapi/nn-opmapi-iopmvideooutput"><strong>IOPMVideoOutput</strong></a> interface.</li><li>Recreate all video surfaces.</li><li>Create a new OPM object and attempt to reestablish content protection. If this fails, display an error message to the user. Do not play any more video content.</li></ol> | 
| <strong>OPM_STATUS_REVOKED_HDCP_DEVICE_ATTACHED</strong> | This flag applies only when HDCP is used, and indicates the presence of a revoked HDCP device. Stop playback and turn off all protection mechanisms on this video output. When this flag is set, the <strong>OPM_STATUS_LINK_LOST</strong> flag is also set. | 
| <strong>OPM_STATUS_REVOKED_HDCP_DEVICE_ATTACHED</strong> | The driver has detected tampering. Stop playback, and do not play any more video using this video output. It is also a good idea to stop using any other video outputs, because the system might be compromised. | 




 

## Using HDCP to Protect Content

This section describes how to enable HDCP output protection using OPM. Here is a general outline of the steps the application must take. Details are given later in this section.

1.  The application might have to provide an SRM to the video output. The mechanism for receiving SRMs is outside the scope of the OPM interface. For example, SRMs might be delivered as part of a broadcast stream.
2.  The application enables HDCP output protection.
3.  The application plays the video content. Periodically, the application polls the driver to make sure HDCP is on.
4.  When playback is complete, the application turns off HDCP.

### Setting the SRM

To set the SRM, perform the following steps.

1.  Initialize an [**OPM\_SET\_HDCP\_SRM\_PARAMETERS**](/windows/desktop/api/opmapi/ns-opmapi-opm_set_hdcp_srm_parameters) structure with the SRM version number.
2.  Store the SRM in a variable.
3.  Send an [**OPM\_SET\_HDCP\_SRM**](opm-set-hdcp-srm.md) command to the video output. Use the procedure described in [Sending OPM Commands](#sending-opm-commands).
    -   The **abParameters** member of the [**OPM\_CONFIGURE\_PARAMETERS**](/windows/desktop/api/opmapi/ns-opmapi-opm_configure_parameters) structure contains the [**OPM\_SET\_HDCP\_SRM\_PARAMETERS**](/windows/desktop/api/opmapi/ns-opmapi-opm_set_hdcp_srm_parameters) structure.
    -   The *pbAdditionalParameters* parameter of the [**IOPMVideoOutput::Configure**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-configure) method points to the variable that contains the SRM.
4.  Send an [**OPM\_GET\_CURRENT\_HDCP\_SRM\_VERSION**](opm-get-current-hdcp-srm-version.md) status request to the video output. Use the procedure described in [Sending OPM Status Requests](#sending-opm-status-requests). This status request has no input data, so the contents of the **abParameters** member of the [**OPM\_GET\_INFO\_PARAMETERS**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_get_info_parameters) structure are undefined.
5.  When the [**IOPMVideoOutput::GetInformation**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-getinformation) method returns, the **abRequestedInformation** array in the [**OPM\_REQUESTED\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_requested_information) structure contains an [**OPM\_STANDARD\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_standard_information) structure. The **ulInformation** member of this structure contains the version number of the current SRM. This value must equal the value from step 2.

### Enabling HDCP

To enable HDCP, perform the following steps.

1.  Initialize an [**OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS**](/windows/desktop/api/opmapi/ns-opmapi-opm_set_protection_level_parameters) structure with the following values:
    -   **ulProtectionType** = **OPM\_PROTECTION\_TYPE\_HDCP**
    -   **ulProtectionLevel** = **OPM\_HDCP\_ON**
    -   **Reserved** = 0
    -   **Reserved2** = 0
2.  Send an [**OPM\_SET\_PROTECTION\_LEVEL**](opm-set-protection-level.md) command. The input data in the **abParameters** array is the [**OPM\_SET\_PROTECTION\_LEVEL\_PARAMETERS**](/windows/desktop/api/opmapi/ns-opmapi-opm_set_protection_level_parameters) structure.
3.  Send an [**OPM\_GET\_VIRTUAL\_PROTECTION\_LEVEL**](opm-get-virtual-protection-level.md) status request to check whether HDCP is enabled. The first 4 bytes of the **abParameters** member of the [**OPM\_GET\_INFO\_PARAMETERS**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_get_info_parameters) structure contain the value **OPM\_PROTECTION\_TYPE\_HDCP**.

When the [**GetInformation**](/windows/desktop/api/opmapi/nf-opmapi-iopmvideooutput-getinformation) method returns, the **abRequestedInformation** array in the [**OPM\_REQUESTED\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_requested_information) structure contains an [**OPM\_STANDARD\_INFORMATION**](/windows/desktop/api/ksopmapi/ns-ksopmapi-opm_standard_information) structure. The **ulInformation** member of this structure contains a value from the [**OPM\_HDCP\_PROTECTION\_LEVEL**](/windows/desktop/api/opmapi/ne-opmapi-opm_hdcp_protection_level) enumeration. If the value equals **OPM\_HDCP\_ON**, it means HDCP is enabled. Otherwise, repeat steps 1–2 until HDCP is enabled, or an error occurs. (Remember to increment the sequence number and generate a new random number each time.)

It usually takes between 100 and 200 milliseconds to enable HDCP, but it can take longer. Do not assume that HDCP is enabled until you have verified it.

When the application finishes playing protected content, turn off HDCP. The steps are the same as for enabling HDCP, but in step 1, set **ulProtectionLevel** to **OPM\_HDCP\_OFF**.

> [!Note]  
> Do not enable HDCP if the connector type is **OPM\_CONNECTOR\_TYPE\_DISPLAYPORT\_EMBEDDED**. (See [**OPM Connector Type Flags**](opm-connector-type-flags.md).)

 

## Related topics

<dl> <dt>

[Output Protection Manager](output-protection-manager.md)
</dt> </dl>

 

 



