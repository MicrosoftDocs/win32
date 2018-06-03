---
title: Adding and Removing Port Mappings (JScript)
description: Adding and Removing Port Mappings (JScript)
ms.assetid: 845887de-4b68-480c-8081-bc56bd0f45ff
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding and Removing Port Mappings (JScript)

\[Internet Connection Firewall may be altered or unavailable in subsequent versions. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The following JScript demonstrates adding and removing port mappings from network connections. First the code adds a port mapping to every shared or firewalled connection on the local computer. The code then enumerates the connections in order to identify those that have port mappings added, and removes the port mappings from those connections.


```JScript
Copyright (c) Microsoft Corporation.  All rights reserved.

ICSSC_DEFAULT = 0;

ICSTT_NAME      = 0;
ICSTT_IPADDRESS = 1;

// from netcon.idl
//NCM_SHAREDACCESSHOST_LAN = 8;
//NCM_SHAREDACCESSHOST_RAS = 9;

NAT_PROTOCOL_TCP = 6
NAT_PROTOCOL_UDP = 17

// from netcon.idl
NCCF_SHARED     = 0x0100;   // Connection is shared
NCCF_FIREWALLED = 0x0400;   // Connection is firewalled

WScript.Echo ("Starting....");
Main();
WScript.Echo ("Ending....");

function Main()
{
    var objShare = new ActiveXObject("HNetCfg.HNetShare.1");
    if (objShare == null)
        WScript.Echo ("failed to create HNetCfg.HNetShare object!");
    else
        DoTheWork (objShare);
    return;
}

function DoTheWork (objShare)
{
    var objEveryConnColl = objShare.EnumEveryConnection;
    if (objEveryConnColl == null) 
        WScript.Echo ("failed to get EveryConnectionCollection!");
    else {
        // enum INetConnections until props are correct
        var objEveryEnum = new Enumerator (objEveryConnColl);
        if (objEveryEnum == null)
            WScript.Echo ("failed to create Enumerator from EveryConnectionCollection");
        else {
            for (objEveryEnum.moveFirst(); !objEveryEnum.atEnd(); objEveryEnum.moveNext()) {

                var objNetConn = objEveryEnum.item();
                if (objNetConn == null)
                    WScript.Echo ("can't get any net connections!");
                else {
                    var objNetConnProps = objShare.NetConnectionProps (objNetConn);
                    if (objNetConnProps == null)
                        WScript.Echo ("can't get net connection props!");
                    else {
                        if ((objNetConnProps.Characteristics & NCCF_SHARED) ||
                            (objNetConnProps.Characteristics & NCCF_FIREWALLED))
                        {
                            // found one!
                            var objShareConf = objShare.INetSharingConfigurationForINetConnection (objNetConn);
                            if (objShareConf == null)
                                WScript.Echo ("can't make INetSharingConfiguration object!");
                            else {
                                AddAsymmetricPortMapping (objShareConf);
                                WScript.Echo ("added a port mapping named 'Ben's Port Mapping'.");
                            }
                        }
                    }
                }
            }
        }
    }

    // do other work here.
    // when you're done,
    // clean up port mapping
    WScript.Echo ("cleaning up");
    if (objShareConf != null)
        DeletePortMapping (objShareConf, NAT_PROTOCOL_TCP, 555, 444);
}

function AddAsymmetricPortMapping (objShareConf)
{
    // in case it exists already....
    DeletePortMapping (objShareConf, NAT_PROTOCOL_TCP, 555, 444);

    var objPortMapping = objShareConf.AddPortMapping (
                                "Ben's Port Mapping",
                                NAT_PROTOCOL_TCP,
                                555,
                                444,
                                0,
                                "compnametst2", ICSTT_NAME);
// or                           "192.168.0.2", ICSTT_IPADDRESS);

    if (objPortMapping != null) {
        WScript.Echo ("just added NAT_PROTOCOL_TCP, 555, 444!");
        
        objPortMapping.Enable();
        WScript.Echo ("just enabled port mapping!");
    } else
        WScript.Echo ("failed to add asymmetric port mapping!");
}

function DeletePortMapping (objShareConf, typeProtocol, iExternalPort, iInternalPort)
{
    // enum, deleting match, if any
    var objPMColl = objShareConf.EnumPortMappings (ICSSC_DEFAULT);
    if (objPMColl == null)
        WScript.Echo ("can't get 'every' collection!");
    else {
        var varEnumerator = new Enumerator (objPMColl);
        if (varEnumerator != null) {
            for (varEnumerator.moveFirst(); !varEnumerator.atEnd(); varEnumerator.moveNext()) {
                var objPortMapping = varEnumerator.item();
                if (objPortMapping != null) {
                    var objPMProps = objPortMapping.Properties;
                    if (objPMProps != null) {
                        if ((objPMProps.IPProtocol   == typeProtocol ) &amp;&amp;
                            (objPMProps.ExternalPort == iExternalPort) &amp;&amp;
                            (objPMProps.InternalPort == iInternalPort))
                        {
                            objPortMapping.Delete();
                            // or objShareConf.RemovePortMapping (objPortMapping);

                            WScript.Echo ("just deleted " + typeProtocol + ", " + iExternalPort + ", " + iInternalPort + "!")
                        }
                    }
                }
            }
        }
    }
}
```



 

 




