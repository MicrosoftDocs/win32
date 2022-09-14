---
title: DNS WMI Provider Samples—Managing DNS Zones
description: DNS WMI Provider Samples—Managing DNS Zones
ms.assetid: 12958b71-b47d-4dd7-bd08-409ecd369e4f
keywords:
- DNS WMI Provider Samples 8212;Managing DNS Zones
ms.topic: article
ms.date: 05/31/2018
---

# DNS WMI Provider Samples—Managing DNS Zones

This section demonstrates scripting tasks associated with managing DNS zones. The following links link to subroutines in the script file.

-   [Create a DNS zone](#create-a-dns-zone)
-   [Modify a DNS zone](#modify-a-dns-zone)
-   [Delete a DNS zone](#delete-a-dns-zone)
-   [Add a zone IP address](#add-a-zone-ip-address)
-   [Delete a zone IP address](#delete-a-zone-ip-address)
-   [Pause a zone](#pause-a-zone)
-   [Resume a zone](#resume-a-zone)
-   [Update a zone](#update-a-zone)
-   [Reload a zone](#reload-a-zone)
-   [Refresh a zone](#refresh-a-zone)


```VB
'***********************************************************
'*
'*  File:           DnsZones.vbs
'*
'*  Main Function:  Gets and sets DNS Zone information for a computer.
'*
'********************************************************************

OPTION EXPLICIT

    'Define constants
    CONST CONST_ERROR                   = 0
    CONST CONST_WSCRIPT                 = 1
    CONST CONST_CSCRIPT                 = 2
    CONST CONST_SHOW_USAGE              = 3
    CONST CONST_DISPLAY                 = 4
    CONST CONST_LIST                    = 5
    CONST CONST_CREATE                  = 6
    CONST CONST_MODIFY                  = 7
    CONST CONST_DELETE                  = 8
    CONST CONST_ADDIP                   = 9
    CONST CONST_DELETEIP                = 10
    CONST CONST_PAUSE                   = 11
    CONST CONST_RESUME                  = 12
    CONST CONST_WRITE                   = 13
    CONST CONST_UPDATE                  = 14
    CONST CONST_RELOAD                  = 15
    CONST CONST_REFRESH                 = 16
    
    ' Declare variables.
    Dim intOpMode, i
    Dim strServer, strUserName, strPassword, strOutputFile
    Dim strPropertyArray(), strValueArray(), strZoneArray()
    Dim blnContextHelp
    
    ' Ensure that the host is script, if not then abort.
    VerifyHostIsCscript()

    ' Parse the command line.
    intOpMode = intParseCmdLine(strServer        , _
                                strUserName      , _
                                strPassword      , _
                                strOutputFile    , _
                                strPropertyArray , _
                                strValueArray    , _
                                strZoneArray     , _
                                blnContextHelp     )

    Select Case intOpMode

        Case CONST_SHOW_USAGE
            Call ShowUsage()

        Case CONST_DISPLAY
            Call Display(strOutputFile, blnContextHelp)

        Case CONST_LIST
            Call DnsZoneList(strServer        , _
                             strUserName      , _
                             strPassword      , _
                             strOutputFile    , _
                             strPropertyArray , _
                             blnContextHelp     )

        Case CONST_CREATE
            Call DnsCreate(strServer        , _
                           strUserName      , _
                           strPassword      , _
                           strOutputFile    , _
                           strPropertyArray , _
                           blnContextHelp     )

        Case CONST_MODIFY
            Call DnsModify(strServer        , _
                           strUserName      , _
                           strPassword      , _
                           strOutputFile    , _
                           strPropertyArray , _
                           strValueArray    , _
                           strZoneArray     , _
                           blnContextHelp     )

        Case CONST_DELETE
            Call DnsDelete(strServer        , _
                           strUserName      , _
                           strPassword      , _
                           strOutputFile    , _
                           strPropertyArray , _
                           blnContextHelp     )

        Case CONST_ADDIP
            Call DnsADDIP(strServer        , _
                          strUserName      , _
                          strPassword      , _
                          strOutputFile    , _
                          strZoneArray     , _
                          strPropertyArray , _
                          strValueArray    , _
                          blnContextHelp     )

        Case CONST_DELETEIP
            Call DnsDELETEIP(strServer        , _
                             strUserName      , _
                             strPassword      , _
                             strOutputFile    , _
                             strZoneArray     , _
                             strPropertyArray , _
                             strValueArray    , _
                             blnContextHelp     )
        Case CONST_PAUSE
            Call DnsPause(strServer     , _
                          strUserName   , _
                          strPassword   , _
                          strOutputFile , _
                          strZoneArray  , _
                          blnContextHelp  )

        Case CONST_RESUME
            Call DnsResume(strServer     , _
                           strUserName   , _
                           strPassword   , _
                           strOutputFile , _
                           strZoneArray  , _
                           blnContextHelp  )

        Case CONST_WRITE
            Call DnsWrite(strServer     , _
                          strUserName   , _
                          strPassword   , _
                          strOutputFile , _
                          strZoneArray  , _
                          blnContextHelp  )

        Case CONST_UPDATE
            Call DnsUpdate(strServer     , _
                           strUserName   , _
                           strPassword   , _
                           strOutputFile , _
                           strZoneArray  , _
                           blnContextHelp  )

        Case CONST_RELOAD
            Call DnsReload(strServer     , _
                           strUserName   , _
                           strPassword   , _
                           strOutputFile , _
                           strZoneArray  , _
                           blnContextHelp  )

        Case CONST_REFRESH
            Call DnsRefresh(strServer     , _
                            strUserName   , _
                            strPassword   , _
                            strOutputFile , _
                            strZoneArray  , _
                            blnContextHelp  )

        Case CONST_ERROR
            Call Wscript.Echo("Error occurred in passing parameters.")

        Case Else                    ' Default - should never occur.
            Call Wscript.Echo("Error occurred in passing parameters.")

    End Select

'********************************************************************
'* End of Script
'********************************************************************

'********************************************************************
'*
'* Sub DnsZoneList()
'*
'* Purpose: Lists the value of all server properties.
'*
'* Input:   strServer           A server name
'*          strUserName         The current user name
'*          strPassword         The current user password
'*          strOutputFile       An output file name
'*          strPropertyArray    An array of zone properties
'*          blnContextHelp      Show context sensitve Help
'*
'* Output:  Results are either printed on screen or saved in 
'*          strOutputFile.
'*
'********************************************************************

Sub DnsZoneList(strServer        , _
                strUserName      , _
                strPassword      , _
                strOutputFile    , _
                strPropertyArray , _
                blnContextHelp     )


    ON ERROR RESUME NEXT

    Dim objFileSystem, objOutputFile, objService, objDNS, objInst
    Dim objServer, strMessage
    
    If blnContextHelp then
        Wscript.Echo ""
        Wscript.Echo "Displays the current Zone settings."
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo "  DnsZones List [zonename] [/S <server>]"
        Wscript.Echo "                [/U <username>] [/W <password>]"
        Wscript.Echo "                [/O <outputfile>]"
                Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   server        A server name"
        Wscript.Echo "   username      The current user name"
        Wscript.Echo "   password      The current user password"
        Wscript.Echo "   outputfile    The output file name"
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Wscript.Echo "1.  DnsZones.vbs List"
        Wscript.Echo "    Displays a list of all zones."
        Wscript.Echo "2.  DnsZones.vbs List example.com"
        Wscript.Echo "    Displays details on example.com."
        Wscript.Echo ""
        Exit Sub
    End If

    ' Open a text file for output if the file is requested.
    If Not IsEmpty(strOutputFile) Then
        If (NOT blnOpenFile(strOutputFile, objOutputFile)) Then
            Call Wscript.Echo ("Cannot open an output file.")
            Exit Sub
        End If
    End If

    ' Establish a connection with the server.
    If blnConnect("root\microsoftdns" , _
                   strUserName , _
                   strPassword , _
                   strServer   , _
                   objService  ) Then
        Call Wscript.Echo("")
        Call Wscript.Echo("Verify the server name, credentials and WBEM Core.")
        Exit Sub
    End If

    If IsEmpty(strPropertyArray(0)) then

        Set objDNS = objService.InstancesOf("MicrosoftDNS_Zone")
        If blnErrorOccurred("DNS Server not available.") then Exit Sub


        If objDNS.Count = 0 Then
          Call Wscript.Echo("No zones are available.")
          Exit Sub
        End If

        Call Wscript.Echo("Zones on Server " & strServer)
        Call Wscript.Echo("")

        strMessage = strPackString("Zone Name", 40, True, True)
        strMessage = strMessage + strPackString("Type", 10, True, True)
        strMessage = strMessage + strPackString("Revers", 10, True, True)
        strMessage = strMessage + strPackString("Pause", 10, True, True)
        strMessage = strMessage + strPackString("ShutDown", 10, True, True)
        Call WriteLine(strMessage, objOutputFile)

        For Each objInst In objDNS
            strMessage = strPackString(objInst.ContainerName, 40, True, True)
            strMessage = strMessage + strPackString(objInst.ZoneType,10, True, True)
            strMessage = strMessage + strPackString(objInst.Reverse, 10, True, True)
            strMessage = strMessage + strPackString(objInst.Paused, 10, True, True)
            strMessage = strMessage + strPackString(objInst.Shutdown, 10, True, True)
            Call WriteLine(strMessage, objOutputFile)

            Call WriteLine("", objOutputFile)
        Next
    Else
        set objServer = objService.Get ("MicrosoftDNS_Server.name="".""")
        Set objDNS = objService.Get( _ 
        "MicrosoftDNS_Zone.ContainerName=""" & strPropertyArray(0) _
        & """,DnsServerName=""" & objServer.Name & """,Name=""" _
        & strPropertyArray(0) & """")
        If blnErrorOccurred("Zone not available.") then Exit Sub
        Call WriteLine("  Settings for Zone " & _ 
        strDisplayNull(objDns.ContainerName) & " on server " _
        & objServer.Name & ".", objOutputFile)
        Call WriteLine("", objOutputFile)
        Call WriteLine("AllowUpdate       : " & strDisplayNull(objDns.AllowUpdate), objOutputFile)
        Call WriteLine("AutoCreated       : " & strDisplayNull(objDns.AutoCreated), objOutputFile)
        Call WriteLine("DataFile          : " & strDisplayNull(objDns.DataFile), objOutputFile)
        Call WriteLine("DisableWins       : " & strDisplayNull(objDns.DisableWINSRecordReplication), _
        objOutputFile)
        Call WriteLine("Notify            : " & strDisplayNull(objDns.Notify), objOutputFile)
        Call WriteLine("Paused            : " & strDisplayNull(objDns.Paused), objOutputFile)
        Call WriteLine("Reverse           : " & strDisplayNull(objDns.Reverse), objOutputFile)
        Call WriteLine("SecureSecondaries : " & strDisplayNull(objDns.SecureSecondaries), objOutputFile)
        Call WriteLine("Shutdown          : " & strDisplayNull(objDns.Shutdown), objOutputFile)
        Call WriteLine("UseWins           : " & strDisplayNull(objDns.UseWins), objOutputFile)
        Call WriteLine("ZoneType          : " & strDisplayNull(objDns.ZoneType), objOutputFile)
        If IsNull(objDns.MastersIPAddressesArray) then
            Call WriteLine("MastersIPArray    : <NULL>", _
            objOutputFile)
        Else
            Call WriteLine("MastersIPArray    :", objOutputFile)
            For I = lbound(objDns.MastersIPAddressesArray) _
            to ubound(objDns.MastersIPAddressesArray)
                Call WriteLine("                    " _
                & objDns.MastersIPAddressesArray(I), objOutputFile)
            Next
        End If
        If IsNull(objDns.NotifyIPAddressesArray) then
            Call WriteLine("NotifyIPArray     : <NULL>", objOutputFile)
        Else
            Call WriteLine("NotifyIPArray     :", objOutputFile)
            For I = lbound(objDns.NotifyIPAddressesArray) _
            to ubound(objDns.NotifyIPAddressesArray)
                Call WriteLine("                    " _
                & objDns.NotifyIPAddressesArray(I), objOutputFile)
            Next
        End If
        If IsNull(objDns.SecondariesIPAddressesArray) then
            Call WriteLine("SecondariesIPArray: <NULL>", _
            objOutputFile)
        Else
            Call WriteLine("SecondariesIPArray:", objOutputFile)
            For I = lbound(objDns.SecondariesIPAddressesArray) _
            to ubound(objDns.SecondariesIPAddressesArray)
                Call WriteLine("                    " _ 
                & objDns.SecondariesIPAddressesArray(I), _
                objOutputFile)
            Next
        End If
        Call WriteLine("", objOutputFile)
    End If

    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " & strOutputFile & ".")
    End If

End Sub          
```



## Create a DNS Zone


```VB
'***********************************************************
'*
'* Sub DnsCreate()
'*
'* Purpose: Creates a Zone.
'*
'* Input:   strServer           A server name
'*          strOutputFile       An output file name
'*          strUserName         The current user name
'*          strPassword         The current user password
'*          intServiceTask      The task to perform
'*
'* Output:  Results are either printed on screen or saved in 
'*          strOutputFile.
'*
'********************************************************************

Private Sub DnsCreate(strServer        , _
                      strUserName      , _
                      strPassword      , _
                      strOutputFile    , _
                      strPropertyArray , _
                      blnContextHelp     )

    ON ERROR RESUME NEXT

    Dim objFileSystem, objOutputFile, objService, objDnsSet
    Dim  objServer, objInst, strTempArray(0)

    If blnContextHelp then
        Wscript.Echo ""
        Wscript.Echo "Creates a Zone."
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo _ 
        "  DnsZones Create [ Primary | Secondary | DSIntegrated]"
        Wscript.Echo "                  [ Forward | Reverse ]"
        Wscript.Echo "                  [ <ZoneName> ] " _
        & "[ <MasterIPAddress>]"
        Wscript.Echo "               [ <filename> ] [/S <server>] " _
        & "[/U <username>]"
        Wscript.Echo "             [/W <password>] [/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   ZoneName         The name of the Zone to " _
        & "Create."
        Wscript.Echo "   MasterIPAddress  The address of the " _
        & "primary Dns Server"
        Wscript.Echo "                    (Only required for " _
        & "Secondary Zones)"
        Wscript.Echo "   filename         The Zone File name to use"
        Wscript.Echo "                    (This is only required " _
        & "when creating"
        Wscript.Echo "                    a new zone from an " _
        & "existing file.)"
        Wscript.Echo "   server           A server name"
        Wscript.Echo "   username         The current user name"
        Wscript.Echo "   password         The current user password"
        Wscript.Echo "   outputfile       The output file name"
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Wscript.Echo "1.  DnsZones Create Primary Forward " _
        & "example.com  /S MyMachine2"
        Wscript.Echo " Creates a Primary Forward zone on " _
        & "MyMachine2 called example.com."
        Wscript.Echo ""
        Wscript.Echo "2.  DnsZones Create Secondary " _
        & "Reverse 15.251.123.in-addr.arpa 157.55.254.212"
        Wscript.Echo "    Creates a Secondary Reverse."
        Exit Sub
    End If

    ' Open a text file for output if the file is requested.
    If Not IsEmpty(strOutputFile) Then
        If (NOT blnOpenFile(strOutputFile, objOutputFile)) Then
            Call Wscript.Echo ("Cannot open an output file.")
            Exit Sub
        End If
    End If

    ' Establish a connection with the server.
    If blnConnect("root\microsoftdns" , _
                   strUserName , _
                   strPassword , _
                   strServer   , _
                   objService  ) Then
        Call Wscript.Echo("")
        Call Wscript.Echo("Verify the server name, " _
                        & "credentials and WBEM Core.")
        Exit Sub
    End If

    set objServer = objService.Get("MicrosoftDNS_Server.name="".""")
    Set objDNSSet = objService.Get("MicrosoftDNS_ZONE")
    If blnErrorOccurred(" DNS Server not available.") then Exit Sub

    Select Case strPropertyArray(0)
        Case 2
            strTempArray(0) = strPropertyArray(4)
            If IsEmpty(strPropertyArray(3)) Then
                ObjInst = objDNSSet.CreateZone(strPropertyArray(2), _
                strPropertyArray(0),,strTempArray)
            Else
                ObjInst = objDNSSet.CreateZone(strPropertyArray(2), _
                strPropertyArray(0), strPropertyArray(3),strTempArray)
            End If
        
        Case Else
            If IsEmpty(strPropertyArray(3)) Then
                ObjInst = objDNSSet.CreateZone(strPropertyArray(2), _
                strPropertyArray(0))
            Else
                ObjInst = objDNSSet.CreateZone(strPropertyArray(2), _
                strPropertyArray(0), strPropertyArray(3))
            End If

    
    End Select

    If blnErrorOccurred(" DNS Zone not created.") then
        Exit Sub
    Else
        Call WriteLine("Operation successful.", objOutputFile)
    End If

    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " _
        & strOutputFile & ".")
    End If
    
End Sub
```



## Modify a DNS Zone


```VB
'***********************************************************
'*
'* Sub DnsModify()
'*
'* Purpose: Stops, starts, or restarts the DNS Server.
'*
'* Input:   strServer           A server name
'*          strOutputFile       An output file name
'*          strUserName         The current user name
'*          strPassword         The current user password
'*          strPropertyArray    The properties to change
'*          strValueArray       The new values
'*
'* Output:  Results are either printed on screen or saved in 
'*          strOutputFile.
'*
'********************************************************************

Private Sub DnsModify(strServer        , _
                      strUserName      , _
                      strPassword      , _
                      strOutputFile    , _
                      strPropertyArray , _
                      strValueArray    , _
                      strZoneArray     , _
                      blnContextHelp     )
                      
' ON ERROR RESUME NEXT
    Dim objFileSystem, objOutputFile, objService, objDnsSet, objServer
    Dim objInst, strTempArray(0), strZoneFile, strMastersIP(0), G
    Dim blnError, blnContinue

    If blnContextHelp then
        Wscript.Echo ""
        Wscript.Echo "Modifies Dns Zone Properties."
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo "  DnsZones Modify <ZoneName> <Property1> " _
        & "<Value1> [Modify <ZoneName> <Property2> <Value2>] [...]"
        Wscript.Echo "                [/S <server>]"
        Wscript.Echo "                [/U <username>] [/W <password>]"
        Wscript.Echo "                [/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   server        A server name"
        Wscript.Echo "   username      The current user name"
        Wscript.Echo "   password      The current user password"
        Wscript.Echo "   outputfile    The output file name"
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Wscript.Echo "  DnsZones.vbs Modify example.com ZoneType 1 " _
        & "Modify example.com ZoneFile example.com.Dns"
        Wscript.Echo "  Changes the Zone Type to Primary using " _
        & "example.com.Dns as the new Zone File."
        Wscript.Echo ""
        Wscript.Echo "NOTE"
        Wscript.Echo ""
        Wscript.Echo "1.  Use the display command to see a list of " _
        & "properties and descriptions."
        Wscript.Echo ""
        Wscript.Echo "2.  If you are change a Zone from Primary to " _
        & "Secondary you will need to"
        Wscript.Echo "    Specify a MastersIP address in one of " _
        & "the properties."
        Exit Sub
    End If

    ' Open a text file for output if the file is requested.
    If Not IsEmpty(strOutputFile) Then
        If (NOT blnOpenFile(strOutputFile, objOutputFile)) Then
            Call Wscript.Echo ("Cannot open an output file.")
            Exit Sub
        End If
    End If

    ' Establish a connection with the server.
    If blnConnect("root\microsoftdns" , _
                   strUserName , _
                   strPassword , _
                   strServer   , _
                   objService  ) Then
        Call Wscript.Echo("")
        Call Wscript.Echo("Please verify the server name, " _
                        & "credentials and WBEM Core.")
        Exit Sub
    End If

    set objServer = objService.Get("MicrosoftDNS_Server.name="".""")
    ' Find ZoneType Changes
    For I = LBound(strZoneArray) to UBound(strZoneArray)
        If lcase(strPropertyArray(I)) = "zonetype" then
            Select Case strValueArray(I)
                Case 0
                    Set objDNSSet = objService.Get( _
                    "MicrosoftDNS_Zone.ContainerName=""" _
                    & strZoneArray(i) & """,DnsServerName=""" _ 
                    & objServer.Name & """,Name=""" _
                    & strZoneArray(i) & """")
                    objInst = objDNSSet.ChangeZoneType(0)
                    strPropertyArray(I) = "skip"
                    Call WriteLine ("Zone type has been changed to " _
                    & "DS Intergrated.", objOutputFile)
                Case 1
                    For G = LBound(strZoneArray) to _
                    UBound(strZoneArray)
                        If lcase(strPropertyArray(G)) = _
                        "zonefile" then
                            blnContinue = True
                            strZoneFile = strValueArray(G)
                            strPropertyArray(G) = "skip"
                        End If
                    Next
                    If blnContinue = False then
                        Call WriteLine("In order to change the " _
                        & "Zone Type to Primary you must specify a " _
                        & "zonefile.", objOutputFile)
                        Exit Sub
                    End If
                    Set objDNSSet = objService.Get(_
                    "MicrosoftDNS_Zone.ContainerName=""" _
                     & strZoneArray(i) & """,DnsServerName=""" _
                     & objServer.Name & """,Name=""" _
                     & strZoneArray(i) & """")
                    objInst = objDNSSet.ChangeZoneType(1,strZoneFile)
                    strPropertyArray(I) = "skip"
                    Call WriteLine ("Zone type has been changed to Primary.", objOutputFile)
                Case 2
                    For G = Lbound(strZoneArray) _
                    to UBound(strZoneArray)
                        If lcase(strPropertyArray(G)) = _
                                                                                                        "mastersip" then
                            blnContinue = True
                            strMastersIP(0) = strValueArray(G)
                            strPropertyArray(G) = "skip"
                        End If
                    Next
                    If blnContinue = False then
                       Call WriteLine("To change the Zone " _
                       & "Type to Secondary you must specify a " _
                       & "Masters IP Address.", objOutputFile)
                       Exit Sub
                    End If
                    Set objDNSSet = objService.Get( _
                    "MicrosoftDNS_Zone.ContainerName=""" _
                    & strZoneArray(i) & """,DnsServerName=""" _
                    & objServer.Name & """,Name=""" _
                    & strZoneArray(i) & """")
                    objInst = objDNSSet.ChangeZoneType(2,, _
                    strMastersIP)
                    strPropertyArray(I) = "skip"
                    Call WriteLine ("Zone type has been changed to " _
                    & "secondary.", objOutputFile)
            End Select
        End If
    Next
    For I = LBound(strZoneArray) to UBound(strZoneArray)
        If Not IsEmpty(strZoneArray(i)) then
            Set objDNSSet = objService.Get( _
            "MicrosoftDNS_Zone.ContainerName=""" & strZoneArray(i) _
            & """,DnsServerName=""" & objServer.Name _
            & """,Name=""" & strZoneArray(i) & """")
            If blnErrorOccurred(" DNS Server not available.") _
            then Exit Sub

            If Not IsEmpty(strPropertyArray(I)) then
                blnError = False
                Select Case lcase(strPropertyArray(I))
                    Case "allowupdate"
                        objDNSSet.AllowUpdate = strValueArray(I)
                        objDNSSet.Put_
                    Case "disablewins"
                        objDNSSet.DisableWins = strValueArray(I)
                        objDNSSet.Put_
                    Case "notify"
                        objDNSSet.Notify = strValueArray(I)
                        objDNSSet.Put_
                    Case "reverse"
                        objDNSSet.Reverse = strValueArray(I)
                        objDNSSet.Put_
                    Case "securesecondaries"
                        objDNSSet.SecureSecondaries = strValueArray(I)
                        objDNSSet.Put_
                    Case "mastersip"
                        strTempArray(0) = strValueArray(I)
                        objDnsSet.MastersIPAddressesArray = _
                        strTempArray
                        objDNSSet.Put_
                    Case "skip"
                        'Do Nothing
                    Case Else
                        blnError = True
                        Call WriteLine(strPropertyArray(I) _
                        & " is not valid.", objOutputFile)
                End Select
            End If
            
            If blnError = False then
                If strPropertyArray(I) <> "skip" then
                    Call WriteLine(strPropertyArray(I) _
                    & " updated.", objOutputFile)
                End If
            End If
        End If
    Next

    If blnErrorOccurred("Zone properties not updated.") then
        Exit Sub
    Else
        Call WriteLine("Zone properties are now updated.", objOutputFile)
    End If
        
    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " & strOutputFile & ".")
    End If        

End Sub
```



## Delete a DNS Zone


```VB
'***********************************************************
'*
'* Sub DnsDelete()
'*
'* Purpose: Deletes a Zone.
'*
'* Input:   strServer           A server name
'*          strOutputFile       An output file name
'*          strUserName         The current user name
'*          strPassword         The current user password
'*
'* Output:  Results are either printed on screen or saved in 
'*          strOutputFile.
'*
'********************************************************************

Sub DnsDelete(strServer        , _
              strUserName      , _
              strPassword      , _
              strOutputFile    , _
              strPropertyArray , _
              blnContextHelp     )


    ON ERROR RESUME NEXT

    Dim objFileSystem, objOutputFile, objService, objDNS, objServer
    
    If blnContextHelp then
        Wscript.Echo ""
        Wscript.Echo "Delets a Zone."
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo "  DnsZones Delete [zonename]"
        Wscript.Echo "                  [/S <server>] [/U <username>]"
        Wscript.Echo "                  [/W <password>]"
        Wscript.Echo "                  [/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   server        A server name"
        Wscript.Echo "   username      The current user name"
        Wscript.Echo "   password      The current user password"
        Wscript.Echo "   outputfile    The output file name"
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Wscript.Echo "1.  DnsZones.vbs Delete example.com"
        Wscript.Echo "    Deletes the zone example.com."
        Wscript.Echo "2.  DnsZones.vbs Delete " _
        & "example.com /s MyMachine2"
        Wscript.Echo "    Deletes the zone example.com " _
        & "from server MyMachine2."
        Wscript.Echo ""
        Exit Sub
    End If

    ' Open a text file for output if the file is requested.
    If Not IsEmpty(strOutputFile) Then
        If (NOT blnOpenFile(strOutputFile, objOutputFile)) Then
            Call Wscript.Echo ("Cannot open an output file.")
            Exit Sub
        End If
    End If

    ' Establish a connection with the server.
    If blnConnect("root\microsoftdns" , _
                   strUserName , _
                   strPassword , _
                   strServer   , _
                   objService  ) Then
        Call Wscript.Echo("")
        Call Wscript.Echo("Please verify the server name, " _
                        & "credentials and WBEM Core.")
        Exit Sub
    End If

    set objServer = objService.Get("MicrosoftDNS_Server.name="".""")
    Set objDNS = objService.Get("MicrosoftDNS_Zone.ContainerName=""" _
    & strPropertyArray(0) & """,DnsServerName=""" & objServer.Name _
    & """,Name=""" & strPropertyArray(0) & """")
    objDns.Delete_
    If blnErrorOccurred("Error Deleting zone.") then Exit Sub
    Call WriteLine("Zone deleted from server " _
    & objserver.name & ".", objOutputFile)
    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " & strOutputFile & ".")
    End If

End Sub          
```



## Add a Zone IP Address


```VB
'************************************************************
'*
'* Sub DnsADDIP()
'*
'* Purpose: Adds an IP Addresses to an Array.
'*
'* Input:   strServer           A server name
'*          strOutputFile       An output file name
'*          strUserName         The current user name
'*          strPassword         The current user password
'*          strPropertyArray    The properties to change
'*          strValueArray       The new values
'*
'* Output:  Results are either printed on screen or saved in 
'*          strOutputFile.
'*
'********************************************************************

Private Sub DnsADDIP(strServer        , _
                     strUserName      , _
                     strPassword      , _
                     strOutputFile    , _
                     strZoneArray     , _
                     strPropertyArray , _
                     strValueArray    , _
                     blnContextHelp     )

    ' ON ERROR RESUME NEXT
    Dim objFileSystem, objOutputFile, objService, objServer, objDnsSet
    Dim strTempArray()
    Dim J, H
    Redim strTempArray(20)
    
    If blnContextHelp then
        Wscript.Echo ""
        Wscript.Echo "Adds an IP address to a property."
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo "  DnsZones AddIP <Zone> <Property1> <Value1> " _
        & "[AddIP <Zone> <Property2> <Value2>] [...]"
        Wscript.Echo "                  [/S <server>] " _
        & "[/U <username>] [/W <password>]"
        Wscript.Echo "                  [/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   server        A server name"
        Wscript.Echo "   username      The current user name"
        Wscript.Echo "   password      The current user password"
        Wscript.Echo "   outputfile    The output file name"
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Wscript.Echo "  DnsZones.vbs AddIP example.com  " _
        & "MastersIP 10.10.10.10"
        Wscript.Echo "  Adds 10.10.10.10 to the MastersIP " _
        & "property."
        Wscript.Echo ""
        Exit Sub
    End If

    ' Open a text file for output if the file is requested.
    If Not IsEmpty(strOutputFile) Then
        If (NOT blnOpenFile(strOutputFile, objOutputFile)) Then
            Call Wscript.Echo ("Cannot open an output file.")
            Exit Sub
        End If
    End If

    ' Establish a connection with the server.
    If blnConnect("root\microsoftdns" , _
                   strUserName , _
                   strPassword , _
                   strServer   , _
                   objService  ) Then
        Call Wscript.Echo("")
        Call Wscript.Echo("Please verify the server name, " _
                        & "credentials and WBEM Core.")
        Exit Sub
    End If

    set objServer = objService.Get("MicrosoftDNS_Server.name="".""")

    For I = 0 to ubound(strZoneArray)
        Set objDNSset = objService.Get( _
        "MicrosoftDNS_Zone.ContainerName=""" & strZoneArray(0) _
        & """,DnsServerName=""" & objServer.Name & """,Name=""" _
        & strZoneArray(0) & """")

        If blnErrorOccurred(" DNS Server not available.") _ 
        then Exit Sub
    
        If Not IsEmpty(strZoneArray(I)) then
            Select Case lcase(strPropertyArray(I))
                Case "mastersip"
                    Redim strTempArray(20)
                    If IsNull(objDNSSet.MastersIPAddressesArray) then
                        strTempArray(0) = strValueArray(I)
                        Redim Preserve strTempArray(0)
                        objDNSSet.MastersIPAddressesArray = _
                        strTempArray
                    Else
                        J = 0
                        For H = _ 
                        lbound(objDNSSet.MastersIPAddressesArray) _
                        to ubound(objDNSSet.MastersIPAddressesArray)
                            strTempArray(H) = _
                            objDNSSet.MastersIPAddressesArray(H)
                            J = J + 1
                        Next
                        strTempArray(J) = strValueArray(I)
                        ReDim Preserve strTempArray(J)
                        objDNSSet.MastersIPAddressesArray = _
                        strTempArray
                    End If
                    objDNSSet.Put_
                    If err.Number <> 0 then
                        Call WriteLine("Error adding IP address.", _
                        objOutputFile)
                        Exit Sub                        
                    Else
                        Call WriteLine( _
                        "IP address successfully added.", _
                        objOutputFile)
                    End If

                Case "notifyip"
                    Redim strTempArray(20)
                    If IsNull(objDNSSet.NotifyIPAddressesArray) then
                        strTempArray(0) = strValueArray(I)
                        Redim Preserve strTempArray(0)
                        objDNSSet.NotifyIPAddressesArray = _
                        strTempArray
                    Else
                        J = 0
                        For H = lbound( _
                        objDNSSet.NotifyIPAddressesArray) _
                        to ubound(objDNSSet.NotifyIPAddressesArray)
                            strTempArray(H) = _
                            objDNSSet.NotifyIPAddressesArray(H)
                            J = J + 1
                        Next
                        strTempArray(J) = strValueArray(I)
                        ReDim Preserve strTempArray(J)
                        objDNSSet.NotifyIPAddressesArray = _ 
                        strTempArray
                    End If
                    objDNSSet.Put_
                    If err.Number <> 0 then
                        Call WriteLine("Error adding IP address.", objOutputFile)
                        Exit Sub                        
                    Else
                        Call WriteLine("IP address successfully added.", objOutputFile)
                    End If

                Case "secondariesip"
                    Redim strTempArray(20)
                    If IsNull(objDNSSet.SecondariesIPAddressesArray) _
                    then
                        strTempArray(0) = strValueArray(I)
                        Redim Preserve strTempArray(0)
                        objDNSSet.SecondariesIPAddressesArray = strTempArray
                    Else
                        J = 0
                        For H = lbound( objDNSSet.SecondariesIPAddressesArray) _
                        to ubound( objDNSSet.SecondariesIPAddressesArray)
                            strTempArray(H) = _
                            objDNSSet.SecondariesIPAddressesArray(H)
                            J = J + 1
                        Next
                        strTempArray(J) = strValueArray(I)
                        ReDim Preserve strTempArray(J)
                        objDNSSet.SecondariesIPAddressesArray = strTempArray
                    End If
                    objDNSSet.Put_
                    If err.Number <> 0 then
                        Call WriteLine("Error adding IP address.", objOutputFile)
                        Exit Sub                        
                    Else
                        Call WriteLine( _
                        "IP address successfully added.", objOutputFile)
                    End If
                
                Case Else
                    Call WriteLine("Cannot add an IP address to " _
                          & strPropertyArray(I), objOutputFile)

            End Select
        End If    
    Next

    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " & strOutputFile & ".")
    End If

End Sub
```



## Delete a Zone IP Address


```VB
'************************************************************
'*
'* Sub DnsDeleteIP()
'*
'* Purpose: Adds an IP Addresses to an Array.
'*
'* Input:   strServer           A server name
'*          strOutputFile       An output file name
'*          strUserName         The current user name
'*          strPassword         The current user password
'*          strPropertyArray    The properties to change
'*          strValueArray       The new values
'*
'* Output:  Results are either printed on screen or saved in 
'*          strOutputFile.
'*
'********************************************************************

Private Sub DnsDeleteIP(strServer        , _
                        strUserName      , _
                        strPassword      , _
                        strOutputFile    , _
                        strZoneArray     , _
                        strPropertyArray , _
                        strValueArray    , _
                        blnContextHelp     )

    ON ERROR RESUME NEXT
    Dim objFileSystem, objOutputFile, objService, objServer, objDnsSet
    Dim J, H
    Dim strTempArray()
    Redim strTempArray(20)
    
    If blnContextHelp then
        Wscript.Echo ""
        Wscript.Echo "Removes an IP address from a property."
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo "  DnsZones DeleteIP <Zone> <Property1> " _
        & "<Value1> [AddIP <Zone> <Property2> <Value2>] [...]"
        Wscript.Echo "                    [/S <server>] " _
        & "[/U <username>] [/W <password>]"
        Wscript.Echo "                    [/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   server        A server name"
        Wscript.Echo "   username      The current user name"
        Wscript.Echo "   password      The current user password"
        Wscript.Echo "   outputfile    The output file name"
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Wscript.Echo "  DnsZones.vbs DeleteIP MastersIP 10.10.10.10"
        Wscript.Echo " Removes 10.10.10.10 from the MastersIP property."
        Wscript.Echo ""
        Exit Sub
    End If

    ' Open a text file for output if the file is requested.
    If Not IsEmpty(strOutputFile) Then
        If (NOT blnOpenFile(strOutputFile, objOutputFile)) Then
            Call Wscript.Echo ("Cannot open an output file.")
            Exit Sub
        End If
    End If

    ' Establish a connection with the server.
    If blnConnect("root\microsoftdns" , _
                   strUserName , _
                   strPassword , _
                   strServer   , _
                   objService  ) Then
        Call Wscript.Echo("")
        Call Wscript.Echo("Please verify the server name, " _
                        & "credentials and WBEM Core.")
        Exit Sub
    End If

    set objServer = objService.Get("MicrosoftDNS_Server.name="".""")
    Set objDNSset = objService.Get( _
    "MicrosoftDNS_Zone.ContainerName=""" & strZoneArray(0) _
    & """,DnsServerName=""" & objServer.Name & """,Name=""" _
    & strZoneArray(0) & """")

    For I = 0 to ubound(strPropertyArray)
        If Not IsEmpty(strPropertyArray(I)) then
            Select Case lcase(strPropertyArray(I))
                Case "mastersip"
                    Redim strTempArray(20)
                    If IsNull(objDNSSet.MastersIPAddressesArray) then
                       Call WriteLine("There are no IP addresses " _
                       & "to delete.", objOutputFile)
                    Else
                        J = 0
                        For H = _
                        lbound(objDNSSet.MastersIPAddressesArray) _
                        to ubound(objDNSSet.MastersIPAddressesArray)
                            If strValueArray(I) <> _
                            objDNSSet.MastersIPAddressesArray(H) then
                                strTempArray(J) = _
                                objDNSSet.MastersIPAddressesArray(H)
                                J = J + 1
                            End If
                        Next
                        If J <> 0 then
                            ReDim Preserve strTempArray(J - 1)
                            objDNSSet.MastersIPAddressesArray = _
                            strTempArray
                        Else
                            objDnsSet.MastersIPAddressesArray = Null
                        End If
                    End If
                    objDNSSet.Put_
                    If err.Number <> 0 then
                        Call WriteLine("Error deleting IP address.", _
                        objOutputFile)
                        Exit Sub                        
                    Else
                        Call WriteLine("IP address successfully " _
                        & "deleted.", objOutputFile)
                    End If

                Case "notifyip"
                    Redim strTempArray(20)
                    If IsNull(objDNSSet.NotifyIPAddressesArray) then
                        Call WriteLine("There are no IP addresses " _
                        & "to delete.", objOutputFile)
                    Else
                        J = 0
                        For H = _
                        lbound(objDNSSet.NotifyIPAddressesArray) _
                        to ubound(objDNSSet.NotifyIPAddressesArray)
                            If strValueArray(I) <> _
                            objDNSSet.NotifyIPAddressesArray(H) then
                                strTempArray(J) = _
                                objDNSSet.NotifyIPAddressesArray(H)
                                J = J + 1
                            End If
                        Next
                        If J <> 0 then
                            ReDim Preserve strTempArray(J - 1)
                            objDNSSet.NotifyIPAddressesArray = _
                            strTempArray
                        Else
                            objDnsSet.NotifyIPAddressesArray = Null
                        End If
                    End If
                    objDNSSet.Put_
                    If err.Number <> 0 then
                        Call WriteLine("Error deleting IP address.", _
                        objOutputFile)
                        Exit Sub                        
                    Else
                        Call WriteLine("IP address successfully deleted.", objOutputFile)
                    End If

                Case "secondariesip"
                    Redim strTempArray(20)
                    If IsNull(objDNSSet.SecondariesIPAddressesArray) then
                        Call WriteLine("There are no IP addresses " _
                        & "to delete.", objOutputFile)
                    Else
                      J = 0
                      For H = _
                      lbound(objDNSSet.SecondariesIPAddressesArray) _
                      to ubound(objDNSSet.SecondariesIPAddressesArray)
                          If strValueArray(I) <> objDNSSet.SecondariesIPAddressesArray(H) _
                          then
                              strTempArray(J) = objDNSSet.SecondariesIPAddressesArray(H)
                              J = J + 1
                          End If
                      Next
                      If J <> 0 then
                          ReDim Preserve strTempArray(J - 1)
                          objDNSSet.SecondariesIPAddressesArray = strTempArray
                      Else
                          objDnsSet.SecondariesIPAddressesArray = Null
                      End If
                    End If
                    objDNSSet.Put_
                    If err.Number <> 0 then
                        Call WriteLine("Error deleting IP address.", objOutputFile)
                        Exit Sub                        
                    Else
                        Call WriteLine("IP address successfully deleted.", objOutputFile)
                    End If


                Case Else
                    Call WriteLine("Cannot add an IP address to " & strPropertyArray(I), objOutputFile)

            End Select
        End If    
    
    Next
    

    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " & strOutputFile & ".")
    End If

End Sub
```



## Pause a Zone


```VB
'**********************************************************
'*
'* Sub DnsPause()
'*
'* Purpose: Pauses a Zone.
'*
'* Input:   strServer           A server name
'*          strOutputFile       An output file name
'*          strUserName         The current user name
'*          strPassword         The current user password
'*
'* Output:  Results are either printed on screen or saved in 
'*          strOutputFile.
'*
'********************************************************************

Private Sub DnsPause(strServer        , _
                     strUserName      , _
                     strPassword      , _
                     strOutputFile    , _
                     strZoneArray     , _
                     blnContextHelp     )


    ON ERROR RESUME NEXT
    Dim objFileSystem, objOutputFile, objService, objDnsSet
    Dim objServer, Inst
    
    If blnContextHelp then
        Wscript.Echo ""
        Wscript.Echo "Pauses a Zone."
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo "  DnsZones Pause <Zone>"
        Wscript.Echo "    [/S <server>] [/U <username>] " _
        & "[/W <password>]"
        Wscript.Echo "    [/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   server        A server name"
        Wscript.Echo "   username      The current user name"
        Wscript.Echo "   password      The current user password"
        Wscript.Echo "   outputfile    The output file name"
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Wscript.Echo "  DnsZones.vbs Pause example.com /s MyMachine2"
        Wscript.Echo "  Pauses the zone example.com on server " _
        & "MyMachine2"
        Wscript.Echo ""
        Exit Sub
    End If

    
    ' Open a text file for output if the file is requested.
    If Not IsEmpty(strOutputFile) Then
        If (NOT blnOpenFile(strOutputFile, objOutputFile)) Then
            Call Wscript.Echo ("Camnot open an output file.")
            Exit Sub
        End If
    End If

    ' Establish a connection with the server.
    If blnConnect("root\microsoftdns" , _
                   strUserName , _
                   strPassword , _
                   strServer   , _
                   objService  ) Then
        Call Wscript.Echo("")
        Call Wscript.Echo("Please verify the server name, " _
                        & "credentials and WBEM Core.")
        Exit Sub
    End If

    set objServer = objService.Get("MicrosoftDNS_Server.name="".""")
    Set objDNSset = objService.Get( _
    "MicrosoftDNS_Zone.ContainerName=""" & strZoneArray(0) _
    & """,DnsServerName=""" & objServer.Name & """,Name=""" _
    & strZoneArray(0) & """")
    If blnErrorOccurred(" DNS Server not available.") then Exit Sub
    If objDnsset.Paused = False then
        Inst = objDNSSet.PauseZone
        If blnErrorOccurred(" Zone not available.") then Exit Sub
        Call WriteLine("Zone " & objDNSSet.Name _ 
        & " paused on server " & objServer.Name & ".", objOutputFile)
    Else
        Call WriteLine("The Zone is already Paused.", objOutputFile)
    End If
    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " _
        & strOutputFile & ".")
    End If


End Sub
```



## Resume a Zone


```VB
'***********************************************************
'*
'* Sub DnsResume()
'*
'* Purpose: UnPauses a Zone.
'*
'* Input:   strServer           A server name
'*          strOutputFile       An output file name
'*          strUserName         The current user name
'*          strPassword         The current user password
'*
'* Output:  Results are either printed on screen or saved in 
'*          strOutputFile.
'*
'********************************************************************

Private Sub DnsResume(strServer        , _
                      strUserName      , _
                      strPassword      , _
                      strOutputFile    , _
                      strZoneArray     , _
                      blnContextHelp     )


    ON ERROR RESUME NEXT
    Dim objFileSystem, objOutputFile, objService, objDnsSet
    Dim objServer, Inst
    
    If blnContextHelp then
        Wscript.Echo ""
        Wscript.Echo "Resumes a Zone."
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo "  DnsZones Resume <Zone>"
        Wscript.Echo "    [/S <server>] [/U <username>] " _
        & "[/W <password>]"
        Wscript.Echo "    [/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   server        A server name"
        Wscript.Echo "   username      The current user name"
        Wscript.Echo "   password      The current user password"
        Wscript.Echo "   outputfile    The output file name"
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Wscript.Echo "  DnsZones.vbs Resume example.com /s MyMachine2"
        Wscript.Echo "  Unpauses the zone example.com on server " _
        & "MyMachine2."
        Exit Sub
    End If

    
    ' Open a text file for output if the file is requested.
    If Not IsEmpty(strOutputFile) Then
        If (NOT blnOpenFile(strOutputFile, objOutputFile)) Then
            Call Wscript.Echo ("Cannot open an output file.")
            Exit Sub
        End If
    End If

    ' Establish a connection with the server.
    If blnConnect("root\microsoftdns" , _
                   strUserName , _
                   strPassword , _
                   strServer   , _
                   objService  ) Then
        Call Wscript.Echo("")
        Call Wscript.Echo("Please verify the server name, " _
                        & "credentials and WBEM Core.")
        Exit Sub
    End If
    set objServer = objService.Get("MicrosoftDNS_Server.name="".""")
    Set objDNSset = objService.Get( _
    "MicrosoftDNS_Zone.ContainerName=""" & strZoneArray(0) _
    & """,DnsServerName=""" & objServer.Name & """,Name=""" _
    & strZoneArray(0) & """")
    If blnErrorOccurred(" DNS Server not available.") then Exit Sub
    If objDNSSet.Paused = True then
        Inst = objDNSSet.ResumeZone
        If blnErrorOccurred(" Zone not available.") then Exit Sub
        Call WriteLine("Zone " & objDNSSet.Name _
        & " resumed on server " & objServer.Name _ 
        & ".", objOutputFile)
    Else
        Call WriteLine("The Zone is not paused.", objOutputFile)
    End If
    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " _
        & strOutputFile & ".")
    End If


End Sub

'********************************************************************
'*
'* Sub DnsWrite()
'*
'* Purpose: Writes a Zone back to its file.
'*
'* Input:   strServer           A server name
'*          strOutputFile       An output file name
'*          strUserName         The current user name
'*          strPassword         The current user password
'*
'* Output:  Results are either printed on screen or saved in
'*          strOutputFile.
'*
'********************************************************************

Private Sub DnsWrite(strServer        , _
                     strUserName      , _
                     strPassword      , _
                     strOutputFile    , _
                     strZoneArray     , _
                     blnContextHelp     )


    ON ERROR RESUME NEXT
    Dim objFileSystem, objOutputFile, objService, objDnsSet
    Dim objServer, Inst
    
    If blnContextHelp then
        Wscript.Echo ""
        Wscript.Echo "Writes a Zone back to its file."
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo "  DnsZones Write <Zone>"
        Wscript.Echo "    [/S <server>] [/U <username>] " _
        & "[/W <password>]"
        Wscript.Echo "    [/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   server        A server name"
        Wscript.Echo "   username      The current user name"
        Wscript.Echo "   password      The current user password"
        Wscript.Echo "   outputfile    The output file name"
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Wscript.Echo "  DnsZones.vbs Write example.com"
        Wscript.Echo "  Writes any changes to example.com to its " _
        & "zone file."
        Wscript.Echo ""
        Exit Sub
    End If

    
    ' Open a text file for output if the file is requested.
    If Not IsEmpty(strOutputFile) Then
        If (NOT blnOpenFile(strOutputFile, objOutputFile)) Then
            Call Wscript.Echo ("Cannot open an output file.")
            Exit Sub
        End If
    End If

    'Establish a connection with the server.
    If blnConnect("root\microsoftdns" , _
                   strUserName , _
                   strPassword , _
                   strServer   , _
                   objService  ) Then
        Call Wscript.Echo("")
        Call Wscript.Echo("Please verify the server name, " _
                        & "credentials and WBEM Core.")
        Exit Sub
    End If
    set objServer = objService.Get("MicrosoftDNS_Server.name="".""")
    Set objDNSset = objService.Get( _
    "MicrosoftDNS_Zone.ContainerName=""" & strZoneArray(0) _
    & """,DnsServerName=""" & objServer.Name & """,Name=""" _
    & strZoneArray(0) & """")
    If blnErrorOccurred(" DNS Server not available.") then Exit Sub
    Inst = objDNSSet.ResumeZone
    If blnErrorOccurred(" Zone not available.") then Exit Sub
    Call WriteLine("Zone " & objDNSSet.Name & " has written its " _
    & "contents back to the zone file on server " & _
                        objServer.Name & ".", objOutputFile)
    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " _
        & strOutputFile & ".")
    End If


End Sub
```



## Update a Zone


```VB
'************************************************************
'*
'* Sub DnsUpdate()
'*
'* Purpose: Updates a DS integrated zone with data from the DS.
'*
'* Input:   strServer           A server name
'*          strOutputFile       An output file name
'*          strUserName         The current user name
'*          strPassword         The current user password
'*
'* Output:  Results are either printed on screen or saved in 
'*          strOutputFile.
'*
'********************************************************************

Private Sub DnsUpdate(strServer        , _
                      strUserName      , _
                      strPassword      , _
                      strOutputFile    , _
                      strZoneArray     , _
                      blnContextHelp     )


    ON ERROR RESUME NEXT
    Dim objFileSystem, objOutputFile, objService, objDnsSet 
    Dim objServer, Inst
    
    If blnContextHelp then
        Wscript.Echo ""
        Wscript.Echo "Updates a DS integrated zone with data " _
        & "from the Directory Services."
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo "  DnsZones Update <Zone>"
        Wscript.Echo "    [/S <server>] [/U <username>] " _
        & "[/W <password>]"
        Wscript.Echo "    [/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   server        A server name"
        Wscript.Echo "   username      The current user name"
        Wscript.Echo "   password      The current user password"
        Wscript.Echo "   outputfile    The output file name"
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Wscript.Echo "  DnsZones.vbs Update example.com"
        Wscript.Echo "  Updates example.com from DS Data."
        Wscript.Echo ""
        Exit Sub
    End If

    
    ' Open a text file for output if the file is requested.
    If Not IsEmpty(strOutputFile) Then
        If (NOT blnOpenFile(strOutputFile, objOutputFile)) Then
            Call Wscript.Echo ("Cannot open an output file.")
            Exit Sub
        End If
    End If

    'Establish a connection with the server.
    If blnConnect("root\microsoftdns" , _
                   strUserName , _
                   strPassword , _
                   strServer   , _
                   objService  ) Then
        Call Wscript.Echo("")
        Call Wscript.Echo("Please verify the server name, " _
                        & "credentials and WBEM Core.")
        Exit Sub
    End If
    set objServer = objService.Get("MicrosoftDNS_Server.name="".""")
    Set objDNSset = objService.Get( _
    "MicrosoftDNS_Zone.ContainerName=""" & strZoneArray(0) _
    & """,DnsServerName=""" & objServer.Name & """,Name=""" _
    & strZoneArray(0) & """")
    If blnErrorOccurred(" DNS Server not available.") then Exit Sub
    If objDNSSet.ZoneType = 0 then
        Inst = objDNSSet.UpdateDSIntegratedZoneByDataFromDS
        If blnErrorOccurred(" Zone not available.") then Exit Sub
        Call WriteLine("Zone " & objDNSSet.Name & _ 
        " has been updated from the directory services.", objOutputFile)
    Else
        Call WriteLine("Zone " & objDNSSet.Name & " is not a DS " _
        & "Integreated (ZoneType = 0) Zone.", objOutputFile)
    End If
    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " & strOutputFile & ".")
    End If


End Sub
```



## Reload a Zone


```VB
'************************************************************
'*
'* Sub DnsReload()
'*
'* Purpose: Reloads a Zone from its ZoneFile.
'*
'* Input:   strServer           A server name
'*          strOutputFile       An output file name
'*          strUserName         The current user name
'*          strPassword         The current user password
'*
'* Output:  Results are either printed on screen or saved in 
'*          strOutputFile.
'*
'********************************************************************

Private Sub DnsReload(strServer        , _
                      strUserName      , _
                      strPassword      , _
                      strOutputFile    , _
                      strZoneArray     , _
                      blnContextHelp     )


    ON ERROR RESUME NEXT
    Dim objFileSystem, objOutputFile, objService, objDnsSet 
    Dim objServer, Inst
    
    If blnContextHelp then
        Wscript.Echo ""
        Wscript.Echo "Reloads a Zone from its Zone File."
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo "  DnsZones Reload <Zone>"
        Wscript.Echo "    [/S <server>] [/U <username>] " _
        & "[/W <password>]"
        Wscript.Echo "    [/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   server        A server name"
        Wscript.Echo "   username      The current user name"
        Wscript.Echo "   password      The current user password"
        Wscript.Echo "   outputfile    The output file name"
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Wscript.Echo "  DnsZones.vbs Reload example.com"
        Wscript.Echo "  Reloads Zone example.com from its Zone File."
        Wscript.Echo ""
        Exit Sub
    End If

    
    ' Open a text file for output if the file is requested.
    If Not IsEmpty(strOutputFile) Then
        If (NOT blnOpenFile(strOutputFile, objOutputFile)) Then
            Call Wscript.Echo ("Cannot open an output file.")
            Exit Sub
        End If
    End If

    'Establish a connection with the server.
    If blnConnect("root\microsoftdns" , _
                   strUserName , _
                   strPassword , _
                   strServer   , _
                   objService  ) Then
        Call Wscript.Echo("")
        Call Wscript.Echo("Please verify the server name, " _
                        & "credentials and WBEM Core.")
        Exit Sub
    End If
    set objServer = objService.Get("MicrosoftDNS_Server.name="".""")
    Set objDNSset = objService.Get( _
    "MicrosoftDNS_Zone.ContainerName=""" & strZoneArray(0) _
    & """,DnsServerName=""" & objServer.Name & """,Name=""" _
    & strZoneArray(0) & """")
    If blnErrorOccurred(" DNS Server not available.") then Exit Sub
    Inst = objDNSSet.ReloadZone
    If blnErrorOccurred(" Zone not available.") then Exit Sub
    Call WriteLine("Zone " & objDNSSet.Name & " has written its " _
    & "contents back to the zone file on server " & objServer.Name _
    & ".", objOutputFile)
    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " & strOutputFile & ".")
    End If


End Sub
```



## Refresh a Zone


```VB
'************************************************************
'*
'* Sub DnsRefresh()
'*
'* Purpose: Resfreshes a Secondary Zone from its Master Zone.
'*
'* Input:   strServer           A server name
'*          strOutputFile       An output file name
'*          strUserName         The current user name
'*          strPassword         The current user password
'*
'* Output:  Results are either printed on screen or saved in 
'*          strOutputFile.
'*
'********************************************************************

Private Sub DnsRefresh(strServer        , _
                      strUserName      , _
                      strPassword      , _
                      strOutputFile    , _
                      strZoneArray     , _
                      blnContextHelp     )


    ON ERROR RESUME NEXT
    Dim objFileSystem, objOutputFile, objService, objDnsSet
    Dim objServer, Inst
    
    If blnContextHelp then
        Wscript.Echo ""
        Wscript.Echo "Resfreshes a Secondary Zone " _
        & "from its Master Zone."
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo "  DnsZones DnsRefresh <Zone>"
        Wscript.Echo "    [/S <server>] [/U <username>] " _
        & "[/W <password>]"
        Wscript.Echo "    [/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   server        A server name"
        Wscript.Echo "   username      The current user name"
        Wscript.Echo "   password      The current user password"
        Wscript.Echo "   outputfile    The output file name"
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Wscript.Echo "  DnsZones DnsRefresh example.com"
        Wscript.Echo "  Refreshes the secondary Zone example.com " _
        & "from its Primary Zone."
        Wscript.Echo ""
        Exit Sub
    End If

    
    ' Open a text file for output if the file is requested.
    If Not IsEmpty(strOutputFile) Then
        If (NOT blnOpenFile(strOutputFile, objOutputFile)) Then
            Call Wscript.Echo ("Cannot open an output file.")
            Exit Sub
        End If
    End If

    ' Establish a connection with the server.
    If blnConnect("root\microsoftdns" , _
                   strUserName , _
                   strPassword , _
                   strServer   , _
                   objService  ) Then
        Call Wscript.Echo("")
        Call Wscript.Echo("Please verify the server name, " _
                        & "credentials and WBEM Core.")
        Exit Sub
    End If
    set objServer = objService.Get("MicrosoftDNS_Server.name="".""")
    Set objDNSset = objService.Get( _
    "MicrosoftDNS_Zone.ContainerName=""" & strZoneArray(0) _
    & """,DnsServerName=""" & objServer.Name & """,Name=""" _
    & strZoneArray(0) & """")
    If blnErrorOccurred(" DNS Server not available.") then Exit Sub
    If objDNSset.ZoneType = 2 then
        Inst = objDNSSet.ForceRefreshOfSecondaryZoneFromMaster
        If blnErrorOccurred("An error occurred while refreshing " _
        & "secondary zone.") then Exit Sub
        Call WriteLine("Zone " & objDNSSet.Name & " has written " _
        & "its contents back to the zone file on server " _
        & objServer.Name & ".", objOutputFile)
    Else
        Call WriteLine("Zone " & objDNSSet.Name & _
                        " is not a secondary (ZoneType = 2) Zone.", objOutputFile)
    End If
    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " & strOutputFile & ".")
    End If


End Sub

'********************************************************************
'*
'* Function intParseCmdLine()
'*
'* Purpose: Parses the command line.
'* Input:   
'*
'* Output:  strServer         A remote server ("" = local server")
'*          strUserName       The current user name
'*          strPassword       The current user password
'*          strOutputFile     An output file name
'*
'********************************************************************
Private Function intParseCmdLine( ByRef strServer        , _
                                  ByRef strUserName      , _
                                  ByRef strPassword      , _
                                  ByRef strOutputFile    , _
                                  ByRef strPropertyArray , _
                                  ByRef strValueArray    , _
                                  ByRef strZoneArray     , _
                                  ByRef blnContextHelp     )
    

    ON ERROR RESUME NEXT

    Dim strFlag, strProperty, strValue
    Dim intState, intArgIter, intPropertyCount
    Dim objFileSystem
    ReDim strPropertyArray(20)
    ReDim strValueArray(20)
    ReDim strZoneArray(20)

    blnContextHelp = False
    intPropertyCount = 0
    
    If Wscript.Arguments.Count > 0 Then
        strFlag = Wscript.arguments.Item(0)
    End If

    If IsEmpty(strFlag) Then 
               'No arguments have been received
        intParseCmdLine = CONST_LIST
        Exit Function
    End If

    'Check if the user is asking for help or is just confused
    If (strFlag="help") OR (strFlag="/h") OR (strFlag="\h") OR _
    (strFlag="-h") OR (strFlag = "\?") OR (strFlag = "/?") OR _
    (strFlag = "?") OR (strFlag="h") Then
        intParseCmdLine = CONST_SHOW_USAGE
        Exit Function
    End If

    'Retrieve the command line and set appropriate variables
    intArgIter = 0
    Do While intArgIter <= Wscript.arguments.Count - 1
        Select Case lcase(Wscript.arguments.Item(intArgIter))
  
            Case "/s"
                If Not blnGetArg("Server", strServer, intArgIter) Then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If
                intArgIter = intArgIter + 1

            Case "/o"
                If Not blnGetArg("Output File", strOutputFile, _
                intArgIter) Then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If
                intArgIter = intArgIter + 1

            Case "/u"
                If Not blnGetArg("User Name", strUserName, _
                intArgIter) Then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If
                intArgIter = intArgIter + 1

            Case "/w"
                If Not blnGetArg("User Password", strPassword, _
                intArgIter) Then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If
                intArgIter = intArgIter + 1

            Case "create"
                intParseCmdLine = CONST_CREATE

                If Wscript.Arguments.Count < intArgIter + 2 then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If
                Select Case lcase(Wscript.Arguments(intArgIter + 1))
                    Case "/?"
                        blnContextHelp = True
                        intArgIter = intArgIter + 2
                        Exit Function
                    Case "primary"
                        strPropertyArray(0) = "1"
                    Case "secondary"
                        strPropertyArray(0) = "2"
                    Case "dsintegrated"
                        strPropertyArray(0) = "0"
                    Case Else
                        intParseCmdLine = CONST_ERROR
                        Exit Function
                End Select

                If  Wscript.Arguments.count < intArgIter + 3 then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If
                Select Case Lcase(Wscript.Arguments(intArgIter + 2))
                    Case "forward"
                        strPropertyArray(1) = "False"
                    Case "reverse"
                        strPropertyArray(1) = "True"
                    Case Else
                        intParseCmdLine = CONST_ERROR
                        Exit Function
                End Select

                If Wscript.Arguments.count < intArgIter + 4 then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If
                If Left(Wscript.Arguments(intArgIter + 3),1) = _ 
                "/" then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If
                strPropertyArray(2) = _
                Wscript.Arguments(intArgIter + 3)

                If strPropertyArray(0) = "2" then
                    If Wscript.Arguments.count < intArgIter + 5 then
                        intParseCmdLine = CONST_ERROR
                        Exit Function
                    End If
                    If Left(Wscript.Arguments(intArgIter + 4),1) = _
                    "/" then
                        intParseCmdLine = CONST_ERROR
                        Exit Function
                    End If
                    strPropertyArray(4) = _
                    Wscript.Arguments(intArgIter + 4)

                    If Wscript.Arguments.Count < intArgIter + 6 then
                        intArgIter = intArgIter + 5
                    Else
                        If Left(Wscript.Arguments(intArgIter + 5),1) _
                        = "/" then
                            intArgIter = intArgIter + 5
                        Else
                            strPropertyArray(3) = _
                            Wscript.Arguments(intArgIter + 5)
                            intArgIter = intArgITer + 6
                        End If
                    End If
                Else
                    If Wscript.Arguments.Count < intArgIter + 5 then
                        intArgIter = intArgIter + 4
                    Else
                        If Left(Wscript.Arguments(intArgIter + 4),1) _
                        = "/" then
                            intArgIter = intArgIter + 4
                        Else
                            strPropertyArray(3) = _
                            Wscript.Arguments(intArgIter + 4)
                            intArgIter = intArgIter + 5
                        End If
                    End IF
                End If

            Case "pause"
                If Wscript.Arguments.Count <= intArgIter + 1 then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If
                If Wscript.Arguments(intArgIter + 1) = "/?" then
                    blnContextHelp = True
                    intParseCmdLine = CONST_PAUSE
                    intArgIter = intArgIter + 2
                Else
                    strZoneArray(0) = _
                    Wscript.Arguments(intArgIter + 1)
                    intParseCmdLine = CONST_PAUSE
                    intArgIter = intArgIter + 2
                End If

            Case "resume"
                If Wscript.Arguments.Count <= intArgIter + 1 then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If
                If Wscript.Arguments(intArgIter + 1) = "/?" then
                    blnContextHelp = True
                    intParseCmdLine = CONST_RESUME
                    intArgIter = intArgIter + 2
                Else
                    strZoneArray(0) = _
                    Wscript.Arguments(intArgIter + 1)
                    intParseCmdLine = CONST_RESUME
                    intArgIter = intArgIter + 2
                End If

            Case "write"
                If Wscript.Arguments.Count <= intArgIter + 1 then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If
                If Wscript.Arguments(intArgIter + 1) = "/?" then
                    blnContextHelp = True
                    intParseCmdLine = CONST_WRITE
                    intArgIter = intArgIter + 2
                Else
                    strZoneArray(0) = _
                    Wscript.Arguments(intArgIter + 1)
                    intParseCmdLine = CONST_WRITE
                    intArgIter = intArgIter + 2
                End If

            Case "update"
                If Wscript.Arguments.Count <= intArgIter + 1 then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If
                If Wscript.Arguments(intArgIter + 1) = "/?" then
                    blnContextHelp = True
                    intParseCmdLine = CONST_UPDATE
                    intArgIter = intArgIter + 2
                Else
                    strZoneArray(0) = _
                    Wscript.Arguments(intArgIter + 1)
                    intParseCmdLine = CONST_UPDATE
                    intArgIter = intArgIter + 2
                End If

            Case "reload"
                If Wscript.Arguments.Count <= intArgIter + 1 then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If
                If Wscript.Arguments(intArgIter + 1) = "/?" then
                    blnContextHelp = True
                    intParseCmdLine = CONST_RELOAD
                    intArgIter = intArgIter + 2
                Else
                    strZoneArray(0) = _
                    Wscript.Arguments(intArgIter + 1)
                    intParseCmdLine = CONST_RELOAD
                    intArgIter = intArgIter + 2
                End If

            Case "refresh"
                If Wscript.Arguments.Count <= intArgIter + 1 then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If
                If Wscript.Arguments(intArgIter + 1) = "/?" then
                    blnContextHelp = True
                    intParseCmdLine = CONST_REFRESH
                    intArgIter = intArgIter + 2
                Else
                    strZoneArray(0) = _
                    Wscript.Arguments(intArgIter + 1)
                    intParseCmdLine = CONST_REFRESH
                    intArgIter = intArgIter + 2
                End If

            Case "delete"
                If Wscript.Arguments.Count <= intArgIter + 1 then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If
                If Wscript.Arguments(intArgIter + 1) = "/?" then
                    blnContextHelp = True
                    intParseCmdLine = CONST_DELETE
                    intArgIter = intArgIter + 2
                Else
                    strPropertyArray(0) = _
                    Wscript.Arguments(intArgIter + 1)
                    intParseCmdLine = CONST_DELETE
                    intArgIter = intArgIter + 2
                End If

            Case "list"
                intParseCmdLine = CONST_LIST
                intArgIter = intArgIter + 1      
                If Wscript.Arguments.Count => intArgIter then
                    If Left(Wscript.Arguments(intArgIter),1) <> _
                    "/" then
                        strPropertyArray(0) = _
                        Wscript.Arguments(intArgIter)
                        intArgIter = intArgIter + 1
                    End If
                End If

            Case "display"
                intParseCmdLine = CONST_DISPLAY
                intArgIter = intArgIter + 1      

            Case "addip"
                If Wscript.arguments.count <= intArgIter + 1 then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                Else
                    If Wscript.arguments(intArgIter + 1) = "/?" then
                        blnContextHelp = True
                        intParseCmdLine = CONST_ADDIP
                        intArgIter = intArgIter + 2
                    Else
                        If Wscript.arguments.count <= intArgIter + 3 _
                        then
                            intParseCmdLine = CONST_ERROR
                            Exit Function
                        End If
                        intParseCmdLine = CONST_ADDIP
                        strZoneArray(intPropertyCount) = _
                        Wscript.Arguments(intArgIter + 1)
                        strPropertyArray(intPropertyCount) = _
                        Wscript.Arguments(intArgIter + 2)
                        strValueArray(intPropertyCount) = _
                        Wscript.Arguments(intArgIter + 3)
                        intArgIter = intArgIter + 4
                        intPropertyCount = intPropertyCount + 1
                    End If
                End If

            Case "deleteip"
                If Wscript.arguments.count <= intArgIter + 1 then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                Else
                    If Wscript.arguments(intArgIter + 1) = "/?" then
                        blnContextHelp = True
                        intParseCmdLine = CONST_DELETEIP
                        intArgIter = intArgIter + 2
                    Else
                        If Wscript.arguments.count <= intArgIter + 3 _
                        then
                            intParseCmdLine = CONST_ERROR
                            Exit Function
                        End If
                        intParseCmdLine = CONST_DELETEIP
                        strZoneArray(intPropertyCount) = _
                        Wscript.Arguments(intArgIter + 1)
                        strPropertyArray(intPropertyCount) = _
                        Wscript.Arguments(intArgIter + 2)
                        strValueArray(intPropertyCount) = _
                        Wscript.Arguments(intArgIter + 3)
                        intArgIter = intArgIter + 4
                        intPropertyCount = intPropertyCount + 1
                    End If
                End If

            Case "modify"
                If Wscript.arguments.count <= intArgIter + 1 then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                Else
                    If Wscript.arguments(intArgIter + 1) = "/?" then
                        blnContextHelp = True
                        intParseCmdLine = CONST_MODIFY
                        intArgIter = intArgIter + 2
                    Else
                        If Wscript.arguments.count <= intArgIter + 3 _
                        then
                            intParseCmdLine = CONST_ERROR
                            Exit Function
                        End If
                        intParseCmdLine = CONST_MODIFY
                        strZoneArray(intPropertyCount) = _
                        Wscript.Arguments(intArgIter + 1)
                        strPropertyArray(intPropertyCount) = _
                        Wscript.Arguments(intArgIter + 2)
                        strValueArray(intPropertyCount) = _
                        Wscript.Arguments(intArgIter + 3)
                        intArgIter = intArgIter + 4
                        intPropertyCount = intPropertyCount + 1
                    End If
                End If

            Case "/?"
               blnContextHelp = True
                intArgIter = intArgIter + 1
            
            Case Else
                intParseCmdLine = CONST_ERROR
                Exit Function
                
        End Select


    Loop '** intArgIter <= Wscript.arguments.Count - 1
    
    If IsEmpty(intParseCmdLine) Then 
        If blnContextHelp = True then
            intParseCmdLine = CONST_SHOW_USAGE
        Else
            intParseCmdLine = CONST_LIST
        End If
    End If

End Function

'********************************************************************
'*
'* Sub ShowUsage()
'*
'* Purpose: Shows the correct usage to the user.
'*
'* Input:   None
'*
'* Output:  Help messages are displayed on screen.
'*
'********************************************************************
Private Sub ShowUsage()

    Wscript.Echo ""
    Wscript.Echo "Gets and Sets DNS Server information " _
    & "for a computer."
    Wscript.Echo ""
    Wscript.Echo "SYNTAX:"
    Wscript.Echo "  DnsServer operation <Parameter List>"
    Wscript.Echo "                      [/S <server>] " _
    & "[/U <username>] [/W <password>]"
    Wscript.Echo "                      [/O <outputfile>]"
    Wscript.Echo ""
    Wscript.Echo "  operation   [List | Create | Modify | Delete | " _
    & "Pause | Resume |"
    Wscript.Echo "               Write | UpdateDS | Reload | " _
    & "Refresh | AddIP | DeleteIP]"
    Wscript.Echo ""
    Wscript.Echo "    For help on a specific operation type:"
    Wscript.Echo ""
    Wscript.Echo "              DnsZones List /?"
    Wscript.Echo "              DnsZones Display /?"
    Wscript.Echo "              DnsZones Create /?"
    Wscript.Echo "              DnsZones Modify /?"
    Wscript.Echo "              DnsZones Delete /?"
    Wscript.Echo "              DnsZones AddIP /?"
    Wscript.Echo "              DnsZones DeleteIP /?"
    Wscript.Echo "              DnsZones Pause /?"
    Wscript.Echo "              DnsZones Resume /?"
    Wscript.Echo "              DnsZones Write /?"
    Wscript.Echo "              DnsZones UpdateDS /?"
    Wscript.Echo "              DnsZones Reload /?"
    Wscript.Echo "              DnsZones Refresh /?"
    Wscript.Echo ""
    Wscript.Echo "PARAMETER SPECIFIERS:"
    Wscript.Echo "   server        A server name"
    Wscript.Echo "   username      The current user name"
    Wscript.Echo "   password      The current user password"
    Wscript.Echo "   outputfile    The output file name"
    Wscript.Echo ""

End Sub

'********************************************************************
'*
'* Sub Display()
'*
'* Purpose: Shows a list of all available properties with
'*          descriptions.
'*
'* Input:   None
'*
'* Output:  Displayed on screen.
'*
'********************************************************************
Private Sub Display(strOutputFile, blnContextHelp)

    Dim objOutputFile

    ' Open a text file for output if the file is requested.
    If Not IsEmpty(strOutputFile) Then
        If (NOT blnOpenFile(strOutputFile, objOutputFile)) Then
            Call Wscript.Echo ("Cannot open an output file.")
            Exit Sub
        End If
    End If

    If blnContextHelp then
        Wscript.Echo ""
        Wscript.Echo "Displays all available property types and " _
        & "descriptions."
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo "  DnsServer Display [/S <server>] " _
        & "[/U <username>] [/W <password>]"
        Wscript.Echo "                    [/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   server        A server name"
        Wscript.Echo "   username      The current user name"
        Wscript.Echo "   password      The current user password"
        Wscript.Echo "   outputfile    The output file name"
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Wscript.Echo "  DnsZones.vbs Display"
        Wscript.Echo ""
        Exit Sub
    End If

    Call WriteLine("Property            Type       Description",  _
    & "objOutputFile")
    Call WriteLine("-----------------------------------------------" _
    & "------------------------------", objOutputFile)
    Call WriteLine(" AllowUpdate        True/False This Boolean " _
    & "indicates whether the Zone should", objOutputFile)
    Call WriteLine("                               accept dynamic " _
    & "update requests.", objOutputFile)
    Call WriteLine(" AutoCreated        read-only  This Boolean " _
    & "indicates whether the Zone is", objOutputFile)
    Call WriteLine("                               autocreated.", _
    objOutputFile)
    Call WriteLine(" ContainerName      read-only  Indicates the " _
    & "Name of the Container (which", objOutputFile)
    Call WriteLine("                               could be a " _
    & "Zone, Cache or RootHints)", objOutputFile)
    Call WriteLine("                               containing this " _
    & "domain. In cases where the", objOutputFile)
    Call WriteLine("                               Container is a " _
    & "Zone (an instance of the", objOutputFile)
    Call WriteLine("                               " _
    & "MicrosoftDNS_Zone subclass), this property", objOutputFile)
    Call WriteLine("                               contains the " _
    & "fully qualified domain name of", objOutputFile)
    Call WriteLine("                               the Zone. When " _
    & "the Container is the root zone,", objOutputFile)
    Call WriteLine("                               the string, " _
    & """."",should be used.  In cases", objOutputFile)
    Call WriteLine("                               where the " _
    & "Container is the DNS' cache of", objOutputFile)
    Call WriteLine("                               resource " _
    & "records (an instance of the", objOutputFile)
    Call WriteLine("                               " _
    & "MicrosoftDNS_Cache subclass), this property is", objOutputFile)
    Call WriteLine("                               set to the " _
    & "string, ""..Cache"".  If the ", objOutputFile)
    Call WriteLine("                               Container is " _
    & "Root Hints (an instance of the", objOutputFile)
    Call WriteLine("                               " _
    & "MicrosoftDNS_RootHints subclass), then this", objOutputFile)
    CAll WriteLine("                               property should " _
    & "be set to ""..RootHints"".", objOutputFile)
    Call WriteLine(" ZoneFile           read-only  Indicates the " _
    & "name of the zone file.", objOutputFile)
    Call WriteLine(" DisableWins        True/False This Boolean " _
    & "indicates whether the WINS record", objOutputFile)
    Call WriteLine("                               is NOT " _
    & "replicated. If set to TRUE, WINS record", objOutputFile)
    Call WriteLine("                               replication " _
    & "is disabled.", objOutputFile)
    Call WriteLine(" Notify             True/False This Boolean " _
    & "indicates whether the master Zone", objOutputFile)
    Call WriteLine("                               notifies " _
    & "secondaries of any changes in its", objOutputFile)
    Call WriteLine("                               Resource " _
    & "Records database. If set to TRUE,", objOutputFile)
    Call WriteLine("                               secondaries are " _
    & "notified.", objOutputFile)
    Call WriteLine(" Paused             read-only  This Boolean " _
    & "indicates whether the Zone is", objOutputFile)
    Call WriteLine("                               paused.", _
    objOutputFile)
    Call WriteLine(" Reverse            True/False This Boolean " _
    & "indicates whether the Zone is", objOutputFile)
    Call WriteLine("                               reverse (TRUE) " _
    & "or forward (FALSE).", objOutputFile)
    Call WriteLine(" SecureSecondaries  True/False This Boolean " _
    & "indicates whether zone transfer", objOutputFile)
    Call WriteLine("                               is allowed - " _
    & "but only to designated", objOutputFile)
    Call WriteLine("                               secondaries.  " _
    & "Designated secondaries are DNS", objOutputFile)
    Call WriteLine("                               servers " _
    & "whose IP addresses are listed in the", objOutputFile)
    Call WriteLine("                               array, " _
    & "SecondariesIPAddressesArray.", objOutputFile)
    Call WriteLine(" Shutdown           read-only  This Boolean " _
    & "indicates whether the copy of the", objOutputFile)
    Call WriteLine("                               Zone is " _
    & "expired. If TRUE, the Zone is expired,", objOutputFile)
    Call WriteLine("                               or 'shutdown'.", _
    objOutputFile)
    Call WriteLine(" UseWins            read-only  This Boolean " _
    & "indicates whether the Zone uses", objOutputFile)
    Call WriteLine("                               WINS lookup.", _
    objOutputFile)
    Call WriteLine(" ZoneType           Number     Indicates the " _ 
    & "type of the Zone.", objOutputFile)    
    Call WriteLine("                    ""0""        DS Integrated " _
    & "Zone", objOutputFile)
    Call WriteLine("                    ""1""        Primary Zone", _
    objOutputFile)
    Call WriteLine("                    ""2""        Secondary " _
    & "Zone", objOutputFile)
    Call WriteLine("", objOutputFile)
    Call WriteLine("IP Array            Type       Description", _
    objOutputFile)
    Call WriteLine("-----------------------------------------------" _
    & "------------------------------", objOutputFile)
    Call WriteLine(" NotifyIP           Array      This array of " _
    & "strings enumerates the list of", objOutputFile)
    Call WriteLine("                               IP addresses of " _
    & "the DNS servers that should be", objOutputFile)
    Call WriteLine("                               notified of " _
    & "changes in this zone.", objOutputFile)
    Call WriteLine(" MastersIP          Array      This array of " _
    & "strings enumerates the list of", objOutputFile)
    Call WriteLine("                               IP addresses of " _
    & "Master DNS servers, to be", objOutputFile)
    Call WriteLine("                               addressed for " _
    & "zone replication. It is", objOutputFile)
    Call WriteLine("                               applicable to " _
    & "secondary zones only (ZoneType =", objOutputFile)
    Call WriteLIne("                               2, " _
    & " ""Secondary"").", objOutputFile)
    Call WriteLine(" SecondariesIP      Array      This array of " _
    & "strings enumerates the list of", objOutputFile)
    Call WriteLine("                               IP addresses of " _
    & "the DNS servers that are", objOutputFile)
    Call WriteLine("                               allowed to " _
    & "receive this zone through zone", objOutputFile)
    Call WriteLine("                               replication.", _
    objOutputFile)
    Call WriteLine("", objOutputFile)
    
    
    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " _
        & strOutputFile & ".")
    End If
    
End Sub

'********************************************************************
'* General Routines
'********************************************************************

'********************************************************************
'*
'* Function strDisplayNull()
'*
'* Purpose: Returns the input or a "<NULL>" string.
'*
'* Input:   strProperty     the property to be evaualted
'*
'* Output:  The input or a "<NULL"> string.
'*
'********************************************************************

Function strDisplayNull(strProperty)

    If IsNull(strProperty) then
        strDisplayNull = "<NULL>"
    Else
        strDisplayNull = strProperty
    End If

End Function

'********************************************************************
'*
'* Function strPackString()
'*
'* Purpose: Attaches spaces to a string to increase the length to 
'*          intWidth.
'*
'* Input:   strString   a string
'*          intWidth    the intended length of the string
'*          blnAfter    Should spaces be added after the string?
'*          blnTruncate specifies whether to truncate the string or
'*                      not if the string length is longer than 
'*                      intWidth
'*
'* Output:  strPackString is returned as the packed string.
'*
'********************************************************************
Private Function strPackString( ByVal strString, _
                                ByVal intWidth,  _
                                ByVal blnAfter,  _
                                ByVal blnTruncate)

    ON ERROR RESUME NEXT

    intWidth      = CInt(intWidth)
    blnAfter      = CBool(blnAfter)
    blnTruncate   = CBool(blnTruncate)

    If Err.Number Then
        Call Wscript.Echo ("Argument type is incorrect!")
        Err.Clear
        Wscript.Quit
    End If

    If IsNull(strString) Then
        strPackString = "null" & Space(intWidth-4)
        Exit Function
    End If

    strString = CStr(strString)
    If Err.Number Then
        Call Wscript.Echo ("Argument type is incorrect!")
        Err.Clear
        Wscript.Quit
    End If

    If intWidth > Len(strString) Then
        If blnAfter Then
            strPackString = strString & Space(intWidth-Len(strString))
        Else
            strPackString = Space(intWidth-Len(strString)) _
            & strString & " "
        End If
    Else
        If blnTruncate Then
            strPackString = Left(strString, intWidth-1) & " "
        Else
            strPackString = strString & " "
        End If
    End If

End Function

'********************************************************************
'* 
'*  Function blnGetArg()
'*
'*  Purpose: Helper to intParseCmdLine()
'* 
'*  Usage:
'*
'*     Case "/s" 
'*       blnGetArg ("server name", strServer, intArgIter)
'*
'********************************************************************
Private Function blnGetArg ( ByVal StrVarName,   _
                             ByRef strVar,       _
                             ByRef intArgIter) 

    blnGetArg = False 'failure, changed to 
                      'True upon successful completion

    If Len(Wscript.Arguments(intArgIter)) > 2 then
        If Mid(Wscript.Arguments(intArgIter),3,1) = ":" then
            If Len(Wscript.Arguments(intArgIter)) > 3 then
                strVar = Right(Wscript.Arguments(intArgIter), _
                         Len(Wscript.Arguments(intArgIter)) - 3)
                blnGetArg = True
                Exit Function
            Else
                intArgIter = intArgIter + 1
                If intArgIter > (Wscript.Arguments.Count - 1) Then
                    Call Wscript.Echo( "Invalid " & StrVarName & ".")
                    Call Wscript.Echo( "Please check the input and try again.")
                    Exit Function
                End If

                strVar = Wscript.Arguments.Item(intArgIter)
                If Err.Number Then
                    Call Wscript.Echo( "Invalid " & StrVarName & ".")
                    Call Wscript.Echo( "Please check the input and try again.")
                    Exit Function
                End If

                If InStr(strVar, "/") Then
                    Call Wscript.Echo( "Invalid " & StrVarName)
                    Call Wscript.Echo( "Please check the input and try again.")
                    Exit Function
                End If

                blnGetArg = True 'success
            End If
        Else
            strVar = Right(Wscript.Arguments(intArgIter), _
                     Len(Wscript.Arguments(intArgIter)) - 2)
            blnGetArg = True 'success
            Exit Function
        End If
    Else
        intArgIter = intArgIter + 1
        If intArgIter > (Wscript.Arguments.Count - 1) Then
            Call Wscript.Echo( "Invalid " & StrVarName & ".")
            Call Wscript.Echo( "Please check the input and try again.")
            Exit Function
        End If

        strVar = Wscript.Arguments.Item(intArgIter)
        If Err.Number Then
            Call Wscript.Echo( "Invalid " & StrVarName & ".")
            Call Wscript.Echo( "Please check the input and try again.")
            Exit Function
        End If

        If InStr(strVar, "/") Then
            Call Wscript.Echo( "Invalid " & StrVarName)
            Call Wscript.Echo( "Please check the input and try again.")
            Exit Function
        End If
        blnGetArg = True 'success
    End If
End Function

'********************************************************************
'*
'* Function blnConnect()
'*
'* Purpose: Connects to server strServer.
'*
'* Input:   strServer       A server name
'*          strNameSpace    a namespace
'*          strUserName     name of the current user
'*          strPassword     password of the current user
'*
'* Output:  objService is returned  as a service object.
'*          strServer is set to local host if left unspecified
'*
'********************************************************************
Private Function blnConnect(ByVal strNameSpace, _
                            ByVal strUserName,  _
                            ByVal strPassword,  _
                            ByRef strServer,    _
                            ByRef objService)

    ON ERROR RESUME NEXT

    Dim objLocator, objWshNet

    blnConnect = False     'There is no error.

    'Create Locator object to connect to remote CIM object manager
    Set objLocator = CreateObject("WbemScripting.SWbemLocator")
    If Err.Number then
        Call Wscript.Echo( "Error 0x" & CStr(Hex(Err.Number)) & _
                           " occurred in creating a locator object." )
        If Err.Description <> "" Then
            Call Wscript.Echo( "Error description: " _
            & Err.Description & "." )
        End If
        Err.Clear
        blnConnect = True     'An error occurred
        Exit Function
    End If

    'Connect to the namespace which is either local or remote
    Set objService = objLocator.ConnectServer (strServer, _
    strNameSpace, strUserName, strPassword)
    ObjService.Security_.impersonationlevel = 3
    If Err.Number then
        Call Wscript.Echo( "Error 0x" & CStr(Hex(Err.Number)) & _
                           " occurred in connecting to server " _
           & strServer & ".")
        If Err.Description <> "" Then
            Call Wscript.Echo( "Error description: " _
            & Err.Description & "." )
        End If
        Err.Clear
        blnConnect = True     'An error occurred
    End If

    'Get the current server's name if left unspecified
    If IsEmpty(strServer) Then
        Set objWshNet = CreateObject("Wscript.Network")
    strServer     = objWshNet.ComputerName
    End If

End Function

'********************************************************************
'*
'* Sub      VerifyHostIsCscript()
'*
'* Purpose: Determines which program is used to run this script.
'*
'* Input:   None
'*
'* Output:  If host is not cscript, then an error message is printed 
'*          and the script is aborted.
'*
'********************************************************************
Sub VerifyHostIsCscript()

    ON ERROR RESUME NEXT

    Dim strFullName, strCommand, i, j, intStatus

    strFullName = WScript.FullName

    If Err.Number then
        Call Wscript.Echo( "Error 0x" & CStr(Hex(Err.Number)) _
        & " occurred." )
        If Err.Description <> "" Then
            Call Wscript.Echo( "Error description: " _
            & Err.Description & "." )
        End If
        intStatus =  CONST_ERROR
    End If

    i = InStr(1, strFullName, ".exe", 1)
    If i = 0 Then
        intStatus =  CONST_ERROR
    Else
        j = InStrRev(strFullName, "\", i, 1)
        If j = 0 Then
            intStatus =  CONST_ERROR
        Else
            strCommand = Mid(strFullName, j+1, i-j-1)
            Select Case LCase(strCommand)
                Case "cscript"
                    intStatus = CONST_CSCRIPT
                Case "wscript"
                    intStatus = CONST_WSCRIPT
                Case Else       'should never happen
                    Call Wscript.Echo( "An unexpected program was " _
                    & "used to run this script." )
                    Call Wscript.Echo( "Only CScript.Exe or " _
                    & "WScript.Exe can be used to run this script." )
                    intStatus = CONST_ERROR
                End Select
        End If
    End If

    If intStatus <> CONST_CSCRIPT Then
        Call WScript.Echo( "Please run this script using CScript." _
             & vbCRLF & "This can be achieved by" & vbCRLF & _
             "1. Using ""CScript PS.VBS arguments"" for Windows " _
             & "95/98 or " & vbCRLF & "2. Changing the default " _
             & "Windows Script Host setting to CScript" & vbCRLF _
             & "    using ""CScript //H:CScript //S"" and running " _
             & "the script using" & vbCRLF & "    ""PS.VBS " _
             & "arguments"" for Windows NT/2000." )
        WScript.Quit
    End If

End Sub

'********************************************************************
'*
'* Sub WriteLine()
'* Purpose: Writes a text line either to a file or on screen.
'* Input:   strMessage  the string to print
'*          objFile     an output file object
'* Output:  strMessage is either displayed on screen or written to a
'*          file.
'*
'********************************************************************
Sub WriteLine(ByVal strMessage, ByVal objFile)

    On Error Resume Next
    If IsObject(objFile) then        'objFile should be a file object
        objFile.WriteLine strMessage
    Else
        Call Wscript.Echo( strMessage )
    End If

End Sub

'********************************************************************
'* 
'* Function blnErrorOccurred()
'*
'* Purpose: Reports error with a string that identifies
'*          what the error occurred in.
'*
'* Input:   strIn        String that identifies what the error 
'*                                                                                                                                                                                      occurred in.
'*
'* Output:  displayed on screen 
'* 
'********************************************************************
Private Function blnErrorOccurred (ByVal strIn)

    If Err.Number Then
        Call Wscript.Echo( "Error 0x" & CStr(Hex(Err.Number)) & ": "_
        & strIn)
        If Err.Description <> "" Then
            Call Wscript.Echo("Error description: " & Err.Description)
        End If
        Err.Clear
        blnErrorOccurred = True
    Else
        blnErrorOccurred = False
    End If

End Function

'********************************************************************
'* 
'* Function blnOpenFile
'*
'* Purpose: Opens a file.
'*
'* Input:   strFileName        A string with the name of the file.
'*
'* Output:  Sets objOpenFile to a FileSystemObject and setis it to 
'*            Nothing upon Failure.
'* 
'********************************************************************
Private Function blnOpenFile(ByVal strFileName, ByRef objOpenFile)

    ON ERROR RESUME NEXT

    Dim objFileSystem

    Set objFileSystem = Nothing

    If IsEmpty(strFileName) OR strFileName = "" Then
        blnOpenFile = False
        Set objOpenFile = Nothing
        Exit Function
    End If

    ' Create a file object.
    Set objFileSystem = CreateObject("Scripting.FileSystemObject")
    If blnErrorOccurred("Could not create filesystem object.") Then
        blnOpenFile = False
        Set objOpenFile = Nothing
        Exit Function
    End If

    ' Open the file for output.
    Set objOpenFile = objFileSystem.OpenTextFile(strFileName, 8, True)
    If blnErrorOccurred("Could not open") Then
        blnOpenFile = False
        Set objOpenFile = Nothing
        Exit Function
    End If
    blnOpenFile = True

End Function

'********************************************************************
'*                                                                  *
'*                           End of File                            *
'*                                                                  *
'********************************************************************
```



 

 




