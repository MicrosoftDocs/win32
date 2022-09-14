---
title: WinRM Best Practices
description: This topic explains some of the best practices for using the various features of the WinRM API.
ms.assetid: FC2CD030-199F-43C2-804E-9827EA2A46D5
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# WinRM Best Practices

This topic explains some of the best practices for using the various features of the WinRM API.

## Quotas

When a quota is hit, the WinRM service returns an error to the client. As a result, the client logic must explicitly retry the operation based on the returned error.

## Event subscriptions

When using Collector-initiated subscriptions, limit the number of remote computers to 500 and isolate the [Windows Event Collector](/windows/desktop/WEC/windows-event-collector) service (wecsvc) in a separate host process.

A connection error will hold a thread until it times out. A large number of simultaneous connection errors can cause thread pool exhaustion and render the server unresponsive.

 

 