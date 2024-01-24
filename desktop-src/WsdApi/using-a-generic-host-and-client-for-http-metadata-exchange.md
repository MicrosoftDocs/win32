---
description: If the client and host cannot exchange metadata, then a generic host and client can be substituted for the custom host and client to help troubleshoot the issue.
ms.assetid: 7e5c8444-b3ee-4e9c-984f-13d54f2bbfc0
title: Using a Generic Host and Client for HTTP Metadata Exchange
ms.topic: article
ms.date: 05/31/2018
---

# Using a Generic Host and Client for HTTP Metadata Exchange

If the client and host cannot exchange metadata, then a generic host and client can be substituted for the custom host and client to help troubleshoot the issue. If the device address or device metadata does not appear in the WSD Debug Client output, then the supplied transport addresses or the network environment may be causing the failure. For more information about the generic host and client, see [Debugging Tools](debugging-tools.md).

If it has been verified that a generic host and client can complete both WS-Discovery and HTTP metadata exchange, then this diagnostic procedure can be skipped and troubleshooting can be continued by following the procedures in [Using WinHTTP Logging to Verify Get Traffic](using-winhttp-logging-to-verify-get-traffic.md).

If either the host or client is an application running on a PC, the generic host or client should be run in the same security context as the actual host or client. For example, if the actual host or client runs as Administrator, then the generic host or client must run as Administrator. Also, if either the host or client is a standalone device, it should be completely replaced by a PC running a generic host or client in a security context that guarantees unlimited network access (for example, running as Administrator).

**To using a generic host and client to troubleshoot HTTP metadata exchange**

1.  Open a command prompt window.
2.  Run the following command: **WSDDebug\_host.exe /mode metadata /start**

    > [!Note]  
    > A **Windows Security Alert** dialog box may appear. If so, click **Unblock** to allow the WSD Debug Host to run.

     

    This command generates output similar to the following. Make a note of the device ID.

    ``` syntax
    WSDAPI Debug Host
    Copyright (C) Microsoft Corporation 2007.  All rights reserved.
    Device ID is urn:uuid:37f86d35-e6ac-4241-964f-1d9ae46fb366
    Host metadata>
    ```

3.  Run the following command: **WSDDebug\_client.exe /mode metadata /hello off /resolve** *&lt;id&gt;*. Replace *&lt;id&gt;* with the device ID identified in step 2.
    > [!Note]  
    > A **Windows Security Alert** dialog box may appear. If so, click **Unblock** to allow the WSD Debug Client to run.

     

WSD Debug Client generates output similar to the following.

``` syntax
WSDAPI Debug Client
Copyright (C) Microsoft Corporation 2007.  All rights reserved.
Client ID is urn:uuid:0f571af7-6b0e-4daf-8054-f2233ac27910
Hello mode is disabled
Client metadata>
*****************************************************************************
Add at 02/28/07 15:16:51
+ EPR:
  + Address:                 urn:uuid:37f86d35-e6ac-4241-964f-1d9ae46fb366
+ Types:
    (wsdp) https://schemas.xmlsoap.org/ws/2006/02/devprof:Device
+ XAddrs:
  https://[::1]:5357/37f86d35-e6ac-4241-964f-1d9ae46fb366
+ Metadata version:          2
+ Instance ID:               1
+ Probe/Resolve tag:         WSDAPI debug_client
+ Remote transport address:  [::1]:3702
+ Local transport address:   ::1
+ Local interface GUID:      42133cd4-6a70-11db-bbc9-806e6f6e6963
Client metadata>
*****************************************************************************
Getting metadata for host at 02/28/07 15:16:51:
+ Endpoint reference:
  + Address:
    urn:uuid:37f86d35-e6ac-4241-964f-1d9ae46fb366
Using xAddr: https://[::1]:5357/37f86d35-e6ac-4241-964f-1d9ae46fb366
Client metadata>
*****************************************************************************
Metadata for host:
+ Endpoint reference:
  + Address:           urn:uuid:37f86d35-e6ac-4241-964f-1d9ae46fb366
Metadata section:
  + Dialect:
    https://schemas.xmlsoap.org/ws/2006/02/devprof/ThisDevice
  + Friendly name:
    [no lang]: Debugging Host
  + Firmware version:  1.0
  + Serial number:     00000000
Metadata section:
  + Dialect:
    https://schemas.xmlsoap.org/ws/2006/02/devprof/ThisModel
  + Manufacturer:
    [no lang]: Microsoft Corporation
  + Manufacturer URL:  https://www.microsoft.com/
  + Model names:
    [no lang]: Microsoft Debugging Host
  + Model number:      https://www.microsoft.com/
End of metadata
Client metadata>
```

The WSD Debug Client may generate a lot of output on a network with many DPWS devices. The output can be redirected to a file for easier analysis. Type **log tee** *&lt;filename&gt;* at the WSD Debug Client prompt to redirect output to a file. Output redirection can be stopped by typing **log tee stop** at the WSD Debug Client prompt.

Make a note of the endpoint reference (EPR) address. This EPR address should match the device ID identified in step 2 above. Also, verify that the WSD Debug Client completely printed the metadata for the device. The device metadata begins with `Metadata for host` and ends with `End of metadata`.

If the device ID and device metadata appears correctly in the WSD Debug Client output, then the application failure is likely not related to the supplied transport addresses, the operating system, or the network environment. Replace the generic host and client with the custom host and client, and continue troubleshooting by following the procedures in [Using WinHTTP Logging to Verify Get Traffic](using-winhttp-logging-to-verify-get-traffic.md).

If the device address and device metadata do not appear in the WSD Debug Client output, then the failure could have one or more of the following causes:

-   The transport address advertised by the host is incorrect or malformed. WSD Debug Client attempts to get device metadata from the URL provided in the **XAddrs** element of a [ProbeMatches](probematches-message.md) or [ResolveMatches](resolvematches-message.md) message. The URL used for metadata exchange appears in the WSD Debug Client output, prefixed by the phrase `Using xAddr`. The following example shows the XAddrs used for metadata exchange in the above WSD Debug Client output.

    ``` syntax
    Using xAddr: https://[::1]:5357/37f86d35-e6ac-4241-964f-1d9ae46fb366
    ```

    If the supplied XAddrs do not conform to the [XAddr validation rules](xaddr-validation-rules.md), then the WSD Debug Client cannot get the device's metadata.

-   The application is running in the wrong security context. Verify that the application is using the correct credentials and that the client and host have sufficient permission to access the network.
-   The firewall configuration is wrong. Follow the instructions in [Inspecting Adapter and Firewall Settings](inspecting-adapter-and-firewall-settings.md) to verify that the Windows Firewall settings are correct and that there are no other rules dropping the packets. The client and host can also be copied onto a "pristine" machine (one with a default operating system installation that has never been joined to a domain) in order to attempt to reproduce the failure.
-   An IPSec policy is blocking the application. Copy the client and host onto a machine that is not subject to IPSec policies and try to reproduce the failure.

## Related topics

<dl> <dt>

[WSDAPI Diagnostic Procedures](wsdapi-diagnostic-procedures.md)
</dt> <dt>

[Getting Started with WSDAPI Troubleshooting](getting-started-with-wsdapi-troubleshooting.md)
</dt> </dl>

 

 



