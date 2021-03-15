---
title: IWMPNetwork setProxyPort method
description: The setProxyPort method specifies the proxy port to use. | IWMPNetwork setProxyPort method
ms.assetid: df4b33f6-52b5-437f-ade2-0d08ca2878a9
keywords:
- setProxyPort method Windows Media Player
- setProxyPort method Windows Media Player , IWMPNetwork interface
- IWMPNetwork interface Windows Media Player , setProxyPort method
topic_type:
- apiref
api_name:
- IWMPNetwork.setProxyPort
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPNetwork::setProxyPort method

The **setProxyPort** method specifies the proxy port to use.

## Syntax


```CSharp
public void setProxyPort(
  System.String bstrProtocol,
  System.Int32 lProxyPort
);
```


```VB

Public Sub setProxyPort( _
  ByVal bstrProtocol As System.String, _
  ByVal lProxyPort As System.Int32 _
)
Implements IWMPNetwork.setProxyPort
```





## Parameters

<dl> <dt>

*bstrProtocol* \[in\]
</dt> <dd>

A **System.String** that is the protocol name. For a list of supported protocols, see [Supported Protocols and File Types](supported-protocols-and-file-types.md).

</dd> <dt>

*lProxyPort* \[in\]
</dt> <dd>

A **System.Int32** that is the proxy port to use.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method has no effect unless the value retrieved from **IWMPNetwork.getProxySettings** is 2 (use manual settings).

This method fails unless the calling application is running on the local computer or intranet.

## Examples

The following code example uses **setProxyPort** to specify the Windows Media Player proxy port number for the MMS protocol. The port number is retrieved from a text box when a button is clicked. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
private void setProxyPort_Click(object sender, System.EventArgs e)
{
    // Test whether proxy settings are manual.
    if (player.network.getProxySettings("MMS") == 2)
    {
        // Store the user's new proxy port number.
        int portnumber = System.Convert.ToInt32(portText.Text);

        // Set the proxy port.
        player.network.setProxyPort("MMS", portnumber);
    }
    else
    {
        // Warn that the proxy settings must be set to 2 (manual).
        System.Windows.Forms.MessageBox.Show("Proxy settings must be manual!");
    }
}
```


```VB

Public Sub setProxyPort_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles setProxyPort.Click

    &#39; Test whether proxy settings are manual.
    If (player.network.getProxySettings(&quot;MMS&quot;) = 2) Then

        &#39; Store the user&#39;s new proxy port number.
        Dim portnumber As Integer = System.Convert.ToInt32(portText.Text)

        &#39; Set the proxy port.
        player.network.setProxyPort(&quot;MMS&quot;, portnumber)

    Else

        &#39; Warn that the proxy settings must be set to 2 (manual).
        System.Windows.Forms.MessageBox.Show(&quot;Proxy settings must be manual!&quot;)

    End If

End Sub
```





## Requirements



|                      |                                                                                                                        |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPNetwork Interface (VB and C#)**](iwmpnetwork--vb-and-c.md)
</dt> <dt>

[**IWMPNetwork.getProxyPort (VB and C#)**](wmplibiwmpnetwork-iwmpnetwork-getproxyport--vb-and-c.md)
</dt> <dt>

[**IWMPNetwork.getProxySettings (VB and C#)**](wmplibiwmpnetwork-iwmpnetwork-getproxysettings--vb-and-c.md)
</dt> </dl>

 

 





