---
Description: In Windows Vista, the FaxConfiguration object is used to set properties of archive and queue folders. The following Microsoft Visual Basic examples show how to do this.
ms.assetid: ff01d86e-3aae-4bbf-8221-e0d219d2687c
title: Managing Queues and Archives
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Managing Queues and Archives

In Windows Vista, the [**FaxConfiguration**](-mfax-faxconfiguration.md) object is used to set properties of archive and queue folders. The following Microsoft Visual Basic examples show how to do this.


```VB
    Private Sub Form_Load()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim objFaxConfiguration As FAXCOMEXLib.FaxConfiguration

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server
        objFaxServer.Connect("")

        'Get the configuration object
        objFaxConfiguration = objFaxServer.Configuration

        'Display the archive properties
        MsgBox("AgeLimit: " & objFaxConfiguration.ArchiveAgeLimit & _
        vbCrLf & "Archive folder: " & objFaxConfiguration.ArchiveLocation & _
        vbCrLf & "High quota water mark: " & objFaxConfiguration.HighQuotaWaterMark & _
        vbCrLf & "Low quota water mark: " & objFaxConfiguration.LowQuotaWaterMark & _
        vbCrLf & "Size quota warning: " & objFaxConfiguration.SizeQuotaWarning & _
        vbCrLf & "Is archive used?: " & objFaxConfiguration.UseArchive)

        'Set OutgoingQueue Properties
        objFaxConfiguration.DiscountRateStart = Date.FromOADate(15.0)
        objFaxConfiguration.DiscountRateEnd = Date.FromOADate(15.25)
        'Set the number of retries
        objFaxConfiguration.Retries = 6
        'Set the retry delay to 10 minutes
        objFaxConfiguration.RetryDelay = 10
        'Use the device TSID
        objFaxConfiguration.UseDeviceTSID = True

        'Set the age limit to 4 days
        objFaxConfiguration.ArchiveAgeLimit = 4

        'Save the changes
        objFaxConfiguration.Save()


        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        'implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



 

 



