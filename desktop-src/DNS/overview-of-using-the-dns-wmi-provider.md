---
title: Overview of Using the DNS WMI Provider
description: The following general steps get you started in creating your own script or program that makes use of the DNS WMI Provider.
ms.assetid: d9d64bda-0564-4074-9f0a-a249c7315042
ms.topic: article
ms.date: 05/31/2018
---

# Overview of Using the DNS WMI Provider

The following general steps get you started in creating your own script or program that makes use of the DNS WMI Provider.

**To create a script or program using the DNS WMI Provider**

1.  Connect to the DNS WMI Provider.
    ```VB
    Set objLocator = CreateObject("WbemScripting.SWbemLocator")

    'Connect to the namespace which is either local or remote
    Set objService = objLocator.ConnectServer (strServer, strNameSpace, _
                                                                                                                                                                                strUserName, strPassword)
    ```

    

    > [!Note]  
    > The name space for the DNS WMI Provider will always be "root\\microsoftdns".

     

2.  Get a DNS Server instance.
    ```VB
    set objServer = objService.Get("MicrosoftDNS_Server.name="".""")
    ```

    

3.  Depending on the type action you want to perform, get a DNS zone or record instance.
    ```VB
    Set objDNSSet = objService.Get("MicrosoftDNS_ZONE")
    Set objDNSset = objService.Get("MicrosoftDNS_Zone.ContainerName=""" _
                                                                    & strZoneArray(0) & """,DnsServerName=""" & _ 
                    objServer.Name & """,Name=""" & _
                    strZoneArray(0) & """")
    ```

    

4.  Perform the desired actions:
    -   Execute a method
    -   Display a property
    -   Modify a property (must have Read/Write access)

 

 




