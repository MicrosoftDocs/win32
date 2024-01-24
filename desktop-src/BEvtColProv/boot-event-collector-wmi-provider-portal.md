---
description: The Boot Event Collector WMI provider provides access to connection and configuration information for the Setup and Boot Event Collection feature on Windows Server.
ms.assetid: ab9ac8f0-69a5-4a2d-8ee5-1f003aa1bb5b
ms.tgt_platform: multiple
title: Boot Event Collector WMI Provider
ms.topic: article
ms.date: 05/31/2018
---

# Boot Event Collector WMI Provider

## Purpose

The Boot Event Collector WMI provider provides access to connection and configuration information for the Setup and Boot Event Collection feature on Windows Server. This allows you to view a list of the current connections and the connection history between a collector server and its target computers. In addition, this provider allows you to manage the configuration of a collector server.

> [!Note]  
> The Boot Event Collector WMI provider is implemented in BEvtCol.exe.

 

## In this section

<dl> <dt>

[**TargetForwarding**](targetforwarding.md)
</dt> <dd>

Retrieves forwarding data from a target computer.

</dd> <dt>

[**TargetForwardingDestination**](targetforwardingdestination.md)
</dt> <dd>

The known destinations containing the collected data. Available only if the collector is running with the status log enabled.

</dd> <dt>

[**TargetForwardingHistory**](targetforwardinghistory.md)
</dt> <dd>

The recent history of changes to the forwarding data for a target computer.

</dd> <dt>

[**Control**](control.md)
</dt> <dd>

Control of the collector instance. Requires the Administrator (BA) privileges.

</dd> </dl>

 

 



