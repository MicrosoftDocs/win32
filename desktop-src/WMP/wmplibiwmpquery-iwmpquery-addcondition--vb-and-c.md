---
title: IWMPQuery addCondition method
description: The addCondition method adds a condition to the compound query using AND logic.
ms.assetid: 4594ee6f-b153-4d53-b3ee-cd1718a4d5dc
keywords:
- addCondition method Windows Media Player
- addCondition method Windows Media Player , IWMPQuery interface
- IWMPQuery interface Windows Media Player , addCondition method
topic_type:
- apiref
api_name:
- IWMPQuery.addCondition
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPQuery::addCondition method

The **addCondition** method adds a condition to the compound query using **AND** logic.

## Syntax


```CSharp
public void addCondition(
  System.String bstrAttribute,
  System.String bstrOperator,
  System.String bstrValue
);
```


```VB

Public Sub addCondition( _
  ByVal bstrAttribute As System.String, _
  ByVal bstrOperator As System.String, _
  ByVal bstrValue As System.String _
)
Implements IWMPQuery.addCondition
```





## Parameters

<dl> <dt>

*bstrAttribute* \[in\]
</dt> <dd>

A **System.String** that is the name of the attribute to be added to the query.

</dd> <dt>

*bstrOperator* \[in\]
</dt> <dd>

A **System.String** that is the operator. See Remarks for supported values.

</dd> <dt>

*bstrValue* \[in\]
</dt> <dd>

A **System.String** that is the attribute value.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Conditions contained in a compound query are organized into condition groups. Multiple conditions within a condition group are always concatenated by using **AND** logic. Condition groups are always concatenated to each other by using **OR** logic. To start a new condition group, call [IWMPQuery.beginNextGroup](wmplibiwmpquery-iwmpquery-beginnextgroup--vb-and-c.md).

Compound queries using **IWMPQuery** are not case sensitive.

A list of values for the *bstrAttribute* parameter can be found in [Alphabetical Attribute Reference](alphabetical-attribute-reference.md).

The following table lists the supported values for *bstrOperator*.



| String              | Applies to     |
|---------------------|----------------|
| BeginsWith          | Strings        |
| Contains            | Strings        |
| Equals              | All types      |
| GreaterThan         | Numbers, Dates |
| GreaterThanOrEquals | Numbers, Dates |
| LessThan            | Numbers, Dates |
| LessThanOrEquals    | Numbers, Dates |
| NotBeginsWith       | Strings        |
| NotContains         | Strings        |
| NotEquals           | All types      |



 

## Examples

The following example creates a query, adds two conditions to it, and uses that query to extract the results of the query as a string collection. The results are then displayed in a list box. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
// Get a new Query interface.
WMPLib.IWMPMediaCollection2 mc = (WMPLib.IWMPMediaCollection2)player.mediaCollection;
WMPLib.IWMPQuery q = mc.createQuery();

// Add two conditions to the Query. 
q.addCondition("WM/Composer", "Equals", "Antonio Vivaldi");
q.addCondition("Title", "Contains", "Trio");

// Query the media collection and get a string collection containing the result.
// In this case, the string collection will contain the titles of all audio items that
// match the query.
WMPLib.IWMPStringCollection2 result = (WMPLib.IWMPStringCollection2)mc.getStringCollectionByQuery("Title", q, "audio", "", false);

// Display the results by adding them to a list box.
for (int i = 0; i < result.count; i++)
{
    queryResults.Items.Add(result.Item(i));
}
```


```VB

' Get a new Query interface.
Dim mc As WMPLib.IWMPMediaCollection2 = player.mediaCollection
Dim q As WMPLib.IWMPQuery = mc.createQuery()

&#39; Add two conditions to the Query. 
q.addCondition(&quot;WM/Composer&quot;, &quot;Equals&quot;, &quot;Antonio Vivaldi&quot;)
q.addCondition(&quot;Title&quot;, &quot;Contains&quot;, &quot;Trio&quot;)

&#39; Query the media collection and get a string collection containing the result.
&#39; In this case, the string collection will contain the titles of all audio items that
&#39; match the query.
Dim result As WMPLib.IWMPStringCollection2 = mc.getStringCollectionByQuery(&quot;Title&quot;, q, &quot;audio&quot;, &quot;&quot;, False)

&#39; Display the results by adding them to a list box.
For i As Integer = 0 To (result.count - 1)

    queryResults.Items.Add(result.Item(i))

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

[**Alphabetical Attribute Reference**](alphabetical-attribute-reference.md)
</dt> <dt>

[**IWMPMediaCollection2.createQuery (VB and C#)**](wmplibiwmpmediacollection2-iwmpmediacollection2-createquery--vb-and-c.md)
</dt> <dt>

[**IWMPMediaCollection2.getPlaylistByQuery (VB and C#)**](wmplibiwmpmediacollection2-iwmpmediacollection2-getplaylistbyquery--vb-and-c.md)
</dt> <dt>

[**IWMPMediaCollection2.getStringCollectionByQuery (VB and C#)**](wmplibiwmpmediacollection2-iwmpmediacollection2-getstringcollectionbyquery--vb-and-c.md)
</dt> <dt>

[**IWMPQuery Interface**](iwmpquery--vb-and-c.md)
</dt> </dl>

 

 





