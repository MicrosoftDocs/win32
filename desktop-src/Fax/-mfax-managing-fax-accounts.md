---
Description: The following example shows how to add, remove and enumerate fax accounts.
ms.assetid: a7256ab7-07b0-4f08-8efb-c35af2ee5eea
title: Managing Fax Accounts
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Managing Fax Accounts

The following example shows how to add, remove and enumerate fax accounts.


```VB
    Private Sub Form_Load()
        Dim objFaxServer As New FAXCOMEXLib.FaxServer
        Dim objFaxAccSet As FAXCOMEXLib.FaxAccountSet
        Dim objFaxAccounts As FAXCOMEXLib.FaxAccounts
        Dim strAccountName As String

        'Error handling
        On Error GoTo Error_Handler

        'Connect to the fax server
        objFaxServer.Connect("")

        'Get the accountset object
        objFaxAccSet = objFaxServer.FaxAccountSet

        'Display the list of accounts 
        'Get the FaxAccounts object 
        objFaxAccounts = objFaxAccSet.GetAccounts()
        'Print the number of FaxAccounts
        MsgBox("Number of accounts: " & objFaxAccounts.Count)

        For i = 1 To objFaxAccounts.Count
            MsgBox(objFaxAccounts(i).AccountName)
        Next

        'add new account
        strAccountName = InputBox("Enter an account name (DomainName\UserName)?")
        objFaxAccSet.AddAccount(strAccountName)


        'now delete the same account
        objFaxAccSet.RemoveAccount(strAccountName)

Error_Handler:
        'Implement error handling at the end of your subroutine. This 
        'implementation is for demonstration purposes
        MsgBox("Error number: " & Hex(Err.Number) & ", " & Err.Description)

    End Sub
```



 

 



