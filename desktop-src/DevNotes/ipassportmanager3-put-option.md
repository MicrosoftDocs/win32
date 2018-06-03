---
Description: Sets a specific Microsoft .NET Passport sign-in option.
ms.assetid: 5ec79faa-1c74-42a4-b964-ea15edacda79
title: IPassportManager3::put\_Option method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPassportManager3::put\_Option method

Sets a specific Microsoft .NET Passport sign-in option.

> [!Note]  
> The **put\_Option** method belongs to the [**IPassportManager3**](https://www.bing.com/search?q=**IPassportManager3**) interface. This topic supplements the initial documentation.

 

## Syntax


```C++
HRESULT put_Option(
   BSTR    name,
   VARIANT newVal
);
```



## Parameters

<dl> <dt>

*name* 
</dt> <dd>

The sign-in option to be set. Currently, the only supported option is iMode.

</dd> <dt>

*newVal* 
</dt> <dd>

A **VARIANT** (VT\_BOOL) that specifies the new value for the option. This value can be True or False.

</dd> </dl>

## Return value

Returns S\_OK when the method succeeds.

## Remarks

This method ships with older versions of the Passport SDK.

 

 



