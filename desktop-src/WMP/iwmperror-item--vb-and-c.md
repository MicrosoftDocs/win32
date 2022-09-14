---
title: IWMPError.Item (VB and C )
description: The Item property (the get\_Item method in C\ ) gets an IWMPErrorItem interface at the specified index in the error queue.
ms.assetid: acfaaaa5-eb13-4ba0-8417-4229adc62c5d
keywords:
- IWMPError.Item (VB and C ) Windows Media Player
topic_type:
- apiref
api_name:
- IWMPError.Item (VB and C )
api_location:
- Interop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPError.Item (VB and C#)

The **Item** property (the **get\_Item** method in C#) gets an **IWMPErrorItem** interface at the specified index in the error queue.


```
[Visual Basic]
ReadOnly Property Item(
  dwIndex As System.Integer
) As IWMPErrorItem
```




```
[C#]
IWMPErrorItem get_Item (
  System.Int32 dwIndex
);
```



## Parameters

*dwIndex*

A **System.Int32** that is the zero-based index of an **IWMPErrorItem** interface in the error queue.

## Property Value

A **WMPLib.IWMPErrorItem** interface.

## Remarks

Windows Media Player can generate a number of errors in response to an error condition. This property gets a specific error in the queue by using an index number. The index numbers for the error queue begin with zero.

You should set **IWMPSettings.enableErrorDialogs** to **false** if you choose to display custom error messages.

## Examples

The following example uses the **Item** property (the **get\_Item** method in C#) in an Error event handler to retrieve and display information about the most recent error in the error queue. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
private void player_ErrorEvent_get_Item(object sender, System.EventArgs e)
{
    // Store the index of the most recent error.
    int max = (player.Error.errorCount - 1);

    // Get an interface for the most recent error item. Cast it to
    // a WMPLib.IWMPErrorItem2 interface to get all of the available functionality.
    WMPLib.IWMPErrorItem2 errItem = (WMPLib.IWMPErrorItem2)player.Error.get_Item(max);

    // Use the interface to access and store the error info.
    int errNum = errItem.errorCode;
    string errDesc = errItem.errorDescription;

    // Display the error info.
    System.Windows.Forms.MessageBox.Show(errNum.ToString() + ":  " + errDesc);
}
```


```VB

Public Sub player_ErrorEvent_get_Item(ByVal sender As Object, ByVal e As System.EventArgs) Handles player.ErrorEvent

    &#39; Store the index of the most recent error.
    Dim max As Integer = (player.Error.errorCount - 1)

    &#39; Get an interface for the most recent error item. 
    Dim errItem As WMPLib.IWMPErrorItem2 = player.Error.Item(max)

    &#39; Use the interface to access and store the error info.
    Dim errNum As Integer = errItem.errorCode
    Dim errDesc As String = errItem.errorDescription

    &#39; Display the error info.
    System.Windows.Forms.MessageBox.Show(errNum.ToString() + &quot;:  &quot; + errDesc)

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

[**IWMPErrorItem Interface (VB and C#)**](iwmperroritem--vb-and-c.md)
</dt> <dt>

[**IWMPSettings.enableErrorDialogs (VB and C#)**](wmplibiwmpsettings-iwmpsettings-enableerrordialogs--vb-and-c.md)
</dt> </dl>

 

 





