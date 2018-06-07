---
Description: Specifies a trace provider (ETW or WPP) for MFTrace.
ms.assetid: 4A3A96FB-A7C5-40BB-AB8F-12A7F00FDCD1
title: provider element
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# provider element

Specifies a trace provider (ETW or WPP) for [MFTrace](mftrace.md).

## Usage

``` syntax
<provider
  ID = "CDATA"
  level = "CDATA">
  child elements
</provider>
```

## Attributes



| Attribute            | Type             | Required       | Description                                              |
|----------------------|------------------|----------------|----------------------------------------------------------|
| **ID**<br/>    | CDATA<br/> | Yes<br/> | The name or GUID of the provider.<br/> <br/> |
| **level**<br/> | CDATA<br/> | Yes<br/> | The trace level.<br/> <br/>                  |



## Child elements



| Element                               |
|---------------------------------------|
| [**keyword**](keyword.md)<br/> |



### Child element sequence

``` syntax
keyword+
```

## Parent elements



| Element                                   |
|-------------------------------------------|
| [**providers**](providers.md)<br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[MFTrace Configuration File](mftrace-configuration-file.md)
</dt> </dl>

 

 




