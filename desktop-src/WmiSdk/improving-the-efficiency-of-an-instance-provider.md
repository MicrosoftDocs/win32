---
Description: 'A WMI high-performance provider greatly increases the speed at which a WMI client can obtain information from a WMI instance provider.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '767a16bb-44b6-4c56-b79b-23241fcc216e'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: Improving the Efficiency of an Instance Provider
---

# Improving the Efficiency of an Instance Provider

A WMI high-performance provider greatly increases the speed at which a WMI client can obtain information from a WMI instance provider. The main change is that a high-performance provider runs as an in-process server to either the client application or to WMI. By placing the provider inside the client process, you can speed up the interaction between the two.

For more information about how to make your instance provider a high-performance provider, see [Making an Instance Provider into a High-Performance Provider](making-an-instance-provider-into-a-high-performance-provider.md).

 

 



