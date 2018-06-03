---
Description: This topic provides a glossary of technical terms used in the Offline Files API and WMI provider documentation.
Robots: noindex, nofollow
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 05235ca5-dca0-4e6e-8686-83fc9c043306
ms.prod: windows-server-dev
ms.technology: offline-files
ms.tgt_platform: multiple
title: Offline Files Glossary
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Offline Files Glossary

This topic provides a glossary of technical terms used in the Offline Files API and WMI provider documentation.

<dl> <dt>

<span id="of.offline_files_glossary_active"></span><span id="OF.OFFLINE_FILES_GLOSSARY_ACTIVE"></span>**active**
</dt> <dd>

The Offline Files feature is active if it is currently running. If the Offline Files feature is active but not enabled, the computer must be restarted to complete the transition from disabled to enabled.

</dd> <dt>

<span id="of.offline_files_glossary_cache_object"></span><span id="OF.OFFLINE_FILES_GLOSSARY_CACHE_OBJECT"></span>**cache object**
</dt> <dd>

Represents the Offline Files cache as a whole, providing facilities to add items to the cache, find items in the cache, enumerate items in the cache, remove items from the cache, and synchronize items in the cache with their corresponding copies on a server.

</dd> <dt>

<span id="of.offline_files_glossary_client_side_caching"></span><span id="OF.OFFLINE_FILES_GLOSSARY_CLIENT_SIDE_CACHING"></span>**client-side caching (CSC)**
</dt> <dd>

Another name for the Offline Files feature.

</dd> <dt>

<span id="of.offline_files_glossary_disabled"></span><span id="OF.OFFLINE_FILES_GLOSSARY_DISABLED"></span>**disabled**
</dt> <dd>

The Offline Files feature is disabled if it is not configured to run. If the Offline Files feature is disabled but is currently running, the computer must be restarted to complete the transition from enabled to disabled.

</dd> <dt>

<span id="of.offline_files_glossary_enabled"></span><span id="OF.OFFLINE_FILES_GLOSSARY_ENABLED"></span>**enabled**
</dt> <dd>

The Offline Files feature is enabled if it is configured to run. If the Offline Files feature is enabled but not running, the computer must be restarted to complete the transition from disabled to enabled.

</dd> <dt>

<span id="of.offline_files_glossary_event_sink"></span><span id="OF.OFFLINE_FILES_GLOSSARY_EVENT_SINK"></span>**event sink**
</dt> <dd>

An instance of the IWbemEventSink class. An Offline Files application or script creates an event sink and registers it to receive progress notifications for an Offline Files operation.

</dd> <dt>

<span id="of.offline_files_glossary_item_object"></span><span id="OF.OFFLINE_FILES_GLOSSARY_ITEM_OBJECT"></span>**item object**
</dt> <dd>

Represents a single server, share, directory, or file in the cache. Item objects are available primarily for querying state about the items. An interested process locates a particular item explicitly or enumerates sets of items then examines and evaluates the state of those returned items.

</dd> </dl>

 

 



