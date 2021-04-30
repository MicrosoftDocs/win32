---
title: ItsPubPlugin pluginName property
description: Retrieves the name of the plug-in.
ms.assetid: c1ea46b6-fac6-4140-a278-cb04ee9af739
ms.tgt_platform: multiple
keywords:
- pluginName property Remote Desktop Services
- pluginName property Remote Desktop Services , ItsPubPlugin interface
- ItsPubPlugin interface Remote Desktop Services , pluginName property
topic_type:
- apiref
api_name:
- ItsPubPlugin.pluginName
- ItsPubPlugin.get_pluginName
api_location:
- Cpubplugin.idl
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ItsPubPlugin::pluginName property

Retrieves the name of the plug-in.

This property is read-only.

## Syntax


```C++
HRESULT get_pluginName(
  [out, retval] BSTR *pVal
);
```



## Property value

A pointer to a **BSTR** variable to receive the name of the plug-in.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                         |
| IDL<br/>                      | <dl> <dt>Cpubplugin.idl</dt> </dl> |



## See also

<dl> <dt>

[**ItsPubPlugin**](/windows/desktop/api/tspubplugincom/nn-tspubplugincom-itspubplugin)
</dt> </dl>

 

 





