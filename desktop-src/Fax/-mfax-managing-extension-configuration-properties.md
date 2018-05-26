---
Description: The Fax Extension Configuration API mechanism is a means of persistently storing configuration data without having to write directly to the fax service registry.
ms.assetid: e9800209-9ff9-495d-ab60-a0cee64eb569
title: Managing Extension Configuration Properties
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Managing Extension Configuration Properties

The Fax Extension Configuration API mechanism is a means of persistently storing configuration data without having to write directly to the fax service registry. The following Microsoft Visual Basic code examples demonstrate how to set and get the extension configuration information for a fax device and for the fax server. For more information, see [About the Fax Extension Configuration API](-mfax-about-the-fax-extension-configuration-api.md).

## For a fax device:


```VB
    Private Sub Form_Load()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim objFaxDevice As FAXCOMEXLib.FaxDevice
        Dim DeviceProperty(2) As Byte
        Dim ExtProperty As Object

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server
        objFaxServer.Connect("")

        'Get the first device
        objFaxDevice = objFaxServer.GetDevices.Item(1)

        'Define the values of the array members
        DeviceProperty(0) = 1
        DeviceProperty(1) = 2
        DeviceProperty(2) = 3

        objFaxDevice.SetExtensionProperty("{B1F944B9-9A16-45d1-933A-4060A4871AB0}", DeviceProperty)

        'Get the extension property
        ExtProperty = objFaxDevice.GetExtensionProperty("{B1F944B9-9A16-45d1-933A-4060A4871AB0}")

        'Display the members of the property array
        Dim i As Integer
        For i = 0 To UBound(ExtProperty)
            MsgBox(ExtProperty(i))
        Next
        Exit Sub

Error_Handler:
    'Implement error handling at the end of your subroutine. This 
    'implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



## For a fax server:


```VB
    Private Sub Form_Load()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim ServerProperty(2) As Byte
        Dim ExtProperty As Object

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server
        objFaxServer.Connect("")

        'Define the values of the array members
        ServerProperty(0) = 4
        ServerProperty(1) = 2
        ServerProperty(2) = 3

        'Set the extension property
        objFaxServer.SetExtensionProperty("{AC7D0DEE-B6E5-4a44-AF45-835C58CB44D2}", ServerProperty)

        'Get the extension property
        ExtProperty = objFaxServer.GetExtensionProperty("{AC7D0DEE-B6E5-4a44-AF45-835C58CB44D2}")

        'Display the members of the property array
        Dim i As Integer
        For i = 0 To UBound(ExtProperty)
            MsgBox(ExtProperty(i))
        Next
        Exit Sub

Error_Handler:
    'Implement error handling at the end of your subroutine. This 
    'implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



 

 



