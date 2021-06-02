---
description: ICE52 checks for private properties in the AppSearch table. See About Properties.
ms.assetid: 18d1489e-666a-488d-ae12-5dbe60885a2e
title: ICE52
ms.topic: article
ms.date: 05/31/2018
---

# ICE52

ICE52 checks for private properties in the [AppSearch table](appsearch-table.md). See [About Properties](about-properties.md).

When using Windows 2000 all properties set in the Property column of the AppSearch table must be public properties.

## Result

ICE52 posts a warning if there is a private property in the AppSearch table.

## Example

ICE52 posts the following warning for the example shown.

``` syntax
Property 'Property2' in AppSearch row 'Property2'.'Signature2' 
    is not public. It should be all uppercase.
```

[AppSearch Table](appsearch-table.md)



| Property  | Signature  |
|-----------|------------|
| PROPERTY1 | Signature1 |
| Property2 | Signature2 |



 

To fix this warning change to the custom public property: PROPERTY2.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



