---
title: ShowMessageAction.MessageBody property
description: For scripting, gets or sets the message text that is displayed in the body of the message box.
ms.assetid: '7166e379-95f0-43f1-93a0-6a3d706dd627'
keywords:
- MessageBody property Task Scheduler
- MessageBody property Task Scheduler , ShowMessageAction object
- ShowMessageAction object Task Scheduler , MessageBody property
topic_type:
- apiref
api_name:
- ShowMessageAction.MessageBody
api_location:
- taskschd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ShowMessageAction.MessageBody property

\[This object is no longer supported. You can use IExecAction with the Windows scripting [**MsgBox function**](/previous-versions/sfw6660x(v=vs.80)) to show a message in the user session.\]

For scripting, gets or sets the message text that is displayed in the body of the message box.

## Syntax


```VB
ShowMessageAction.MessageBody As String
```



## Property value

The message text that is displayed in the body of the message box.

## Remarks

Parameterized strings can be used in the message text of the message box. For more information, see the Examples section in [**EventTrigger.ValueQueries**](eventtrigger-valuequeries.md).

When setting this property value, the value can be text that is retrieved from a resource .dll file. A specialized string is used to reference the text from the resource file. The format of the string is $(@ \[Dll\], \[ResourceID\]) where \[Dll\] is the path to the .dll file that contains the resource and \[ResourceID\] is the identifier for the resource text. For example, the setting this property value to $(@ %SystemRoot%\\System32\\ResourceName.dll, -101) will set the property to the value of the resource text with an identifier equal to -101 in the %SystemRoot%\\System32\\ResourceName.dll file.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows 7<br/>                                                                    |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                       |
| Type library<br/>             | <dl> <dt>Taskschd.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Taskschd.dll</dt> </dl> |



## See also

<dl> <dt>

[**ShowMessageAction**](showmessageaction.md)
</dt> </dl>

 

