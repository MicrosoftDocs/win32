---
title: Enabling EAPHost Tracing
description: Can assist users in finding the root causes of issues that occur during the EAP authentication process. The debugging information can include API calls performed, internal function calls performed, and state transitions performed.
ms.assetid: 5f401101-59aa-4ee8-825a-0b998489eed9
ms.topic: article
ms.date: 05/31/2018
---

# Enabling EAPHost Tracing

Trace logs containing debugging information can assist users in finding the root causes of issues that occur during the EAP authentication process. The debugging information can include API calls performed, internal function calls performed, and state transitions performed.

Tracing can be enabled on both the client side and the authenticator side. Tracing can also be enabled for calls to the [Routing and Remote Access Service (RRAS)](/windows/desktop/RRAS/routing-start-page) APIs. For more information, see [Tracing on the Routing and Remote Access Service](#tracing-on-the-routing-and-remote-access-service).

>[!NOTE]
>Trace logs are available in English only.

When EAPHost tracing is enabled, logging information is stored in an .etl file in a user-specified location. If errors occur during EAP authentication, tracing generates an .etl file that can be sent to Microsoft Developer Support for root cause analysis. Partners that have access to Microsoft windows build shares, symbols, and traceformat files can convert the .etl files into a plain text file using the **tracerpt** tool.

Network policy server (NPS) failures are not captured in the EAPHost logs. If you are trying to troubleshoot a NPS failure, view the IASSAM.LOG and IASNAP.LOG files (see [Tools for Troubleshooting NAP - Log files](/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/dd348461(v=ws.10)#log-files)).

## Tracing on the Client

To enable tracing on the client side:

1. Open an elevated command prompt window.
2. Run the following command: **logman** **start trace** **EapHostPeer** **-o** **.\\EapHostPeer.etl** **-p** **{5F31090B-D990-4e91-B16D-46121D0255AA} 0x4000ffff 0** **-ets**
3. Reproduce the scenario that you want to trace.
4. Run the following command: **logman** **stop** **EapHostPeer** **-ets**
5. Convert the etl file into text using the following command: **tracerpt EapHostPeer.etl** **–pdb** **&lt;pdbpath&gt;** **-tp** **&lt;tracemessagefilesdirectorypath&gt;** **-o** **EapHostPeer.txt**
    > [!NOTE]  
    > If you do not have access to the tracerpt tool, avoid the last step and send the .etl file to Microsoft Developer Support.

## Tracing on the Authenticator

To enable tracing on the authenticator side:

1. Open an elevated command prompt window.
2. Run the following command: **logman** **start trace** **EapHostAuthr** **-o** **.\\EapHostAuthr.etl** **-p** **{F6578502-DF4E-4a67-9661-E3A2F05D1D9B} 0x4000ffff 0** **-ets**
3. Reproduce the scenario that you want to trace.
4. Run the following command: **logman** **stop** **EapHostAuthr** **-ets**
5. Convert the etl file into text using the following command: **tracerpt EapHostAuthr.etl** **–pdb** **&lt;pdbpath&gt;** **-tp** **&lt;tracemessagefilesdirectorypath&gt;** **-o** **EapHostAuthr.txt**
    > [!Note]  
    > If you do not have access to the tracerpt tool, avoid the last step and instead send the .etl file to Microsoft Developer Support.

## Event tracing

In Windows 7 and later versions of Windows, EapHost provides event based tracing on the authenticator and the peer. The advantage of event based tracing is that no symbol files are needed to view the trace messages. To enable event tracing:

1. Open **EventViewer**.
2. Critical EapHost messages are logged under: “Custom Views\\Administrative Events”
3. Non-critical messages are logged under: “Applications and Services\\Microsoft\\Windows\\EapHost
4. "Analytic" and "Debug" type event messages can be seen under the same path by selecting **Show Analytic and Debug Logs** from the **view** menu in the title bar.

## Tracing on the Routing and Remote Access Service

To enable RRAS tracing:

1. Open an elevated command prompt window.
2. Run the following command: **netsh** **ras** **set** **tr** **\*** **en**
3. Open **%systemroot%\\tracing** to view RAS traces

To disable RRAS tracing:

1. Open an elevated command prompt window.
2. Run the following command: **netsh** **ras** **set** **tr** **\*** **dis**

For more information, see [Netsh Commands](/previous-versions/windows/it-pro/windows-server-2003/cc779693(v=ws.10)).

## Related topics

[Using EAPHost](using-eap-host.md)

[Routing and Remote Access Service (RRAS)](/windows/desktop/RRAS/routing-start-page)
