---
title: IWMPNetwork bufferingTime property
description: The bufferingTime property gets or sets the amount of time in milliseconds allocated for buffering incoming data before playback begins.
ms.assetid: b5936b21-a17b-4801-a5fc-c6d6521e05aa
keywords:
- bufferingTime property Windows Media Player
- bufferingTime property Windows Media Player , IWMPNetwork interface
- IWMPNetwork interface Windows Media Player , bufferingTime property
topic_type:
- apiref
api_name:
- IWMPNetwork.bufferingTime
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPNetwork::bufferingTime property

The **bufferingTime** property gets or sets the amount of time in milliseconds allocated for buffering incoming data before playback begins.

## Syntax


```CSharp
public System.Int32 bufferingTime {get; set;}
```


```VB

Public Property bufferingTime As System.Int32
```





## Property value

A **System.Int32** that is the buffering time in milliseconds, which ranges from zero to 60,000 with a default value of 5,000.

## Examples

The following code example uses **bufferingTime** to specify the number of seconds allocated for buffering incoming data. A text box allows the user to enter a new value for **bufferingTime**, and the property is updated in response to the Click event of a button. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
private void setBufTime_Click(object sender, System.EventArgs e)
{
    // Retrieve input from the user and convert it to an integer.
    int newTime = System.Convert.ToInt32(bufText.Text);

    // Test whether the integer is within the valid range. 
    if (newTime >= 0 & newTime <= 60) 
    {
        // Set the new bufferingTime in miliseconds.
        player.network.bufferingTime = (newTime * 1000);
    }
    else
    {
        System.Windows.Forms.MessageBox.Show("Buffering time must be between 0 and 60.");
    }
}
```


```VB

Public Sub setBufTime_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles setBufTime.Click

    &#39; Retrieve input from the user and convert it to an integer.
    Dim newTime As Integer = System.Convert.ToInt32(bufText.Text)

    &#39; Test whether the integer is within the valid range. 
    If (newTime >= 0 And newTime <= 60) Then

        &#39; Set the new bufferingTime in miliseconds.
        player.network.bufferingTime = (newTime * 1000)

    Else

        System.Windows.Forms.MessageBox.Show(&quot;Buffering time must be between 0 and 60.&quot;)

    End If

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

[**IWMPNetwork Interface (VB and C#)**](iwmpnetwork--vb-and-c.md)
</dt> </dl>

 

 





