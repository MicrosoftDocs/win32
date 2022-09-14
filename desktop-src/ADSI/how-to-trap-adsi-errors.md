---
title: How to Trap ADSI Errors
description: VBScript only offers one way to trap errors inline error handling.
ms.assetid: 65379edf-54b0-475b-89ee-97d544d0d809
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# How to Trap ADSI Errors

VBScript only offers one way to trap errors: inline error handling. An inline error handler begins with the **On Error Resume Next** statement. Since **On Error Resume Next** will prevent any errors from stopping execution of the script until the end of the scope from which **On Error Resume Next** is called, you must check the value of **Err** at every point after the **On Error Resume Next** statement where you expect an error might occur. The following example demonstrates inline error handling in an ADSI script:


```VB
On Error Resume Next

Set myComputer = GetObject(computerPath)
If Err Then AdsiErr()

' Create the new user account
Set newUser = myComputer.Create("user", username)
newUser.SetInfo
If Err Then AdsiErr()

Sub AdsiErr()
    Dim s
    Dim e
    
    If Err.Number = &H8000500E Then
        WScript.Echo "The user " & username & " already exists."
    Elseif Err.Number = &H80005000 Then
        WScript.Echo "Computer " & computerPath & " not found.  Check the ADsPath and try again."
    Else
        e = Hex(Err.Number)
        WScript.Echo "Unexpected Error " & e & "(" & Err.Number & ")"
    End If
    WScript.Quit(1)

End Sub
```



After each location where the script is likely to encounter an error, there is an **If Err** statement. The **Err** object contains the error code of the last error that occurred during execution of the script; if no error has occurred, **Err** will always be zero (0). In the previous example, an error will cause execution to jump to the **AdsiErr** subroutine, which checks the value of **Err.Number** for expected errors. Instead of dying with a cryptic error message, the script will give a somewhat better explanation for why it stopped running.

Remember that within the scope in which **On Error Resume Next** is called, any error that occurs after the **On Error Resume Next** call will be ignored. This can actually make a script harder to debug if you forget to check the value of **Err** in appropriate locations. Wherever you expect an error to be likely, be sure to check the value of **Err**.

(When you are initially debugging the script you may want to simply let the script halt its execution and display the offending line number on an error, then add the error handlers after the basic program flow is correct.)

 

 




