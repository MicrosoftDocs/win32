---
title: Retrieving the Properties of a Connection (VBScript)
description: Retrieving the Properties of a Connection (VBScript)
ms.assetid: '72cbd58a-931d-41c6-b399-1184c83c7c0c'
---

# Retrieving the Properties of a Connection (VBScript)

\[Internet Connection Firewall may be altered or unavailable in subsequent versions. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The following VBScript code enumerates the connections on the local computer. For each connection, the code obtains a sharing configuration interface for the connection, and retrieves the properties for the connection.


```VB
' Copyright (C) Microsoft.  All rights reserved.

Main( )

function Main()
    DIM objShare
    DIM objEveryColl
    
    set objShare = Wscript.CreateObject("HNetCfg.HNetShare.1")
    if(IsObject(objShare) = FALSE ) then
        exit function
    end if
    
    set objEveryColl = objShare.EnumEveryConnection
    
    if (IsObject(objEveryColl) = TRUE) then
    
    DIM objNetConn
    
    for each objNetConn in objEveryColl
      DIM objShareCfg
      set objShareCfg = objShare.INetSharingConfigurationForINetConnection(objNetConn)
      if (IsObject(objShareCfg) = TRUE) then
        DIM objNCProps
        set objNCProps = objShare.NetConnectionProps(objNetConn)
        if (IsObject(objNCProps) = TRUE) then
          DIM str
          str = "Name: "   & objNCProps.Name & chr(13) & _
          "Guid: "       & objNCProps.Guid & chr(13) & _
          "DeviceName: " & objNCProps.DeviceName & chr(13) & _
          "Status: "     & objNCProps.Status & chr(13) & _
          "MediaType: "  & objNCProps.MediaType
            
          WScript.Echo( str )
          'Add code here.
        end if
        
      end if
    next
    end if
    
end function
```



 

 




