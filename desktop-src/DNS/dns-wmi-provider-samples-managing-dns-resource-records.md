---
title: DNS WMI Provider Samples—Managing DNS Resource Records
description: DNS WMI Provider Samples—Managing DNS Resource Records
ms.assetid: 4b038c74-eec8-459c-9e3f-3be2a244d313
ms.topic: article
ms.date: 05/31/2018
---

# DNS WMI Provider Samples—Managing DNS Resource Records

This section demonstrates scripting tasks associated with managing DNS resource records. The links below jump to subroutines in the script file.

-   [List resource records](#list-resource-records)
-   [Add a resource record](#add-a-resource-record)
-   [Delete a resource record](#delete-a-resource-record)
-   [Modify a resource record](#modify-a-resource-record)
-   [Connect to the DNS WMI Provider](#connect-to-the-dns-wmi-provider)

The general implementation of the script is as follows:

1.  A class is created for each resource record type.
2.  Resource record data is provided through user command-line inputs and DNS WMI Provider information for each record type class.
3.  Common functions such as list, delete, and modify are created and can be used on individual resource record type classes.

This code example shows tasks associated with Managing DNS resource records.


```VB
'********************************************************************
'*
'*  File:           DnsResource.vbs
'*
'*  Main Function:  Gets DNS Resource Record Data.
'*
'********************************************************************

OPTION EXPLICIT

    'Define constants
    CONST CONST_ERROR                   = 0
    CONST CONST_WSCRIPT                 = 1
    CONST CONST_CSCRIPT                 = 2
    CONST CONST_SHOW_USAGE              = 3
    CONST CONST_CREATE                  = 4
    CONST CONST_DELETE                  = 5
    CONST CONST_MODIFY                  = 6
    CONST CONST_LIST                    = 7

    'Declare variables
    Dim intOpMode, i, intCount
    Dim strServer, strUserName, strPassword, strOutputFile
    Dim blnContextHelp
    Dim strOwner, strZone, strDomain, strRecordDAta
    Dim intTTL
    Dim ObjService, objOutputFile
    Dim cResource
    
    ' Ensure the host is script, If not then abort
    VerIfyHostIsCscript()

    'Parse the command line
    intOpMode = intParseCmdLine(strServer        , _
                                strUserName      , _
                                strPassword      , _
                                strOutputFile    , _
                                strDomain        , _
                                cResource        , _
                                blnContextHelp     )
    Select Case intOpMode

        Case CONST_SHOW_USAGE
            Call ShowUsage()

        Case CONST_LIST
            Call DnsList(strServer        , _
                         strUserName      , _
                         strPassword      , _
                         strOutputFile    , _
                         strDomain        , _
                         cResource        , _
                         blnContextHelp     )

        Case CONST_CREATE
            Call DnsCreate(strServer        , _
                           strUserName      , _
                           strPassword      , _
                           strOutputFile    , _
                           cResource        , _
                           blnContextHelp     )

        Case CONST_DELETE
            Call DnsDelete(strServer        , _
                           strUserName      , _
                           strPassword      , _
                           strOutputFile    , _
                           cResource        , _
                           blnContextHelp     )

        Case CONST_Modify
            Call DnsModify(strServer        , _
                           strUserName      , _
                           strPassword      , _
                           strOutputFile    , _
                           cResource        , _
                           blnContextHelp     )

        Case CONST_ERROR
            Call Wscript.Echo("Error occurred in passing parameters.")

        Case Else                    'Default -- should never happen
            Call Wscript.Echo("Error occurred in passing parameters.")

    End Select

'********************************************************************
'* End of Script
'********************************************************************

'********************************************************************
'* Classes
'********************************************************************

Class A_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strRecordData
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "A"
        intParseArguments = 2
        strClass = "MicrosoftDNS_AType"
        ReDim strModifyPropertyArray(1,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds an A (Host) Record to a Zone.", _
                        "  DnsResource /Add A <zone> <host> <ipaddress>", _
                       "   host          A host name." & vbCRLF & _
                       "   ipaddress     The IP Address for the host.", _
                       "   DnsResource.vbs /Add A Example.microsoft.com MyHost.MyDomain " _ 
                           & "192.78.101.4" & vbCRLF & _
                       "   Creates an A record in " & _
                           "Example.microsoft.com, " & _
                       "in the MyDomain domain, with the " _
                       & "name MyHost.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes an A (Host) Record from a Zone.", _
                       "  DnsResource /Delete A <zone> <host> <ipaddress>", _
                       "   host          A host name." & vbCRLF & _
                       "   ipaddress     The IP Address for the host.", 
                   "   DnsResource.vbs /Delete A Example.microsoft.com " & _ 
                   " MyHost.MyDomain 192.78.101.4" & vbCRLF & _
                   "   Deletes the A record in Example.microsoft.com, in the" & _ 
                   " MyDomain domain, with the name MyHost.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies an A (Host) Record.", _
                       "  DnsResource /Modify A <zone> <host> ", & _
                       "<ipaddress> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   IPAddress" & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   value         The new value for the listed property." & _
                       "   host          A host name." & vbCRLF & _
                       "   ipaddress     The IP Address for the host.", _
                       "   DnsResource.vbs /Modify A Example.microsoft.com " _
                       & "MyHost.MyDomain 192.78.101.4 " _ 
                       & "IPAddress 192.78.101.38 " _
                   & "TTL 7200" & vbCRLF & _
                       "   Modifies an A record's ip address and TTL.")
        ModifyHelp = 1
    End Function

    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, _
                                            strArgArray(1))
        strRecordData = strArgArray(2)
        strText = strOwnername & " IN A " & strRecordData
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strRecordData = objDNS.RecordData
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Host Name  : " & strOwnerName, objOutputFile)
        Call WriteLine("  IP Address : " & strRecordData, objOutputFile)
        Call WriteLine("  DNS Server : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone       : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain     : " & strDomainName,objOutputFile)
        Call WriteLine("  TTL        : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn
        strQuery = strStandardQuery(strClass, strContainerName, _
                                    strDnsServerName, strDomainName, _
                                    strOwnerName, strTTL)

        If Not IsEmpty(strRecordData) then
            strQuery = strQuery & _
                       " RecordData=""" & strRecordData & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") _
        Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 1
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "ipaddress"
                        objInParam.IPAddress = _
                          strModifyPropertyArray(I,1)
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) _
                                       & " is not a valid property.",
                                       objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class CNAME_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strRecordData
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "CNAME"
        intParseArguments = 2
        strClass = "MicrosoftDNS_CNAMEType"
        ReDim strModifyPropertyArray(1,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds a CNAME (Alias) Record to a Zone.", _
                       "  DnsResource /Add CNAME <zone> <alias> " _
                       &"<host>", _
                       "   alias         Alias name." & vbCRLF & _
                       "   host          Name of the host.", _
                       "   DnsResource.vbs /Add CNAME " _
                       &"Example.microsoft.com www.MyDomain " _
                       &"MyHost.MyDomain" & vbCRLF & _
                       "   Creates an alias for MyHost called " _
                       & "www in the MyDomain.Example.microsoft.com" _
                       &" domain.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes a /Delete CNAME Record from " _
                       & "a Zone.", _
                       "  DnsResource /Add CNAME <zone> <alias> " _
                       & "<host>", _
                       "   alias         Alias name." & vbCRLF & _
                       "   host          Name of the host.", _
                       "   DnsResource.vbs /Delete CNAME " & _
                       "Example.microsoft.com www.MyDomain " _
                       "MyHost.MyDomain" & vbCRLF & _
                       "   Deletes the alias for MyHost called " _
                       & "www in the MyDomain.Example.microsoft.com" _
                       & "domain.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies a CNAME (Alias) Record.", _
                       "  DnsResource /Modify CNAME <zone> <alias> " _
                       & " <host> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & _
                       vbCRLF & _
                       "                   Host" & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   value         The new value for the " _
                       & "listed property." & vbCRLF & _
                       "   alias         Alias name." & vbCRLF & _
                       "   host          Name of the host.", _
                       "   DnsResource.vbs /Modify CNAME " _
                       & "Example.microsoft.com www.MyDomain " _
                       & "MyHost.MyDomain ttl 7400" & vbCRLF & _
                       "   Modifies the alias' TTL value to 7400.")
        ModifyHelp = 1
    End Function
    
    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, _
                                            strArgArray(1))
        strRecordData = strFindFQDNOwnerName(strContainerName, _
                                             strArgArray(2))
        strText = strOwnername & " IN CNAME " & strRecordData
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strRecordData = objDNS.RecordData
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Alias Name : " & strOwnerName, _
                        objOutputFile)
        Call WriteLine("  Host Name  : " & strRecordData, _
                        objOutputFile)
        Call WriteLine("  DNS Server : " & strDNSServerName, _
                        objOutputFile)
        Call WriteLine("  Zone       : " & strContainerName, _
                        objOutputFile)
        Call WriteLine("  Domain     : " & strDomainName, _
                        objOutputFile)
        Call WriteLine("  TTL        : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn
        strQuery = strStandardQuery(strClass, strContainerName,_
                                    strDnsServerName, strDomainName, _
                                    strOwnerName, strTTL)
        If Not IsEmpty(strRecordData) then
            strQuery = strQuery & _
              " RecordData=""" & strRecordData & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") _
        Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 1
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                  Case "ttl"
                      objInParam.TTL = strModifyPropertyArray(I,1)
                  Case "host"
                      objInParam.PrimaryName = _
                       strModifyPropertyArray(I,1)
                  Case else
                      Modify = True
                      Call WriteLine(strModifyPropertyArray(I,0) _
                                     & " is not a valid property.", _
                                     objOutputFile)
                      Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class MX_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strRecordData
    Public strPreference
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "MX"
        intParseArguments = 3
        strClass = "MicrosoftDNS_MXType"
        ReDim strModifyPropertyArray(2,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds a MX (Mail Exchange) Record " _
                       & "to a Zone.", _
                       "  DnsResource /Add MX <zone> " _
                       & "<recordname> <mailexchange> <preference>", _
                       "   recordname    Name for the MX record." _
                       & vbCRLF & _
                       "   mailexchange  Name of the mail server." _
                       & vbCRLF & _
                       "   preference    The preference given " _
                       & "to this MX record over others (Low values " _
                       & "are preferred).", _
                       "   DnsResource.vbs /Add MX Example.microsoft.com" _
                       & " @ Mail 10" & vbCRLF & _
                       "   Creates a MX Record that sends mail addressed" _
                       & " to Example.microsoft.com to the host " _
                       & "Mail.Example.microsoft.com.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes a MX (Mail Exchange) Record from a Zone.", _
                       "  DnsResource /DeleteMX <zone> <recordname>" _
                       & " <mailexchange> <preference>", _
                       "   recordname    Name for the MX record." _
                       & vbCRLF & _
                       "   mailexchange  Name of the mail server." _
                       & vbCRLF & _
                       "   preference    The preference given to " _
                       & "this MX record over others (Low values " _
                       & "are preferred).", _
                       "   DnsResource.vbs /Delete MX " _
                       & "Example.microsoft.com Example.microsoft.com " _
                       & "Mail.Example.microsoft.com 10" & vbCRLF & _
                       "   Deletes the MX Record that sends mail " _
                       & "addressed to Example.microsoft.com to " _
                       & "the host Mail.Example.microsoft.com.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies a MX (Mail Exchange) Record.", _
                       "  DnsResource /Modify MX <zone> <zone> <recordname> <mailexchange> <preference> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   recordname" & vbCRLF & _
                       "                   mailexchange" & vbCRLF & _
                       "                   preference" & vbCRLF & _
                       "   value         The new value for the listed property." & vbCRLF & _
                       "   recordname    Name for the MX record." & vbCRLF & _
                       "   mailexchange  Name of the mail server." & vbCRLF & _
                       "   preference    The preference given to this MX record over others (Low values are preferred).", _
                       "   DnsResource.vbs /Modify MX Example.microsoft.com Example.microsoft.com Mail.Example.microsoft.com 10 preference 90" & vbCRLF & _
                       "   Modifies the MX record's TTL preference to 90.")
        ModifyHelp = 1
    End Function

    
    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, strArgArray(1))
        strRecordData = strFindFQDNOwnerName(strContainerName, strArgArray(2))
        strPreference = strArgArray(3)
        strText = strOwnername & " IN MX  " & strPreference & " " & strRecordData
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strRecordData = objDNS.MailExchange
        strPreference = objDNS.Preference
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Record Name   : " & strOwnerName, objOutputFile)
        Call WriteLine("  Mail Exchange : " & strRecordData, objOutputFile)
        Call WriteLine("  Preference    : " & strPreference, objOutputFile)
        Call WriteLine("  DNS Server    : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone          : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain        : " & strDomainName, objOutputFile)
        Call WriteLine("  TTL           : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn
        
        strQuery = strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)
        If Not IsEmpty(strRecordData) then
            strQuery = strQuery & " MailExchange=""" & strRecordData & """ and"
        End If
        If Not IsEmpty(strPreference) then
            strQuery = strQuery & " Preference=""" & strPreference & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 2
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "mailexchange"
                        objInParam.MailExchange = strModifyPropertyArray(I,1)
                    Case "preference"
                        objInParam.Preference = strModifyPropertyArray(I,1)
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class SOA_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strExpireLimit
    Public strMinimumTTL
    Public strPrimaryServer
    Public strRefreshInterval
    Public strResponsibleParty
    Public strRetryDelay
    Public strSerialNumber
    Public strTTL
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "SOA"
        intParseArguments = 0
        strClass = "MicrosoftDNS_SOAType"
        ReDim strModifyPropertyArray(7,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function ModifyHelp
        Call ClassHelp("Modifies a SOA (Start Of Authority) Record.", _
                       "    DnsResource /Modify SOA <zone> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   expirelimit" & vbCRLF & _
                       "                   minimumttl" & vbCRLF & _
                       "                   primaryserver" & vbCRLF & _
                       "                   refreshinterval" & vbCRLF & _
                       "                   responsibleparty" & vbCRLF & _
                       "                   retrydelay" & vbCRLF & _
                       "                   serialnumber" & vbCRLF & _
                       "                   ttl" & vbCRLF & _
                       "   value         The new value for the listed property." ,  _
                       "    DnsResource.vbs /Modify Example.microsoft.com SOA expirelimit 70000 retrydelay 500" & vbCRLF & _
                       "    Modifies the SOA record's expire limit and retry delay properties.")
        ModifyHelp = 1
    End Function
    
    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strExpireLimit = objDNS.ExpireLimit
        strMinimumTTL = objDns.MinimumTTL
        strPrimaryServer = objDns.PrimaryServer
        strRefreshInterval = objDns.RefreshInterval
        strRetryDelay = objDns.RetryDelay
        strSerialNumber = objDns.SerialNumber
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Expire Limit      : " & strExpireLimit, objOutputFile)
        Call WriteLine("  Minimum TTL       : " & strMinimumTTL, objOutputFile)
        Call WriteLine("  Primary Server    : " & strPrimaryServer, objOutputFile)
        Call WriteLine("  Refresh Interval  : " & strRefreshInterval, objOutputFile)
        Call WriteLine("  Responsible Party : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Retry Delay       : " & strRetryDelay, objOutputFile)
        Call WriteLine("  Serial Number     : " & strSerialNumber, objOutputFile)
        Call WriteLine("  TTL               : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn
        
        strQuery = "Select * From MicrosoftDNS_SOAtype Where"
        If Not IsEmpty(strContainerName) then
            strQuery = strQuery & " ContainerName=""" & strContainerName & """ and"
        End If
        If Not IsEmpty(strDnsServerName) then
            strQuery = strQuery & " DnsServerName=""" & strDnsServerName & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 7
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "expirelimit"
                        objInParam.ExpireLimit = strModifyPropertyArray(I,1)
                    Case "minimumttl"
                        objInParam.MinimumTTL = strModifyPropertyArray(I,1)
                    Case "primaryserver"
                        objInParam.PrimaryServer = strModifyPropertyArray(I,1)
                    Case "refreshinterval"
                        objInParam.RefreshInterval = strModifyPropertyArray(I,1)
                    Case "responsibleparty"
                        objInParam.ResponsibleParty = strModifyPropertyArray(I,1)
                    Case "retrydelay"
                        objInParam.RetryDelay = strModifyPropertyArray(I,1)
                    Case "serialnumber"
                        objInParam.SerialNumber = strModifyPropertyArray(I,1)
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function

End Class

Class PTR_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strRecordData
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "PTR"
        intParseArguments = 2
        strClass = "MicrosoftDNS_PTRType"
        ReDim strModifyPropertyArray(1,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds a PTR (Pointer) Record to a Zone.", _
                       "  DnsResource /Add PTR <zone> <recordname> <host>", _
                       "   recordname    The name of the pointer record" & vbCRLF & _
                       "   host          Name of the host.", _
                       "   DnsResource.vbs /Add PTR 15.251.123.in-addr.arpa 5 MyHost.Example.microsoft.com." & vbCRLF & _
                       "   Creates a pointer to the ip address of 15.251.123.5 to MyHost.Example.microsoft.com.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes a PTR (Pointer) Record from a Zone.", _
                       "  DnsResource /Delete PTR <zone> <recordname> <host>", _
                       "   recordname    The name of the pointer record" & vbCRLF & _
                       "   host          Name of the host.", _
                       "   DnsResource.vbs /Delete PTR 15.251.123.in-addr.arpa 5 MyHost.Example.microsoft.com." & vbCRLF & _
                       "   Deletes the pointer to the ip address of 15.251.123.5 to MyHost.Example.microsoft.com.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies a PTR (Pointer) Record.", _
                       "  DnsResource /Modify PTR <zone> <recordname> <host> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   Host" & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   recordname    The name of the pointer record" & vbCRLF & _
                       "   host          Name of the host.", _
                       "    DnsResource.vbs /Modify PTR 15.251.123.in-addr.arpa 5 MyHost.Example.microsoft.com ttl 7400" & vbCRLF & _
                       "    Modifies the pointers' TTL value to 7400.")
        ModifyHelp = 1
    End Function

    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, strArgArray(1))
        strRecordData = strFindFQDNOwnerName(strContainerName, strArgArray(2))
        strText = strOwnername & " IN PTR " & strRecordData
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strRecordData = objDNS.RecordData
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Record Name : " & strOwnerName, objOutputFile)
        Call WriteLine("  Host Name   : " & strRecordData, objOutputFile)
        Call WriteLine("  DNS Server  : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone        : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain      : " & strDomainName, objOutputFile)
        Call WriteLine("  TTL         : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn

        strQuery = strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)        
        If Not IsEmpty(strRecordData) then
            strQuery = strQuery & " RecordData=""" & strRecordData & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 1
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "host"
                        objInParam.PTRDomainName = strModifyPropertyArray(I,1)
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class NS_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strRecordData
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "NS"
        intParseArguments = 2
        strClass = "MicrosoftDNS_NSType"
        ReDim strModifyPropertyArray(1,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds a NS (Name Server) Record to a Zone.", _
                       "  DnsResource /Add NS <zone> <recordname> <nshost>", _
                       "   recordname    The name of the NS Record" & vbCRLF & _
                       "   nshost        Name of the host.", _
                       "   DnsResource.vbs /Add NS Example.microsoft.com MyDomain MyHost.MyDomain" & vbCRLF & _
                       "   Creates a NS record for MyHost.MyDomain.Example.microsoft.com in the MyDomain domain.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes a NS (Name Server) Record from a Zone.", _
                       "  DnsResource /Delete NS <zone> <recordname> <nshost>", _
                       "   recordname    The name of the NS Record" & vbCRLF & _
                       "   nshost        Name of the host.", _
                       "   DnsResource.vbs /Delete NS Example.microsoft.com MyDomain MyHost.MyDomain" & vbCRLF & _
                       "   Deletes the NS record for MyHost.MyDomain.Example.microsoft.com in the MyDomain domain.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies a NS (Name Server) Record.", _
                       "  DnsResource /Modify NS <zone> <recordname> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   NSHost" & vbCRLF & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   value         The new value for the listed property." & vbCRLF & _
                       "   recordname    The name of the NS Record" & vbCRLF & _
                       "   nshost        Name of the host.", _
                       "   DnsResource.vbs /Modify NS Example.microsoft.com MyDomain MyHost.MyDomain ttl 7400" & vbCRLF & _
                       "   Modifies the NS Records' TTL value to 7400.")
        ModifyHelp = 1
    End Function

    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, strArgArray(1))
        strRecordData = strFindFQDNOwnerName(strContainerName, strArgArray(2))
        strText = strOwnername & " IN NS " & strRecordData
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strRecordData = objDNS.RecordData
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Record Name : " & strOwnerName, objOutputFile)
        Call WriteLine("  NS Host     : " & strRecordData, objOutputFile)
        Call WriteLine("  DNS Server  : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone        : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain      : " & strDomainName, objOutputFile)
        Call WriteLine("  TTL         : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn
        
        strQuery = strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)
        If Not IsEmpty(strRecordData) then
            strQuery = strQuery & " RecordData=""" & strRecordData & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        wscript.echo(strQuery)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 1
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "nshost"
                        objInParam.NSHost = strModifyPropertyArray(I,1)
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next
        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class AAAA_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strRecordData
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "AAAA"
        intParseArguments = 2
        strClass = "MicrosoftDNS_AAAAType"
        ReDim strModifyPropertyArray(1,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds an AAAA (IPV6) Record to a Zone.", _
                       "  DnsResource /Add AAAA <zone> <host> <ipv6>", _
                       "   host          A host name." & vbCRLF & _
                       "   ipv6          The IPV6 Host Address", _
                       "   DnsResource.vbs /Add AAAA Example.microsoft.com MyHost 4321:0:1:2:3:4:567:89ab" & vbCRLF & _
                       "   Creates an AAAA record for MyHost.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes an AAAA (IPV6) Record from a Zone.", _
                       "  DnsResource /Delete AAAA <zone> <host> <ipv6>", _
                       "   host          A host name." & vbCRLF & _
                       "   ipv6          The IPV6 Host Address", _
                       "   DnsResource.vbs /Delete AAAA Example.microsoft.com MyHost 4321:0:1:2:3:4:567:89ab" & vbCRLF & _
                       "   Deletes the AAAA record for MyHost.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies an AAAA (IPV6) Record.", _
                       "  DnsResource /Modify AAAA <zone> <host> <ipv6> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   ipv6" & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   value         The new value for the listed property." & vbCRLF & _
                       "   host          A host name." & vbCRLF & _
                       "   ipv6          The IPV6 Host Address", _
                       "   DnsResource.vbs /Modify AAAA Example.microsoft.com MyHost 4321:0:1:2:3:4:567:89ab ttl 7400" & vbCRLF & _
                       "   Modifies the AAAA TTL value to 7400.")
        ModifyHelp = 1
    End Function
    
    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, strArgArray(1))
        strRecordData = strArgArray(2)
        strText = strOwnername & " IN AAAA " & strRecordData
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strRecordData = objDNS.RecordData
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Host Name  : " & strOwnerName, objOutputFile)
        Call WriteLine("  IPV6       : " & strRecordData, objOutputFile)
        Call WriteLine("  DNS Server : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone       : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain     : " & strDomainName, objOutputFile)
        Call WriteLine("  TTL        : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn

        strQuery = strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)        
        If Not IsEmpty(strRecordData) then
            strQuery = strQuery & " RecordData=""" & strRecordData & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 1
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "ipv6"
                        objInParam.IPV6Address = strModifyPropertyArray(I,1)
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class AFSDB_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strSubType
    Public strRecordData
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "AFSDB"
        intParseArguments = 3
        strClass = "MicrosoftDNS_AFSDBType"
        ReDim strModifyPropertyArray(2,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds an AFSDB (AFS Database) Record to a Zone.", _
                       "  DnsResource /Add AFSDB <zone> <recordname> <host> <subtype>", _
                       "   recordname    The name of the AFSDB record" & vbCRLF & _
                       "   host          Name of the host." & vbCRLF & _
                       "   subtype       The subtype of the host AFS Server." & vbCRLF & _
                       "                 1 = AFS" & vbCRLF & _
                       "                 2 = DCE", _
                       "    DnsResource.vbs /Add AFSDB Example.microsoft.com afsdb.MyDomain MyHost.MyDomain 2" & vbCRLF & _
                       "    Creates a DCE type AFSDB record for MyHost.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes an AFSDB (AFS Database) Record from a Zone.", _
                       "  DnsResource /Delete AFSDB <zone> <recordname> <host> <subtype>", _
                       "   recordname    The name of the AFSDB record" & vbCRLF & _
                       "   host          Name of the host." & vbCRLF & _
                       "   subtype       The subtype of the host AFS Server." & vbCRLF & _
                       "                 1 = AFS" & vbCRLF & _
                       "                 2 = DCE", _
                       "    DnsResource.vbs /Delete AFSDB Example.microsoft.com afsdb.MyDomain MyHost.MyDomain 2" & vbCRLF & _
                       "    Deletes the DCE type AFSDB record for MyHost.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies an AFSDB (AFS Database) Record.", _
                       "  DnsResource /Modify AFSDB <zone> <recordname> <host> <subtype> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   Host" & vbCRLF & _
                       "                   Subtype" & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   value         The new value for the listed property." & _
                       "   recordname    The name of the AFSDB record" & vbCRLF & _
                       "   host          Name of the host." & vbCRLF & _
                       "   subtype       The subtype of the host AFS Server." & vbCRLF & _
                       "                 1 = AFS" & vbCRLF & _
                       "                 2 = DCE", _
                       "    DnsResource.vbs /Modify AFSDB Example.microsoft.com afsdb.MyDomain MyHost.MyDomain 2 ttl 7400" & vbCRLF & _
                       "    Modifies the AFSDB's  TTL value to 7400.")
        ModifyHelp = 1
    End Function
    
    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, strArgArray(1))
        strRecordData = strFindFQDNOwnerName(strContainerName, strArgArray(2))
        strSubtype = strArgArray(3)
        strText = strOwnername & " IN AFSDB  " & strSubtype & " " & strRecordData
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strRecordData = objDNS.ServerName
        strSubtype = objDNS.SubType
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Record Name : " & strOwnerName, objOutputFile)
        Call WriteLine("  Host Name   : " & strRecordData, objOutputFile)
        Call WriteLine("  Subtype     : " & strRecordData, objOutputFile)
        Call WriteLine("  DNS Server  : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone        : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain      : " & strDomainName, objOutputFile)
        Call WriteLine("  TTL         : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn
        
        strQuery = strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)
        If Not IsEmpty(strRecordData) then
            strQuery = strQuery & " ServerName=""" & strRecordData & """ and"
        End If
        If Not IsEmpty(strSubType) then
            strQuery = strQuery & " Subtype=""" & strSubType & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        wscript.echo strQuery
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 1
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "host"
                        objInParam.ServerName = strModifyPropertyArray(I,1)
                    Case "subtype"
                        objInParam.SubType = strModifyPropertyArray(I,1)
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class ATMA_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strRecordData
    Public strFormat
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "ATMA"
        intParseArguments = 3
        strClass = "MicrosoftDNS_ATMAType"
        ReDim strModifyPropertyArray(2,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds an ATMA (ATM Host) Record to a Zone.", _
                       "  DnsResource /Add ATMA <zone> <recordname> <address> <format>", _
                       "   recordname    The name of the ATMA record" & vbCRLF & _
                       "   address       The ATM Address." & vbCRLF & _
                       "   format        The type of ATM Address:" & vbCRLF & _
                       "                   E164" & vbCRLF & _
                       "                   NSAP", _
                       "    DnsResource.vbs /Add ATMA Example.microsoft.com ATMA.MyDomain ????? E164" & vbCRLF & _
                       "    Creates an ATMA record for ATMA in the MyDomain.Example.microsoft.com domain.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes an ATMA (ATM Host) Record from a Zone.", _
                       "  DnsResource /Delete <zone> <recordname> <address> <format>", _
                       "   recordname    The name of the ATMA record" & vbCRLF & _
                       "   address       The ATM Address." & vbCRLF & _
                       "   format        The type of ATM Address:" & vbCRLF & _
                       "                   E164" & vbCRLF & _
                       "                   NSAP", _
                       "    DnsResource.vbs /Delete ATMA Example.microsoft.com ATMA.MyDomain ????? E164" & vbCRLF & _
                       "    Deletes the ATMA record for ATMA in the MyDomain.Example.microsoft.com domain.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies an ATMA (ATM Host) Record.", _
                       "  DnsResource /Modify ATMA <zone> <recordname> <address> <format> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   address" & vbCRLF & _
                       "                   format" & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   value         The new value for the listed property." & vbCRLF & _
                       "   recordname    The name of the ATMA record" & vbCRLF & _
                       "   address       The ATM Address." & vbCRLF & _
                       "   format        The type of ATM Address:" & vbCRLF & _
                       "                   E164" & vbCRLF & _
                       "                   NSAP", _
                       "    DnsResource.vbs /Modify ATMA Example.microsoft.com ATMA.MyDomain ????? E164 ttl 7400" & vbCRLF & _
                       "    Modifies the ATMA Record's TTL value to 7400.")
        ModifyHelp = 1
    End Function

    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        If blnContextHelp = True then
            Exit Function
        End If
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, strArgArray(1))
        strRecordData = strArgArray(2)
        Select Case LCase(strArgArray(3))
            Case "e164"
                strFormat = 1
            Case "nsap"
                strFormat = 2
            Case Else
                Wscript.Echo(strArgArray(3) & " is not a valid format.")
                Wscript.Quit
        End Select
        strText = strOwnername & " IN ATMA  " & strFormat & " " & strRecordData
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strRecordData = objDNS.ATMAddress
        strFormat = objDNS.Format
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Record Name : " & strOwnerName, objOutputFile)
        Select Case strFormat
            Case 0
                Call WriteLine("  Host Name   : E164", objOutputFile)
            Case 1
                Call WriteLine("  Host Name   : NSAP", objOutputFile)
        End Select
        Call WriteLine("  Address    : " & strRecordData, objOutputFile)
        Call WriteLine("  DNS Server : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone       : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain     : " & strDomainName, objOutputFile)
        Call WriteLine("  TTL        : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn

        strQuery = strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)
        If Not IsEmpty(strRecordData) then
             strQuery = strQuery & " ATMAddress=""" & strRecordData & """ and"
        End If
        If Not IsEmpty(strFormat) then
            strQuery = strQuery & " Format=""" & strFormat & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 2
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "address"
                        objInParam.ATMaddress = strModifyPropertyArray(I,1)
                    Case "format"
                        Select Case LCase(strModifyPropertyArray(I,1))
                            Case "e164"
                                objInParam.ATMaddress = 1
                            Case "nsap"
                                objInParam.ATMaddress = 2
                            Case else
                                Call WriteLine("Cannot update Format to type " & strModifyPropertyArray(I,1), objOutputFile)
                        End Select
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class HINFO_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strRecordData
    Public strOS
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "HINFO"
        intParseArguments = 3
        strClass = "MicrosoftDNS_HINFOType"
        ReDim strModifyPropertyArray(2,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds a HINFO (Host Information) Record to a Zone.", _
                       "  DnsResource /Add HINFO <zone> <recordname> <cpu> <os> <host>", _
                       "   cpu           The type of CPU the host uses." & vbCRLF & _
                       "   os            The operating system of the host.", _
                       "   DnsResource.vbs /Add HINFO Example.microsoft.com MyHost.MyDomain Intel-Pentium WIN32" & vbCRLF & _
                       "   Creates a HINFO record for MyHost.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes a HINFO (Host Information) Record to a Zone.", _
                       "  DnsResource /Delete HINFO <zone> <recordname> <cpu> <os> <host>", _
                       "   cpu           The type of CPU the host uses." & vbCRLF & _
                       "   os            The operating system of the host.", _
                       "   DnsResource.vbs /Delete HINFO Example.microsoft.com MyHost.MyDomain Intel-Pentium WIN32" & vbCRLF & _
                       "   Deletes the HINFO record for MyHost.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies a HINFO (Host Information) Record.", _
                       "  DnsResource /Modify HINFO <zone> <recordname> <cpu> <os> <host> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   cpu" & vbCRLF & _
                       "                   os" & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   value         The new value for the listed property." & vbCRLF & _
                       "   cpu           The type of CPU the host uses." & vbCRLF & _
                       "   os            The operating system of the host.", _
                       "   DnsResource.vbs /Modify HINFO Example.microsoft.com MyHost.MyDomain Intel-Pentium WIN32 ttl 7400" & vbCRLF & _
                       "   Modifies the HINFO's TTL value to 7400.")
        ModifyHelp = 1
    End Function

    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, strArgArray(1))
        strRecordData = strArgArray(2)
        strOS = strArgArray(3)
        strText = strOwnername & " IN HINFO """ & strOS & """ """ & strRecordData & """"
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strRecordData = objDNS.CPU
        strOS = objDns.OS
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Record Name : " & strOwnerName, objOutputFile)
        Call WriteLine("  CPU         : " & strRecordData, objOutputFile)
        Call WriteLine("  OS          : " & strOS, objOutputFile)
        Call WriteLine("  DNS Server : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone       : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain     : " & strDomainName, objOutputFile)
        Call WriteLine("  TTL        : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn
        
        strQuery = strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)
        If Not IsEmpty(strRecordData) then
            strQuery = strQuery & " CPU=""" & strRecordData & """ and"
        End If
        If Not IsEmpty(strOS) then
            strQuery = strQuery & " OSU=""" & strOS & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 1
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "cpu"
                        objInParam.CPU = strModifyPropertyArray(I,1)
                    Case "os"
                        objInParam.OS = strModifyPropertyArray(I,1)
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class ISDN_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strRecordData
    Public strSubaddress
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "ISDN"
        intParseArguments = 3
        strClass = "MicrosoftDNS_ISDNType"
        ReDim strModifyPropertyArray(1,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds a ISDN Record to a Zone.", _
                       "  DnsResource /Add ISDN <zone> <recordname> <number> <subaddress>", _
                       "   recordname    The name of the ISDN Record." & vbCRLF & _
                       "   number        The ISDN number." & vbCRLF & _
                       "   subaddresss   The ISDN sub address.", _
                       "   DnsResource.vbs /Add ISDN Example.microsoft.com MyISDN.MyDomain 150862028003217 004" & vbCRLF & _
                       "   Creates a ISDN record in Example.microsoft.com, in the MyDomain domain.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes a ISDN Record from a Zone.", _
                       "  DnsResource /Delete ISDN <zone> <recordname> <number> <subaddress>", _
                       "   recordname    The name of the ISDN Record." & vbCRLF & _
                       "   number        The ISDN number." & vbCRLF & _
                       "   subaddresss   The ISDN sub address.", _
                       "   DnsResource.vbs /Delete ISDN Example.microsoft.com MyISDN.MyDomain 150862028003217 004" & vbCRLF & _
                       "   Deletes the ISDN record in Example.microsoft.com, in the MyDomain domain.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies a ISDN Record.", _
                       "  DnsResource /Modify ISDN <zone> <recordname> <number> <subaddress> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   number" & vbCRLF & _
                       "                   subaddress" & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   value         The new value for the listed property." & vbCRLF & _
                       "   recordname    The name of the ISDN Record." & vbCRLF & _
                       "   number        The ISDN number." & vbCRLF & _
                       "   subaddresss   The ISDN sub address.", _
                       "   DnsResource.vbs /Modify ISDN Example.microsoft.com MyISDN.MyDomain 150862028003217004 number 150862032100144" & vbCRLF & _
                       "   Modifies a ISDN record's ISDN number.")
        ModifyHelp = 1
    End Function

    
    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, strArgArray(1))
        strRecordData = strArgArray(2)
        strSubAddress = strArgArray(3)
        strText = strOwnername & " IN ISDN """ & strSubAddress & """ """ & strRecordData & """"
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strRecordData = objDNS.ISDNNumber
        strSubAddress = objDNS.SubAddress
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Record Name : " & strOwnerName, objOutputFile)
        Call WriteLine("  ISDN Number : " & strRecordData, objOutputFile)
        Call WriteLine("  Sub Address : " & strSubAddress, objOutputFile)
        Call WriteLine("  DNS Server  : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone        : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain      : " & strDomainName, objOutputFile)
        Call WriteLine("  TTL         : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn
        
        strQuery = strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)
        If Not IsEmpty(strRecordData) then
            strQuery = strQuery & " ISDNNumber=""" & strRecordData & """ and"
        End If
        If Not IsEmpty(strSubAddress) then
            strQuery = strQuery & " SubAddress=""" & strSubAddress & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 1
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "number"
                        objInParam.ISDNNumber = strModifyPropertyArray(I,1)
                    Case "subaddress"
                        objInParam.SubAddress = strModifyPropertyArray(I,1)
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class MB_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strRecordData
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "MB"
        intParseArguments = 2
        strClass = "MicrosoftDNS_MBType"
        ReDim strModifyPropertyArray(1,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds a MB (Mail Box) Record to a Zone.", _
                       "  DnsResource /Add MB <zone> <mailbox> <host>", _
                       "   mailbox       A mailbox name." & vbCRLF & _
                       "   host          Name of the host.", _
                       "   DnsResource.vbs /Add MB Example.microsoft.com Mailbox.MyDomain MyHost.MyDomain" & vbCRLF & _
                       "   Creates a mailbox for MyHost called in the MyDomain.Example.microsoft.com domain.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes a MB (Mail Box) Record to a Zone.", _
                       "  DnsResource /Add MB <zone> <mailbox> <host>", _
                       "   mailbox       A mailbox name." & vbCRLF & _
                       "   host          Name of the host.", _
                       "   DnsResource.vbs /Delete MB Example.microsoft.com Mailbox.MyDomain MyHost.MyDomain" & vbCRLF & _
                       "   Deletes the mailbox for MyHost called in the MyDomain.Example.microsoft.com domain.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies a MB (Mail Box) Record.", _
                       "  DnsResource /Modify MB <zone> <mailbox> <host> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   Host" & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   value         The new value for the listed property." & vbCRLF & _
                       "   mailbox       A mailbox name." & vbCRLF & _
                       "   host          Name of the host.", _
                       "   DnsResource.vbs /Modify MB Example.microsoft.com Mailbox.MyDomain MyHost.MyDomain ttl 7400" & vbCRLF & _
                       "   Modifies the MB Record's TTL value to 7400.")
        ModifyHelp = 1
    End Function

    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, strArgArray(1))
        strRecordData = strFindFQDNOwnerName(strContainerName, strArgArray(0))
        strText = strOwnername & " IN MB " & strRecordData
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strRecordData = objDNS.RecordData
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Mailbox    : " & strOwnerName, objOutputFile)
        Call WriteLine("  Host Name  : " & strRecordData, objOutputFile)
        Call WriteLine("  DNS Server : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone       : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain     : " & strDomainName, objOutputFile)
        Call WriteLine("  TTL        : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn
        
        strQuery = strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)
        If Not IsEmpty(strRecordData) then
            strQuery = strQuery & " RecordData=""" & strRecordData & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 1
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "host"
                        objInParam.MBHost = strModifyPropertyArray(I,1)
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class MD_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strRecordData
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "MD"
        intParseArguments = 2
        strClass = "MicrosoftDNS_MDType"
        ReDim strModifyPropertyArray(1,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds a MD Record to a Zone.", _
                       "  DnsResource /Add MD <zone> <recordname> <host>", _
                       "   recordname    The name of the MD record." & vbCRLF & _
                       "   host          Name of the host.", _
                       "   DnsResource.vbs /Add MD Example.microsoft.com MDRecord.MyDomain MyHost.MyDomain" & vbCRLF & _
                       "   Creates a MD Record for MyHost in the MyDomain.Example.microsoft.com domain.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes a MD Record to a Zone.", _
                       "  DnsResource /Delete MD <zone> <recordname> <host>", _
                       "   recordname    The name of the MD record." & vbCRLF & _
                       "   host          Name of the host.", _
                       "   DnsResource.vbs /Delete MD Example.microsoft.com MDRecord.MyDomain MyHost.MyDomain" & vbCRLF & _
                       "   Deletes the MD Record for MyHost in the MyDomain.Example.microsoft.com domain.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies a MD Record.", _
                       "  DnsResource /Delete MD <zone> <recordname> <host>", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   Host" & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   value         The new value for the listed property." & vbCRLF & _
                       "   recordname    The name of the MD record." & vbCRLF & _
                       "   host          Name of the host.", _
                       "   DnsResource.vbs /Modify MD Example.microsoft.com MDRecord.MyDomain MyHost.MyDomain ttl 7400" & vbCRLF & _
                       "   Modifies the MD record's TTL value to 7400.")
        ModifyHelp = 1
    End Function

    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, strArgArray(1))
        strRecordData = strFindFQDNOwnerName(strContainerName, strArgArray(2))
        strText = strOwnername & " IN MD " & strRecordData
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strRecordData = objDNS.RecordData
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Record Name : " & strOwnerName, objOutputFile)
        Call WriteLine("  Host Name   : " & strRecordData, objOutputFile)
        Call WriteLine("  DNS Server  : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone        : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain      : " & strDomainName, objOutputFile)
        Call WriteLine("  TTL         : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn
        
        strQuery = strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)
        If Not IsEmpty(strRecordData) then
            strQuery = strQuery & " RecordData=""" & strRecordData & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 1
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "host"
                        objInParam.MDHost = strModifyPropertyArray(I,1)
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class MF_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strRecordData
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "MF"
        intParseArguments = 2
        strClass = "MicrosoftDNS_MFType"
        ReDim strModifyPropertyArray(1,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds a MF Record to a Zone.", _
                       "  DnsResource /Add MF <zone> <recordname> <host>", _
                       "   recordname    The name of the MF record." & vbCRLF & _
                       "   host          Name of the host.", _
                       "   DnsResource.vbs /Add MF Example.microsoft.com MFRecord.MyDomain MyHost.MyDomain" & vbCRLF & _
                       "   Creates a MF Record for MyHost in the MyDomain.Example.microsoft.com domain.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes a MF Record to a Zone.", _
                       "  DnsResource /Delete MF <zone> <recordname> <host>", _
                       "   recordname    The name of the MF record." & vbCRLF & _
                       "   host          Name of the host.", _
                       "   DnsResource.vbs /Delete MF Example.microsoft.com MFRecord.MyDomain MyHost.MyDomain" & vbCRLF & _
                       "   Deletes the MF Record for MyHost in the MyDomain.Example.microsoft.com domain.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies a MF Record.", _
                       "  DnsResource /Modify MF <zone> <recordname> <host> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   Host" & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   value         The new value for the listed property." & vbCRLF & _
                       "   recordname    The name of the MF record." & vbCRLF & _
                       "   host          Name of the host.", _
                       "   DnsResource.vbs /Modify MF Example.microsoft.com MFRecord.MyDomain MyHost.MyDomain ttl 7400" & vbCRLF & _
                       "   Modifies the MF record's TTL value to 7400.")
        ModifyHelp = 1
    End Function
    
    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, strArgArray(1))
        strRecordData = strFindFQDNOwnerName(strContainerName, strArgArray(2))
        strText = strOwnername & " IN MF " & strRecordData
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strRecordData = objDNS.RecordData
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Record Name : " & strOwnerName, objOutputFile)
        Call WriteLine("  Host Name   : " & strRecordData, objOutputFile)
        Call WriteLine("  DNS Server  : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone        : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain      : " & strDomainName, objOutputFile)
        Call WriteLine("  TTL         : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn
        
        strQuery = strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)
        If Not IsEmpty(strRecordData) then
            strQuery = strQuery & " RecordData=""" & strRecordData & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 1
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "host"
                        objInParam.MFHost = strModifyPropertyArray(I,1)
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class MG_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strRecordData
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "MG"
        intParseArguments = 2
        strClass = "MicrosoftDNS_MGType"
        ReDim strModifyPropertyArray(1,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds a MG (Mail Group) Record to a Zone.", _
                       "  DnsResource /Add MG <zone> <recordname> <mailbox>", _
                       "   recordname    The name of the MD record." & vbCRLF & _
                       "   mailbox       Name of the mailbox.", _
                       "   DnsResource.vbs /Add MG Example.microsoft.com MailBox.MyDomain MyHost.MyDomain" & vbCRLF & _
                       "   Creates a MG Record for MailBox in the MyDomain.Example.microsoft.com domain.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes a MG (Mail Group) Record to a Zone.", _
                       "  DnsResource /Delete MG <zone> <recordname> <mailbox>", _
                       "   recordname    The name of the MD record." & vbCRLF & _
                       "   mailbox       Name of the mailbox.", _
                       "   DnsResource.vbs /Delete MG Example.microsoft.com MailBox.MyDomain MyHost.MyDomain" & vbCRLF & _
                       "   Deletes the MG Record for MyHost in the MyDomain.Example.microsoft.com domain.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies a MG (Mail Group) Record.", _
                       "  DnsResource /Modify MG <zone> <recordname> <mailbox> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   mailbox" & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   value         The new value for the listed property." & vbCRLF & _
                       "   recordname    The name of the MD record." & vbCRLF & _
                       "   mailbox       Name of the mailbox.", _
                       "   DnsResource.vbs /Modify MG Example.microsoft.com MDRecord.MyDomain MyHost.MyDomain ttl 7400" & vbCRLF & _
                       "   Modifies the MG record's TTL value to 7400.")
        ModifyHelp = 1
    End Function
    
    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, strArgArray(1))
        strRecordData = strFindFQDNOwnerName(strContainerName, strArgArray(2))
        strText = strOwnername & " IN MG " & strRecordData
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strRecordData = objDNS.RecordData
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Record Name  : " & strOwnerName, objOutputFile)
        Call WriteLine("  Mailbox Name : " & strRecordData, objOutputFile)
        Call WriteLine("  DNS Server   : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone         : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain       : " & strDomainName, objOutputFile)
        Call WriteLine("  TTL          : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn
        
        strQuery = strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)
        If Not IsEmpty(strRecordData) then
            strQuery = strQuery & " RecordData=""" & strRecordData & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 1
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "mailbox"
                        objInParam.MGMailbox = strModifyPropertyArray(I,1)
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class MINFO_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strRecordData
    Public strErrorBox
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "MINFO"
        intParseArguments = 3
        strClass = "MicrosoftDNS_MINFOType"
        ReDim strModifyPropertyArray(2,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds a MINFO (Mailbox Information) Record to a Zone.", _
                       "  DnsResource /Add MINFO <zone> <recordname> <responsible> <error>", _
                       "   recordname    The name of the MD record." & vbCRLF & _
                       "   responsible   Name of the responsible mailbox." & vbCRLF & _
                       "   error         Name of the error mailbox.", _
                       "   DnsResource.vbs /Add MINFO Example.microsoft.com MyMailBox ResponsibleMailBox ErrorMailBox" & vbCRLF & _
                       "   Creates a MINFO Record for MyMailBox.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes a MINFO (Mailbox Information) Record from a Zone.", _
                       "  DnsResource /Delete MINFO <zone> <recordname> <responsible> <error>", _
                       "   recordname    The name of the MD record." & vbCRLF & _
                       "   responsible   Name of the responsible mailbox." & vbCRLF & _
                       "   error         Name of the error mailbox.", _
                       "   DnsResource.vbs /Delete MINFO Example.microsoft.com MyMailBox ResponsibleMailBox ErrorMailBox" & vbCRLF & _
                       "   Deletes the MINFO Record for MyMailBox.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies a MINFO (Mailbox Information) Record.", _
                       "  DnsResource /Modify MINFO <zone> <recordname> <responsible> <error> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   responsible" & vbCRLF & _
                       "                   error" & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   value         The new value for the listed property." & vbCRLF & _
                       "   recordname    The name of the MD record." & vbCRLF & _
                       "   responsible   Name of the responsible mailbox." & vbCRLF & _
                       "   error         Name of the error mailbox.", _
                       "    DnsResource.vbs /Modify MINFO Example.microsoft.com MyMailBox ResponsibleMailBox ErrorMailBox ttl 7400" & vbCRLF & _
                       "    Modifies the MINFO's record's TTL value to 7400.")
        ModifyHelp = 1
    End Function
    
    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, strArgArray(1))
        strRecordData = strFindFQDNOwnerName(strContainerName, strArgArray(2))
        strErrorBox = strFindFQDNOwnerName(strContainerName, strArgArray(3))
        strText = strOwnername & " IN MINFO " & strRecordData & " " & strErrorBox
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strRecordData = objDNS.ResponsibleMailbox
        strErrorBox = objDNS.ErrorMailbox
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Record Name         : " & strOwnerName, objOutputFile)
        Call WriteLine("  Responsible Mailbox : " & strRecordData, objOutputFile)
        Call WriteLine("  Error Mailbox       : " & strErrorBox, objOutputFile)
        Call WriteLine("  DNS Server          : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone                : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain              : " & strDomainName, objOutputFile)
        Call WriteLine("  TTL                 : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn
        
        strQuery = strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)
        If Not IsEmpty(strRecordData) then
            strQuery = strQuery & " ResponsibleMailbox=""" & strRecordData & """ and"
        End If
        If Not IsEmpty(strErrorBox) then
            strQuery = strQuery & " ErrorMailbox=""" & strErrorBox & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 1
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "responsible"
                        objInParam.ResponsibleMailbox = strModifyPropertyArray(I,1)
                    Case "error"
                        objInParam.ErrorMailbox = strModifyPropertyArray(I,1)
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class MR_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strRecordData
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "MR"
        intParseArguments = 2
        strClass = "MicrosoftDNS_MRType"
        ReDim strModifyPropertyArray(1,1)
    End Sub

    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds a MR (Rename Mailbox) Record to a Zone.", _
                       "  DnsResource /Add MR <zone> <mailbox> <replacement>", _
                       "   mailbox       The old mailbox name" & vbCRLF & _
                       "   replacement   The new mailbox name.", _
                       "   DnsResource.vbs /Add MR Example.microsoft.com OldBox.MyDomain NewBox.MyDomain" & vbCRLF & _
                       "   Creates a MR record to replace OldBox with NewBox.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes a MR (Rename Mailbox) Record from a Zone.", _
                       "  DnsResource /Delete MR <zone> <mailbox> <replacement>", _
                       "   mailbox       The old mailbox name" & vbCRLF & _
                       "   replacement   The new mailbox name.", _
                       "   DnsResource.vbs /Delete MR Example.microsoft.com OldBox.MyDomain NewBox.MyDomain" & vbCRLF & _
                       "   Deletes the MR record to replace OldBox with NewBox.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies a MR (Rename Mailbox) Record.", _
                       "  DnsResource /Modify MR <zone> <mailbox> <replacement> [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   NewBox" & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   value         The new value for the listed property." & vbCRLF & _
                       "   mailbox       The old mailbox name" & vbCRLF & _
                       "   replacement   The new mailbox name.", _
                       "   DnsResource.vbs /Modify MR Example.microsoft.com OldBox.MyDomain NewBox.MyDomain ttl 7400" & vbCRLF & _
                       "   Modifies the MS Record's TTL value to 7400.")
        ModifyHelp = 1
    End Function

    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, strArgArray(1))
        strRecordData = strFindFQDNOwnerName(strContainerName, strArgArray(2))
        strText = strOwnername & " IN MR " & strRecordData
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strRecordData = objDNS.RecordData
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Old Box    : " & strOwnerName, objOutputFile)
        Call WriteLine("  New Box    : " & strRecordData, objOutputFile)
        Call WriteLine("  DNS Server : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone       : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain     : " & strDomainName, objOutputFile)
        Call WriteLine("  TTL        : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn
        
        strQuery = strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)
        If Not IsEmpty(strRecordData) then
            strQuery = strQuery & " RecordData=""" & strRecordData & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 1
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "newbox"
                        objInParam.MRMailbox = strModifyPropertyArray(I,1)
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class RP_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strRecordData
    Public strTXTDomain
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "RP"
        intParseArguments = 3
        strClass = "MicrosoftDNS_RPtype"
        ReDim strModifyPropertyArray(2,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds a RP (Responsible Person) Record to a Zone.", _
                       "  DnsResource /Add RP <zone> <recordname> <mailbox> <textrecord>", _
                       "   recordname    The name of the RP Record." & vbCRLF & _
                       "   mailbox       The Mailbox of the responsible person." & vbCRLF & _
                       "   textrecord    An associated text record.", _
                       "   DnsResource.vbs /Add RP Example.microsoft.com MyDomain admim.example admim-info.example" & vbCRLF & _
                       "   Creates a MR Record for the MyDomain domain.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes a RP (Responsible Person) Record from a Zone.", _
                       "  DnsResource /Delete RP <zone> <recordname> <mailbox> <textrecord>", _
                       "   recordname    The name of the RP Record." & vbCRLF & _
                       "   mailbox       The Mailbox of the responsible person." & vbCRLF & _
                       "   textrecord    An associated text record.", _
                       "   DnsResource.vbs /Delete RP Example.microsoft.com MyDomain admim.example admim-info.example" & vbCRLF & _
                       "   Deletes the MR Record for the MyDomain domain.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies a RP (Responsible Person) Record.", _
                       "  DnsResource /Modify RP <zone> <recordname> <mailbox> <textrecord> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   mailbox" & vbCRLF & _
                       "                   textrecord" & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   value         The new value for the listed property." & vbCRLF & _
                       "   recordname    The name of the RP Record." & vbCRLF & _
                       "   mailbox       The Mailbox of the responsible person." & vbCRLF & _
                       "   textrecord    An associated text record.", _
                       "   DnsResource.vbs /Modify RP Example.microsoft.com MyDomain admim.example admim-info.example ttl 7400" & vbCRLF & _
                       "   Modifies the RP record's TTL value to 7400.")
        ModifyHelp = 1
    End Function

    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, strArgArray(1))
        strRecordData = strFindFQDNOwnerName(strContainerName, strArgArray(2))
        strTXTDomain = strFindFQDNOwnerName(strContainerName, strArgArray(3))
        strText = strOwnername & " IN RP " & strRecordData & " " & strTXTDomain
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strRecordData = objDNS.RPMailbox
        strTXTDomain = objDNS.TXTDomainName
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Record Name : " & strOwnerName, objOutputFile)
        Call WriteLine("  Mailbox     : " & strRecordData, objOutputFile)
        Call WriteLine("  Text Record : " & strTXTDomain, objOutputFile)
        Call WriteLine("  DNS Server  : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone        : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain      : " & strDomainName, objOutputFile)
        Call WriteLine("  TTL         : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn
        
        strQuery = strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)
        If Not IsEmpty(strRecordData) then
            strQuery = strQuery & " RPMAilbox=""" & strRecordData & """ and"
        End If
        If Not IsEmpty(strTXTDomain) then
            strQuery = strQuery & " TXTDomainName=""" & strTXTDomain & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 1
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "mailbox"
                        objInParam.RPMailbox = strModifyPropertyArray(I,1)
                    Case "textrecord"
                        objInParam.TXTDomainName = strModifyPropertyArray(I,1)
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class RT_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strRecordData
    Public strPreference
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "RT"
        intParseArguments = 3
        strClass = "MicrosoftDNS_RTType"
        ReDim strModifyPropertyArray(2,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds a RT (Route Through) Record to a Zone.", _
                       "  DnsResource /Add RT <zone> <recordname> <host> <preference>", _
                       "   recordname    The name of the RT Record." & vbCRLF & _
                       "   host          Name of the host." & vbCRLF & _
                       "   preference    The priority this record has over others.", _
                       "   DnsResource.vbs /Add RT Example.microsoft.com rtrecord lan-router 10" & vbCRLF & _
                       "   Creates a RT record.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes a RT (Route Through) Record from a Zone.", _
                       "  DnsResource /Delete RT <zone> <recordname> <host> <preference>", _
                       "   recordname    The name of the RT Record." & vbCRLF & _
                       "   host          Name of the host." & vbCRLF & _
                       "   preference    The priority this record has over others.", _
                       "   DnsResource.vbs /Delete RT Example.microsoft.com rtrecord lan-router 10" & vbCRLF & _
                       "   Deletes the RT Record.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies a RT (Route Through) Record.", _
                       "  DnsResource /Modify RT <zone> <recordname> <host> <preference> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   Host" & vbCRLF & _
                       "                   preference" & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   value         The new value for the listed property." & vbCRLF & _
                       "   recordname    The name of the RT Record." & vbCRLF & _
                       "   host          Name of the host." & vbCRLF & _
                       "   preference    The priority this record has over others.", _
                       "   DnsResource.vbs /Modify RT Example.microsoft.com rtrecord lan-router 10 ttl 7400" & vbCRLF & _
                       "   Modifies the RT record's TTL value to 7400.")
        ModifyHelp = 1
    End Function
    
    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, strArgArray(1))
        strRecordData = strFindFQDNOwnerName(strContainerName, strArgArray(2))
        strPreference = strArgArray(3)
        strText = strOwnername & " IN RT " & strPreference & " " & strRecordData
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strRecordData = objDNS.IntermediateHost
        strPreference = objDNS.Preference
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Record Name : " & strOwnerName, objOutputFile)
        Call WriteLine("  Host Name   : " & strRecordData, objOutputFile)
        Call WriteLine("  Preference  : " & strPreference, objOutputFile)
        Call WriteLine("  DNS Server  : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone        : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain      : " & strDomainName, objOutputFile)
        Call WriteLine("  TTL         : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn
        
        strQuery = strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)
        If Not IsEmpty(strRecordData) then
            strQuery = strQuery & " IntermediateHost=""" & strRecordData & """ and"
        End If
        If Not IsEmpty(strPreference) then
            strQuery = strQuery & " Preference=""" & strPreference & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 2
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "host"
                        objInParam.IntermediateHost = strModifyPropertyArray(I,1)
                    Case "preference"
                        objInParam.Preference = strModifyPropertyArray(I,1)
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class SRV_RecordData

    'Class Constructor
    Sub Class_Initialize
        Wscript.Echo("SRV Record is not currently supported.")
        Wscript.Quit
    End Sub
    
    
End Class

Class TXT_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strRecordData
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "TXT"
        intParseArguments = 2
        strClass = "MicrosoftDNS_TXTType"
        ReDim strModifyPropertyArray(1,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds a TXT (Text) Record to a Zone.", _
                       "  DnsResource /Add TXT <zone> <recordname> <text>", _
                       "   recordname    The name of the TXT record." & vbCRLF & _
                       "   text          Descriptive text.", _
                       "   DnsResource.vbs /Add TXT Example.microsoft.com MyText ""This is sample text""" & vbCRLF & _
                       "   Creates a TXT record in Example.microsoft.com with the name MyHost.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes a TXT (Text) Record to a Zone.", _
                       "  DnsResource /Delete TXT <zone> <recordname> <text>", _
                       "   recordname    The name of the TXT record." & vbCRLF & _
                       "   text          Descriptive text.", _
                       "   DnsResource.vbs /Delete TXT Example.microsoft.com MyText ""This is sample text""" & vbCRLF & _
                       "   Deletes the TXT record in Example.microsoft.com with the name MyHost.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies a TXT (Text) Record to a Zone.", _
                       "  DnsResource /Modify TXT <zone> <recordname> <text> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   text" & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   value         The new value for the listed property." & vbCRLF & _
                       "   recordname    The name of the TXT record." & vbCRLF & _
                       "   text          Descriptive text.", _
                       "   DnsResource.vbs /Modify TXT Example.microsoft.com MyText ""This is sample text"" text ""This is new text""" & vbCRLF & _
                       "   Modifies a TXT record's text.")
        ModifyHelp = 1
    End Function
    
    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, strArgArray(1))
        strRecordData = strArgArray(2)
        strText = strOwnername & " IN TXT " & """" & strRecordData & """"
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strRecordData = objDNS.RecordData
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Record Name : " & strOwnerName, objOutputFile)
        Call WriteLine("  Text        : " & strRecordData, objOutputFile)
        Call WriteLine("  DNS Server  : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone        : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain      : " & strDomainName, objOutputFile)
        Call WriteLine("  TTL         : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn
        
        strQuery = strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)
        If Not IsEmpty(strRecordData) then
            strQuery = strQuery & " RecordData=""" & "\""" & strRecordData & "\""" & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 1
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "text"
                        objInParam.DescriptiveText = "" & strModifyPropertyArray(I,1) & ""
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class WINSR_RecordData

    'Class Constructor
    Sub Class_Initialize
        Wscript.Echo("WINSR Record is not currently supported.")
        Wscript.Quit
    End Sub
    
    
End Class

Class WINS_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strCacheTimeout
    Public strLookupTimeout
    Public strMappingFlag
    Public strWinsServers
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "WINS"
        intParseArguments = 5
        strClass = "MicrosoftDNS_WINSType"
        ReDim strModifyPropertyArray(5,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds a WINS Record to a Zone.", _
                       "  DnsResource /Add WINS <zone> <recordname> <servers> <cachetimeout> <lookuptimeout> <replicate>", _
                       "   recordname    The name of the WINS record." & vbCRLF & _
                       "   servers       The IP Address(es) for the WINS Server(s)." & vbCRLF & _
                       "   lookuptimeout The time in seconds to cache a Wins server's response." & vbCRLF & _
                       "   cachetimeout  The time in seconds to wait for a Wins server's response." & vbCRLF & _
                       "   replicate     Whether to include WINS records in Zone replication:" & vbCRLF & _
                       "                   True" & vbCRLF & _
                       "                   False", _
                       "   DnsResource.vbs /Add WINS Example.microsoft.com @ ""192.78.101.4 192.78.101.5"" 72000 1200 false" & vbCRLF & _
                       "   Creates a WINS record for Example.microsoft.com with two WINS servers.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes a WINS Record from a Zone.", _
                       "  DnsResource /Delete WINS <zone> <recordname> <servers> <cachetimeout> <lookuptimeout> <replicate>", _
                       "   recordname    The name of the WINS record." & vbCRLF & _
                       "   servers       The IP Address(es) for the WINS Server(s)." & vbCRLF & _
                       "   lookuptimeout The time in seconds to cache a Wins server's response." & vbCRLF & _
                       "   cachetimeout  The time in seconds to wait for a Wins server's response." & vbCRLF & _
                       "   replicate     Whether to include WINS records in Zone replication:" & vbCRLF & _
                       "                   True" & vbCRLF & _
                       "                   False", _
                       "   DnsResource.vbs /Delete WINS Example.microsoft.com @ ""192.78.101.4 192.78.101.5"" 72000 1200 false" & vbCRLF & _
                       "   Deletes the WINS record for Example.microsoft.com with two WINS servers.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies a WINS Record.", _
                       "  DnsResource /Modify WINS <zone> <recordname> <servers> <cachetimeout> <lookuptimeout> <replicate> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   servers" & vbCRLF & _
                       "                   cachetimeout" & vbCRLF & _
                       "                   lookuptimeout" & vbCRLF & _
                       "                   replicate" & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   recordname    The name of the WINS record." & vbCRLF & _
                       "   recordname    The name of the WINS record." & vbCRLF & _
                       "   servers       The IP Address(es) for the WINS Server(s)." & vbCRLF & _
                       "   lookuptimeout The time in seconds to cache a Wins server's response." & vbCRLF & _
                       "   cachetimeout  The time in seconds to wait for a Wins server's response." & vbCRLF & _
                       "   replicate     Whether to include WINS records in Zone replication:" & vbCRLF & _
                       "                   True" & vbCRLF & _
                       "                   False", _
                       "   DnsResource.vbs /Modify WINS Example.microsoft.com @ ""192.78.101.4 192.78.101.5 72000 1200 false servers ""192.78.101.4 192.78.101.5""" & vbCRLF & _
                       "   Changes the order of WINS Servers in a WINS Record.")
        ModifyHelp = 1
    End Function

    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        Stop
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, strArgArray(1))
        strWinsServers = strArgArray(2)
        strCacheTimeout = strArgArray(3)
        strLookupTimeout = strArgArray(4)
        Select Case LCase(strArgArray(5))
            Case "true"
                strMappingFlag = 1
            Case "false"
                strMappingFlag = 0
            Case Else
                Wscript.Echo(strArgArray(5) & " is not a valid value for replicate")
        End Select

        strText = strOwnername & " IN WINS " & strMappingFlag & " " & strLookupTimeout & " " & strCacheTimeout & " " & strWinsServers
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strWinsServers = objDNS.WinsServers
        strCacheTimeout = objDNS.CacheTimeout
        strLookupTimeout = objDNS.LookupTimeout
        strMappingFlag = objDNS.MappingFlag
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Record Name    : " & strOwnerName, objOutputFile)
        Call WriteLine("  Wins Servers   : " & strWinsServers, objOutputFile)
        Call WriteLine("  Cache Timeout  : " & strCacheTimeout, objOutputFile)
        Call WriteLine("  Lookup Timeput : " & strLookupTimeout, objOutputFile)
        Select Case strMappingFlag
            Case 0
                Call WriteLine("  Replicate      : False", objOutputFile)
            Case 1
                Call WriteLine("  Replicate      : True", objOutputFile)
        End Select
        Call WriteLine("  DNS Server     : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone           : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain         : " & strDomainName, objOutputFile)
        Call WriteLine("  TTL            : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn
        
        strQuery = strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)
        If Not IsEmpty(strWinsServers) then
            strQuery = strQuery & " WinsServers=""" & strWinsServers & """ and"
        End If
        If Not IsEmpty(strCacheTimeout) then
            strQuery = strQuery & " CacheTimeout=""" & strCacheTimeout & """ and"
        End If
        If Not IsEmpty(strLookupTimeout) then
            strQuery = strQuery & " LookupTimeout=""" & strLookupTimeout & """ and"
        End If
        If Not IsEmpty(strMappingFlag) then
            strQuery = strQuery & " MappingFlag=""" & strMappingFlag & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 5
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "servers"
                        objInParam.WinsServers = strModifyPropertyArray(I,1)
                    Case "cachetimeout"
                        objInParam.CacheTimeout = strModifyPropertyArray(I,1)
                    Case "lookuptimeout"
                        objInParam.LookupTimeout = strModifyPropertyArray(I,1)
                    Case "replicate"
                        Select Case LCase(strModifyPropertyArray(I,1))
                            Case "true"
                                objInParam.MappingFlag = 1
                            Case "false"
                                objInParam.MappingFlag = 0
                            Case Else
                                Modify = True
                                Wscript.Echo(strModifyPropertyArray(I,1) & " is not a valid value for Replicate.")
                                Exit Function
                        End Select
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class WKS_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strIP
    Public strProtocol
    Public strServices
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "WKS"
        intParseArguments = 4
        strClass = "MicrosoftDNS_WKSType"
        ReDim strModifyPropertyArray(4,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds a WKS (Well Known Services) Record to a Zone.", _
                       "  DnsResource /Add WKS <zone> <recordname> <ip> <protocol> <services>", _
                       "   recordname    The name of the WKS Record." & vbCRLF & _
                       "   ip            The IP Address for the service." & vbCRLF & _
                       "   protocol      The IP Protocol the service uses:" & vbCRLF & _
                       "                   tcp" & vbCRLF & _
                       "                   udp" & vbCRLF & _
                       "   services      The name of the service(s).", _
                       "   DnsResource.vbs /Add WKS Example.microsoft.com MyWKS 192.78.101.4 tcp ""telnet ftp""" & vbCRLF & _
                       "   Creates a WKS record in Example.microsoft.com.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes a WKS (Well Known Services) Record from a Zone.", _
                       "  DnsResource /Delete WKS <zone> <recordname> <ip> <protocol> <services>", _
                       "   recordname    The name of the WKS Record." & vbCRLF & _
                       "   ip            The IP Address for the service." & vbCRLF & _
                       "   protocol      The IP Protocol the service uses:" & vbCRLF & _
                       "                   tcp" & vbCRLF & _
                       "                   udp" & vbCRLF & _
                       "   services      The name of the service(s).", _
                       "   DnsResource.vbs /Delete WKS Example.microsoft.com MyWKS 192.78.101.4 tcp ""telnet ftp""" & vbCRLF & _
                       "   Deletes the WKS record in Example.microsoft.com.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies a WKS (Well Known Services) Record.", _
                       "  DnsResource /Modify WKS <zone> <recordname> <ip> <protocol> <services> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   ip" & vbCRLF & _
                       "                   protocol" & vbCRLF & _
                       "                   services" & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   value         The new value for the listed property." & vbCRLF & _
                       "   recordname    The name of the WKS Record." & vbCRLF & _
                       "   ip            The IP Address for the service." & vbCRLF & _
                       "   protocol      The IP Protocol the service uses:" & vbCRLF & _
                       "                   tcp" & vbCRLF & _
                       "                   udp" & vbCRLF & _
                       "   services      The name of the service(s).", _
                       "   DnsResource.vbs /Modify WKS Example.microsoft.com MyWKS 192.78.101.4 tcp ""telnet ftp"" services ""telnet""" & vbCRLF & _
                       "   Removes ftp from the list of services.")
        ModifyHelp = 1
    End Function
    
    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, strArgArray(1))
        strIP = strArgArray(2)
        strProtocol = strArgArray(3)
        strServices = strArgArray(4)
        strText = strOwnername & " IN WKS " & strProtocol & " " & strIP & " """ & strServices & """"
    End Function
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strIP = objDNS.InternetAddress
        strProtocol = objDNS.IPProtocol
        strServices = objDNS.Services
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Record Name : " & strOwnerName, objOutputFile)
        Call WriteLine("  IP          : " & strIP, objOutputFile)
        Call WriteLine("  Protocol    : " & strProtocol, objOutputFile)
        Call WriteLine("  Services    : " & strServices, objOutputFile)
        Call WriteLine("  DNS Server : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone       : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain     : " & strDomainName, objOutputFile)
        Call WriteLine("  TTL        : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn
        
        strQuery = strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)
        If Not IsEmpty(strIP) then
            strQuery = strQuery & " InternetAddress=""" & strIP & """ and"
        End If
        If Not IsEmpty(strProtocol) then
            strQuery = strQuery & " IPProtocol=""" & strProtocol & """ and"
        End If
        If Not IsEmpty(strServices) then
            strQuery = strQuery & " Services=""" & "\""" & strServices & "\""" & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 3
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "ip"
                        objInParam.InternetAddress = strModifyPropertyArray(I,1)
                    Case "protocol"
                        objInParam.IPProtocol = strModifyPropertyArray(I,1)
                    Case "service"
                        objInParam.Services = "\""" & strModifyPropertyArray(I,1) & "\""" 
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

Class X25_RecordData

    Public strContainerName
    Public strDnsServerName
    Public strDomainName
    Public strOwnerName
    Public strTTL
    Public strRecordData
    Public strText
    Public strRelPath
    Public strClassType
    Public strClass
    Public intParseArguments
    Public strModifyPropertyArray()

    'Class Constructor
    Sub Class_Initialize
        strClassType = "X25"
        intParseArguments = 2
        strClass = "MicrosoftDNS_X25Type"
        ReDim strModifyPropertyArray(1,1)
    End Sub
    
    'Help for this Resource Record.
    Public Function AddHelp
        Call ClassHelp("Adds a X25 (X.25) Record to a Zone.", _
                       "  DnsResource /Add X25 <zone> <recordname> <address>", _
                       "   recordname    The name of the X.25 record" & vbCRLF & _
                       "   address       The X.121 PSDN address.", _
                       "   DnsResource.vbs /Add X25 Example.microsoft.com MyX25 52204455506" & vbCRLF & _
                       "   Creates a X.25 record in Example.microsoft.com.")
        AddHelp = 1
    End Function
    Public Function DeleteHelp
        Call ClassHelp("Deletes a X25 (X.25) Record to a Zone.", _
                       "  DnsResource /Delete X25 <zone> <recordname> <address>", _
                       "   recordname    The name of the X.25 record" & vbCRLF & _
                       "   address       The X.121 PSDN address.", _
                       "   DnsResource.vbs /Delete X25 Example.microsoft.com MyX25 52204455506" & vbCRLF & _
                       "   Deletes the X.25 record in Example.microsoft.com.")
        DeleteHelp = 1
    End Function
    Public Function ModifyHelp
        Call ClassHelp("Modifies a X25 (X.25) Record.", _
                       "  DnsResource /Modify X25 <zone> <recordname> <address> [<property> <value>] [...]", _
                       "   property      Valid Properties are:" & vbCRLF & _
                       "                   Address" & vbCRLF & _
                       "                   TTL" & vbCRLF & _
                       "   value         The new value for the listed property." & vbCRLF & _
                       "   recordname    The name of the X.25 record" & vbCRLF & _
                       "   address       The X.121 PSDN address.", _
                       "   DnsResource.vbs /Modify X25 Example.microsoft.com MyX25 52204455506 address 52204455506" & vbCRLF & _
                       "   Modifies a X25 record's address to 52204455506.")
        ModifyHelp = 1
    End Function

    'Fill in Class properties from Parse Data
    Public Function PopulateClass(strArgArray)
        strContainerName = strArgArray(0)
        strOwnerName = strFindFQDNOwnerName(strContainerName, strArgArray(1))
        strRecordData = strArgArray(2)
        strText = strOwnername & " IN X25 """ & strRecordData & """"
    End Function
    
    'Update Class Properties from a object
    Public Function UpdateProperties(objDNS)
        'On Error Resume Next
        strContainerName = objDNS.ContainerName
        strDNSServerName = objDNS.DNSServerName
        strDomainName = objDNS.DomainName
        strOwnername = objDNS.OwnerName
        strTTL = objDNS.TTL
        strRecordData = objDNS.RecordData
        strText = objDns.TextRepresentation
        strRelPath = objDns.Path_.Relpath
        If blnErrorOccurred("Error while updating properties.") then
            UpdateProperties = 1
        Else
            UpdateProperties = 0
        End If
    End Function
    
    'Display Class Properties to screen
    Public Function DisplayProperties
        Call WriteLine("  Record Name : " & strOwnerName, objOutputFile)
        Call WriteLine("  Address     : " & strRecordData, objOutputFile)
        Call WriteLine("  DNS Server  : " & strDNSServerName, objOutputFile)
        Call WriteLine("  Zone        : " & strContainerName, objOutputFile)
        Call WriteLine("  Domain      : " & strDomainName, objOutputFile)
        Call WriteLine("  TTL         : " & strTTL, objOutputFile)
        DisplayProperties = 0
    End Function

    'Find the Class Instance based on current Class property Data
    Public Function GetInstanceFromQuery
        'On Error Resume Next
        Dim strQuery
        Dim objQuery, objInst
        Dim intReturn
        
        strQuery = strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)
        If Not IsEmpty(strRecordData) then
            strQuery = strQuery & " RecordData=""" & "\""" & strRecordData  & "\""" & """ and"
        End If
        strQuery = Left(strQuery,Len(strQuery)-4)
        Set objQuery = objService.ExecQuery(strQuery)
        If objQuery.Count <> 1 then
            GetInstanceFromQuery = objQuery.Count
        Else
            GetInstanceFromQuery = 1
            For Each objInst in objQuery
                intReturn = UpdateProperties(objInst)
            Next
        End If
        
        If blnErrorOccurred("Error while finding Resource Record") Then
            Wscript.Quit
        End If
    End Function

    'Modify the Record
    Public Function Modify
        'On Error Resume Next
        Dim objDns, objMethod, objInParam, objOutParam
        Dim intReturn
        Set objDNS = objService.Get(strRelPath)
        Set objMethod = objDNS.Methods_("Modify")
        Set objInParam = objMethod.inParameters.SpawnInstance_()
        
        For I = 0 to 1
            If Not IsEmpty(strModifyPropertyArray(I,0)) Then
                Select Case LCase(strModifyPropertyArray(I,0))
                    Case "ttl"
                        objInParam.TTL = strModifyPropertyArray(I,1)
                    Case "address"
                        objInParam.PSDNAddress = """" & strModifyPropertyArray(I,1) & """"
                    Case else
                        Modify = True
                        Call WriteLine(strModifyPropertyArray(I,0) & " is not a valid property.", objOutputFile)
                        Exit Function
                End Select
            End If
        Next

        Set objOutParam = objDNS.ExecMethod_("Modify", ObjInParam)
  
        Set objDNS = objService.Get(objOutParam.RR)
        If UpdateProperties(objDNS) = 1 then
            Modify = 1
            Exit Function
        End If
        intReturn = DisplayProperties

        If blnErrorOccurred("Modifing Resource Record") then
            Modify = 1
        Else
            Modify = 0
        End If
    End Function
    
End Class

'********************************************************************
'* Main Program
'********************************************************************
```



## List Resource Records

This code example shows tasks associated with listing resource records.


```VB
Private Sub DnsList(strServer        , _
                    strUserName      , _
                    strPassword      , _
                    strOutputFile    , _
                    strDomain        , _
                    cResource        , _
                    blnContextHelp     )

    'On Error Resume Next
    Dim strTemp
    Dim objFileSystem, objDns, objInst, objDomain
    Dim intReturn

    If blnContextHelp then
        Wscript.Echo ""
        Wscript.Echo "Lists Resource Record in a domain."
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo "  DnsResource /List <recordtype> <domain>"
        Wscript.Echo "    [/S <server>] [/U <username>] [/W <password>]"
        Wscript.Echo "    [/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIFIERS:"
        Wscript.Echo "   recordtype    A resource record type.  Valid Types are:"
        Wscript.Echo "                   A, CNAME, MX, PTR, NS, AAAA, AFSDB, ATMA, HINFO, ISDN"
        Wscript.Echo "                   MB, MD, MF, MG, MINFO, MR, RP, RT, SRV, TXT, WINSR, WINS"
        Wscript.Echo "                   WKS, X25, SOA"
        Wscript.Echo "   domain        The domain in which to enumerate records."
        Wscript.Echo "   server        The name of the DNS Server."
        Wscript.Echo "   username      The current user's name."
        Wscript.Echo "   password      Password of the current user."
        Wscript.Echo "   outputfile    The output file name."
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE:"
        Wscript.Echo ""
        Wscript.Echo "    DnsResource.vbs /List MX MyDomain.Example.microsoft.com"
        Wscript.Echo "    Lists all MX records in the MyDomain domain."
        Exit Sub
    End If
     
    'Open a text file for output If the file is requested
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

    If IsEmpty(cResource) then
        Call WriteLine("All Resource Records in " & strDomain & ":", objOutputFile)
        Set objDNS = objService.ExecQuery("Select * from MicrosoftDNS_ResourceRecord where DomainName=""" & strDomain & """",,48)
        For Each objInst in objDNS    
            Call WriteLine("  " & strFindType(objInst.TextRepresentation) & " Record:", objOutputFile)
            If GetClass(strFindType(objInst.TextRepresentation), cResource) then
                Call WriteLine("Error Finding Record Class", objOutputFile)
                Wscript.Quit
            End If
            intReturn = cResource.UpdateProperties(objInst)
            intReturn = cResource.DisplayProperties
            Call WriteLine("", objOutputFile)
            'Call WriteLine("  " & objInst.TextRepresentation, objOutputFile)
        Next
    Else
        Call WriteLine("All " & cResource.strClassType & " Records in " & strDomain & ":", objOutputFile)
        Set objDNS = objService.ExecQuery("Select * from " & cResource.strClass & " where DomainName=""" & strDomain & """",,48)
        For Each objInst in objDNS
            intReturn = cResource.UpdateProperties(objInst)
            intReturn = cResource.DisplayProperties
            Call WriteLine("", objOutputFile)
        Next
    End If

    Set objDNS = objService.ExecQuery("Select * from MicrosoftDNS_Zone where name=""" & strDomain & """")
    If objDNS.Count = 0 then
        Set objDNS = objService.ExecQuery("Select * from MicrosoftDNS_Domain where name=""" & strDomain & """")
        If objDNS.Count = 1 then
            For Each objInst in objDNS
                strTemp = objInst.Path_.RelPath
            Next
        End If
    Else
        For Each objInst in objDNS
            strTemp = objInst.Path_.RelPath
        Next
    End If
    
    Set objDNS = objService.ExecQuery("Select * from MicrosoftDNS_DomainDomainContainment where GroupComponent=""" & strConvertQuotes(strTemp) & """")
    If objDNS.count <> 0 then
        Call WriteLine("", objOutputFile)
        Call WriteLine("Domains:", objOutputFile)
        For Each objInst in objDNS
            Set objDomain = objService.Get(objInst.PartComponent)
            Call WriteLine("  " & objDomain.Name, objOutputfile)
        Next
    End If        
    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " & strOutputFile & ".")
    End If


End Sub
```



## Add a Resource Record

This code example shows tasks associated with adding resource records.


```VB
Private Sub DnsCreate(strServer        , _
                      strUserName      , _
                      strPassword      , _
                      strOutputFile    , _
                      cResource        , _
                      blnContextHelp     )

    'On Error Resume Next
    Dim objFileSystem, objDns, objServer,  Inst, intReturn, objMethod, objInParam, objOutParam

    If blnContextHelp then
        If IsEmpty(cResource) then
            Wscript.Echo ""
            Wscript.Echo "Adds a Resource Record to a Zone."
            Wscript.Echo ""
            Wscript.Echo "SYNTAX:"
            Wscript.Echo "  DnsResource /Add <recordtype> <zone> <properties>"
            Call CommonHelp(False)
            Wscript.Echo "    DnsResource.vbs /Add A Example.microsoft.com MyHost.MyDomain.Example.microsoft.com 192.78.101.4"
            Wscript.Echo "    Creates an A record in Example.microsoft.com, in the MyDomain domain, with the name MyHost."
            Wscript.Echo ""
            Wscript.Echo "NOTES:"
            Wscript.Echo ""
            Wscript.Echo "    To see help for a specific type use the following syntax:"
            Wscript.Echo "    DnsResource / Add <recordtype> /?"
        Else
            intReturn = cResource.AddHelp
        End If
        Exit Sub
    End If
    
    'Open a text file for output If the file is requested
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

    Set objDNS = objService.Get("MicrosoftDNS_ResourceRecord")
    Set objServer = objService.Get("MicrosoftDNS_Server.Name="".""")
    Set objMethod = objDNS.Methods_("CreateInstanceFromTextRepresentation")
    Set ObjInParam = objMethod.inParameters.SpawnInstance_()
        
    ObjInParam.TextRepresentation = cResource.strText
    ObjInParam.DnsServerName = objServer.Name
    ObjInParam.ContainerName = cResource.strContainerName
    Call WriteLine("Creating Resource Record...", objOutputFile)
    Set objOutParam = objDNS.ExecMethod_("CreateInstanceFromTextRepresentation", ObjInParam)
    Set objDNS = objService.Get(objOutParam.RR)
    If cResource.UpdateProperties(objDNS) = 1 then
        Exit Sub
    End If
    intReturn = cResource.DisplayProperties

    If blnErrorOccurred("Creating object.") then
        Exit Sub
    Else            
        Call WriteLine("Operation Successful!", objOutputFile)
    End If
   
    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " & strOutputFile & ".")
    End If


End Sub
```



## Delete a Resource Record

This code example shows tasks associated with deleting resource records.


```VB
Private Sub DnsDelete(strServer        , _
                      strUserName      , _
                      strPassword      , _
                      strOutputFile    , _
                      cResource        , _
                      blnContextHelp     )

    'On Error Resume Next
    Dim objFileSystem, objDns, objDnsServer, Inst, intReturn

    If blnContextHelp then
        If IsEmpty(cResource) then
            Wscript.Echo ""
            Wscript.Echo "Deletes a Resource Record from a Zone."
            Wscript.Echo ""
            Wscript.Echo "SYNTAX:"
            Wscript.Echo "  DnsResource /Delete <recordtype> <zone> <properties>"
            Call CommonHelp(False)
            Wscript.Echo "    DnsResource.vbs /Delete A Example.microsoft.com MyHost.MyDomain.Example.microsoft.com 192.78.101.4"
            Wscript.Echo "    Deletes the A record in Example.microsoft.com, in the MyDomain domain, with the name MyHost."
            Wscript.Echo ""
            Wscript.Echo "NOTES:"
            Wscript.Echo ""
            Wscript.Echo "    To see help for a specific type use the following syntax:"
            Wscript.Echo "    DnsResource / Delete <recordtype> /?"
        Else
            intReturn = cResource.DeleteHelp
        End If
        Exit Sub
    End If
    
    'Open a text file for output If the file is requested
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

    intReturn =  cResource.GetInstanceFromQuery
    If intReturn <> 1 then
        Call WriteLine("Could not Delete because the information you supplied returned " & intReturn & " results.", objOutputFile)
    Else
        Call WriteLine("Deleting Resource Record...", objOutputFile)
        Call WriteLine("  " & cResource.strClassType & " Record", objOutputFile)
        intReturn = cResource.DisplayProperties
        Set objDNS = objService.Get(cResource.strRelPath)
        objDNS.Delete_
        If blnErrorOccurred("Deleting object.") then
            Exit Sub
        Else            
            Call WriteLine("Operation Successful!", objOutputFile)
        End If
    End If
    
    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " & strOutputFile & ".")
    End If


End Sub
```



## Modify a Resource Record

This code example shows tasks associated with changing resource records.


```VB
Private Sub DnsModify(strServer        , _
                      strUserName      , _
                      strPassword      , _
                      strOutputFile    , _
                      cResource        , _
                      blnContextHelp     )

    'On Error Resume Next
    Dim objFileSystem, objDns, objDnsServer, Inst, intReturn
    If blnContextHelp then
        If IsEmpty(cResource) then
            Wscript.Echo ""
            Wscript.Echo "ModIfies a Resource Record."
            Wscript.Echo ""
            Wscript.Echo "SYNTAX:"
            Wscript.Echo "  DnsResource /Modify <recordtype> <zone> <properties> [<property> <value>] [...]"
            Call CommonHelp(True)
            Wscript.Echo "    DnsResource.vbs /Modify A Example.microsoft.com MyHost.MyDomain.Example.microsoft.com 192.78.101.4 IPAddress 192.78.101.5 TTL 7200"
            Wscript.Echo "    ModIfies an A record's ip address and TTL."
            Wscript.Echo ""
            Wscript.Echo "NOTES:"
            Wscript.Echo ""
            Wscript.Echo "    To see help for a specific type use the following syntax:"
            Wscript.Echo "    DnsResource / Modify <recordtype> /?"
        Else
            intReturn = cResource.ModifyHelp
        End If
        Exit Sub
    End If
    
    'Open a text file for output If the file is requested
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
    intReturn = cResource.GetInstanceFromQuery
    If intReturn <> 1 then
        Call WriteLine("Could not Modify because the information you supplied returned " & intReturn & " results.", objOutputFile)
    Else
        Call WriteLine("Modifing Resource Record...", objOutputFile)
        intReturn = cResource.Modify
    End If
    
    If IsObject(objOutputFile) Then
        objOutputFile.Close
        Call Wscript.Echo ("Results are saved in file " & strOutputFile & ".")
    End If


End Sub

Function strFindType(strText)
    Dim intCounter
    Dim strTemp
    strTemp = ""
    intCounter = 0
    I = 0
    Do Until I > len(strText)
        I = I + 1
        If Mid(strText,I,1) = " " then
            intCounter = intCounter + 1
            If intCounter = 2 then Exit Do
        End If
    Loop
    Do Until I > len(strText)
        I = I + 1
        If Mid(strText,I,1) = " " then
            Exit Do
        Else
            strTemp = strTemp & Mid(strText,I,1)
        End If
    Loop
    strFindType = Trim(strTemp)
End Function

Function strConvertQuotes(strTemp)
    strConvertQuotes = ""
    For I = 1 to Len(strTemp)
        If Mid(strTemp, I, 1) = """" then
            strConvertQuotes = strConvertQuotes & "'"
        Else
            strConvertQuotes = strConvertQuotes & Mid(strTemp, I, 1)
        End If
    Next

End Function

Function strStandardQuery(strClass, strContainerName, strDnsServerName, strDomainName, strOwnerName, strTTL)
    Dim strQuery
    strQuery = "Select * From " & strClass & " Where"
    If Not IsEmpty(strContainerName) then
        strQuery = strQuery & " ContainerName=""" & strContainerName & """ and"
    End If
    If Not IsEmpty(strDnsServerName) then
        strQuery = strQuery & " DnsServerName=""" & strDnsServerName & """ and"
    End If
    If Not IsEmpty(strDomainName) then
        strQuery = strQuery & " DomainName=""" & strDomainName & """ and"
    End If
    If Not IsEmpty(strOwnerName) then
        strQuery = strQuery & " OwnerName=""" & strOwnerName & """ and"
    End If
    If Not IsEmpty(strTTL) then
        strQuery = strQuery & " TTL=" & strTTL & " and"
    End If
    strStandardQuery = strQuery
End Function

Sub CommonHelp(blnSOA)
    Wscript.Echo "    [/S <server>] [/U <username>] [/W <password>]"
    Wscript.Echo "    [/O <outputfile>]"
    Wscript.Echo ""
    Wscript.Echo "PARAMETER SPECIFIERS:"
    Wscript.Echo "   recordtype    A resource record type.  Valid Types are:"
    Wscript.Echo "                   A, CNAME, MX, PTR, NS, AAAA, AFSDB, ATMA, HINFO, ISDN"
    Wscript.Echo "                   MB, MD, MF, MG, MINFO, MR, RP, RT, SRV, TXT, WINSR, WINS"
    If blnSOA = True then
        Wscript.Echo "                   WKS, X25, SOA"
    Else
        Wscript.Echo "                   WKS, X25"
    End If
    Wscript.Echo "   zone          The Zone in which to create the record."
    Wscript.Echo "   properties    The properties for the resource record."
    Wscript.Echo "   value         The new value for the listed property."
    Wscript.Echo "   server        The name of the DNS Server."
    Wscript.Echo "   username      The current user's name."
    Wscript.Echo "   password      Password of the current user."
    Wscript.Echo "   outputfile    The output file name."
    Wscript.Echo ""
    Wscript.Echo "EXAMPLE:"
    Wscript.Echo ""
End Sub

Sub ClassHelp(strDescription, strSyntax, strParameter, strExample)
        Wscript.Echo ""
        Wscript.Echo strDescription
        Wscript.Echo ""
        Wscript.Echo "SYNTAX:"
        Wscript.Echo strSyntax
        Wscript.Echo "    [/S <server>] [/U <username>] [/W <password>]"
        Wscript.Echo "    [/O <outputfile>]"
        Wscript.Echo ""
        Wscript.Echo "PARAMETER SPECIfIERS:"
        Wscript.Echo "   zone          The name of the zone."
        Wscript.Echo strParameter
        Wscript.Echo "   server        The name of the DNS Server."
        Wscript.Echo "   username      The current user's name."
        Wscript.Echo "   password      Password of the current user."
        Wscript.Echo "   outputfile    The output file name."
        Wscript.Echo ""
        Wscript.Echo "EXAMPLE"
        Wscript.Echo ""
        Wscript.Echo strExample
 End Sub

Function strFindFQDNOwnerName(strContainerName, strOwnerName)
    If strOwnerName = "@" then
        strFindFQDNOwnerName = strContainerName
    Else
        If Not Right(strOwnerName,1) = "." then
            strFindFQDNOwnerName = strOwnerName & "." & strContainerName
        Else
            strFindFQDNOwnerName = strOwnerName
        End If
    End If
End Function

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
                                  ByRef strDomain        , _
                                  ByRef cResource        , _
                                  ByRef blnContextHelp     )
    

    'On Error Resume Next

    Dim strFlag, strProperty, strValue
    Dim intState, intArgIter, intPropertyCount
    Dim objFileSystem
    Dim blnError
    Dim strArgArray()
    Dim intModifyCount

    blnContextHelp = False
    intPropertyCount = 0
    
    If Wscript.Arguments.Count > 0 Then
        strFlag = Wscript.arguments.Item(0)
    End If

    'Check If the user is asking for help or is just confused
    If (strFlag="help") OR (strFlag="/h") OR (strFlag="\h") OR (strFlag="-h") _
        OR (strFlag = "\?") OR (strFlag = "/?") OR (strFlag = "?") _ 
        OR (strFlag="h") Then
        intParseCmdLine = CONST_SHOW_USAGE
        Exit Function
    End If

    'Retrieve the command line and set appropriate variables
     intArgIter = 0
    Do While intArgIter <= Wscript.arguments.Count - 1
        Select Case LCase(Wscript.arguments.Item(intArgIter))
  
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

            Case "/list"
                intParseCmdLine = CONST_LIST
                intArgIter = intArgIter + 1
                Select Case intChkNextArgument(intArgIter)
                    Case 3
                        blnContextHelp = True
                        intArgIter = intArgIter + 1
                    Case 2
                        intParseCmdLine = CONST_ERROR
                        Exit Function
                    Case 1
                        If GetClass(Wscript.Arguments(intArgIter), cResource) then
                            strDomain = Wscript.Arguments(intArgIter)
                            intArgIter = intArgIter + 1
                        Else
                            intArgIter = intArgIter + 1
                            If intChkNextArgument(intArgIter) = 1 then
                                strDomain=Wscript.Arguments(intArgIter)
                                intArgIter = intArgIter + 1
                            Else
                                intParseCmdLine = CONST_ERROR
                                Exit Function
                            End If
                        End If
                End Select

            Case "/add"
                intParseCmdLine = CONST_CREATE
                If CommonParse(intArgIter, blnContextHelp, CResource, False) then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If

            Case "/delete"
                intParseCmdLine = CONST_DELETE
                If CommonParse(intArgIter, blnContextHelp, CResource, False) then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If

            Case "/modify"
                intParseCmdLine = CONST_Modify
                If CommonParse(intArgIter, blnContextHelp, CResource, True) then
                    intParseCmdLine = CONST_ERROR
                    Exit Function
                End If
                If blnContextHelp = False Then
                    Do
                        If intChkNextArgument(intArgIter) <> 1 Then
                            Exit Do
                        End If
                        intArgIter = intArgIter + 1
                        If intChkNextArgument(intArgIter) <> 1 Then
                            intParseCmdLine = CONST_ERROR
                            Exit Function
                        End If
                        cResource.strModifyPropertyArray(intModifyCount,0) = Wscript.Arguments(intArgIter - 1)
                        cResource.strModifyPropertyArray(intModifyCount,1) = Wscript.Arguments(intArgIter)
                        intArgIter = intArgIter + 1
                        intModifyCount = intModifyCount + 1
                    Loop
                End If

            Case Else
                intParseCmdLine = CONST_ERROR
                Exit Function

        End Select
    Loop '** intArgIter <= Wscript.arguments.Count - 1
    
    If err.Number <> 0 then
        err.Clear
        intParseCmdLine = CONST_ERROR
        Exit Function
    End If
    
    If IsEmpty(intParseCmdLine) Then 
        If blnContextHelp = True then
            intParseCmdLine = CONST_SHOW_USAGE
        Else
            intParseCmdLine = CONST_ERROR
            Exit Function
        End If
    End If

End Function

'********************************************************************
'*
'* Function GetClass()
'*
'* Purpose: Determines which class to use
'*
'********************************************************************
Function GetClass(strClass, CResource)
    GetClass = False
    Select Case LCase(strClass)
        Case "a"
            Set cResource = New A_RecordData
        Case "cname"
            Set CResource = New CNAME_RecordData
        Case "mx"
            Set CResource = New MX_RecordData
        Case "soa"
            Set CResource = New SOA_RecordData
        Case "ptr"
            Set CResource = New PTR_RecordData
        Case "ns"
            Set CResource = New NS_RecordData
        Case "aaaa"
            Set CResource = New AAAA_RecordData
        Case "afsdb"
            Set CResource = New AFSDB_RecordData
        Case "atma"
            Set CResource = New ATMA_RecordData
        Case "hinfo"
            Set CResource = New HINFO_RecordData
        Case "isdn"
            Set CResource = New ISDN_RecordData
        Case "mb"
            Set CResource = New MB_RecordData
        Case "md"
            Set CResource = New MD_RecordData
        Case "mf"
            Set CResource = New MF_RecordData
        Case "mg"
            Set CResource = New MG_RecordData
        Case "minfo"
            Set CResource = New MINFO_RecordData
        Case "mr"
            Set CResource = New MR_RecordData
        Case "rp"
            Set CResource = New RP_RecordData
        Case "rt"
            Set CResource = New RT_RecordData
        Case "srv"
            Set CResource = New SRV_RecordData
        Case "txt"
            Set CResource = New TXT_RecordData
        Case "winsr"
            Set CResource = New WINSR_RecordData
        Case "wins"
            Set CResource = New WINS_RecordData
        Case "wks"
            Set CResource = New WKS_RecordData
        Case "x25"
            Set CResource = New X25_RecordData
        Case Else
            GetClass = True
    End Select

End Function

'********************************************************************
'*
'* Function CommonParse()
'*
'* Purpose: Parses the commandline based on Class.
'*
'********************************************************************
Function CommonParse(intArgIter, blnContextHelp, CResource, blnSOA)
    CommonParse = False
    intArgIter = intArgIter + 1
    Select Case intChkNextArgument(intArgIter)
        Case 3
            blnContextHelp = True
            intArgIter = intArgIter + 1
        Case 2
            CommonParse = True
            Exit Function
        Case 1
            If GetClass(Wscript.Arguments(intArgIter), CResource) then
                CommonParse = True
                Exit Function
            End If
            If CResource.strClassType = "SOA" then
                If blnSOA = False then
                    CommonParse = True
                    Exit Function
                End If
            End If
            ReDim strArgArray(cResource.intParseArguments)
            intArgIter = intArgIter + 1
            For I = 0 to cResource.intParseArguments
                Select Case intChkNextArgument(intArgIter)
                    Case 3
                        blnContextHelp = True
                        intArgIter = intArgIter + 1
                        I = cResource.intParseArguments
                    Case 2
                        CommonParse = True
                        Exit Function
                    Case 1
                        strArgArray(i) = Wscript.Arguments(intArgIter)
                        intArgIter = intArgIter + 1
                End Select
            Next
            cResource.PopulateClass(strArgArray)
        End Select
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
    Wscript.Echo " Gets or sets DNS Resource Record Data."
    Wscript.Echo ""
    Wscript.Echo "SYNTAX:"
    Wscript.Echo "  DnsResource operation <Parameter List>"
    Wscript.Echo "                      [/S <server>] [/U <username>] [/W <password>]"
    Wscript.Echo "                      [/O <outputfile>]"
    Wscript.Echo ""
    Wscript.Echo "  operation   [/list | /add | /delete | /Modify]"
    Wscript.Echo ""
    Wscript.Echo "    For help on a specific operation type:"
    Wscript.Echo ""
    Wscript.Echo "              DnsResource /list /?"
    Wscript.Echo "              DnsResource /add /?"
    Wscript.Echo "              DnsResource /delete /?"
    Wscript.Echo "              DnsResource /Modify /?"
    Wscript.Echo ""
    Wscript.Echo "PARAMETER SPECIFIERS:"
    Wscript.Echo "   server        A machine name."
    Wscript.Echo "   username      The current user's name."
    Wscript.Echo "   password      Password of the current user."
    Wscript.Echo "   outputfile    The output file name."
    Wscript.Echo ""

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
'* Function intChkNextArgument(intArgIter)
'*
'* Purpose: Checks to see If the next argument is valid.
'*
'********************************************************************
Function intChkNextArgument(intArgIter)
    intChkNextArgument = 1
    If Wscript.Arguments.Count < intArgIter + 1 then
        intChkNextArgument = 2
        Exit Function
    End If
    If Left(Wscript.Arguments(intArgIter),1) = "/" then
        intChkNextArgument = 2
    End If
    If Wscript.Arguments(intArgIter) = "/?" then
        intChkNextArgument = 3
    End If
End Function
'********************************************************************
'*
'* Function strPackString()
'*
'* Purpose: Attaches spaces to a string to increase the length to intWidth.
'*
'* Input:   strString   a string
'*          intWidth    the intended length of the string
'*          blnAfter    Should spaces be added after the string?
'*          blnTruncate specifies whether to truncate the string or not if
'*                      the string length is longer than intWidth
'*
'* Output:  strPackString is returned as the packed string.
'*
'********************************************************************
Private Function strPackString( ByVal strString, _
                                ByVal intWidth,  _
                                ByVal blnAfter,  _
                                ByVal blnTruncate)

    'On Error Resume Next

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

    blnGetArg = False 'failure, changed to True upon successful completion

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
```



## Connect to the DNS WMI Provider

This code example shows tasks associated with connecting to a DNS WMI Provider.


```VB
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
'*          strServer is set to local host If left unspecIfied
'*
'********************************************************************
Private Function blnConnect(ByVal strNameSpace, _
                            ByVal strUserName,  _
                            ByVal strPassword,  _
                            ByRef strServer,    _
                            ByRef objService)

    'On Error Resume Next

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
    Set objService = objLocator.ConnectServer (strServer, strNameSpace, _
       strUserName, strPassword)
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

    'Get the current server's name If left unspecified
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

    'On Error Resume Next

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
                    Call Wscript.Echo( "An unexpected program was used to " _
                                       & "run this script." )
                    Call Wscript.Echo( "Only CScript.Exe or WScript.Exe can " _
                                       & "be used to run this script." )
                    intStatus = CONST_ERROR
                End Select
        End If
    End If

    If intStatus <> CONST_CSCRIPT Then
        Call WScript.Echo( "Please run this script using CScript." & vbCRLF & _
             "This can be achieved by" & vbCRLF & _
             "1. Using ""CScript PS.VBS arguments"" for Windows 95/98 or" _
             & vbCRLF & "2. Changing the default Windows Script Host " _
             & "setting to CScript" & vbCRLF & "    using ""CScript " _
             & "//H:CScript //S"" and running the script using" & vbCRLF & _
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
'* Output:  strMessage is either displayed on screen or written to a file.
'*
'********************************************************************
Sub WriteLine(ByVal strMessage, ByVal objFile)

    'On Error Resume Next
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
'* Purpose: Reports error with a string saying what the error occurred in.
'*
'* Input:   strIn        string saying what the error occurred in.
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
'* Input:   strFileName        A string with the name of the file.
'*
'* Output:  Sets objOpenFile to a FileSystemObject and setis it to 
'*            Nothing upon Failure.
'* 
'********************************************************************
Private Function blnOpenFile(ByVal strFileName, ByRef objOpenFile)

    'On Error Resume Next

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



 

 




