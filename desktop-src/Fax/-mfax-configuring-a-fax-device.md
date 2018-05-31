---
Description: You can configure a fax device using scripts.
ms.assetid: 64bdc08c-1902-448a-9eda-b557ab4bb095
title: Configuring a Fax Device
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Configuring a Fax Device

You can configure a fax device using scripts.

The following Microsoft Visual Basic code example configures a fax device.


```VB
    Private Sub Form_Load()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim objFaxDevice As FAXCOMEXLib.FaxDevice

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server
        objFaxServer.Connect("")

        'Get the device
        objFaxDevice = objFaxServer.GetDevices.Item(1)

        'Set the device properties
        objFaxDevice.CSID = "Accounts payable"
        objFaxDevice.Description = "Primary fax device"
        objFaxDevice.ReceiveMode = FAXCOMEXLib.FAX_DEVICE_RECEIVE_MODE_ENUM.fdrmAUTO_ANSWER
        objFaxDevice.RingsBeforeAnswer = 5
        objFaxDevice.SendEnabled = True
        objFaxDevice.TSID = "Accounts payable"

        'Save the device configuration
        objFaxDevice.Save()
        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        'implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



 

 



