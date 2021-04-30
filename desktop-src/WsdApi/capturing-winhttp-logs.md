---
description: WinHTTP logs can be used to help troubleshoot WSDAPI applications. This is helpful when metadata exchange fails or when SSL/TLS negotiation fails.
ms.assetid: 75ba330d-afcd-4d8f-93c7-a1b9f80dd050
title: Capturing WinHTTP Logs
ms.topic: article
ms.date: 05/31/2018
---

# Capturing WinHTTP Logs

[WinHTTP](/windows/desktop/WinHttp/winhttp-start-page) logs can be used to help troubleshoot WSDAPI applications. This is helpful when metadata exchange fails or when SSL/TLS negotiation fails.

This procedure shows how to capture WinHTTP logs on the client PC. The WSDAPI-based client application must not be running when logging is enabled. If the client application is running when logging is enabled, the client and/or the PC must be restarted before WS-Discovery and metadata exchange traffic will appear in the WinHTTP logs.

**To capture WinHTTP logs**

1.  Open an elevated command prompt window on the client PC.
2.  Run the following command: **netsh winhttp set tracing trace-file-prefix="C:\\Temp\\dpws" level=verbose format=ansi state=enabled max-trace-file-size=1073741824**

    This command enables WinHTTP logging. All log files will be stored in the C:\\Temp directory, and the filenames will begin with the dpws prefix. At most 1 GB of log files will be stored.

3.  If the process using WinHTTP on the client is already running, restart the computer. For example, if the [Function Discovery](/previous-versions/windows/desktop/fundisc/fd-portal) APIs are being used, the computer must be restarted. The Function Discovery APIs call WinHTTP from inside a service host, which may have already started when tracing was enabled.
4.  Start the WSDAPI-based client application. The application being debugged or the WSD Debug Client can be used.
5.  Reproduce the application failure.
6.  Terminate the WSDAPI-based client application.
7.  If the process using WinHTTP is not terminated with the client application, restart the computer. For example, if the [Function Discovery](/previous-versions/windows/desktop/fundisc/fd-portal) APIs are being used, the computer must be restarted.
8.  Run the following command: **netsh winhttp set tracing state=disabled**

    This command disables WinHTTP logging.

9.  Inspect the DPWS logs in C:\\Temp and verify that the required requests and messages were sent.
10. If secure channel (HTTPS) communication is being used, check for SSL/TLS failures.

Once WinHTTP logs have been captured, the logs can be examined to look for the cause of a WSDAPI application failure. Note that the text editor used to view these logs must be run as Administrator. For more information, see [Using WinHTTP Logging to Verify Get Traffic](using-winhttp-logging-to-verify-get-traffic.md).

## Related topics

<dl> <dt>

[WinHTTP](/windows/desktop/WinHttp/winhttp-start-page)
</dt> <dt>

[Using WinHTTP Logging to Verify Get Traffic](using-winhttp-logging-to-verify-get-traffic.md)
</dt>
</dl>
