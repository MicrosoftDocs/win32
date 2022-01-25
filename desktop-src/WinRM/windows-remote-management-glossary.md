---
title: Windows Remote Management Glossary
description: Glossary page
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: bbda0db7-f473-444b-85ab-f3c5240c4b18
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Windows Remote Management Glossary


<dl> <dt>

****wsman:Items****
</dt> <dd>

A WS-Management protocol element returned in an enumeration that obtains both the instances and the instance [*EPRs*](/windows). **wsman:Items** is a container that holds an instance and its EPR. This type of enumeration is initiated when the **WSManFlagReturnObjectAndEPR** flag is set in the request.

</dd> </dl>

## B

<dl> <dt>

**baseboard management controller (BMC)**
</dt> <dd>

A microcontroller attached locally to a server. BMCs have sensors that monitor the physical state of the server and a separate network connection that can communicate over the network, even if the server is offline. You have access to BMC data through the [*Intelligent Platform Management Interface (IPMI)*](windows-remote-management-glossary.md) WMI provider.

</dd> <dt>

**Basic authentication**
</dt> <dd>

The user name and password sent in the authentication exchange. Basic authentication can be configured to use either HTTP or HTTPS transport in a domain or workgroup. This method is the least secure method of authentication.

</dd> <dt>

**BMC**
</dt> <dd>

See [*baseboard management controller (BMC)*](windows-remote-management-glossary.md).

</dd> </dl>

## C

<dl> <dt>

**CIM**
</dt> <dd>

See [*Common Information Model (CIM)*](windows-remote-management-glossary.md).

</dd> <dt>

**client**
</dt> <dd>

The client application using the WS-Management protocol to access the management service on either the local or a remote computer.

</dd> <dt>

**Common Information Model (CIM)**
</dt> <dd>

The [*Distributed Management Task Force (DMTF)*](windows-remote-management-glossary.md) model that describes how to represent real-world computer and network objects. CIM uses an object-oriented paradigm, where managed objects are modeled using the concepts of classes and instances.

</dd> </dl>

## D

<dl> <dt>

**Digest authentication**
</dt> <dd>

An exchange wherein the server receives a request from a client and sends data about the client to an authenticating server, typically a domain controller. If the client is authenticated, then the server receives a Digest session key used to authenticate subsequent requests from the client.

</dd> <dt>

**Distributed Management Task Force (DMTF)**
</dt> <dd>

The industry organization developing management standards and integration technology for enterprise and Internet environments.

</dd> <dt>

**DMTF**
</dt> <dd>

See [*Distributed Management Task Force (DMTF)*](windows-remote-management-glossary.md).

</dd> </dl>

## E

<dl> <dt>

**endpoint**
</dt> <dd>

A resource that can be addressed by an [*endpoint reference (EPR)*](windows-remote-management-glossary.md).

</dd> <dt>

**endpoint reference (EPR)**
</dt> <dd>

A combination of WS-Addressing and WS-Management addressing elements that together describe an address for a resource in the message SOAP header. This is a web service term.

</dd> <dt>

**enumeration**
</dt> <dd>

A set, or collection, of [*resource*](windows-remote-management-glossary.md) instances or the action of requesting such a set. In WS-Management protocol, [*WS-Enumeration*](windows-remote-management-glossary.md) is used to obtain the collection. In the WinRM service scripting implementation of enumeration, [**Session.Enumerate**](session-enumerate.md) and the [**Enumerator**](enumerator.md) object are used. The corresponding C++ method and interface are [**IWSManSession::Enumerate**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmansession-enumerate) and [**IWSManEnumerator**](/windows/desktop/api/WSManDisp/nn-wsmandisp-iwsmanenumerator).

</dd> <dt>

**EPR**
</dt> <dd>

See [*endpoint reference (EPR)*](windows-remote-management-glossary.md).

</dd> <dt>

**Event Collection Service**
</dt> <dd>

The operating system component that receives events from the BMC and other operating system components or applications.

</dd> <dt>

**event forwarding**
</dt> <dd>

A notification of events that occur on remote computers can be sent to subscribing applications. Event forwarding is not a feature of WinRM, but of the [Windows Event Log](/windows/desktop/WES/windows-event-log). Event forwarding becomes available for the first time in Windows Vista. The Management applications, such as Microsoft Operations Manager (MOM) use event forwarding.

</dd> </dl>

## F

<dl> <dt>

**filter**
</dt> <dd>

A query mechanism for specifying a limited set of instances in the request for a [*resource*](windows-remote-management-glossary.md). You can specify a *filter* parameter on calls to [**Session.Enumerate**](session-enumerate.md) or [**IWSManSession::Enumerate**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmansession-enumerate).

</dd> <dt>

**filter dialect**
</dt> <dd>

An XML string that identifies the XML dialect used to specify a [*filter*](windows-remote-management-glossary.md) in a call to [**Session.Enumerate**](session-enumerate.md) or [**IWSManSession::Enumerate**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmansession-enumerate). The WinRM service supports [WQL](/windows/desktop/WmiSdk/wql-sql-for-wmi) as a filter dialect when receiving requests.

</dd> <dt>

**fragment**
</dt> <dd>

An XML string that identifies part of an instance of a resource rather than the entire resource. Fragment support is found in the [**ResourceLocator**](resourcelocator.md) object.

</dd> <dt>

**fragment dialect**
</dt> <dd>

An XML string that identifies the XML dialect used to specify a [*fragment*](windows-remote-management-glossary.md). Fragment support is found in the [**ResourceLocator**](resourcelocator.md) object. The WinRM service supports [*XPath*](windows-remote-management-glossary.md) for fragment dialect when receiving requests.

</dd> </dl>

## I

<dl> <dt>

**in-band**
</dt> <dd>

The client application obtains BMC data through the WinRM [*listener*](windows-remote-management-glossary.md) in the operating system.

</dd> <dt>

**Intelligent Platform Management Interface (IPMI)**
</dt> <dd>

An IT industry standard for the architecture of [*baseboard management controller (BMC)*](windows-remote-management-glossary.md). The Windows hardware management features supply an [*IPMI driver*](windows-remote-management-glossary.md) and a WMI [*IPMI provider*](windows-remote-management-glossary.md) that allow management scripts, command-line tools, and applications to obtain BMC data. The IPMI provider has WMI [classes](/previous-versions/windows/desktop/ipmiprv/ipmi-provider).

</dd> <dt>

**IPMI**
</dt> <dd>

See [*Intelligent Platform Management Interface (IMPI)*](windows-remote-management-glossary.md).

</dd> <dt>

**IPMI driver**
</dt> <dd>

The kernel driver that enables access to [*baseboard management controller (BMC)*](windows-remote-management-glossary.md) devices from the operating system components.

</dd> <dt>

**IPMI provider**
</dt> <dd>

A standard WMI provider that defines classes modeling the [*IPMI*](windows-remote-management-glossary.md) and its data. The [IPMI provider](/previous-versions/windows/desktop/ipmiprv/ipmi-provider) is a COM DLL that obtains data from the BMC.

</dd> </dl>

## K

<dl> <dt>

**KCS**
</dt> <dd>

See [*Keyboard Controller Style (KCS)*](windows-remote-management-glossary.md).

</dd> <dt>

**Kerberos authentication**
</dt> <dd>

A method of mutual authentication between the client and server that uses encrypted keys. For computers running on a Windows-based operating system, the client account must be a domain account in the same domain as the server. When a client uses default credentials, Kerberos is the authentication method if the connection string is not one of the following: localhost, 127.0.0.1, or \[::1\].

</dd> <dt>

**Keyboard Controller Style (KCS)**
</dt> <dd>

The protocol used by the [*IPMI driver*](windows-remote-management-glossary.md) to communicate with the [*baseboard management controller (BMC)*](windows-remote-management-glossary.md).

</dd> </dl>

## L

<dl> <dt>

**listener**
</dt> <dd>

A management service that implements WS-Management protocol to send and receive messages. WinRM is a listener service. A listener is defined by a transport (HTTP or HTTPS) and an IPv4 or IPv6 address. You can create more than one WinRM listener instance on a single computer by giving them a different TCP/IP address or port number.

</dd> </dl>

## M

<dl> <dt>

**message**
</dt> <dd>

A package of information transmitted between computers or separate networks constructed with the [*SOAP*](windows-remote-management-glossary.md) protocol. The package has a header, that describes the message target and transport, and a body that contains the content to be used when the message arrives. A message is a combination of elements from specifications such as [*WS-Addressing*](windows-remote-management-glossary.md), [*WS-Transfer*](windows-remote-management-glossary.md), and [*WS-Management*](windows-remote-management-glossary.md).

</dd> </dl>

## N

<dl> <dt>

**namespace**
</dt> <dd>

A [*WMI*](windows-remote-management-glossary.md) namespace, which is a logical grouping of WMI classes and instances to control scope and access. The most frequent source of management data for systems running Windows is the root\\cimv2 namespace, which contains classes such as [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process). Namespaces appear in the resource URI for WMI classes, for example `https://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/Win32\_Service`.

</dd> <dt>

**Negotiate authentication**
</dt> <dd>

A negotiated, single sign on type of authentication that is the Windows implementation of [*Simple and Protected GSSAPI Negotiation Mechanism (SPNEGO)*](windows-remote-management-glossary.md). SPNEGO negotiation determines whether authentication is handled by Kerberos or NTLM. Kerberos is the preferred mechanism. Negotiate authentication on Windows-based systems is also called Windows Integrated Authentication.

</dd> <dt>

**numeric sensor**
</dt> <dd>

A numeric type of sensor in a [*baseboard management controller (BMC)*](windows-remote-management-glossary.md), for example temperature or voltage.

</dd> </dl>

## O

<dl> <dt>

**option**
</dt> <dd>

The additional data required by the resource provider to process a request. For example, some WMI providers require additional data supplied as [**IWbemContext**](/windows/desktop/api/wbemcli/nn-wbemcli-iwbemcontext) or [**SWbemNamedValueSet**](/windows/desktop/WmiSdk/swbemnamedvalueset) objects. Option support is found in the [**ResourceLocator**](resourcelocator.md) object.

</dd> <dt>

**out-of-band**
</dt> <dd>

The client application obtains data directly from the [*baseboard management controller (BMC)*](windows-remote-management-glossary.md) of another computer, rather than through the WinRM [*listener*](windows-remote-management-glossary.md) in the operating system.

</dd> </dl>

## P

<dl> <dt>

**pull**
</dt> <dd>

A [*WS-Enumeration*](windows-remote-management-glossary.md) pull message is sent to continue an enumeration started by an initial call to WS-Enumeration:Enumerate. The pull operation in the WinRM service is performed by [**Enumerator.ReadItem**](enumerator-readitem.md) or [**IWSManEnumerator::ReadItem**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmanenumerator-readitem).

</dd> </dl>

## R

<dl> <dt>

**resource**
</dt> <dd>

An [*endpoint*](windows-remote-management-glossary.md) that represents a distinct type of management operation or value. A service exposes one or more resources and some resources can have more than one instance. A management resource is similar to a WMI class or a database table, and an instance is similar to an instance of the class or a row in the table. For example, the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class represents a resource. `Win32_LogicalDisk="C:\"` is a specific instance of the resource.

</dd> <dt>

**resource URI**
</dt> <dd>

The [*uniform resource identifier (URI)*](windows-remote-management-glossary.md) used to identify a specific type of resource, such as disks or processes, on a system.

</dd> </dl>

## S

<dl> <dt>

**SEL**
</dt> <dd>

See [*System Event Log (SEL)*](windows-remote-management-glossary.md).

</dd> <dt>

**SEL adapter**
</dt> <dd>

The adapter that sends [*baseboard management controller (BMC)*](windows-remote-management-glossary.md) data to the [*Event Collector*](windows-remote-management-glossary.md).

</dd> <dt>

**selector**
</dt> <dd>

A name and value pair that represents a particular instance of a [*resource*](windows-remote-management-glossary.md). This is essentially a filter or "key" that identifies the desired instance of the resource. Selector support is found in the [**ResourceLocator**](resourcelocator.md) object.

</dd> <dt>

**sensor**
</dt> <dd>

A measurement device in a [*baseboard management controller (BMC)*](windows-remote-management-glossary.md).

</dd> <dt>

**service**
</dt> <dd>

An application that provides management services to clients through the WS-Management protocol and other [*web services*](windows-remote-management-glossary.md). A service is usually the same as the [*listener*](windows-remote-management-glossary.md) on a network. The service has a physical transport address.

</dd> <dt>

**session**
</dt> <dd>

A connection between a Windows Remote Management [*client*](windows-remote-management-glossary.md) and the local or remote WinRM [*listener*](windows-remote-management-glossary.md), or service. This connection is similar to the connection between a WMI client script and WMI on a remote server. The session operations, such as enumerating a resource (Enumerate), getting an instance of a resource (Get), or running a resource method (Invoke) are methods of the **Session** object. A **Session** object is created by [**WSMan.CreateSession**](wsman-createsession.md).

</dd> <dt>

**Simple and Protected GSS-API Negotiation Mechanism (SPNEGO)**
</dt> <dd>

An authentication mechanism used by the client or server receiving requests for data through the WinRM in an Active Directory context. SPNEGO is based on an Request For Comments (RFC) protocol produced by the Internet Engineering Task Force (IETF). SPNEGO is also known as [*Windows Integrated Authentication*](windows-remote-management-glossary.md), the term used in the Windows Remote Management help topics.

</dd> <dt>

**Simple Object Access Protocol (SOAP)**
</dt> <dd>

An XML-based protocol used by web services.

</dd> <dt>

**SOAP**
</dt> <dd>

See [*Simple Object Access Protocol (SOAP)*](windows-remote-management-glossary.md).

</dd> <dt>

**SPNEGO**
</dt> <dd>

See [*Simple and Protected GSS-API Negotiation Mechanism (SPNEGO)*](windows-remote-management-glossary.md).

</dd> <dt>

**System Event Log (SEL)**
</dt> <dd>

The database of events in the [*baseboard management controller (BMC)*](windows-remote-management-glossary.md) hardware. The [*SEL adapter*](windows-remote-management-glossary.md) conveys these events to the operating system.

</dd> </dl>

## U

<dl> <dt>

**uniform resource identifier (URI)**
</dt> <dd>

A string that identifies a resource in the enterprise, such as a computer, a process, a disk drive, or a temperature sensor in a [*baseboard management controller (BMC)*](windows-remote-management-glossary.md). The URI is the web service addressing mechanism defined in Internet Engineering Task Force (IETF) Uniform Resource Identifier (URI): Generic Syntax \[RFC3986\].

</dd> <dt>

**URI**
</dt> <dd>

See [*uniform resource identifier (URI)*](windows-remote-management-glossary.md).

</dd> </dl>

## W

<dl> <dt>

**web service**
</dt> <dd>

A software application used for interaction between computers across the Internet or a network. Web services are described by the [*Web Service Description Language (WSDL)*](windows-remote-management-glossary.md). The specific description of the web service tells other services how to interact with the web service by using SOAP messages. The messages are conveyed between computers by a transport, typically HTTP or HTTPS. [*WS-Addressing*](windows-remote-management-glossary.md), [*WS-Eventing*](windows-remote-management-glossary.md), and [*WS-Management*](windows-remote-management-glossary.md) are examples of protocols used by web service applications to communicate with each other.

</dd> <dt>

**Web Service Description Language (WSDL)**
</dt> <dd>

An XML-based language used to define how to interact with a web service. Typically, the WSDL describes what SOAP messages the web service requires to return data or carry out operations. The WSDL allows an implementation from one operating system to communicate with the web service implemented on another operating system, as long as the requirements of the WSDL are met.

</dd> <dt>

**Windows Integrated Authentication**
</dt> <dd>

See [*Negotiate authentication*](windows-remote-management-glossary.md).

</dd> <dt>

**Windows Management Instrumentation (WMI)**
</dt> <dd>

The Microsoft implementation of the Web-Based Enterprise Management (WBEM) standard published by the [*Distributed Management Task Force (DMTF)*](windows-remote-management-glossary.md). WMI allows you to manage local and remote computers and models computer and network objects using an extension of the [*Common Information Model (CIM)*](windows-remote-management-glossary.md) standard.

</dd> <dt>

**Windows Remote Management (WinRM)**
</dt> <dd>

The Microsoft implementation of a management web service based on the public standard [*WS-Management*](windows-remote-management-glossary.md) protocol.

</dd> <dt>

**Windows Remote Shell (WinRS)**
</dt> <dd>

A shell tool that relies on [*Windows Remote Management*](windows-remote-management-glossary.md) to execute remote commands, especially for headless servers. The command-line tool is Winrs.

</dd> <dt>

**WMI**
</dt> <dd>

See [*Windows Management Instrumentation (WMI)*](windows-remote-management-glossary.md).

</dd> <dt>

**WMI plug-in**
</dt> <dd>

The WinRM plug-in that makes WMI data available to WinRM clients.

</dd> <dt>

**WS-Addressing (wsa)**
</dt> <dd>

A public standard protocol, which is SOAP-based, that creates an addressing system used in the headers of messages sent across the Internet. The standard defines how resources can be located across networks and firewalls. WS-Addressing is one of the web service protocols which compose the WS-Management protocol.

</dd> <dt>

**WS-Enumeration (wsen)**
</dt> <dd>

A public standard protocol, which is SOAP-based, for enumerating a sequence of XML elements that may represent data collections, logs, or other linear information structures. WS-Enumeration is one of the web service protocols which compose the WS-Management protocol.

</dd> <dt>

**WS-Eventing (wse)**
</dt> <dd>

A public standard protocol, which is SOAP-based, that allows one web service (the subscriber) to subscribe to and accept event notification messages from another web service (the event source). WS-Eventing is one of the web service protocols which compose the WS-Management protocol.

</dd> <dt>

**WS-Management**
</dt> <dd>

A public standard protocol, which is SOAP-based, for sharing management data among all operating systems, computers, and devices. All [*messages*](windows-remote-management-glossary.md) sent by the WinRM client or server components use this protocol.

</dd> <dt>

**WS-Transfer (wxf)**
</dt> <dd>

A public standard protocol, which is SOAP-based, for accessing XML representations of web service-based resources through a simple set of verbs such as Get, Put, Invoke, or Delete. WS-Transfer defines operations for sending and receiving the representation of a particular resource and operations for creating or deleting a resource and its corresponding representation.

</dd> </dl>

## X

<dl> <dt>

**XPath**
</dt> <dd>

A path notation for addressing parts of an XML document, similar to a URL. An XPath expression is a sequence of phrases to get from the current location in the XML document to another node or set of nodes. The phrases are separated by forward-slash ("/") characters. The WinRM service supports [XPath](/previous-versions/dotnet/netframework-4.0/ms256115(v=vs.100)) for [*fragment dialect*](windows-remote-management-glossary.md).

</dd> </dl>

 

 
