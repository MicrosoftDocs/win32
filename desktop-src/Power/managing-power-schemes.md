---
description: Power Scheme Management
ms.assetid: b79e7b64-be56-4165-af59-a8251284d029
title: Power Scheme Management
ms.topic: article
ms.date: 05/31/2018
---

# Power Scheme Management

Each power scheme is uniquely identified by a **GUID**. To enumerate all available power schemes, use the [**PowerEnumerate**](/windows/desktop/api/PowrProf/nf-powrprof-powerenumerate) function. **PowerEnumerate** can also be used to retrieve all of the power settings for a specified scheme.

The power scheme that is currently in use on the system is called the active power scheme or plan. To retrieve the **GUID** of the active plan, call the [**PowerGetActiveScheme**](/windows/desktop/api/Powersetting/nf-powersetting-powergetactivescheme) function. To change the active power plan, call the [**PowerSetActiveScheme**](/windows/desktop/api/Powersetting/nf-powersetting-powersetactivescheme) function.

To create a power scheme, you need to first duplicate an existing scheme by using the [**PowerDuplicateScheme**](/windows/desktop/api/PowrProf/nf-powrprof-powerduplicatescheme) function, specifying the **GUID** of the scheme you wish to base your new scheme upon. You should copy one of the built-in schemes and modify the power settings to your needs. Note that creating a power plan does not automatically update the active power plan. You must always call [**PowerSetActiveScheme**](/windows/desktop/api/Powersetting/nf-powersetting-powersetactivescheme) to update the active power plan. Existing power plans can be modified and then applied in the same manner.

To remove a power plan, call the [**PowerDeleteScheme**](/windows/desktop/api/PowrProf/nf-powrprof-powerdeletescheme) function.

> [!Note]  
> To retrieve additional information about the system power state, call the [**CallNtPowerInformation**](/windows/desktop/api/Powerbase/nf-powerbase-callntpowerinformation) function.

 

## Related topics

<dl> <dt>

[Power Schemes](power-schemes.md)
</dt> </dl>

 

 



