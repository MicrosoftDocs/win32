---
Description: The following Microsoft Visual Basic code example demonstrates how to manage a collection of fax devices.
ms.assetid: 8e0d5b13-2126-49a2-80b7-ae3a817496bd
title: Managing the Fax Device Collection
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Managing the Fax Device Collection

The following Microsoft Visual Basic code example demonstrates how to manage a collection of fax devices.


```
    Private Sub Form_Load()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim collFaxDevices As FAXCOMEXLib.FaxDevices
        Dim objFaxDevice As FAXCOMEXLib.FaxDevice

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server
        objFaxServer.Connect("")

        collFaxDevices = objFaxServer.GetDevices
        MsgBox("This server has " & collFaxDevices.Count & " fax devices.")

        Dim I As Object
        For I = 1 To collFaxDevices.Count
            objFaxDevice = collFaxDevices.Item(I)
            MsgBox("Device ID for device number " & I & " is: " & objFaxDevice.ID)
        Next

        Dim ID As Long
        ID = InputBox("Input a device ID to get information about that device")
        objFaxDevice = collFaxDevices.ItemById(ID)

        'Refresh the device information
        objFaxDevice.Refresh()

        MsgBox("Device name: " & objFaxDevice.DeviceName & _
        vbCrLf & "Device ID: " & objFaxDevice.Id & _
        vbCrLf & "Provider unique name: " & objFaxDevice.ProviderUniqueName & _
        vbCrLf & "Powered off: " & objFaxDevice.PoweredOff & _
        vbCrLf & "Receiving now: " & objFaxDevice.ReceivingNow & _
        vbCrLf & "Ringing now: " & objFaxDevice.RingingNow & _
        vbCrLf & "Sending now: " & objFaxDevice.SendingNow)

        'Display the routing methods for the device
        Dim RoutingMethods() As String
        RoutingMethods = objFaxDevice.UsedRoutingMethods
        'UBound finds the size of the array
        For j = 0 To UBound(RoutingMethods)
            MsgBox("Method number " & j & _
            vbCrLf & RoutingMethods(j))
        Next

        'Stop using the first routing method
        objFaxDevice.UseRoutingMethod(RoutingMethods(0), False)


        'Save the change
        objFaxDevice.Save()
        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        ' implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



 

 



