---
description: This topic describes video content&\#8211;protection capabilities that a graphics driver can provide.
ms.assetid: 3FDB4908-C75D-4AE0-B32E-93F840E4F30A
title: GPU-Based Content Protection with D3D11 Video
ms.topic: article
ms.date: 05/31/2018
---

# GPU-Based Content Protection with D3D11 Video

This topic describes video content–protection capabilities that a graphics driver can provide.

-   [Introduction](#introduction)
-   [Overview of the Decoding Process](#overview-of-the-decoding-process)
-   [Encrypting Compressed Video Buffers for the Decoder](#encrypting-compressed-video-buffers-for-the-decoder)
    -   [1. Query the Content Protection Capabilities of the Driver](#1-query-the-content-protection-capabilities-of-the-driver)
    -   [2. Configure the Authenticated Channel](#2-configure-the-authenticated-channel)
    -   [3. Configure the Cryptographic Session](#3-configure-the-cryptographic-session)
    -   [4. Associate the decoder with the Cryptographic Session](#4-associate-the-decoder-with-the-cryptographic-session)
-   [Sending Authenticated Channel Commands](#sending-authenticated-channel-commands)
-   [Sending Authenticated Channel Queries](#sending-authenticated-channel-queries)
-   [Related topics](#related-topics)

## Introduction

The following diagram shows a simplified view of how protected video content travels through the pipeline to be rendered.

![a diagram that shows protected video content.](images/d3d9video01.png)

> [!Note]
>
> The [Protected Media Path](protected-media-path.md) (PMP) is not depicted in this diagram. The data flow that is shown here might occur within a PMP process, or within an application process.

 

The decoder receives encrypted, compressed video data from an external source. It is assumed also the decoder also receives a cryptographic key to decrypt this data. This topic does not describe the key exchange between the video source and decoder, but the PMP defines one possible mechanism. The GPU is not involved at this stage.

For hardware-accelerated decoding, the software decoder passes compressed video content to the GPU. To protect this content, the decoder re-encrypts the data, typically using AES-CTR, before passing it to the hardware accelerator. A key-exchange mechanism is defined between the decoder and the graphics driver.

Decoded video frames are stored in video memory, generally in the clear. At this point, the frames are processed and then presented. There are two main options for presentation.

-   When using the D3D9 API, frames can be presented using a hardware overlay. Hardware overly is not supported in D3D11. For more information, see [Hardware Overlay Support](hardware-overlay-support.md).
-   Frames can be presented by the Desktop Window Manage (DWM) using a shared surface.

The last step is to display the frame on the monitor, which may require link protection between the graphics card and the display device. An example of link protection is High-Bandwidth Digital Content Protection (HDCP). Link protection is configured using [Output Protection Manager](output-protection-manager.md) (OPM). This topic does not describe OPM; for more information, see [Using Output Protection Manager](using-output-protection-manager.md).

## Overview of the Decoding Process

During hardware-accelerated decoding, the software decoder must pass compressed video data to the graphics card. For premium content, this data typically must be encrypted, using symmetric-key encryption, before it is sent to the GPU.

To encrypt the video for decoding, the software decoder uses the following interfaces:

-   [**ID3D11VideoDecoder**](/windows/desktop/api/d3d11/nn-d3d11-id3d11videodecoder). Represents the decoder device, also called the accelerator.
-   [**ID3D11CryptoSession**](/windows/desktop/api/d3d11/nn-d3d11-id3d11cryptosession). Represents a cryptographic session, which provides the encryption key.
-   [**ID3D11AuthenticatedChannel**](/windows/desktop/api/d3d11/nn-d3d11-id3d11authenticatedchannel). Represents an authenticated channel, which enables the software decoder to associate the cryptographic session with the decoder.

![a diagram that shows the direct3d9 decoding interfaces.](images/d3d9video02.png)

All of these interfaces are obtained from the Direct3D11 device, as follows:



| Interface                                                        | Creation                                                                                                                                                |
|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ID3D11VideoDecoder**](/windows/desktop/api/d3d11/nn-d3d11-id3d11videodecoder)                 | Call [**ID3D11VideoDevice::CreateVideoDecoder**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videodevice-createvideodecoderoutputview). The decoder type is identified by a profile GUID. |
| [**ID3D11CryptoSession**](/windows/desktop/api/d3d11/nn-d3d11-id3d11cryptosession)               | Call [**ID3D11VideoDevice::CreateCryptoSession**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videodevice-createcryptosession).                                                           |
| [**ID3D11AuthenticatedChannel**](/windows/desktop/api/d3d11/nn-d3d11-id3d11authenticatedchannel) | Call [**ID3D11VideoDevice::CreateAuthenticatedChannel**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videodevice-createauthenticatedchannel).                                             |



 

> [!Note]  
> To get a pointer to the [**ID3D11VideoDevice**](/windows/desktop/api/d3d11/nn-d3d11-id3d11videodevice) interface, call [**QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) on [**ID3D11Device**](/windows/win32/api/d3d11/nn-d3d11-id3d11device) interface.

 

The authenticated channel provides a trusted communication channel between the software decoder and the driver. The communication channel works as follows:

-   The driver provides an X.509 certificate chain whose root certificate is signed by Microsoft.
-   The certificate contains an RSA public key for the driver.
-   The software decoder uses the public key to send the driver a 128-bit AES session key.
-   The software decoder sends queries and commands to the authenticated channel.
-   The session key is used to compute message authentication codes (MACs) for the queries and commands. The driver uses the MACs to verify the integrity of the query/command data, and the software decoder uses them to verify the integrity of the response data from the driver.

## Encrypting Compressed Video Buffers for the Decoder

Here is a high-level overview of the encryption and decoding process:

1.  The software decoder receives a stream of encrypted data from the video source. The decoder decrypts this stream.
2.  The software decoder negotiates a session key with the cryptographic session.
3.  The software decoder uses the authenticated channel to associate the cryptographic session with the decoder device.
4.  The software decoder puts compressed data in buffers that it gets from the decoder device (accelerator). For protected content, the software encoder encrypts the data that is puts into the buffers, using the session key for the encryption.
    > [!Note]  
    > Some drivers use a content key, instead of the session key, for encryption. The content key could change from one frame to the next.

     

5.  The decoder submits the encrypted compressed buffers to the accelerator. For AES-CTR, the decoder also passes the initialization vector. If a content key is used, the decoder passes the content key, encrypted using the session key.

Direct3D11 has standard support for 128-bit AES-CTR, but is designed to extend to additional encryption types.

The next five sections give more detailed steps.

-   [1. Query the Content Protection Capabilities of the Driver](#1-query-the-content-protection-capabilities-of-the-driver)
-   [2. Configure the Authenticated Channel](#2-configure-the-authenticated-channel)
-   [3. Configure the Cryptographic Session](#3-configure-the-cryptographic-session)
-   [4. Associate the decoder with the Cryptographic Session](#4-associate-the-decoder-with-the-cryptographic-session)

### 1. Query the Content Protection Capabilities of the Driver

Before attempting to apply encryption, get the content protection capabilities of the driver.

1.  Get a pointer to the ID3D11Device interface.
2.  Call [**QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) for the [**ID3D11VideoDevice**](/windows/desktop/api/d3d11/nn-d3d11-id3d11videodevice) interface.
3.  Call [**ID3D11VideoDevice::GetContentProtectionCaps**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videodevice-getcontentprotectioncaps). This method fills in a [**D3D11_VIDEO_CONTENT_PROTECTION_CAPS**](/windows/desktop/api/d3d11/ns-d3d11-d3d11_video_content_protection_caps) structure with the driver’s content protection capabilities.

In particular, look for the following capabilities:

-   If the **Caps** member contains the **D3D11_CONTENT_PROTECTION_CAPS_SOFTWARE** or **D3D11_CONTENT_PROTECTION_CAPS_HARDWARE** flag, the driver can perform encryption.
-   If the **Caps** member contains the **D3D11_CONTENT_PROTECTION_CAPS_CONTENT_KEY** flag, the driver uses a separate content key for decryption.
-   Call [**ID3D11VideoDevice::CheckCryptoKeyExchange**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videodevice-checkcryptokeyexchange) to determine which types of key exchanges the driver supports for generating the session key.

Additional capabilities are indicated in the **Caps** member.

### 2. Configure the Authenticated Channel

The next step is to configure the authenticated channel.

1.  Call [**ID3D11VideoDevice::CreateAuthenticatedChannel**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videodevice-createauthenticatedchannel) to create the authenticated channel. For the *ChannelType* parameter, specify a channel type that matches the capabilities of the driver.
    -   The **D3D11_AUTHENTICATED_CHANNEL_DRIVER_SOFTWARE** channel type corresponds to **D3D11_CONTENT_PROTECTION_CAPS_SOFTWARE**.
    -   The **D3D11_AUTHENTICATED_CHANNEL_DRIVER_HARDWARE** channel type corresponds to **D3D11_CONTENT_PROTECTION_CAPS_HARDWARE**.

    The **CreateAuthenticatedChannel** method returns a pointer to the [**ID3D11AuthenticatedChannel**](/windows/desktop/api/d3d11/nn-d3d11-id3d11authenticatedchannel) interface.
2.  Call [**ID3D11AuthenticatedChannel::GetCertificateSize**](/windows/desktop/api/d3d11/nf-d3d11-id3d11authenticatedchannel-getcertificatesize) to get the size of the driver's X.509 certificate. Allocate a buffer of the required size.
3.  Call [**ID3D11AuthenticatedChannel::GetCertificate**](/windows/desktop/api/d3d11/nf-d3d11-id3d11authenticatedchannel-getcertificate) to get the certificate. The method copies the certificate into the buffer that was allocated in the previous step.
4.  Verify that the driver’s certificate was signed by Microsoft and has not been revoked.
5.  Get the public key from the certificate.
6.  Generate a random RSA session key. This session key is used to sign data that is sent to the authenticated channel. Encrypt the session key using the driver's public key.
7.  Call [**ID3D11VideoContext::NegotiateAuthenticatedChannelKeyExchange**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videocontext-negotiateauthenticatedchannelkeyexchange) to send the encrypted session key to the driver.
8.  Initialize the secure channel as follows:
    1.  Fill in a [**D3D11_AUTHENTICATED_CONFIGURE_INITIALIZE_INPUT**](/windows/desktop/api/d3d11/ns-d3d11-d3d11_authenticated_configure_initialize_input) structure as described in the documentation.
    2.  Send the [**D3D11_AUTHENTICATED_CONFIGURE_INITIALIZE_INPUT**](/windows/desktop/api/d3d11/ns-d3d11-d3d11_authenticated_configure_initialize_input) command by calling [**ID3D11VideoContext::ConfigureAuthenticatedChannel**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videocontext-configureauthenticatedchannel) as described in the section [Sending Authenticated Channel Commands](#sending-authenticated-channel-commands). This command contains the starting sequence numbers for the commands and queries that are sent to the authenticated channel.
9.  Verify the channel type by sending a [**D3D11_AUTHENTICATED_QUERY_CHANNEL_TYPE**](/windows/desktop/api/d3d11/ns-d3d11-d3d11_authenticated_query_channel_type_output) query to the authenticated channel, as described in the section [Sending Authenticated Channel Queries](#sending-authenticated-channel-queries). Check that the channel type matches what you specified in the [**CreateAuthenticatedChannel**](/windows/desktop/api/d3d9/nf-d3d9-idirect3ddevice9video-createauthenticatedchannel) method.

### 3. Configure the Cryptographic Session

Next, configure the cryptographic session and establish the session key.

1.  Call [**ID3D11VideoDevice::CreateCryptoSession**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videodevice-createcryptosession) to create the cryptographic session. This method returns a pointer to the [**ID3D11CryptoSession**](/windows/desktop/api/d3d11/nn-d3d11-id3d11cryptosession) interface.
2.  Call [**ID3D11CryptoSession::GetCertificateSize**](/windows/desktop/api/d3d11/nf-d3d11-id3d11cryptosession-getcertificatesize) to get the size of the driver's X.509 certificate. Allocate a buffer of the required size.
3.  Call [**ID3D11CryptoSession::GetCertificate**](/windows/desktop/api/d3d11/nf-d3d11-id3d11cryptosession-getcertificate) to get the certificate. The method copies the certificate into the buffer that was allocated in the previous step.
4.  Verify that the driver’s certificate was signed by Microsoft and has not been revoked.
5.  Get the public key from the certificate.
6.  Generate a random RSA session key. This is a separate session key from the authenticated channel session key. Encrypt the session key using the driver's public key.
7.  Call [**ID3D11VideoContext::NegotiateCryptoSessionKeyExchange**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videocontext-negotiatecryptosessionkeyexchange) to send the encrypted session key to the driver.
8.  If the content protection capabilities include **3D11_CONTENT_PROTECTION_CAPS_CONTENT_KEY**, create a random RSA content key. This will be used later in the decoding process.

### 4. Associate the decoder with the Cryptographic Session

Next, associate the decoder device with the Direct3D11 device and the cryptographic session, as follows:

1.  Get a handle to the Direct3D11 device, by sending a [**D3D11_AUTHENTICATED_QUERY_DEVICE_HANDLE**](/windows/desktop/api/d3d11/ns-d3d11-d3d11_authenticated_query_device_handle_output) query to the authenticated channel.
2.  Fill in a [**D3D11_AUTHENTICATED_CONFIGURE_CRYPTO_SESSION_INPUT**](/windows/desktop/api/d3d11/ns-d3d11-d3d11_authenticated_configure_crypto_session_input) structure with the following information:
    -   Set the **DecodeHandle** member to the handle returned from [**ID3D11VideoDecoder::GetDriverHandle**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videodecoder-getdriverhandle).
    -   Set the **CryptoSessionHandle** member to the handle returned from [**ID3D11CryptoSession::GetCryptoSessionHandle**](/windows/desktop/api/d3d11/nf-d3d11-id3d11cryptosession-getcryptosessionhandle).
    -   Set the **DeviceHandle** member to the Direct3D11 device handle.
3.  Call [**ID3D11VideoContext::ConfigureAuthenticatedChannel**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videocontext-configureauthenticatedchannel) to send a [**D3D11_AUTHENTICATED_CONFIGURE_CRYPTO_SESSION**](/windows/desktop/api/d3d11/ns-d3d11-d3d11_authenticated_configure_crypto_session_input) command to the authenticated channel.

The following diagram illustrates the exchange of handles:

![a diagram that shows how the dxva decoder is associated with the cryptographic session.](images/d3d9video03.png)

The software decoder can now use the cryptographic session key to encrypt the compressed video buffers. Each compressed buffer will have its own initialization vector (IV) specified in the **pIV** member of the [**D3D11_VIDEO_DECODER_BUFFER_DESC**](/windows/desktop/api/d3d11/ns-d3d11-d3d11_video_decoder_buffer_desc) structure.

## Sending Authenticated Channel Commands

A set of commands are defined for configuring the authenticated channel and setting various content protections. For a list of commands, see [Content Protection Commands](content-protection-commands.md).

To send a command to the authenticated channel, perform the following steps.

1.  Fill in the input data structure. This data structure is always a [**D3D11_AUTHENTICATED_CONFIGURE_INPUT**](/windows/desktop/api/d3d11/ns-d3d11-d3d11_authenticated_configure_input) structure followed by additional fields. Fill in the **D3D11_AUTHENTICATED_CONFIGURE_INPUT** structure as shown in the following table.

    
| Member | Description | 
|--------|-------------|
| <strong>omac</strong> | Skip this field for now. | 
| <strong>ConfigureType</strong> | GUID that identifies the command. For a list of commands, see <a href="content-protection-commands.md">Content Protection Commands</a>. | 
| <strong>hChannel</strong> | The handle to the authenticated channel. | 
| <strong>SequenceNumber</strong> | The sequence number. The first sequence number is specified by sending a <a href="/windows/desktop/api/d3d11/ns-d3d11-d3d11_authenticated_configure_initialize_input"><strong>D3D11_AUTHENTICATED_CONFIGURE_INITIALIZE</strong></a> command. Each time you send another command, increment this number by 1. The sequence number guards against replay attacks.    <blockquote>    [!Note]<br />    Two separate sequence numbers are used, one for commands and one for queries.    </blockquote><br /><br /> | 






2.  Calculate the OMAC tag for the block of data that appears after the **omac** member of the input structure. Then copy this tag value into the **omac** member.
3.  Call [**ID3D11VideoContext::ConfigureAuthenticatedChannel**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videocontext-configureauthenticatedchannel).
4.  The driver places the output from the command in the [**D3D11_AUTHENTICATED_CONFIGURE_OUTPUT**](/windows/desktop/api/d3d11/ns-d3d11-d3d11_authenticated_configure_output) structure.
5.  Calculate the OMAC tag for the block of data that appears after the **omac** member of the output structure. Compare this with the value of the **omac** member. Fail if they do not match.
6.  Compare the values of the **ConfigureType**, **hChannel**, and **SequenceNumber** members in the output structure against your values for those members. Fail if they do not match.
7.  Increment the sequence number for the next command.

## Sending Authenticated Channel Queries

A set of queries are defined for retrieving information about the authenticated channel. For a list of queries, see [Content Protection Queries](content-protection-queries.md).

To send a command to the authenticated channel, perform the following steps.

1.  Fill in the input data structure. This data structure is always a [**D3D11_AUTHENTICATED_QUERY_INPUT**](/windows/desktop/api/d3d11/ns-d3d11-d3d11_authenticated_query_input) structure, possibly followed by additional fields. Fill in the **D3D11_AUTHENTICATED_QUERY_INPUT** structure as shown in the following table.

    
| Member | Description | 
|--------|-------------|
| <strong>QueryType</strong> | GUID that identifies the query. For a list of queries, see <a href="content-protection-queries.md">Content Protection Queries</a>. | 
| <strong>hChannel</strong> | The handle to the authenticated channel. | 
| <strong>SequenceNumber</strong> | The sequence number. The first sequence number is specified by sending a <a href="/windows/desktop/api/d3d11/ns-d3d11-d3d11_authenticated_configure_initialize_input"><strong>D3D11_AUTHENTICATED_CONFIGURE_INITIALIZE</strong></a> command. Each time you send another query, increment this number by 1. The sequence number guards against replay attacks.    <blockquote>    [!Note]<br />    Two separate sequence numbers are used, one for commands and one for queries.    </blockquote><br /><br /> | 






2.  Call [**ID3D11VideoContext::QueryAuthenticatedChannel**](/windows/desktop/api/d3d11/nf-d3d11-id3d11videocontext-queryauthenticatedchannel).
3.  The driver places the output from the query in a [**D3D11_AUTHENTICATED_QUERY_OUTPUT**](/windows/desktop/api/d3d11/ns-d3d11-d3d11_authenticated_query_output) structure. This structure is followed by additional fields, depending on the query type.
4.  Calculate the OMAC tag for the block of data that appears after the **omac** member of the output structure. Compare this with the value of the **omac** member. Fail if they do not match.
5.  Compare the values of the **ConfigureType**, **hChannel**, and **SequenceNumber** members in the output structure against your values for those members. Fail if they do not match.
6.  Increment the sequence number for the next query.

## Related topics

<dl> <dt>

[Direct3D 11 Video APIs](direct3d-11-video-apis.md)
</dt> </dl>

 

 
