---
Description: 'The following Microsoft Visual Basic code example demonstrates how to manage fax device providers.'
ms.assetid: '422003a1-7db2-4eff-97bd-8ca889a3e5f6'
title: Managing Fax Device Providers
---

# Managing Fax Device Providers

The following Microsoft Visual Basic code example demonstrates how to manage fax device providers.


```VB
    Private Sub Form_Load()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim collFaxDeviceProviders As FAXCOMEXLib.FaxDeviceProviders
        Dim objFaxDeviceProvider As FAXCOMEXLib.FaxDeviceProvider

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server
        objFaxServer.Connect("")

        collFaxDeviceProviders = objFaxServer.GetDeviceProviders

        Dim n As Long
        n = collFaxDeviceProviders.Count

        'Display the properties for each fax device provider
        Dim i As Integer
        For i = 1 To n
            objFaxDeviceProvider = collFaxDeviceProviders.Item(i)
            MsgBox("Debug = " & objFaxDeviceProvider.Debug & _
            vbCrLf & "Name = " & objFaxDeviceProvider.FriendlyName & _
            vbCrLf & "Image name = " & objFaxDeviceProvider.ImageName & _
            vbCrLf & "Init error code = " & objFaxDeviceProvider.InitErrorCode & _
            vbCrLf & "Build and version = " & objFaxDeviceProvider.MajorBuild & "." & _
                objFaxDeviceProvider.MinorBuild & "." & _
                objFaxDeviceProvider.MajorVersion & "." & _
                objFaxDeviceProvider.MinorVersion & _
            vbCrLf & "Status = " & objFaxDeviceProvider.Status & _
            vbCrLf & "Tapi provider = " & objFaxDeviceProvider.TapiProviderName & _
            vbCrLf & "Unique name = " & objFaxDeviceProvider.UniqueName)

            'Display the device ids for that provider
            Dim DeviceArray() As Long
            DeviceArray = objFaxDeviceProvider.DeviceIds
            'UBound finds the size of the array
            Dim j As Integer
            For j = 0 To UBound(DeviceArray)
                MsgBox("Device ID: " & DeviceArray(j))
            Next
        Next
        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        'implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



 

 



