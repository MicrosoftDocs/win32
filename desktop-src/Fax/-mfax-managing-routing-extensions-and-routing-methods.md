---
Description: The following Microsoft Visual Basic code example demonstrates how to access information about routing extensions and routing methods.
ms.assetid: cef24608-cab1-4090-aa94-3a1b76733e98
title: Managing Routing Extensions and Routing Methods
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Managing Routing Extensions and Routing Methods

The following Microsoft Visual Basic code example demonstrates how to access information about routing extensions and routing methods.


```VB
    Private Sub Form_Load()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim objFaxInboundRouting As FAXCOMEXLib.FaxInboundRouting
        Dim collFaxInboundRoutingExtensions As FAXCOMEXLib.FaxInboundRoutingExtensions
        Dim objFaxInboundRoutingExtension As FAXCOMEXLib.FaxInboundRoutingExtension
        Dim collFaxInboundRoutingMethods As FAXCOMEXLib.FaxInboundRoutingMethods
        Dim collFaxInboundRoutingMethod As FAXCOMEXLib.FaxInboundRoutingMethod

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server
        objFaxServer.Connect("")

        collFaxInboundRoutingExtensions = objFaxServer.InboundRouting.GetExtensions
        collFaxInboundRoutingMethods = objFaxServer.InboundRouting.GetMethods

        Dim ECount As Integer
        Dim MCount As Integer
        'Get and display the number of routing extensions and methods on this server
        ECount = collFaxInboundRoutingExtensions.Count
        MCount = collFaxInboundRoutingMethods.Count
        MsgBox("There are " & ECount & " routing extensions and " & _
        vbCrLf & MCount & " routing methods on this server.")

        Dim n As Integer
        For n = 1 To ECount
            MsgBox("Routing extension number " & n & vbCrLf & _
            vbCrLf & "Debug = " & collFaxInboundRoutingExtensions(n).Debug & _
            vbCrLf & "Name = " & collFaxInboundRoutingExtensions(n).FriendlyName & _
            vbCrLf & "Image name = " & collFaxInboundRoutingExtensions(n).ImageName & _
            vbCrLf & "Init error code = " & collFaxInboundRoutingExtensions(n).InitErrorCode & _
            vbCrLf & "Build and version = " & collFaxInboundRoutingExtensions(n).MajorBuild & "." & _
                collFaxInboundRoutingExtensions(n).MinorBuild & "." & _
                collFaxInboundRoutingExtensions(n).MajorVersion & "." & _
                collFaxInboundRoutingExtensions(n).MinorVersion & _
            vbCrLf & "Status = " & collFaxInboundRoutingExtensions(n).Status & _
            vbCrLf & "Unique name = " & collFaxInboundRoutingExtensions(n).UniqueName)

            'Display the method GUIDs for this extension
            Dim MethodArray() As String
            MethodArray = collFaxInboundRoutingExtensions(n).Methods
            'UBound finds the size of the array
            For j = 0 To UBound(MethodArray)
                MsgBox("Routing extension number " & n & ", Method number " & j & vbCrLf & _
                MethodArray(j))
            Next

        Next

        Dim m As Integer
        For m = 1 To MCount
            collFaxInboundRoutingMethods(m).Refresh()
            MsgBox("Routing method number " & m & vbCrLf & _
            vbCrLf & "Friendly name = " & collFaxInboundRoutingMethods(m).ExtensionFriendlyName & _
            vbCrLf & "Image name = " & collFaxInboundRoutingMethods(m).ExtensionImageName & _
            vbCrLf & "Function name = " & collFaxInboundRoutingMethods(m).FunctionName & _
            vbCrLf & "Guid = " & collFaxInboundRoutingMethods(m).Guid & _
            vbCrLf & "Name = " & collFaxInboundRoutingMethods(m).Name & _
            vbCrLf & "Priority = " & collFaxInboundRoutingMethods(m).Priority)

            'Allow change in priority
            Dim Answer As String
            Answer = InputBox("Change priority? (Y/N)")
            If Answer = "Y" Then
                Dim NewPriority As Long
                NewPriority = InputBox("Provide new priority")
                collFaxInboundRoutingMethods(m).Priority = NewPriority
                collFaxInboundRoutingMethods(m).Save()
            End If

        Next
        Exit Sub

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        'implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



 

 



