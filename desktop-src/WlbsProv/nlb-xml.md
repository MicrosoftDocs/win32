---
title: Nlb.xml
description: Nlb.xml is an XML document containing configuration information.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 055caea0-ac4a-45d1-8b77-1ba1efe28b30
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Nlb.xml

Nlb.xml is an XML document containing configuration information. NlbScriptLib.vbs parses this document to plug in values for the cluster IP address, the dedicated IP address, and so on. To extend the document to include more setting and configuration information, simply add more tags.

Note that Nlb.xml is a basic XML document. To store configuration information for an entire cluster, a DTD or an XML schema would enforce a uniform object model.

``` syntax
<?xml version="1.0" encoding="US-ASCII"?>
<!-- NLB Cluster Configuration Data (single node only) -->
<!-- TODO:  Change these values to reflect your cluster! -->
<nodeinfo>
  <clusterIP>172.50.66.14</clusterIP>
  <dedicatedIP>172.50.35.12</dedicatedIP>
  <hostID>1</hostID>
  <portnumber>65535</portnumber>
</nodeinfo>
```

 

 




