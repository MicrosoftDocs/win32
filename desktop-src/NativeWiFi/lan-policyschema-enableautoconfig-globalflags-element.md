---
Description: Specifies whether machines use the built-in automatic configuration service to manage connections to wired networks that require layer 2 authentication (such as 802.1X).
ms.assetid: c7a0f6bc-4d42-4d95-8483-2c480f4d8db9
title: enableAutoConfig (globalFlags) Element
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# enableAutoConfig (globalFlags) Element

The **enableAutoConfig** (globalFlags) element specifies whether machines use the built-in automatic configuration service to manage connections to wired networks that require layer 2 authentication (such as 802.1X).

When **enableAutoConfig** has a value of FALSE, machines must not use built-in automatic configuration service to manage connections that require layer 2 authentication. Instead, the network specified in the [**profileList**](lan-policyschema-profilelist-lanpolicy-element.md) element is the only network available for connection. The automatic configuration service will only respond to requests to enable the service.

When **enableAutoConfig** has a value of TRUE, machines may use the built-in automatic configuration service to connect to wired networks that require layer 2 authentication.

``` syntax
<xs:element name="enableAutoConfig"
    type="boolean"
 />
```

The **enableAutoConfig** element is defined by the [**globalFlags**](lan-policyschema-globalflags-lanpolicy-element.md) element.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**globalFlags**](lan-policyschema-globalflags-lanpolicy-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**globalFlags (LANPolicy)**](lan-policyschema-globalflags-lanpolicy-element.md)
</dt> </dl>

 

 




