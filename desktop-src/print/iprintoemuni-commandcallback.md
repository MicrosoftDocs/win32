---
Description: The IPrintOemUni::CommandCallback method is used to provide dynamically generated printer commands for Unidrv-supported printers.
ms.assetid: e1708017-a546-4770-8ad1-7052b3d4e264
title: IPrintOemUni::CommandCallback method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUni::CommandCallback method

The `IPrintOemUni::CommandCallback` method is used to provide dynamically generated printer commands for Unidrv-supported printers.

## Syntax


```C++
HRESULT CommandCallback(
        PDEVOBJ pdevobj,
        DWORD   dwCallbackID,
        DWORD   dwCount,
        PDWORD  pdwParams,
  [out] INT     *piResult
);
```



## Parameters

<dl> <dt>

*pdevobj* 
</dt> <dd>

Caller-supplied pointer to a [**DEVOBJ**](devobj.md) structure.

</dd> <dt>

*dwCallbackID* 
</dt> <dd>

Caller-supplied value representing the printer command's \***CallbackID** attribute in the printer's [*GPD*](https://msdn.microsoft.com/f67c673d-c6f0-49f0-850a-d8b00e99ddd4) file. (For more information, see the following Remarks section.)

</dd> <dt>

*dwCount* 
</dt> <dd>

Caller-supplied value representing the number of elements in the array pointed to by *pdwParams*. Can be 0.

</dd> <dt>

*pdwParams* 
</dt> <dd>

Caller-supplied pointer to an array of DWORD-sized parameters containing values specified by the printer commands \***Params** attribute in the printer's GPD file. (For more information, see the following Remarks section.) Can be **NULL**.

</dd> <dt>

*piResult* \[out\]
</dt> <dd>

Receives a method-supplied result value. See the following Remarks section.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed<br/>           |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

The `IPrintOemUni::CommandCallback` method is used by rendering plug-ins to dynamically generate printer commands, for printers that are supported by [*Unidrv*](https://msdn.microsoft.com/0a51fa2b-3d09-4a5f-9fff-40604877a414).

If you want to dynamically generate a printer command, you must include a \***CallbackID** attribute and, optionally, a \***Params** attribute, within the command's \*Command entry in the printer's GPD file. For more information see [Dynamically Generated Printer Commands](https://www.bing.com/search?q=Dynamically+Generated+Printer+Commands).

When Unidrv calls the `IPrintOemUni::CommandCallback` method, it supplies the \*Command entry's \***CallbackID** attribute value as the *dwCallbackID* parameter. It also places the \*Command entry's \***Params** attribute value inside a DWORD array and supplies the array's address as the *pParams* parameter. The array contains set of Unidrv-defined [standard variables](https://www.bing.com/search?q=standard+variables) values, and the *dwCount* parameter specifies the number of parameters contained in the array. For more information about the attributes see [Command Attributes](https://www.bing.com/search?q=Command+Attributes).

The method should use the *dwCallbackID* parameter value to determine which command to process. For each supported command, the method must be aware of which, if any, standard variables have been specified by the \*Command entry's \***Params** attribute, and in which order.

The method is responsible for constructing a printer command, and then sending the command to the print spooler by calling the [**IPrintOemDriverUni::DrvWriteSpoolBuf**](iprintoemdriveruni-drvwritespoolbuf.md) method.

The value supplied for *piResult* should always return zero unless the method is processing a cursor command. For [cursor commands](https://www.bing.com/search?q=cursor+commands) that move the cursor in either the *x* or direction, the method should return the new cursor position.

The `IPrintOemUni::CommandCallback` method is optional. If a rendering plug-in implements this method, the plug-in's [**IPrintOemUni::GetImplementedMethod**](iprintoemuni-getimplementedmethod.md) method must return S\_OK when it receives "CommandCallback" as input.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni::CommandCallback%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




