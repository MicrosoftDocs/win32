---
description: The following example demonstrates aspects of working with the Store object. It shows opening stores in the CAPICOM\_MEMORY\_STORE, CAPICOM\_CURRENT\_USER\_STORE, and CAPICOM\_LOCAL\_MACHINE\_STORE locations.
ms.assetid: bfb7ff48-1d6b-404f-9dd4-6de1898354b7
title: Using Stores in Different Locations
ms.topic: article
ms.date: 05/31/2018
---

# Using Stores in Different Locations

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the .NET Framework to implement security features. For more information, see [Alternatives to Using CAPICOM](alternatives-to-using-capicom.md).\]

The following example demonstrates aspects of working with the [**Store**](store.md) object. It shows opening stores in the CAPICOM\_MEMORY\_STORE, CAPICOM\_CURRENT\_USER\_STORE, and CAPICOM\_LOCAL\_MACHINE\_STORE locations.

The example shows exporting [*certificates*](../secgloss/c-gly.md) from an open [*store*](../secgloss/c-gly.md), writing the exported certificates to a file, reading them back in and importing them into a different store. The newly imported certificates are then enumerated and displayed.

On any CAPICOM error, a negative decimal value of **Err.Number** is returned. For more information, see [**CAPICOM\_ERROR\_CODE**](capicom-error-code.md). For information about positive decimal values of **Err.Number**, see Winerror.h.


```VB
Sub OpenStores()

    On Error GoTo ErrorHandler

    'Open Memory, current user, and local machine stores
    Dim MemoryStore As New Store
    Dim CurrentUserStore As New Store
    Dim LocalMachineStore As New Store
    Dim NumCerts As Integer

    MemoryStore.Open(CAPICOM_MEMORY_STORE, "MemStore", _
        CAPICOM_STORE_OPEN_READ_WRITE)
    CurrentUserStore.Open(CAPICOM_CURRENT_USER_STORE, _
        CAPICOM_MY_STORE, CAPICOM_STORE_OPEN_READ_ONLY)
    LocalMachineStore.Open(CAPICOM_LOCAL_MACHINE_STORE, _
        CAPICOM_CA_STORE, CAPICOM_STORE_OPEN_READ_ONLY)

    ' Check the number of certificates in the stores.
    NumCerts = MemoryStore.Certificates.Count
    MsgBox("There are " & NumCerts & _
        " certificates in the memory store. ")
    NumCerts = CurrentUserStore.Certificates.Count
    MsgBox("There are " & NumCerts & _
        " certificates in the current user store. ")
    NumCerts = LocalMachineStore.Certificates.Count
    MsgBox("There are " & NumCerts & _
        " certificates in the local machine store. ")


    '  Export the certificates in the current user MY store
    '  to a file.
    Dim ExportString As String
    ExportString = CurrentUserStore.Export
Open "Exportcerts.txt" For Output As #1
Write #1, ExportString
Close #1

    ' Read the store the file.
    Dim importString As String
Open "exportcerts.txt" For Input As #2
Input #2, importString
Close #2
    MemoryStore.Import(importString)

    ' Check the number of certificates in the memory store after 
    ' import()
    NumCerts = MemoryStore.Certificates.Count
    MsgBox("There are " & NumCerts & _
        " certificates now in the memory store. ")

    ' Enumerate the certificates in the memory store and display each
    ' certificate
    Dim i As Long
    For i = 1 To NumCerts
        MemoryStore.Certificates.Item(i).Display()
    Next i

    ' Release the store objects
    MemoryStore = Nothing
    CurrentUserStore = Nothing
    LocalMachineStore = Nothing
    Exit Sub
ErrorHandler:
    If Err.Number > 0 Then
        MsgBox("Visual Basic error found: " & Err.Description)
    Else
        MsgBox("CAPICOM error found : " & Err.Number)
    End If
End Sub
```



 

 
