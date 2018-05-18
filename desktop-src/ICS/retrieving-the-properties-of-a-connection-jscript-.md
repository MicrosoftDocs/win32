---
title: Retrieving the Properties of a Connection (JScript)
description: The following JScript code enumerates the connections on the local computer. For each connection, the code obtains a sharing configuration interface for the connection, and retrieves the properties for the connection.
ms.assetid: '5f39c71d-1a29-485a-9412-23b4d10d304a'
---

# Retrieving the Properties of a Connection (JScript)

\[Internet Connection Firewall may be altered or unavailable in subsequent versions. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The following JScript code enumerates the connections on the local computer. For each connection, the code obtains a sharing configuration interface for the connection, and retrieves the properties for the connection.


```JScript
Copyright (c) Microsoft Corporation.  All rights reserved.

function Main()
{
    // create net sharing manager
    var objShare = new ActiveXObject("HNetCfg.HNetShare.1");
    
    // get enumerator for every connection
    var objEveryColl = objShare.EnumEveryConnection;
    
    if (objEveryColl != null) {
        varCount = objEveryColl.Count;
        if (varCount > 0) {
            // convert to built-in Java-style enumerator
            var e = new Enumerator (objEveryColl);
            e.moveFirst();
            for (; !e.atEnd(); e.moveNext()) {

                // get an INetConnection interface (not an ole-automation object)
                var objNetConn = e.item();
                if (objNetConn != null) {

                    // find the right connection, by examining the NetConnectionProps
                    var objNCProps = objShare.NetConnectionProps (objNetConn);
                    if (objNCProps != null) {
                        var str = "";
                        
                        // select correct INetConnection using Name, Guid or Device name
                        str +=   "Name: "         + objNCProps.Name +
                                 ", Guid: "       + objNCProps.Guid +
                                 ", DeviceName: " + objNCProps.DeviceName +
                                 ", Status: "     + objNCProps.Status +
                                 ", MediaType: "  + objNCProps.MediaType;
                        WScript.Echo (str);

                        // add code here; for example, to enable the firewall on a named connection:
                        // if (objNCProps.Name != "Local Area Connection 2")
                        //     continue;
                        // var objShareCfg = objShare.INetSharingConfigurationForINetConnection (objNetConn);
                        // if (objShareCfg != null)
                        //     objShareCfg.EnableInternetFirewall();
                        // break;
                    }
                }
            }
        }
    }
}
```



 

 




