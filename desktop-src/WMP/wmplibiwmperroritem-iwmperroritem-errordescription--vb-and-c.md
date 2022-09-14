---
title: IWMPErrorItem errorDescription property
description: The errorDescription property gets a description of the error.
ms.assetid: a9914c24-1d10-422a-bcba-80be9fb85108
keywords:
- errorDescription property Windows Media Player
- errorDescription property Windows Media Player , IWMPErrorItem interface
- IWMPErrorItem interface Windows Media Player , errorDescription property
topic_type:
- apiref
api_name:
- IWMPErrorItem.errorDescription
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPErrorItem::errorDescription property

The **errorDescription** property gets a description of the error.

## Syntax


```CSharp
public System.String errorDescription {get; set;}
```


```VB

Public ReadOnly Property errorDescription As System.String
```





## Property value

A **System.String** that is the error description.

## Remarks

You should set **IWMPSettings.enableErrorDialogs** to **false** if you choose to display custom error messages.

## Examples

The following example uses **errorDescription** in an Error event handler to display the error description to the user. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
private void player_ErrorEvent_errorDescription(object sender, System.EventArgs e)
{
    // Get the error description for the first error item.
    string errDesc = player.Error.get_Item(0).errorDescription;

    // Display the error description.
    System.Windows.Forms.MessageBox.Show("Error: " + errDesc);
}
```


```VB

Public Sub player_ErrorEvent_errorDescription(ByVal sender As Object, ByVal e As System.EventArgs) Handles player.ErrorEvent

    &#39; Get the error description for the first error item.
    Dim errDesc As String = player.Error.Item(0).errorDescription

    &#39; Display the error description.
    System.Windows.Forms.MessageBox.Show(&quot;Error: &quot; + errDesc)

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

[**IWMPErrorItem Interface (VB and C#)**](iwmperroritem--vb-and-c.md)
</dt> <dt>

[**IWMPSettings.enableErrorDialogs (VB and C#)**](wmplibiwmpsettings-iwmpsettings-enableerrordialogs--vb-and-c.md)
</dt> </dl>

 

 





