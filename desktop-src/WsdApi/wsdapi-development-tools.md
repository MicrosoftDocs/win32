---
description: The WSDAPI development tools included in the Windows SDK (WSD CodeGen, WSD Debug Host, and WSD Debug Client) enable developers to create and debug WSDAPI-based clients and devices.
ms.assetid: 8bf6424e-1eed-4b0a-9d56-7aaf03a47992
title: WSDAPI Development Tools
ms.topic: article
ms.date: 05/31/2018
---

# WSDAPI Development Tools

The WSDAPI development tools included in the Windows SDK (WSD CodeGen, WSD Debug Host, and WSD Debug Client) enable developers to create and debug WSDAPI-based clients and devices. The source code for these tools is not available. SDK tools are located in the following directory: \<Windows SDK Install Folder>\\Bin.

WSD CodeGen (wsdcodegen.exe) converts a WSDL contract into generated C++ code, which developers can call directly into. It handles the data serialization and wire representation so developers can focus on designing applications. For more information about WSD CodeGen, see [Web Services on Devices Code Generator](web-services-for-devices-code-generator.md). This tool is available in the Microsoft Windows Software Development Kit (SDK) and in the Windows Driver Kit (WDK).

The WSD Debug Host (wsddebug\_host.exe) and WSD Debug Client (wsddebug\_client.exe) tools help developers debug their clients and hosts. These tools can be used to verify and inspect WS-Discovery and metadata exchange traffic. For more information about WSD Debug Host and WSD Debug Client, see [Debugging Tools](debugging-tools.md). These tools are available only in the Windows SDK.

There is an additional development tool, named [WSDAPI Basic Interoperability Tool (WSDBIT)](https://msdn.microsoft.com/library/cc264250.aspx), that is available only in the WDK. This tool is used for testing service methods, Message Transmission Optimization Mechanism (MTOM), attachments or WS-Eventing.

## Related topics

<dl> <dt>

[WSD Application Development on Windows](wsd-application-development-on-windows.md)
</dt> <dt>

[Web Services on Devices Code Generator](web-services-for-devices-code-generator.md)
</dt> <dt>

[WSDAPI Basic Interoperability Tool (WSDBIT)](https://msdn.microsoft.com/library/cc264250.aspx)
</dt> <dt>

[Debugging Tools](debugging-tools.md)
</dt> </dl>

 

 



