---
description: The AcceptParentalLevelChange method accepts or rejects the new temporary parental management level.
ms.assetid: b3d58069-16dc-4598-90ea-6136c2f62ac7
title: AcceptParentalLevelChange Method
ms.topic: reference
ms.date: 05/31/2018
---

# AcceptParentalLevelChange Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The AcceptParentalLevelChange method accepts or rejects the new temporary parental management level.

``` syntax
        MSWebDVD.AcceptParentalLevelChange(bAccept)
```

## Parameters

<dl> <dt>

<span id="bAccept"></span><span id="baccept"></span><span id="BACCEPT"></span>*bAccept*
</dt> <dd>

Specifies the new parental level as a Boolean value.



| Value | Description                               |
|-------|-------------------------------------------|
| true  | Accept the new parental management level. |
| false | Reject the new parental management level. |



 

</dd> </dl>

## Return Value

No return value.

## Remarks

Call this method in response to an EC\_DVD\_PARENTAL\_LEVEL\_CHANGE event notification to specify whether the DVD Navigator should play the content with the new parental level, or branch to where the disc specifies if the new level is rejected.

## See also

<dl> <dt>

[Enforcing Parental Management Levels](enforcing-parental-management-levels.md)
</dt> <dt>

[**GetPlayerParentalCountry**](getplayerparentalcountry-method.md)
</dt> <dt>

[**GetPlayerParentalLevel**](getplayerparentallevel-method.md)
</dt> <dt>

[**GetTitleParentalLevels**](gettitleparentallevels-method.md)
</dt> <dt>

[**NotifyParentalLevelChange**](notifyparentallevelchange-method.md)
</dt> <dt>

[**SelectParentalCountry**](selectparentalcountry-method.md)
</dt> <dt>

[**SelectParentalLevel**](selectparentallevel-method.md)
</dt> </dl>

 

 



