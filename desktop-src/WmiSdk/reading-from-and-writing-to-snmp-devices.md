---
description: SNMP devices can be accessed by reading from or writing to their corresponding class instance in the WMI SMIR (SNMP Module Information Repository).
ms.assetid: af5e1321-b552-447e-a217-eecbebe1f203
ms.tgt_platform: multiple
title: Reading from and Writing to SNMP Devices
ms.topic: article
ms.date: 05/31/2018
---

# Reading from and Writing to SNMP Devices

SNMP devices can be accessed by reading from or writing to their corresponding class instance in the WMI SMIR (SNMP Module Information Repository). When you are working with multiple devices of the same type, for efficiency, load the MIBs for one SNMP device type into the SMIR.

> [!Note]  
> For more information about installing the provider, see [Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md).

 

Select one of the following options to read to or write from each SNMP device type by updating the context information of the instance before communicating with each one.

-   Use a DNS name instead of the IP address when referencing a specific device.

    The following example shows how to use the DNS name for a specific device.

    ```VB
    strNamedValue = Context.Add("AgentAddress", "Router1" )
    ```

    

-   Create a separate namespace and associate a device address to the namespace object using the AgentAddress instance qualifier so that the namespace is permanently bound to the device. In this case, you need not specify the context object information.
-   Read from an SNMP device.

    The following example performs a Get operation on a device class.

    ```VB
    Set objLocator = CreateObject("wbemscripting.swbemlocator")
    Set objServices = objLocator.ConnectServer(, "root\snmp\mngd_hub")
    objServices.security_.privileges.AddAsString("SeSecurityPrivilege")
    Set objSet = objServices.ExecQuery _
        ("SELECT * FROM SNMP_NET_DEVICE_123 WHERE hdwr_idx>1",, _
          wbemFlagReturnWhenComplete)
    for each obj in objset 
      'do whatever 
    next
    ```

    

-   Write to an SNMP device.

    The following example performs a Set operation on a device class.

    ```VB
    Set objLocator = CreateObject("wbemscripting.swbemlocator")
    Set objServices = objLocator.ConnectServer(, "root\snmp\mngd_hub")
    objServices.security_.privileges.AddAsString("SeSecurityPrivilege")
    Set obj= objServices.Get("SNMP_NET_DEVICE_123=@")
    obj.deviceLocation = "40/5073"
    obj.put_
    ```

    

Correlated classes are those that a given SNMP device is known to support when enumeration occurs. Correlation affects the set of classes returned from the SMIR. Noncorrelated enumeration returns all classes present within the SMIR, regardless of whether the device supports them. For more information about using WMI correlation techniques, see [WMI SNMP Class Correlation](wmi-snmp-class-correlation.md).

 

 



