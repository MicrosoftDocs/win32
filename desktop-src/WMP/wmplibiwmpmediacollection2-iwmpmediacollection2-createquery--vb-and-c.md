---
title: IWMPMediaCollection2 createQuery method
description: The createQuery method returns an IWMPQuery interface that represents a new query.
ms.assetid: a12da325-e77e-4e44-93d1-5e9c5733ea44
keywords:
- createQuery method Windows Media Player
- createQuery method Windows Media Player , IWMPMediaCollection2 interface
- IWMPMediaCollection2 interface Windows Media Player , createQuery method
topic_type:
- apiref
api_name:
- IWMPMediaCollection2.createQuery
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPMediaCollection2::createQuery method

The `createQuery` method returns an **IWMPQuery** interface that represents a new query.

## Syntax


```CSharp
public IWMPQuery createQuery();
```


```VB

Public Function createQuery() As IWMPQuery
Implements IWMPMediaCollection2.createQuery
```





## Parameters

This method has no parameters.

## Return value

A **WMPLib.IWMPQuery** interface that represents a new, empty query.

## Remarks

Creating a new query is the first step toward creating a compound query.

## Examples

The following example uses `createQuery` to get an **IWMPQuery** interface that is initialized to null. Because this query has no conditions added to it, when it is used as an argument in the **getStringCollectionByQuery** method, the method will return a string collection that contains all of the media items of the specified media type. The string collection is then displayed in a list box.


```CSharp
// Get an IWMPMediaCollection2 interface so that you can access the createQuery and
// getStringCollectionByQuery methods.
WMPLib.IWMPMediaCollection2 mc = (WMPLib.IWMPMediaCollection2)player.mediaCollection;

// Create an IWMPQuery interface with no conditions added to it.
WMPLib.IWMPQuery nullQuery = mc.createQuery();

// Get a string collection that contains the titles of all the audio items in the media
// collection.
WMPLib.IWMPStringCollection2 allTitles = (WMPLib.IWMPStringCollection2)mc.getStringCollectionByQuery("Title", nullQuery, "audio", "", false);

// Display the titles by adding them to a list box.
for (int i = 0; i < allTitles.count; i++)
{
    queryResults.Items.Add(allTitles.Item(i));
}
```


```VB

' Get an IWMPMediaCollection2 interface so that you can access
&#39; the createQuery and getStringCollectionByQuery methods.
Dim mc As WMPLib.IWMPMediaCollection2 = player.mediaCollection

&#39; Create an IWMPQuery interface with no conditions added to it.
Dim nullQuery As WMPLib.IWMPQuery = mc.createQuery()

&#39; Get a string collection that contains the titles of all the audio items in the media
&#39; collection
Dim allTitles As WMPLib.IWMPStringCollection2 = mc.getStringCollectionByQuery(&quot;Title&quot;, nullQuery, &quot;audio&quot;, &quot;&quot;, False)

&#39; Display the titles by adding them to a ListBox
For i As Integer = 0 To (allTitles.count - 1)

    queryResults.Items.Add(allTitles.Item(i))

Next i
```





## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPMediaCollection2 Interface (VB and C#)**](iwmpmediacollection2--vb-and-c.md)
</dt> <dt>

[**IWMPQuery Interface (VB and C#)**](iwmpquery--vb-and-c.md)
</dt> </dl>

 

 





