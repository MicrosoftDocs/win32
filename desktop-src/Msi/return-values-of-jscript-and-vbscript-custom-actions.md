---
description: Custom actions written in JScript or Visual Basic, Scripting Edition (VBScript) can call an optional function. These functions must return one of the values shown in the following table.
ms.assetid: f05d0b94-e79e-440e-9f2b-99fe0e9e2646
title: Return Values of JScript and VBScript Custom Actions
ms.topic: article
ms.date: 05/31/2018
---

# Return Values of JScript and VBScript Custom Actions

Custom actions written in JScript or Visual Basic, Scripting Edition (VBScript) can call an optional function. These functions must return one of the values shown in the following table.



| Return value              | Value        | Description                                                                                                |
|---------------------------|--------------|------------------------------------------------------------------------------------------------------------|
| msiDoActionStatusNoAction | 0            | Action not executed.                                                                                       |
| msiDoActionStatusSuccess  | IDOK = 1     | Action completed successfully.                                                                             |
| msiDoActionStatusUserExit | IDCANCEL = 2 | Premature termination by user.                                                                             |
| msiDoActionStatusFailure  | IDABORT = 3  | Unrecoverable error. Returned if there is an error during parsing or execution of the JScript or VBScript. |
| msiDoActionStatusSuspend  | IDRETRY = 4  | Suspended sequence to be resumed later.                                                                    |
| msiDoActionStatusFinished | IDIGNORE = 5 | Skip remaining actions. Not an error.                                                                      |



 

Note that Windows Installer translates the return values from all actions when it writes the return value into the log file. For example, if the action return value appears as 1 (one) in the log file, this means that the action returned msiDoActionStatusSuccess. For more information about this translation see [Logging of Action Return Values](logging-of-action-return-values.md).

To return a value other than success from a script custom action, you must use a function target for the custom action. The target function is specified in the Target column of the [CustomAction Table](customaction-table.md).

The following script example shows you how to return success or failure from a VBScript custom action.


```VB
Function MyVBScriptCA()

    If Session.Property("CustomErrorStatus") <> "0" Then
        'return error
        MyVBScriptCA = 3
        Exit Function
    End If

    ' return success
    MyVBScriptCA = 1
    Exit Function

End Function
```



If this VBScript were embedded in the [Binary table](binary-table.md) of the installation package as MyCA.vbs, the [CustomAction Table](customaction-table.md) entry for the script would be the following:



| Action         | Type | Source   | Target       |
|----------------|------|----------|--------------|
| MyCustomAction | 6    | MyCA.vbs | MyVBScriptCA |



 

 

 



