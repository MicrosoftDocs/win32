---
Description: The following Microsoft Visual Basic code example creates an outbound routing group and adds devices to the group. It then displays information about all of the outbound routing groups on the server, and allows you to remove a group.
ms.assetid: 5a05df3b-c56b-4dfc-a0ee-7f1c2861e9ae
title: Managing Outbound Routing Groups
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Managing Outbound Routing Groups

The following Microsoft Visual Basic code example creates an outbound routing group and adds devices to the group. It then displays information about all of the outbound routing groups on the server, and allows you to remove a group.

> [!Note]  
> This example will fail if you try to add a group using the name of an existing group.

 


```VB
    Private Sub Form_Load()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim objFaxOutboundRouting As FAXCOMEXLib.FaxOutboundRouting
        Dim collFaxOutboundRoutingGroups As FAXCOMEXLib.FaxOutboundRoutingGroups
        Dim objFaxOutboundRoutingGroup As FAXCOMEXLib.FaxOutboundRoutingGroup
        Dim collFaxDevices As FAXCOMEXLib.FaxDevices
        Dim objFaxDevice As FAXCOMEXLib.FaxDevice

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server. An empty string defaults to the local server
        objFaxServer.Connect("")

        'Create the outbound routing object
        objFaxOutboundRouting = objFaxServer.OutboundRouting

        'Get the routing group collection
        collFaxOutboundRoutingGroups = objFaxOutboundRouting.GetGroups

        'Create the outbound routing group object
        Dim GroupName As String
        GroupName = InputBox("Provide a name for the outbound routing group.")
        objFaxOutboundRoutingGroup = collFaxOutboundRoutingGroups.Add(GroupName)

        'Get the devices collection
        collFaxDevices = objFaxServer.GetDevices

        'Add devices to the routing group
        For n = 1 To collFaxDevices.Count
            objFaxDevice = collFaxDevices.Item(n)
            objFaxOutboundRoutingGroup.DeviceIds.Add(objFaxDevice.Id)
        Next n
        'Move last device to the top of the order
        objFaxOutboundRoutingGroup.DeviceIds.SetOrder(collFaxDevices.Item(n - 1).Id, 1)

        'Display the number of devices, and the device id of the first device,
        'to confirm its location in the order
        MsgBox("Number of devices " & objFaxOutboundRoutingGroup.DeviceIds.Count & _
            vbCrLf & "ID of first device " & objFaxOutboundRoutingGroup.DeviceIds.Item(1))

        'Remove the first device
        objFaxOutboundRoutingGroup.DeviceIds.Remove(1)

        'Display the number of routing groups in the collection
        MsgBox("There are " & collFaxOutboundRoutingGroups.Count & " routing groups on this server")

        Dim i As Integer
        For i = 1 To collFaxOutboundRoutingGroups.Count
            objFaxOutboundRoutingGroup = collFaxOutboundRoutingGroups.Item(i)
            'Display the name of each group, and the status of its devices
            MsgBox("Routing group number: " & i & _
            vbCrLf & "Outbound routing group name: " & objFaxOutboundRoutingGroup.Name & _
            vbCrLf & "Device status: " & objFaxOutboundRoutingGroup.Status)
        Next

        'Allow user to remove a routing group
        Dim Answer As String
        Answer = InputBox("Do you want to remove a routing group (Y/N)?")
        If Answer = "Y" Then
            Dim ItemNumber As Integer
            ItemNumber = InputBox("Provide the item number for the group you want to remove.")
            collFaxOutboundRoutingGroups.Remove(ItemNumber)
        End If
        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        'implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



 

 



