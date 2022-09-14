---
title: AxWindowsMediaPlayer.launchURL method
description: The launchURL method sends a URL to the user's default browser to be rendered. | AxWindowsMediaPlayer.launchURL method
ms.assetid: 3e8dfdbb-b5ad-44ea-97a6-e860386b7fb4
keywords:
- launchURL method Windows Media Player
- launchURL method Windows Media Player , AxWindowsMediaPlayer class
- AxWindowsMediaPlayer class Windows Media Player , launchURL method
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.launchURL
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# AxWindowsMediaPlayer.launchURL method

The launchURL method sends a URL to the user's default browser to be rendered.

## Syntax


```CSharp
public void launchURL(
  System.String bstrURL
);
```


```VB

Public Sub launchURL( _
  ByVal bstrURL As System.String _
)
```





## Parameters

<dl> <dt>

*bstrURL* 
</dt> <dd>

The **System.String** that is the URL to launch.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method only opens webpages using the HTTP or HTTPS protocols.

## Examples

The following example creates a button that, when clicked, displays the Microsoft website in a new browser window. The AxWMPLib.AxWindowsMediaPlayer object is represented by the variable named player.


```CSharp
private void goToMS_Click(object sender, System.EventArgs e)
{
    // Open the Microsoft website. 
    player.launchURL("https://www.microsoft.com");
}
```


```VB

Public Sub goToMS_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles goToMS.Click

    &#39; Open the Microsoft website. 
    player.launchURL(&quot;https://www.microsoft.com&quot;)

End Sub
```





## Requirements



| Requirement | Value |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                          |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                                    |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib.dll (AxInterop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> </dl>

 

 





