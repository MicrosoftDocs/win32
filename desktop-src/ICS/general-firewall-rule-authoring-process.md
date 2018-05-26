---
title: General Firewall Rule Authoring Process
description: When planning the firewall rules for your feature, you must analyze the networking requirements and component dependencies.
ms.assetid: fbb2d683-0fd3-4bcd-ade5-bd8643d4daf4
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# General Firewall Rule Authoring Process

When planning the firewall rules for your feature, you must analyze the networking requirements and component dependencies. Your feature may have processes, services and drivers that send or receive traffic and those components may depend on other network-facing components that are external to your feature.

## Identifying Networking Requirements

The first step in firewall rule creation is to identify which components in your feature are network-facing. A network-facing component is defined as one that uses network sockets in-process.

Identify network-facing applications — identify the full path to applications that use the network, the protocols that are used and the ports that are used (if applicable)

Identify network-facing services — identify the short service names for the services that use the network, the protocols that are utilized and the ports that are used (if applicable)

Identify network-facing drivers — identify the protocols that are utilized and the ports that are used (if applicable)

It may be helpful to construct a table to record each of the above items. A sample is provided below.



| Component   | Path                    | Short Svc Name | Direction | Protocol | (UDP/TCP) Port | Group | Purpose                                        |
|-------------|-------------------------|----------------|-----------|----------|----------------|-------|------------------------------------------------|
| Application | %system32%\\calc.exe    | N/A            | Inbound   | TCP      | 13555          | Core  | Allow calculator to access web service         |
| Application | %system32%\\calc.exe    | N/A            | Inbound   | UDP      | 1466           | Admin | Allow calculator to discover other calculators |
| Service     | %system32%\\svchost.exe | foosvc         | Outbound  | TCP      | 38555          | Core  | Allow foosvc to send reports                   |
| Driver      | System                  | N/A            | Inbound   | UDP      | 4566           | Core  | Allow foo.sys to receive notifications         |



 

> [!Note]  
> For kernel mode drivers, the application path should be set to system.

 

## Identifying Dependencies

The next step is to identify network-facing dependencies. This could be as simple as enumerating the out-of-proc transports utilized by your feature or as complex as tracing out all the applications, services or drivers that your feature depends on which are not covered in the first step.

Common out-of-process transports are listed in the table below.



| Abbreviation | Name                                          | Usage                                                                    |
|--------------|-----------------------------------------------|--------------------------------------------------------------------------|
| RPC          | Remote Procedure Call                         | Commonly used by components for remote management                        |
| SSDP         | Simple Service Discovery Protocol             | Primarily used for device discovery                                      |
| UPnP         | Universal Plug and Play                       | Used in conjunction with SSDP for device discovery and management        |
| WSD          | Web Services for Devices                      | A replacement for UPnP for discovering and managing WSD capable entities |
| WMI          | Windows Management Instrumentation            | Commonly used by components for remote management                        |
| DCOM         | Distributed Component Object Model            | Commonly used for remote COM activation within components                |
| HTTP.Sys     | HyperText Transfer Protocol Engine            | Used by components requiring HTTP parsing                                |
| MSDTC        | Microsoft Distributed Transaction Coordinator | Used by components requiring transactions                                |



 

The firewall rule requirements when dependent on one of the above transports are described in detail in a later section, [Firewall Rules Needed for Common Transports](firewall-rules-needed-for-common-transports.md). If your component is dependent on a specific Windows component, you may enable the applicable rule group.

 

 




