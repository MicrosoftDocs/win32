---
title: Enabling Internet Connection Firewall (VBScript)
description: Enabling Internet Connection Firewall (VBScript)
ms.assetid: 43211c86-c21b-4b88-851d-5e007d3556e3
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enabling Internet Connection Firewall (VBScript)

\[Internet Connection Firewall may be altered or unavailable in subsequent versions. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The following VBScript code first determines if Internet Connection Sharing and Internet Connection Firewall are available on the local computer. If so, the code enumerates the connections on the local computer, and enables Internet Connection Firewall on the connection that is specified as a command line argument.


```VB
' Copyright (C) Microsoft.  All rights reserved.

OPTION EXPLICIT

DIM ICSSC_DEFAULT, CONNECTION_PUBLIC, CONNECTION_PRIVATE, CONNECTION_ALL
DIM NetSharingManager
DIM PublicConnection, PrivateConnection
DIM EveryConnectionCollection

DIM objArgs
DIM con 

ICSSC_DEFAULT         = 0
CONNECTION_PUBLIC     = 0
CONNECTION_PRIVATE    = 1
CONNECTION_ALL        = 2

Main( )

sub Main( )
    Set objArgs = WScript.Arguments

    if objArgs.Count = 1 then
        con = objArgs(0)
        
        WScript.Echo con

        if Initialize() = TRUE then    
            GetConnectionObjects()

            FirewallTestByName(con)
        end if
    else
        DIM szMsg
        szMsg = "Invalid usage! Please provide the name of the connection as the argument." & chr(13) & chr(13) & _
                "Usage:" & chr(13) & _ 
                "       " + WScript.scriptname + " " + chr(34) + "Connection Name" + chr(34)
        WScript.Echo( szMsg )                
    end if

end sub


sub FirewallTestByName(conName)
on error resume next
    DIM Item
    DIM EveryConnection
    DIM objNCProps
    DIM szMsg
    DIM bFound
    
    bFound = false        
    for each Item in EveryConnectionCollection
        set EveryConnection = NetSharingManager.INetSharingConfigurationForINetConnection(Item)
        set objNCProps = NetSharingManager.NetConnectionProps(Item)
        if (ucase(conName) = ucase(objNCProps.Name)) then
            szMsg = "Enabling Firwall on connection:" & chr(13) & _
                    "Name: "       & objNCProps.Name & chr(13) & _
                    "Guid: "       & objNCProps.Guid & chr(13) & _
                    "DeviceName: " & objNCProps.DeviceName & chr(13) & _
                    "Status: "     & objNCProps.Status & chr(13) & _
                    "MediaType: "  & objNCProps.MediaType
            
            WScript.Echo(szMsg)
            bFound = true
            EveryConnection.EnableInternetFirewall
            exit for
        end if
    next
    
    if( bFound = false ) then
        WScript.Echo( "Connection " & chr(34) & conName & chr(34) & " was not found" )
    end if
    
end sub

function Initialize()
    DIM bReturn
    bReturn = FALSE

    set NetSharingManager = Wscript.CreateObject("HNetCfg.HNetShare.1")
    if (IsObject(NetSharingManager)) = FALSE then
        Wscript.Echo("Unable to get the HNetCfg.HnetShare.1 object")
    else
        if (IsNull(NetSharingManager.SharingInstalled) = TRUE) then
            Wscript.Echo("Sharing isn't available on this platform.")
        else
            bReturn = TRUE
        end if
    end if
    Initialize = bReturn
end function

function GetConnectionObjects()
    DIM bReturn
    DIM Item
    
    bReturn = TRUE
    
    if GetConnection(CONNECTION_PUBLIC) = FALSE then
        bReturn = FALSE
    end if
    
    if GetConnection(CONNECTION_PRIVATE) = FALSE then
        bReturn = FALSE
    end if
    
    if GetConnection(CONNECTION_ALL) = FALSE then
        bReturn = FALSE
    end if
    
    GetConnectionObjects = bReturn     
     
end function


function GetConnection(CONNECTION_TYPE)
    DIM bReturn     
    DIM Connection
    DIM Item
    bReturn = TRUE
    
    if (CONNECTION_PUBLIC = CONNECTION_TYPE) then
        set Connection = NetSharingManager.EnumPublicConnections(ICSSC_DEFAULT)
        if (Connection.Count > 0) and (Connection.Count < 2) then
            for each Item in Connection
                set PublicConnection = NetSharingManager.INetSharingConfigurationForINetConnection(Item)
            next          
        else
            bReturn = FALSE
        end if
    elseif (CONNECTION_PRIVATE = CONNECTION_TYPE) then
        set Connection = NetSharingManager.EnumPrivateConnections(ICSSC_DEFAULT)
        if (Connection.Count > 0) and (Connection.Count < 2) then
            for each Item in Connection
                set PrivateConnection = NetSharingManager.INetSharingConfigurationForINetConnection(Item)
            next
        else
            bReturn = FALSE
        end if
    elseif (CONNECTION_ALL = CONNECTION_TYPE) then
        set Connection = NetSharingManager.EnumEveryConnection
        if (Connection.Count > 0) then
            set EveryConnectionCollection = Connection
        else
            bReturn = FALSE
        end if
    else
        bReturn = FALSE
    end if
    
    if (TRUE = bReturn)  then
    
        if (Connection.Count = 0) then
            Wscript.Echo("No " + CStr(ConvertConnectionTypeToString(CONNECTION_TYPE)) + " connections exist (Connection.Count gave us 0)")
            bReturn = FALSE
        'valid to have more than 1 connection returned from EnumEveryConnection
        elseif (Connection.Count > 1) and (CONNECTION_ALL <> CONNECTION_TYPE) then          
            Wscript.Echo("ERROR: There was more than one " + ConvertConnectionTypeToString(CONNECTION_TYPE) + " connection (" + CStr(Connection.Count) + ")")
            bReturn = FALSE               
        end if
    end if
    Wscript.Echo(CStr(Connection.Count) + " objects for connection type " + ConvertConnectionTypeToString(CONNECTION_TYPE))
    
    GetConnection = bReturn
end function

function ConvertConnectionTypeToString(ConnectionID)
    DIM ConnectionString
    
    if (ConnectionID = CONNECTION_PUBLIC) then
        ConnectionString = "public"
    elseif (ConnectionID = CONNECTION_PRIVATE) then
        ConnectionString = "private"
    elseif (ConnectionID = CONNECTION_ALL) then
        ConnectionString = "all"
    else
        ConnectionString = "Unknown: " + CStr(ConnectionID)
    end if
    
    ConvertConnectionTypeToString = ConnectionString
end function


```



 

 




