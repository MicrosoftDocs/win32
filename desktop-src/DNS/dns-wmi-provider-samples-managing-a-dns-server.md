---
title: DNS WMI Provider Samples—Managing a DNS Server
description: DNS WMI Provider Samples—Managing a DNS Server
ms.assetid: 7846fbaf-cc15-4cd0-aa3f-796617380bb6
ms.topic: article
ms.date: 05/31/2018
---

# DNS WMI Provider Samples—Managing a DNS Server

> [!NOTE]
> This article contains references to the term slave, a term that Microsoft no longer uses. When the term is removed from the software, we’ll remove it from this article.

This section demonstrates scripting tasks associated with managing a DNS Server. The links below jump to subroutines in the script file:

-   [List DNS Server properties](#list-dns-server-properties)
-   [Stop, start, or restart a DNS Server](#stop-start-or-restart-a-dns-server)
-   [Modify DNS Server properties](#modify-dns-server-properties)
-   [Add an IP address](#add-an-ip-address)
-   [Delete an IP address](#delete-an-ip-address)
-   [List Zones](#list-zones)


```VB
'********************************************************************
'*
'*  File:           DnsServer.vbs
'*
'*  Main Function:  Gets and Sets DNS Server information
'*                                                                        for a machine.
'*
'*  To Be Done: The IP section is waiting for some provider bug fixes.
'*                          The Restart Server is wating for some provider bug fixes.
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
    CONST CONST_SERVICE                 = 6
    CONST CONST_START                   = 7
    CONST CONST_STOP                    = 8
    CONST CONST_RESTART                 = 9
    CONST CONST_MODIFY                  = 10
    CONST CONST_ZONE                    = 11
    CONST CONST_ADD                     = 12
    CONST CONST_DELETE                  = 13

    'Declare variables
    Dim intOpMode, i, intServiceTask
    Dim strServer, strUserName, strPassword, strOutputFile
    Dim blnContextHelp
    Dim strPropertyArray(), strValueArray()
    
    'Ensure that the host is script, if not then abort
    VerifyHostIsCscript()

    'Parse the command line
    intOpMode = intParseCmdLine(strServer        , _
                                strUserName      , _
                                strPassword      , _
                                strOutputFile    , _
                                intServiceTask   , _
                                strPropertyArray , _
                                strValueArray    , _
                                blnContextHelp     )

    Select Case intOpMode

        Case CONST_SHOW_USAGE
            Call ShowUsage()

        Case CONST_DISPLAY
            Call Display(strOutputFile, blnContextHelp)

        Case CONST_LIST
            Call DnsServerList(strServer     , _
                               strUserName   , _
                               strPassword   , _
                               strOutputFile , _
                               blnContextHelp  )

        Case CONST_SERVICE
            Call DnsService(strServer     , _
                            strUserName   , _
                            strPassword   , _
                            strOutputFile , _
                            intServiceTask, _
                            blnContextHelp  )

        Case CONST_MODIFY
            Call DnsModify(strServer        , _
                           strUserName      , _
                           strPassword      , _
                           strOutputFile    , _
                           strPropertyArray , _
                           strValueArray    , _
                           blnContextHelp     )

        Case CONST_ADD
            Call DnsADDIP(strServer        , _
                          strUserName      , _
                          strPassword      , _
                          strOutputFile    , _
                          strPropertyArray , _
                          strValueArray    , _
                          blnContextHelp     )

        Case CONST_DELETE
            Call DnsDeleteIP(strServer        , _
                             strUserName      , _
                             strPassword      , _
                             strOutputFile    , _
                             strPropertyArray , _
                             strValueArray    , _
                             blnContextHelp     )

        Case CONST_ZONE
            Call DnsZone(strServer        , _
                         strUserName      , _
                         strPassword      , _
                         strOutputFile    , _
                         blnContextHelp     )

        Case CONST_ERROR
            Call Wscript.Echo("Error occurred in passing parameters.")

        Case Else                    'Default -- should never happen
            Call Wscript.Echo("Error occurred in passing parameters.")

    End Select

'********************************************************************
'* End of Script
'********************************************************************
```



## List DNS Server properties


```VB
'********************************************************************
'*
'* Sub DnsServerList()
'*
'* Purpose: Lists the Value of all server properties.
'*
'* Input:   strServer           a machine name
'*          strOutputFile       an output file name
'*          strUserName         the current user's name
'*          strPassword         the current user's password
'*
'* Output:  Results are either printed on screen or saved 
'*            in strOutputFile.
'*
'********************************************************************

Sub DnsServerList(strServer     , _
                  strUserName   , _
                  strPassword   , _
                  strOutputFile , _
                  blnContextHelp  )


    ON ERROR RESUME NEXT

    Dim objFileSystem, objOutputFile, objService, objDnsSet, objDNS
    Dim strWBEMClass
    
    If blnContextHelp then
        Wscript.Echo ""
        Wscript.Echo "Displays the values of all the properties on the server."
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo "  DnsServer List [/S <server>] [/U <username>]"
        Wscript.Echo "                 [/W <password>] " & _
                                                                                    "[/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   server        A machine name."
        Wscript.Echo "   username      The current user's name."
        Wscript.Echo "   password      Password of the current user."
        Wscript.Echo "   outputfile    The output file name."
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Wscript.Echo "  DnsServer.vbs List"
        Wscript.Echo ""
        Exit Sub
    End If

    'Open a text file for output if the file is requested
    If Not IsEmpty(strOutputFile) Then
        If (NOT blnOpenFile(strOutputFile, objOutputFile)) Then
            Call Wscript.Echo ("Could not open an output file.")
            Exit Sub
        End If
    End If

    'Establish a connection with the server.</a>
    If blnConnect("root\microsoftdns" , _
                   strUserName , _
                   strPassword , _
                   strServer   , _
                   objService  ) Then
        Call Wscript.Echo("")
        Call Wscript.Echo("Please check the server name, " _
                        & "credentials and WBEM Core.")
        Exit Sub
    End If

    strWBEMClass = "MicrosoftDNS_Server"

    Set objDNS = objService.Get("MicrosoftDNS_Server.Name="".""")
    If blnErrorOccurred(" DNS Server not available.") then Exit Sub

    Call WriteLine("SERVER", objOutputFile)
    Call WriteLine(" Name    : " & _
                    strDisplayNull(objDNS.Name), objOutputFile)
    Call WriteLine(" Version : " & _
                    Hex(strDisplayNull(objDNS.Version)), objOutputFile)
    Call WriteLine(" Slave   : " & _ 
                    strDisplayNull(objDNS.Slave), objOutputFile)
    Call WriteLine("", objOutputFile)  
    Call WriteLine("CACHE", objOutputFile)
    Call WriteLine(" AutoCacheUpdate : " & _
                    strDisplayNull(objDNS.AutoCacheUpdate), objOutputFile)
    Call WriteLine(" MaxCacheTTL     : " & _
                    strDisplayNull(objDNS.MaxCacheTTL), objOutputFile)        
    Call WriteLine("", objOutputFile) 
    Call WriteLine("COMMUNICATION",  objOutputFile)
    Call WriteLine(" AddressAnswerLimit : " & _
                    strDisplayNull(objDNS.AddressAnswerLimit), objOutputFile)
    Call WriteLine(" AllowUpdate        : " & _
                 strDisplayNull(objDNS.AllowUpdate), objOutputFile)
    Call WriteLine(" DisjointNets       : " & _
                    strDisplayNull(objDNS.DisjointNets), objOutputFile)
    Call WriteLine(" ForwardDelegation  : " & _
                    strDisplayNull(objDNS.ForwardDelegation), objOutputFile)
    Call WriteLine(" LocalNetPriority   : " & _
                    strDisplayNull(objDNS.LocalNetPriority), objOutputFile)
    Call WriteLine(" RpcProtocol        : " & _
                    strDisplayNull(objDNS.RpcProtocol), objOutputFile)
    Call WriteLine(" SendOnNonDnsPort   : " & _
                    strDisplayNull(objDNS.SendOnNonDnsPort), objOutputFile)
    Call WriteLine(" SlowZoneTransfer   : " & _
                    strDisplayNull(objDNS.SlowZoneTransfer), objOutputFile)
    Call WriteLine("", objOutputFile) 
    Call WriteLine("DIRECTORY SERVICES",  objOutputFile)
    Call WriteLine(" DsAvailable       : " & _
                    strDisplayNull(objDNS.DsAvailable), objOutputFile)
    Call WriteLine(" DsPollingInterval : " & _
                    strDisplayNull(objDNS.DsPollingInterval), objOutputFile)
    Call WriteLine("", objOutputFile) 
    Call WriteLine("IP ADDRESSES",  objOutputFile)
    If IsNull(objDNS.ServerIPAddressesArray) then
        Call WriteLine(" ServerIPAddressesArray     : <NULL>", _
                                                                                        objOutputFile)
    Else
        Call WriteLine(" ServerIPAddressesArray     :", _
                                                                                        objOutputFile)
        For I = LBound(objDNS.ServerIPAddressesArray) to _
                                                                UBound(objDNS.ServerIPAddressesArray)
            Call WriteLine("                              " & _
                                                                    strDisplayNull(objDNS.ServerIPAddressesArray(I)),_
                                                                    objOutputFile)
        Next
    End If
    If IsNull(objDNS.ForwardersIPAddressesArray) then
        Call WriteLine(" ForwardersIPAddressesArray : <NULL>",_
                                                                                     objOutputFile)
    Else
        Call WriteLine(" ForwardersIPAddressesArray :", objOutputFile)
        For I = LBound(objDNS.ForwardersIPAddressesArray) to _
                                                                UBound(objDNS.ForwardersIPAddressesArray)
            Call WriteLine("                              " & _
              strDisplayNull(objDNS.ForwardersIPAddressesArray(I)),_
                                                        objOutputFile)
        Next
    End If
    If IsNull(objDNS.ListenIPAddressesArray) then
        Call WriteLine(" ListenIPAddressesArray     : <NULL>",_
                                                                                         objOutputFile)
    Else
        Call WriteLine(" ListenIPAddressesArray     :", objOutputFile)
        For I = LBound(objDNS.ListenIPAddressesArray) to _
                                                                UBound(objDNS.ListenIPAddressesArray)
            Call WriteLine("                              " & _
                                                                    strDisplayNull(objDNS.ListenIPAddressesArray(I)),_
                                                                 objOutputFile)
        Next
    End If
    Call WriteLine("", objOutputFile) 
    Call WriteLine("LOGGING",  objOutputFile)
    Call WriteLine(" EventLogLevel : " & _
                    strDisplayNull(objDNS.EventLogLevel), objOutputFile)
    Call WriteLine(" LogLevel      : " & _
                    strDisplayNull(objDNS.LogLevel), objOutputFile)
    Call WriteLine("", objOutputFile) 
    Call WriteLine("RECURSION",  objOutputFile)
    Call WriteLine(" NoRecursion      : " & _
                    strDisplayNull(objDNS.NoRecursion), objOutputFile)        
    Call WriteLine(" RecursionRetry   : " & _
                    strDisplayNull(objDNS.RecursionRetry), objOutputFile)        
    Call WriteLine(" RecursionTimeout : " & _
                    strDisplayNull(objDNS.RecursionTimeout), objOutputFile)        
    Call WriteLine("", objOutputFile)
    Call WriteLine("SERVICE",  objOutputFile)
    Call WriteLine(" Started   : " & _
                    strDisplayNull(objDNS.Started), objOutputFile)        
    Call WriteLine(" StartMode : " & _
                    strDisplayNull(objDNS.StartMode), objOutputFile)        
    Call WriteLine("", objOutputFile)
    Call WriteLine("WRITE AUTHORITY",  objOutputFile)
    Call WriteLine(" WriteAuthorityNS  : " & _
                    strDisplayNull(objDNS.WriteAuthorityNS), objOutputFile)        
    Call WriteLine(" WriteAuthoritySOA : " & _
                    strDisplayNull(objDNS.WriteAuthoritySOA), objOutputFile)        
    Call WriteLine("", objOutputFile)
    Call WriteLine("ZONE SETTINGS",  objOutputFile)
    Call WriteLine(" AutoReverseZones  : " & _
                    strDisplayNull(objDNS.AutoReverseZones), objOutputFile)        
    Call WriteLine(" BootMethod        : " & _
                    strDisplayNull(objDNS.BootMethod), objOutputFile)        
    Call WriteLine(" ForwardTimeout    : " & _
                    strDisplayNull(objDNS.ForwardTimeout), objOutputFile)        
    Call WriteLine(" LooseWildcarding  : " & _
                    strDisplayNull(objDNS.LooseWildcarding), objOutputFile)        
    Call WriteLine(" NameCheckFlag     : " & _
                    strDisplayNull(objDNS.NameCheckFlag), objOutputFile)        
    Call WriteLine(" RoundRobin        : " & _
                    strDisplayNull(objDNS.RoundRobin), objOutputFile)        
    Call WriteLine(" SecureResponses   : " & _
                    strDisplayNull(objDNS.SecureResponses), objOutputFile)        
    Call WriteLine(" StrictFileParsing : " & _
                    strDisplayNull(objDNS.StrictFileParsing), objOutputFile)        
    Call WriteLine("", objOutputFile)

    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " & strOutputFile & ".")
    End If

End Sub           
```



## Stop, Start, or Restart a DNS Server


```VB
'********************************************************************
'*
'* Sub DnsService()
'*
'* Purpose: Stops, starts, or restarts the DNS Server.
'*
'* Input:   strServer           a machine name
'*          strOutputFile       an output file name
'*          strUserName         the current user's name
'*          strPassword         the current user's password
'*          intServiceTask      The job to perform
'*
'* Output:  Results are either printed on screen or 
'*                                        saved in strOutputFile.
'*
'********************************************************************

Private Sub DnsService(strServer     , _
                       strUserName   , _
                       strPassword   , _
                       strOutputFile , _
                       intServiceTask, _
                       blnContextHelp  )

    ON ERROR RESUME NEXT

    Dim objFileSystem, objOutputFile, objService, objDnsSet, objDNS
    Dim intStatus
    Dim strWBEMClass

    If blnContextHelp then
        Wscript.Echo ""
        Select Case intServiceTask
            Case CONST_START
                Wscript.Echo "Starts the DNS Server Service."
            Case CONST_STOP
                Wscript.Echo "Stops the DNS Server Service."
            Case CONST_RESTART
                Wscript.Echo "Restarts the DNS Server Service."
        End Select
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Select Case intServiceTask
            Case CONST_START
                Wscript.Echo "  DnsServer Start [/S <server>] " & _
                                                                                                                    "[/U <username>] [/W <password>]"
            Case CONST_STOP
                Wscript.Echo "  DnsServer Stop [/S <server>] " & _
                                                                                                                    "[/U <username>] [/W <password>]"
            Case CONST_RESTART
                Wscript.Echo "  DnsServer Restart [/S <server>] " & _
                                                                                                                    "[/U <username>] [/W <password>]"
        End Select
        Wscript.Echo "                 [/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   server        A machine name."
        Wscript.Echo "   username      The current user's name."
        Wscript.Echo "   password      Password of the current user."
        Wscript.Echo "   outputfile    The output file name."
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Select Case intServiceTask
            Case CONST_START
                Wscript.Echo "  DnsServer Start /s MyMachine2"
                Wscript.Echo "  Starts the Dns Service on MyMachine2."
            Case CONST_STOP
                Wscript.Echo "  DnsServer Stop /s MyMachine2"
                Wscript.Echo "  Stops the Dns Service on MyMachine2."
            Case CONST_RESTART
                Wscript.Echo "  DnsServer Restart /s MyMachine2"
                Wscript.Echo "  Restarts the Dns Service on MyMachine2."
        End Select

        Wscript.Echo ""
        Exit Sub
    End If


    'Open a text file for output if the file is requested
    If Not IsEmpty(strOutputFile) Then
        If (NOT blnOpenFile(strOutputFile, objOutputFile)) Then
            Call Wscript.Echo ("Could not open an output file.")
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
        Call Wscript.Echo("Please check the server name, " _
                        & "credentials and WBEM Core.")
        Exit Sub
    End If
    strWBEMClass = "MicrosoftDNS_Server"

    Set objDNSSet = objService.Get("MicrosoftDNS_Server.name="".""")
    If blnErrorOccurred(" DNS Server not available.") then Exit Sub
    Select Case intServiceTask
        Case CONST_START
            intStatus = objDnsSet.StartService
        Case CONST_STOP
            intStatus = objDNSSet.StopService
        Case CONST_RESTART
            intStatus = objDNSSet.RestartDNSServer
    End Select

    If blnErrorOccurred(" DNS Service was not changed.") then
        Exit Sub
    Else
        Call WriteLine("Operation successful.", objOutputFile)
    End If

    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " & strOutputFile & ".")
    End If
    
End Sub
```



## Modify DNS Server Properties


```VB
'********************************************************************
'*
'* Sub DnsModify()
'*
'* Purpose: Stops, starts, or restarts the DNS Server.
'*
'* Input:   strServer           a machine name
'*          strOutputFile       an output file name
'*          strUserName         the current user's name
'*          strPassword         the current user's password
'*          strPropertyArray    The properties to change
'*          strValueArray       The New Values
'*
'* Output:  Results are either printed on screen or saved
'*                                     in strOutputFile.
'*
'********************************************************************

Private Sub DnsModify(strServer        , _
                      strUserName      , _
                      strPassword      , _
                      strOutputFile    , _
                      strPropertyArray , _
                      strValueArray    , _
                      blnContextHelp     )
                      
    ON ERROR RESUME NEXT

    Dim objFileSystem, objOutputFile, objService, objDnsSet, objDNS
    Dim intStatus
    Dim strWBEMClass

    If blnContextHelp then
        Wscript.Echo ""
        Wscript.Echo "Modifies Dns Server Properties."
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo "  DnsServer Modify <Property1> <Value1> " & _
                                                                                    "[Modify <Property2> <Value2>] [...]"
        Wscript.Echo "                    [/S <server>] " & _
                                                                                    "[/U <username>] [/W <password>]"
        Wscript.Echo "                    [/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   server        A machine name."
        Wscript.Echo "   username      The current user's name."
        Wscript.Echo "   password      Password of the current user."
        Wscript.Echo "   outputfile    The output file name."
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Wscript.Echo "  DnsServer.vbs Modify AutoReverseZones " & _
                                                                                    "True Modify MaxCacheTTL 1200"
        Wscript.Echo "  Changes the AutoReverseZones Property " & _
                                                                                    " to True and sets the MaxCacheTTL to 1200."
        Wscript.Echo ""
        Wscript.Echo "NOTE"
        Wscript.Echo ""
        Wscript.Echo "  Use the display command to see a list " & _
                                                                                    "of properties and descriptions."
        Wscript.Echo ""
        Exit Sub
    End If


    'Open a text file for output if the file is requested
    If Not IsEmpty(strOutputFile) Then
        If (NOT blnOpenFile(strOutputFile, objOutputFile)) Then
            Call Wscript.Echo ("Could not open an output file.")
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
        Call Wscript.Echo("Please check the server name, " _
                        & "credentials and WBEM Core.")
        Exit Sub
    End If
    strWBEMClass = "MicrosoftDNS_Server"

    Set objDNSSet = objService.Get("MicrosoftDNS_Server.Name="".""")
    If blnErrorOccurred(" DNS Server not available.") then Exit Sub


    For I = LBound(strPropertyArray) to UBound(strPropertyArray)
        If Not IsEmpty(strPropertyArray(I)) then
            Select Case lcase(strPropertyArray(I))
                Case "slave"
                    objDNSSet.Slave = strValueArray(I)
                Case "autocacheupdate"
                    objDNSSet.AutoCacheUpdate = strValueArray(I)
                Case "maxCachettl"
                    objDNSSet.MaxCacheTTL = strValueArray(I)
                Case "addressanswerlimit"
                    objDNSSet.AddressAnswerLimit = strValueArray(I)
                Case "allowupdate"
                    objDNSSet.AllowUpdate = strValueArray(I)
                Case "slowzonetransfer"
                    objDNSSet.SlowZoneTransfer = strValueArray(I)
                Case "disjointnets"
                    objDNSSet.DisjointNets = strValueArray(I)
                Case "forwarddelegation"
                    objDNSSet.ForwardDelegation = strValueArray(I)
                Case "localnetpriority"
                    objDNSSet.LocalNetPriority = strValueArray(I)
                Case "rpcprotocol"
                    objDNSSet.RpcProtocol = strValueArray(I)
                Case "sendonnondnsport"
                    objDNSSet.SendOnNonDnsPort = strValueArray(I)
                Case "dspollinginterval"
                    objDNSSet.DsPollingInterval = strValueArray(I)
                Case "forwardtimeout"
                    objDNSSet.ForwardTimeout = strValueArray(I)
                Case "eventloglevel"
                    objDNSSet.EventLogLevel = strValueArray(I)
                Case "loglevel"
                    objDNSSet.LogLevel = strValueArray(I)
                Case "autoreversezones"
                    objDNSSet.AutoReverseZones = strValueArray(I)
                Case "bootmethod"
                    objDNSSet.BootMethod = strValueArray(I)
                Case "loosewildcarding"
                    objDNSSet.LooseWildcarding = strValueArray(I)
                Case "namecheckflag"
                    objDNSSet.NameCheckFlag = strValueArray(I)
                Case "roundrobin"
                    objDNSSet.RoundRobin = strValueArray(I)
                Case "secureresponses"
                    objDNSSet.SecureResponses = strValueArray(I)
                Case "strictfileparsing"
                    objDNSSet.StrictFileParsing = strValueArray(I)
                Case "norecursion"
                    objDNSSet.NoRecursion = strValueArray(I)
                Case "recursionretry"
                    objDNSSet.RecursionRetry = strValueArray(I)
                Case "recursiontimeout"
                    objDNSSet.RecursionTimeout = strValueArray(I)
                Case "writeauthorityns"
                    objDNSSet.WriteAuthorityNS = strValueArray(I)
                Case "writeauthoritysoa"
                    objDNSSet.WriteAuthoritySOA = strValueArray(I)
                Case Else
                    Call WriteLine(strPropertyArray(I) & " is not valid.", objOutputFile)
                    Exit Sub
            End Select
        End If
    Next
    objDNSSet.Put_
    If blnErrorOccurred("Server properties not updated.") then
        Exit Sub
    Else
        Call WriteLine("Server properties are now updated.", objOutputFile)
    End If
        
    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " & strOutputFile & ".")
    End If        

End Sub
```



## Add an IP Address


```VB
'********************************************************************
'*
'* Sub DnsADDIP()
'*
'* Purpose: Adds an IP Addresses to an Array.
'*
'* Input:   strServer           a machine name
'*          strOutputFile       an output file name
'*          strUserName         the current user's name
'*          strPassword         the current user's password
'*          strPropertyArray    The properties to change
'*          strValueArray       The New Values
'*
'* Output:  Results are either printed on screen or 
'*                                        saved in strOutputFile.
'*
'********************************************************************

Private Sub DnsADDIP(strServer        , _
                     strUserName      , _
                     strPassword      , _
                     strOutputFile    , _
                     strPropertyArray , _
                     strValueArray    , _
                     blnContextHelp     )

    ON ERROR RESUME NEXT
    Dim objFileSystem, objOutputFile, objService, objDnsSet, objDNS
    Dim strTempArray()
    Dim intStatus, J, H
    Dim strWBEMClass
    Redim strTempArray(20)
    
    If blnContextHelp then
        Wscript.Echo ""
        Wscript.Echo "Adds an IP address to a property."
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo "  DnsServer AddIP <Property1> <Value1> " & _
                                                                                    "[Modify <Property2> <Value2>] [...]"
        Wscript.Echo "                  [/S <server>] " & _
                                                                                    "[/U <username>] [/W <password>]"
        Wscript.Echo "                  [/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   server        A machine name."
        Wscript.Echo "   username      The current user's name."
        Wscript.Echo "   password      Password of the current user."
        Wscript.Echo "   outputfile    The output file name."
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Wscript.Echo "  DnsServer.vbs AddIP ForwardersIPAddressesArray 10.10.10.10"
        Wscript.Echo "  Adds 10.10.10.10 to the FowardersIPAddressesArray."
        Wscript.Echo ""
        Exit Sub
    End If

    
    'Open a text file for output if the file is requested
    If Not IsEmpty(strOutputFile) Then
        If (NOT blnOpenFile(strOutputFile, objOutputFile)) Then
            Call Wscript.Echo ("Could not open an output file.")
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
        Call Wscript.Echo("Please check the server name, " _
                        & "credentials and WBEM Core.")
        Exit Sub
    End If

    strWBEMClass = "MicrosoftDNS_Server"
    Set objDNSSet = objService.Get("MicrosoftDNS_Server.Name="".""")
    If blnErrorOccurred(" DNS Server not available.") then Exit Sub
    
    For I = 0 to ubound(strPropertyArray)
        If Not IsEmpty(strPropertyArray(I)) then
            Select Case lcase(strPropertyArray(I))
                Case "forwardersipaddressesarray"
                    Redim strTempArray(20)
                    If IsNull(objDNSSet.forwardersipaddressesarray) _
                                                                                         then
                        strTempArray(0) = strValueArray(I)
                        Redim Preserve strTempArray(0)
                        objDNSSet.forwardersipaddressesarray = strTempArray
                    Else
                      J = 0
                      For H = _
                       lbound(objDNSSet.forwardersipaddressesarray) _
                       to ubound(objDNSSet.forwardersipaddressesarray)
                          strTempArray(H) = _
                            objDNSSet.forwardersipaddressesarray(H)
                          J = J + 1
                      Next
                      strTempArray(J) = strValueArray(I)
                      ReDim Preserve strTempArray(J)
                      objDNSSet.forwardersipaddressesarray = strTempArray
                    End If
                    objDNSSet.Put_
                    If err.Number <> 0 then
                        Call WriteLine("Error adding IP address.", objOutputFile)
                        Exit Sub                        
                    Else
                        Call WriteLine("IP address successfully added.", objOutputFile)
                    End If

                Case "listenipaddressesarray"
                    Redim strTempArray(20)
                    If IsNull(objDNSSet.ListenIPAddressesArray) then
                        strTempArray(0) = strValueArray(I)
                        Redim Preserve strTempArray(0)
                        objDNSSet.ListenIPAddressesArray = strTempArray
                    Else
                      J = 0
                      For H = lbound(objDNSSet.ListenIPAddressesArray) _
                                                    to ubound(objDNSSet.ListenIPAddressesArray)
                          strTempArray(H) = objDNSSet.ListenIPAddressesArray(H)
                          J = J + 1
                      Next
                      strTempArray(J) = strValueArray(I)
                      ReDim  Preserve strTempArray(J)
                      objDNSSet.ListenIPAddressesArray = strTempArray
                    End If
                    objDNSSet.Put_
                    If err.Number <> 0 then
                        Call WriteLine("Error adding IP address.", objOutputFile)
                        Exit Sub                        
                    Else
                        Call WriteLine("IP address successfully added.", objOutputFile)
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



## Delete an IP Address


```VB
'********************************************************************
'*
'* Sub DnsDELETEIP()
'*
'* Purpose: Removes IP addresses from arrays.
'*
'* Input:   strServer           a machine name
'*          strOutputFile       an output file name
'*          strUserName         the current user's name
'*          strPassword         the current user's password
'*          strPropertyArray    The properties to change
'*          strValueArray       The New Values
'*
'* Output:  Results are either printed on screen or 
'*                                        saved in strOutputFile.
'*
'********************************************************************

Private Sub DnsDELETEIP(strServer        , _
                        strUserName      , _
                        strPassword      , _
                        strOutputFile    , _
                        strPropertyArray , _
                        strValueArray    , _
                        blnContextHelp     )

    ON ERROR RESUME NEXT
    Dim objFileSystem, objOutputFile, objService, objDnsSet, objDNS
    Dim strTempArray()
    Dim intStatus, J, H
    Dim strWBEMClass
    Redim strTempArray(20)
    
    If blnContextHelp then
        Wscript.Echo ""
        Wscript.Echo "Deletes an IP address from a property."
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo "  DnsServer DeleteIP <Property1> <Value1> " & _
                                                                                    "[Modify <Property2> <Value2>] [...]"
        Wscript.Echo "                    [/S <server>] " & _
                                                                                    "[/U <username>] [/W <password>]"
        Wscript.Echo "                    [/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   server        A machine name."
        Wscript.Echo "   username      The current user's name."
        Wscript.Echo "   password      Password of the current user."
        Wscript.Echo "   outputfile    The output file name."
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Wscript.Echo "  DnsServer.vbs DeleteIP ForwardersIPAddressesArray 10.10.10.10"
        Wscript.Echo "  Removes 10.10.10.10 from the FowardersIPAddressesArray."
        Wscript.Echo ""
        Exit Sub
    End If

    
    'Open a text file for output if the file is requested
    If Not IsEmpty(strOutputFile) Then
        If (NOT blnOpenFile(strOutputFile, objOutputFile)) Then
            Call Wscript.Echo ("Could not open an output file.")
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
        Call Wscript.Echo("Please check the server name, " _
                        & "credentials and WBEM Core.")
        Exit Sub
    End If

    strWBEMClass = "MicrosoftDNS_Server"
    Set objDNSSet = objService.Get("MicrosoftDNS_Server.Name="".""")
    If blnErrorOccurred(" DNS Server not available.") then Exit Sub
    
    For I = 0 to ubound(strPropertyArray)
        If Not IsEmpty(strPropertyArray(I)) then
            Select Case lcase(strPropertyArray(I))
                Case "forwardersipaddressesarray"
                    Redim strTempArray(20)
                    If IsNull(objDNSSet.forwardersipaddressesarray) _
                    then
                        Call WriteLine("There are no IP addresses " _
                                                                                & "to delete.", objOutputFile)
                    Else
                      J = 0
                      For H = _
                       lbound(objDNSSet.forwardersipaddressesarray) _
                       to ubound(objDNSSet.forwardersipaddressesarray)
                          If strValueArray(I) <>_
                            objDNSSet.forwardersipaddressesarray(H) _
                          then
                            strTempArray(J) = _
                              objDNSSet.forwardersipaddressesarray(H)
                            J = J + 1
                          End If
                      Next
                      If J <> 0 then
                          ReDim Preserve strTempArray(J - 1)
                          objDNSSet.forwardersipaddressesarray = strTempArray
                      Else
                          objDnsSet.ForwardersIpAddressesArray = Null
                      End If
                    End If
                    objDNSSet.Put_
                    If err.Number <> 0 then
                        Call WriteLine("Error deleting IP address.", objOutputFile)
                        Exit Sub                        
                    Else
                        Call WriteLine("IP address successfully deleted.", objOutputFile)
                    End If

                Case "listenipaddressesarray"
                    Redim strTempArray(20)
                    If IsNull(objDNSSet.listenipaddressesarray) then
                        Call WriteLine("There are no IP addresses to delete.", objOutputFile)
                    Else
                        J = 0
                        For H = lbound(objDNSSet.listenipaddressesarray) _
                                                                to ubound(objDNSSet.listenipaddressesarray)
                            If strValueArray(I) <> objDNSSet.listenipaddressesarray(H) then
                                strTempArray(J) = objDNSSet.listenipaddressesarray(H)
                                J = J + 1
                            End If
                        Next
                        If J <> 0 then
                            ReDim Preserve strTempArray(J - 1)
                            objDNSSet.listenipaddressesarray = strTempArray
                        Else
                            objDnsSet.ForwardersIpAddressesArray = Null
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
                    Call WriteLine("Cannot add an IP address to " & _
                                    strPropertyArray(I), _
                                    objOutputFile)

            End Select
        End If    
    
    Next
    

    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " & strOutputFile & ".")
    End If

End Sub
```



## List Zones


```VB
'********************************************************************
'*
'* Sub DnsZone()
'*
'* Purpose: Lists instances of MicrosoftDNS_ServerDomainContainment.
'*
'* Input:   strServer           a machine name
'*          strOutputFile       an output file name
'*          strUserName         the current user's name
'*          strPassword         the current user's password
'*
'* Output:  Results are either printed on screen or saved 
'*          in strOutputFile.
'*
'********************************************************************

Private Sub DnsZone(strServer        , _
                     strUserName      , _
                     strPassword      , _
                     strOutputFile    , _
                     blnContextHelp     )


    ON ERROR RESUME NEXT
    Dim objFileSystem, objOutputFile, objService, objDnsSet, objDNS
    Dim strTempArray()
    Dim intStatus, J, H
    Dim strWBEMClass
    Redim strTempArray(20)
    
    If blnContextHelp then
        Wscript.Echo ""
        Wscript.Echo "Enumerates Domains associated with the Dns Server."
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo "  DnsServer Zone"
        Wscript.Echo "    [/S <server>] [/U <username>] [/W <password>]"
        Wscript.Echo "    [/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   server        A machine name."
        Wscript.Echo "   username      The current user's name."
        Wscript.Echo "   password      Password of the current user."
        Wscript.Echo "   outputfile    The output file name."
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Wscript.Echo "  DnsServer.vbs Zone"
        Wscript.Echo ""
        Exit Sub
    End If

    
    'Open a text file for output if the file is requested
    If Not IsEmpty(strOutputFile) Then
        If (NOT blnOpenFile(strOutputFile, objOutputFile)) Then
            Call Wscript.Echo ("Could not open an output file.")
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
        Call Wscript.Echo("Please check the server name, " _
                        & "credentials and WBEM Core.")
        Exit Sub
    End If
    dim Inst
    'Set objDNSSet = objService.AssociatorsOf("MicrosoftDNS_Server")
    Set objDNSSet = _
        objService.InstancesOf("MicrosoftDNS_ServerDomainContainment")
    If blnErrorOccurred(" DNS Server not available.") then Exit Sub
    Dim strTemp
    Stop
    For Each inst in objDnsSet
        strTemp = Inst.PartComponent & " "
        Do Until Len(strTemp) = 0
            I = 1
            Do Until Mid(strTemp,I,1) = ","
                If I = Len(strTemp) then Exit Do
                I = I + 1
            Loop
            Call WriteLine(Left(strTemp,I - 1), objOutputFile)
            strTemp = Right(strTemp,Len(StrTemp) - I)
        Loop
        Call WriteLine("", objOutputFile)
    Next
        
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
'* Output:  strServer         a remote server ("" = local server")
'*          strUserName       the current user's name
'*          strPassword       the current user's password
'*          strOutputFile     an output file name
'*
'********************************************************************
Private Function intParseCmdLine( ByRef strServer        , _
                                    ByRef strUserName      , _
                                    ByRef strPassword      , _
                                    ByRef strOutputFile    , _
                                    ByRef intServiceTask   , _
                                    ByRef strPropertyArray , _
                                    ByRef strValueArray    , _
                                    ByRef blnContextHelp     )
    

    ON ERROR RESUME NEXT

    Dim strFlag, strProperty, strValue
    Dim intState, intArgIter, intPropertyCount
    Dim objFileSystem
    ReDim strPropertyArray(20)
    ReDim strValueArray(20)

    blnContextHelp = False
    intPropertyCount = 0
    
    If Wscript.Arguments.Count > 0 Then
        strFlag = Wscript.arguments.Item(0)
    End If

    'Check to see if arguments have been received
    If IsEmpty(strFlag) Then                
        intParseCmdLine = CONST_LIST
        Exit Function
    End If

    'Check if the user is asking for help or is just confused
    If (strFlag="help") OR (strFlag="/h") OR (strFlag="\h") _
                        OR (strFlag="-h") OR (strFlag = "\?") _
                        OR (strFlag = "/?") OR (strFlag = "?") _ 
        OR (strFlag="h") Then
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
                If Not blnGetArg("Output File", strOutputFile, intArgIter) Then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If
                intArgIter = intArgIter + 1

            Case "/u"
                If Not blnGetArg("User Name", strUserName, intArgIter) Then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If
                intArgIter = intArgIter + 1

            Case "/w"
                If Not blnGetArg("User Password", strPassword, intArgIter) Then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If
                intArgIter = intArgIter + 1

            Case "addip"
                If Wscript.arguments.count <= intArgIter + 1 then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                Else
                    If Wscript.arguments(intArgIter + 1) = "/?" then
                        blnContextHelp = True
                        intParseCmdLine = CONST_ADD
                        intArgIter = intArgIter + 2
                    Else
                        If Wscript.arguments.count <= intArgIter + 2 then
                            intParseCmdLine = CONST_ERROR
                            Exit Function
                        End If
                        intParseCmdLine = CONST_ADD
                        strPropertyArray(intPropertyCount) = Wscript.Arguments(intArgIter + 1)
                        strValueArray(intPropertyCount) = Wscript.Arguments(intArgIter + 2)
                        intArgIter = intArgIter + 3
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
                        intParseCmdLine = CONST_DELETE
                        intArgIter = intArgIter + 2
                    Else
                        If Wscript.arguments.count <= intArgIter + 2 then
                            intParseCmdLine = CONST_ERROR
                            Exit Function
                        End If
                        intParseCmdLine = CONST_DELETE
                        strPropertyArray(intPropertyCount) = Wscript.Arguments(intArgIter + 1)
                        strValueArray(intPropertyCount) = Wscript.Arguments(intArgIter + 2)
                        intArgIter = intArgIter + 3
                        intPropertyCount = intPropertyCount + 1
                    End If
                End If
                
            Case "start"
                intParseCmdLine = CONST_SERVICE
                intServiceTask = CONST_START
                intArgIter = intArgIter + 1

            Case "stop"
                intParseCmdLine = CONST_SERVICE
                intServiceTask = CONST_STOP
                intArgIter = intArgIter + 1

            Case "restart"
                intParseCmdLine = CONST_SERVICE
                intServiceTask = CONST_RESTART
                intArgIter = intArgIter + 1

            Case "list"
                intParseCmdLine = CONST_LIST
                intArgIter = intArgIter + 1      

            Case "display"
                intParseCmdLine = CONST_DISPLAY
                intArgIter = intArgIter + 1      

            Case "zone"
                intParseCmdLine = CONST_ZONE
                intArgIter = intArgIter + 1      

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
                        If Wscript.arguments.count <= intArgIter + 2 then
                            intParseCmdLine = CONST_ERROR
                            Exit Function
                        End If
                        intParseCmdLine = CONST_MODIFY
                        strPropertyArray(intPropertyCount) = Wscript.Arguments(intArgIter + 1)
                        strValueArray(intPropertyCount) = Wscript.Arguments(intArgIter + 2)
                        intArgIter = intArgIter + 3
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
    Wscript.Echo "Gets and Sets DNS Server information for a machine."
    Wscript.Echo ""
    Wscript.Echo "SYNTAX:"
    Wscript.Echo "  DnsServer operation <Parameter List>"
    Wscript.Echo "                      [/S <server>] " _
                    & "[/U <username>] [/W <password>]"
    Wscript.Echo "                      [/O <outputfile>]"
    Wscript.Echo ""
    Wscript.Echo "  operation   [AddIP | DeleteIP | Start |" _
                    & " Stop | Restart | Modify |"
    Wscript.Echo "               List | Display | Zone]"
    Wscript.Echo ""
    Wscript.Echo "    For help on a specific operation type:"
    Wscript.Echo ""
    Wscript.Echo "              DnsServer AddIP /?"
    Wscript.Echo "              DnsServer DeleteIP /?"
    Wscript.Echo "              DnsServer Start /?"
    Wscript.Echo "              DnsServer Stop /?"
    Wscript.Echo "              DnsServer Restart /?"
    Wscript.Echo "              DnsServer Modify /?"
    Wscript.Echo "              DnsServer List /?"
    Wscript.Echo "              DnsServer Display /?"
    Wscript.Echo "              DnsServer Zone /?"
    Wscript.Echo ""
    Wscript.Echo ""
    Wscript.Echo "PARAMETER SPECIFIERS:"
    Wscript.Echo "   server        A machine name."
    Wscript.Echo "   username      The current user's name."
    Wscript.Echo "   password      Password of the current user."
    Wscript.Echo "   outputfile    The output file name."
    Wscript.Echo ""

End Sub

'********************************************************************
'*
'* Sub Display()
'*
'* Purpose: Shows a list of all available properties
'*          with descriptions.
'*
'* Input:   None
'*
'* Output:  Displayed on screen.
'*
'********************************************************************
Private Sub Display(strOutputFile, blnContextHelp)

    Dim objOutputFile

    'Open a text file for output if the file is requested
    If Not IsEmpty(strOutputFile) Then
        If (NOT blnOpenFile(strOutputFile, objOutputFile)) Then
            Call Wscript.Echo ("Could not open an output file.")
            Exit Sub
        End If
    End If

    If blnContextHelp then
        Wscript.Echo ""
        Wscript.Echo "Displays all available property types and descriptions."
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo "  DnsServer Display [/S <server>][/U <username>] [/W <password>]"
        Wscript.Echo "                    [/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   server        A machine name."
        Wscript.Echo "   username      The current user's name."
        Wscript.Echo "   password      Password of the current user."
        Wscript.Echo "   outputfile    The output file name."
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Wscript.Echo "  DnsServer.vbs Display"
        Wscript.Echo ""
        Exit Sub
    End If

    Call WriteLine("Property            Type       Description", objOutputFile)
    Call WriteLine("-----------------------------------------------------------------------------", objOutputFile)
    Call WriteLine("SERVER", objOutputFile)
    Call WriteLine(" name               read-only  Indicates the Fully Qualified Domain Name or IP", objOutputFile)
    Call WriteLine("                               address of the DNS server.", objOutputFile)
    Call WriteLine(" version            read-only  Indicates the version of the DNS server.", objOutputFile)
    Call WriteLine(" slave              True/False This Boolean indicates whether the DNS server is", objOutputFile)
    Call WriteLine("                               a Slave.", objOutputFile)
    Call WriteLine("", objOutputFile)
    Call WriteLine("CACHE", objOutputFile)
    Call WriteLine(" AutoCacheUpdate    True/False This Boolean indicates whether the DNS server", objOutputFile)
    Call WriteLine("                               attempts to update its cache entries using data", objOutputFile)
    Call WriteLine("                               from root servers.", objOutputFile)
    Call WriteLine(" MaxCacheTTL        Number     Indicates a maximum time (in seconds) a record", objOutputFile)
    Call WriteLine("                               of a recursive name query may remain in the DNS", objOutputFile)
    Call WriteLine("                               server cache.", objOutputFile)    
    Call WriteLine("", objOutputFile)
    Call WriteLine("COMMUNICATION", objOutputFile)
    Call WriteLine(" AddressAnswerLimit Number     Indicates the maximum number of host records", objOutputFile)
    Call WriteLine("                               returned in response to an address request.", objOutputFile)
    Call WriteLine("                               Values between 5 and 28 are valid.", objOutputFile)
    Call WriteLine(" AllowUpdate        Number     This Boolean indicates whether the DNS server", objOutputFile)
    Call WriteLine("                               accepts dynamic update requests.", objOutputFile)
    Call WriteLine(" DisjointNets       True/False This Boolean indicates whether override is", objOutputFile)
    Call WriteLine("                               allowed of the default binding for a socket", objOutputFile)
    Call WriteLine("                               used to send queries to remote DNS servers.", objOutputFile)
    Call WriteLine(" ForwardDelegation  True/False This Boolean indicates whether queries to", objOutputFile)
    Call WriteLine("                               delegated sub-zones are forwarded.", objOutputFile)
    Call WriteLine(" LocalNetPriority   True/False This Boolean indicates whether the DNS server", objOutputFile)
    Call WriteLine("                               gives priority to the local net address", objOutputFile)
    Call WriteLine("                               returning A records.", objOutputFile)
    Call WriteLine(" RpcProtocol        Number     Indicates the protocols over which", objOutputFile)
    Call WriteLine("                               administrative RPC runs.", objOutputFile)
    Call WriteLine(" SendOnNonDnsPort   Number     Indicates the port on which the DNS server", objOutputFile)
    Call WriteLine("                               sends UDP queries to other servers.", objOutputFile)
    Call WriteLine(" SlowZoneTransfer   True/False This Boolean determines the AXFR message format", objOutputFile)
    Call WriteLine("                               when sending to non-Microsoft DNS secondaries.", objOutputFile)
    Call WriteLine("", objOutputFile)
    Call WriteLine("DIRECTORY SERVICES", objOutputFile)
    Call WriteLine(" DsAvailable        True/False This Boolean indicates whether there is an", objOutputFile)
    Call WriteLine("                               available DS on the DNS server.", objOutputFile)
    Call WriteLine(" DsPollingInterval  Number     Indicates the interval (in seconds) to poll", objOutputFile)
    Call WriteLine("                               the DS-integrated zones.", objOutputFile)
    Call WriteLine("", objOutputFile)
    Call WriteLine("LOGGING", objOutputFile)    
    Call WriteLine(" EventLogLevel      Number     Indicates which events the DNS server records", objOutputFile)
    Call WriteLine("                               in the Event Viewer system log.", objOutputFile)
    Call WriteLine("                    ""0""        None", objOutputFile)
    Call WriteLine("                    ""1""        Log only errors", objOutputFile)    
    Call WriteLine("                    ""2""        Log only warnings and errors", objOutputFile)    
    Call WriteLine("                    ""3""        Log all events", objOutputFile)   
    Call WriteLine(" LogLevel           Number     Indicates which policies are activated in the", objOutputFile)
    Call WriteLine("                               Event Viewer system log.", objOutputFile)
    Call WriteLine("", objOutputFile)
    Call WriteLine("RECURSION", objOutputFile)
    Call WriteLine(" NoRecursion        True/False This Boolean indicates whether the DNS server", objOutputFile)
    Call WriteLine("                               does NOT do recursive lookups. If set to TRUE,", objOutputFile)
    Call WriteLine("                               recursive lookups are not done.", objOutputFile)
    Call WriteLine(" RecursionRetry     True/False Indicates the interval (in seconds) before", objOutputFile)
    Call WriteLine("                               retrying a recursive lookup.", objOutputFile)
    Call WriteLine("", objOutputFile)
    Call WriteLine("SERVICE", objOutputFile)
    Call WriteLine(" Started            Read-Only  Started is a boolean indicating whether the", objOutputFile)
    Call WriteLine("                               Service has been started (TRUE), or stopped", objOutputFile)
    Call WriteLine("                               (FALSE).", objOutputFile)
    Call WriteLine(" StartMode          Read-Only  StartMode is a string value indicating whether", objOutputFile)
    Call WriteLine("                               the Service is automatically started by a", objOutputFile)
    Call WriteLine("                               System, Operating System, etc. or only started", objOutputFile)
    Call WriteLine("                               upon request.", objOutputFile)
    Call WriteLine("", objOutputFile)    
    Call WriteLine("WRITE AUTHORITY", objOutputFile)
    Call WriteLine(" WriteAuthorityNS   True/False This Boolean indicates whether the DNS server", objOutputFile)
    Call WriteLine("                               writes NS records to the authority section on", objOutputFile)
    Call WriteLine("                               successful response.", objOutputFile)
    Call WriteLine(" WriteAuthoritySOA  True/False This Boolean indicates whether the DNS server", objOutputFile)
    Call WriteLine("                               writes SOA records to the authority section on", objOutputFile)
    Call WriteLine("                               successful response.", objOutputFile)
    Call WriteLine("", objOutputFile) 
    Call WriteLine("ZONE SETTINGS", objOutputFile)
    Call WriteLine(" AutoReverseZones   True/False This Boolean indicates whether the DNS server", objOutputFile)
    Call WriteLine("                               automatically creates standard reverse lookup", objOutputFile)
    Call WriteLine("                               zones.", objOutputFile)
    Call WriteLine(" BootMethod         Number     Indicates the DNS server's initialization", objOutputFile)
    Call WriteLine("                               method.", objOutputFile)
    Call WriteLine("                    ""0""        Uninitialized", objOutputFile)
    Call WriteLine("                    ""1""        From file", objOutputFile)    
    Call WriteLine("                    ""2""        From registry", objOutputFile)    
    Call WriteLine("                    ""3""        From directory", objOutputFile) 
    Call WriteLine(" ForwardTimeout     Number     Indicates how long (in seconds) a DNS server,", objOutputFile)
    Call WriteLine("                               forwarding a query, will wait for resolution", objOutputFile)
    Call WriteLine("                               from the forwarder, before attepmting to", objOutputFile)
    Call WriteLine("                               resolve the query itself.", objOutputFile)
    Call WriteLine(" LooseWildcarding   True/False This Boolean indicates whether the DNS server", objOutputFile)
    Call WriteLine("                               does wildcarding loosely.", objOutputFile)
    Call WriteLine(" NameCheckFlag      Number     Indicates the set of eligible characters to be", objOutputFile)
    Call WriteLine("                               used in DNS names.", objOutputFile)
    Call WriteLine("                    ""0""        Strict RFC (ANSI)", objOutputFile)
    Call WriteLine("                    ""1""        Non RFC (ANSI)", objOutputFile)    
    Call WriteLine("                    ""2""        From registry", objOutputFile)    
    Call WriteLine("                    ""3""        Multibyte (UTF8)", objOutputFile)    
    Call WriteLine(" RoundRobin         True/False This Boolean indicates whether the DNS server", objOutputFile)
    Call WriteLine("                               round robins multiple A records.", objOutputFile)
    Call WriteLine(" SecureResponses    True/False This Boolean indicates whether the DNS server", objOutputFile)
    Call WriteLine("                               only saves records of names that are in the", objOutputFile)
    Call WriteLine("                               same subtree as the server that provided them.", objOutputFile)
    Call WriteLine(" StrictFileParsing  True/False This Boolean indicates whether the DNS server", objOutputFile)
    Call WriteLine("                               parses zone files strictly.", objOutputFile)
    
    
    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " & strOutputFile & ".")
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
'* Purpose: Attaches spaces to a string to increase 
'*          the length to intWidth.
'*
'* Input:   strString   a string
'*          intWidth    the intended length of the string
'*          blnAfter    Should spaces be added after the string?
'*          blnTruncate specifies whether to truncate the string 
'*                      or not if the string length is longer 
'*                      than intWidth
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
            strPackString = Space(intWidth-Len(strString)) & strString & " "
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

    'this value changes to True upon successful completion
    blnGetArg = False 

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
'* Purpose: Connects to machine strServer.
'*
'* Input:   strServer       a machine name
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
            Call Wscript.Echo( "Error description: " & Err.Description & "." )
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
            Call Wscript.Echo( "Error description: " & Err.Description & "." )
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
        Call Wscript.Echo( "Error 0x" & CStr(Hex(Err.Number)) & " occurred." )
        If Err.Description <> "" Then
            Call Wscript.Echo( "Error description: " & Err.Description & "." )
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
                    Call Wscript.Echo( "An unexpected program " _
                                       & "was used to run this script." )
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
             & "95/98 or" & vbCRLF & "2. Changing the default " _
             & "Windows Script Host setting to CScript" & vbCRLF _
             & "    using ""CScript " & "//H:CScript //S and " _
             & "running the script using" & vbCRLF & _
             "    ""PS.VBS arguments"" for Windows NT/2000." )
        WScript.Quit
    End If

End Sub

'********************************************************************
'*
'* Sub WriteLine()
'* Purpose: Writes a text line either to a file or on screen.
'* Input:   strMessage  the string to print
'*          objFile     an output file object
'* Output:  strMessage is either displayed on screen or 
'*          written to a file.
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
'* Purpose: Reports error with a string saying what the error 
'*          occurred in.
'*
'* Input:   strIn    string saying what the error occurred in.
'*
'* Output:  displayed on screen 
'* 
'********************************************************************
Private Function blnErrorOccurred (ByVal strIn)

    If Err.Number Then
        Call Wscript.Echo( "Error 0x" & CStr(Hex(Err.Number)) & ": " & strIn)
        If Err.Description <> "" Then
            Call Wscript.Echo( "Error description: " & Err.Description)
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
'* Input:   strFileName    A string with the name of the file.
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

    'Create a file object
    Set objFileSystem = CreateObject("Scripting.FileSystemObject")
    If blnErrorOccurred("Could not create filesystem object.") Then
        blnOpenFile = False
        Set objOpenFile = Nothing
        Exit Function
    End If

    'Open the file for output
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



 

 




