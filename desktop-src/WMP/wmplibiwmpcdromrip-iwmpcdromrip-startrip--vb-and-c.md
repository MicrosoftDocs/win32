---
title: IWMPCdromRip startRip method
description: The startRip method rips the CD.
ms.assetid: 3569e29c-e593-4bdd-8afb-74e39721cf80
keywords:
- startRip method Windows Media Player
- startRip method Windows Media Player , IWMPCdromRip interface
- IWMPCdromRip interface Windows Media Player , startRip method
topic_type:
- apiref
api_name:
- IWMPCdromRip.startRip
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPCdromRip::startRip method

The **startRip** method rips the CD.

## Syntax


```CSharp
public void startRip();
```


```VB

Public Sub startRip()
Implements IWMPCdromRip.startRip
```





## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Ripping a CD by using the **IWMPCdromRip** interface has the same effect as ripping music by using the Windows Media Player user interface. Ripped content is automatically added to the library according to the user's preferences. For more information about user preferences for CD ripping, see "Ripping music from CDs" in Windows Media Player Help.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPCdromRip Interface (VB and C#)**](iwmpcdromrip--vb-and-c.md)
</dt> <dt>

[**IWMPCdromRip.stopRip**](wmplibiwmpcdromrip-iwmpcdromrip-stoprip--vb-and-c.md)
</dt> <dt>

[**Ripping a CD**](ripping-a-cd.md)
</dt> </dl>

 

 





