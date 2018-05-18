---
Description: Power Scheme Management
ms.assetid: 'b79e7b64-be56-4165-af59-a8251284d029'
title: Power Scheme Management
---

# Power Scheme Management

Each power scheme is uniquely identified by a **GUID**. To enumerate all available power schemes, use the [**PowerEnumerate**](powerenumerate.md) function. **PowerEnumerate** can also be used to retrieve all of the power settings for a specified scheme.

The power scheme that is currently in use on the system is called the active power scheme or plan. To retrieve the **GUID** of the active plan, call the [**PowerGetActiveScheme**](powergetactivescheme.md) function. To change the active power plan, call the [**PowerSetActiveScheme**](powersetactivescheme.md) function.

To create a power scheme, you need to first duplicate an existing scheme by using the [**PowerDuplicateScheme**](powerduplicatescheme.md) function, specifying the **GUID** of the scheme you wish to base your new scheme upon. You should copy one of the built-in schemes and modify the power settings to your needs. Note that creating a power plan does not automatically update the active power plan. You must always call [**PowerSetActiveScheme**](powersetactivescheme.md) to update the active power plan. Existing power plans can be modified and then applied in the same manner.

To remove a power plan, call the [**PowerDeleteScheme**](powerdeletescheme.md) function.

> [!Note]  
> To retrieve additional information about the system power state, call the [**CallNtPowerInformation**](callntpowerinformation.md) function.

 

## Related topics

<dl> <dt>

[Power Schemes](power-schemes.md)
</dt> </dl>

 

 



