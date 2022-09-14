---
description: The purpose of this guide is to help users troubleshoot failures encountered when using WSDAPI discovery APIs, when creating a WSDAPI host or device proxy, or when using operating system functions (such as Function Discovery or the Network Explorer) that rely on WSDAPI.
ms.assetid: fc01fc66-627a-497f-98dd-613f5d85f6cb
title: WSDAPI Troubleshooting Guide
ms.topic: article
ms.date: 05/31/2018
---

# WSDAPI Troubleshooting Guide

The purpose of this guide is to help users troubleshoot failures encountered when using WSDAPI discovery APIs, when creating a WSDAPI host or device proxy, or when using operating system functions (such as [Function Discovery](/previous-versions/windows/desktop/fundisc/fd-portal) or the Network Explorer) that rely on WSDAPI. The primary goal is to help troubleshoot when a client and host cannot see each other on the network.

For WSDAPI users, this guide contains information that will help you successfully troubleshoot a device proxy (using [**WSDCreateDeviceProxy**](/windows/desktop/api/WsdClient/nf-wsdclient-wsdcreatedeviceproxy)), a discovery provider (using [**WSDCreateDiscoveryProvider**](/windows/desktop/api/WsdDisco/nf-wsddisco-wsdcreatediscoveryprovider)), or a discovery publisher (using [**WSDCreateDiscoveryPublisher**](/windows/desktop/api/WsdDisco/nf-wsddisco-wsdcreatediscoverypublisher)).

This guide assumes that both the client and host can correctly interoperate with WSDAPI in a controlled environment. Accordingly, this guide is not intended to help troubleshoot DPWS stacks that may be generating improper WS messages. For information on testing interoperability with WSDAPI, see the [WSDAPI Basic Interoperability Tool (WSDBIT)](https://msdn.microsoft.com/library/cc264250.aspx) in the Windows Driver Kit (WDK).

Before you begin troubleshooting your application, you should familiarize yourself with [Discovery and Metadata Exchange Message Patterns](discovery-and-metadata-exchange-message-patterns.md).

This guide contains the following sections.

-   [Getting Started with WSDAPI Troubleshooting](getting-started-with-wsdapi-troubleshooting.md)
-   [WSDAPI Diagnostic Procedures](wsdapi-diagnostic-procedures.md)
