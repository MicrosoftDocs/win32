---
description: You can use the following methods to configure application recycling values for your COM+ application.
ms.assetid: 8f6a4879-cf4c-4171-8448-bc07371e038c
title: Configuring COM+ Application Recycling Values
ms.topic: article
ms.date: 05/31/2018
---

# Configuring COM+ Application Recycling Values

You can use the following methods to configure application recycling values for your COM+ application.

> [!Note]  
> You cannot recycle a COM+ application that has been configured to run as a Windows service. Also, library applications have the recycling and pooling properties of their host process.

 

## Component Services Administrative Tool

To configure application recycling for a COM+ application, use the following steps:

1.  In the console tree of the Component Services administrative tool, right-click the COM+ server application you want to be recycled and then click **Properties**.

2.  On the **Pooling & Recycling** tab, enter values for **Lifetime Limit (minutes)**, **Memory Limit (KB)**, **Expiration Timeout (minutes)**, **Call Limit**, and **Activation Limit**, depending on the criteria you want to use.

    -   **Lifetime Limit** indicates the maximum number of minutes a process can run before it's recycled. The valid range is 0 through 30,240 minutes (21 days). The default number of minutes is 0.
    -   **Memory Limit** indicates the maximum amount of process memory usage (in kilobytes) before recycling the process. If the process's memory usage exceeds the specified number for longer than one minute, the process is recycled. The valid range is 0 through 1,048,576 KB, and the default amount of memory usage is 0 KB.
    -   **Expiration Timeout** indicates the number of minutes to wait, before being forcibly shut down, for the release of all external references to objects in the process. The valid range is 1 through 1440 minutes (24 hours), and the default expiration time-out is 15 minutes. This value is used only when it is already determined that a process will be recycled based on the other criteria.
    -   **Call Limit** indicates the maximum number of calls that application objects can accept before recycling the process. The valid range is 0 through 1,048,576 calls, and the default number of calls is 0.
    -   **Activation Limit** indicates the maximum number of application object activations to accept before recycling the process. The valid range is 0 through 1,048,576 activations, and the default number of activations is 0.

    > [!Note]  
    > When the **Lifetime Limit**, **Memory Limit**, **Call Limit**, or **Activation Limit** value is set to 0 (the default value), application recycling for that criterion is disabled. When all four of these criteria are set to 0, application recycling is disabled for the selected application.

     

3.  Click **OK**.

## Visual Basic

The following function in Microsoft Visual Basic demonstrates how you can set the application recycling values for any COM+ server application that you choose. To use it from Visual Basic, add a reference to the COM+ Admin Type Library.


```VB
Function SetMyApplicationRecycling( _
  strApplicationName As String, _
  lngLifetimeLimit As Long, _
  lngMemoryLimit As Long, _
  lngCallLimit As Long, _
  lngActivationLimit As Long, _
  lngExpirationTimeout As Long _
) As Boolean  ' Return False if any errors occur.

    SetMyApplicationRecycling = False  ' Initialize the function.
    On Error GoTo My_Error_Handler  ' Initialize error handling.

    Dim objCatalog As COMAdmin.COMAdminCatalog
    Dim objAppCollection As COMAdmin.COMAdminCatalogCollection
    Dim objApplication As COMAdmin.COMAdminCatalogObject
    Set objCatalog = CreateObject("COMAdmin.COMAdminCatalog")
    Set objAppCollection = objCatalog.GetCollection("Applications")
    objAppCollection.Populate
    For Each objApplication In objAppCollection
        With objApplication
            If .Name = strApplicationName Then
                .Value("RecycleLifetimeLimit") = lngLifetimeLimit
                .Value("RecycleMemoryLimit") = lngMemoryLimit
                .Value("RecycleCallLimit") = lngCallLimit
                .Value("RecycleActivationLimit") = lngActivationLimit
                .Value("RecycleExpirationTimeout") = lngExpirationTimeout
                MsgBox strApplicationName & _
                  " recycling values are now set to the following: " & _
                  vbNewLine & vbNewLine & _
                  "Lifetime Limit = " & lngLifetimeLimit & vbNewLine & _
                  "Memory Limit = " & lngMemoryLimit & vbNewLine & _
                  "Call Limit = " & lngCallLimit & vbNewLine & _
                  "Activation Limit = " & lngActivationLimit & vbNewLine _
                  & "Expiration Timeout = " & lngExpirationTimeout
                Exit For
            End If
        End With
    Next
    objAppCollection.SaveChanges
    Set objApplication = Nothing
    Set objAppCollection = Nothing
    Set objCatalog = Nothing
    SetMyApplicationRecycling = True  ' Successful end to procedure
    Exit Function
    
My_Error_Handler:  ' Replace with specific error handling.
    MsgBox "Error # " & Err.Number & " (Hex: " & Hex(Err.Number) _
      & ")" & vbNewLine & Err.Description
    Set objApplication = Nothing
    Set objAppCollection = Nothing
    Set objCatalog = Nothing
End Function

```



To use the function, provide a string value for the application name and integer values for the desired application recycling settings. The following Visual Basic code shows how to set the **RecycleLifetimeLimit** value to 5, the **RecycleMemoryLimit** value to 10, the **RecycleCallLimit** value to 9, the **RecycleActivationLimit** value to 100, and the **RecycleExpirationTimeout** value to 15.


```VB
Sub Main()
    If Not SetMyApplicationRecycling("MyApp", 5, 10, 9, 100, 15) Then
        MsgBox "SetMyApplicationRecycling failed."
    End If
End Sub

```



## Related topics

<dl> <dt>

[COM+ Application Recycling Concepts](com--application-recycling-concepts.md)
</dt> </dl>

 

 



