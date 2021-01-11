---
title: VB Script Listing all Service Connection Points
ms.assetid: 7a76f872-3e4e-4bb7-8f2d-e30b1246369f
ms.tgt_platform: multiple
description: "Learn more about: VB Script Listing all Service Connection Points"
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# VB Script Listing all Service Connection Points

Service Connection Points can be managed using VB Script. The following sample code shows how to list all Service Connection Points on the domain name provided on the command line:


```VB
Option Explicit

Dim scpDN
scpDN = WScript.Arguments.Named("SCP")

If ( scpDN = "" ) Then
    Usage
Else
    ScpProperties scpDN
End If

' End of Main

Sub Usage
    WScript.Echo "USAGE:  ScpProperties /SCP:<SCP DN>"
    WScript.Echo ""
    Wscript.Echo "Remember to put the SCP DN between quotes"
End Sub

Sub ScpProperties( strDN )

    Dim oConn ' As ADODB.Connection
    Set oConn = CreateObject("ADODB.Connection")
    
    oConn.Open "Provider=ADsDSOObject"
    
    Dim oCmd ' As ADODB.Command
    Set oCmd = CreateObject("ADODB.Command")
    oCmd.ActiveConnection = oConn
    
    ' In the next command, the real magic is in knowing LDAP queries
    ' GC means to ask the global catalog.
    oCmd.CommandText = "<GC://" & strDN & ">;" & _
                        "(objectClass=ServiceConnectionPoint);" & _
                        "distinguishedname,name,serviceDNSName," & _
                        "serviceDNSNameType,serviceBindingInformation," & _
                        "serviceClassName,Keywords;" & _
                        "subtree"

    Dim oRs ' As ADODB.Recordset
    Set oRs = oCmd.Execute
    
    Dim lCount ' As Long
    lCount = 0
    Do While (Not oRs.EOF)
    
        Wscript.Echo "SCP Name: " & oRs("name")
        Wscript.Echo "DN: " & oRs("distinguishedname")
        Wscript.Echo "serviceDNSName: " & oRs("serviceDNSName")
        Wscript.Echo "serviceDNSNameType: " & oRs("serviceDNSNameType")
        Wscript.Echo "serviceClassName: " & oRs("serviceClassName")
        Dim a ' As Variant
        Dim l 'As Long
        
        a = oRs("serviceBindingInformation")
        
        If (Not IsNull(a)) Then
            Wscript.Echo "serviceBindingInformation:"
            For l = LBound(a) To UBound(a)
                Wscript.Echo vbTab & a(l)
            Next
            Wscript.Echo 
        End If
        
        a = oRs("Keywords")
        If (Not IsNull(a)) Then
            Wscript.Echo "Keywords: "
            For l = LBound(a) To UBound(a)
                Wscript.Echo vbTab & a(l)
            Next
        End If
        
        oRs.MoveNext
        lCount = lCount + 1
        Wscript.Echo 
    Loop
    
    Wscript.Echo "Total objects = " & lCount
    oConn.Close
    
End Sub
    
```



 

 




