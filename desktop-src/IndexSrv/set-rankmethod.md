---
title: SET RANKMETHOD
description: SET RANKMETHOD
ms.assetid: 'bcdeac05-13bf-42f5-9b3a-b0a18362505a'
---

# SET RANKMETHOD

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **SET RANKMETHOD** statement sets the ranking method you want to use when issuing queries.

``` syntax
<b>SET</b> <b>RANKMETHOD</b> <i>Method</i>
```

### Parameters

<dl> <dt>

<span id="Method"></span><span id="method"></span><span id="METHOD"></span>*Method*
</dt> <dd>

Specifies the ranking algorithm to use to evaluate the rank of a vector query match for content searching. The algorithm can be one of the following:

-   JACCARD COEFFICIENT (default)
-   DICE COEFFICIENT
-   INNER PRODUCT
-   MINIMUM
-   MAXIMUM

</dd> </dl>

### Remarks

The method specified by the **SET RANKMETHOD** statement lasts the duration of a session with Indexing Service unless a subsequent **SET RANKMETHOD** statement changes the method.

If the *Method* parameter specifies an algorithm that is not in the list of supported algorithms, the default algorithm (JACCARD COEFFICIENT) is used.

### Example

The following is an example of the **SET RANKMETHOD** statement.


```
SET RANKMETHOD DICE COEFFICIENT
```



## Related topics

<dl> <dt>

[SET PROPERTYNAME](set-propertyname.md)
</dt> <dt>

[SET Statement](set-statement.md)
</dt> </dl>

 

 




