---
title: WS-Management Protocol
description: A public standard for remotely exchanging management data with any computer device that implements the protocol.
ms.assetid: 2c47acd2-5d52-4e0f-8848-a11aff59f963
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# WS-Management Protocol

The WS-Management protocol was developed by a group of hardware and software manufacturers as a public standard for remotely exchanging management data with any computer device that implements the protocol.

## Standards

For more information about WS-Management protocol, see [Web Services for Management (WS-Management) Specification](https://dmtf.org/sites/default/files/standards/documents/DSP0226_1.2.0.pdf).

The intent of the protocol is to provide consistency and interoperability for management operations across many types of devices (including firmware) and operating systems. WS-Management protocol can be extended as new operations are identified by the IT industry.

The current implementation of the WS-Management protocol is based on the following standard specifications: HTTPS, SOAP over HTTP (WS-I profile), SOAP 1.2, WS-Addressing, WS-Transfer, WS-Enumeration, and WS-Eventing. For more information about the WS-Management standards and XML schemas see <https://dmtf.org/standards/wsman>

## Messages

The WS-Management protocol provides a standard for constructing XML [*messages*](windows-remote-management-glossary.md) using various web service standards such as [*WS-Addressing*](windows-remote-management-glossary.md) and [*WS-Transfer*](windows-remote-management-glossary.md). These standards define XML schemas for web service messages. The messages refer to a [*resource*](windows-remote-management-glossary.md) using a [*resource URI*](windows-remote-management-glossary.md). The WS-Management protocol adds a set of definitions for management operations and values. For example, WS-Transfer defines the Get, Put, Create, and Delete operations for a resource. WS-Management protocol adds Rename, Partial Get, and Partial Put.

The messages follow the conventions of [*Simple Object Access Protocol (SOAP)*](windows-remote-management-glossary.md) which is used by all web service protocols.

The following code example shows a message with a Get operation. This example is shown as an aid to understanding what the underlying messages look like. You do not need to know how to produce SOAP messages. The messages are assembled by Windows Remote Management when you execute a command using the **Winrm** command-line tool or run a script written with the [WinRM Scripting API](winrm-scripting-api.md).

The message is a request to get the instance of [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) with a **DeviceID** property of "c:" from a server named RemoteComputer. The request uses the HTTP transport through port 80. The account sending the request must be in the local administrators group on the remote computer.

The characters before the colon at the beginning of each tag indicate which standard defines the XML element. For example, ` <wsa:To>` indicates that the To element is defined by the WS-Addressing standard and `<s:Header>` indicates the beginning of the header content in a SOAP message. Be aware that the majority of the message is composed of XML elements defined by SOAP or WS-Addressing. WS-Management protocol adds MaxEnvelopeSize, Selector, and SelectorSet.


```XML
<s:Envelope xmlns:s="https://www.w3.org/2003/05/soap-envelope" 
            xmlns:a="https://schemas.xmlsoap.org/ws/2004/08/addressing" 
            xmlns:w="https://schemas.dmtf.org/wbem/wsman/1/wsman.xsd">
  <s:Header>
    <a:To>https://RemoteComputer:80/wsman</a:To> 
    <w:ResourceURI s:mustUnderstand="true">
      http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/Win32_logicaldisk
    </w:ResourceURI> 
    <a:ReplyTo>
    <a:Address s:mustUnderstand="true">
      https://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous
    </a:Address> 
    </a:ReplyTo>
    <a:Action s:mustUnderstand="true">
      https://schemas.xmlsoap.org/ws/2004/09/transfer/Get
    </a:Action> 
    <w:MaxEnvelopeSize s:mustUnderstand="true">153600</w:MaxEnvelopeSize> 
    <a:MessageID>uuid:4ED2993C-4339-4E99-81FC-C2FD3812781A</a:MessageID> 
    <w:Locale xml:lang="en-US" s:mustUnderstand="false"/> 
    <w:SelectorSet>
    <w:Selector Name="DeviceId">c:</w:Selector> 
    </w:SelectorSet>
    <w:OperationTimeout>PT60.000S</w:OperationTimeout> 
  </s:Header>
  <s:Body/> 
</s:Envelope>
```



## Related topics

<dl> <dt>

[About Windows Remote Management](about-windows-remote-management.md)
</dt> <dt>

[Remote Hardware Management](remote-hardware-management.md)
</dt> </dl>

 

 