---
description: If the client and host cannot see each other on the network, then a generic host and client can be substituted for the custom host and client to help troubleshoot the issue.
ms.assetid: e82ce911-b2a7-4a57-a2f0-9aca6b74478f
title: Using a Generic Host and Client for UDP WS-Discovery
ms.topic: article
ms.date: 05/31/2018
---

# Using a Generic Host and Client for UDP WS-Discovery

If the client and host cannot see each other on the network, then a generic host and client can be substituted for the custom host and client to help troubleshoot the issue. If the device address does not appear in the WSD Debug Client output, then the network environment is probably causing the failure. For more information about the generic host and client, see [Debugging Tools](debugging-tools.md).

If either the host or client is an application running on a PC, the generic host or client should be run in the same security context as the actual host or client. For example, if the actual host or client runs as Administrator, then the generic host or client must run as Administrator. Also, if either the host or client is a standalone device, it should be completely replaced by a PC running a generic host or client.

**To using a generic host and client to troubleshoot UDP WS-Discovery**

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
```

The WSD Debug Client may generate a lot of output on a network with many DPWS devices. The output can be redirected to a file for easier analysis. Type **log tee** *&lt;filename&gt;* at the WSD Debug Client prompt to redirect output to a file. Output redirection can be stopped by typing **log tee stop** at the WSD Debug Client prompt.

Make a note of the endpoint reference (EPR) address. This EPR address should match the device ID identified in step 2 above. If this is the case, then the application failure is likely not related to the operating system or the network environment. Replace the generic host and client with the custom host and client, and continue troubleshooting by following the procedures in [Using WSD Debug Client to Verify Multicast Traffic](using-wsddebug-client-to-verify-multicast-traffic.md).

If the device ID does not match the EPR address, then the application failure is probably related to the operating system or the network environment. The failure could have one or more of the following causes:

-   The application is running in the wrong security context. Verify that the application is using the correct credentials and that the client and host have sufficient permission to access the network.
-   The firewall configuration is wrong. Follow the instructions in [Inspecting Adapter and Firewall Settings](inspecting-adapter-and-firewall-settings.md) to verify that the Windows Firewall settings are correct and that there are no other rules dropping the packets. The client and host can also be copied onto a "pristine" machine (one with a default operating system installation that has never been joined to a domain) in order to attempt to reproduce the failure.
-   An IPSec policy is blocking the application. Copy the client and host onto a machine not subject to IPSec policies and try to reproduce the failure.

## Related topics

<dl> <dt>

[WSDAPI Diagnostic Procedures](wsdapi-diagnostic-procedures.md)
</dt> <dt>

[Getting Started with WSDAPI Troubleshooting](getting-started-with-wsdapi-troubleshooting.md)
</dt> </dl>

 

 



