---
description: Correlation affects the set of classes returned from the SMIR.
ms.assetid: 799a0866-e7a0-492f-956e-b13bf591babe
ms.tgt_platform: multiple
title: WMI SNMP Class Correlation
ms.topic: article
ms.date: 05/31/2018
---

# WMI SNMP Class Correlation

Correlation affects the set of classes returned from the SMIR. Correlated classes are those that a given SNMP device is known to support at the time enumeration occurs. Noncorrelated enumeration returns all classes present within the SMIR, regardless of whether the device supports them. Correlation is a feature of the WMI SNMP provider and can be turned off or on (default).

> [!Note]  
> For more information about installing the provider, see [Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md).

 

Correlation might prevent you from seeing all of the classes that are actually supported by a device. If you know that a particular class is supported but it does not appear in the SMIR, this could be due to several reasons, one of which is correlation. Consider turning correlation off before writing to the device in question. However, turning correlation off results in the likelihood that many classes not supported by the device will appear in the SMIR. Also, there is a performance cost in using correlation because the device is queried to see what classes it supports. When correlation is turned on, the SNMP provider causes an enumeration of device-supported classes similar to the result of running a *mib walk* tool.

For example, a network manager wants to know several key pieces of data about all the managed hubs in a particular network. A database of the current devices and their supported MIBs already exists, so there is no need to rely on the correlation function of the device to provide the supported data elements. In this case, correlation could be turned off.

The following example shows how to turn off correlation.


```VB
set objNamedValueSet = CreateObject( _
    "WbemScripting.SWbemNamedValueSet") 
objNamedValueSet.Add "Correlate", FALSE, 0
```



On the other hand, another network manager may want to monitor all the UNIX machine disk drives on the network but is unfamiliar with the MIB data on those machines. In that case, correlation would be turned on.

 

 



