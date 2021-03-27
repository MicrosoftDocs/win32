---
title: IWMPError errorCount property
description: The errorCount property gets the number of errors in the error queue.
ms.assetid: a30750c8-2025-4087-bd2b-f313ccbde38c
keywords:
- errorCount property Windows Media Player
- errorCount property Windows Media Player , IWMPError interface
- IWMPError interface Windows Media Player , errorCount property
topic_type:
- apiref
api_name:
- IWMPError.errorCount
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPError::errorCount property

The **errorCount** property gets the number of errors in the error queue.

## Syntax


```CSharp
public System.Int32 errorCount {get; set;}
```


```VB

Public ReadOnly Property errorCount As System.Int32
```





## Property value

A **System.Int32** that is the number of errors.

## Remarks

You should set **IWMPSettings.enableErrorDialogs** to **false** if you choose to display custom error messages.

## Examples

The following example uses **errorCount** in an Error event handler to alert the user about the most recent error in the error queue. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
private void player_ErrorEvent_errorCount(object sender, System.EventArgs e)
{
    // Store the number of errors in the queue.
    int max = player.Error.errorCount;

    // Get the description of the last error. Error items start at zero,
    // so the item index will always be one less than the error count.
    string errDesc = player.Error.get_Item(max-1).errorDescription;

    // Display the error description.
    System.Windows.Forms.MessageBox.Show(errDesc);
}
```


```VB

Public Sub player_ErrorEvent_errorCount(ByVal sender As Object, ByVal e As System.EventArgs) Handles player.ErrorEvent

    &#39; Store the number of errors in the queue.
    Dim max As Integer = player.Error.errorCount

    &#39; Get the description of the last error. Error items start at zero,
    &#39; so the item index will always be one less than the error count.
    Dim errDesc As String = player.Error.Item(max - 1).errorDescription

    &#39; Display the error description.
    System.Windows.Forms.MessageBox.Show(errDesc)

End Sub
```





## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPError Interface (VB and C#)**](iwmperror--vb-and-c.md)
</dt> <dt>

[**IWMPSettings.enableErrorDialogs (VB and C#)**](wmplibiwmpsettings-iwmpsettings-enableerrordialogs--vb-and-c.md)
</dt> </dl>

 

 





