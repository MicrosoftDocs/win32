---
Description: You can create outbound routing rules using scripts.
ms.assetid: 35bb803d-fce4-46a3-825a-ec3a5138ed67
title: Creating and Managing Outbound Routing Rules
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating and Managing Outbound Routing Rules

You can create [outbound routing rules](-mfax-outbound-routing-rules.md) using scripts.

The following Microsoft Visual Basic code example creates an outbound routing rule, and demonstrates the management of the rules collection.

> [!Note]  
> This code will not run on Windows XP Home Edition or Windows XP Professional, Windows Vista Business, Windows Vista Enterprise, or Windows Vista Ultimate.

 


```VB
    Private Sub Form_Load()
        'Create the root object
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim collFaxOutboundRoutingRules As FAXCOMEXLib.FaxOutboundRoutingRules
        Dim objFaxOutboundRoutingRule As FAXCOMEXLib.FaxOutboundRoutingRule
        Dim objFaxDevice As FAXCOMEXLib.FaxDevice

        Dim CountryCode As Long
        Dim AreaCode As Long

        Dim ID As Long

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server
        objFaxServer.Connect("")

        'Get the first device. In this example, all rules are associated 
        'with this device
        objFaxDevice = objFaxServer.GetDevices.Item(1)

        'Get the device ID
        ID = objFaxDevice.ID

        'Get the rules collection
        collFaxOutboundRoutingRules = objFaxServer.OutboundRouting.GetRules

        'Display information about the rules collection, and add a group name if 
        'it's an empty string
        MsgBox("There are " & collFaxOutboundRoutingRules.Count & " outbound routing rules on this server.")
        Dim i As Long
        For i = 1 To collFaxOutboundRoutingRules.Count
            'Get the routing rule object
            objFaxOutboundRoutingRule = collFaxOutboundRoutingRules.Item(i)
            'Refresh the object (changes may have been made through 
            'the Fax Service Manager)
            objFaxOutboundRoutingRule.Refresh()

            MsgBox("Outbound routing rule number: " & i & _
            vbCrLf & "Area code: " & objFaxOutboundRoutingRule.AreaCode & _
            vbCrLf & "Country/region code: " & objFaxOutboundRoutingRule.CountryCode & _
            vbCrLf & "Device ID: " & objFaxOutboundRoutingRule.DeviceId & _
            vbCrLf & "Group name: " & objFaxOutboundRoutingRule.GroupName & _
            vbCrLf & "Status: " & objFaxOutboundRoutingRule.Status & _
            vbCrLf & "Is device used: " & objFaxOutboundRoutingRule.UseDevice)

            'Allow chance to change devices, but only if device (rather than group) 
            'is used
            If objFaxOutboundRoutingRule.UseDevice = True Then
                Dim MakeChange As String
                MakeChange = InputBox("Do you want to change the device for this rule (Y/N)?")
                If MakeChange = "Y" Then
                    Dim NewDevice As Long
                    NewDevice = InputBox("Input new device ID.")
                    objFaxOutboundRoutingRule.DeviceId = NewDevice
                    'Save the change
                    objFaxOutboundRoutingRule.Save()
                End If
            End If

        Next

        Dim Choice As Integer
        Choice = InputBox("Do you want to display an item based on its country/region and area code (1), " _
        & "remove an item based on its country/region and area code (2), remove an item based on its" _
        & " item number (3), or add a rule (4)? Input 1, 2, 3 or 4. Input 0 to exit the program.")

        'Exit the program if 0 is input
        If Choice = 0 Then End

        'Display an outbound routing rule based on country/region code and area code
        If Choice = 1 Then

            CountryCode = InputBox("Provide the country/region code")
            AreaCode = InputBox("Provide the area code")
            objFaxOutboundRoutingRule = collFaxOutboundRoutingRules.ItemByCountryAndArea(CountryCode, AreaCode)

            MsgBox("Outbound routing rule number: " & i & _
            vbCrLf & "Area code: " & objFaxOutboundRoutingRule.AreaCode & _
            vbCrLf & "Country/region code: " & objFaxOutboundRoutingRule.CountryCode & _
            vbCrLf & "Device ID: " & objFaxOutboundRoutingRule.DeviceId & _
            vbCrLf & "Group name: " & objFaxOutboundRoutingRule.GroupName & _
            vbCrLf & "Status: " & objFaxOutboundRoutingRule.Status & _
            vbCrLf & "Is device used: " & objFaxOutboundRoutingRule.UseDevice)

        End If

        'Remove an outbound routing rule based on country/region code and area code
        If Choice = 2 Then

            CountryCode = InputBox("Provide the country/region code")
            AreaCode = InputBox("Provide the area code")
            collFaxOutboundRoutingRules.RemoveByCountryAndArea(CountryCode, AreaCode)

        End If

        'Remove an outbound routing rule based on item number
        If Choice = 3 Then

            Dim ItemNumber As Long
            ItemNumber = InputBox("Provide the item number.")
            collFaxOutboundRoutingRules.Remove(ItemNumber)

        End If

        'Add a rule
        If Choice = 4 Then

            'Initialize error handling
1:          On Error Resume Next
            Err.Clear()

            CountryCode = InputBox("Provide the country/region code for the new rule")
            AreaCode = InputBox("Provide the area code for the new rule")

            objFaxOutboundRoutingRule = collFaxOutboundRoutingRules.Add(CountryCode, AreaCode, True, "", ID)
            'Error handling
            If Err.Number <> 0 Then
                MsgBox("A rule for this country/region code and area code exists already, please try again")
                GoTo 1
            End If
        End If
        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        'implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



 

 



