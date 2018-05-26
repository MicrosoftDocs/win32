---
title: Creating Cluster Objects with the Failover Cluster Automation Server
description: The following HTML/VBScript example creates an HTML form that allows users to create new resources.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: af8f3ab9-2ca5-48dd-bafd-829fb134e5a3
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Failover Cluster Automation Server Failover Cluster ,creating cluster objects
- Cluster Automation Server Failover Cluster ,creating cluster objects
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Creating Cluster Objects with the Failover Cluster Automation Server

\[The [Failover Cluster Automation Server](https://msdn.microsoft.com/library/aa372940) is available for use in Windows Server 2008. It may be altered or unavailable in subsequent versions.\]

The following HTML/VBScript example creates an HTML form that allows users to create new resources.


```VB
<HTML>
<HEAD>
<TITLE>Create Cluster Resource</TITLE>
<SCRIPT LANGUAGE="VBScript" RUNAT="Server">
<!--
'  
'  Define globals and open cluster.
'  
    Dim objCluster, objGroup, objResType, objRes
    Dim strResName, strResType, strGroupName
    Dim bSepMon
    Set objCluster = CreateObject("MSCluster.Cluster")
    objCluster.Open ""
    '''''''''''''''''''''''''''''''''
    Sub lstGroups_OnClick()
        strGroupName = ResCreate.lstGroups.Value
    End Sub
    '''''''''''''''''''''''''''''''''
    Sub lstTypes_OnClick()
        strResType = ResCreate.lstTypes.Value
    End Sub
    '''''''''''''''''''''''''''''''''
    Sub chkSepMon_OnClick()
        bSepMon = Not bSepMon
    End Sub
    '''''''''''''''''''''''''''''''''
    Sub btnOK_OnClick()
        Dim str
        str = ResCreate.txtGroupName.Value
    '
    '  If the user has entered text in the group name text box,
    '  try to create a new group using this name. Otherwise
    '  the user needs to have selected an existing group
    '  from the select list.
    '
        If Len(str) > 0 Then
            strGroupName = str
            Set objGroup = objCluster.ResourceGroups.CreateItem(strGroupName)
        ElseIf Len(strGroupName) > 0 Then
            Set objGroup = objCluster.ResourceGroups.Item(strGroupName)
        Else
            MsgBox("Group name cannot be NULL.")
            Exit Sub
        End If
        strResName = ResCreate.txtResName.Value
        If Len(strResName) > 0 Then
            If bSepMon Then
                Set objRes = objGroup.Resources.CreateItem(strResName, strResType, 1)
            Else
                Set objRes = objGroup.Resources.CreateItem(strResName, strResType, 0)
            End If
        Else
            MsgBox("Group name cannot be NULL.")
            Exit Sub
        End If
        Set objRes = Nothing
        Set objGroup = Nothing
        Set objCluster = Nothing
        Document.Navigate "results.html"  ' TODO: create this page!
    End Sub
    '''''''''''''''''''''''''''''''''
    Sub btnCancel_OnClick()
        Document.Navigate "cancel.html"   ' TODO: create this page!
    End Sub
    '''''''''''''''''''''''''''''''''
-->
</SCRIPT>
</HEAD>
<BODY>
<H1>Create Cluster Resource</H1><HR>
<FORM NAME="ResCreate" 
      METHOD="POST" 
      ACTION="rescreate_results.vbs"
      LANGUAGE="VBScript"
      TITLE="Resource Creation Form">
<!--==================================================================
Add a select list for groups.
===================================================================-->
    <B>Select group in which to create resource...</B><BR>
    <SELECT ID="lstGroups" SIZE="5">
    <SCRIPT LANGUAGE="VBScript">
    <!--
        For Each objGroup in objCluster.ResourceGroups
            Document.Write "<OPTION VALUE=" & Chr(34) & objGroup.Name & Chr(34) & ">" & objGroup.Name & vbCrLf
        Next
    -->
    </SCRIPT>
    </SELECT>
    <BR>
<!--==================================================================
Add a text box to allow the user to create a new group..
===================================================================-->
    <B>...or enter new group name:</B><BR>
    <INPUT TYPE="TEXT" ID="txtGroupName" SIZE="40">
    <BR><BR>
<!--==================================================================
Add a select list for resource types.
===================================================================-->
    <B>Specify resource type:</B><BR>
    <SELECT ID="lstTypes" SIZE="5">
    <SCRIPT LANGUAGE="VBScript">
    <!--
        For Each objResType in objCluster.ResourceTypes
            Document.Write "<OPTION VALUE=" & Chr(34) & objResType.Name & Chr(34) & ">" & objResType.Name & vbCrLf
        Next
    -->
    </SCRIPT>
    </SELECT>
    <BR><BR>
<!--==================================================================
Add "separate monitor" check box.
===================================================================-->
    <B>Create resource in a separate Resource Monitor:</B>
    <INPUT TYPE="Checkbox" ID="chkSepMon">
    <BR><BR>
<!--==================================================================
Add a text box for the resource name.
===================================================================-->
    <B>Resource Name:</B>
    <INPUT TYPE="TEXT" ID="txtResName" SIZE="40">
    <BR><HR>
<!--==========================================
Add "OK"and "Cancel" buttons.
===========================================-->
    <INPUT TYPE="BUTTON" ID="btnOK" VALUE="   OK   ">
    <INPUT TYPE="BUTTON" ID="btnCancel" VALUE="Cancel">
</FORM>
</BODY>
</HTML>
```



 

 




