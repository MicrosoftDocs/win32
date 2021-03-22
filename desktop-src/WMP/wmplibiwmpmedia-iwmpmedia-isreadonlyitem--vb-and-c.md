---
title: IWMPMedia isReadOnlyItem method
description: The isReadOnlyItem method returns a value indicating whether the attributes of the specified media item can be edited.
ms.assetid: c810c5c1-8cb9-4ac7-ac49-1ebdc86f5d7f
keywords:
- isReadOnlyItem method Windows Media Player
- isReadOnlyItem method Windows Media Player , IWMPMedia interface
- IWMPMedia interface Windows Media Player , isReadOnlyItem method
topic_type:
- apiref
api_name:
- IWMPMedia.isReadOnlyItem
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPMedia::isReadOnlyItem method

The **isReadOnlyItem** method returns a value indicating whether the attributes of the specified media item can be edited.

## Syntax


```CSharp
public System.Boolean isReadOnlyItem(
  System.String bstrItemName
);
```


```VB

Public Function isReadOnlyItem( _
  ByVal bstrItemName As System.String _
) As System.Boolean
Implements IWMPMedia.isReadOnlyItem
```





## Parameters

<dl> <dt>

*bstrItemName* \[in\]
</dt> <dd>

A **System.String** that is the name of the media item.

</dd> </dl>

## Return value

A **System.Boolean** value that indicates whether the attributes are read-only.

## Remarks

If an attribute is read-only, then it cannot be set with the **setItemInfo** method. Note that this method may return different values for a particular attribute when used with different versions of Windows Media Player.

Before calling this method, you must have read access to the library. For more information, see [Library Access](library-access.md).

## Examples

The following example uses **isReadOnlyItem** to fill a multi-line text box with information about the current media item. The code displays each attribute of the current media item, along with text indicating whether the attribute is read-only or read/write. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
// Store a WMPLib.IWMPMedia3 interface to the current media item.
WMPLib.IWMPMedia3 cm = (WMPLib.IWMPMedia3)player.currentMedia;

// Get the number of attributes in the current media item.
int attCount = player.currentMedia.attributeCount;

// Create an array to store the list of attribute information.
string[] atInfo = new string[attCount];

// Create a variable to hold each attribute name.
string atName;

// Loop through the attribute list.
for (int i = 0; i < cm.attributeCount; i++)
{
    // Get the attribute name.
    atName = cm.getAttributeName(i);

    // Test whether the attribute is read-only.
    string test = ((cm.isReadOnlyItem(atName)) ? "Read-Only" : "Read/Write");

    // Store the attribute information in the array.
    atInfo[i] = (atName + " is " + test);
}

// Display the attribute information in the text box.
rwText.Lines = atInfo;
```


```VB

' Store a WMPLib.IWMPMedia3 interface to the current media item.
Dim cm As WMPLib.IWMPMedia3 = player.currentMedia

&#39; Get the number of attributes in the current media item.
Dim attCount As Integer = player.currentMedia.attributeCount

&#39; Create an array to store the list of attribute information.
Dim atInfo(attCount) As String

&#39; Create a variable to hold each attribute name.
Dim atName As String

&#39; Loop through the attribute list.
For i As Integer = 0 To (cm.attributeCount - 1)

    &#39; Get the attribute name.
    atName = cm.getAttributeName(i)

    &#39; Test whether the attribute is read-only.
    If (cm.isReadOnlyItem(atName)) Then

        atInfo(i) = (atName + &quot; is Read-Only&quot;)

    Else

        atInfo(i) = (atName + &quot; is Read/Write&quot;)

    End If

Next i

&#39; Display the attribute information in the text box.
rwText.Lines = atInfo
```





## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPMedia Interface (VB and C#)**](iwmpmedia--vb-and-c.md)
</dt> <dt>

[**IWMPMedia.setItemInfo (VB and C#)**](wmplibiwmpmedia-iwmpmedia-setiteminfo--vb-and-c.md)
</dt> </dl>

 

 





