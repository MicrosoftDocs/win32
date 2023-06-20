---
title: IWMPMediaCollection getAttributeStringCollection method
description: The getAttributeStringCollection method returns an IWMPStringCollection interface that represents the set of all values for a specified attribute within a media type.
ms.assetid: 5ac19c04-75db-4618-9c4e-b20e2f709024
keywords:
- getAttributeStringCollection method Windows Media Player
- getAttributeStringCollection method Windows Media Player , IWMPMediaCollection interface
- IWMPMediaCollection interface Windows Media Player , getAttributeStringCollection method
topic_type:
- apiref
api_name:
- IWMPMediaCollection.getAttributeStringCollection
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPMediaCollection::getAttributeStringCollection method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getAttributeStringCollection** method returns an **IWMPStringCollection** interface that represents the set of all values for a specified attribute within a media type.

## Syntax


```CSharp
public IWMPStringCollection getAttributeStringCollection(
  System.String bstrAttribute,
  System.String bstrMediaType
);
```


```VB

Public Function getAttributeStringCollection( _
  ByVal bstrAttribute As System.String, _
  ByVal bstrMediaType As System.String _
) As IWMPStringCollection
Implements IWMPMediaCollection.getAttributeStringCollection
```





## Parameters

<dl> <dt>

*bstrAttribute* \[in\]
</dt> <dd>

A **System.String** that is the attribute for which the values are retrieved.

</dd> <dt>

*bstrMediaType* \[in\]
</dt> <dd>

A **System.String** that is the media type for which the values are retrieved.

</dd> </dl>

## Return value

A **WMPLib.IWMPStringCollection** interface for the retrieved values.

## Remarks

Before calling this method, you must have read access to the library. For more information, see [Library Access](library-access.md).

For information about the attributes supported by Windows Media Player, see the [Attribute Reference](attribute-reference.md).

## Examples

The following example uses **getAttributeStringCollection** to display a list of values that correspond to a particular attribute for audio items in the media collection. A list box allows the user to select an attribute, such as Artist, Genre, or Album and a multi-line text box displays the result. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
private void audioAttributes_OnSelectedIndexChanged(object sender, System.EventArgs e)
{
    // Retrieve the attribute type from the ListBox
    string attributeType = (string)((System.Windows.Forms.ListBox)sender).SelectedItem;

    // Get an interface to the mediaCollection.  
    WMPLib.IWMPMediaCollection2 library = (WMPLib.IWMPMediaCollection2)player.mediaCollection;

    // Get an interface to the string collection for the attribute type the user selects.
    WMPLib.IWMPStringCollection2 all = (WMPLib.IWMPStringCollection2)library.getAttributeStringCollection(attributeType, "Audio");

    // Clear the text box of previous results.
    attributeValues.Clear();

    // Create an array to hold the attribute values.
    string[] attributeArray = new string[all.count];
    
    // Loop through the string collection.
    for (int i = 0; i < all.count; i++)
    {
        // Store the items in the array.
        attributeArray[i] = all.Item(i);
    }

    // Display the items in the text box.
    attributeValues.Lines = attributeArray;
}
```


```VB

Public Sub audioAttributes_OnSelectedIndexChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles audioAttributes.SelectedIndexChanged

    &#39; Retrieve the attribute type from the ListBox
    Dim lb As System.Windows.Forms.ListBox = sender
    Dim attributeType As String = lb.SelectedItem

    &#39; Get an interface to the mediaCollection.  
    Dim library As WMPLib.IWMPMediaCollection2 = player.mediaCollection

    &#39; Get an interface to the string collection for the attribute type the user selects.
    Dim all As WMPLib.IWMPStringCollection2 = library.getAttributeStringCollection(attributeType, &quot;Audio&quot;)

    &#39; Clear the text box of previous results.
    attributeValues.Clear()

    &#39; Create an array to hold the attribute values.
    Dim attributeArray(all.count) As String

    &#39; Loop through the string collection.
    For i As Integer = 0 To (all.count - 1)

        &#39; Store the items in the array.
        attributeArray(i) = all.Item(i)

    Next i

    &#39; Display the items in the text box.
    attributeValues.Lines = attributeArray

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

[**IWMPMediaCollection Interface (VB and C#)**](iwmpmediacollection--vb-and-c.md)
</dt> <dt>

[**IWMPStringCollection Interface (VB and C#)**](iwmpstringcollection--vb-and-c.md)
</dt> </dl>

 

 





