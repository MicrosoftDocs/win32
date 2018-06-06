---
Description: The IPrintOemPS::DevMode method, provided by rendering plug-ins for Pscript5, performs operations on private DEVMODEW members.
ms.assetid: 72775113-435c-44cf-83e7-9aa62f7f252e
title: IPrintOemPS::DevMode method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemPS::DevMode method

The `IPrintOemPS::DevMode` method, provided by rendering plug-ins for Pscript5, performs operations on private [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) members.

## Syntax


```C++
STDMETHOD DevMode(
   DWORD       dwMode,
   POEMDMPARAM pOemDMParam
);
```



## Parameters

<dl> <dt>

*dwMode* 
</dt> <dd>

Caller-supplied constant. See the following Remarks section.

</dd> <dt>

*pOemDMParam* 
</dt> <dd>

Caller-supplied pointer to an [**OEMDMPARAM**](oemdmparam.md) structure.

</dd> </dl>

## Return value

This method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed<br/>           |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

If you are providing a user interface plug-in for Pscript5, and if you are adding private members to the driver's DEVMODEW structure, you must implement both the `IPrintOemUI::DevMode` and the `IPrintOemPS::DevMode` methods. The code implementing these methods must be identical and can be placed in a library that is statically linked to both the UI plug-in and the rendering plug-in.

For a description of the `IPrintOemPS::DevMode` method, see [**IPrintOemUI::DevMode**](iprintoemui-devmode.md).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemPS::DevMode%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




