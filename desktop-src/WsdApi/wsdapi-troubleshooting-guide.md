---
Description: 'The purpose of this guide is to help users troubleshoot failures encountered when using WSDAPI discovery APIs, when creating a WSDAPI host or device proxy, or when using operating system functions (such as Function Discovery or the Network Explorer) that rely on WSDAPI.'
ms.assetid: 'fc01fc66-627a-497f-98dd-613f5d85f6cb'
title: WSDAPI Troubleshooting Guide
---

# WSDAPI Troubleshooting Guide

The purpose of this guide is to help users troubleshoot failures encountered when using WSDAPI discovery APIs, when creating a WSDAPI host or device proxy, or when using operating system functions (such as [Function Discovery](https://msdn.microsoft.com/library/windows/desktop/aa814070) or the Network Explorer) that rely on WSDAPI. The primary goal is to help troubleshoot when a client and host cannot see each other on the network.

For WSDAPI users, this guide contains information that will help you successfully troubleshoot a device proxy (using [**WSDCreateDeviceProxy**](wsdcreatedeviceproxy.md)), a discovery provider (using [**WSDCreateDiscoveryProvider**](wsdcreatediscoveryprovider-func.md)), or a discovery publisher (using [**WSDCreateDiscoveryPublisher**](wsdcreatediscoverypublisher-func.md)).

This guide assumes that both the client and host can correctly interoperate with WSDAPI in a controlled environment. Accordingly, this guide is not intended to help troubleshoot DPWS stacks that may be generating improper WS messages. For information on testing interoperability with WSDAPI, see the [WSDAPI Basic Interoperability Tool (WSDBIT)](http://go.microsoft.com/fwlink/p/?linkid=150223) in the Windows Driver Kit (WDK).

Before you begin troubleshooting your application, you should familiarize yourself with [Discovery and Metadata Exchange Message Patterns](discovery-and-metadata-exchange-message-patterns.md).

This guide contains the following sections.

-   [Getting Started with WSDAPI Troubleshooting](getting-started-with-wsdapi-troubleshooting.md)
-   [WSDAPI Diagnostic Procedures](wsdapi-diagnostic-procedures.md)
-   [Troubleshooting HTTPS Secure Channel Communication](troubleshooting-https-secure-channel-communication.md)

 

 



