---
description: The ReadyStateChange event is sent when the ReadyState property of the MSWebDVD control has changed.
ms.assetid: 814a09e1-2e85-4ea3-9135-8377dc2acf64
title: ReadyStateChange
ms.topic: reference
ms.date: 05/31/2018
---

# ReadyStateChange

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `ReadyStateChange` event is sent when the **ReadyState** property of the MSWebDVD control has changed.

``` syntax
ReadyStateChange(ReadyState)
```

## Parameters

<dl> <dt>

<span id="ReadyState"></span><span id="readystate"></span><span id="READYSTATE"></span>*ReadyState*
</dt> <dd>

Specifies the new value of the [**ReadyState**](readystate-property.md) property.



| Value | Description               |
|-------|---------------------------|
| 0     | READYSTATE\_UNINITIALIZED |
| 1     | READYSTATE\_LOADING       |
| 2     | READYSTATE\_LOADED        |
| 3     | READYSTATE\_INTERACTIVE   |
| 4     | READYSTATE\_COMPLETE      |



 

</dd> </dl>

 

 



